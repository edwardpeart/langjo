from fastapi import HTTPException, status, APIRouter
from journal.db.schemas import VocabCreate, VocabRead
from journal.services.vocab_service import VocabService

router = APIRouter()

@router.get(
    "",
    response_model=list[VocabRead],
    status_code=status.HTTP_200_OK,
    summary="Get all vocab",)
def get_all_vocab():
    service = VocabService()
    vocab = service.get_vocab()
    if not vocab:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No vocab found",
        )
    return vocab

@router.get(
    "{vocab_id}",
    response_model=VocabRead,
    status_code=status.HTTP_200_OK,
    summary="Get vocab by ID",)
def get_vocab(vocab_id: int):
    service = VocabService()
    vocab = service.get_vocab_by_id(vocab_id)
    if not vocab:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vocab with ID {vocab_id} not found",
        )
    return vocab

@router.get(
    "entry/{entry_id}",
    response_model=list[VocabRead],
    status_code=status.HTTP_200_OK,
    summary="Get vocab by entry ID",)
def get_vocab_by_entry(entry_id: int):
    service = VocabService()
    vocab = service.get_vocab_by_entry_id(entry_id)
    if not vocab:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No vocab found for entry ID {entry_id}",
        )
    return vocab