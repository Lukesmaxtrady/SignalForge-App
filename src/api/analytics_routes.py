from fastapi import APIRouter
from ..bots.performance import get_performance_summary

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/performance")
def performance(symbol: str = None):
    return get_performance_summary(symbol)
