# -*- mode: python -*-
import sys

sys.modules['FixTk'] = None

extra_files = [
    ('cacerts.pem', '.'),
    ('cloudprint-v2.json', '.'),
    ('contacts-v3.json', '.'),
    ('email-audit-v1.json', '.'),
    ('sites-v1.json', '.')
    ]
a = Analysis(['gam.py'],
             hiddenimports=[],
             hookspath=None,
             excludes=['FixTk', 'tcl', 'tk', '_tkinter', 'tkinter', 'Tkinter'],
             datas=extra_files,
             runtime_hooks=None)

for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break


pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='gam',
          debug=False,
          strip=None,
          upx=False,
          console=True )
