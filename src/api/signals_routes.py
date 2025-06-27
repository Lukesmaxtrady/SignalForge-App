from fastapi import APIRouter, Query, HTTPException
from ..bots.registry import get_signals, get_signal_by_id

router = APIRouter(prefix="/signals", tags=["signals"])

@router.get("/", summary="List all available signals (bots)")
def fetch_signals(
    symbol: str = Query(None, description="Optionally filter by trading symbol"),
    mode: str = Query(None, description="Optionally filter by mode (future use)")
):
    """
    List all registered signal bots.
    `symbol` and `mode` are placeholders for future filtering.
    """
    try:
        # If your get_signals supports args, pass them; otherwise ignore.
        # Here we assume simple get_signals(), update if needed.
        signals = get_signals()
        return {"signals": signals}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch signals: {e}")

@router.get("/{signal_id}", summary="Get info for a specific signal bot")
def fetch_signal(signal_id: str):
    """
    Get a signal bot by its id (name).
    """
    signal = get_signal_by_id(signal_id)
    if not signal:
        raise HTTPException(status_code=404, detail=f"Signal '{signal_id}' not found")
    return signal