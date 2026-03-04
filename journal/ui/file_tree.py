from textual.widgets import DirectoryTree
from pathlib import Path
from typing import Iterable

class FileTreePanel(DirectoryTree):
    """Left panel placeholder for file tree."""
    BORDER_TITLE = "Entries"
    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        return [path for path in paths if not path.name.startswith(".")]
