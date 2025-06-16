+++
draft = false
title = "e2fsprogs 1.47.2-1"
version = "1.47.2-1"
description = "Utilities needed to create and maintain ext2 and ext3 filesystems"
date = "2025-01-30T08:50:41"
aliases = "/packages/2367"
categories = ['base']
upstreamurl = "http://e2fsprogs.sourceforge.net/"
arch = "x86_64"
size = "1207744"
usize = "5368993"
sha1sum = "fb020f68280860610293929709faf7a329a22345"
depends = "['coreutils>=8.29-5', 'glibc>=2.34', 'libblkid>=2.31.1-2', 'libuuid>=2.40.2', 'util-linux>=2.31.1-2']"
reverse_depends = "['aide', 'btrfs-progs', 'cyrus-sasl', 'cyrus-sasl-sql', 'dovecot', 'e2fsimage', 'fsarchiver', 'kernel-initrd', 'kernel-lts-initrd', 'krb5', 'libkrb5', 'partclone', 'parted', 'partitionmanager', 'quota-tools', 'reiserfsprogs']"
+++
### Description: 
Utilities needed to create and maintain ext2 and ext3 filesystems

### Files: 
* /etc/e2scrub.conf
* /etc/mke2fs.conf
* /usr/bin/badblocks
* /usr/bin/chattr
* /usr/bin/compile_et
* /usr/bin/debugfs
* /usr/bin/dumpe2fs
* /usr/bin/e2freefrag
* /usr/bin/e2fsck
* /usr/bin/e2image
* /usr/bin/e2label
* /usr/bin/e2mmpstatus
* /usr/bin/e2scrub
* /usr/bin/e2scrub_all
* /usr/bin/e2undo
* /usr/bin/e4crypt
* /usr/bin/e4defrag
* /usr/bin/filefrag
* /usr/bin/fsck.ext2
* /usr/bin/fsck.ext3
* /usr/bin/fsck.ext4
* /usr/bin/logsave
* /usr/bin/lsattr
* /usr/bin/mke2fs
* /usr/bin/mkfs.ext2
* /usr/bin/mkfs.ext3
* /usr/bin/mkfs.ext4
* /usr/bin/mklost+found
* /usr/bin/mk_cmds
* /usr/bin/resize2fs
* /usr/bin/tune2fs
* /usr/include/com_err.h
* /usr/include/e2p/e2p.h
* /usr/include/et/com_err.h
* /usr/include/ext2fs/bitops.h
* /usr/include/ext2fs/ext2fs.h
* /usr/include/ext2fs/ext2_err.h
* /usr/include/ext2fs/ext2_ext_attr.h
* /usr/include/ext2fs/ext2_fs.h
* /usr/include/ext2fs/ext2_io.h
* /usr/include/ext2fs/ext2_types.h
* /usr/include/ext2fs/ext3_extents.h
* /usr/include/ext2fs/hashmap.h
* /usr/include/ext2fs/qcow2.h
* /usr/include/ext2fs/tdb.h
* /usr/include/ss/ss.h
* /usr/include/ss/ss_err.h
* /usr/lib/libcom_err.so
* /usr/lib/libcom_err.so.2
* /usr/lib/libcom_err.so.2.1
* /usr/lib/libe2p.so
* /usr/lib/libe2p.so.2
* /usr/lib/libe2p.so.2.3
* /usr/lib/libext2fs.so
* /usr/lib/libext2fs.so.2
* /usr/lib/libext2fs.so.2.4
* /usr/lib/libss.so
* /usr/lib/libss.so.2
* /usr/lib/libss.so.2.0
* /usr/lib/pkgconfig/com_err.pc
* /usr/lib/pkgconfig/e2p.pc
* /usr/lib/pkgconfig/ext2fs.pc
* /usr/lib/pkgconfig/ss.pc
* /usr/lib/udev/rules.d/64-ext4.rules
* /usr/lib/udev/rules.d/96-e2scrub.rules
* /usr/share/doc/e2fsprogs-1.47.2/INSTALL
* /usr/share/doc/e2fsprogs-1.47.2/INSTALL.elfbin
* /usr/share/doc/e2fsprogs-1.47.2/README
* /usr/share/doc/e2fsprogs-1.47.2/RELEASE-NOTES
* /usr/share/et/et_c.awk
* /usr/share/et/et_h.awk
* /usr/share/info/libext2fs.info.gz
* /usr/share/locale/ca/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/cs/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/da/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/de/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/eo/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/es/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/fi/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/fr/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/fur/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/hu/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/id/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/it/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/ms/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/nl/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/pl/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/pt/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/ro/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/sr/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/sv/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/tr/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/uk/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/vi/LC_MESSAGES/e2fsprogs.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/e2fsprogs.mo
* /usr/share/man/man1/chattr.1.gz
* /usr/share/man/man1/compile_et.1.gz
* /usr/share/man/man1/lsattr.1.gz
* /usr/share/man/man1/mk_cmds.1.gz
* /usr/share/man/man3/com_err.3.gz
* /usr/share/man/man5/e2fsck.conf.5.gz
* /usr/share/man/man5/ext2.5.gz
* /usr/share/man/man5/ext3.5.gz
* /usr/share/man/man5/ext4.5.gz
* /usr/share/man/man5/mke2fs.conf.5.gz
* /usr/share/man/man8/badblocks.8.gz
* /usr/share/man/man8/debugfs.8.gz
* /usr/share/man/man8/dumpe2fs.8.gz
* /usr/share/man/man8/e2freefrag.8.gz
* /usr/share/man/man8/e2fsck.8.gz
* /usr/share/man/man8/e2image.8.gz
* /usr/share/man/man8/e2label.8.gz
* /usr/share/man/man8/e2mmpstatus.8.gz
* /usr/share/man/man8/e2scrub.8.gz
* /usr/share/man/man8/e2scrub_all.8.gz
* /usr/share/man/man8/e2undo.8.gz
* /usr/share/man/man8/e4crypt.8.gz
* /usr/share/man/man8/e4defrag.8.gz
* /usr/share/man/man8/filefrag.8.gz
* /usr/share/man/man8/fsck.ext2.8.gz
* /usr/share/man/man8/fsck.ext3.8.gz
* /usr/share/man/man8/fsck.ext4.8.gz
* /usr/share/man/man8/logsave.8.gz
* /usr/share/man/man8/mke2fs.8.gz
* /usr/share/man/man8/mkfs.ext2.8.gz
* /usr/share/man/man8/mkfs.ext3.8.gz
* /usr/share/man/man8/mkfs.ext4.8.gz
* /usr/share/man/man8/mklost+found.8.gz
* /usr/share/man/man8/resize2fs.8.gz
* /usr/share/man/man8/tune2fs.8.gz
* /usr/share/ss/ct_c.awk
* /usr/share/ss/ct_c.sed
