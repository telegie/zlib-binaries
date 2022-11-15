#!/usr/bin/env python3
import platform
import subprocess
from pathlib import Path


def cleanup_zconf_h():
    here = Path(__file__).parent.resolve()
    # The line below is needed not to have zlib repository as modified,
    # which leaves an annoying message in git.
    subprocess.run(["mv", f"{here}/zlib/zconf.h.included", f"{here}/zlib/zconf.h"])


def build_arm64_mac_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
                    "-S", f"{here}/zlib",
                    "-B", f"{here}/build/arm64-mac",
                    "-D", "CMAKE_OSX_ARCHITECTURES=arm64",
                    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/arm64-mac"])
    subprocess.run(["make", "-C", f"{here}/build/arm64-mac", "-j8"])
    subprocess.run(["make", "-C", f"{here}/build/arm64-mac", "install"])
    cleanup_zconf_h()


def build_x64_mac_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
                    "-S", f"{here}/zlib",
                    "-B", f"{here}/build/x64-mac",
                    "-D", "CMAKE_OSX_ARCHITECTURES=x86_64",
                    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/x64-mac"])
    subprocess.run(["make", "-C", f"{here}/build/x64-mac", "-j8"])
    subprocess.run(["make", "-C", f"{here}/build/x64-mac", "install"])
    cleanup_zconf_h()


def main():
    print(f"platform.system(): {platform.system()}")
    print(f"platform.machine(): {platform.machine()}")

    if platform.system() == "Darwin":
        if platform.machine() == "arm64":
            build_arm64_mac_binaries()
            return
        elif platform.machine() == "x86_64":
            build_x64_mac_binaries()
            return
    
    raise Error(f"zlib build not supported.")


if __name__ == "__main__":
    main()
