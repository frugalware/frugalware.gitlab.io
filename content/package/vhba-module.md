+++
draft = false
title = "vhba-module 20211218-125"
version = "20211218-125"
date = "2023-11-08T15:14:13"
categories = ['apps-extra']
upstreamurl = "https://sourceforge.net/projects/cdemu"
arch = "x86_64"
size = "41580"
usize = "33607"
sha1sum = "9f6706c2c2e1c8c61aa7b18b14fb05ee9c1c3f79"
depends = "['kernel=6.6.1-1']"
files = "['lib/', 'lib/modules/', 'lib/modules/6.6.1-fw1/', 'lib/modules/6.6.1-fw1/kernel/', 'lib/modules/6.6.1-fw1/kernel/drivers/', 'lib/modules/6.6.1-fw1/kernel/drivers/scsi/', 'lib/modules/6.6.1-fw1/kernel/drivers/scsi/vhba.ko.zst', 'lib/udev/', 'lib/udev/rules.d/', 'lib/udev/rules.d/60-vhba.rules', 'usr/', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/vhba-module-20211218/', 'usr/share/doc/vhba-module-20211218/AUTHORS', 'usr/share/doc/vhba-module-20211218/COPYING', 'usr/share/doc/vhba-module-20211218/ChangeLog', 'usr/share/doc/vhba-module-20211218/INSTALL', 'usr/share/doc/vhba-module-20211218/README']"
+++
VHBA module provides a Virtual (SCSI) HBA, which is the link between userspace daemon and linux kernel.