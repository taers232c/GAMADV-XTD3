# -*- mode: python -*-
ssl_json_files = [
    ('cacerts.pem', '.'),
    ('cros-aue-dates.json', '.'),
    ('cloudprint-v2.json', '.'),
    ('contacts-v3.json', '.'),
    ('email-audit-v1.json', '.'),
    ('email-settings-v2.json', '.'),
    ('sites-v1.json', '.')
    ]
a = Analysis(['gam.py'],
             hiddenimports=['appdirs', 'six', 'packaging', 'packaging.version', 'packaging.specifiers', 'packaging.requirements'],
             datas=ssl_json_files,
             hookspath=None,
             excludes=['_tkinter'],
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
