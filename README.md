# zlib-binaries

## How to Build

Run "python3 build.py"

## For Windows

cmake ..\zlib -G "Visual Studio 16 2019" -A x64 -DCMAKE_INSTALL_PREFIX="../install"

Run zlib.sln

## For Mac

cmake ../zlib -DCMAKE_OSX_ARCHITECTURES=arm64 -DCMAKE_INSTALL_PREFIX="../install"
make
make install

## For Linux

cmake ../zlib -DCMAKE_INSTALL_PREFIX="../1.2.11/x64-linux"
make
make install
