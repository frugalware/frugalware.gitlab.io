+++
draft = false
title = "libcap 2.75-1"
version = "2.75-1"
description = "POSIX 1003.1e capabilities"
date = "2025-03-05T09:27:10"
aliases = "/packages/3151"
categories = ['base']
upstreamurl = "https://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2"
arch = "x86_64"
size = "87356"
usize = "193366"
sha1sum = "9e83dc9d3bd5d4f35f793f0f8d8b47f9695f1fe4"
depends = "['glibc>=2.35', 'xfsprogs-attr>=2.2.53-2']"
reverse_depends = "['android-tools', 'bpf', 'cdrtools', 'chrony', 'coreutils', 'gstreamer1', 'hwloc', 'i3status', 'inetutils', 'iputils', 'libsystemd', 'libu2f-host', 'pure-ftpd', 'systemd-pull', 'systemd-sysvinit', 'thin-provisioning-tools', 'uwsgi', 'virtualbox', 'zsh']"
+++
### Description: 
POSIX 1003.1e capabilities

### Files: 
* /usr/bin/capsh
* /usr/bin/getcap
* /usr/bin/getpcaps
* /usr/bin/setcap
* /usr/include/sys/capability.h
* /usr/include/sys/psx_syscall.h
* /usr/lib/libcap.so
* /usr/lib/libcap.so.2
* /usr/lib/libcap.so.2.75
* /usr/lib/libpsx.so
* /usr/lib/libpsx.so.2
* /usr/lib/libpsx.so.2.75
* /usr/lib/pkgconfig/libcap.pc
* /usr/lib/pkgconfig/libpsx.pc
* /usr/lib/security/pam_cap.so
* /usr/share/doc/libcap-2.75/capability.conf
* /usr/share/doc/libcap-2.75/CHANGELOG
* /usr/share/doc/libcap-2.75/README
* /usr/share/man/man1/capsh.1.gz
* /usr/share/man/man3/capgetp.3.gz
* /usr/share/man/man3/capsetp.3.gz
* /usr/share/man/man3/cap_clear.3.gz
* /usr/share/man/man3/cap_clear_flag.3.gz
* /usr/share/man/man3/cap_compare.3.gz
* /usr/share/man/man3/cap_copy_ext.3.gz
* /usr/share/man/man3/cap_copy_int.3.gz
* /usr/share/man/man3/cap_copy_int_check.3.gz
* /usr/share/man/man3/cap_drop_bound.3.gz
* /usr/share/man/man3/cap_dup.3.gz
* /usr/share/man/man3/cap_fill.3.gz
* /usr/share/man/man3/cap_fill_flag.3.gz
* /usr/share/man/man3/cap_free.3.gz
* /usr/share/man/man3/cap_from_name.3.gz
* /usr/share/man/man3/cap_from_text.3.gz
* /usr/share/man/man3/cap_func_launcher.3.gz
* /usr/share/man/man3/cap_get_bound.3.gz
* /usr/share/man/man3/cap_get_fd.3.gz
* /usr/share/man/man3/cap_get_file.3.gz
* /usr/share/man/man3/cap_get_flag.3.gz
* /usr/share/man/man3/cap_get_mode.3.gz
* /usr/share/man/man3/cap_get_nsowner.3.gz
* /usr/share/man/man3/cap_get_pid.3.gz
* /usr/share/man/man3/cap_get_proc.3.gz
* /usr/share/man/man3/cap_get_secbits.3.gz
* /usr/share/man/man3/cap_iab.3.gz
* /usr/share/man/man3/cap_iab_compare.3.gz
* /usr/share/man/man3/cap_iab_dup.3.gz
* /usr/share/man/man3/cap_iab_fill.3.gz
* /usr/share/man/man3/cap_iab_from_text.3.gz
* /usr/share/man/man3/cap_iab_get_pid.3.gz
* /usr/share/man/man3/cap_iab_get_proc.3.gz
* /usr/share/man/man3/cap_iab_get_vector.3.gz
* /usr/share/man/man3/cap_iab_init.3.gz
* /usr/share/man/man3/cap_iab_set_proc.3.gz
* /usr/share/man/man3/cap_iab_set_vector.3.gz
* /usr/share/man/man3/cap_iab_to_text.3.gz
* /usr/share/man/man3/cap_init.3.gz
* /usr/share/man/man3/cap_launch.3.gz
* /usr/share/man/man3/cap_launcher_callback.3.gz
* /usr/share/man/man3/cap_launcher_setgroups.3.gz
* /usr/share/man/man3/cap_launcher_setuid.3.gz
* /usr/share/man/man3/cap_launcher_set_chroot.3.gz
* /usr/share/man/man3/cap_launcher_set_iab.3.gz
* /usr/share/man/man3/cap_launcher_set_mode.3.gz
* /usr/share/man/man3/cap_max_bits.3.gz
* /usr/share/man/man3/cap_mode.3.gz
* /usr/share/man/man3/cap_mode_name.3.gz
* /usr/share/man/man3/cap_new_launcher.3.gz
* /usr/share/man/man3/cap_prctl.3.gz
* /usr/share/man/man3/cap_prctlw.3.gz
* /usr/share/man/man3/cap_proc_root.3.gz
* /usr/share/man/man3/cap_setgroups.3.gz
* /usr/share/man/man3/cap_setuid.3.gz
* /usr/share/man/man3/cap_set_fd.3.gz
* /usr/share/man/man3/cap_set_file.3.gz
* /usr/share/man/man3/cap_set_flag.3.gz
* /usr/share/man/man3/cap_set_mode.3.gz
* /usr/share/man/man3/cap_set_nsowner.3.gz
* /usr/share/man/man3/cap_set_proc.3.gz
* /usr/share/man/man3/cap_set_secbits.3.gz
* /usr/share/man/man3/cap_set_syscall.3.gz
* /usr/share/man/man3/cap_size.3.gz
* /usr/share/man/man3/cap_to_name.3.gz
* /usr/share/man/man3/cap_to_text.3.gz
* /usr/share/man/man3/libcap.3.gz
* /usr/share/man/man3/libpsx.3.gz
* /usr/share/man/man3/psx_load_syscalls.3.gz
* /usr/share/man/man3/psx_set_sensitivity.3.gz
* /usr/share/man/man3/psx_syscall.3.gz
* /usr/share/man/man3/psx_syscall3.3.gz
* /usr/share/man/man3/psx_syscall6.3.gz
* /usr/share/man/man3/__psx_syscall.3.gz
* /usr/share/man/man5/capability.conf.5.gz
* /usr/share/man/man8/captree.8.gz
* /usr/share/man/man8/getcap.8.gz
* /usr/share/man/man8/getpcaps.8.gz
* /usr/share/man/man8/pam_cap.8.gz
* /usr/share/man/man8/setcap.8.gz
