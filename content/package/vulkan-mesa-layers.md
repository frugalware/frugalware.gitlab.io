+++
draft = false
title = "vulkan-mesa-layers 24.0.1-1"
version = "24.0.1-1"
description = "Mesa Vulkan layers"
date = "2024-02-17T22:37:07"
aliases = "/packages/220464"
categories = ['x11-extra']
upstreamurl = "http://mesa3d.sourceforge.net/"
arch = "x86_64"
size = "284924"
usize = "701252"
sha1sum = "4966aa365ea2b914ae0c5afafebaf8641793ab79"
depends = "['lib32-wayland', 'libdrm', 'libxcb']"
reverse_depends = "['lib32-vulkan-mesa-layers']"
+++
Mesa Vulkan layers"

{{< files text="show files" >}}* /usr/bin/mesa-overlay-control.py
* /usr/lib/libVkLayer_INTEL_nullhw.so
* /usr/lib/libVkLayer_MESA_device_select.so
* /usr/lib/libVkLayer_MESA_overlay.so
* /usr/share/vulkan/explicit_layer.d/VkLayer_INTEL_nullhw.json
* /usr/share/vulkan/explicit_layer.d/VkLayer_MESA_overlay.json
* /usr/share/vulkan/icd.d/virtio_icd.i686.json
* /usr/share/vulkan/icd.d/virtio_icd.x86_64.json
* /usr/share/vulkan/implicit_layer.d/VkLayer_MESA_device_select.json
{{< /files >}}