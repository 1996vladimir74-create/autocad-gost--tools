# AutoCAD GOST Tools

Windows utility for creating a GOST-style drawing sheet directly in AutoCAD.

## Current version

The utility asks for:

- drawing number;
- drawing name;
- sheet format A0-A4;
- portrait or landscape orientation.

It then connects to AutoCAD through Windows COM automation and creates:

- the sheet boundary;
- the drawing frame with a 20 mm left binding margin and 5 mm on the other sides;
- a 185 x 55 mm basic title-block envelope;
- the entered drawing number and name.

The end user does **not** need a terminal. The intended distribution format is a single Windows `.exe` produced with PyInstaller.

## Requirements on the work PC

- Windows;
- installed AutoCAD with COM automation available;
- no Python installation is required when using the compiled EXE;
- no terminal is required.

## Build the EXE

On a Windows development PC with Python installed:

```text
build_windows.bat
```

The resulting file is:

```text
dist\\AutoCAD_GOST_Tools.exe
```

Copy that EXE to a USB flash drive or send it to the work PC.

## Standards basis

The project uses the ESKD sheet-format and frame conventions as the starting point. The repository should be reviewed against the exact edition and company standard before production use, especially the complete title-block field geometry and text formatting.

Relevant standards include ГОСТ 2.301 and ГОСТ 2.104; current drawing requirements also reference ГОСТ Р 2.109-2023.
