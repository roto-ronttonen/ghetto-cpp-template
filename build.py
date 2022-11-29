import platform
from os import listdir, path
from pathlib import Path
import subprocess


ignore_files = [".DS_Store"]


def should_append(file):
    return file not in ignore_files


win_lib_folder = "./lib/win"
mac_lib_folder = "./lib/mac"
linux_lib_folder = "./lib/linux"

lib_folder = ""
src_folder = "src"
build_folder = "build"
prog_name = "prog"

Path(build_folder).mkdir(parents=True, exist_ok=True)

cmd = "g++"
args = ["-std=c++17",
        "-I",
        "include",
        "-o",
        "{}/{}".format(build_folder, prog_name)]


os = platform.system()

if os == "Windows":
    lib_folder = win_lib_folder
elif os == "Darwin":
    # Im always using arm on mac. But make changes here if need to also check the os architecture
    lib_folder = mac_lib_folder
    args.extend(["-framework", "OpenGL"])
    args.extend(["-framework", "Cocoa"])
    args.extend(["-framework", "IOKit"])
else:
    lib_folder = linux_lib_folder
    # Should use package manager versions in linux i guess. Stupid cpp.....
    args.append("-lglfw3")
    # So if on linux and glfw3 not working just install it with apt (https://shnoh171.github.io/gpu%20and%20gpu%20programming/2019/08/26/installing-glfw-on-ubuntu.html)

for f in listdir(lib_folder):
    if should_append(f):
        args.append(path.join(lib_folder, f))

for f in listdir(src_folder):
    if should_append(f):
        args.append(path.join(src_folder, f))


command = [cmd] + args

p = subprocess.Popen(command, universal_newlines=True)

code = p.wait()
print(code)
