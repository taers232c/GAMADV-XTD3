# -*- mode: python -*-

import sys

from PyInstaller.utils.hooks import copy_metadata

from gam.gamlib.glverlibs import GAM_VER_LIBS

sys.modules['FixTk'] = None

extra_files = []
for pkg in GAM_VER_LIBS:
    extra_files += copy_metadata(pkg, recursive=True)
extra_files += [('admin-directory_v1.1beta1.json', '.')]
extra_files += [('cbcm-v1.1beta1.json', '.')]
extra_files += [('contactdelegation-v1.json', '.')]
extra_files += [('datastudio-v1.json', '.')]
extra_files += [('cacerts.pem', '.')]
hidden_imports = [
     'gam.gamlib.yubikey',
     ]
a = Analysis(
    ['gam/__main__.py'],
    pathex=['./gam'],
    binaries=[],
    datas=extra_files,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
    )
for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break
pyz = PYZ(a.pure,
          a.zipped_data,
          cipher=None)
# use strip on all non-Windows platforms
target_arch = 'arm64'
strip = not sys.platform == 'win32'

name = 'gam'
debug = False
bootloader_ignore_signals = False
upx = False
console = True
disable_windowed_traceback = False
argv_emulation = False
codesign_identity = None
entitlements_file = None

exe = EXE(
          pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name=name,
          debug=debug,
          bootloader_ignore_signals=bootloader_ignore_signals,
          strip=strip,
          upx=upx,
          console=console,
          disable_windowed_traceback=disable_windowed_traceback,
          argv_emulation=argv_emulation,
          target_arch=target_arch,
          codesign_identity=codesign_identity,
          entitlements_file=entitlements_file,
          )
