rm -rf gamadv-xtd3
rm -rf build
rm -rf dist
rm -f gamadv-xtd3-$1-macos.tar

pyinstaller3.7 --clean --noupx --strip -F --distpath=gamadv-xtd3 macos-gam.spec
cp LICENSE gamadv-xtd3
cp license.rtf gamadv-xtd3
cp Gam*.txt gamadv-xtd3
cp cacerts.pem gamadv-xtd3

tar -cf gamadv-xtd3-$1-macos.tar gamadv-xtd3/ 
