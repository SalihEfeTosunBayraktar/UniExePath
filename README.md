# Exe Launcher Builder

A Windows desktop tool that creates **portable shortcut executables** (`.exe`) for any target application. Unlike regular Windows shortcuts (`.lnk`), these launchers search for the target EXE **by name** — so they keep working even if the folder is moved to another drive or computer. Perfect for portable game collections!

> **⚠️ Note:** If multiple EXE files with the same name exist in subdirectories, the launcher will start whichever one it finds first. Make sure the target EXE name is unique within the folder tree.

## Features

- **Auto-detect from EXE** — Pull the icon and name directly from an existing `.exe` file
- **Custom icon support** — Select any image (PNG, JPG, BMP, WebP) and it gets converted to a multi-resolution HD `.ico`
- **English / Turkish UI** — Switch languages on the fly via the dropdown
- **Zero dependencies at runtime** — The generated launcher is a standalone `.exe` compiled with the built-in .NET C# compiler

## Requirements

- **Windows** with .NET Framework 4.x (ships with Windows 10/11)
- **Python 3.10+**

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python builder.py
```

1. Enter the **output launcher name** (e.g. `MyGame_Launch.exe`)
2. Enter the **target EXE name** being searched for (e.g. `game.exe`)
3. Optionally select or pull an icon
4. Click **Build!**

The generated `.exe` will recursively search its directory tree for the target and launch it.

## Project Structure

```text
builder.py        # Entry point
gui.py            # Tkinter application window
compiler.py       # C# template and compilation logic
icon_utils.py     # Icon extraction, conversion, enhancement
localization.py   # English / Turkish UI strings
rcedit-x64.exe    # Icon injection tool (bundled)
```

## Acknowledgments

This project uses the following open-source libraries and tools:

| Dependency | Description | License |
| --- | --- | --- |
| [Pillow](https://github.com/python-pillow/Pillow) | Python Imaging Library for icon conversion and enhancement | HPND |
| [icoextract](https://github.com/jlu5/icoextract) | Extract icons from Windows PE (.exe) files | MIT |
| [pefile](https://github.com/erocarrera/pefile) | Parse and work with Portable Executable files | MIT |
| [rcedit](https://github.com/electron/rcedit) | Command-line tool to edit resources of Windows EXEs (bundled) | MIT |

## License

MIT
