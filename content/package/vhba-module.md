+++
draft = false
title = "vhba-module 20211218-131"
version = "20211218-131"
date = "2023-12-13T20:41:37"
categories = ['apps-extra']
upstreamurl = "https://sourceforge.net/projects/cdemu"
arch = "x86_64"
size = "41768"
usize = "33611"
sha1sum = "828b3fb8e598a35f6f399f0156d23b234dbbdbbc"
depends = "['kernel=6.6.7-1']"
files = "['lib/', 'lib/modules/', 'lib/modules/6.6.7-fw1/', 'lib/modules/6.6.7-fw1/kernel/', 'lib/modules/6.6.7-fw1/kernel/drivers/', 'lib/modules/6.6.7-fw1/kernel/drivers/scsi/', 'lib/modules/6.6.7-fw1/kernel/drivers/scsi/vhba.ko.zst', 'lib/udev/', 'lib/udev/rules.d/', 'lib/udev/rules.d/60-vhba.rules', 'usr/', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/vhba-module-20211218/', 'usr/share/doc/vhba-module-20211218/AUTHORS', 'usr/share/doc/vhba-module-20211218/COPYING', 'usr/share/doc/vhba-module-20211218/ChangeLog', 'usr/share/doc/vhba-module-20211218/INSTALL', 'usr/share/doc/vhba-module-20211218/README']"
+++
VHBA module provides a Virtual (SCSI) HBA, which is the link between userspace daemon and linux kernel.