+++
draft = false
title = "vhba-module 20211218-141"
version = "20211218-141"
date = "2024-02-17T19:13:19"
categories = ['apps-extra']
upstreamurl = "https://sourceforge.net/projects/cdemu"
arch = "x86_64"
size = "41924"
usize = "33479"
sha1sum = "df8ea0508e934c21850d1bdd176430e39bdf99a9"
depends = "['kernel=6.7.5-1']"
files = "['usr/', 'usr/lib/', 'usr/lib/modules/', 'usr/lib/modules/6.7.5-fw1/', 'usr/lib/modules/6.7.5-fw1/kernel/', 'usr/lib/modules/6.7.5-fw1/kernel/drivers/', 'usr/lib/modules/6.7.5-fw1/kernel/drivers/scsi/', 'usr/lib/modules/6.7.5-fw1/kernel/drivers/scsi/vhba.ko.zst', 'usr/lib/udev/', 'usr/lib/udev/rules.d/', 'usr/lib/udev/rules.d/60-vhba.rules', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/vhba-module-20211218/', 'usr/share/doc/vhba-module-20211218/AUTHORS', 'usr/share/doc/vhba-module-20211218/COPYING', 'usr/share/doc/vhba-module-20211218/ChangeLog', 'usr/share/doc/vhba-module-20211218/INSTALL', 'usr/share/doc/vhba-module-20211218/README']"
+++
VHBA module provides a Virtual (SCSI) HBA, which is the link between userspace daemon and linux kernel.