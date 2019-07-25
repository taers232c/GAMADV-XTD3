cd src
if [ "$VMTYPE" == "test" ]; then
  export gam="$python gam.py"
  export gampath=$(readlink -e .)
else
  $python -OO -m PyInstaller --clean --noupx --strip -F --distpath=gamadv-xtd3 $GAMOS-gam.spec
  export gam="gamadv-xtd3/gam"
  export gampath=gamadv-xtd3
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
  GAM_ARCHIVE=gam-$GAMVERSION-$GAMOS-$PLATFORM-glibc$this_glibc_ver.tar.xz
  echo "GAM Archive;" $GAM_ARCHIVE
  tar cfJ $GAM_ARCHIVE $gampath/
  echo "PyInstaller GAM info:"
  du -h $gampath/gam
  time $gam version extended
fi
