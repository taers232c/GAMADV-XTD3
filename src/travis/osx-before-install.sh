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
wget https://www.python.org/ftp/python/$BUILD_PYTHON_VERSION/python-$BUILD_PYTHON_VERSION-macosx10.9.pkg
if [ "$PLATFORM" == "x86_64" ]; then
  export pyfile=python-$BUILD_PYTHON_VERSION-macosx10.9.pkg
else
  export pyfile=python-$BUILD_PYTHON_VERSION-macos11.0.pkg
fi
wget https://www.python.org/ftp/python/$BUILD_PYTHON_VERSION/$pyfile
echo "installing Python $BUILD_PYTHON_VERSION..."
sudo installer -pkg ./$pyfile -target /

# This fixes https://github.com/pyinstaller/pyinstaller/issues/5062
codesign --remove-signature /Library/Frameworks/Python.framework/Versions/3.9/Python

$python -V

cd $whereibelong

#export PATH=/usr/local/opt/python/libexec/bin:$PATH
$pip install --upgrade pip
$pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 $pip install -U
$pip install --upgrade -r src/requirements.txt
$pip install --upgrade git+git://github.com/pyinstaller/pyinstaller.git@$PYINSTALLER_COMMIT
