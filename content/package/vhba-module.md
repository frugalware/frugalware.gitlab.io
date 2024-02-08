+++
draft = false
title = "vhba-module 20211218-140"
version = "20211218-140"
date = "2024-02-06T10:38:13"
categories = ['apps-extra']
upstreamurl = "https://sourceforge.net/projects/cdemu"
arch = "x86_64"
size = "41916"
usize = "33501"
sha1sum = "b7035e7e35f8cf2d0829abf395308894eb54f9f4"
depends = "['kernel=6.7.4-1']"
files = "['usr/', 'usr/lib/', 'usr/lib/modules/', 'usr/lib/modules/6.7.4-fw1/', 'usr/lib/modules/6.7.4-fw1/kernel/', 'usr/lib/modules/6.7.4-fw1/kernel/drivers/', 'usr/lib/modules/6.7.4-fw1/kernel/drivers/scsi/', 'usr/lib/modules/6.7.4-fw1/kernel/drivers/scsi/vhba.ko.zst', 'usr/lib/udev/', 'usr/lib/udev/rules.d/', 'usr/lib/udev/rules.d/60-vhba.rules', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/vhba-module-20211218/', 'usr/share/doc/vhba-module-20211218/AUTHORS', 'usr/share/doc/vhba-module-20211218/COPYING', 'usr/share/doc/vhba-module-20211218/ChangeLog', 'usr/share/doc/vhba-module-20211218/INSTALL', 'usr/share/doc/vhba-module-20211218/README']"
+++
VHBA module provides a Virtual (SCSI) HBA, which is the link between userspace daemon and linux kernel.