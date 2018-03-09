rm -rf gam
rm -rf build
rm -rf dist
rm -f gamadv-x3-$1-macos.tar

/Library/Frameworks/Python.framework/Versions/3.6/bin/pyinstaller --clean -F --distpath=gam macos-gam.spec
cp LICENSE gam
cp license.rtf gam
cp whatsnew.txt gam
cp Gam*.txt gam

tar -cf gamadv-x3-$1-macos.tar gam/ 
