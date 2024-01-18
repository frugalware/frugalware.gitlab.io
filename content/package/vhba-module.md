+++
draft = false
title = "vhba-module 20211218-136"
version = "20211218-136"
date = "2024-01-18T09:07:34"
categories = ['apps-extra']
upstreamurl = "https://sourceforge.net/projects/cdemu"
arch = "x86_64"
size = "41760"
usize = "33499"
sha1sum = "ec164b0f048091debe5506b8a1307f39afdf030a"
depends = "['kernel=6.7-2']"
files = "['usr/', 'usr/lib/', 'usr/lib/modules/', 'usr/lib/modules/6.7-fw2/', 'usr/lib/modules/6.7-fw2/kernel/', 'usr/lib/modules/6.7-fw2/kernel/drivers/', 'usr/lib/modules/6.7-fw2/kernel/drivers/scsi/', 'usr/lib/modules/6.7-fw2/kernel/drivers/scsi/vhba.ko.zst', 'usr/lib/udev/', 'usr/lib/udev/rules.d/', 'usr/lib/udev/rules.d/60-vhba.rules', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/vhba-module-20211218/', 'usr/share/doc/vhba-module-20211218/AUTHORS', 'usr/share/doc/vhba-module-20211218/COPYING', 'usr/share/doc/vhba-module-20211218/ChangeLog', 'usr/share/doc/vhba-module-20211218/INSTALL', 'usr/share/doc/vhba-module-20211218/README']"
+++
VHBA module provides a Virtual (SCSI) HBA, which is the link between userspace daemon and linux kernel.