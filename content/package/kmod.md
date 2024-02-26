+++
draft = false
title = "kmod 31-4"
version = "31-4"
date = "2024-01-17T17:26:19"
aliases = "/packages/137173"
categories = ['base']
upstreamurl = "http://kernel.org"
arch = "x86_64"
size = "176220"
usize = "469076"
sha1sum = "0b58a9588178ec29d4792385046fe4a5e4351e43"
depends = "['openssl>=3.1.0', 'xz>=5.2.4-2', 'zlib>=1.2.12', 'zstd>=1.4.4']"
reverse depends = "['dracut', 'hwdata', 'intel-gpu-tools', 'inxi', 'iscsi', 'kernel', 'kernel-initrd', 'kernel-lts', 'kernel-lts-initrd', 'libndctl', 'ndctl', 'pciutils', 'pcmciautils', 'systemd', 'systemd-nspawn', 'systemd-systemctl', 'systemd-sysvinit']"
files = "['/etc/modules-load.d/sysconfig.conf', '/etc/sysconfig/modules', '/usr/bin/depmod', '/usr/bin/insmod', '/usr/bin/kmod', '/usr/bin/lsmod', '/usr/bin/modinfo', '/usr/bin/modprobe', '/usr/bin/rmmod', '/usr/include/libkmod.h', '/usr/lib/libkmod.so', '/usr/lib/libkmod.so.2', '/usr/lib/libkmod.so.2.4.1', '/usr/lib/pkgconfig/libkmod.pc', '/usr/share/bash-completion/completions/kmod', '/usr/share/doc/kmod-31/COPYING', '/usr/share/doc/kmod-31/CREDITS', '/usr/share/doc/kmod-31/NEWS', '/usr/share/doc/kmod-31/README', '/usr/share/doc/kmod-31/README.md', '/usr/share/doc/kmod-31/TODO', '/usr/share/man/man5/depmod.d.5.gz', '/usr/share/man/man5/modprobe.d.5.gz', '/usr/share/man/man5/modules.dep.5.gz', '/usr/share/man/man5/modules.dep.bin.5.gz', '/usr/share/man/man8/depmod.8.gz', '/usr/share/man/man8/insmod.8.gz', '/usr/share/man/man8/kmod.8.gz', '/usr/share/man/man8/lsmod.8.gz', '/usr/share/man/man8/modinfo.8.gz', '/usr/share/man/man8/modprobe.8.gz', '/usr/share/man/man8/rmmod.8.gz']"
+++
Utilities for inserting and removing modules from the Linux kernel