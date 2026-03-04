from config import ENTRIES_DIR
from datetime import datetime

def save_entry(content: str):
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    filename = now.strftime("%Y-%m-%d") + ".md"
    
    entry_dir = ENTRIES_DIR / year / month
    entry_dir.mkdir(parents=True, exist_ok=True)

    file_path = entry_dir / filename

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return file_path
