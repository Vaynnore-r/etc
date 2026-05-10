#!/bin/bash

# 1. Building Structure 
cd ~/data
rm -rf build_test 
mkdir -p build_test/DEBIAN
mkdir -p build_test/usr/bin
mkdir -p build_test/usr/share/test

# 2. Copying and perms
cp test/test.sh build_test/usr/bin/test
chmod 755 build_test/usr/bin/test
cp -r test/* build_test/usr/share/test/

# 3. CONFIG
cat <<EOF > build_test/DEBIAN/control
Package: test
Version: version
Section: section
Priority: optional
Architecture: all
Depends: depends
Maintainer: author
Description: description
EOF

# 4. Building deb
dpkg-deb --build build_test test_version_full.deb

echo "Package build succeded."

