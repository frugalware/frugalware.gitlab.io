+++
draft = false
title = "vhba-module 20211218-137"
version = "20211218-137"
date = "2024-01-22T14:45:56"
categories = ['apps-extra']
upstreamurl = "https://sourceforge.net/projects/cdemu"
arch = "x86_64"
size = "41808"
usize = "33500"
sha1sum = "301bbe0b84c020d6590d5d10ceab9a1d4fe3aad2"
depends = "['kernel=6.7.1-1']"
files = "['usr/', 'usr/lib/', 'usr/lib/modules/', 'usr/lib/modules/6.7.1-fw1/', 'usr/lib/modules/6.7.1-fw1/kernel/', 'usr/lib/modules/6.7.1-fw1/kernel/drivers/', 'usr/lib/modules/6.7.1-fw1/kernel/drivers/scsi/', 'usr/lib/modules/6.7.1-fw1/kernel/drivers/scsi/vhba.ko.zst', 'usr/lib/udev/', 'usr/lib/udev/rules.d/', 'usr/lib/udev/rules.d/60-vhba.rules', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/vhba-module-20211218/', 'usr/share/doc/vhba-module-20211218/AUTHORS', 'usr/share/doc/vhba-module-20211218/COPYING', 'usr/share/doc/vhba-module-20211218/ChangeLog', 'usr/share/doc/vhba-module-20211218/INSTALL', 'usr/share/doc/vhba-module-20211218/README']"
+++
VHBA module provides a Virtual (SCSI) HBA, which is the link between userspace daemon and linux kernel.