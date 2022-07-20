# -*- mode: python -*-

import sys

from PyInstaller.utils.hooks import copy_metadata

sys.modules['FixTk'] = None

extra_files = [
    ('cacerts.pem', '.'),
    ('admin-directory_v1.1beta1.json', '.'),
    ('cbcm-v1.1beta1.json', '.'),
    ('contactdelegation-v1.json', '.'),
    ('datastudio-v1.json', '.'),
    ]
extra_files += copy_metadata('google-api-python-client')

a = Analysis(['gam/__main__.py'],
             pathex=['./gam'],
             hookspath=None,
             excludes=['FixTk', 'tcl', 'tk', '_tkinter', 'tkinter', 'Tkinter'],
             datas=extra_files,
             runtime_hooks=None)

for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

# use strip on all non-Windows platforms
strip = not sys.platform == 'win32'

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='gam',
          debug=False,
          strip=strip,
          upx=False,
          console=True )
