from fastapi import HTTPException, status, APIRouter
from journal.db.schemas import StatsResponse
from journal.services.stats_service import StatsService

router = APIRouter()

@router.get(
    "",
    response_model=StatsResponse,
    status_code=status.HTTP_200_OK,
    summary="Get stats overview",)
def get_stats_overview():
    service = StatsService()
    return service.get_overview()