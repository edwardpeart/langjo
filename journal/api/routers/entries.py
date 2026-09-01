from fastapi import HTTPException, status, Depends, APIRouter
from journal.db.schemas import EntryRead, EntryCreate, EntryUpdate
from journal.services.journal_service import JournalService

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
    response_model=EntryCreate,
    status_code=status.HTTP_200_OK,
    summary="Save new entry",)
def create_entry(body: str):
    service = JournalService()
    new_entry = service.save(body)
    if not body:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Entry cannot be empty",
        )
    return new_entry

@router.put(
    "",
    response_model=EntryUpdate,
    status_code=status.HTTP_200_OK,
    summary="Update existing entry",)
def update_entry(body: str):
    service = JournalService()
    entry_update = service.update(body)
    if not body:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Entry cannot be empty",
        )
    return update_entry
    