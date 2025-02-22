+++
draft = false
title = "kmod 34-2"
version = "34-2"
description = "Utilities for inserting and removing modules from the Linux kernel"
date = "2025-02-22T12:49:52"
aliases = "/packages/221568"
categories = ['base']
upstreamurl = "http://kernel.org"
arch = "x86_64"
size = "150040"
usize = "411971"
sha1sum = "377d66b7ea82279b39b8ad593f3710314ab0c66c"
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
* /usr/share/doc/kmod-34/COPYING
* /usr/share/doc/kmod-34/NEWS
* /usr/share/doc/kmod-34/README.md
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
