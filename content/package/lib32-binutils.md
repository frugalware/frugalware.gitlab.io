+++
draft = false
title = "lib32-binutils 2.42-2"
version = "2.42-2"
description = "A set of programs to assemble and manipulate binary and object files ( 32bit )"
date = "2024-02-02T23:23:49"
aliases = "/packages/221229"
categories = ['lib32-extra']
upstreamurl = "http://www.gnu.org/software/binutils/"
arch = "x86_64"
size = "4406388"
usize = "20594089"
sha1sum = "1dbf8c679f7c8ce0e74c6f3048d09f6616037d2b"
depends = "['lib32-zstd']"
reverse_depends = "['lib32-cairo']"
+++
A set of programs to assemble and manipulate binary and object files ( 32bit ){{< files text="show files" >}}* /usr/i686-frugalware-linux/bin/addr2line
* /usr/i686-frugalware-linux/bin/ar
* /usr/i686-frugalware-linux/bin/as
* /usr/i686-frugalware-linux/bin/c++filt
* /usr/i686-frugalware-linux/bin/dwp
* /usr/i686-frugalware-linux/bin/elfedit
* /usr/i686-frugalware-linux/bin/gp-archive
* /usr/i686-frugalware-linux/bin/gp-collect-app
* /usr/i686-frugalware-linux/bin/gp-display-html
* /usr/i686-frugalware-linux/bin/gp-display-src
* /usr/i686-frugalware-linux/bin/gp-display-text
* /usr/i686-frugalware-linux/bin/gprof
* /usr/i686-frugalware-linux/bin/gprofng
* /usr/i686-frugalware-linux/bin/ld
* /usr/i686-frugalware-linux/bin/ld.bfd
* /usr/i686-frugalware-linux/bin/ld.gold
* /usr/i686-frugalware-linux/bin/nm
* /usr/i686-frugalware-linux/bin/objcopy
* /usr/i686-frugalware-linux/bin/objdump
* /usr/i686-frugalware-linux/bin/ranlib
* /usr/i686-frugalware-linux/bin/readelf
* /usr/i686-frugalware-linux/bin/size
* /usr/i686-frugalware-linux/bin/strings
* /usr/i686-frugalware-linux/bin/strip
* /usr/i686-frugalware-linux/include/ansidecl.h
* /usr/i686-frugalware-linux/include/bfd.h
* /usr/i686-frugalware-linux/include/bfdlink.h
* /usr/i686-frugalware-linux/include/collectorAPI.h
* /usr/i686-frugalware-linux/include/ctf-api.h
* /usr/i686-frugalware-linux/include/ctf.h
* /usr/i686-frugalware-linux/include/diagnostics.h
* /usr/i686-frugalware-linux/include/dis-asm.h
* /usr/i686-frugalware-linux/include/libcollector.h
* /usr/i686-frugalware-linux/include/libfcollector.h
* /usr/i686-frugalware-linux/include/libiberty/ansidecl.h
* /usr/i686-frugalware-linux/include/libiberty/demangle.h
* /usr/i686-frugalware-linux/include/libiberty/dyn-string.h
* /usr/i686-frugalware-linux/include/libiberty/fibheap.h
* /usr/i686-frugalware-linux/include/libiberty/floatformat.h
* /usr/i686-frugalware-linux/include/libiberty/hashtab.h
* /usr/i686-frugalware-linux/include/libiberty/libiberty.h
* /usr/i686-frugalware-linux/include/libiberty/objalloc.h
* /usr/i686-frugalware-linux/include/libiberty/partition.h
* /usr/i686-frugalware-linux/include/libiberty/safe-ctype.h
* /usr/i686-frugalware-linux/include/libiberty/sort.h
* /usr/i686-frugalware-linux/include/libiberty/splay-tree.h
* /usr/i686-frugalware-linux/include/libiberty/timeval-utils.h
* /usr/i686-frugalware-linux/include/plugin-api.h
* /usr/i686-frugalware-linux/include/sframe-api.h
* /usr/i686-frugalware-linux/include/sframe.h
* /usr/i686-frugalware-linux/include/symcat.h
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.x
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xbn
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xc
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xce
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xd
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xdc
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xdce
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xde
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xdw
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xdwe
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xe
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xn
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xr
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xs
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xsc
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xsce
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xse
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xsw
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xswe
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xu
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xw
* /usr/i686-frugalware-linux/lib/ldscripts/elf32_x86_64.xwe
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.x
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xbn
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xc
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xce
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xd
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xdc
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xdce
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xde
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xdw
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xdwe
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xe
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xn
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xr
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xs
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xsc
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xsce
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xse
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xsw
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xswe
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xu
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xw
* /usr/i686-frugalware-linux/lib/ldscripts/elf_i386.xwe
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.x
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xbn
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xc
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xce
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xd
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xdc
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xdce
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xde
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xdw
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xdwe
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xe
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xn
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xr
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xs
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xsc
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xsce
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xse
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xsw
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xswe
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xu
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xw
* /usr/i686-frugalware-linux/lib/ldscripts/elf_iamcu.xwe
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.x
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xbn
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xc
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xce
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xd
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xdc
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xdce
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xde
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xdw
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xdwe
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xe
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xn
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xr
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xs
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xsc
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xsce
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xse
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xsw
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xswe
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xu
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xw
* /usr/i686-frugalware-linux/lib/ldscripts/elf_x86_64.xwe
* /usr/i686-frugalware-linux/lib/ldscripts/stamp
* /usr/lib32/bfd-plugins/libdep.so
* /usr/lib32/gprofng/libgp-collector.so
* /usr/lib32/gprofng/libgp-collectorAPI.so
* /usr/lib32/gprofng/libgp-heap.so
* /usr/lib32/gprofng/libgp-iotrace.so
* /usr/lib32/gprofng/libgp-sync.so
* /usr/lib32/libbfd-2.42.so
* /usr/lib32/libbfd.so
* /usr/lib32/libctf-nobfd.so
* /usr/lib32/libctf-nobfd.so.0
* /usr/lib32/libctf-nobfd.so.0.0.0
* /usr/lib32/libctf.so
* /usr/lib32/libctf.so.0
* /usr/lib32/libctf.so.0.0.0
* /usr/lib32/libgprofng.so
* /usr/lib32/libgprofng.so.0
* /usr/lib32/libgprofng.so.0.0.0
* /usr/lib32/libopcodes-2.42.so
* /usr/lib32/libopcodes.so
* /usr/lib32/libsframe.so
* /usr/lib32/libsframe.so.1
* /usr/lib32/libsframe.so.1.0.0
{{< /files >}}