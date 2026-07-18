"""Stubs for optional game-format icon imports."""
from __future__ import annotations

class _Missing:
    def __getattr__(self, name):
        raise ImportError(
            f"Optional feature '{name}' is not available in this build. "
            "Provide a plugin if you need this."
        )

# Absorb "from qtpy_filedialog._optional_extras import tools" style leftovers
tools = _Missing()
resource = _Missing()
