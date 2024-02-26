+++
draft = false
title = "scikit-build 0.17.6-1"
version = "0.17.6-1"
description = "Improved build system generator for CPython C, C++, Cython and Fortran extensions"
date = "2023-10-05T17:34:44"
aliases = "/packages/220749"
categories = ['devel-extra']
upstreamurl = "https://scikit-build.org/"
arch = "x86_64"
size = "108744"
usize = "601099"
sha1sum = "18e937d75362af96f47217f076c2fe2973c0d295"
depends = "['cmake', 'python3-distro', 'python3-setuptools', 'python3-wheel']"
+++
Improved build system generator for CPython C, C++, Cython and Fortran extensions{{< spoiler text="show files" >}}* /usr/lib/python3.12/site-packages/scikit_build-0.17.6.dist-info/licenses/AUTHORS.rst
* /usr/lib/python3.12/site-packages/scikit_build-0.17.6.dist-info/licenses/LICENSE
* /usr/lib/python3.12/site-packages/scikit_build-0.17.6.dist-info/METADATA
* /usr/lib/python3.12/site-packages/scikit_build-0.17.6.dist-info/RECORD
* /usr/lib/python3.12/site-packages/scikit_build-0.17.6.dist-info/WHEEL
* /usr/lib/python3.12/site-packages/skbuild/cmaker.py
* /usr/lib/python3.12/site-packages/skbuild/command/bdist.py
* /usr/lib/python3.12/site-packages/skbuild/command/bdist_wheel.py
* /usr/lib/python3.12/site-packages/skbuild/command/build.py
* /usr/lib/python3.12/site-packages/skbuild/command/build_ext.py
* /usr/lib/python3.12/site-packages/skbuild/command/build_py.py
* /usr/lib/python3.12/site-packages/skbuild/command/clean.py
* /usr/lib/python3.12/site-packages/skbuild/command/egg_info.py
* /usr/lib/python3.12/site-packages/skbuild/command/generate_source_manifest.py
* /usr/lib/python3.12/site-packages/skbuild/command/install.py
* /usr/lib/python3.12/site-packages/skbuild/command/install_lib.py
* /usr/lib/python3.12/site-packages/skbuild/command/install_scripts.py
* /usr/lib/python3.12/site-packages/skbuild/command/sdist.py
* /usr/lib/python3.12/site-packages/skbuild/command/test.py
* /usr/lib/python3.12/site-packages/skbuild/command/__init__.py
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/bdist.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/bdist.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/bdist_wheel.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/bdist_wheel.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/build.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/build.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/build_ext.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/build_ext.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/build_py.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/build_py.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/clean.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/clean.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/egg_info.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/egg_info.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/generate_source_manifest.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/generate_source_manifest.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/install.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/install.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/install_lib.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/install_lib.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/install_scripts.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/install_scripts.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/sdist.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/sdist.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/test.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/test.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/command/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/constants.py
* /usr/lib/python3.12/site-packages/skbuild/exceptions.py
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/abstract.py
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/aix.py
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/bsd.py
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/cygwin.py
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/linux.py
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/osx.py
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/platform_factory.py
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/sunos.py
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/unix.py
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/windows.py
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__init__.py
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/abstract.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/abstract.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/aix.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/aix.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/bsd.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/bsd.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/cygwin.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/cygwin.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/linux.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/linux.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/osx.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/osx.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/platform_factory.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/platform_factory.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/sunos.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/sunos.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/unix.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/unix.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/windows.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/windows.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/platform_specifics/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/py.typed
* /usr/lib/python3.12/site-packages/skbuild/resources/cmake/FindCython.cmake
* /usr/lib/python3.12/site-packages/skbuild/resources/cmake/FindF2PY.cmake
* /usr/lib/python3.12/site-packages/skbuild/resources/cmake/FindNumPy.cmake
* /usr/lib/python3.12/site-packages/skbuild/resources/cmake/FindPythonExtensions.cmake
* /usr/lib/python3.12/site-packages/skbuild/resources/cmake/targetLinkLibrariesWithDynamicLookup.cmake
* /usr/lib/python3.12/site-packages/skbuild/resources/cmake/UseCython.cmake
* /usr/lib/python3.12/site-packages/skbuild/resources/cmake/UseF2PY.cmake
* /usr/lib/python3.12/site-packages/skbuild/resources/cmake/UsePythonExtensions.cmake
* /usr/lib/python3.12/site-packages/skbuild/setuptools_wrap.py
* /usr/lib/python3.12/site-packages/skbuild/utils/__init__.py
* /usr/lib/python3.12/site-packages/skbuild/utils/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/utils/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/_compat/tomllib.py
* /usr/lib/python3.12/site-packages/skbuild/_compat/typing.py
* /usr/lib/python3.12/site-packages/skbuild/_compat/__init__.py
* /usr/lib/python3.12/site-packages/skbuild/_compat/__pycache__/tomllib.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/_compat/__pycache__/tomllib.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/_compat/__pycache__/typing.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/_compat/__pycache__/typing.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/_compat/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/_compat/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/_version.py
* /usr/lib/python3.12/site-packages/skbuild/_version.pyi
* /usr/lib/python3.12/site-packages/skbuild/__init__.py
* /usr/lib/python3.12/site-packages/skbuild/__pycache__/cmaker.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/__pycache__/cmaker.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/__pycache__/constants.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/__pycache__/constants.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/__pycache__/exceptions.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/__pycache__/exceptions.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/__pycache__/setuptools_wrap.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/__pycache__/setuptools_wrap.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/__pycache__/_version.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/__pycache__/_version.cpython-312.pyc
* /usr/lib/python3.12/site-packages/skbuild/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/skbuild/__pycache__/__init__.cpython-312.pyc
* /usr/share/doc/scikit-build-0.17.6/LICENSE
* /usr/share/doc/scikit-build-0.17.6/README.rst
{{< /spoiler >}}