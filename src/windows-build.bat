set GAMPLATFORM=gamadv-xtd3
set GAMVERSION=%1
set WIXVERSION=3.11

rmdir /q /s build
rmdir /q /s dist
del /q /f %GAMPLATFORM%-%GAMVERSION%-windows-x86.zip
del /q /f %GAMPLATFORM%-%GAMVERSION%-windows-x86.msi
del /q /f %GAMPLATFORM%-%GAMVERSION%-windows-x86_64.zip
del /q /f %GAMPLATFORM%-%GAMVERSION%-windows-x86_64.msi

rmdir /q /s %GAMPLATFORM%
c:\python38-32\scripts\pyinstaller --clean --noupx -F --distpath=%GAMPLATFORM% windows-gam.spec
xcopy LICENSE %GAMPLATFORM%\
xcopy license.rtf %GAMPLATFORM%\
xcopy gam-setup.bat %GAMPLATFORM%\
xcopy Gam*.txt %GAMPLATFORM%\
xcopy cacerts.pem %GAMPLATFORM%\
"%ProgramFiles%\7-Zip\7z.exe" a -tzip %GAMPLATFORM%-%GAMVERSION%-windows-x86.zip %GAMPLATFORM%\ -xr!.svn
del /q /f *.wixobj
del /q /f *.wixpdb
"%ProgramFiles(x86)%\WiX Toolset v%WIXVERSION%\bin\candle.exe" -arch x86 gam.wxs
"%ProgramFiles(x86)%\WiX Toolset v%WIXVERSION%\bin\light.exe" -ext "%ProgramFiles(x86)%\WiX Toolset v%WIXVERSION%\bin\WixUIExtension.dll" gam.wixobj -o %GAMPLATFORM%-%GAMVERSION%-windows-x86.msi
del /q /f *.wixpdb

rmdir /q /s %GAMPLATFORM%
c:\python38-64\scripts\pyinstaller --clean --noupx -F --distpath=%GAMPLATFORM% windows-gam.spec
xcopy LICENSE %GAMPLATFORM%\
xcopy license.rtf %GAMPLATFORM%\
xcopy gam-setup.bat %GAMPLATFORM%\
xcopy Gam*.txt %GAMPLATFORM%\
xcopy cacerts.pem %GAMPLATFORM%\
"%ProgramFiles%\7-Zip\7z.exe" a -tzip %GAMPLATFORM%-%GAMVERSION%-windows-x86_64.zip %GAMPLATFORM%\ -xr!.svn
del /q /f *.wixobj
del /q /f *.wixpdb
"%ProgramFiles(x86)%\WiX Toolset v%WIXVERSION%\bin\candle.exe" -arch x64 gam.wxs
"%ProgramFiles(x86)%\WiX Toolset v%WIXVERSION%\bin\light.exe" -ext "%ProgramFiles(x86)%\WiX Toolset v%WIXVERSION%\bin\WixUIExtension.dll" gam.wixobj -o %GAMPLATFORM%-%GAMVERSION%-windows-x86_64.msi
del /q /f *.wixpdb
