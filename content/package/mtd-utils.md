+++
draft = false
title = "mtd-utils 2.1.6-1"
version = "2.1.6-1"
description = "Utilities for dealing with MTD (flash) devices"
date = "2024-01-09T20:45:15"
aliases = "/packages/137096"
categories = ['apps-extra']
upstreamurl = "http://www.linux-mtd.infradead.org/"
arch = "x86_64"
size = "418264"
usize = "2300275"
sha1sum = "837cacb8943ab7e494b590819b3d6d6a6ac38b18"
depends = "['libuuid', 'lzo', 'openssl>=3.1.0', 'zlib>=1.2.12', 'zstd']"
reverse_depends = "['binwalk']"
+++
Utilities for dealing with MTD (flash) devices

{{< files text="show files" >}}* /usr/bin/docfdisk
* /usr/bin/doc_loadbios
* /usr/bin/fectest
* /usr/bin/flashcp
* /usr/bin/flash_erase
* /usr/bin/flash_eraseall
* /usr/bin/flash_lock
* /usr/bin/flash_otp_dump
* /usr/bin/flash_otp_erase
* /usr/bin/flash_otp_info
* /usr/bin/flash_otp_lock
* /usr/bin/flash_otp_write
* /usr/bin/flash_unlock
* /usr/bin/ftl_check
* /usr/bin/ftl_format
* /usr/bin/jffs2dump
* /usr/bin/jffs2reader
* /usr/bin/lsmtd
* /usr/bin/mkfs.jffs2
* /usr/bin/mkfs.ubifs
* /usr/bin/mount.ubifs
* /usr/bin/mtdinfo
* /usr/bin/mtdpart
* /usr/bin/mtd_debug
* /usr/bin/nanddump
* /usr/bin/nandflipbits
* /usr/bin/nandtest
* /usr/bin/nandwrite
* /usr/bin/nftldump
* /usr/bin/nftl_format
* /usr/bin/recv_image
* /usr/bin/rfddump
* /usr/bin/rfdformat
* /usr/bin/serve_image
* /usr/bin/sumtool
* /usr/bin/ubiattach
* /usr/bin/ubiblock
* /usr/bin/ubicrc32
* /usr/bin/ubidetach
* /usr/bin/ubiformat
* /usr/bin/ubihealthd
* /usr/bin/ubimkvol
* /usr/bin/ubinfo
* /usr/bin/ubinize
* /usr/bin/ubirename
* /usr/bin/ubirmvol
* /usr/bin/ubirsvol
* /usr/bin/ubiscan
* /usr/bin/ubiupdatevol
* /usr/lib/mtd-utils/mtd-utils/checkfs
* /usr/lib/mtd-utils/mtd-utils/filljffs2.sh
* /usr/lib/mtd-utils/mtd-utils/flash_readtest
* /usr/lib/mtd-utils/mtd-utils/flash_speed
* /usr/lib/mtd-utils/mtd-utils/flash_stress
* /usr/lib/mtd-utils/mtd-utils/flash_torture
* /usr/lib/mtd-utils/mtd-utils/free_space
* /usr/lib/mtd-utils/mtd-utils/fstest_monitor
* /usr/lib/mtd-utils/mtd-utils/fs_help_all.sh
* /usr/lib/mtd-utils/mtd-utils/fs_run_all.sh
* /usr/lib/mtd-utils/mtd-utils/fs_stress00.sh
* /usr/lib/mtd-utils/mtd-utils/fs_stress01.sh
* /usr/lib/mtd-utils/mtd-utils/ftrunc
* /usr/lib/mtd-utils/mtd-utils/fwrite00
* /usr/lib/mtd-utils/mtd-utils/gcd_hupper
* /usr/lib/mtd-utils/mtd-utils/integ
* /usr/lib/mtd-utils/mtd-utils/integck
* /usr/lib/mtd-utils/mtd-utils/io_basic
* /usr/lib/mtd-utils/mtd-utils/io_paral
* /usr/lib/mtd-utils/mtd-utils/io_read
* /usr/lib/mtd-utils/mtd-utils/io_update
* /usr/lib/mtd-utils/mtd-utils/JitterTest
* /usr/lib/mtd-utils/mtd-utils/load_nandsim.sh
* /usr/lib/mtd-utils/mtd-utils/makefiles
* /usr/lib/mtd-utils/mtd-utils/mkvol_bad
* /usr/lib/mtd-utils/mtd-utils/mkvol_basic
* /usr/lib/mtd-utils/mtd-utils/mkvol_paral
* /usr/lib/mtd-utils/mtd-utils/nandbiterrs
* /usr/lib/mtd-utils/mtd-utils/nandpagetest
* /usr/lib/mtd-utils/mtd-utils/nandsubpagetest
* /usr/lib/mtd-utils/mtd-utils/orph
* /usr/lib/mtd-utils/mtd-utils/pdfrun
* /usr/lib/mtd-utils/mtd-utils/perf
* /usr/lib/mtd-utils/mtd-utils/plotJittervsFill
* /usr/lib/mtd-utils/mtd-utils/rmdir00
* /usr/lib/mtd-utils/mtd-utils/rndrm00
* /usr/lib/mtd-utils/mtd-utils/rndrm99
* /usr/lib/mtd-utils/mtd-utils/rndwrite00
* /usr/lib/mtd-utils/mtd-utils/rsvol
* /usr/lib/mtd-utils/mtd-utils/runubitests.sh
* /usr/lib/mtd-utils/mtd-utils/stress_1
* /usr/lib/mtd-utils/mtd-utils/stress_2
* /usr/lib/mtd-utils/mtd-utils/stress_3
* /usr/lib/mtd-utils/mtd-utils/test_1
* /usr/lib/mtd-utils/mtd-utils/test_2
* /usr/lib/mtd-utils/mtd-utils/ubi-stress-test.sh
* /usr/lib/mtd-utils/mtd-utils/volrefcnt
* /usr/share/doc/mtd-utils-2.1.6/COPYING
* /usr/share/man/man1/mkfs.jffs2.1.gz
* /usr/share/man/man8/lsmtd.8.gz
* /usr/share/man/man8/ubinize.8.gz
{{< /files >}}