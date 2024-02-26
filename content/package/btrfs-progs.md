+++
draft = false
title = "btrfs-progs 6.7.1-1"
version = "6.7.1-1"
description = "Utilities for managing btrfs filesystems."
date = "2024-02-17T22:14:24"
aliases = "/packages/219969"
categories = ['base']
upstreamurl = "https://btrfs.wiki.kernel.org"
arch = "x86_64"
size = "1201384"
usize = "7180801"
sha1sum = "7ea0d0056be8ff8ec97094ea0fc83bdec0705a80"
depends = "['e2fsprogs>=1.43.8-2', 'lzo>=2.10-3', 'zstd>=1.3.3-2']"
reverse_depends = "['docker', 'kernel-initrd', 'kernel-lts-initrd', 'udisks2']"
+++
Utilities for managing btrfs filesystems.

{{< files text="show files" >}}* /usr/bin/btrfs
* /usr/bin/btrfs-convert
* /usr/bin/btrfs-find-root
* /usr/bin/btrfs-image
* /usr/bin/btrfs-map-logical
* /usr/bin/btrfs-select-super
* /usr/bin/btrfsck
* /usr/bin/btrfstune
* /usr/bin/fsck.btrfs
* /usr/bin/mkfs.btrfs
* /usr/include/btrfs/ctree.h
* /usr/include/btrfs/ioctl.h
* /usr/include/btrfs/kerncompat.h
* /usr/include/btrfs/list.h
* /usr/include/btrfs/rbtree.h
* /usr/include/btrfs/rbtree_types.h
* /usr/include/btrfs/send-stream.h
* /usr/include/btrfs/send-utils.h
* /usr/include/btrfs/send.h
* /usr/include/btrfs/version.h
* /usr/include/btrfsutil.h
* /usr/lib/libbtrfs.so
* /usr/lib/libbtrfs.so.0
* /usr/lib/libbtrfs.so.0.1
* /usr/lib/libbtrfsutil.so
* /usr/lib/libbtrfsutil.so.1
* /usr/lib/libbtrfsutil.so.1.2.0
* /usr/lib/pkgconfig/libbtrfsutil.pc
* /usr/lib/udev/rules.d/64-btrfs-dm.rules
* /usr/lib/udev/rules.d/64-btrfs-zoned.rules
* /usr/share/doc/btrfs-progs-6.7.1/CHANGES
* /usr/share/doc/btrfs-progs-6.7.1/COPYING
* /usr/share/doc/btrfs-progs-6.7.1/INSTALL
* /usr/share/doc/btrfs-progs-6.7.1/README.md
* /usr/share/doc/btrfs-progs-6.7.1/VERSION
* /usr/share/man/man5/btrfs.5.gz
* /usr/share/man/man8/btrfs-balance.8.gz
* /usr/share/man/man8/btrfs-check.8.gz
* /usr/share/man/man8/btrfs-convert.8.gz
* /usr/share/man/man8/btrfs-device.8.gz
* /usr/share/man/man8/btrfs-filesystem.8.gz
* /usr/share/man/man8/btrfs-find-root.8.gz
* /usr/share/man/man8/btrfs-image.8.gz
* /usr/share/man/man8/btrfs-inspect-internal.8.gz
* /usr/share/man/man8/btrfs-map-logical.8.gz
* /usr/share/man/man8/btrfs-property.8.gz
* /usr/share/man/man8/btrfs-qgroup.8.gz
* /usr/share/man/man8/btrfs-quota.8.gz
* /usr/share/man/man8/btrfs-receive.8.gz
* /usr/share/man/man8/btrfs-replace.8.gz
* /usr/share/man/man8/btrfs-rescue.8.gz
* /usr/share/man/man8/btrfs-restore.8.gz
* /usr/share/man/man8/btrfs-scrub.8.gz
* /usr/share/man/man8/btrfs-select-super.8.gz
* /usr/share/man/man8/btrfs-send.8.gz
* /usr/share/man/man8/btrfs-subvolume.8.gz
* /usr/share/man/man8/btrfs.8.gz
* /usr/share/man/man8/btrfsck.8.gz
* /usr/share/man/man8/btrfstune.8.gz
* /usr/share/man/man8/fsck.btrfs.8.gz
* /usr/share/man/man8/mkfs.btrfs.8.gz
{{< /files >}}