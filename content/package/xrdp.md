+++
draft = false
title = "xrdp 0.10.2-1"
version = "0.10.2-1"
description = "RDP Server - An open source RDP server and X server capable of accepting connections from rdesktop and ms terminal server clients."
date = "2025-02-13T21:05:36"
aliases = "/packages/136338"
categories = ['xapps-extra']
upstreamurl = "https://github.com/neutrinolabs/xrdp"
arch = "x86_64"
size = "532900"
usize = "3510558"
sha1sum = "c15a23cd955bf47f0d3d3598c6c009e11fe408cd"
depends = "['fuse3', 'libjpeg-turbo', 'libx11', 'libxau', 'libxcb', 'libxdmcp', 'libxext', 'libxfixes', 'libxrandr', 'libxrender', 'openssl>=3.1.0', 'opus', 'pam']"
+++
### Description: 
RDP Server - An open source RDP server and X server capable of accepting connections from rdesktop and ms terminal server clients.

### Files: 
* /etc/default/xrdp
* /etc/init.d/xrdp
* /etc/pam.d/xrdp-sesman
* /etc/xrdp/cert.pem
* /etc/xrdp/gfx.toml
* /etc/xrdp/key.pem
* /etc/xrdp/km-00000405.ini
* /etc/xrdp/km-00000406.ini
* /etc/xrdp/km-00000407.ini
* /etc/xrdp/km-00000409.ini
* /etc/xrdp/km-0000040a.ini
* /etc/xrdp/km-0000040b.ini
* /etc/xrdp/km-0000040c.ini
* /etc/xrdp/km-00000410.ini
* /etc/xrdp/km-00000411.ini
* /etc/xrdp/km-00000412.ini
* /etc/xrdp/km-00000414.ini
* /etc/xrdp/km-00000415.ini
* /etc/xrdp/km-00000416.ini
* /etc/xrdp/km-00000419.ini
* /etc/xrdp/km-0000041d.ini
* /etc/xrdp/km-00000807.ini
* /etc/xrdp/km-00000809.ini
* /etc/xrdp/km-0000080a.ini
* /etc/xrdp/km-0000080c.ini
* /etc/xrdp/km-00000813.ini
* /etc/xrdp/km-00000816.ini
* /etc/xrdp/km-0000100c.ini
* /etc/xrdp/km-00010409.ini
* /etc/xrdp/km-19360409.ini
* /etc/xrdp/pulse/default.pa
* /etc/xrdp/reconnectwm.sh
* /etc/xrdp/rsakeys.ini
* /etc/xrdp/sesman.ini
* /etc/xrdp/startwm.sh
* /etc/xrdp/xrdp.ini
* /etc/xrdp/xrdp_keyboard.ini
* /usr/bin/xrdp
* /usr/bin/xrdp-chansrv
* /usr/bin/xrdp-dis
* /usr/bin/xrdp-dumpfv1
* /usr/bin/xrdp-genkeymap
* /usr/bin/xrdp-keygen
* /usr/bin/xrdp-sesadmin
* /usr/bin/xrdp-sesman
* /usr/bin/xrdp-sesrun
* /usr/include/ms-erref.h
* /usr/include/ms-fscc.h
* /usr/include/ms-rdpbcgr.h
* /usr/include/ms-rdpeclip.h
* /usr/include/ms-rdpedisp.h
* /usr/include/ms-rdpefs.h
* /usr/include/ms-rdpegdi.h
* /usr/include/ms-rdpele.h
* /usr/include/ms-rdperp.h
* /usr/include/ms-smb2.h
* /usr/include/painter.h
* /usr/include/rfxcodec_common.h
* /usr/include/rfxcodec_decode.h
* /usr/include/rfxcodec_encode.h
* /usr/include/xrdp_client_info.h
* /usr/include/xrdp_constants.h
* /usr/include/xrdp_rail.h
* /usr/include/xrdp_sockets.h
* /usr/lib/pkgconfig/libpainter.pc
* /usr/lib/pkgconfig/rfxcodec.pc
* /usr/lib/pkgconfig/xrdp.pc
* /usr/lib/xrdp/libcommon.so
* /usr/lib/xrdp/libcommon.so.0
* /usr/lib/xrdp/libcommon.so.0.0.0
* /usr/lib/xrdp/libipm.so
* /usr/lib/xrdp/libipm.so.0
* /usr/lib/xrdp/libipm.so.0.0.0
* /usr/lib/xrdp/libmc.so
* /usr/lib/xrdp/libsesman.so
* /usr/lib/xrdp/libsesman.so.0
* /usr/lib/xrdp/libsesman.so.0.0.0
* /usr/lib/xrdp/libtoml.so
* /usr/lib/xrdp/libtoml.so.1
* /usr/lib/xrdp/libtoml.so.1.0.0
* /usr/lib/xrdp/libvnc.so
* /usr/lib/xrdp/libxrdp.so
* /usr/lib/xrdp/libxrdp.so.0
* /usr/lib/xrdp/libxrdp.so.0.0.0
* /usr/lib/xrdp/libxrdpapi.so
* /usr/lib/xrdp/libxrdpapi.so.0
* /usr/lib/xrdp/libxrdpapi.so.0.0.0
* /usr/lib/xrdp/libxup.so
* /usr/lib/xrdp/xrdp/waitforx
* /usr/lib/xrdp/xrdp/xrdp-droppriv
* /usr/lib/xrdp/xrdp/xrdp-sesexec
* /usr/share/doc/xrdp-0.10.2/COPYING
* /usr/share/doc/xrdp-0.10.2/README.md
* /usr/share/man/man1/xrdp-dis.1.gz
* /usr/share/man/man5/gfx.toml.5.gz
* /usr/share/man/man5/sesman.ini.5.gz
* /usr/share/man/man5/xrdp.ini.5.gz
* /usr/share/man/man8/xrdp-chansrv.8.gz
* /usr/share/man/man8/xrdp-dumpfv1.8.gz
* /usr/share/man/man8/xrdp-genkeymap.8.gz
* /usr/share/man/man8/xrdp-keygen.8.gz
* /usr/share/man/man8/xrdp-sesadmin.8.gz
* /usr/share/man/man8/xrdp-sesman.8.gz
* /usr/share/man/man8/xrdp-sesrun.8.gz
* /usr/share/man/man8/xrdp.8.gz
* /usr/share/xrdp/ad24b.bmp
* /usr/share/xrdp/ad256.bmp
* /usr/share/xrdp/cursor0.cur
* /usr/share/xrdp/cursor1.cur
* /usr/share/xrdp/README.logo
* /usr/share/xrdp/sans-10.fv1
* /usr/share/xrdp/sans-18.fv1
* /usr/share/xrdp/xrdp-chkpriv
* /usr/share/xrdp/xrdp24b.bmp
* /usr/share/xrdp/xrdp256.bmp
* /usr/share/xrdp/xrdp_logo.bmp
* /usr/share/xrdp/xrdp_logo.png
