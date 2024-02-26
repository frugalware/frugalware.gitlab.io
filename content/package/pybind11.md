+++
draft = false
title = "pybind11 2.11.1-1"
version = "2.11.1-1"
description = "A lightweight header-only library that exposes C++ types in Python and vice versa"
date = "2023-10-06T08:01:52"
aliases = "/packages/220212"
categories = ['devel-extra']
upstreamurl = "https://pybind11.readthedocs.org/"
arch = "x86_64"
size = "174048"
usize = "1691957"
sha1sum = "e70eb8ed27b32babf2ba12b2996b2032fc0e6b03"
depends = "['python3>=3.12']"
reverse_depends = "['audiotube', 'dlib', 'opencolorio', 'openimageio', 'python3-scipy']"
+++
A lightweight header-only library that exposes C++ types in Python and vice versa

{{< files text="show files" >}}* /usr/bin/pybind11-config
* /usr/include/pybind11/attr.h
* /usr/include/pybind11/buffer_info.h
* /usr/include/pybind11/cast.h
* /usr/include/pybind11/chrono.h
* /usr/include/pybind11/common.h
* /usr/include/pybind11/complex.h
* /usr/include/pybind11/detail/class.h
* /usr/include/pybind11/detail/common.h
* /usr/include/pybind11/detail/descr.h
* /usr/include/pybind11/detail/init.h
* /usr/include/pybind11/detail/internals.h
* /usr/include/pybind11/detail/typeid.h
* /usr/include/pybind11/detail/type_caster_base.h
* /usr/include/pybind11/eigen.h
* /usr/include/pybind11/eigen/common.h
* /usr/include/pybind11/eigen/matrix.h
* /usr/include/pybind11/eigen/tensor.h
* /usr/include/pybind11/embed.h
* /usr/include/pybind11/eval.h
* /usr/include/pybind11/functional.h
* /usr/include/pybind11/gil.h
* /usr/include/pybind11/iostream.h
* /usr/include/pybind11/numpy.h
* /usr/include/pybind11/operators.h
* /usr/include/pybind11/options.h
* /usr/include/pybind11/pybind11.h
* /usr/include/pybind11/pytypes.h
* /usr/include/pybind11/stl.h
* /usr/include/pybind11/stl/filesystem.h
* /usr/include/pybind11/stl_bind.h
* /usr/include/pybind11/type_caster_pyobject_ptr.h
* /usr/lib/pkgconfig/pybind11.pc
* /usr/lib/python3.12/site-packages/pybind11-2.11.1-py3.12.egg-info/dependency_links.txt
* /usr/lib/python3.12/site-packages/pybind11-2.11.1-py3.12.egg-info/entry_points.txt
* /usr/lib/python3.12/site-packages/pybind11-2.11.1-py3.12.egg-info/not-zip-safe
* /usr/lib/python3.12/site-packages/pybind11-2.11.1-py3.12.egg-info/PKG-INFO
* /usr/lib/python3.12/site-packages/pybind11-2.11.1-py3.12.egg-info/requires.txt
* /usr/lib/python3.12/site-packages/pybind11-2.11.1-py3.12.egg-info/SOURCES.txt
* /usr/lib/python3.12/site-packages/pybind11-2.11.1-py3.12.egg-info/top_level.txt
* /usr/lib/python3.12/site-packages/pybind11/commands.py
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/attr.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/buffer_info.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/cast.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/chrono.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/common.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/complex.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/detail/class.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/detail/common.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/detail/descr.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/detail/init.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/detail/internals.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/detail/typeid.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/detail/type_caster_base.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/eigen.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/eigen/common.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/eigen/matrix.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/eigen/tensor.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/embed.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/eval.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/functional.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/gil.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/iostream.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/numpy.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/operators.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/options.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/pybind11.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/pytypes.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/stl.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/stl/filesystem.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/stl_bind.h
* /usr/lib/python3.12/site-packages/pybind11/include/pybind11/type_caster_pyobject_ptr.h
* /usr/lib/python3.12/site-packages/pybind11/py.typed
* /usr/lib/python3.12/site-packages/pybind11/setup_helpers.py
* /usr/lib/python3.12/site-packages/pybind11/share/cmake/pybind11/FindPythonLibsNew.cmake
* /usr/lib/python3.12/site-packages/pybind11/share/cmake/pybind11/pybind11Common.cmake
* /usr/lib/python3.12/site-packages/pybind11/share/cmake/pybind11/pybind11Config.cmake
* /usr/lib/python3.12/site-packages/pybind11/share/cmake/pybind11/pybind11ConfigVersion.cmake
* /usr/lib/python3.12/site-packages/pybind11/share/cmake/pybind11/pybind11NewTools.cmake
* /usr/lib/python3.12/site-packages/pybind11/share/cmake/pybind11/pybind11Targets.cmake
* /usr/lib/python3.12/site-packages/pybind11/share/cmake/pybind11/pybind11Tools.cmake
* /usr/lib/python3.12/site-packages/pybind11/share/pkgconfig/pybind11.pc
* /usr/lib/python3.12/site-packages/pybind11/_version.py
* /usr/lib/python3.12/site-packages/pybind11/__init__.py
* /usr/lib/python3.12/site-packages/pybind11/__main__.py
* /usr/lib/python3.12/site-packages/pybind11/__pycache__/commands.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pybind11/__pycache__/setup_helpers.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pybind11/__pycache__/_version.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pybind11/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pybind11/__pycache__/__main__.cpython-312.pyc
* /usr/share/cmake/pybind11/FindPythonLibsNew.cmake
* /usr/share/cmake/pybind11/pybind11Common.cmake
* /usr/share/cmake/pybind11/pybind11Config.cmake
* /usr/share/cmake/pybind11/pybind11ConfigVersion.cmake
* /usr/share/cmake/pybind11/pybind11NewTools.cmake
* /usr/share/cmake/pybind11/pybind11Targets.cmake
* /usr/share/cmake/pybind11/pybind11Tools.cmake
* /usr/share/doc/pybind11-2.11.1/LICENSE
* /usr/share/doc/pybind11-2.11.1/README.rst
{{< /files >}}