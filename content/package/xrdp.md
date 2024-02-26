+++
draft = false
title = "xrdp 0.9.24-1"
version = "0.9.24-1"
description = "RDP Server - An open source RDP server and X server capable of accepting connections from rdesktop and ms terminal server clients."
date = "2024-01-08T21:03:25"
aliases = "/packages/136338"
categories = ['xapps-extra']
upstreamurl = "https://github.com/neutrinolabs/xrdp"
arch = "x86_64"
size = "2188896"
usize = "4519576"
sha1sum = "c33d1b26d8000049fc3852a6a2710a2625a5a865"
depends = "['fuse', 'glibc', 'libjpeg-turbo', 'libx11', 'libxau', 'libxcb', 'libxdmcp', 'libxext', 'libxfixes', 'libxrandr', 'libxrender', 'openssl>=3.1.0', 'openssl>=3.1.0', 'opus', 'pam']"
+++
RDP Server - An open source RDP server and X server capable of accepting connections from rdesktop and ms terminal server clients.

{{< files text="show files" >}}* /etc/default/xrdp
* /etc/init.d/xrdp
* /etc/pam.d/xrdp-sesman
* /etc/xrdp/cert.pem
* /etc/xrdp/key.pem
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
* /usr/lib/libpainter.a
* /usr/lib/libpainter.la
* /usr/lib/libpainter.so
* /usr/lib/libpainter.so.0
* /usr/lib/libpainter.so.0.0.0
* /usr/lib/librfxencode.a
* /usr/lib/librfxencode.la
* /usr/lib/librfxencode.so
* /usr/lib/librfxencode.so.0
* /usr/lib/librfxencode.so.0.0.0
* /usr/lib/pkgconfig/libpainter.pc
* /usr/lib/pkgconfig/rfxcodec.pc
* /usr/lib/pkgconfig/xrdp.pc
* /usr/lib/xrdp/libcommon.a
* /usr/lib/xrdp/libcommon.la
* /usr/lib/xrdp/libcommon.so
* /usr/lib/xrdp/libcommon.so.0
* /usr/lib/xrdp/libcommon.so.0.0.0
* /usr/lib/xrdp/libmc.a
* /usr/lib/xrdp/libmc.la
* /usr/lib/xrdp/libmc.so
* /usr/lib/xrdp/libscp.a
* /usr/lib/xrdp/libscp.la
* /usr/lib/xrdp/libscp.so
* /usr/lib/xrdp/libscp.so.0
* /usr/lib/xrdp/libscp.so.0.0.0
* /usr/lib/xrdp/libvnc.a
* /usr/lib/xrdp/libvnc.la
* /usr/lib/xrdp/libvnc.so
* /usr/lib/xrdp/libxrdp.a
* /usr/lib/xrdp/libxrdp.la
* /usr/lib/xrdp/libxrdp.so
* /usr/lib/xrdp/libxrdp.so.0
* /usr/lib/xrdp/libxrdp.so.0.0.0
* /usr/lib/xrdp/libxrdpapi.a
* /usr/lib/xrdp/libxrdpapi.la
* /usr/lib/xrdp/libxrdpapi.so
* /usr/lib/xrdp/libxrdpapi.so.0
* /usr/lib/xrdp/libxrdpapi.so.0.0.0
* /usr/lib/xrdp/libxup.a
* /usr/lib/xrdp/libxup.la
* /usr/lib/xrdp/libxup.so
* /usr/share/doc/xrdp-0.9.24/COPYING
* /usr/share/doc/xrdp-0.9.24/README.md
* /usr/share/man/man1/xrdp-dis.1.gz
* /usr/share/man/man5/sesman.ini.5.gz
* /usr/share/man/man5/xrdp.ini.5.gz
* /usr/share/man/man8/xrdp-chansrv.8.gz
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
* /usr/share/xrdp/sans-10.fv1
* /usr/share/xrdp/xrdp24b.bmp
* /usr/share/xrdp/xrdp256.bmp
* /usr/share/xrdp/xrdp_logo.bmp
{{< /files >}}