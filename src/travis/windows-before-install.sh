if [[ "$PLATFORM" == "x86_64" ]]; then
  export BITS="64"
  export PYTHONFILE_BITS="-amd64"
  export OPENSSL_BITS="-x64"
  export WIX_BITS="x64"
elif [[ "$PLATFORM" == "x86" ]]; then
  export BITS="32"
  export PYTHONFILE_BITS=""
  export OPENSSL_BITS=""
  export WIX_BITS="x86"
fi
echo "This is a ${BITS}-bit build for ${PLATFORM}"

export mypath=$(pwd)
cd ~

# .NET Core
echo "Installing Net-Framework-Core..."
until powershell Install-WindowsFeature Net-Framework-Core; do echo "Trying .NET install again..."; done

# Chocolatey
#echo "Upgrading Chocolatey.."
#until choco upgrade chocolatey -y; do echo "Trying Chocolatey upgrade again..."; done

# VS 2015
#echo "Upgrading Visual Studio 2015.."
#until choco upgrade vcbuildtools -y; do echo "Trying Visual Studio upgrade again..."; done

# WIX Toolset
echo "Upgrading WIX Toolset.."
until choco upgrade wixtoolset -y; do echo "Trying WIX Toolset upgrade again..."; done

# Python
echo "Installing Python..."
export python_file=python-${BUILD_PYTHON_VERSION}${PYTHONFILE_BITS}.exe
if [ ! -e $python_file ]; then
  echo "Downloading $python_file..."
  wget --quiet https://www.python.org/ftp/python/$BUILD_PYTHON_VERSION/$python_file
fi
until powershell ".\\${python_file} /quiet InstallAllUsers=1 TargetDir=c:\\python include_lib=1 include_pip=1"; do echo "trying python again..."; done
export python=/c/python/python.exe
export pip=/c/python/scripts/pip.exe
until [ -f $pip ]; do echo "waiting for pip"; ls -l /c/python; sleep 10; done
export PATH=$PATH:/c/python/scripts

# OpenSSL
echo "Installing OpenSSL..."
#export exefile=Win${BITS}OpenSSL_Light-${BUILD_OPENSSL_VERSION//./_}.exe
#if [ ! -e $exefile ]; then
#  echo "Downloading $exefile..."
#  wget --quiet https://slproweb.com/download/$exefile
#fi
#until powershell ".\\${exefile} /silent /sp- /suppressmsgboxes /DIR=C:\\ssl"; do echo "trying openssl again..."; done
#until cp -v /c/ssl/libcrypto-1_1${OPENSSL_BITS}.dll /c/python/DLLs/; do echo "trying libcrypto copy again..."; sleep 3; done
#until cp -v /c/ssl/libssl-1_1${OPENSSL_BITS}.dll /c/python/DLLs/; do echo "trying libssl copy again..."; done
#if [[ "$PLATFORM" == "x86_64" ]]; then
#  cp -v /c/python/DLLs/libssl-1_1-x64.dll /c/python/DLLs/libssl-1_1.dll
#  cp -v /c/python/DLLs/libcrypto-1_1-x64.dll /c/python/DLLs/libcrypto-1_1.dll
#fi

export zipfile=openssl-${BUILD_OPENSSL_VERSION}.zip
if [ ! -e $zipfile ]; then
  echo "Downloading $zipfile..."
  wget --quiet https://mirror.firedaemon.com/OpenSSL/$zipfile
fi
unzip $zipfile
if [[ "$PLATFORM" == "x86_64" ]]; then
  until cp -v ~/openssl-1.1/x64/bin/libcrypto-1_1-x64.dll /c/python/DLLs/libcrypto-1_1.dll; do echo "Copying libcrypto..."; sleep 2; done
  until cp -v ~/openssl-1.1/x64/bin/libssl-1_1-x64.dll /c/python/DLLs/libssl-1_1.dll; do echo "Copying libssl..."; sleep 2; done
else
  until cp -v ~/openssl-1.1/x86/bin/libcrypto-1_1.dll /c/python/DLLs/; do echo "Copying libcrypto..."; sleep 2; done
  until cp -v ~/openssl-1.1/x86/bin/libssl-1_1.dll /c/python/DLLs/; do echo "Copying libssl..."; sleep 2; done
fi
ls -l /c/python/DLLs

cd $mypath

$pip install --upgrade pip
$pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 $pip install -U
$pip install --upgrade -r src/requirements.txt
$pip install --upgrade pyinstaller
# Install PyInstaller from source and build bootloader
# to try and avoid getting flagged as malware since
# lots of malware uses PyInstaller default bootloader
# https://stackoverflow.com/questions/53584395/how-to-recompile-the-bootloader-of-pyinstaller
#echo "Downloading PyInstaller..."
#wget --quiet https://github.com/pyinstaller/pyinstaller/archive/$PYINSTALLER_COMMIT.tar.gz
#tar xf $PYINSTALLER_COMMIT.tar.gz
#mv pyinstaller-$PYINSTALLER_COMMIT pyinstaller
#cd pyinstaller/bootloader
#echo "bootloader before:"
#md5sum ../PyInstaller/bootloader/Windows-${BITS}bit/*
#
#$python ./waf all --target-arch=${BITS}bit --msvc_version "msvc 14.0"
#
#echo "bootloader after:"
#md5sum ../PyInstaller/bootloader/Windows-${BITS}bit/*
#echo "PATH: $PATH"
#cd ..
#$python setup.py install
echo "cd to $mypath"
cd $mypath
