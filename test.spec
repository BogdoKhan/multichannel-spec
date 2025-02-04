# -*- mode: python ; coding: utf-8 -*-

import sys
sys.path.append("./")

block_cipher = None

a = Analysis(['test.py'],
             pathex=['./',
             'transport/',
			 'filters/'],
             binaries=[],
             datas=[],
             hiddenimports=["mainwin", "pyvisa", "oscilloscope",
			 "pyqt_instruments", "spectrometer", "widgets",
			 "devices"],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False
             )

pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher
          )

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='test_spec_'+'b.0.1.14',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False
          )
