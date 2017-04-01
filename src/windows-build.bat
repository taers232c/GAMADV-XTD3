rmdir /q /s gam
rmdir /q /s gam-64
rmdir /q /s build
rmdir /q /s dist
del /q /f gamadv-x3-%1-windows.zip
del /q /f gamadv-x3-%1-windows-x64.zip
del /q /f gamadv-x3-%1-windows-x64.msi
del /q /f *.wixobj
del /q /f *.wixpdb

c:\python27-32\scripts\pyinstaller --clean -F --distpath=gam windows-gam.spec
xcopy LICENSE gam\
xcopy license.rtf gam\
xcopy whatsnew.txt gam\
xcopy gam-setup.bat gam\
xcopy Gam*.txt gam\
del gam\w9xpopen.exe
"%ProgramFiles%\7-Zip\7z.exe" a -tzip gamadv-x3-%1-windows.zip gam\ -xr!.svn

c:\python27-64\scripts\pyinstaller --clean -F --distpath=gam-64 windows-gam.spec
xcopy LICENSE gam-64\
xcopy license.rtf gam-64\
xcopy whatsnew.txt gam-64\
xcopy gam-setup.bat gam-64\
xcopy Gam*.txt gam-64\
"%ProgramFiles%\7-Zip\7z.exe" a -tzip gamadv-x3-%1-windows-x64.zip gam-64\ -xr!.svn

set GAMVERSION=%1
"%ProgramFiles(x86)%\WiX Toolset v3.10\bin\candle.exe" -arch x64 gam.wxs
"%ProgramFiles(x86)%\WiX Toolset v3.10\bin\light.exe" -ext "%ProgramFiles(x86)%\WiX Toolset v3.10\bin\WixUIExtension.dll" gam.wixobj -o gamadv-x3-%1-windows-x64.msi
del /q /f gamadv-x3-%1-windows-x64.wixpdb
