+++
draft = false
title = "nvidia 570.86.16-1"
version = "570.86.16-1"
description = "3D accelerated display driver for Nvidia cards"
date = "2025-01-31T09:44:27"
aliases = "/packages/3749"
categories = ['x11-extra']
upstreamurl = "http://www.nvidia.com/object/unix.html"
arch = "x86_64"
size = "67730876"
usize = "394785761"
sha1sum = "ad73beb83a1b1c4e236c2893b5d2b3704349277f"
depends = "['libglvnd', 'nvidia-settings>=', 'nvidia-xconfig>=570.86.16', 'open-gpu-kernel-modules>=']"
reverse_depends = "['cuda', 'lib32-nvidia']"
+++
### Description: 
3D accelerated display driver for Nvidia cards

### Files: 
* /etc/OpenCL/vendors/nvidia.icd
* /etc/X11/xorg.conf.d/15-nvidia.conf
* /usr/bin/nvidia-bug-report.sh
* /usr/bin/nvidia-smi
* /usr/lib/libcuda.so
* /usr/lib/libcuda.so.1
* /usr/lib/libcuda.so.570.86.16
* /usr/lib/libEGL_nvidia.so
* /usr/lib/libEGL_nvidia.so.0
* /usr/lib/libEGL_nvidia.so.570.86.16
* /usr/lib/libGLESv1_CM_nvidia.so
* /usr/lib/libGLESv1_CM_nvidia.so.1
* /usr/lib/libGLESv1_CM_nvidia.so.570.86.16
* /usr/lib/libGLESv2_nvidia.so
* /usr/lib/libGLESv2_nvidia.so.2
* /usr/lib/libGLESv2_nvidia.so.570.86.16
* /usr/lib/libGLX_nvidia.so
* /usr/lib/libGLX_nvidia.so.0
* /usr/lib/libGLX_nvidia.so.570.86.16
* /usr/lib/libnvcuvid.so
* /usr/lib/libnvcuvid.so.1
* /usr/lib/libnvcuvid.so.570.86.16
* /usr/lib/libnvidia-cfg.so
* /usr/lib/libnvidia-cfg.so.1
* /usr/lib/libnvidia-cfg.so.570.86.16
* /usr/lib/libnvidia-egl-wayland.so
* /usr/lib/libnvidia-egl-wayland.so.1
* /usr/lib/libnvidia-egl-wayland.so.1.1.17
* /usr/lib/libnvidia-eglcore.so
* /usr/lib/libnvidia-eglcore.so.570.86.16
* /usr/lib/libnvidia-encode.so
* /usr/lib/libnvidia-encode.so.1
* /usr/lib/libnvidia-encode.so.570.86.16
* /usr/lib/libnvidia-fbc.so
* /usr/lib/libnvidia-fbc.so.1
* /usr/lib/libnvidia-fbc.so.570.86.16
* /usr/lib/libnvidia-glcore.so
* /usr/lib/libnvidia-glcore.so.570.86.16
* /usr/lib/libnvidia-glsi.so
* /usr/lib/libnvidia-glsi.so.570.86.16
* /usr/lib/libnvidia-glvkspirv.so.570.86.16
* /usr/lib/libnvidia-gpucomp.so.570.86.16
* /usr/lib/libnvidia-gtk2.so.570.86.16
* /usr/lib/libnvidia-gtk3.so.570.86.16
* /usr/lib/libnvidia-ml.so
* /usr/lib/libnvidia-ml.so.1
* /usr/lib/libnvidia-ml.so.570.86.16
* /usr/lib/libnvidia-opencl.so.570.86.16
* /usr/lib/libnvidia-ptxjitcompiler.so
* /usr/lib/libnvidia-ptxjitcompiler.so.1
* /usr/lib/libnvidia-ptxjitcompiler.so.570.86.16
* /usr/lib/libnvidia-tls.so
* /usr/lib/libnvidia-tls.so.570.86.16
* /usr/lib/vdpau/libvdpau_nvidia.so
* /usr/lib/vdpau/libvdpau_nvidia.so.1
* /usr/lib/vdpau/libvdpau_nvidia.so.1.0
* /usr/lib/vdpau/libvdpau_nvidia.so.570.86.16
* /usr/lib/xorg/modules/drivers/nvidia_drv.so
* /usr/lib/xorg/modules/nvidia/extensions/libglxserver_nvidia.so
* /usr/lib/xorg/modules/nvidia/extensions/libglxserver_nvidia.so.570.86.16
* /usr/share/doc/nvidia-570.86.16/html/acknowledgements.html
* /usr/share/doc/nvidia-570.86.16/html/addressingcapabilities.html
* /usr/share/doc/nvidia-570.86.16/html/addtlresources.html
* /usr/share/doc/nvidia-570.86.16/html/appendices.html
* /usr/share/doc/nvidia-570.86.16/html/audiosupport.html
* /usr/share/doc/nvidia-570.86.16/html/commonproblems.html
* /usr/share/doc/nvidia-570.86.16/html/configlaptop.html
* /usr/share/doc/nvidia-570.86.16/html/configmultxscreens.html
* /usr/share/doc/nvidia-570.86.16/html/configtwinview.html
* /usr/share/doc/nvidia-570.86.16/html/depth30.html
* /usr/share/doc/nvidia-570.86.16/html/displaydevicenames.html
* /usr/share/doc/nvidia-570.86.16/html/dma_issues.html
* /usr/share/doc/nvidia-570.86.16/html/dpi.html
* /usr/share/doc/nvidia-570.86.16/html/dynamicboost.html
* /usr/share/doc/nvidia-570.86.16/html/dynamicpowermanagement.html
* /usr/share/doc/nvidia-570.86.16/html/editxconfig.html
* /usr/share/doc/nvidia-570.86.16/html/egpu.html
* /usr/share/doc/nvidia-570.86.16/html/faq.html
* /usr/share/doc/nvidia-570.86.16/html/flippingubb.html
* /usr/share/doc/nvidia-570.86.16/html/framelock.html
* /usr/share/doc/nvidia-570.86.16/html/gbm.html
* /usr/share/doc/nvidia-570.86.16/html/glxsupport.html
* /usr/share/doc/nvidia-570.86.16/html/gpunames.html
* /usr/share/doc/nvidia-570.86.16/html/gsp.html
* /usr/share/doc/nvidia-570.86.16/html/i2c.html
* /usr/share/doc/nvidia-570.86.16/html/index.html
* /usr/share/doc/nvidia-570.86.16/html/installationandconfiguration.html
* /usr/share/doc/nvidia-570.86.16/html/installdriver.html
* /usr/share/doc/nvidia-570.86.16/html/installedcomponents.html
* /usr/share/doc/nvidia-570.86.16/html/introduction.html
* /usr/share/doc/nvidia-570.86.16/html/kernel_open.html
* /usr/share/doc/nvidia-570.86.16/html/kms.html
* /usr/share/doc/nvidia-570.86.16/html/knownissues.html
* /usr/share/doc/nvidia-570.86.16/html/minimumrequirements.html
* /usr/share/doc/nvidia-570.86.16/html/newusertips.html
* /usr/share/doc/nvidia-570.86.16/html/ngx.html
* /usr/share/doc/nvidia-570.86.16/html/nvidia-debugdump.html
* /usr/share/doc/nvidia-570.86.16/html/nvidia-ml.html
* /usr/share/doc/nvidia-570.86.16/html/nvidia-peermem.html
* /usr/share/doc/nvidia-570.86.16/html/nvidia-persistenced.html
* /usr/share/doc/nvidia-570.86.16/html/nvidia-smi.html
* /usr/share/doc/nvidia-570.86.16/html/nvidiasettings.html
* /usr/share/doc/nvidia-570.86.16/html/openglenvvariables.html
* /usr/share/doc/nvidia-570.86.16/html/optimus.html
* /usr/share/doc/nvidia-570.86.16/html/powermanagement.html
* /usr/share/doc/nvidia-570.86.16/html/primerenderoffload.html
* /usr/share/doc/nvidia-570.86.16/html/procinterface.html
* /usr/share/doc/nvidia-570.86.16/html/profiles.html
* /usr/share/doc/nvidia-570.86.16/html/programmingmodes.html
* /usr/share/doc/nvidia-570.86.16/html/randr14.html
* /usr/share/doc/nvidia-570.86.16/html/retpoline.html
* /usr/share/doc/nvidia-570.86.16/html/selectdriver.html
* /usr/share/doc/nvidia-570.86.16/html/sli.html
* /usr/share/doc/nvidia-570.86.16/html/supportedchips.html
* /usr/share/doc/nvidia-570.86.16/html/vdpausupport.html
* /usr/share/doc/nvidia-570.86.16/html/wayland-issues.html
* /usr/share/doc/nvidia-570.86.16/html/xcompositeextension.html
* /usr/share/doc/nvidia-570.86.16/html/xconfigoptions.html
* /usr/share/doc/nvidia-570.86.16/html/xineramaglx.html
* /usr/share/doc/nvidia-570.86.16/html/xrandrextension.html
* /usr/share/doc/nvidia-570.86.16/html/xwayland.html
* /usr/share/doc/nvidia-570.86.16/LICENSE
* /usr/share/doc/nvidia-570.86.16/README.txt
* /usr/share/egl/egl_external_platform.d/10_nvidia_wayland.json
* /usr/share/glvnd/egl_vendor.d/10_nvidia.json
* /usr/share/man/man1/nvidia-smi.1.gz
* /usr/share/nvidia/nvidia-application-profiles-570.86.16-key-documentation
* /usr/share/nvidia/nvidia-application-profiles-570.86.16-rc
* /usr/share/vulkan/icd.d/nvidia_icd.json
