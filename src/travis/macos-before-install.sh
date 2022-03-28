mypath=$(pwd)
cpucount=$(sysctl -n hw.ncpu)
export LD_LIBRARY_PATH=~/ssl/lib
echo "This device has $cpucount CPUs for compiling..."

SSLVER=$(~/ssl/bin/openssl version)
SSLRESULT=$?
if [ $SSLRESULT -ne 0 ] || [[ "$SSLVER" != "OpenSSL $MACOS_BUILD_OPENSSL_VERSION "* ]]; then
  echo "SSL Result: $SSLRESULT - SSL Ver: $SSLVER"
  if [ $SSLRESULT -ne 0 ]; then
    echo "sslresult -ne 0"
  fi
  if [[ "$SSLVER" != "OpenSSL $MACOS_BUILD_OPENSSL_VERSION "* ]]; then
    echo "sslver not equal to..."
  fi
  cd ~
  rm -rf ssl
  mkdir ssl
# Compile latest OpenSSL # wget --quiet https://www.openssl.org/source/openssl-$MACOS_BUILD_OPENSSL_VERSION.tar.gz
  ls -l ${mypath}/sslinstalls
  cp ${mypath}/sslinstalls/openssl-$MACOS_BUILD_OPENSSL_VERSION.tar.gz .
  echo "Extracting OpenSSL..."
  tar xf openssl-$MACOS_BUILD_OPENSSL_VERSION.tar.gz
  cd openssl-$MACOS_BUILD_OPENSSL_VERSION
  echo "Compiling OpenSSL $MACOS_BUILD_OPENSSL_VERSION..."
  ./config shared --prefix=$HOME/ssl
  echo "Running make for OpenSSL..."
  make -j$cpucount -s
  echo "Running make install for OpenSSL..."
  make install > /dev/null
  cd ~
fi

# Use official Python.org version of Python which is backwards compatible
# with older MacOS versions
export pyfile=python-$BUILD_PYTHON_VERSION-macos11.pkg
/bin/rm -f $pyfile

wget https://www.python.org/ftp/python/$BUILD_PYTHON_VERSION/$pyfile
echo "Installing Python $BUILD_PYTHON_VERSION..."
sudo installer -pkg ./$pyfile -target /

cd ~

export python=/usr/local/bin/python3
export pip=/usr/local/bin/pip3

$python -V

cd $mypath

#export PATH=/usr/local/opt/python/libexec/bin:$PATH
$pip install --upgrade pip
$pip install --upgrade packaging
$pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 $pip install -U
$pip install --upgrade git+https://github.com/pyinstaller/pyinstaller.git@$PYINSTALLER_VERSION
$pip install --upgrade -r src/requirements.txt
