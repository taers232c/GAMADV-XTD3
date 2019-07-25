cd src
$python -OO -m PyInstaller --clean --noupx --strip -F --distpath=gam $GAMOS-gam.spec
export gam="gam/gam"
export gampath=gam
$gam version extended
export GAMVERSION=`gam/gam version simple`
cp LICENSE gam
cp license.rtf gam
cp Gam*.txt gam
cp cacerts.pem gam
GAM_ARCHIVE=gam-$GAMVERSION-$GAMOS-$PLATFORM.tar
rm gam/lastupdatecheck.txt
tar cf $GAM_ARCHIVE gam/
