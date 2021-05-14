echo "MacOS Version Info According to Python:"
python -c "import platform; print(platform.mac_ver())"
echo "Xcode version:"
xcodebuild -version
export gampath="dist/gamadv-xtd3"
rm -rf $gampath
if [ "$PLATFORM" == "x86_64" ]; then
    export specfile="gam.spec"
else
    export specfile="gam-universal2.spec"
fi
$python -OO -m PyInstaller --clean --noupx --strip -F --distpath "${gampath}" "${specfile}"
export gam="${gampath}/gam"
$gam version extended
export GAMVERSION=`$gam version simple | head -n 1 | cut -c1-7`
cp license.rtf $gampath/
cp Gam*.txt $gampath/
cp LICENSE $gampath/
cp cacerts.pem $gampath/
GAM_ARCHIVE="gamadv-xtd3-${GAMVERSION}-${GAMOS}-${PLATFORM}.tar"
# tar will cd to dist/ and tar up gam/
tar -C dist/ --create --file $GAM_ARCHIVE gamadv-xtd3
