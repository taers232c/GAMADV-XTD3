# -*- mode: python -*-
import sys

sys.modules['FixTk'] = None

ssl_json_files = [
    ('cacerts.pem', '.'),
    ('cros-aue-dates.json', '.'),
    ('cloudprint-v2.json', '.'),
    ('contacts-v3.json', '.'),
    ('email-audit-v1.json', '.'),
    ('sites-v1.json', '.')
    ]
a = Analysis(['gam.py'],
             hiddenimports=['appdirs', 'six', 'packaging', 'packaging.version', 'packaging.specifiers', 'packaging.requirements'],
             datas=ssl_json_files,
             hookspath=None,
             excludes=['FixTk', 'tcl', 'tk', '_tkinter', 'tkinter', 'Tkinter'],
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
