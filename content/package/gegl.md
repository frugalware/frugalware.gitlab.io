+++
draft = false
title = "gegl 0.4.46-1"
version = "0.4.46-1"
date = "2023-09-01T08:25:47"
categories = ['xlib-extra']
upstreamurl = "http://www.gegl.org/"
arch = "x86_64"
size = "2734876"
usize = "14283324"
sha1sum = "a31272e9925262443f1203c25d3e5729ea803e3e"
depends = "['babl>=0.1.92', 'ffmpeg>=6.0', 'json-glib>=1.0.4-3', 'libraw>=0.21.1', 'openexr>=3.2.0', 'libwebp>=0.6.0', 'librsvg>=2.40.12-2', 'libjpeg-turbo', 'libtiff>=4.0.6', 'libffi>=3.2.1', 'libstdc++>=9.1.0-3', 'jasper>=2.0.10', 'suitesparse>=7.0.1', 'dejavu-ttf']"
files = "['usr/', 'usr/bin/', 'usr/bin/gegl', 'usr/bin/gegl-imgcmp', 'usr/include/', 'usr/include/gegl-0.4/', 'usr/include/gegl-0.4/gegl-apply.h', 'usr/include/gegl-0.4/gegl-audio-fragment.h', 'usr/include/gegl-0.4/gegl-buffer-backend.h', 'usr/include/gegl-0.4/gegl-buffer-enums.h', 'usr/include/gegl-0.4/gegl-buffer.h', 'usr/include/gegl-0.4/gegl-buffer-iterator.h', 'usr/include/gegl-0.4/gegl-buffer-matrix2.h', 'usr/include/gegl-0.4/gegl-buffer-swap.h', 'usr/include/gegl-0.4/gegl-color.h', 'usr/include/gegl-0.4/gegl-cpuaccel.h', 'usr/include/gegl-0.4/gegl-curve.h', 'usr/include/gegl-0.4/gegl-debug.h', 'usr/include/gegl-0.4/gegl-enums.h', 'usr/include/gegl-0.4/gegl-graph-debug.h', 'usr/include/gegl-0.4/gegl.h', 'usr/include/gegl-0.4/gegl-init.h', 'usr/include/gegl-0.4/gegl-lookup.h', 'usr/include/gegl-0.4/gegl-math.h', 'usr/include/gegl-0.4/gegl-matrix.h', 'usr/include/gegl-0.4/gegl-memory.h', 'usr/include/gegl-0.4/gegl-metadata.h', 'usr/include/gegl-0.4/gegl-metadatahash.h', 'usr/include/gegl-0.4/gegl-metadatastore.h', 'usr/include/gegl-0.4/gegl-node.h', 'usr/include/gegl-0.4/gegl-operations-util.h', 'usr/include/gegl-0.4/gegl-op.h', 'usr/include/gegl-0.4/gegl-parallel.h', 'usr/include/gegl-0.4/gegl-paramspecs.h', 'usr/include/gegl-0.4/gegl-path.h', 'usr/include/gegl-0.4/gegl-plugin.h', 'usr/include/gegl-0.4/gegl-processor.h', 'usr/include/gegl-0.4/gegl-random.h', 'usr/include/gegl-0.4/gegl-rectangle.h', 'usr/include/gegl-0.4/gegl-scratch.h', 'usr/include/gegl-0.4/gegl-tile-backend.h', 'usr/include/gegl-0.4/gegl-tile.h', 'usr/include/gegl-0.4/gegl-tile-handler.h', 'usr/include/gegl-0.4/gegl-tile-source.h', 'usr/include/gegl-0.4/gegl-types.h', 'usr/include/gegl-0.4/gegl-utils.h', 'usr/include/gegl-0.4/gegl-version.h', 'usr/include/gegl-0.4/npd/', 'usr/include/gegl-0.4/npd/deformation.h', 'usr/include/gegl-0.4/npd/graphics.h', 'usr/include/gegl-0.4/npd/lattice_cut.h', 'usr/include/gegl-0.4/npd/npd_common.h', 'usr/include/gegl-0.4/npd/npd_debug.h', 'usr/include/gegl-0.4/npd/npd_gegl.h', 'usr/include/gegl-0.4/npd/npd.h', 'usr/include/gegl-0.4/npd/npd_math.h', 'usr/include/gegl-0.4/opencl/', 'usr/include/gegl-0.4/opencl/cl_d3d10.h', 'usr/include/gegl-0.4/opencl/cl_ext.h', 'usr/include/gegl-0.4/opencl/cl_gl_ext.h', 'usr/include/gegl-0.4/opencl/cl_gl.h', 'usr/include/gegl-0.4/opencl/cl.h', 'usr/include/gegl-0.4/opencl/cl_platform.h', 'usr/include/gegl-0.4/opencl/gegl-cl-color.h', 'usr/include/gegl-0.4/opencl/gegl-cl.h', 'usr/include/gegl-0.4/opencl/gegl-cl-init.h', 'usr/include/gegl-0.4/opencl/gegl-cl-random.h', 'usr/include/gegl-0.4/opencl/gegl-cl-types.h', 'usr/include/gegl-0.4/opencl/opencl.h', 'usr/include/gegl-0.4/operation/', 'usr/include/gegl-0.4/operation/gegl-extension-handler.h', 'usr/include/gegl-0.4/operation/gegl-operation-area-filter.h', 'usr/include/gegl-0.4/operation/gegl-operation-composer3.h', 'usr/include/gegl-0.4/operation/gegl-operation-composer.h', 'usr/include/gegl-0.4/operation/gegl-operation-context.h', 'usr/include/gegl-0.4/operation/gegl-operation-filter.h', 'usr/include/gegl-0.4/operation/gegl-operation.h', 'usr/include/gegl-0.4/operation/gegl-operation-handlers.h', 'usr/include/gegl-0.4/operation/gegl-operation-meta.h', 'usr/include/gegl-0.4/operation/gegl-operation-meta-json.h', 'usr/include/gegl-0.4/operation/gegl-operation-point-composer3.h', 'usr/include/gegl-0.4/operation/gegl-operation-point-composer.h', 'usr/include/gegl-0.4/operation/gegl-operation-point-filter.h', 'usr/include/gegl-0.4/operation/gegl-operation-point-render.h', 'usr/include/gegl-0.4/operation/gegl-operation-property-keys.h', 'usr/include/gegl-0.4/operation/gegl-operation-sink.h', 'usr/include/gegl-0.4/operation/gegl-operation-source.h', 'usr/include/gegl-0.4/operation/gegl-operation-temporal.h', 'usr/include/gegl-0.4/sc/', 'usr/include/gegl-0.4/sc/sc-common.h', 'usr/include/gegl-0.4/sc/sc-context.h', 'usr/include/gegl-0.4/sc/sc-outline.h', 'usr/include/gegl-0.4/sc/sc-sample.h', 'usr/lib/', 'usr/lib/gegl-0.4/', 'usr/lib/gegl-0.4/dropshadow2.json', 'usr/lib/gegl-0.4/exr-load.so', 'usr/lib/gegl-0.4/exr-save.so', 'usr/lib/gegl-0.4/ff-load.so', 'usr/lib/gegl-0.4/ff-save.so', 'usr/lib/gegl-0.4/gegl-common-cxx.so', 'usr/lib/gegl-0.4/gegl-common-cxx-x86_64-v2.so', 'usr/lib/gegl-0.4/gegl-common-cxx-x86_64-v3.so', 'usr/lib/gegl-0.4/gegl-common-gpl3.so', 'usr/lib/gegl-0.4/gegl-common-gpl3-x86_64-v2.so', 'usr/lib/gegl-0.4/gegl-common-gpl3-x86_64-v3.so', 'usr/lib/gegl-0.4/gegl-common.so', 'usr/lib/gegl-0.4/gegl-common-x86_64-v2.so', 'usr/lib/gegl-0.4/gegl-common-x86_64-v3.so', 'usr/lib/gegl-0.4/gegl-core.so', 'usr/lib/gegl-0.4/gegl-generated.so', 'usr/lib/gegl-0.4/gegl-generated-x86_64-v2.so', 'usr/lib/gegl-0.4/gegl-generated-x86_64-v3.so', 'usr/lib/gegl-0.4/gegl-transformops-x86_64-v2.so', 'usr/lib/gegl-0.4/gegl-transformops-x86_64-v3.so', 'usr/lib/gegl-0.4/gif-load.so', 'usr/lib/gegl-0.4/grey2.json', 'usr/lib/gegl-0.4/jp2-load.so', 'usr/lib/gegl-0.4/jpg-load.so', 'usr/lib/gegl-0.4/jpg-save.so', 'usr/lib/gegl-0.4/lcms-from-profile.so', 'usr/lib/gegl-0.4/matting-levin.so', 'usr/lib/gegl-0.4/npd.so', 'usr/lib/gegl-0.4/npy-save.so', 'usr/lib/gegl-0.4/path.so', 'usr/lib/gegl-0.4/pixbuf-load.so', 'usr/lib/gegl-0.4/pixbuf-save.so', 'usr/lib/gegl-0.4/png-load.so', 'usr/lib/gegl-0.4/png-save.so', 'usr/lib/gegl-0.4/ppm-load.so', 'usr/lib/gegl-0.4/ppm-save.so', 'usr/lib/gegl-0.4/raw-load.so', 'usr/lib/gegl-0.4/rgbe-load.so', 'usr/lib/gegl-0.4/rgbe-save.so', 'usr/lib/gegl-0.4/sdl2-display.so', 'usr/lib/gegl-0.4/seamless-clone-compose.so', 'usr/lib/gegl-0.4/seamless-clone.so', 'usr/lib/gegl-0.4/svg-load.so', 'usr/lib/gegl-0.4/text.so', 'usr/lib/gegl-0.4/tiff-load.so', 'usr/lib/gegl-0.4/tiff-save.so', 'usr/lib/gegl-0.4/transformops.so', 'usr/lib/gegl-0.4/v4l.so', 'usr/lib/gegl-0.4/vector-fill.so', 'usr/lib/gegl-0.4/vector-stroke.so', 'usr/lib/gegl-0.4/webp-load.so', 'usr/lib/gegl-0.4/webp-save.so', 'usr/lib/girepository-1.0/', 'usr/lib/girepository-1.0/Gegl-0.4.typelib', 'usr/lib/libgegl-0.4.so', 'usr/lib/libgegl-0.4.so.0', 'usr/lib/libgegl-0.4.so.0.445.1', 'usr/lib/libgegl-npd-0.4.so', 'usr/lib/libgegl-sc-0.4.so', 'usr/lib/pkgconfig/', 'usr/lib/pkgconfig/gegl-0.4.pc', 'usr/lib/pkgconfig/gegl-sc-0.4.pc', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/gegl-0.4.46/', 'usr/share/doc/gegl-0.4.46/AUTHORS', 'usr/share/doc/gegl-0.4.46/COPYING', 'usr/share/doc/gegl-0.4.46/COPYING.LESSER', 'usr/share/doc/gegl-0.4.46/NEWS', 'usr/share/doc/gegl-0.4.46/README', 'usr/share/gir-1.0/', 'usr/share/gir-1.0/Gegl-0.4.gir', 'usr/share/locale/', 'usr/share/locale/bs/', 'usr/share/locale/bs/LC_MESSAGES/', 'usr/share/locale/bs/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/ca/', 'usr/share/locale/ca/LC_MESSAGES/', 'usr/share/locale/ca/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/da/', 'usr/share/locale/da/LC_MESSAGES/', 'usr/share/locale/da/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/de/', 'usr/share/locale/de/LC_MESSAGES/', 'usr/share/locale/de/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/el/', 'usr/share/locale/el/LC_MESSAGES/', 'usr/share/locale/el/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/en_GB/', 'usr/share/locale/en_GB/LC_MESSAGES/', 'usr/share/locale/en_GB/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/eo/', 'usr/share/locale/eo/LC_MESSAGES/', 'usr/share/locale/eo/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/es/', 'usr/share/locale/es/LC_MESSAGES/', 'usr/share/locale/es/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/eu/', 'usr/share/locale/eu/LC_MESSAGES/', 'usr/share/locale/eu/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/fr/', 'usr/share/locale/fr/LC_MESSAGES/', 'usr/share/locale/fr/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/gl/', 'usr/share/locale/gl/LC_MESSAGES/', 'usr/share/locale/gl/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/hr/', 'usr/share/locale/hr/LC_MESSAGES/', 'usr/share/locale/hr/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/id/', 'usr/share/locale/id/LC_MESSAGES/', 'usr/share/locale/id/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/is/', 'usr/share/locale/is/LC_MESSAGES/', 'usr/share/locale/is/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/it/', 'usr/share/locale/it/LC_MESSAGES/', 'usr/share/locale/it/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/ka/', 'usr/share/locale/kab/', 'usr/share/locale/kab/LC_MESSAGES/', 'usr/share/locale/kab/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/ka/LC_MESSAGES/', 'usr/share/locale/ka/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/ko/', 'usr/share/locale/ko/LC_MESSAGES/', 'usr/share/locale/ko/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/lv/', 'usr/share/locale/lv/LC_MESSAGES/', 'usr/share/locale/lv/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/mr/', 'usr/share/locale/mr/LC_MESSAGES/', 'usr/share/locale/mr/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/nb/', 'usr/share/locale/nb/LC_MESSAGES/', 'usr/share/locale/nb/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/ne/', 'usr/share/locale/ne/LC_MESSAGES/', 'usr/share/locale/ne/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/nl/', 'usr/share/locale/nl/LC_MESSAGES/', 'usr/share/locale/nl/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/oc/', 'usr/share/locale/oc/LC_MESSAGES/', 'usr/share/locale/oc/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/pl/', 'usr/share/locale/pl/LC_MESSAGES/', 'usr/share/locale/pl/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/pt/', 'usr/share/locale/pt_BR/', 'usr/share/locale/pt_BR/LC_MESSAGES/', 'usr/share/locale/pt_BR/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/pt/LC_MESSAGES/', 'usr/share/locale/pt/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/ro/', 'usr/share/locale/ro/LC_MESSAGES/', 'usr/share/locale/ro/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/ru/', 'usr/share/locale/ru/LC_MESSAGES/', 'usr/share/locale/ru/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/sk/', 'usr/share/locale/sk/LC_MESSAGES/', 'usr/share/locale/sk/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/sl/', 'usr/share/locale/sl/LC_MESSAGES/', 'usr/share/locale/sl/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/sr/', 'usr/share/locale/sr@latin/', 'usr/share/locale/sr@latin/LC_MESSAGES/', 'usr/share/locale/sr@latin/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/sr/LC_MESSAGES/', 'usr/share/locale/sr/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/sv/', 'usr/share/locale/sv/LC_MESSAGES/', 'usr/share/locale/sv/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/tr/', 'usr/share/locale/tr/LC_MESSAGES/', 'usr/share/locale/tr/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/uk/', 'usr/share/locale/uk/LC_MESSAGES/', 'usr/share/locale/uk/LC_MESSAGES/gegl-0.4.mo', 'usr/share/locale/zh_CN/', 'usr/share/locale/zh_CN/LC_MESSAGES/', 'usr/share/locale/zh_CN/LC_MESSAGES/gegl-0.4.mo']"
+++
GEGL is a graph based image processing framework.