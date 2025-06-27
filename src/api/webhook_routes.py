from fastapi import APIRouter, Request

router = APIRouter(prefix="/webhook", tags=["webhook"])

@router.post("/external-signal")
async def external_signal(request: Request):
    payload = await request.json()
    # Process and dispatch to appropriate bot
    return {"status": "received", "payload": payload}
