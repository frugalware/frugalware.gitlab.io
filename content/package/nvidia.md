+++
draft = false
title = "nvidia 560.35.03-9"
version = "560.35.03-9"
description = "3D accelerated display driver for Nvidia cards"
date = "2024-10-13T23:25:30"
aliases = "/packages/3749"
categories = ['x11-extra']
upstreamurl = "http://www.nvidia.com/object/unix.html"
arch = "x86_64"
size = "112787964"
usize = "337321650"
sha1sum = "0608b2ffb52eba2f71e1e72d519f301ace10b6c5"
depends = "['kernel=6.11.3-2', 'libglvnd', 'nvidia-settings>=', 'nvidia-xconfig>=560.35.03']"
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
* /usr/lib/libcuda.so.560.35.03
* /usr/lib/libEGL_nvidia.so
* /usr/lib/libEGL_nvidia.so.0
* /usr/lib/libEGL_nvidia.so.560.35.03
* /usr/lib/libGLESv1_CM_nvidia.so
* /usr/lib/libGLESv1_CM_nvidia.so.1
* /usr/lib/libGLESv1_CM_nvidia.so.560.35.03
* /usr/lib/libGLESv2_nvidia.so
* /usr/lib/libGLESv2_nvidia.so.2
* /usr/lib/libGLESv2_nvidia.so.560.35.03
* /usr/lib/libGLX_nvidia.so
* /usr/lib/libGLX_nvidia.so.0
* /usr/lib/libGLX_nvidia.so.560.35.03
* /usr/lib/libnvcuvid.so
* /usr/lib/libnvcuvid.so.1
* /usr/lib/libnvcuvid.so.560.35.03
* /usr/lib/libnvidia-cfg.so
* /usr/lib/libnvidia-cfg.so.1
* /usr/lib/libnvidia-cfg.so.560.35.03
* /usr/lib/libnvidia-egl-wayland.so
* /usr/lib/libnvidia-egl-wayland.so.1
* /usr/lib/libnvidia-egl-wayland.so.1.1.13
* /usr/lib/libnvidia-eglcore.so
* /usr/lib/libnvidia-eglcore.so.560.35.03
* /usr/lib/libnvidia-encode.so
* /usr/lib/libnvidia-encode.so.1
* /usr/lib/libnvidia-encode.so.560.35.03
* /usr/lib/libnvidia-fbc.so
* /usr/lib/libnvidia-fbc.so.1
* /usr/lib/libnvidia-fbc.so.560.35.03
* /usr/lib/libnvidia-glcore.so
* /usr/lib/libnvidia-glcore.so.560.35.03
* /usr/lib/libnvidia-glsi.so
* /usr/lib/libnvidia-glsi.so.560.35.03
* /usr/lib/libnvidia-glvkspirv.so.560.35.03
* /usr/lib/libnvidia-gpucomp.so.560.35.03
* /usr/lib/libnvidia-gtk2.so.560.35.03
* /usr/lib/libnvidia-gtk3.so.560.35.03
* /usr/lib/libnvidia-ml.so
* /usr/lib/libnvidia-ml.so.1
* /usr/lib/libnvidia-ml.so.560.35.03
* /usr/lib/libnvidia-opencl.so.560.35.03
* /usr/lib/libnvidia-ptxjitcompiler.so
* /usr/lib/libnvidia-ptxjitcompiler.so.1
* /usr/lib/libnvidia-ptxjitcompiler.so.560.35.03
* /usr/lib/libnvidia-tls.so
* /usr/lib/libnvidia-tls.so.560.35.03
* /usr/lib/modules/6.11.3-fw2/kernel/drivers/video/nvidia-drm.ko.zst
* /usr/lib/modules/6.11.3-fw2/kernel/drivers/video/nvidia-modeset.ko.zst
* /usr/lib/modules/6.11.3-fw2/kernel/drivers/video/nvidia-uvm.ko.zst
* /usr/lib/modules/6.11.3-fw2/kernel/drivers/video/nvidia.ko.zst
* /usr/lib/vdpau/libvdpau_nvidia.so
* /usr/lib/vdpau/libvdpau_nvidia.so.1
* /usr/lib/vdpau/libvdpau_nvidia.so.1.0
* /usr/lib/vdpau/libvdpau_nvidia.so.560.35.03
* /usr/lib/xorg/modules/drivers/nvidia_drv.so
* /usr/lib/xorg/modules/nvidia/extensions/libglxserver_nvidia.so
* /usr/lib/xorg/modules/nvidia/extensions/libglxserver_nvidia.so.560.35.03
* /usr/share/doc/nvidia-560.35.03/html/acknowledgements.html
* /usr/share/doc/nvidia-560.35.03/html/addressingcapabilities.html
* /usr/share/doc/nvidia-560.35.03/html/addtlresources.html
* /usr/share/doc/nvidia-560.35.03/html/appendices.html
* /usr/share/doc/nvidia-560.35.03/html/audiosupport.html
* /usr/share/doc/nvidia-560.35.03/html/commonproblems.html
* /usr/share/doc/nvidia-560.35.03/html/configlaptop.html
* /usr/share/doc/nvidia-560.35.03/html/configmultxscreens.html
* /usr/share/doc/nvidia-560.35.03/html/configtwinview.html
* /usr/share/doc/nvidia-560.35.03/html/depth30.html
* /usr/share/doc/nvidia-560.35.03/html/displaydevicenames.html
* /usr/share/doc/nvidia-560.35.03/html/dma_issues.html
* /usr/share/doc/nvidia-560.35.03/html/dpi.html
* /usr/share/doc/nvidia-560.35.03/html/dynamicboost.html
* /usr/share/doc/nvidia-560.35.03/html/dynamicpowermanagement.html
* /usr/share/doc/nvidia-560.35.03/html/editxconfig.html
* /usr/share/doc/nvidia-560.35.03/html/egpu.html
* /usr/share/doc/nvidia-560.35.03/html/faq.html
* /usr/share/doc/nvidia-560.35.03/html/flippingubb.html
* /usr/share/doc/nvidia-560.35.03/html/framelock.html
* /usr/share/doc/nvidia-560.35.03/html/gbm.html
* /usr/share/doc/nvidia-560.35.03/html/glxsupport.html
* /usr/share/doc/nvidia-560.35.03/html/gpunames.html
* /usr/share/doc/nvidia-560.35.03/html/gsp.html
* /usr/share/doc/nvidia-560.35.03/html/i2c.html
* /usr/share/doc/nvidia-560.35.03/html/index.html
* /usr/share/doc/nvidia-560.35.03/html/installationandconfiguration.html
* /usr/share/doc/nvidia-560.35.03/html/installdriver.html
* /usr/share/doc/nvidia-560.35.03/html/installedcomponents.html
* /usr/share/doc/nvidia-560.35.03/html/introduction.html
* /usr/share/doc/nvidia-560.35.03/html/kernel_open.html
* /usr/share/doc/nvidia-560.35.03/html/kms.html
* /usr/share/doc/nvidia-560.35.03/html/knownissues.html
* /usr/share/doc/nvidia-560.35.03/html/minimumrequirements.html
* /usr/share/doc/nvidia-560.35.03/html/newusertips.html
* /usr/share/doc/nvidia-560.35.03/html/ngx.html
* /usr/share/doc/nvidia-560.35.03/html/nvidia-debugdump.html
* /usr/share/doc/nvidia-560.35.03/html/nvidia-ml.html
* /usr/share/doc/nvidia-560.35.03/html/nvidia-peermem.html
* /usr/share/doc/nvidia-560.35.03/html/nvidia-persistenced.html
* /usr/share/doc/nvidia-560.35.03/html/nvidia-smi.html
* /usr/share/doc/nvidia-560.35.03/html/nvidiasettings.html
* /usr/share/doc/nvidia-560.35.03/html/openglenvvariables.html
* /usr/share/doc/nvidia-560.35.03/html/optimus.html
* /usr/share/doc/nvidia-560.35.03/html/powermanagement.html
* /usr/share/doc/nvidia-560.35.03/html/primerenderoffload.html
* /usr/share/doc/nvidia-560.35.03/html/procinterface.html
* /usr/share/doc/nvidia-560.35.03/html/profiles.html
* /usr/share/doc/nvidia-560.35.03/html/programmingmodes.html
* /usr/share/doc/nvidia-560.35.03/html/randr14.html
* /usr/share/doc/nvidia-560.35.03/html/retpoline.html
* /usr/share/doc/nvidia-560.35.03/html/selectdriver.html
* /usr/share/doc/nvidia-560.35.03/html/sli.html
* /usr/share/doc/nvidia-560.35.03/html/supportedchips.html
* /usr/share/doc/nvidia-560.35.03/html/vdpausupport.html
* /usr/share/doc/nvidia-560.35.03/html/wayland-issues.html
* /usr/share/doc/nvidia-560.35.03/html/xcompositeextension.html
* /usr/share/doc/nvidia-560.35.03/html/xconfigoptions.html
* /usr/share/doc/nvidia-560.35.03/html/xineramaglx.html
* /usr/share/doc/nvidia-560.35.03/html/xrandrextension.html
* /usr/share/doc/nvidia-560.35.03/html/xwayland.html
* /usr/share/doc/nvidia-560.35.03/LICENSE
* /usr/share/doc/nvidia-560.35.03/README.txt
* /usr/share/egl/egl_external_platform.d/10_nvidia_wayland.json
* /usr/share/glvnd/egl_vendor.d/10_nvidia.json
* /usr/share/man/man1/nvidia-smi.1.gz
* /usr/share/nvidia/nvidia-application-profiles-560.35.03-key-documentation
* /usr/share/nvidia/nvidia-application-profiles-560.35.03-rc
* /usr/share/vulkan/icd.d/nvidia_icd.json
