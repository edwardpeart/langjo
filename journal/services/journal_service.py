from ..db.repositories.entry_repo import EntryRepository

class JournalService():
    def __init__(self):
        self.repo = EntryRepository()

    def save(self, text: str):
        return self.repo.create_entry(text)

    def update(self, text: str):
        return self.repo.update_entry(text)

    def get(self, id: str):
        return self.repo.get_entry(id)