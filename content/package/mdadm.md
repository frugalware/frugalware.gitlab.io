+++
draft = false
title = "mdadm 4.2-3"
version = "4.2-3"
description = "A tool for managing software RAID under Linux"
date = "2024-01-02T22:20:31"
aliases = "/packages/3223"
categories = ['base']
upstreamurl = "http://www.kernel.org/pub/linux/utils/raid/mdadm/"
arch = "x86_64"
size = "379248"
usize = "1059154"
sha1sum = "6c9aabb9c4bf63a2cf3c1b2ea285bd5ce5fba47c"
depends = "['glibc>=2.34']"
reverse_depends = "['kernel-initrd', 'kernel-lts-initrd']"
+++
A tool for managing software RAID under Linux

{{< files text="show files" >}}* /etc/dracut.conf.d/11-raid.conf
* /etc/tmpfiles.d/mdadm.conf
* /usr/bin/mdadm
* /usr/bin/mdmon
* /usr/lib/systemd/system/mdadm.service
* /usr/lib/udev/rules.d/01-md-raid-creating.rules
* /usr/lib/udev/rules.d/63-md-raid-arrays.rules
* /usr/lib/udev/rules.d/64-md-raid-assembly.rules
* /usr/lib/udev/rules.d/69-md-clustered-confirm-device.rules
* /usr/share/doc/mdadm-4.2/ChangeLog
* /usr/share/doc/mdadm-4.2/COPYING
* /usr/share/doc/mdadm-4.2/INSTALL
* /usr/share/doc/mdadm-4.2/README.initramfs
* /usr/share/doc/mdadm-4.2/TODO
* /usr/share/man/man4/md.4.gz
* /usr/share/man/man5/mdadm.conf.5.gz
* /usr/share/man/man8/mdadm.8.gz
* /usr/share/man/man8/mdmon.8.gz
{{< /files >}}