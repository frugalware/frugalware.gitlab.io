+++
draft = false
title = "elfutils 0.190-1"
version = "0.190-1"
description = "Collection of libraries and utilities for working with ELF object files and DWARF debugging information"
date = "2023-11-04T19:30:06"
aliases = "/packages/137191"
categories = ['base']
upstreamurl = "https://sourceware.org/elfutils/"
arch = "x86_64"
size = "794904"
usize = "4783608"
sha1sum = "e9a1842447f01319ef6ace173e64c6e3a4c872b6"
depends = "['bzip2>=1.0.6-16', 'glibc>=2.35', 'libstdc++>=11.3', 'xz>=5.2.4-2', 'zlib>=1.2.12', 'zstd']"
reverse_depends = "['aide', 'bcc', 'dracut', 'elfutils-debuginfod', 'glib2', 'lib32-mesa-libswrast', 'libosmesa', 'libsystemd', 'libva-mesa-driver', 'mesa-dri-drivers', 'mesa-nine', 'mesa-opemax', 'mesa-pipe-drivers', 'mesa-vdpau-drivers', 'modemmanager', 'perf', 'v4l-utils']"
+++
Collection of libraries and utilities for working with ELF object files and DWARF debugging information

{{< files text="show files" >}}* /etc/profile.d/debuginfod.csh
* /etc/profile.d/debuginfod.sh
* /usr/bin/eu-addr2line
* /usr/bin/eu-ar
* /usr/bin/eu-elfclassify
* /usr/bin/eu-elfcmp
* /usr/bin/eu-elfcompress
* /usr/bin/eu-elflint
* /usr/bin/eu-findtextrel
* /usr/bin/eu-make-debug-archive
* /usr/bin/eu-nm
* /usr/bin/eu-objdump
* /usr/bin/eu-ranlib
* /usr/bin/eu-readelf
* /usr/bin/eu-size
* /usr/bin/eu-srcfiles
* /usr/bin/eu-stack
* /usr/bin/eu-strings
* /usr/bin/eu-strip
* /usr/bin/eu-unstrip
* /usr/include/dwarf.h
* /usr/include/elfutils/elf-knowledge.h
* /usr/include/elfutils/known-dwarf.h
* /usr/include/elfutils/libasm.h
* /usr/include/elfutils/libdw.h
* /usr/include/elfutils/libdwelf.h
* /usr/include/elfutils/libdwfl.h
* /usr/include/elfutils/version.h
* /usr/include/gelf.h
* /usr/include/libelf.h
* /usr/include/nlist.h
* /usr/lib/libasm-0.190.so
* /usr/lib/libasm.so
* /usr/lib/libasm.so.1
* /usr/lib/libdw-0.190.so
* /usr/lib/libdw.so
* /usr/lib/libdw.so.1
* /usr/lib/libelf-0.190.so
* /usr/lib/libelf.so
* /usr/lib/libelf.so.1
* /usr/lib/pkgconfig/libdebuginfod.pc
* /usr/lib/pkgconfig/libdw.pc
* /usr/lib/pkgconfig/libelf.pc
* /usr/share/doc/elfutils-0.190/AUTHORS
* /usr/share/doc/elfutils-0.190/ChangeLog
* /usr/share/doc/elfutils-0.190/COPYING
* /usr/share/doc/elfutils-0.190/COPYING-GPLV2
* /usr/share/doc/elfutils-0.190/COPYING-LGPLV3
* /usr/share/doc/elfutils-0.190/INSTALL
* /usr/share/doc/elfutils-0.190/NEWS
* /usr/share/doc/elfutils-0.190/README
* /usr/share/doc/elfutils-0.190/THANKS
* /usr/share/doc/elfutils-0.190/TODO
* /usr/share/locale/de/LC_MESSAGES/elfutils.mo
* /usr/share/locale/en@boldquot/LC_MESSAGES/elfutils.mo
* /usr/share/locale/en@quot/LC_MESSAGES/elfutils.mo
* /usr/share/locale/es/LC_MESSAGES/elfutils.mo
* /usr/share/locale/ja/LC_MESSAGES/elfutils.mo
* /usr/share/locale/pl/LC_MESSAGES/elfutils.mo
* /usr/share/locale/uk/LC_MESSAGES/elfutils.mo
* /usr/share/man/man1/eu-elfclassify.1.gz
* /usr/share/man/man1/eu-readelf.1.gz
* /usr/share/man/man1/eu-srcfiles.1.gz
* /usr/share/man/man3/elf_begin.3.gz
* /usr/share/man/man3/elf_clone.3.gz
* /usr/share/man/man3/elf_getdata.3.gz
* /usr/share/man/man3/elf_update.3.gz
* /usr/share/man/man7/debuginfod-client-config.7.gz
{{< /files >}}