from __future__ import annotations

import runpy
from pathlib import Path


def main() -> None:
    app_path = Path(__file__).resolve().parent / "textual-ui" / "main.py"
    runpy.run_path(str(app_path), run_name="__main__")
