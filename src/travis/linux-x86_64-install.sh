cd src
if [ "$VMTYPE" == "test" ]; then
  export gam="$python gam.py"
  export gampath=$(readlink -e .)
else
  $python -OO -m PyInstaller --clean --noupx --strip -F --distpath=gam $GAMOS-gam.spec
  export gam="gam/gam"
  export gampath=$(readlink -e gam)
  export GAMVERSION=`$gam version simple`
  cp LICENSE $gampath
  cp license.rtf $gampath
  cp Gam*.txt $gampath
  cp cacerts.pem $gampath
  this_glibc_ver=$(ldd --version | awk '/ldd/{print $NF}')
  GAM_ARCHIVE=gam-$GAMVERSION-$GAMOS-$PLATFORM-glibc$this_glibc_ver.tar.xz
  rm $gampath/lastupdatecheck.txt
  tar cfJ $GAM_ARCHIVE gam/
  echo "PyInstaller GAM info:"
  du -h gam/gam
  time $gam version extended
fi
