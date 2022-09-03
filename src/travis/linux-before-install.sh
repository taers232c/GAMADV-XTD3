echo "RUNNING: apt update..."
sudo apt-get -qq --yes update > /dev/null
export mypath=$(pwd)
echo "We are running on Ubuntu $TRAVIS_DIST $PLATFORM"
ldd --version
export LD_LIBRARY_PATH=~/ssl/lib:~/python/lib
export cpucount=$(nproc --all)
echo "This device has $cpucount CPUs for compiling..."
sudo apt-get -qq --yes install xz-utils > /dev/null
sudo apt-get -qq --yes install libwww-curl-perl > /dev/null
export SSLVER=$(~/ssl/bin/openssl version)
export SSLRESULT=$?
export PYVER=$(~/python/bin/python3 -V)
export PYRESULT=$?
sudo apt-get -qq --yes install libxml2-dev > /dev/null
sudo apt-get -qq --yes install libxslt-dev > /dev/null
if [ $SSLRESULT -ne 0 ] || [[ "$SSLVER" != "OpenSSL $LINUX_BUILD_OPENSSL_VERSION "* ]] || [ $PYRESULT -ne 0 ] || [[ "$PYVER" != "Python $BUILD_PYTHON_VERSION"* ]]; then
  echo "SSL Result: $SSLRESULT - SSL Ver: $SSLVER - Py Result: $PYRESULT - Py Ver: $PYVER"
  if [ $SSLRESULT -ne 0 ]; then
    echo "sslresult -ne 0"
  fi
  if [[ "$SSLVER" != "OpenSSL $LINUX_BUILD_OPENSSL_VERSION "* ]]; then
    echo "sslver not equal to..."
  fi
  if [ $PYRESULT -ne 0 ]; then
    echo "pyresult -ne 0"
  fi
  if [[ "$PYVER" != "Python $BUILD_PYTHON_VERSION" ]]; then
    echo "pyver not equal to..."
  fi
  cd ~
  rm -rf ssl
  rm -rf python
  mkdir ssl
  mkdir python
  echo "RUNNING: apt upgrade..."
  sudo apt-mark hold openssh-server
  if [[ "$DIST_UPGRADE" == "true" ]]; then
    sudo apt-get -qq --yes upgrade
    sudo apt-get -qq --yes --with-new-pkgs upgrade
  fi
  echo "Installing build tools..."
  sudo apt-get -qq --yes install build-essential
  echo "Installing deps for python3"
  sudo cp -v /etc/apt/sources.list /tmp
  sudo chmod a+rwx /tmp/sources.list
  echo "deb-src http://archive.ubuntu.com/ubuntu/ $TRAVIS_DIST main" >> /tmp/sources.list
  sudo cp -v /tmp/sources.list /etc/apt
  sudo apt-get -qq --yes update > /dev/null
  sudo apt-get -qq --yes build-dep python3 > /dev/null

  # Compile latest OpenSSL
  ls -l ${mypath}/sslinstalls
  cp ${mypath}/sslinstalls/openssl-$LINUX_BUILD_OPENSSL_VERSION.tar.gz .
  echo "Extracting OpenSSL..."
  tar xf openssl-$LINUX_BUILD_OPENSSL_VERSION.tar.gz
  cd openssl-$LINUX_BUILD_OPENSSL_VERSION
  echo "Compiling OpenSSL $LINUX_BUILD_OPENSSL_VERSION..."
  ./config shared --prefix=$HOME/ssl
  echo "Running make for OpenSSL..."
  make -j$cpucount -s
  echo "Running make install for OpenSSL..."
  make install > /dev/null
  cd ~

  # Compile latest Python
  echo "Downloading Python $BUILD_PYTHON_VERSION..."
  curl -O --silent "https://www.python.org/ftp/python/${BUILD_PYTHON_VERSION}/Python-${BUILD_PYTHON_VERSION}.tar.xz"
  echo "Extracting Python..."
  tar xf "Python-${BUILD_PYTHON_VERSION}.tar.xz"
  cd Python-${BUILD_PYTHON_VERSION}
  echo "Compiling Python ${BUILD_PYTHON_VERSION}..."
  safe_flags="--with-openssl=$HOME/ssl --enable-shared --prefix=${HOME}/python --with-ensurepip=upgrade"
  unsafe_flags="--enable-optimizations --with-lto"
  if [ ! -e Makefile ]; then
    echo "running configure with safe and unsafe"
    ./configure $safe_flags $unsafe_flags > /dev/null
  fi
  make -j$cpucount -s
  RESULT=$?
  echo "First make exited with $RESULT"
  if [ $RESULT != 0 ]; then
    echo "Trying Python compile again without unsafe flags..."
    make clean
    ./configure $safe_flags > /dev/null
    make -j$cpucount -s
    echo "Sticking with safe Python for now..."
  fi
  echo "Installing Python..."
  make install > /dev/null
  cd ~
fi

python=~/python/bin/python3
pip=~/python/bin/pip3

if ([ "${TRAVIS_DIST}" == "precise" ] || [ "${TRAVIS_DIST}" == "trusty" ] || [ "${TRAVIS_DIST}" == "xenial" ]) && [ "${PLATFORM}" == "x86_64" ]; then
  echo "Installing deps for StaticX..."
  if [ ! -d patchelf-$PATCHELF_VERSION ]; then
    echo "Downloading PatchELF $PATCHELF_VERSION"
#      wget https://nixos.org/releases/patchelf/patchelf-$PATCHELF_VERSION/patchelf-$PATCHELF_VERSION.tar.bz2
#      tar xf patchelf-$PATCHELF_VERSION.tar.bz2
#      cd patchelf-$PATCHELF_VERSION
    wget https://github.com/NixOS/patchelf/archive/$PATCHELF_VERSION.tar.gz 
    tar xf $PATCHELF_VERSION.tar.gz
    cd patchelf-$PATCHELF_VERSION/
    ./bootstrap.sh
    ./configure
    make
    sudo make install
  fi
  $pip install staticx
fi

$pip install --upgrade git+https://github.com/pyinstaller/pyinstaller.git@$PYINSTALLER_VERSION

cd $mypath

echo "Upgrading pip packages..."
$pip install --upgrade pip
$pip install --upgrade packaging
$pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 $pip install -U
$pip install --upgrade -r src/requirements.txt
$pip install wheel
