name = "blosc"

version = "1.17.0"

description = \
    """
    Blosc is a high performance compressor optimized for binary data.
    """

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
]

variants = [
]

uuid = "repository.c-blosc"

def pre_build_commands():

    info = {}
    with open("/etc/os-release", 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line_info = line.replace('\n', '').split('=')
            if len(line_info) != 2:
                continue
            info[line_info[0]] = line_info[1].replace('"', '')
    linux_distro = info.get("NAME", "centos")
    print("Using Linux distro: " + linux_distro)

    if linux_distro.lower().startswith("centos"):
        command("source /opt/rh/devtoolset-6/enable")
    elif linux_distro.lower().startswith("rocky"):
        pass

def commands():
    env.BLOSC_LOCATION = "{root}"
    env.BLOSC_ROOT = "{root}"
    env.BLOSC_INCLUDE_DIR = "{root}/include"
    env.BLOSC_LIBRARY_DIR = "{root}/lib"
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")
