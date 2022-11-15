#!/usr/bin/env python3
import platform
import subprocess
from pathlib import Path


def build_arm64_mac_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
                    "-S", f"{here}/zlib",
                    "-B", f"{here}/build/arm64-mac",
                    "-D", "CMAKE_OSX_ARCHITECTURES=arm64",
                    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/arm64-mac"])
    subprocess.run(["make", "-C", f"{here}/build/arm64-mac", "-j8"])
    subprocess.run(["make", "-C", f"{here}/build/arm64-mac", "install"])
    # The line below is needed not to have zlib repository as modified,
    # which leaves an annoying message in git.
    subprocess.run(["mv", f"{here}/zlib/zconf.h.included", f"{here}/zlib/zconf.h"])


def main():
    if platform.system() == "Darwin":
        build_arm64_mac_binaries()


if __name__ == "__main__":
    main()
