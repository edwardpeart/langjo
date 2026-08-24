from textual.widgets import Tree
from sqlalchemy.orm import Session

from ..db.database import SessionLocal
from ..db.repositories.entry_repo import EntryRepository


class EntryTreePanel(Tree):
    """Tree view of journal entries grouped by year, month, and date."""

    BORDER_TITLE = "Entries"

    def __init__(self, *args, **kwargs):
        super().__init__("Journal Entries", *args, **kwargs)
        self.repo = EntryRepository()
        self.root.expand()

    def on_mount(self) -> None:
        self.populate()

    @staticmethod
    def group_entries(entries):
        grouped = {}
        for entry in entries:
            dt = entry.created_at
            year = str(dt.year)
            month = dt.strftime("%B")
            grouped.setdefault(year, {}).setdefault(month, []).append(entry)
        return grouped

    def populate(self):
        self.root.remove_children()
        self.root.label = "Journal Entries"
        self.root.expand()

        db: Session
        with SessionLocal() as db:
            entries = self.repo.get_entries_date_desc(db)

        grouped = self.group_entries(entries)

        for year, months in grouped.items():
            year_node = self.root.add(year)
            year_node.expand()

            for month, month_entries in months.items():
                month_node = year_node.add(month)
                month_node.expand()

                for entry in month_entries:
                    summary = entry.body.strip().replace("\n", " ")
                    if len(summary) > 55:
                        summary = summary[:55] + "..."
                    label = f"{entry.created_at.strftime('%Y-%m-%d')} {summary}"
                    entry_node = month_node.add(label)
                    entry_node.data = entry.id

