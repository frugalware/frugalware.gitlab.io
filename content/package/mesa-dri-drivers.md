+++
draft = false
title = "mesa-dri-drivers 24.0.1-1"
version = "24.0.1-1"
description = "Mesa OpenGL DRI drivers."
date = "2024-02-17T22:37:07"
aliases = "/packages/136774"
categories = ['x11']
upstreamurl = "http://mesa3d.sourceforge.net/"
arch = "x86_64"
size = "15089368"
usize = "58182221"
sha1sum = "638448d620b43b13747ed4fff4b10ce9e60a242a"
depends = "['elfutils>=0.167-2', 'expat>=2.1.0-6', 'libdrm>=2.4.71', 'libffi>=3.2.1-2', 'libunwind', 'llvm-libs>=17.0.6', 'lmsensors>=3.5.0', 'zstd']"
reverse_depends = "['libgl', 'virtualbox-guest-additions', 'xorg-server']"
+++
Mesa OpenGL DRI drivers."

{{< files text="show files" >}}* /usr/include/GL/internal/dri_interface.h
* /usr/lib/dri/crocus_dri.so
* /usr/lib/dri/d3d12_dri.so
* /usr/lib/dri/d3d12_drv_video.so
* /usr/lib/dri/i915_dri.so
* /usr/lib/dri/iris_dri.so
* /usr/lib/dri/kms_swrast_dri.so
* /usr/lib/dri/nouveau_dri.so
* /usr/lib/dri/r300_dri.so
* /usr/lib/dri/r600_dri.so
* /usr/lib/dri/radeonsi_dri.so
* /usr/lib/dri/swrast_dri.so
* /usr/lib/dri/virtio_gpu_dri.so
* /usr/lib/dri/virtio_gpu_drv_video.so
* /usr/lib/dri/vmwgfx_dri.so
* /usr/lib/dri/zink_dri.so
* /usr/lib/pkgconfig/dri.pc
* /usr/share/drirc.d/00-mesa-defaults.conf
* /usr/share/drirc.d/00-radv-defaults.conf
{{< /files >}}