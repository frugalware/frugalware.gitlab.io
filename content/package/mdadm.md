+++
draft = false
title = "mdadm 4.3-1"
version = "4.3-1"
description = "A tool for managing software RAID under Linux"
date = "2024-03-01T09:17:00"
aliases = "/packages/3223"
categories = ['base']
upstreamurl = "http://www.kernel.org/pub/linux/utils/raid/mdadm/"
arch = "x86_64"
size = "390224"
usize = "1123538"
sha1sum = "7355989757f1ec7e177ab47f5c58c2420f9239b4"
depends = "['glibc>=2.34']"
reverse_depends = "['kernel-initrd', 'kernel-lts-initrd']"
+++
### Description: 
A tool for managing software RAID under Linux

### Files: 
* /etc/dracut.conf.d/11-raid.conf
* /etc/tmpfiles.d/mdadm.conf
* /usr/bin/mdadm
* /usr/bin/mdmon
* /usr/lib/systemd/system/mdadm.service
* /usr/lib/udev/rules.d/01-md-raid-creating.rules
* /usr/lib/udev/rules.d/63-md-raid-arrays.rules
* /usr/lib/udev/rules.d/64-md-raid-assembly.rules
* /usr/lib/udev/rules.d/69-md-clustered-confirm-device.rules
* /usr/share/doc/mdadm-4.3/ChangeLog
* /usr/share/doc/mdadm-4.3/COPYING
* /usr/share/doc/mdadm-4.3/INSTALL
* /usr/share/doc/mdadm-4.3/README.initramfs
* /usr/share/doc/mdadm-4.3/TODO
* /usr/share/man/man4/md.4.gz
* /usr/share/man/man5/mdadm.conf.5.gz
* /usr/share/man/man8/mdadm.8.gz
* /usr/share/man/man8/mdmon.8.gz
