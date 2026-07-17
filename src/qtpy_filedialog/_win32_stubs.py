"""Optional Win32 COM stubs when native dialog helpers are unavailable."""
from __future__ import annotations

S_OK = 0

class GUID:
    def __init__(self, *args, **kwargs):
        pass

class HRESULT(int):
    pass

class SIGDN:
    SIGDN_FILESYSPATH = 0x80058000

class IShellItem:
    pass

class COMDLG_FILTERSPEC:
    pass

class FileDialogControlEvents:
    pass
