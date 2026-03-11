
from pathlib import Path
from ..repository.file_repository import FileRepository

class JournalService:
    def __init__(self):
        self.repo = FileRepository()
   
    def save_entry(self, text: str):
        return self.repo.save(text)
    
    def read_entry(self, path: Path):
        return self.repo.read(path)
    
    def count_entries(self):
        return self.repo.count()
