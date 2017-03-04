rm -rf gam
rm -rf build
rm -rf dist
rm -rf gamadv-x3-$1-macos.tar.xz

/Library/Frameworks/Python.framework/Versions/2.7/bin/pyinstaller --clean -F --distpath=gam macos-gam.spec
cp LICENSE gam
cp license.rtf gam
cp whatsnew.txt gam
cp Gam*.txt gam

tar cfJ gamadv-x3-$1-macos.tar.xz gam/ 
