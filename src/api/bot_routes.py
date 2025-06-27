from fastapi import APIRouter, HTTPException
from src.bots.manager import launch_bot, stop_bot, get_bot_status, list_bots

router = APIRouter(
    prefix="/bots",
    tags=["bots"],
)

@router.get("/", summary="List all available bots")
def api_list_bots() -> dict:
    """
    List all available trading bots.
    """
    bots = list_bots()
    return {"bots": bots}

@router.post("/start/{bot_name}", summary="Start a bot by name")
def api_start_bot(bot_name: str) -> dict:
    """
    Start a trading bot by name.
    """
    if launch_bot(bot_name):
        return {"status": "started", "bot": bot_name}
    raise HTTPException(status_code=404, detail=f"Bot '{bot_name}' not found or failed to start.")

@router.post("/stop/{bot_name}", summary="Stop a bot by name")
def api_stop_bot(bot_name: str) -> dict:
    """
    Stop a trading bot by name.
    """
    if stop_bot(bot_name):
        return {"status": "stopped", "bot": bot_name}
    raise HTTPException(status_code=404, detail=f"Bot '{bot_name}' not found or failed to stop.")

@router.get("/status/{bot_name}", summary="Get status of a bot by name")
def api_bot_status(bot_name: str) -> dict:
    """
    Get the status of a trading bot by name.
    """
    status = get_bot_status(bot_name)
    if status is not None:
        return {"bot": bot_name, "status": status}
    raise HTTPException(status_code=404, detail=f"Bot '{bot_name}' not found or failed to get status.")
