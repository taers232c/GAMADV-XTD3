cd src
export gampath="gamadv-xtd3"
echo "MacOS Version Info According to Python:"
python -c "import platform; print(platform.mac_ver())"
$python -OO -m PyInstaller --clean --noupx --strip -F --distpath=$gampath $GAMOS-gam.spec
export gam="$gampath/gam"
export GAMVERSION=`$gam version simple | head -n 1 | cut -c1-7`
cp LICENSE $gampath/
cp license.rtf $gampath/
cp Gam*.txt $gampath/
cp cacerts.pem $gampath/
MACOSVERSION=$(defaults read loginwindow SystemVersionStampAsString | cut -c1-5)
GAM_ARCHIVE=$gampath-$GAMVERSION-$GAMOS-$MACOSVERSION-$PLATFORM.tar
echo "GAM Archive:" $GAM_ARCHIVE
tar cf $GAM_ARCHIVE $gampath/
