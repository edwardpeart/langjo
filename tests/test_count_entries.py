from journal.repository.file_repository import FileRepository
from config import ENTRIES_DIR

repo = FileRepository()

print(repo.count())

files = list(ENTRIES_DIR.glob("**/*.md")) # Using **/*.md to catch nested files
for f in files:
    print(f.name)
print(f"Total: {len(files)}")