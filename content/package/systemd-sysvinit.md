+++
draft = false
title = "systemd-sysvinit 255.3-2"
version = "255.3-2"
description = "systemd System V init tools"
date = "2024-02-01T13:22:45"
aliases = "/packages/103629"
categories = ['base']
upstreamurl = "http://www.freedesktop.org/wiki/Software/systemd"
arch = "x86_64"
size = "30272"
usize = "5189"
sha1sum = "5bfe3c5bab056f4b385026f2bc8ac87314deffa8"
depends = "['kmod>=25-2', 'libcap>=2.25-4', 'libgcrypt>=1.8.0-2', 'lz4>=1.8.1.2-2', 'pam>=1.3.0-4', 'systemd=255.3']"
reverse_depends = "['systemd']"
+++
systemd System V init tools"

{{< files text="show files" >}}* /usr/bin/halt
* /usr/bin/init
* /usr/bin/poweroff
* /usr/bin/reboot
* /usr/bin/runlevel
* /usr/bin/shutdown
* /usr/bin/telinit
* /usr/share/man/man8/halt.8.gz
* /usr/share/man/man8/poweroff.8.gz
* /usr/share/man/man8/reboot.8.gz
* /usr/share/man/man8/runlevel.8.gz
* /usr/share/man/man8/shutdown.8.gz
* /usr/share/man/man8/telinit.8.gz
{{< /files >}}