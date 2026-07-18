"""pathlib Path stand-in for case-aware path helpers."""
from __future__ import annotations
from pathlib import Path

class CaseAwarePath(type(Path())):  # type: ignore[misc]
    """Alias to pathlib.Path for standalone builds."""
    pass

# Prefer plain Path for simplicity on Python 3.8+
CaseAwarePath = Path  # type: ignore[misc, assignment]
