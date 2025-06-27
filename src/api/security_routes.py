from fastapi import APIRouter, HTTPException, status, Depends, Request
from pydantic import BaseModel
import secrets
import logging

router = APIRouter(prefix="/security", tags=["security"])
logger = logging.getLogger("security")

# --- In-memory user/token store for demo purposes ---
fake_users_db = {
    "alice": {"username": "alice", "password": "wonderland", "role": "admin"},
    "bob":   {"username": "bob", "password": "builder",   "role": "trader"},
}
# This would be replaced with a real database and JWTs in production!
active_tokens = {}

# --- Pydantic Schemas ---
class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ApiKeyCreate(BaseModel):
    name: str

# --- Dependency for protected routes ---
def get_current_user(request: Request):
    auth = request.headers.get("Authorization")
    if not auth or not auth.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing bearer token")
    token = auth.split(" ")[1]
    user = active_tokens.get(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user

# --- ROUTES ---

@router.get("/ping", summary="Basic security health check")
def ping():
    return {"status": "secure", "msg": "Security API OK"}

@router.post("/login", response_model=TokenResponse, summary="Login and get a token (fictional, demo only)")
def login(login: LoginRequest):
    user = fake_users_db.get(login.username)
    if not user or secrets.compare_digest(user["password"], login.password) is False:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    # Create a fake token
    token = secrets.token_urlsafe(24)
    active_tokens[token] = user
    logger.info(f"User {user['username']} logged in, token issued.")
    return TokenResponse(access_token=token)

@router.get("/me", summary="Show current user info", tags=["security"])
def get_me(user: dict = Depends(get_current_user)):
    return {"username": user["username"], "role": user["role"]}

@router.get("/admin-check", summary="Check if current user is admin", tags=["security"])
def admin_check(user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    return {"status": "ok", "admin": user["username"]}

# --- Fictional API Key Management ---
fake_api_keys = {}

@router.post("/api-keys", summary="Create an API key (fictional)", tags=["security"])
def create_api_key(req: ApiKeyCreate, user: dict = Depends(get_current_user)):
    key = secrets.token_hex(16)
    fake_api_keys[key] = {"name": req.name, "owner": user["username"]}
    logger.info(f"API key created for {user['username']}: {key}")
    return {"api_key": key, "name": req.name}

@router.get("/api-keys", summary="List my API keys (fictional)", tags=["security"])
def list_api_keys(user: dict = Depends(get_current_user)):
    keys = [ {"api_key": k, "name": v["name"]} for k,v in fake_api_keys.items() if v["owner"] == user["username"] ]
    return {"keys": keys}

@router.delete("/api-keys/{api_key}", summary="Delete an API key (fictional)", tags=["security"])
def delete_api_key(api_key: str, user: dict = Depends(get_current_user)):
    if api_key not in fake_api_keys or fake_api_keys[api_key]["owner"] != user["username"]:
        raise HTTPException(status_code=404, detail="API key not found")
    del fake_api_keys[api_key]
    logger.info(f"API key deleted by {user['username']}: {api_key}")
    return {"status": "deleted"}

