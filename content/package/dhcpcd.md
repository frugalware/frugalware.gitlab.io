+++
draft = false
title = "dhcpcd 10.0.6-2"
version = "10.0.6-2"
description = "A DHCP client daemon"
date = "2024-01-03T09:45:16"
aliases = "/packages/2363"
categories = ['base']
upstreamurl = "https://roy.marples.name/projects/dhcpcd/"
arch = "x86_64"
size = "207596"
usize = "510971"
sha1sum = "9507faef6036f8a4e4483c03e0b0af358eab8371"
depends = "['glibc>=2.34', 'libudev>=242']"
+++
A DHCP client daemon

{{< files text="show files" >}}* /etc/dhcpcd.conf
* /usr/bin/dhcpcd
* /usr/lib/dhcpcd/dev/udev.so
* /usr/lib/dhcpcd/dhcpcd-hooks/01-test
* /usr/lib/dhcpcd/dhcpcd-hooks/20-resolv.conf
* /usr/lib/dhcpcd/dhcpcd-hooks/30-hostname
* /usr/lib/dhcpcd/dhcpcd-hooks/50-timesyncd.conf
* /usr/lib/dhcpcd/dhcpcd-run-hooks
* /usr/share/dhcpcd/hooks/10-wpa_supplicant
* /usr/share/dhcpcd/hooks/15-timezone
* /usr/share/dhcpcd/hooks/29-lookup-hostname
* /usr/share/dhcpcd/hooks/50-yp.conf
* /usr/share/doc/dhcpcd-10.0.6/LICENSE
* /usr/share/doc/dhcpcd-10.0.6/README.md
* /usr/share/man/man5/dhcpcd.conf.5.gz
* /usr/share/man/man8/dhcpcd-run-hooks.8.gz
* /usr/share/man/man8/dhcpcd.8.gz
{{< /files >}}