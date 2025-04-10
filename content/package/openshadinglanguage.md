+++
draft = false
title = "openshadinglanguage 1.13.12.0-5"
version = "1.13.12.0-5"
description = "Advanced shading language for production GI renderers"
date = "2025-04-07T11:22:34"
aliases = "/packages/220207"
categories = ['xlib-extra']
upstreamurl = "https://github.com/AcademySoftwareFoundation/openshadinglanguage"
arch = "x86_64"
size = "2229332"
usize = "7304723"
sha1sum = "a50b6e9d8be1099c6d0b8b3ec55cf06d5d7df080"
depends = "['clang-libs>=19.1.1', 'intel-tbb', 'libboost>=1.87.0', 'openexr', 'openimageio>=2.5', 'pugixml', 'python3>=3.13']"
+++
### Description: 
Advanced shading language for production GI renderers

### Files: 
* /usr/bin/oslc
* /usr/bin/oslinfo
* /usr/bin/osltoy
* /usr/bin/testrender
* /usr/bin/testshade
* /usr/bin/testshade_dso
* /usr/build-scripts/serialize-bc.py
* /usr/cmake/llvm_macros.cmake
* /usr/include/OSL/accum.h
* /usr/include/OSL/batched_rendererservices.h
* /usr/include/OSL/batched_shaderglobals.h
* /usr/include/OSL/batched_texture.h
* /usr/include/OSL/device_ptr.h
* /usr/include/OSL/device_string.h
* /usr/include/OSL/dual.h
* /usr/include/OSL/dual_vec.h
* /usr/include/OSL/encodedtypes.h
* /usr/include/OSL/export.h
* /usr/include/OSL/fmt_util.h
* /usr/include/OSL/genclosure.h
* /usr/include/OSL/Imathx/ImathColor.h
* /usr/include/OSL/Imathx/ImathFun.h
* /usr/include/OSL/Imathx/ImathLimits.h
* /usr/include/OSL/Imathx/ImathMatrix.h
* /usr/include/OSL/Imathx/ImathVec.h
* /usr/include/OSL/Imathx/Imathx.h
* /usr/include/OSL/journal.h
* /usr/include/OSL/llvm_util.h
* /usr/include/OSL/mask.h
* /usr/include/OSL/matrix22.h
* /usr/include/OSL/optautomata.h
* /usr/include/OSL/oslclosure.h
* /usr/include/OSL/oslcomp.h
* /usr/include/OSL/oslconfig.h
* /usr/include/OSL/oslexec.h
* /usr/include/OSL/oslnoise.h
* /usr/include/OSL/oslquery.h
* /usr/include/OSL/oslversion.h
* /usr/include/OSL/platform.h
* /usr/include/OSL/rendererservices.h
* /usr/include/OSL/rs_free_function.h
* /usr/include/OSL/sfmath.h
* /usr/include/OSL/sfm_simplex.h
* /usr/include/OSL/sfm_staticmatrix.h
* /usr/include/OSL/shaderglobals.h
* /usr/include/OSL/strdecls.h
* /usr/include/OSL/variant.h
* /usr/include/OSL/wide.h
* /usr/lib/cmake/OSL/OSLConfig.cmake
* /usr/lib/cmake/OSL/OSLConfigVersion.cmake
* /usr/lib/cmake/OSL/OSLTargets-release.cmake
* /usr/lib/cmake/OSL/OSLTargets.cmake
* /usr/lib/liboslcomp.so
* /usr/lib/liboslcomp.so.1.13
* /usr/lib/liboslcomp.so.1.13.12
* /usr/lib/liboslexec.so
* /usr/lib/liboslexec.so.1.13
* /usr/lib/liboslexec.so.1.13.12
* /usr/lib/liboslnoise.so
* /usr/lib/liboslnoise.so.1.13
* /usr/lib/liboslnoise.so.1.13.12
* /usr/lib/liboslquery.so
* /usr/lib/liboslquery.so.1.13
* /usr/lib/liboslquery.so.1.13.12
* /usr/lib/libtestshade.so
* /usr/lib/libtestshade.so.1.13
* /usr/lib/libtestshade.so.1.13.12
* /usr/lib/osl.imageio.so
* /usr/lib/pkgconfig/oslcomp.pc
* /usr/lib/pkgconfig/oslexec.pc
* /usr/lib/pkgconfig/oslquery.pc
* /usr/lib/python3.13/site-packages/oslquery.so
* /usr/share/doc/openshadinglanguage-1.13.12.0/INSTALL.md
* /usr/share/doc/openshadinglanguage-1.13.12.0/README.md
* /usr/share/doc/OSL/CHANGES.md
* /usr/share/doc/OSL/docdeep.md.html
* /usr/share/doc/OSL/docs.css
* /usr/share/doc/OSL/Figures/osltoy/osltoy-error.jpg
* /usr/share/doc/OSL/Figures/osltoy/osltoy-fbm.jpg
* /usr/share/doc/OSL/Figures/osltoy/osltoy-start.jpg
* /usr/share/doc/OSL/Figures/testshade/fBm_default.jpg
* /usr/share/doc/OSL/Figures/testshade/fBm_freq.jpg
* /usr/share/doc/OSL/Figures/testshade/fBm_gain.jpg
* /usr/share/doc/OSL/Figures/testshade/fBm_lac.jpg
* /usr/share/doc/OSL/Figures/testshade/fBm_octaves.jpg
* /usr/share/doc/OSL/Figures/testshade/makenoise.jpg
* /usr/share/doc/OSL/Figures/testshade/noisetex.jpg
* /usr/share/doc/OSL/Figures/testshade/show_uv.jpg
* /usr/share/doc/OSL/INSTALL.md
* /usr/share/doc/OSL/LICENSE.md
* /usr/share/doc/OSL/markdeep.min.js
* /usr/share/doc/OSL/osl-languagespec.pdf
* /usr/share/doc/OSL/OSLQuery.md.html
* /usr/share/doc/OSL/osltoy.md.html
* /usr/share/doc/OSL/README.md
* /usr/share/doc/OSL/testshade.md.html
* /usr/share/OSL/shaders/color2.h
* /usr/share/OSL/shaders/color4.h
* /usr/share/OSL/shaders/emitter.osl
* /usr/share/OSL/shaders/emitter.oso
* /usr/share/OSL/shaders/glass.osl
* /usr/share/OSL/shaders/glass.oso
* /usr/share/OSL/shaders/image.osl
* /usr/share/OSL/shaders/image.oso
* /usr/share/OSL/shaders/mandelbrot.osl
* /usr/share/OSL/shaders/mandelbrot.oso
* /usr/share/OSL/shaders/matrix33.h
* /usr/share/OSL/shaders/matte.osl
* /usr/share/OSL/shaders/matte.oso
* /usr/share/OSL/shaders/metal.osl
* /usr/share/OSL/shaders/metal.oso
* /usr/share/OSL/shaders/oslutil.h
* /usr/share/OSL/shaders/stdosl.h
* /usr/share/OSL/shaders/ubersurface.osl
* /usr/share/OSL/shaders/ubersurface.oso
* /usr/share/OSL/shaders/vector2.h
* /usr/share/OSL/shaders/vector4.h
