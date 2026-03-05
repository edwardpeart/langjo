from config import ENTRIES_DIR
from datetime import datetime
from pathlib import Path

class FileRepository:
    def save(self, text: str) -> Path:
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        filename = now.strftime("%Y-%m-%d") + ".md"
        
        entry_dir = ENTRIES_DIR / year / month
        entry_dir.mkdir(parents=True, exist_ok=True)
        file_path = entry_dir / filename


        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)

        return file_path
    
    def read(self, file_path: Path) -> str:
        if not file_path.is_file():
            raise FileNotFoundError(f"{file_path} does not exist")
        
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()