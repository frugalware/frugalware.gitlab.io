+++
draft = false
title = "libseccomp 2.5.5-1"
version = "2.5.5-1"
description = "Enhanced seccomp library"
date = "2023-12-03T12:22:57"
aliases = "/packages/219075"
categories = ['base']
upstreamurl = "https://github.com/seccomp/libseccomp"
arch = "x86_64"
size = "89432"
usize = "280757"
sha1sum = "a96a47a5031285b8d8fd0ec8c015c6dcdc59cc28"
depends = "['glibc>=2.35']"
reverse_depends = "['flatpak', 'gnome-desktop', 'kscreenlocker', 'qemu', 'runc', 'systemd', 'systemd-nspawn', 'systemd-systemctl', 'tor', 'usbguard', 'webkit-gtk3']"
+++
Enhanced seccomp library

{{< files text="show files" >}}* /usr/bin/scmp_sys_resolver
* /usr/include/seccomp-syscalls.h
* /usr/include/seccomp.h
* /usr/lib/libseccomp.so
* /usr/lib/libseccomp.so.2
* /usr/lib/libseccomp.so.2.5.5
* /usr/lib/pkgconfig/libseccomp.pc
* /usr/share/doc/libseccomp-2.5.5/CHANGELOG
* /usr/share/doc/libseccomp-2.5.5/CREDITS
* /usr/share/doc/libseccomp-2.5.5/LICENSE
* /usr/share/doc/libseccomp-2.5.5/README.md
* /usr/share/man/man1/scmp_sys_resolver.1.gz
* /usr/share/man/man3/seccomp_api_get.3.gz
* /usr/share/man/man3/seccomp_api_set.3.gz
* /usr/share/man/man3/seccomp_arch_add.3.gz
* /usr/share/man/man3/seccomp_arch_exist.3.gz
* /usr/share/man/man3/seccomp_arch_native.3.gz
* /usr/share/man/man3/seccomp_arch_remove.3.gz
* /usr/share/man/man3/seccomp_arch_resolve_name.3.gz
* /usr/share/man/man3/seccomp_attr_get.3.gz
* /usr/share/man/man3/seccomp_attr_set.3.gz
* /usr/share/man/man3/seccomp_export_bpf.3.gz
* /usr/share/man/man3/seccomp_export_pfc.3.gz
* /usr/share/man/man3/seccomp_init.3.gz
* /usr/share/man/man3/seccomp_load.3.gz
* /usr/share/man/man3/seccomp_merge.3.gz
* /usr/share/man/man3/seccomp_notify_alloc.3.gz
* /usr/share/man/man3/seccomp_notify_fd.3.gz
* /usr/share/man/man3/seccomp_notify_free.3.gz
* /usr/share/man/man3/seccomp_notify_id_valid.3.gz
* /usr/share/man/man3/seccomp_notify_receive.3.gz
* /usr/share/man/man3/seccomp_notify_respond.3.gz
* /usr/share/man/man3/seccomp_release.3.gz
* /usr/share/man/man3/seccomp_reset.3.gz
* /usr/share/man/man3/seccomp_rule_add.3.gz
* /usr/share/man/man3/seccomp_rule_add_array.3.gz
* /usr/share/man/man3/seccomp_rule_add_exact.3.gz
* /usr/share/man/man3/seccomp_rule_add_exact_array.3.gz
* /usr/share/man/man3/seccomp_syscall_priority.3.gz
* /usr/share/man/man3/seccomp_syscall_resolve_name.3.gz
* /usr/share/man/man3/seccomp_syscall_resolve_name_arch.3.gz
* /usr/share/man/man3/seccomp_syscall_resolve_name_rewrite.3.gz
* /usr/share/man/man3/seccomp_syscall_resolve_num_arch.3.gz
* /usr/share/man/man3/seccomp_version.3.gz
{{< /files >}}