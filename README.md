# zlib-binaries

## How to Build

- git submodule update --init --recursive
- python3 build.py

## For Windows

cmake ..\zlib -G "Visual Studio 16 2019" -A x64 -DCMAKE_INSTALL_PREFIX="../install"

Run zlib.sln

