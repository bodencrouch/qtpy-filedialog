"""Stubs for optional KotOR-specific imports (TPC icons etc.)."""
from __future__ import annotations

class _Missing:
    def __getattr__(self, name):
        raise ImportError(
            f"Optional KotOR feature '{name}' is not available in qtpy-filedialog standalone. "
            "Install pykotor extras or provide a plugin."
        )

# Absorb "from qtpy_filedialog._optional_pykotor import tools" style leftovers
tools = _Missing()
resource = _Missing()
