export gampath="dist/gamadv-xtd3"
rm -rf $gampath
mkdir -p $gampath
export gampath=$(readlink -e $gampath)
$python -OO -m PyInstaller --clean --noupx --strip -F --distpath $gampath gam.spec
export gam="${gampath}/gam"
export GAMVERSION=`$gam version simple | head -n 1 | cut -c1-7`
cp LICENSE $gampath/
cp license.rtf $gampath/
cp Gam*.txt $gampath/
cp cacerts.pem $gampath/
this_glibc_ver=$(ldd --version | awk '/ldd/{print $NF}')
GAM_ARCHIVE="gamadv-xtd3-${GAMVERSION}-${GAMOS}-${PLATFORM}-glibc${this_glibc_ver}.tar.xz"
echo "GAM Archive:" $GAM_ARCHIVE
# tar will cd to dist and tar up gam/
tar -C dist/ --create --file $GAM_ARCHIVE --xz gamadv-xtd3
echo "PyInstaller GAM info:"
du -h $gam
time $gam version extended
if ([ "${ImageOS}" == "ubuntu16" ]) && [ "${HOSTTYPE}" == "x86_64" ]; then
  GAM_LEGACY_ARCHIVE=gamadv-xtd3-${GAMVERSION}-${GAMOS}-${PLATFORM}-legacy.tar.xz
  $python -OO -m staticx -l /lib/x86_64-linux-gnu/libresolv.so.2 -l /lib/x86_64-linux-gnu/libnss_dns.so.2 $gam $gam-staticx
  strip $gam-staticx
  rm $gampath/gam
  mv $gam-staticx $gam
  chmod 755 $gam
  rm $gampath/lastupdatecheck.txt
  tar -C dist/ --create --file $GAM_LEGACY_ARCHIVE --xz gamadv-xtd3
  echo "Legacy StaticX GAM info:"
  du -h $gam
  time $gam version extended
fi
echo "GAM packages:"
ls -l gamadv-xtd3-*.tar.xz
