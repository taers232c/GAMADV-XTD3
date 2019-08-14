cd src
export gampath="gamadv-xtd3"
pyinstaller --clean --noupx -F --distpath=$gampath $GAMOS-gam.spec
export gam="$gampath/gam"
$gam version extended
export GAMVERSION=`$gam version simple | head -n 1 | cut -c1-7`
cp LICENSE $gampath/
cp license.rtf $gampath/
cp gam-setup.bat $gampath
cp Gam*.txt $gampath/
cp cacerts.pem $gampath/
GAM_ARCHIVE=$gampath-$GAMVERSION-$GAMOS-$PLATFORM.zip
/c/Program\ Files/7-Zip/7z.exe a -tzip $GAM_ARCHIVE $gampath -xr!.svn
mkdir gam-64
cp -rf $gampath/* gam-64/;
/c/Program\ Files\ \(x86\)/WiX\ Toolset\ v3.11/bin/candle.exe -arch x86 gam.wxs
/c/Program\ Files\ \(x86\)/WiX\ Toolset\ v3.11/bin/light.exe -ext /c/Program\ Files\ \(x86\)/WiX\ Toolset\ v3.11/bin/WixUIExtension.dll gam.wixobj -o $gampath-$GAMVERSION-$GAMOS-$PLATFORM.msi || true;
rm *.wixpdb
