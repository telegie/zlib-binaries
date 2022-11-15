#!/usr/bin/env python3
import platform
import shutil
import subprocess
from pathlib import Path


def cleanup_zconf_h():
    here = Path(__file__).parent.resolve()
    # The line below is needed not to have zlib repository as modified,
    # which leaves an annoying message in git.
    shutil.move(f"{here}/zlib/zconf.h.included", f"{here}/zlib/zconf.h")


def build_x64_windows_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
                    "-S", f"{here}/zlib",
                    "-B", f"{here}/build/x64-windows",
                    "-A" "x64",
                    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/x64-windows"],
                   check=True)
    subprocess.run(["msbuild",
                    f"{here}/build/x64-windows/INSTALL.vcxproj",
                    "/p:Configuration=RelWithDebInfo"],
                   check=True)
    cleanup_zconf_h()


def build_arm64_mac_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
                    "-S", f"{here}/zlib",
                    "-B", f"{here}/build/arm64-mac",
                    "-D", "CMAKE_OSX_ARCHITECTURES=arm64",
                    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/arm64-mac"],
                   check=True)
    subprocess.run(["make", "-C", f"{here}/build/arm64-mac", "-j8"], check=True)
    subprocess.run(["make", "-C", f"{here}/build/arm64-mac", "install"], check=True)
    cleanup_zconf_h()


def build_x64_mac_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
                    "-S", f"{here}/zlib",
                    "-B", f"{here}/build/x64-mac",
                    "-D", "CMAKE_OSX_ARCHITECTURES=x86_64",
                    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/x64-mac"],
                   check=True)
    subprocess.run(["make", "-C", f"{here}/build/x64-mac", "-j8"], check=True)
    subprocess.run(["make", "-C", f"{here}/build/x64-mac", "install"], check=True)
    cleanup_zconf_h()


def build_x64_linux_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
                    "-S", f"{here}/zlib",
                    "-B", f"{here}/build/x64-linux",
                    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/x64-linux"],
                   check=True)
    subprocess.run(["make", "-C", f"{here}/build/x64-linux", "-j8"], check=True)
    subprocess.run(["make", "-C", f"{here}/build/x64-linux", "install"], check=True)
    cleanup_zconf_h()


def main():
    print(f"platform system: {platform.system()}, machine: ({platform.machine()})", flush=True)

    if platform.system() == "Windows":
        build_x64_windows_binaries()
        return
    elif platform.system() == "Darwin":
        build_arm64_mac_binaries()
        build_x64_mac_binaries()
        return
    elif platform.system() == "Linux":
        build_x64_linux_binaries()
        return
    
    raise Exception(f"zlib build not supported.")


if __name__ == "__main__":
    main()
