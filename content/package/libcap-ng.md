+++
draft = false
title = "libcap-ng 0.8.3-1"
version = "0.8.3-1"
date = "2022-07-10T13:07:37"
categories = ['base', 'chroot-core']
upstreamurl = "http://people.redhat.com/sgrubb/libcap-ng/"
arch = "x86_64"
size = "95760"
usize = "278990"
sha1sum = "a7f41ac1881a6d310fa23f8baadd90688c1e441e"
depends = "['glibc>=2.35']"
license = "LGPL2.1"
files = "['usr/', 'usr/bin/', 'usr/bin/captest', 'usr/bin/filecap', 'usr/bin/netcap', 'usr/bin/pscap', 'usr/include/', 'usr/include/cap-ng.h', 'usr/lib/', 'usr/lib/libcap-ng.so', 'usr/lib/libcap-ng.so.0', 'usr/lib/libcap-ng.so.0.0.0', 'usr/lib/libdrop_ambient.so', 'usr/lib/libdrop_ambient.so.0', 'usr/lib/libdrop_ambient.so.0.0.0', 'usr/lib/pkgconfig/', 'usr/lib/pkgconfig/libcap-ng.pc', 'usr/share/', 'usr/share/aclocal/', 'usr/share/aclocal/cap-ng.m4', 'usr/share/doc/', 'usr/share/doc/libcap-ng-0.8.3/', 'usr/share/doc/libcap-ng-0.8.3/AUTHORS', 'usr/share/doc/libcap-ng-0.8.3/COPYING', 'usr/share/doc/libcap-ng-0.8.3/COPYING.LIB', 'usr/share/doc/libcap-ng-0.8.3/CREDITS', 'usr/share/doc/libcap-ng-0.8.3/ChangeLog', 'usr/share/doc/libcap-ng-0.8.3/INSTALL', 'usr/share/doc/libcap-ng-0.8.3/README', 'usr/share/man/', 'usr/share/man/man3/', 'usr/share/man/man3/capng_apply.3.gz', 'usr/share/man/man3/capng_apply_caps_fd.3.gz', 'usr/share/man/man3/capng_capability_to_name.3.gz', 'usr/share/man/man3/capng_change_id.3.gz', 'usr/share/man/man3/capng_clear.3.gz', 'usr/share/man/man3/capng_fill.3.gz', 'usr/share/man/man3/capng_get_caps_fd.3.gz', 'usr/share/man/man3/capng_get_caps_process.3.gz', 'usr/share/man/man3/capng_get_rootid.3.gz', 'usr/share/man/man3/capng_have_capabilities.3.gz', 'usr/share/man/man3/capng_have_capability.3.gz', 'usr/share/man/man3/capng_lock.3.gz', 'usr/share/man/man3/capng_name_to_capability.3.gz', 'usr/share/man/man3/capng_print_caps_numeric.3.gz', 'usr/share/man/man3/capng_print_caps_text.3.gz', 'usr/share/man/man3/capng_restore_state.3.gz', 'usr/share/man/man3/capng_save_state.3.gz', 'usr/share/man/man3/capng_set_rootid.3.gz', 'usr/share/man/man3/capng_setpid.3.gz', 'usr/share/man/man3/capng_update.3.gz', 'usr/share/man/man3/capng_updatev.3.gz', 'usr/share/man/man7/', 'usr/share/man/man7/libdrop_ambient.7.gz', 'usr/share/man/man8/', 'usr/share/man/man8/captest.8.gz', 'usr/share/man/man8/filecap.8.gz', 'usr/share/man/man8/netcap.8.gz', 'usr/share/man/man8/pscap.8.gz']"
+++
A library making programming with POSIX capabilities easier than traditional libcap