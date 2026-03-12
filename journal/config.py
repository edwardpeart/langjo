from pathlib import Path
import os

ENTRIES_DIR = Path("./data/entries")
VOCAB_FILE = Path("./data/vocab/vocab.json")
DEMO_MODE = os.getenv("LANGJO_DEMO") == "1"
