from fastapi import HTTPException, status, APIRouter
from backend.app.db.schemas import EntryRead, EntryCreateResponse, EntryUpdate
from backend.app.services.journal_service import JournalService
from backend.app.services.parsing.japanese_parser import JapaneseParser

router = APIRouter()

@router.get(
        "",
        response_model=list[EntryRead],
        status_code=status.HTTP_200_OK,
        summary="Get all entries",)
def get_all_entries():
    service = JournalService()
    entries = service.get_all_entries()
    if not entries:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No entries found",
        )
    return entries

@router.get(
        "{entry_id}",
        response_model=EntryRead,
        status_code=status.HTTP_200_OK,
        summary="Get an entry by ID",)
def get_entry(entry_id: int):
    service = JournalService()
    entry = service.get_entry(entry_id)
    if not entry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Entry with ID {entry_id} not found",
        )
    return entry

@router.post(
    "",
    response_model=EntryCreateResponse,
    status_code=status.HTTP_200_OK,
    summary="Save new entry",
)
def create_entry(body: str):
    if not body.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Entry cannot be empty",
        )

    service = JournalService()
    return service.save_entry(None, body)

@router.put(
    "{entry_id}",
    response_model=EntryUpdate,
    status_code=status.HTTP_200_OK,
    summary="Update existing entry",)
def update_entry(entry_id: int, body: str):
    service = JournalService()
    entry_update = service.save_entry(entry_id, body)
    if not body:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Entry cannot be empty",
        )
    return entry_update
    