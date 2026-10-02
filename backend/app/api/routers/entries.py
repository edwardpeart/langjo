from datetime import datetime

from fastapi import HTTPException, status, APIRouter
from backend.app.db.schemas import EntryRead, EntryReadResponse, EntryCreateResponse, EntryTreeResponse
from backend.app.services.journal_service import JournalService

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
        response_model=EntryReadResponse,
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
    response_model=EntryCreateResponse,
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


@router.get(
    "tree",
    response_model=EntryTreeResponse,
    status_code=status.HTTP_200_OK,
    summary="Get entries as tree nodes",
)
def get_entry_tree():
    service = JournalService()
    entries = service.get_all_entries()
    if not entries:
        return EntryTreeResponse(__root__=[])

    def to_title(created_at: datetime) -> str:
        return created_at.strftime("%d")
        

    def to_preview(body: str) -> str:
        txt = (body or "").strip()
        return txt[:200] + ("..." if len(txt) > 200 else "")

    # Group entries by year -> month
    tree: dict[str, dict[str, list[dict]]] = {}
    for e in entries:
        year = e.created_at.strftime("%Y")
        month = e.created_at.strftime("%B")
        tree.setdefault(year, {}).setdefault(month, []).append(e)

    root_nodes: list[dict] = []
    for year, months in sorted(tree.items(), reverse=True):
        month_nodes: list[dict] = []
        for month, items in sorted(months.items(), reverse=True):
            entry_nodes = [
                {
                    "id": it.id,
                    "title": to_title(it.created_at),
                    "preview": to_preview(it.body),
                    "slug": None,
                    "created_at": it.created_at,
                    "updated_at": it.updated_at,
                    "has_children": False,
                    "children": None,
                }
                for it in sorted(items, key=lambda x: x.created_at, reverse=True)
            ]

            month_nodes.append(
                {
                    "id": hash(month) & 0xFFFFFFFF,
                    "title": month,
                    "preview": None,
                    "slug": None,
                    "created_at": None,
                    "updated_at": None,
                    "has_children": True,
                    "children": entry_nodes,
                }
            )

        root_nodes.append(
            {
                "id": hash(year) & 0xFFFFFFFF,
                "title": year,
                "preview": None,
                "slug": None,
                "created_at": None,
                "updated_at": None,
                "has_children": True,
                "children": month_nodes,
            }
        )

    return EntryTreeResponse(__root__=root_nodes)
    