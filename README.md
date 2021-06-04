# zlib-binaries

mkdir build

cd build

## For Windows

### For x64-windows
cmake ..\zlib -G "Visual Studio 16 2019" -A x64 -DCMAKE_INSTALL_PREFIX="../install"

### For x86-uwp
cmake ..\zlib -G "Visual Studio 16 2019" -A Win32 -DCMAKE_SYSTEM_NAME=WindowsStore -DCMAKE_SYSTEM_VERSION="10.0" -DCMAKE_INSTALL_PREFIX="../install"

Run zlib.sln

## For Mac

cmake ../zlib -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX="../install"

make

make install
