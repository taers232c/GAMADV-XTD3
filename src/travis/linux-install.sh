cd src
export gampath="dist/gamadv-xtd3"
rm -rf $gampath
mkdir -p $gampath
export gampath=$(readlink -e $gampath)
$python -OO -m PyInstaller --clean --distpath $gampath gam.spec
export gam="${gampath}/gam"
export GAMVERSION=`$gam version simple | head -n 1 | cut -c1-7`
cp LICENSE $gampath/
cp license.rtf $gampath/
cp Gam*.txt $gampath/
cp cacerts.pem $gampath/
this_glibc_ver=$(ldd --version | awk '/ldd/{print $NF}')
GAM_ARCHIVE=gamadv-xtd3-$GAMVERSION-$GAMOS-$PLATFORM-glibc$this_glibc_ver.tar.xz
echo "GAM Archive:" $GAM_ARCHIVE
# tar will cd to dist and tar up gam/
tar -C dist/ --create --file $GAM_ARCHIVE --xz gamadv-xtd3
echo "PyInstaller GAM info:"
$gam version extended
echo "GAM packages:"
ls -l gamadv-xtd3-*.tar.xz
