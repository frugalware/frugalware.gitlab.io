+++
draft = false
title = "xf86-input-wacom 0.36.0-6"
version = "0.36.0-6"
description = "X.Org driver for wacom input devices"
date = "2024-01-06T13:50:02"
aliases = "/packages/88753"
categories = ['x11']
upstreamurl = "http://xorg.freedesktop.org"
arch = "x86_64"
size = "278348"
usize = "1107150"
sha1sum = "d92e8f32805619de9686a8b75585969878eb5066"
depends = "['libudev>=242', 'libxi>=1.7.6-2', 'libxinerama>=1.1.3-2', 'libxrandr>=1.5.0-4', 'systemd>=231-6', 'xorg-server>=1.20.4-3']"
license = "GPL2"
+++
X.Org driver for wacom input devices

{{< files text="show files" >}}* /usr/bin/isdv4-serial-debugger
* /usr/bin/isdv4-serial-inputattach
* /usr/bin/xsetwacom
* /usr/include/xorg/isdv4.h
* /usr/include/xorg/wacom-properties.h
* /usr/include/xorg/wacom-util.h
* /usr/include/xorg/Xwacom.h
* /usr/lib/pkgconfig/xorg-wacom.pc
* /usr/lib/systemd/system/wacom-inputattach@.service
* /usr/lib/udev/rules.d/wacom.rules
* /usr/lib/xorg/modules/input/wacom_drv.so
* /usr/share/doc/xf86-input-wacom-0.36.0/AUTHORS
* /usr/share/doc/xf86-input-wacom-0.36.0/ChangeLog
* /usr/share/doc/xf86-input-wacom-0.36.0/INSTALL
* /usr/share/doc/xf86-input-wacom-0.36.0/README
* /usr/share/man/man1/xsetwacom.1.gz
* /usr/share/man/man4/wacom.4.gz
* /usr/share/X11/xorg.conf.d/70-wacom.conf
{{< /files >}}