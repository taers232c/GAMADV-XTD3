if [[ "$PLATFORM" == "x86_64" ]]; then
  export BITS="64"
  export PYTHONFILE_BITS="-amd64"
  export OPENSSL_BITS="-x64"
elif [[ "$PLATFORM" == "x86" ]]; then
  export BITS="32"
  export PYTHONFILE_BITS=""
  export OPENSSL_BITS=""
fi
echo "This is a ${BITS}-bit build for ${PLATFORM}"
export mypath=$(pwd)
cd ~
export python="python"
export pip="pip"

# pyscard needs swig, keep these two together
#choco install $CHOCOPTIONS swig
#$pip install pyscard

cd $mypath

#echo "PATH: $PATH"
#cd ..
#$python setup.py install
#echo "cd to $mypath"
#cd $mypath
