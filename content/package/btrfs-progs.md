+++
draft = false
title = "btrfs-progs 6.6.2-1"
version = "6.6.2-1"
date = "2023-11-16T08:53:03"
categories = ['base']
upstreamurl = "https://btrfs.wiki.kernel.org"
arch = "x86_64"
size = "1191508"
usize = "7129811"
sha1sum = "9482ea529ae56e77bdc4976d9638aff53a971d0a"
depends = "['e2fsprogs>=1.43.8-2', 'lzo>=2.10-3', 'zstd>=1.3.3-2']"
files = "['lib/', 'lib/udev/', 'lib/udev/rules.d/', 'lib/udev/rules.d/64-btrfs-dm.rules', 'lib/udev/rules.d/64-btrfs-zoned.rules', 'sbin/', 'sbin/btrfs', 'sbin/btrfs-convert', 'sbin/btrfs-find-root', 'sbin/btrfs-image', 'sbin/btrfs-map-logical', 'sbin/btrfs-select-super', 'sbin/btrfsck', 'sbin/btrfstune', 'sbin/fsck.btrfs', 'sbin/mkfs.btrfs', 'usr/', 'usr/include/', 'usr/include/btrfs/', 'usr/include/btrfs/ctree.h', 'usr/include/btrfs/ioctl.h', 'usr/include/btrfs/kerncompat.h', 'usr/include/btrfs/list.h', 'usr/include/btrfs/rbtree.h', 'usr/include/btrfs/rbtree_types.h', 'usr/include/btrfs/send-stream.h', 'usr/include/btrfs/send-utils.h', 'usr/include/btrfs/send.h', 'usr/include/btrfs/version.h', 'usr/include/btrfsutil.h', 'usr/lib/', 'usr/lib/libbtrfs.so', 'usr/lib/libbtrfs.so.0', 'usr/lib/libbtrfs.so.0.1', 'usr/lib/libbtrfsutil.so', 'usr/lib/libbtrfsutil.so.1', 'usr/lib/libbtrfsutil.so.1.2.0', 'usr/lib/pkgconfig/', 'usr/lib/pkgconfig/libbtrfsutil.pc', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/btrfs-progs-6.6.2/', 'usr/share/doc/btrfs-progs-6.6.2/CHANGES', 'usr/share/doc/btrfs-progs-6.6.2/COPYING', 'usr/share/doc/btrfs-progs-6.6.2/INSTALL', 'usr/share/doc/btrfs-progs-6.6.2/README.md', 'usr/share/doc/btrfs-progs-6.6.2/VERSION', 'usr/share/man/', 'usr/share/man/man5/', 'usr/share/man/man5/btrfs.5.gz', 'usr/share/man/man8/', 'usr/share/man/man8/btrfs-balance.8.gz', 'usr/share/man/man8/btrfs-check.8.gz', 'usr/share/man/man8/btrfs-convert.8.gz', 'usr/share/man/man8/btrfs-device.8.gz', 'usr/share/man/man8/btrfs-filesystem.8.gz', 'usr/share/man/man8/btrfs-find-root.8.gz', 'usr/share/man/man8/btrfs-image.8.gz', 'usr/share/man/man8/btrfs-inspect-internal.8.gz', 'usr/share/man/man8/btrfs-map-logical.8.gz', 'usr/share/man/man8/btrfs-property.8.gz', 'usr/share/man/man8/btrfs-qgroup.8.gz', 'usr/share/man/man8/btrfs-quota.8.gz', 'usr/share/man/man8/btrfs-receive.8.gz', 'usr/share/man/man8/btrfs-replace.8.gz', 'usr/share/man/man8/btrfs-rescue.8.gz', 'usr/share/man/man8/btrfs-restore.8.gz', 'usr/share/man/man8/btrfs-scrub.8.gz', 'usr/share/man/man8/btrfs-select-super.8.gz', 'usr/share/man/man8/btrfs-send.8.gz', 'usr/share/man/man8/btrfs-subvolume.8.gz', 'usr/share/man/man8/btrfs.8.gz', 'usr/share/man/man8/btrfsck.8.gz', 'usr/share/man/man8/btrfstune.8.gz', 'usr/share/man/man8/fsck.btrfs.8.gz', 'usr/share/man/man8/mkfs.btrfs.8.gz']"
+++
Utilities for managing btrfs filesystems.