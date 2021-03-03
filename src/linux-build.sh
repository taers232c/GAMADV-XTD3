rm -rf gamadv-xtd3
rm -rf build
rm -rf dist

export gampath="dist/gamadv-xtd3"
rm -rf $gampath
mkdir -p $gampath
pyinstaller --clean --noupx --strip -F --distpath=$gampath gam.spec
export gam="$gampath/gam"
$gam version extended
export GAMVERSION=`$gam version simple | head -n 1 | cut -c1-7`
cp LICENSE $gampath/
cp license.rtf $gampath/
cp Gam*.txt $gampath/
cp cacerts.pem $gampath/
arch=$(uname -m)
this_glibc_ver=$(ldd --version | awk '/ldd/{print $NF}')
GAM_ARCHIVE=gamadv-xtd3-$GAMVERSION-linux-$arch-glibc$this_glibc_ver.tar.xz
rm -f $GAM_ARCHIVE
tar -C dist/ --create --xz --file $GAM_ARCHIVE gamadv-xtd3
