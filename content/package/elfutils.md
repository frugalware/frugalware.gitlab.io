+++
draft = false
title = "elfutils 0.193-3"
version = "0.193-3"
description = "Collection of libraries and utilities for working with ELF object files and DWARF debugging information"
date = "2025-06-25T13:43:28"
aliases = "/packages/137191"
categories = ['base']
upstreamurl = "https://sourceware.org/elfutils/"
arch = "x86_64"
size = "894176"
usize = "5148514"
sha1sum = "3570f74e1d52aeca4a285e03bd34c66522262f88"
depends = "['bzip2>=1.0.6-16', 'glibc>=2.41', 'json-c', 'libarchive', 'libstdc++>=11.3', 'xz>=5.2.4-2', 'zlib-ng', 'zstd']"
reverse_depends = "['aide', 'bcc', 'dracut', 'elfutils-debuginfod', 'glib2', 'lib32-mesa-libswrast', 'libbpf', 'libsystemd', 'libva-mesa-driver', 'mesa-dri-drivers', 'mesa-libswrast', 'mesa-vdpau-drivers', 'modemmanager', 'perf', 'v4l-utils']"
+++
### Description: 
Collection of libraries and utilities for working with ELF object files and DWARF debugging information

### Files: 
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
* /usr/include/elfutils/libdwfl_stacktrace.h
* /usr/include/elfutils/version.h
* /usr/include/gelf.h
* /usr/include/libelf.h
* /usr/include/nlist.h
* /usr/lib/libasm-0.193.so
* /usr/lib/libasm.so
* /usr/lib/libasm.so.1
* /usr/lib/libdw-0.193.so
* /usr/lib/libdw.so
* /usr/lib/libdw.so.1
* /usr/lib/libelf-0.193.so
* /usr/lib/libelf.so
* /usr/lib/libelf.so.1
* /usr/lib/pkgconfig/libdebuginfod.pc
* /usr/lib/pkgconfig/libdw.pc
* /usr/lib/pkgconfig/libelf.pc
* /usr/share/doc/elfutils-0.193/AUTHORS
* /usr/share/doc/elfutils-0.193/ChangeLog
* /usr/share/doc/elfutils-0.193/COPYING
* /usr/share/doc/elfutils-0.193/COPYING-GPLV2
* /usr/share/doc/elfutils-0.193/COPYING-LGPLV3
* /usr/share/doc/elfutils-0.193/INSTALL
* /usr/share/doc/elfutils-0.193/NEWS
* /usr/share/doc/elfutils-0.193/README
* /usr/share/doc/elfutils-0.193/THANKS
* /usr/share/doc/elfutils-0.193/TODO
* /usr/share/fish/vendor_conf.d/debuginfod.fish
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
* /usr/share/man/man3/elf32_checksum.3.gz
* /usr/share/man/man3/elf32_fsize.3.gz
* /usr/share/man/man3/elf32_getchdr.3.gz
* /usr/share/man/man3/elf32_getehdr.3.gz
* /usr/share/man/man3/elf32_getphdr.3.gz
* /usr/share/man/man3/elf32_getshdr.3.gz
* /usr/share/man/man3/elf32_newehdr.3.gz
* /usr/share/man/man3/elf32_newphdr.3.gz
* /usr/share/man/man3/elf32_offscn.3.gz
* /usr/share/man/man3/elf32_xlatetof.3.gz
* /usr/share/man/man3/elf32_xlatetom.3.gz
* /usr/share/man/man3/elf64_checksum.3.gz
* /usr/share/man/man3/elf64_fsize.3.gz
* /usr/share/man/man3/elf64_getchdr.3.gz
* /usr/share/man/man3/elf64_getehdr.3.gz
* /usr/share/man/man3/elf64_getphdr.3.gz
* /usr/share/man/man3/elf64_getshdr.3.gz
* /usr/share/man/man3/elf64_newehdr.3.gz
* /usr/share/man/man3/elf64_newphdr.3.gz
* /usr/share/man/man3/elf64_offscn.3.gz
* /usr/share/man/man3/elf64_xlatetof.3.gz
* /usr/share/man/man3/elf64_xlatetom.3.gz
* /usr/share/man/man3/elf_begin.3.gz
* /usr/share/man/man3/elf_clone.3.gz
* /usr/share/man/man3/elf_errmsg.3.gz
* /usr/share/man/man3/elf_errno.3.gz
* /usr/share/man/man3/elf_getdata.3.gz
* /usr/share/man/man3/elf_getscn.3.gz
* /usr/share/man/man3/elf_ndxscn.3.gz
* /usr/share/man/man3/elf_update.3.gz
* /usr/share/man/man3/elf_version.3.gz
* /usr/share/man/man3/libelf.3.gz
* /usr/share/man/man7/debuginfod-client-config.7.gz
* /usr/share/man/man8/debuginfod.8.gz
* /usr/share/man/man8/debuginfod.service.8.gz
