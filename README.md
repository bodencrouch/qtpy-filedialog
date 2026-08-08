# qtpy-filedialog

File dialog / filesystem explorer stack on top of qtpy. Tries to behave closer to the C++ Qt dialogs than the stock Python wrappers.

Uses plain `pathlib.Path`. Extra file-type icon plugins are optional; without them you just get generic icons.

## Install

```bash
pip install git+https://github.com/bodencrouch/qtpy-filedialog.git
pip install qtpy PyQt5
```

## Development setup

```bash
python3 -m pip install -U pip pytest
python3 -m pip install qtpy PyQt5
python3 -m pip install -e .
QT_QPA_PLATFORM=offscreen python3 -m pytest -q --tb=short tests
```

Optional GUI smoke demo (needs a display or `QT_QPA_PLATFORM=offscreen`):

```bash
python3 scripts/dev_demo.py
```

## License

LGPL-3.0-or-later
