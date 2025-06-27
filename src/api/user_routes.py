from fastapi import APIRouter, Depends
from ..db.db_manager import get_user, create_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
def register_user(user_data: dict):
    return create_user(user_data)

@router.get("/{user_id}")
def fetch_user(user_id: str):
    return get_user(user_id)
