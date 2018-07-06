rmdir /q /s gamadv-xtd3
rmdir /q /s gamadv-xtd3-64
rmdir /q /s build
rmdir /q /s dist
del /q /f gamadv-xtd3-%1-windows.zip
del /q /f gamadv-xtd3-%1-windows-x64.zip
del /q /f gamadv-xtd3-%1-windows-x64.msi
del /q /f *.wixobj
del /q /f *.wixpdb

set WIXVERSION=3.11

c:\python36-32\scripts\pyinstaller --clean -F --distpath=gamadv-xtd3 windows-gam.spec
xcopy LICENSE gamadv-xtd3\
xcopy license.rtf gamadv-xtd3\
xcopy whatsnew.txt gamadv-xtd3\
xcopy gam-setup.bat gamadv-xtd3\
xcopy Gam*.txt gamadv-xtd3\
xcopy cacerts.pem gamadv-xtd3\
del gamadv-xtd3\w9xpopen.exe
"%ProgramFiles%\7-Zip\7z.exe" a -tzip gamadv-xtd3-%1-windows.zip gamadv-xtd3\ -xr!.svn

c:\python36-64\scripts\pyinstaller --clean -F --distpath=gamadv-xtd3-64 windows-gam.spec
xcopy LICENSE gamadv-xtd3-64\
xcopy license.rtf gamadv-xtd3-64\
xcopy whatsnew.txt gamadv-xtd3-64\
xcopy gam-setup.bat gamadv-xtd3-64\
xcopy Gam*.txt gamadv-xtd3-64\
xcopy cacerts.pem gamadv-xtd3-64\
"%ProgramFiles%\7-Zip\7z.exe" a -tzip gamadv-xtd3-%1-windows-x64.zip gamadv-xtd3-64\ -xr!.svn

set GAMVERSION=%1
"%ProgramFiles(x86)%\WiX Toolset v%WIXVERSION%\bin\candle.exe" -arch x64 gam.wxs
"%ProgramFiles(x86)%\WiX Toolset v%WIXVERSION%\bin\light.exe" -ext "%ProgramFiles(x86)%\WiX Toolset v%WIXVERSION%\bin\WixUIExtension.dll" gam.wixobj -o gamadv-xtd3-%1-windows-x64.msi
del /q /f gamadv-xtd3-%1-windows-x64.wixpdb
