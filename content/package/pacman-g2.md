+++
draft = false
title = "pacman-g2 3.9.4-50"
version = "3.9.4-50"
description = "A .tar.xz based package manager library (libpacman) and client (pacman-g2) with dependency support."
date = "2024-05-08T08:55:47"
aliases = "/packages/14795"
categories = ['base']
upstreamurl = "https://ftp.frugalware.org/pub/other/pacman-g2/"
arch = "x86_64"
size = "3111132"
usize = "8200206"
sha1sum = "03a9a07e9f3f9f29d50bc28d803aed99e84cdb1c"
depends = "['coreutils', 'diffutils', 'glibc>=2.36', 'grep>=2.5.3-4', 'libarchive>=3.3.2', 'lz4>=r131-8', 'nettle>=3.5.1', 'openssl>=3.0.7', 'python3>=3.12', 'shadow', 'util-linux>=2.28.2-2', 'xz>=5.2.2-4', 'zstd']"
reverse_depends = "['etckeeper', 'pacman-tools']"
+++
### Description: 
A .tar.xz based package manager library (libpacman) and client (pacman-g2) with dependency support.

### Files: 
* /etc/bash_completion.d/pacman-g2
* /etc/makepkg.d/current-makepkg.conf
* /etc/pacman-g2.conf
* /etc/pacman-g2/hooks/foreign
* /etc/pacman-g2/hooks/orphans
* /etc/pacman-g2/repos/frugalware-current
* /usr/bin/gensync
* /usr/bin/makepkg
* /usr/bin/makeworld
* /usr/bin/pacman
* /usr/bin/pacman-g2
* /usr/bin/pacman-g2.static
* /usr/bin/updatesync
* /usr/bin/vercmp
* /usr/bin/versort
* /usr/include/pacman.h
* /usr/lib/libpacman.a
* /usr/lib/libpacman.so
* /usr/lib/libpacman.so.0
* /usr/lib/libpacman.so.0.3.8
* /usr/lib/perl5/site_perl/auto/Pacman/Core/Core.so
* /usr/lib/perl5/site_perl/Pacman/Core.pm
* /usr/lib/pkgconfig/pacman.pc
* /usr/lib/python3.12/site-packages/pacman.py
* /usr/lib/python3.12/site-packages/pacman.pyc
* /usr/lib/python3.12/site-packages/_pacman.so
* /usr/share/doc/pacman-g2-3.9.4/AUTHORS
* /usr/share/doc/pacman-g2-3.9.4/ChangeLog
* /usr/share/doc/pacman-g2-3.9.4/COPYING
* /usr/share/doc/pacman-g2-3.9.4/HACKING
* /usr/share/doc/pacman-g2-3.9.4/NEWS
* /usr/share/doc/pacman-g2-3.9.4/README
* /usr/share/doc/pacman-g2-3.9.4/TODO
* /usr/share/locale/da/LC_MESSAGES/libpacman.mo
* /usr/share/locale/da/LC_MESSAGES/pacman-g2.mo
* /usr/share/locale/de/LC_MESSAGES/pacman-g2.mo
* /usr/share/locale/fr/LC_MESSAGES/libpacman.mo
* /usr/share/locale/hu/LC_MESSAGES/libpacman.mo
* /usr/share/locale/hu/LC_MESSAGES/pacman-g2.mo
* /usr/share/locale/vi/LC_MESSAGES/libpacman.mo
* /usr/share/man/man3/libpacman.3.gz
* /usr/share/man/man3/pacman_conflict.3.gz
* /usr/share/man/man3/pacman_conflict_getinfo.3.gz
* /usr/share/man/man3/pacman_databases.3.gz
* /usr/share/man/man3/pacman_db_getgrpcache.3.gz
* /usr/share/man/man3/pacman_db_getinfo.3.gz
* /usr/share/man/man3/pacman_db_getpkgcache.3.gz
* /usr/share/man/man3/pacman_db_readgrp.3.gz
* /usr/share/man/man3/pacman_db_readpkg.3.gz
* /usr/share/man/man3/pacman_db_register.3.gz
* /usr/share/man/man3/pacman_db_search.3.gz
* /usr/share/man/man3/pacman_db_setserver.3.gz
* /usr/share/man/man3/pacman_db_test.3.gz
* /usr/share/man/man3/pacman_db_unregister.3.gz
* /usr/share/man/man3/pacman_db_update.3.gz
* /usr/share/man/man3/pacman_db_whatprovides.3.gz
* /usr/share/man/man3/pacman_dep.3.gz
* /usr/share/man/man3/pacman_dep_getinfo.3.gz
* /usr/share/man/man3/pacman_fetch_pkgurl.3.gz
* /usr/share/man/man3/pacman_get_md5sum.3.gz
* /usr/share/man/man3/pacman_get_option.3.gz
* /usr/share/man/man3/pacman_get_sha1sum.3.gz
* /usr/share/man/man3/pacman_groups.3.gz
* /usr/share/man/man3/pacman_grp_getinfo.3.gz
* /usr/share/man/man3/pacman_initialize.3.gz
* /usr/share/man/man3/pacman_interface.3.gz
* /usr/share/man/man3/pacman_list.3.gz
* /usr/share/man/man3/pacman_list_count.3.gz
* /usr/share/man/man3/pacman_list_first.3.gz
* /usr/share/man/man3/pacman_list_free.3.gz
* /usr/share/man/man3/pacman_list_getdata.3.gz
* /usr/share/man/man3/pacman_list_next.3.gz
* /usr/share/man/man3/pacman_log.3.gz
* /usr/share/man/man3/pacman_logaction.3.gz
* /usr/share/man/man3/pacman_misc.3.gz
* /usr/share/man/man3/pacman_options.3.gz
* /usr/share/man/man3/pacman_packages.3.gz
* /usr/share/man/man3/pacman_parse_config.3.gz
* /usr/share/man/man3/pacman_pkg_free.3.gz
* /usr/share/man/man3/pacman_pkg_getinfo.3.gz
* /usr/share/man/man3/pacman_pkg_getowners.3.gz
* /usr/share/man/man3/pacman_pkg_load.3.gz
* /usr/share/man/man3/pacman_pkg_vercmp.3.gz
* /usr/share/man/man3/pacman_reg_match.3.gz
* /usr/share/man/man3/pacman_release.3.gz
* /usr/share/man/man3/pacman_set_option.3.gz
* /usr/share/man/man3/pacman_sync.3.gz
* /usr/share/man/man3/pacman_sync_cleancache.3.gz
* /usr/share/man/man3/pacman_sync_getinfo.3.gz
* /usr/share/man/man3/pacman_trans.3.gz
* /usr/share/man/man3/pacman_trans_addtarget.3.gz
* /usr/share/man/man3/pacman_trans_commit.3.gz
* /usr/share/man/man3/pacman_trans_getinfo.3.gz
* /usr/share/man/man3/pacman_trans_init.3.gz
* /usr/share/man/man3/pacman_trans_prepare.3.gz
* /usr/share/man/man3/pacman_trans_release.3.gz
* /usr/share/man/man3/pacman_trans_sysupgrade.3.gz
* /usr/share/man/man5/FrugalBuild.5.gz
* /usr/share/man/man8/makepkg.8.gz
* /usr/share/man/man8/pacman-g2.8.gz
* /usr/share/vala/vapi/pacman.vapi
