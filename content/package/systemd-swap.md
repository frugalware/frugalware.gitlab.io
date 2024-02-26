+++
draft = false
title = "systemd-swap 4.4.0-2"
version = "4.4.0-2"
description = "Script for creating hybrid swap space from zram swaps, swap files and swap partitions."
date = "2024-01-15T13:17:27"
aliases = "/packages/217473"
categories = ['apps-extra']
upstreamurl = "https://github.com/Nefelim4ag/systemd-swap"
arch = "x86_64"
size = "23856"
usize = "77005"
sha1sum = "1e5ada0b0b2d38ff954849b40ffb160974af1c46"
depends = "['bash', 'systemd']"
license = "GPL3"
+++
Script for creating hybrid swap space from zram swaps, swap files and swap partitions.

{{< files text="show files" >}}* /etc/systemd/swap.conf
* /usr/bin/systemd-swap
* /usr/lib/systemd/system/systemd-swap.service
* /usr/share/doc/systemd-swap-4.4.0/LICENSE
* /usr/share/doc/systemd-swap-4.4.0/README.md
{{< /files >}}