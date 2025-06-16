+++
draft = false
title = "nvidia 575.57.08-1"
version = "575.57.08-1"
description = "3D accelerated display driver for Nvidia cards"
date = "2025-06-02T11:25:30"
aliases = "/packages/3749"
categories = ['x11-extra']
upstreamurl = "http://www.nvidia.com/object/unix.html"
arch = "x86_64"
size = "71919524"
usize = "449808599"
sha1sum = "a20056f0b8b6c84401be2bd24d0880970df836c0"
depends = "['libglvnd', 'nvidia-settings>=', 'nvidia-xconfig>=575.57.08', 'open-gpu-kernel-modules>=']"
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
* /usr/lib/libcuda.so.575.57.08
* /usr/lib/libEGL_nvidia.so
* /usr/lib/libEGL_nvidia.so.0
* /usr/lib/libEGL_nvidia.so.575.57.08
* /usr/lib/libGLESv1_CM_nvidia.so
* /usr/lib/libGLESv1_CM_nvidia.so.1
* /usr/lib/libGLESv1_CM_nvidia.so.575.57.08
* /usr/lib/libGLESv2_nvidia.so
* /usr/lib/libGLESv2_nvidia.so.2
* /usr/lib/libGLESv2_nvidia.so.575.57.08
* /usr/lib/libGLX_nvidia.so
* /usr/lib/libGLX_nvidia.so.0
* /usr/lib/libGLX_nvidia.so.575.57.08
* /usr/lib/libnvcuvid.so
* /usr/lib/libnvcuvid.so.1
* /usr/lib/libnvcuvid.so.575.57.08
* /usr/lib/libnvidia-cfg.so
* /usr/lib/libnvidia-cfg.so.1
* /usr/lib/libnvidia-cfg.so.575.57.08
* /usr/lib/libnvidia-egl-wayland.so
* /usr/lib/libnvidia-egl-wayland.so.1
* /usr/lib/libnvidia-egl-wayland.so.1.1.19
* /usr/lib/libnvidia-eglcore.so
* /usr/lib/libnvidia-eglcore.so.575.57.08
* /usr/lib/libnvidia-encode.so
* /usr/lib/libnvidia-encode.so.1
* /usr/lib/libnvidia-encode.so.575.57.08
* /usr/lib/libnvidia-fbc.so
* /usr/lib/libnvidia-fbc.so.1
* /usr/lib/libnvidia-fbc.so.575.57.08
* /usr/lib/libnvidia-glcore.so
* /usr/lib/libnvidia-glcore.so.575.57.08
* /usr/lib/libnvidia-glsi.so
* /usr/lib/libnvidia-glsi.so.575.57.08
* /usr/lib/libnvidia-glvkspirv.so.575.57.08
* /usr/lib/libnvidia-gpucomp.so.575.57.08
* /usr/lib/libnvidia-gtk2.so.575.57.08
* /usr/lib/libnvidia-gtk3.so.575.57.08
* /usr/lib/libnvidia-ml.so
* /usr/lib/libnvidia-ml.so.1
* /usr/lib/libnvidia-ml.so.575.57.08
* /usr/lib/libnvidia-opencl.so.575.57.08
* /usr/lib/libnvidia-ptxjitcompiler.so
* /usr/lib/libnvidia-ptxjitcompiler.so.1
* /usr/lib/libnvidia-ptxjitcompiler.so.575.57.08
* /usr/lib/libnvidia-tls.so
* /usr/lib/libnvidia-tls.so.575.57.08
* /usr/lib/vdpau/libvdpau_nvidia.so
* /usr/lib/vdpau/libvdpau_nvidia.so.1
* /usr/lib/vdpau/libvdpau_nvidia.so.1.0
* /usr/lib/vdpau/libvdpau_nvidia.so.575.57.08
* /usr/lib/xorg/modules/drivers/nvidia_drv.so
* /usr/lib/xorg/modules/nvidia/extensions/libglxserver_nvidia.so
* /usr/lib/xorg/modules/nvidia/extensions/libglxserver_nvidia.so.575.57.08
* /usr/share/doc/nvidia-575.57.08/html/acknowledgements.html
* /usr/share/doc/nvidia-575.57.08/html/addressingcapabilities.html
* /usr/share/doc/nvidia-575.57.08/html/addtlresources.html
* /usr/share/doc/nvidia-575.57.08/html/appendices.html
* /usr/share/doc/nvidia-575.57.08/html/audiosupport.html
* /usr/share/doc/nvidia-575.57.08/html/commonproblems.html
* /usr/share/doc/nvidia-575.57.08/html/configlaptop.html
* /usr/share/doc/nvidia-575.57.08/html/configmultxscreens.html
* /usr/share/doc/nvidia-575.57.08/html/configtwinview.html
* /usr/share/doc/nvidia-575.57.08/html/depth30.html
* /usr/share/doc/nvidia-575.57.08/html/displaydevicenames.html
* /usr/share/doc/nvidia-575.57.08/html/dma_issues.html
* /usr/share/doc/nvidia-575.57.08/html/dpi.html
* /usr/share/doc/nvidia-575.57.08/html/dynamicboost.html
* /usr/share/doc/nvidia-575.57.08/html/dynamicpowermanagement.html
* /usr/share/doc/nvidia-575.57.08/html/editxconfig.html
* /usr/share/doc/nvidia-575.57.08/html/egpu.html
* /usr/share/doc/nvidia-575.57.08/html/faq.html
* /usr/share/doc/nvidia-575.57.08/html/flippingubb.html
* /usr/share/doc/nvidia-575.57.08/html/framelock.html
* /usr/share/doc/nvidia-575.57.08/html/gbm.html
* /usr/share/doc/nvidia-575.57.08/html/glxsupport.html
* /usr/share/doc/nvidia-575.57.08/html/gpunames.html
* /usr/share/doc/nvidia-575.57.08/html/gsp.html
* /usr/share/doc/nvidia-575.57.08/html/i2c.html
* /usr/share/doc/nvidia-575.57.08/html/index.html
* /usr/share/doc/nvidia-575.57.08/html/installationandconfiguration.html
* /usr/share/doc/nvidia-575.57.08/html/installdriver.html
* /usr/share/doc/nvidia-575.57.08/html/installedcomponents.html
* /usr/share/doc/nvidia-575.57.08/html/introduction.html
* /usr/share/doc/nvidia-575.57.08/html/kernel_open.html
* /usr/share/doc/nvidia-575.57.08/html/kms.html
* /usr/share/doc/nvidia-575.57.08/html/knownissues.html
* /usr/share/doc/nvidia-575.57.08/html/minimumrequirements.html
* /usr/share/doc/nvidia-575.57.08/html/newusertips.html
* /usr/share/doc/nvidia-575.57.08/html/ngx.html
* /usr/share/doc/nvidia-575.57.08/html/nvidia-debugdump.html
* /usr/share/doc/nvidia-575.57.08/html/nvidia-ml.html
* /usr/share/doc/nvidia-575.57.08/html/nvidia-peermem.html
* /usr/share/doc/nvidia-575.57.08/html/nvidia-persistenced.html
* /usr/share/doc/nvidia-575.57.08/html/nvidia-smi.html
* /usr/share/doc/nvidia-575.57.08/html/nvidiasettings.html
* /usr/share/doc/nvidia-575.57.08/html/nvpresent.html
* /usr/share/doc/nvidia-575.57.08/html/openglenvvariables.html
* /usr/share/doc/nvidia-575.57.08/html/optimus.html
* /usr/share/doc/nvidia-575.57.08/html/powermanagement.html
* /usr/share/doc/nvidia-575.57.08/html/primerenderoffload.html
* /usr/share/doc/nvidia-575.57.08/html/procinterface.html
* /usr/share/doc/nvidia-575.57.08/html/profiles.html
* /usr/share/doc/nvidia-575.57.08/html/programmingmodes.html
* /usr/share/doc/nvidia-575.57.08/html/randr14.html
* /usr/share/doc/nvidia-575.57.08/html/retpoline.html
* /usr/share/doc/nvidia-575.57.08/html/selectdriver.html
* /usr/share/doc/nvidia-575.57.08/html/sli.html
* /usr/share/doc/nvidia-575.57.08/html/supportedchips.html
* /usr/share/doc/nvidia-575.57.08/html/vdpausupport.html
* /usr/share/doc/nvidia-575.57.08/html/wayland-issues.html
* /usr/share/doc/nvidia-575.57.08/html/xcompositeextension.html
* /usr/share/doc/nvidia-575.57.08/html/xconfigoptions.html
* /usr/share/doc/nvidia-575.57.08/html/xineramaglx.html
* /usr/share/doc/nvidia-575.57.08/html/xrandrextension.html
* /usr/share/doc/nvidia-575.57.08/html/xwayland.html
* /usr/share/doc/nvidia-575.57.08/LICENSE
* /usr/share/doc/nvidia-575.57.08/README.txt
* /usr/share/egl/egl_external_platform.d/10_nvidia_wayland.json
* /usr/share/glvnd/egl_vendor.d/10_nvidia.json
* /usr/share/man/man1/nvidia-smi.1.gz
* /usr/share/nvidia/nvidia-application-profiles-575.57.08-key-documentation
* /usr/share/nvidia/nvidia-application-profiles-575.57.08-rc
* /usr/share/vulkan/icd.d/nvidia_icd.json
