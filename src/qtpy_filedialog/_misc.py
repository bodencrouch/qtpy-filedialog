from __future__ import annotations
from pathlib import Path

def ensure_directory_exists(path):
    Path(path).mkdir(parents=True, exist_ok=True)
