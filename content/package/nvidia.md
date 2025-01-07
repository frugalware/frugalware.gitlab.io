+++
draft = false
title = "nvidia 565.77-6"
version = "565.77-6"
description = "3D accelerated display driver for Nvidia cards"
date = "2025-01-03T11:14:31"
aliases = "/packages/3749"
categories = ['x11-extra']
upstreamurl = "http://www.nvidia.com/object/unix.html"
arch = "x86_64"
size = "124306712"
usize = "389827886"
sha1sum = "3ba6a1ef24ca316d57525a08afac4120f4673247"
depends = "['kernel=6.12.8-1', 'libglvnd', 'nvidia-settings>=', 'nvidia-xconfig>=565.77']"
reverse_depends = "['cuda', 'lib32-nvidia']"
+++
### Description: 
3D accelerated display driver for Nvidia cards

### Files: 
* /etc/modprobe.d/nvidia.conf
* /etc/OpenCL/vendors/nvidia.icd
* /etc/X11/xorg.conf.d/15-nvidia.conf
* /usr/bin/nvidia-bug-report.sh
* /usr/bin/nvidia-smi
* /usr/lib/libcuda.so
* /usr/lib/libcuda.so.1
* /usr/lib/libcuda.so.565.77
* /usr/lib/libEGL_nvidia.so
* /usr/lib/libEGL_nvidia.so.0
* /usr/lib/libEGL_nvidia.so.565.77
* /usr/lib/libGLESv1_CM_nvidia.so
* /usr/lib/libGLESv1_CM_nvidia.so.1
* /usr/lib/libGLESv1_CM_nvidia.so.565.77
* /usr/lib/libGLESv2_nvidia.so
* /usr/lib/libGLESv2_nvidia.so.2
* /usr/lib/libGLESv2_nvidia.so.565.77
* /usr/lib/libGLX_nvidia.so
* /usr/lib/libGLX_nvidia.so.0
* /usr/lib/libGLX_nvidia.so.565.77
* /usr/lib/libnvcuvid.so
* /usr/lib/libnvcuvid.so.1
* /usr/lib/libnvcuvid.so.565.77
* /usr/lib/libnvidia-cfg.so
* /usr/lib/libnvidia-cfg.so.1
* /usr/lib/libnvidia-cfg.so.565.77
* /usr/lib/libnvidia-egl-wayland.so
* /usr/lib/libnvidia-egl-wayland.so.1
* /usr/lib/libnvidia-egl-wayland.so.1.1.17
* /usr/lib/libnvidia-eglcore.so
* /usr/lib/libnvidia-eglcore.so.565.77
* /usr/lib/libnvidia-encode.so
* /usr/lib/libnvidia-encode.so.1
* /usr/lib/libnvidia-encode.so.565.77
* /usr/lib/libnvidia-fbc.so
* /usr/lib/libnvidia-fbc.so.1
* /usr/lib/libnvidia-fbc.so.565.77
* /usr/lib/libnvidia-glcore.so
* /usr/lib/libnvidia-glcore.so.565.77
* /usr/lib/libnvidia-glsi.so
* /usr/lib/libnvidia-glsi.so.565.77
* /usr/lib/libnvidia-glvkspirv.so.565.77
* /usr/lib/libnvidia-gpucomp.so.565.77
* /usr/lib/libnvidia-gtk2.so.565.77
* /usr/lib/libnvidia-gtk3.so.565.77
* /usr/lib/libnvidia-ml.so
* /usr/lib/libnvidia-ml.so.1
* /usr/lib/libnvidia-ml.so.565.77
* /usr/lib/libnvidia-opencl.so.565.77
* /usr/lib/libnvidia-ptxjitcompiler.so
* /usr/lib/libnvidia-ptxjitcompiler.so.1
* /usr/lib/libnvidia-ptxjitcompiler.so.565.77
* /usr/lib/libnvidia-tls.so
* /usr/lib/libnvidia-tls.so.565.77
* /usr/lib/modules/6.12.8-fw1/kernel/drivers/video/nvidia-drm.ko.zst
* /usr/lib/modules/6.12.8-fw1/kernel/drivers/video/nvidia-modeset.ko.zst
* /usr/lib/modules/6.12.8-fw1/kernel/drivers/video/nvidia-uvm.ko.zst
* /usr/lib/modules/6.12.8-fw1/kernel/drivers/video/nvidia.ko.zst
* /usr/lib/vdpau/libvdpau_nvidia.so
* /usr/lib/vdpau/libvdpau_nvidia.so.1
* /usr/lib/vdpau/libvdpau_nvidia.so.1.0
* /usr/lib/vdpau/libvdpau_nvidia.so.565.77
* /usr/lib/xorg/modules/drivers/nvidia_drv.so
* /usr/lib/xorg/modules/nvidia/extensions/libglxserver_nvidia.so
* /usr/lib/xorg/modules/nvidia/extensions/libglxserver_nvidia.so.565.77
* /usr/share/doc/nvidia-565.77/html/acknowledgements.html
* /usr/share/doc/nvidia-565.77/html/addressingcapabilities.html
* /usr/share/doc/nvidia-565.77/html/addtlresources.html
* /usr/share/doc/nvidia-565.77/html/appendices.html
* /usr/share/doc/nvidia-565.77/html/audiosupport.html
* /usr/share/doc/nvidia-565.77/html/commonproblems.html
* /usr/share/doc/nvidia-565.77/html/configlaptop.html
* /usr/share/doc/nvidia-565.77/html/configmultxscreens.html
* /usr/share/doc/nvidia-565.77/html/configtwinview.html
* /usr/share/doc/nvidia-565.77/html/depth30.html
* /usr/share/doc/nvidia-565.77/html/displaydevicenames.html
* /usr/share/doc/nvidia-565.77/html/dma_issues.html
* /usr/share/doc/nvidia-565.77/html/dpi.html
* /usr/share/doc/nvidia-565.77/html/dynamicboost.html
* /usr/share/doc/nvidia-565.77/html/dynamicpowermanagement.html
* /usr/share/doc/nvidia-565.77/html/editxconfig.html
* /usr/share/doc/nvidia-565.77/html/egpu.html
* /usr/share/doc/nvidia-565.77/html/faq.html
* /usr/share/doc/nvidia-565.77/html/flippingubb.html
* /usr/share/doc/nvidia-565.77/html/framelock.html
* /usr/share/doc/nvidia-565.77/html/gbm.html
* /usr/share/doc/nvidia-565.77/html/glxsupport.html
* /usr/share/doc/nvidia-565.77/html/gpunames.html
* /usr/share/doc/nvidia-565.77/html/gsp.html
* /usr/share/doc/nvidia-565.77/html/i2c.html
* /usr/share/doc/nvidia-565.77/html/index.html
* /usr/share/doc/nvidia-565.77/html/installationandconfiguration.html
* /usr/share/doc/nvidia-565.77/html/installdriver.html
* /usr/share/doc/nvidia-565.77/html/installedcomponents.html
* /usr/share/doc/nvidia-565.77/html/introduction.html
* /usr/share/doc/nvidia-565.77/html/kernel_open.html
* /usr/share/doc/nvidia-565.77/html/kms.html
* /usr/share/doc/nvidia-565.77/html/knownissues.html
* /usr/share/doc/nvidia-565.77/html/minimumrequirements.html
* /usr/share/doc/nvidia-565.77/html/newusertips.html
* /usr/share/doc/nvidia-565.77/html/ngx.html
* /usr/share/doc/nvidia-565.77/html/nvidia-debugdump.html
* /usr/share/doc/nvidia-565.77/html/nvidia-ml.html
* /usr/share/doc/nvidia-565.77/html/nvidia-peermem.html
* /usr/share/doc/nvidia-565.77/html/nvidia-persistenced.html
* /usr/share/doc/nvidia-565.77/html/nvidia-smi.html
* /usr/share/doc/nvidia-565.77/html/nvidiasettings.html
* /usr/share/doc/nvidia-565.77/html/openglenvvariables.html
* /usr/share/doc/nvidia-565.77/html/optimus.html
* /usr/share/doc/nvidia-565.77/html/powermanagement.html
* /usr/share/doc/nvidia-565.77/html/primerenderoffload.html
* /usr/share/doc/nvidia-565.77/html/procinterface.html
* /usr/share/doc/nvidia-565.77/html/profiles.html
* /usr/share/doc/nvidia-565.77/html/programmingmodes.html
* /usr/share/doc/nvidia-565.77/html/randr14.html
* /usr/share/doc/nvidia-565.77/html/retpoline.html
* /usr/share/doc/nvidia-565.77/html/selectdriver.html
* /usr/share/doc/nvidia-565.77/html/sli.html
* /usr/share/doc/nvidia-565.77/html/supportedchips.html
* /usr/share/doc/nvidia-565.77/html/vdpausupport.html
* /usr/share/doc/nvidia-565.77/html/wayland-issues.html
* /usr/share/doc/nvidia-565.77/html/xcompositeextension.html
* /usr/share/doc/nvidia-565.77/html/xconfigoptions.html
* /usr/share/doc/nvidia-565.77/html/xineramaglx.html
* /usr/share/doc/nvidia-565.77/html/xrandrextension.html
* /usr/share/doc/nvidia-565.77/html/xwayland.html
* /usr/share/doc/nvidia-565.77/LICENSE
* /usr/share/doc/nvidia-565.77/README.txt
* /usr/share/egl/egl_external_platform.d/10_nvidia_wayland.json
* /usr/share/glvnd/egl_vendor.d/10_nvidia.json
* /usr/share/man/man1/nvidia-smi.1.gz
* /usr/share/nvidia/nvidia-application-profiles-565.77-key-documentation
* /usr/share/nvidia/nvidia-application-profiles-565.77-rc
* /usr/share/vulkan/icd.d/nvidia_icd.json
