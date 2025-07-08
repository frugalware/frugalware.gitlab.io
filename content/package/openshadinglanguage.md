+++
draft = false
title = "openshadinglanguage 1.14.6.0-1"
version = "1.14.6.0-1"
description = "Advanced shading language for production GI renderers"
date = "2025-07-08T16:28:19"
aliases = "/packages/220207"
categories = ['xlib-extra']
upstreamurl = "https://github.com/AcademySoftwareFoundation/openshadinglanguage"
arch = "x86_64"
size = "5767736"
usize = "26022601"
sha1sum = "325932a1d26817425c02d30c1ed4eb238539277d"
depends = "['clang-libs>=20.1.6', 'intel-tbb', 'openexr', 'openimageio>=2.5', 'partio', 'pugixml', 'python3>=3.13']"
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
* /usr/include/OSL/dual.h
* /usr/include/OSL/dual_vec.h
* /usr/include/OSL/encodedtypes.h
* /usr/include/OSL/export.h
* /usr/include/OSL/fmt_util.h
* /usr/include/OSL/genclosure.h
* /usr/include/OSL/hashes.h
* /usr/include/OSL/Imathx/Imathx.h
* /usr/include/OSL/journal.h
* /usr/include/OSL/llvm_util.h
* /usr/include/OSL/mask.h
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
* /usr/lib/liboslcomp.so.1.14
* /usr/lib/liboslcomp.so.1.14.6
* /usr/lib/liboslexec.so
* /usr/lib/liboslexec.so.1.14
* /usr/lib/liboslexec.so.1.14.6
* /usr/lib/liboslnoise.so
* /usr/lib/liboslnoise.so.1.14
* /usr/lib/liboslnoise.so.1.14.6
* /usr/lib/liboslquery.so
* /usr/lib/liboslquery.so.1.14
* /usr/lib/liboslquery.so.1.14.6
* /usr/lib/libtestshade.so
* /usr/lib/libtestshade.so.1.14
* /usr/lib/libtestshade.so.1.14.6
* /usr/lib/lib_b16_AVX512_noFMA_oslexec.so
* /usr/lib/lib_b16_AVX512_oslexec.so
* /usr/lib/lib_b4_SSE2_oslexec.so
* /usr/lib/lib_b8_AVX2_noFMA_oslexec.so
* /usr/lib/lib_b8_AVX2_oslexec.so
* /usr/lib/lib_b8_AVX512_noFMA_oslexec.so
* /usr/lib/lib_b8_AVX512_oslexec.so
* /usr/lib/lib_b8_AVX_oslexec.so
* /usr/lib/osl.imageio.so
* /usr/lib/pkgconfig/oslcomp.pc
* /usr/lib/pkgconfig/oslexec.pc
* /usr/lib/pkgconfig/oslquery.pc
* /usr/lib/python3.13/site-packages/oslquery/oslquery.cpython-313-x86_64-linux-gnu.so
* /usr/lib/python3.13/site-packages/oslquery/__init__.py
* /usr/share/doc/openshadinglanguage-1.14.6.0/INSTALL.md
* /usr/share/doc/openshadinglanguage-1.14.6.0/README.md
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
