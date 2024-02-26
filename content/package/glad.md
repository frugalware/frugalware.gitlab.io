+++
draft = false
title = "glad 2.0.4-2"
version = "2.0.4-2"
description = "Multi-Language Vulkan/GL/GLES/EGL/GLX/WGL Loader-Generator based on the official specs"
date = "2023-10-12T11:07:59"
aliases = "/packages/220869"
categories = ['devel-extra']
upstreamurl = "https://github.com/Dav1dde/glad"
arch = "x86_64"
size = "471052"
usize = "6116674"
sha1sum = "c173acf6358bf8de2cb606f078f6af12ae87853c"
depends = "['python3-jinja', 'python3-lxml', 'python3-setuptools']"
+++
Multi-Language Vulkan/GL/GLES/EGL/GLX/WGL Loader-Generator based on the official specs{{< spoiler text="show files" >}}* /usr/bin/glad
* /usr/lib/python3.12/site-packages/glad/config.py
* /usr/lib/python3.12/site-packages/glad/files/egl.xml
* /usr/lib/python3.12/site-packages/glad/files/eglplatform.h
* /usr/lib/python3.12/site-packages/glad/files/gl.xml
* /usr/lib/python3.12/site-packages/glad/files/glx.xml
* /usr/lib/python3.12/site-packages/glad/files/khrplatform.h
* /usr/lib/python3.12/site-packages/glad/files/vk.xml
* /usr/lib/python3.12/site-packages/glad/files/vk_platform.h
* /usr/lib/python3.12/site-packages/glad/files/vulkan_video_codec_h264std.h
* /usr/lib/python3.12/site-packages/glad/files/vulkan_video_codec_h264std_decode.h
* /usr/lib/python3.12/site-packages/glad/files/vulkan_video_codec_h264std_encode.h
* /usr/lib/python3.12/site-packages/glad/files/vulkan_video_codec_h265std.h
* /usr/lib/python3.12/site-packages/glad/files/vulkan_video_codec_h265std_decode.h
* /usr/lib/python3.12/site-packages/glad/files/vulkan_video_codec_h265std_encode.h
* /usr/lib/python3.12/site-packages/glad/files/wgl.xml
* /usr/lib/python3.12/site-packages/glad/files/__init__.py
* /usr/lib/python3.12/site-packages/glad/files/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/glad/files/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/base_template.c
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/base_template.h
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/egl.c
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/egl.h
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/gl.c
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/gl.h
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/glx.c
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/glx.h
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/header_only.h
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/impl_util.c
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/loader/egl.c
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/loader/egl.h
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/loader/gl.c
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/loader/gl.h
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/loader/gles1.c
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/loader/gles1.h
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/loader/gles2.c
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/loader/gles2.h
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/loader/glsc2.c
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/loader/glsc2.h
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/loader/glx.c
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/loader/glx.h
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/loader/library.c
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/loader/vulkan.c
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/loader/vulkan.h
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/loader/wgl.c
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/loader/wgl.h
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/platform.h
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/template_utils.h
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/vk.c
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/vk.h
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/wgl.c
* /usr/lib/python3.12/site-packages/glad/generator/c/templates/wgl.h
* /usr/lib/python3.12/site-packages/glad/generator/c/__init__.py
* /usr/lib/python3.12/site-packages/glad/generator/c/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/glad/generator/c/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/glad/generator/rust/templates/Cargo.toml
* /usr/lib/python3.12/site-packages/glad/generator/rust/templates/impl.rs
* /usr/lib/python3.12/site-packages/glad/generator/rust/templates/lib.rs
* /usr/lib/python3.12/site-packages/glad/generator/rust/templates/template_utils.rs
* /usr/lib/python3.12/site-packages/glad/generator/rust/templates/types/egl.rs
* /usr/lib/python3.12/site-packages/glad/generator/rust/templates/types/gl.rs
* /usr/lib/python3.12/site-packages/glad/generator/rust/templates/types/glx.rs
* /usr/lib/python3.12/site-packages/glad/generator/rust/templates/types/khrplatform.rs
* /usr/lib/python3.12/site-packages/glad/generator/rust/templates/types/vk.rs
* /usr/lib/python3.12/site-packages/glad/generator/rust/templates/types/wgl.rs
* /usr/lib/python3.12/site-packages/glad/generator/rust/__init__.py
* /usr/lib/python3.12/site-packages/glad/generator/rust/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/glad/generator/rust/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/glad/generator/util.py
* /usr/lib/python3.12/site-packages/glad/generator/__init__.py
* /usr/lib/python3.12/site-packages/glad/generator/__pycache__/util.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/glad/generator/__pycache__/util.cpython-312.pyc
* /usr/lib/python3.12/site-packages/glad/generator/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/glad/generator/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/glad/opener.py
* /usr/lib/python3.12/site-packages/glad/parse.py
* /usr/lib/python3.12/site-packages/glad/plugin.py
* /usr/lib/python3.12/site-packages/glad/sink.py
* /usr/lib/python3.12/site-packages/glad/specification.py
* /usr/lib/python3.12/site-packages/glad/util.py
* /usr/lib/python3.12/site-packages/glad/__init__.py
* /usr/lib/python3.12/site-packages/glad/__main__.py
* /usr/lib/python3.12/site-packages/glad/__pycache__/config.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/glad/__pycache__/config.cpython-312.pyc
* /usr/lib/python3.12/site-packages/glad/__pycache__/opener.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/glad/__pycache__/opener.cpython-312.pyc
* /usr/lib/python3.12/site-packages/glad/__pycache__/parse.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/glad/__pycache__/parse.cpython-312.pyc
* /usr/lib/python3.12/site-packages/glad/__pycache__/plugin.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/glad/__pycache__/plugin.cpython-312.pyc
* /usr/lib/python3.12/site-packages/glad/__pycache__/sink.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/glad/__pycache__/sink.cpython-312.pyc
* /usr/lib/python3.12/site-packages/glad/__pycache__/specification.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/glad/__pycache__/specification.cpython-312.pyc
* /usr/lib/python3.12/site-packages/glad/__pycache__/util.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/glad/__pycache__/util.cpython-312.pyc
* /usr/lib/python3.12/site-packages/glad/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/glad/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/glad/__pycache__/__main__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/glad/__pycache__/__main__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/glad2-2.0.4.dist-info/entry_points.txt
* /usr/lib/python3.12/site-packages/glad2-2.0.4.dist-info/LICENSE
* /usr/lib/python3.12/site-packages/glad2-2.0.4.dist-info/METADATA
* /usr/lib/python3.12/site-packages/glad2-2.0.4.dist-info/RECORD
* /usr/lib/python3.12/site-packages/glad2-2.0.4.dist-info/top_level.txt
* /usr/lib/python3.12/site-packages/glad2-2.0.4.dist-info/WHEEL
* /usr/share/doc/glad-2.0.4/AUTHORS
* /usr/share/doc/glad-2.0.4/ChangeLog
* /usr/share/doc/glad-2.0.4/COPYING
* /usr/share/doc/glad-2.0.4/LICENSE
* /usr/share/doc/glad-2.0.4/README.md
* /usr/share/doc/glad-2.0.4/VERSION
{{< /spoiler >}}