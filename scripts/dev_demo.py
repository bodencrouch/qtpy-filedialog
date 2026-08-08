#!/usr/bin/env python3
"""Minimal GUI demo for verifying the qtpy-filedialog development environment."""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

from qtpy.QtCore import Qt
from qtpy.QtGui import QFont
from qtpy.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from qtpy_filedialog.common_filesystem.file_properties_dialog import (
    FileProperties,
    FilePropertiesDialog,
)
from qtpy_filedialog.common_filesystem.filename_validator import FileNameValidator
from qtpy_filedialog.common_filesystem.preview_widget import PreviewWidget


def build_sample_properties(path: Path) -> FileProperties:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    size = path.stat().st_size if path.exists() else 0
    return FileProperties(
        name=path.name or path.as_posix(),
        path=str(path.resolve()),
        type="File" if path.is_file() else "Directory",
        size=f"{size} bytes",
        size_on_disk=f"{size} bytes",
        created=now,
        modified=now,
        accessed=now,
        mime_type="inode/directory" if path.is_dir() else "text/plain",
        owner="dev",
        group="dev",
        permissions="rwxr-xr-x",
        inode=0,
        num_hard_links=1,
        device=0,
        is_symlink=path.is_symlink() if path.exists() else False,
        symlink_target="",
        md5="",
        sha1="",
        sha256="",
        is_hidden=path.name.startswith("."),
        is_system=False,
        is_archive=False,
        is_compressed=False,
        is_encrypted=False,
        is_readonly=False,
        is_temporary=False,
        extension=path.suffix.lstrip("."),
    )


class DevDemoWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("qtpy-filedialog — Dev Environment Demo")
        self.resize(720, 420)

        root = QWidget(self)
        self.setCentralWidget(root)
        layout = QVBoxLayout(root)

        title = QLabel("qtpy-filedialog")
        title.setFont(QFont("DejaVu Sans", 22, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(title)

        subtitle = QLabel(
            "Development environment smoke UI using PreviewWidget, "
            "FileNameValidator, and FilePropertiesDialog."
        )
        subtitle.setWordWrap(True)
        layout.addWidget(subtitle)

        row = QHBoxLayout()
        self.name_edit = QLineEdit("example-file.txt")
        self.name_edit.setValidator(FileNameValidator(self))
        self.name_edit.setPlaceholderText("Filename (validated)")
        row.addWidget(QLabel("Name:"))
        row.addWidget(self.name_edit)
        layout.addLayout(row)

        self.preview = PreviewWidget(self)
        style = QApplication.style()
        if style is not None:
            self.preview.set_icon(style.standardIcon(style.StandardPixmap.SP_DirIcon))
        layout.addWidget(self.preview)

        buttons = QHBoxLayout()
        props_btn = QPushButton("Open File Properties…")
        props_btn.clicked.connect(self.open_properties)
        quit_btn = QPushButton("Quit")
        quit_btn.clicked.connect(self.close)
        buttons.addWidget(props_btn)
        buttons.addStretch()
        buttons.addWidget(quit_btn)
        layout.addLayout(buttons)

        self.statusBar().showMessage("Environment ready — Qt + qtpy-filedialog loaded")

    def open_properties(self) -> None:
        target = Path.cwd() / (self.name_edit.text() or "example-file.txt")
        dialog = FilePropertiesDialog(build_sample_properties(target), self)
        dialog.exec()


def main() -> int:
    app = QApplication(sys.argv)
    window = DevDemoWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
