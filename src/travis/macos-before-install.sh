mypath=$(pwd)
cpucount=$(sysctl -n hw.ncpu)
export LD_LIBRARY_PATH=~/ssl/lib
echo "This device has $cpucount CPUs for compiling..."

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
$pip install --upgrade -r src/requirements.txt
$pip install --upgrade git+https://github.com/pyinstaller/pyinstaller.git@$PYINSTALLER_VERSION
