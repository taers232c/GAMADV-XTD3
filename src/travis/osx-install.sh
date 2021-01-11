cd src
echo "MacOS Version Info According to Python:"
python -c "import platform; print(platform.mac_ver())"
export gampath="dist/gamadv-xtd3"
rm -rf $gampath
mkdir -p $gampath
$python -OO -m PyInstaller --clean --noupx --strip -F --distpath $gampath gam.spec
export gam="$gampath/gam"
export GAMVERSION=`$gam version simple | head -n 1 | cut -c1-7`
cp LICENSE $gampath/
cp license.rtf $gampath/
cp Gam*.txt $gampath/
cp cacerts.pem $gampath/
MACOSVERSION=$(defaults read loginwindow SystemVersionStampAsString | cut -c1-5)
GAM_ARCHIVE=gamadv-xtd3-$GAMVERSION-$GAMOS-$MACOSVERSION-$PLATFORM.tar
echo "GAM Archive:" $GAM_ARCHIVE
# tar will cd to dist/ and tar up gam/
tar -C dist/ --create --file $GAM_ARCHIVE gamadv-xtd3
echo "PyInstaller GAM info:"
$gam version extended
if [[ "$MACOSVERSION" == "11.1" ]]; then
  cp -p gamadv-xtd3-$GAMVERSION-$GAMOS-$MACOSVERSION-$PLATFORM.tar gamadv-xtd3-$GAMVERSION-$GAMOS-11.0-$PLATFORM.tar
fi
echo "GAM packages:"
ls -l gamadv-xtd3-*.tar
