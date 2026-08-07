# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(

    [
        "app/main.py"
    ],

    pathex=[],

    binaries=[],

    datas=[

        (
            "config",
            "config"
        ),

        (
            "resources",
            "resources"
        )

    ],

    hiddenimports=[

        "win32com",

        "win32com.client"

    ],

    cipher=block_cipher

)



pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)



exe = EXE(

    pyz,

    a.scripts,

    a.binaries,

    a.datas,

    [],

    name="AutoCAD_GOST_Tools",

    debug=False,

    strip=False,

    upx=True,

    console=False,

    icon="resources/icon.ico"

)
