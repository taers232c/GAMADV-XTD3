cd src
echo "MacOS Version Info According to Python:"
python -c "import platform; print(platform.mac_ver()[0])"
echo "Xcode versionn:"
xcodebuild -version
export gampath="dist/gamadv-xtd3"
rm -rf $gampath
mkdir -p $gampath
$python -OO -m PyInstaller --clean -F --distpath $gampath gam.spec
export gam="$gampath/gam"
$gam version extended
export GAMVERSION=`$gam version simple | head -n 1 | cut -c1-7`
cp license.rtf $gampath/
cp Gam*.txt $gampath/
cp LICENSE $gampath/
cp cacerts.pem $gampath/
GAM_ARCHIVE=gamadv-xtd3-$GAMVERSION-$GAMOS-$PLATFORM.tar
echo "GAM Archive:" $GAM_ARCHIVE
# tar will cd to dist/ and tar up gam/
tar -C dist/ --create --file $GAM_ARCHIVE gamadv-xtd3
