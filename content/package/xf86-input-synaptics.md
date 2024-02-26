+++
draft = false
title = "xf86-input-synaptics 1.9.2-1"
version = "1.9.2-1"
description = "X.Org driver for synaptics input devices"
date = "2022-08-12T10:12:12"
aliases = "/packages/39921"
categories = ['x11']
upstreamurl = "http://xorg.freedesktop.org"
arch = "x86_64"
size = "186416"
usize = "676761"
sha1sum = "ee16943c2f830ae56e30f40d12a854785e021754"
depends = "['libevdev', 'libudev>=242', 'libxi>=1.7.6-2', 'mtdev>=1.1.5-$', 'xorg-server>=1.20.4-3']"
license = "GPL2"
+++
X.Org driver for synaptics input devices"

{{< files text="show files" >}}* /etc/X11/xorg.conf.d/20-synaptics.conf
* /usr/bin/synclient
* /usr/bin/syndaemon
* /usr/include/xorg/synaptics-properties.h
* /usr/lib/pkgconfig/xorg-synaptics.pc
* /usr/lib/xorg/modules/input/synaptics_drv.so
* /usr/share/doc/xf86-input-synaptics-1.9.2/ChangeLog
* /usr/share/doc/xf86-input-synaptics-1.9.2/COPYING
* /usr/share/doc/xf86-input-synaptics-1.9.2/INSTALL
* /usr/share/doc/xf86-input-synaptics-1.9.2/README.md
* /usr/share/man/man1/synclient.1.gz
* /usr/share/man/man1/syndaemon.1.gz
* /usr/share/man/man4/synaptics.4.gz
{{< /files >}}