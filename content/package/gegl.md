+++
draft = false
title = "gegl 0.4.52-1"
version = "0.4.52-1"
description = "GEGL is a graph based image processing framework."
date = "2025-01-03T13:17:23"
aliases = "/packages/38778"
categories = ['xlib-extra']
upstreamurl = "http://www.gegl.org/"
arch = "x86_64"
size = "1852632"
usize = "9659611"
sha1sum = "312527e131cf532366730ce04083231f0c82970d"
depends = "['babl>=0.1.92', 'dejavu-ttf', 'ffmpeg>=7.0', 'jasper>=2.0.10', 'json-glib>=1.0.4-3', 'libffi>=3.2.1', 'libjpeg-turbo', 'libraw>=0.21.1', 'librsvg>=2.40.12-2', 'libstdc++>=9.1.0-3', 'libtiff>=4.0.6', 'libwebp>=0.6.0', 'openexr>=3.3.0', 'suitesparse>=7.0.1']"
reverse_depends = "['gimp', 'libmypaint']"
+++
### Description: 
GEGL is a graph based image processing framework.

### Files: 
* /usr/bin/gegl
* /usr/bin/gegl-imgcmp
* /usr/include/gegl-0.4/gegl-apply.h
* /usr/include/gegl-0.4/gegl-audio-fragment.h
* /usr/include/gegl-0.4/gegl-buffer-backend.h
* /usr/include/gegl-0.4/gegl-buffer-enums.h
* /usr/include/gegl-0.4/gegl-buffer-iterator.h
* /usr/include/gegl-0.4/gegl-buffer-matrix2.h
* /usr/include/gegl-0.4/gegl-buffer-swap.h
* /usr/include/gegl-0.4/gegl-buffer.h
* /usr/include/gegl-0.4/gegl-color.h
* /usr/include/gegl-0.4/gegl-cpuaccel.h
* /usr/include/gegl-0.4/gegl-curve.h
* /usr/include/gegl-0.4/gegl-debug.h
* /usr/include/gegl-0.4/gegl-enums.h
* /usr/include/gegl-0.4/gegl-graph-debug.h
* /usr/include/gegl-0.4/gegl-init.h
* /usr/include/gegl-0.4/gegl-lookup.h
* /usr/include/gegl-0.4/gegl-math.h
* /usr/include/gegl-0.4/gegl-matrix.h
* /usr/include/gegl-0.4/gegl-memory.h
* /usr/include/gegl-0.4/gegl-metadata.h
* /usr/include/gegl-0.4/gegl-metadatahash.h
* /usr/include/gegl-0.4/gegl-metadatastore.h
* /usr/include/gegl-0.4/gegl-node.h
* /usr/include/gegl-0.4/gegl-op.h
* /usr/include/gegl-0.4/gegl-operations-util.h
* /usr/include/gegl-0.4/gegl-parallel.h
* /usr/include/gegl-0.4/gegl-paramspecs.h
* /usr/include/gegl-0.4/gegl-path.h
* /usr/include/gegl-0.4/gegl-plugin.h
* /usr/include/gegl-0.4/gegl-processor.h
* /usr/include/gegl-0.4/gegl-random.h
* /usr/include/gegl-0.4/gegl-rectangle.h
* /usr/include/gegl-0.4/gegl-scratch.h
* /usr/include/gegl-0.4/gegl-tile-backend.h
* /usr/include/gegl-0.4/gegl-tile-handler.h
* /usr/include/gegl-0.4/gegl-tile-source.h
* /usr/include/gegl-0.4/gegl-tile.h
* /usr/include/gegl-0.4/gegl-types.h
* /usr/include/gegl-0.4/gegl-utils.h
* /usr/include/gegl-0.4/gegl-version.h
* /usr/include/gegl-0.4/gegl.h
* /usr/include/gegl-0.4/npd/deformation.h
* /usr/include/gegl-0.4/npd/graphics.h
* /usr/include/gegl-0.4/npd/lattice_cut.h
* /usr/include/gegl-0.4/npd/npd.h
* /usr/include/gegl-0.4/npd/npd_common.h
* /usr/include/gegl-0.4/npd/npd_debug.h
* /usr/include/gegl-0.4/npd/npd_gegl.h
* /usr/include/gegl-0.4/npd/npd_math.h
* /usr/include/gegl-0.4/opencl/cl.h
* /usr/include/gegl-0.4/opencl/cl_d3d10.h
* /usr/include/gegl-0.4/opencl/cl_d3d11.h
* /usr/include/gegl-0.4/opencl/cl_dx9_media_sharing.h
* /usr/include/gegl-0.4/opencl/cl_egl.h
* /usr/include/gegl-0.4/opencl/cl_ext.h
* /usr/include/gegl-0.4/opencl/cl_gl.h
* /usr/include/gegl-0.4/opencl/cl_half.h
* /usr/include/gegl-0.4/opencl/cl_icd.h
* /usr/include/gegl-0.4/opencl/cl_layer.h
* /usr/include/gegl-0.4/opencl/cl_platform.h
* /usr/include/gegl-0.4/opencl/cl_va_api_media_sharing_intel.h
* /usr/include/gegl-0.4/opencl/cl_version.h
* /usr/include/gegl-0.4/opencl/gegl-cl-color.h
* /usr/include/gegl-0.4/opencl/gegl-cl-init.h
* /usr/include/gegl-0.4/opencl/gegl-cl-random.h
* /usr/include/gegl-0.4/opencl/gegl-cl-types.h
* /usr/include/gegl-0.4/opencl/gegl-cl-version.h
* /usr/include/gegl-0.4/opencl/gegl-cl.h
* /usr/include/gegl-0.4/opencl/opencl.h
* /usr/include/gegl-0.4/opencl/opencl.hpp
* /usr/include/gegl-0.4/operation/gegl-extension-handler.h
* /usr/include/gegl-0.4/operation/gegl-operation-area-filter.h
* /usr/include/gegl-0.4/operation/gegl-operation-composer.h
* /usr/include/gegl-0.4/operation/gegl-operation-composer3.h
* /usr/include/gegl-0.4/operation/gegl-operation-context.h
* /usr/include/gegl-0.4/operation/gegl-operation-filter.h
* /usr/include/gegl-0.4/operation/gegl-operation-handlers.h
* /usr/include/gegl-0.4/operation/gegl-operation-meta-json.h
* /usr/include/gegl-0.4/operation/gegl-operation-meta.h
* /usr/include/gegl-0.4/operation/gegl-operation-point-composer.h
* /usr/include/gegl-0.4/operation/gegl-operation-point-composer3.h
* /usr/include/gegl-0.4/operation/gegl-operation-point-filter.h
* /usr/include/gegl-0.4/operation/gegl-operation-point-render.h
* /usr/include/gegl-0.4/operation/gegl-operation-property-keys.h
* /usr/include/gegl-0.4/operation/gegl-operation-sink.h
* /usr/include/gegl-0.4/operation/gegl-operation-source.h
* /usr/include/gegl-0.4/operation/gegl-operation-temporal.h
* /usr/include/gegl-0.4/operation/gegl-operation.h
* /usr/include/gegl-0.4/sc/sc-common.h
* /usr/include/gegl-0.4/sc/sc-context.h
* /usr/include/gegl-0.4/sc/sc-outline.h
* /usr/include/gegl-0.4/sc/sc-sample.h
* /usr/lib/gegl-0.4/dropshadow2.json
* /usr/lib/gegl-0.4/exr-load.so
* /usr/lib/gegl-0.4/exr-save.so
* /usr/lib/gegl-0.4/ff-load.so
* /usr/lib/gegl-0.4/ff-save.so
* /usr/lib/gegl-0.4/gegl-common-cxx-x86_64-v2.so
* /usr/lib/gegl-0.4/gegl-common-cxx-x86_64-v3.so
* /usr/lib/gegl-0.4/gegl-common-cxx.so
* /usr/lib/gegl-0.4/gegl-common-gpl3-x86_64-v2.so
* /usr/lib/gegl-0.4/gegl-common-gpl3-x86_64-v3.so
* /usr/lib/gegl-0.4/gegl-common-gpl3.so
* /usr/lib/gegl-0.4/gegl-common-x86_64-v2.so
* /usr/lib/gegl-0.4/gegl-common-x86_64-v3.so
* /usr/lib/gegl-0.4/gegl-common.so
* /usr/lib/gegl-0.4/gegl-core.so
* /usr/lib/gegl-0.4/gegl-generated-x86_64-v2.so
* /usr/lib/gegl-0.4/gegl-generated-x86_64-v3.so
* /usr/lib/gegl-0.4/gegl-generated.so
* /usr/lib/gegl-0.4/gegl-transformops-x86_64-v2.so
* /usr/lib/gegl-0.4/gegl-transformops-x86_64-v3.so
* /usr/lib/gegl-0.4/gif-load.so
* /usr/lib/gegl-0.4/grey2.json
* /usr/lib/gegl-0.4/jp2-load.so
* /usr/lib/gegl-0.4/jpg-load.so
* /usr/lib/gegl-0.4/jpg-save.so
* /usr/lib/gegl-0.4/lcms-from-profile.so
* /usr/lib/gegl-0.4/matting-levin.so
* /usr/lib/gegl-0.4/npd.so
* /usr/lib/gegl-0.4/npy-save.so
* /usr/lib/gegl-0.4/path.so
* /usr/lib/gegl-0.4/pixbuf-load.so
* /usr/lib/gegl-0.4/pixbuf-save.so
* /usr/lib/gegl-0.4/png-load.so
* /usr/lib/gegl-0.4/png-save.so
* /usr/lib/gegl-0.4/ppm-load.so
* /usr/lib/gegl-0.4/ppm-save.so
* /usr/lib/gegl-0.4/raw-load.so
* /usr/lib/gegl-0.4/rgbe-load.so
* /usr/lib/gegl-0.4/rgbe-save.so
* /usr/lib/gegl-0.4/sdl2-display.so
* /usr/lib/gegl-0.4/seamless-clone-compose.so
* /usr/lib/gegl-0.4/seamless-clone.so
* /usr/lib/gegl-0.4/svg-load.so
* /usr/lib/gegl-0.4/text.so
* /usr/lib/gegl-0.4/tiff-load.so
* /usr/lib/gegl-0.4/tiff-save.so
* /usr/lib/gegl-0.4/transformops.so
* /usr/lib/gegl-0.4/v4l.so
* /usr/lib/gegl-0.4/vector-fill.so
* /usr/lib/gegl-0.4/vector-stroke.so
* /usr/lib/gegl-0.4/webp-load.so
* /usr/lib/gegl-0.4/webp-save.so
* /usr/lib/girepository-1.0/Gegl-0.4.typelib
* /usr/lib/libgegl-0.4.so
* /usr/lib/libgegl-0.4.so.0
* /usr/lib/libgegl-0.4.so.0.451.1
* /usr/lib/libgegl-npd-0.4.so
* /usr/lib/libgegl-sc-0.4.so
* /usr/lib/pkgconfig/gegl-0.4.pc
* /usr/lib/pkgconfig/gegl-sc-0.4.pc
* /usr/share/doc/gegl-0.4.52/AUTHORS
* /usr/share/doc/gegl-0.4.52/COPYING
* /usr/share/doc/gegl-0.4.52/COPYING.LESSER
* /usr/share/doc/gegl-0.4.52/NEWS
* /usr/share/doc/gegl-0.4.52/README
* /usr/share/gir-1.0/Gegl-0.4.gir
