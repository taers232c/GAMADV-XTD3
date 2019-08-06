cd src
$python -OO -m PyInstaller --clean --noupx --strip -F --distpath=gamadv-xtd3 $GAMOS-gam.spec
export gampath="gamadv-xtd3"
export gam="$gampath/gam"
export GAMVERSION=`$gam version simple | head -n 1 | cut -c1-7`
cp LICENSE $gampath/
cp license.rtf $gampath/
cp Gam*.txt $gampath/
cp cacerts.pem $gampath/
ls -l $gampath
this_glibc_ver=$(ldd --version | awk '/ldd/{print $NF}')
echo "GAM Version:" $GAMVERSION
echo "GAM OS:" $GAMOS
echo "GAM Platform:" $PLATFORM
echo "glibc:"  glibc$this_glibc_ver
GAM_ARCHIVE=$gampath-$GAMVERSION-$GAMOS-$PLATFORM-glibc$this_glibc_ver.tar.xz
echo "GAM Archive;" $GAM_ARCHIVE
tar cfJ $GAM_ARCHIVE $gampath/
echo "PyInstaller GAM info:"
du -h $gampath/gam
time $gam version extended

if [[ "$dist" == "precise" ]]; then
  GAM_LEGACY_ARCHIVE=gam-$GAMVERSION-$GAMOS-$PLATFORM-legacy.tar.xz
  $python -OO -m staticx gam/gam gam/gam-staticx
  strip gam/gam-staticx
  rm gam/gam
  mv gam/gam-staticx gam/gam
  tar cfJ $GAM_LEGACY_ARCHIVE gam/
  echo "Legacy StaticX GAM info:"
  du -h gam/gam
  time $gam version extended
fi
