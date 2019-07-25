cd src
if [ "$VMTYPE" == "test" ]; then
  export gam="$python gam.py"
  export gampath=$(readlink -e .)
else
  $python -OO -m PyInstaller --clean --noupx --strip -F --distpath=gamadv-xtd3 $GAMOS-gam.spec
  export gam="gamadv-xtd3/gam"
  export gampath=$(readlink -e gamadv-xtd3)
  export GAMVERSION=`$gam version simple`
  cp LICENSE $gampath
  cp license.rtf $gampath
  cp Gam*.txt $gampath
  cp cacerts.pem $gampath
  this_glibc_ver=$(ldd --version | awk '/ldd/{print $NF}')
  GAM_ARCHIVE=gam-$GAMVERSION-$GAMOS-$PLATFORM-glibc$this_glibc_ver.tar.xz
  rm $gampath/lastupdatecheck.txt
  tar cfJ $GAM_ARCHIVE gamadv-xtd3/
  echo "PyInstaller GAM info:"
  du -h gamadv-xtd3/gam
  time $gam version extended
fi
