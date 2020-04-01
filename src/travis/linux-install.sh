cd src
if [[ "$TRAVIS_JOB_NAME" == *"Testing" ]]; then
  export gam="$python gam.py"
  export gampath=$(readlink -e .)
else
  export gampath="gamadv-xtd3"
  $python -OO -m PyInstaller --clean --noupx --strip -F --distpath=$gampath $GAMOS-gam.spec
  export gam="$gampath/gam"
  export GAMVERSION=`$gam version simple | head -n 1 | cut -c1-7`
  cp LICENSE $gampath/
  cp license.rtf $gampath/
  cp Gam*.txt $gampath/
  cp cacerts.pem $gampath/
  this_glibc_ver=$(ldd --version | awk '/ldd/{print $NF}')
  GAM_ARCHIVE=$gampath-$GAMVERSION-$GAMOS-$PLATFORM-glibc$this_glibc_ver.tar.xz
  tar cfJ $GAM_ARCHIVE $gampath/
  echo "PyInstaller GAM info:"
  du -h $gampath/gam
  time $gam version extended

  if [ "${TRAVIS_DIST}" == "precise" ] && [ "${PLATFORM}" == "x86_64" ]; then
    GAM_LEGACY_ARCHIVE=$gampath-${GAMVERSION}-${GAMOS}-${PLATFORM}-legacy.tar.xz
    $python -OO -m staticx $gampath/gam $gampath/gam-staticx
    strip $gampath/gam-staticx
    rm $gampath/gam
    mv $gampath/gam-staticx $gampath/gam
    chmod 755 $gampath/gam
    tar cfJ $GAM_LEGACY_ARCHIVE $gampath/
    echo "Legacy StaticX GAM info:"
    du -h $gampath/gam
    time $gam version extended
  fi
  echo "GAM packages:"
  ls -l $gampath-*.xz
fi
