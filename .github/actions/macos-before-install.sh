mypath=$HOME
whereibelong=$(pwd)
cpucount=$(sysctl -n hw.ncpu)
echo "This device has $cpucount CPUs for compiling..."

brew install coreutils
brew install bash

# prefer standard GNU tools like date over MacOS defaults
export PATH="/usr/local/opt/coreutils/libexec/gnubin:$(brew --prefix)/opt/gnu-tar/libexec/gnubin:$PATH"

date --version
gdate --version
bash --version

cd ~

# Use official Python.org version of Python which is backwards compatible
# with older MacOS versions
if [ "$PLATFORM" == "x86_64" ]; then
  export pyfile=python-$BUILD_PYTHON_VERSION-macosx10.9.pkg
else
  export pyfile=python-$BUILD_PYTHON_VERSION-macos11.pkg
fi

wget https://www.python.org/ftp/python/$BUILD_PYTHON_VERSION/$pyfile
echo "installing Python $BUILD_PYTHON_VERSION..."
sudo installer -pkg ./$pyfile -target /

# This fixes https://github.com/pyinstaller/pyinstaller/issues/5062
codesign --remove-signature /Library/Frameworks/Python.framework/Versions/3.9/Python

cd ~

export python=/usr/local/bin/python3
export pip=/usr/local/bin/pip3
SSLVER=$($openssl version)
SSLRESULT=$?
PYVER=$($python -V)
PYRESULT=$?

#brew install swig
#$pip install pyscard

$python -V

cd $whereibelong

