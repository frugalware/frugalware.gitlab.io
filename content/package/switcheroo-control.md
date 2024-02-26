+++
draft = false
title = "switcheroo-control 2.6-3"
version = "2.6-3"
description = "D-Bus service to check the availability of dual-GPU"
date = "2024-01-30T10:03:50"
aliases = "/packages/221086"
categories = ['apps']
upstreamurl = "https://gitlab.freedesktop.org/hadess/switcheroo-control"
arch = "x86_64"
size = "23488"
usize = "101723"
sha1sum = "4105d76d2ac485ebf64479d0e2d9526dc26d9670"
depends = "['glib2', 'libgudev', 'pygobject3']"
reverse_depends = "['kio']"
+++
D-Bus service to check the availability of dual-GPU

{{< files text="show files" >}}* /usr/bin/switcherooctl
* /usr/lib/switcheroo-control/switcheroo-control
* /usr/lib/systemd/system/switcheroo-control.service
* /usr/lib/udev/hwdb.d/30-pci-intel-gpu.hwdb
* /usr/share/dbus-1/system.d/net.hadess.SwitcherooControl.conf
* /usr/share/doc/switcheroo-control-2.6/COPYING
* /usr/share/doc/switcheroo-control-2.6/NEWS
* /usr/share/doc/switcheroo-control-2.6/README.md
{{< /files >}}