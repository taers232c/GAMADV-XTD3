cd src
echo "compiling GAM with pyinstaller..."
export gampath="dist/gamadv-xtd3"
rm -rf $gampath
mkdir -p $gampath
export gampath=$(readlink -e $gampath)
pyinstaller --clean --distpath $gampath gamwin.spec
export gam="${gampath}/gam"
echo "running compiled GAM..."
$gam version
export GAMVERSION=`$gam version simple | head -n 1 | cut -c1-7`
cp LICENSE $gampath/
cp license.rtf $gampath/
cp gam-setup.bat $gampath/
cp Gam*.txt $gampath/
cp cacerts.pem $gampath/
GAM_ARCHIVE=gamadv-xtd3-$GAMVERSION-$GAMOS-$PLATFORM.zip
/c/Program\ Files/7-Zip/7z.exe a -tzip $GAM_ARCHIVE $gampath -xr!.svn

echo "Running WIX candle $WIX_BITS..."
/c/Program\ Files\ \(x86\)/WiX\ Toolset\ v3.11/bin/candle.exe -arch $WIX_BITS gam.wxs
echo "Done with WIX candle..."
echo "Running WIX light..."
/c/Program\ Files\ \(x86\)/WiX\ Toolset\ v3.11/bin/light.exe -ext /c/Program\ Files\ \(x86\)/WiX\ Toolset\ v3.11/bin/WixUIExtension.dll gam.wixobj -o gamadv-xtd3-$GAMVERSION-$GAMOS-$PLATFORM.msi || true;
echo "Done with WIX light..."
rm *.wixpdb
