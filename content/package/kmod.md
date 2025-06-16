+++
draft = false
title = "kmod 34.2-1"
version = "34.2-1"
description = "Utilities for inserting and removing modules from the Linux kernel"
date = "2025-03-31T08:09:54"
aliases = "/packages/221568"
categories = ['base']
upstreamurl = "http://kernel.org"
arch = "x86_64"
size = "150688"
usize = "412311"
sha1sum = "1bdd5452b3c1ffe25a7c47f110fcfb50acdf9c52"
depends = "['openssl>=3.1.0', 'xz>=5.2.4-2', 'zlib-ng', 'zstd>=1.4.4']"
reverse_depends = "['dracut', 'hwdata', 'intel-gpu-tools', 'inxi', 'iscsi', 'kernel', 'kernel-initrd', 'kernel-lts', 'kernel-lts-initrd', 'libndctl', 'ndctl', 'systemd', 'systemd-nspawn', 'systemd-systemctl', 'systemd-sysvinit']"
+++
### Description: 
Utilities for inserting and removing modules from the Linux kernel

### Files: 
* /etc/modules-load.d/sysconfig.conf
* /etc/sysconfig/modules
* /usr/bin/depmod
* /usr/bin/insmod
* /usr/bin/kmod
* /usr/bin/lsmod
* /usr/bin/modinfo
* /usr/bin/modprobe
* /usr/bin/rmmod
* /usr/include/libkmod.h
* /usr/lib/libkmod.so
* /usr/lib/libkmod.so.2
* /usr/lib/libkmod.so.2.5.1
* /usr/lib/pkgconfig/libkmod.pc
* /usr/share/bash-completion/completions/insmod
* /usr/share/bash-completion/completions/kmod
* /usr/share/bash-completion/completions/lsmod
* /usr/share/bash-completion/completions/rmmod
* /usr/share/doc/kmod-34.2/COPYING
* /usr/share/doc/kmod-34.2/NEWS
* /usr/share/doc/kmod-34.2/README.md
* /usr/share/fish/vendor_functions.d/insmod.fish
* /usr/share/fish/vendor_functions.d/lsmod.fish
* /usr/share/fish/vendor_functions.d/rmmod.fish
* /usr/share/man/man5/depmod.d.5.gz
* /usr/share/man/man5/modprobe.conf.5.gz
* /usr/share/man/man5/modprobe.d.5.gz
* /usr/share/man/man5/modules.dep.5.gz
* /usr/share/man/man5/modules.dep.bin.5.gz
* /usr/share/man/man8/depmod.8.gz
* /usr/share/man/man8/insmod.8.gz
* /usr/share/man/man8/kmod.8.gz
* /usr/share/man/man8/lsmod.8.gz
* /usr/share/man/man8/modinfo.8.gz
* /usr/share/man/man8/modprobe.8.gz
* /usr/share/man/man8/rmmod.8.gz
* /usr/share/pkgconfig/kmod.pc
* /usr/share/zsh/site-functions/_insmod
* /usr/share/zsh/site-functions/_lsmod
* /usr/share/zsh/site-functions/_rmmod
