+++
draft = false
title = "dev86 0.16.21-5"
version = "0.16.21-5"
description = "The dev86 package provides an assembler and linker for real mode 80x86 instructions"
date = "2022-02-16T10:20:36"
aliases = "/packages/14296"
categories = ['devel-extra']
upstreamurl = "https://github.com/lkundrak/dev86"
arch = "x86_64"
size = "233624"
usize = "859873"
sha1sum = "7d5a1c53ae1eaf7218900b06f2faad6452a1ce8c"
depends = "['bin86', 'glibc>=2.27-2']"
reverse_depends = "['virtualbox']"
+++
### Description: 
The dev86 package provides an assembler and linker for real mode 80x86 instructions

### Files: 
* /usr/bin/ar86
* /usr/bin/bcc
* /usr/lib/bcc/as86_encap
* /usr/lib/bcc/bcc-cc1
* /usr/lib/bcc/bcc-cpp
* /usr/lib/bcc/copt
* /usr/lib/bcc/crt0.o
* /usr/lib/bcc/i386/crt0.o
* /usr/lib/bcc/i386/libc.a
* /usr/lib/bcc/i386/rules.386
* /usr/lib/bcc/i386/rules.end
* /usr/lib/bcc/i386/rules.start
* /usr/lib/bcc/include/a.out.h
* /usr/lib/bcc/include/ar.h
* /usr/lib/bcc/include/arch/errno.h
* /usr/lib/bcc/include/arch/ioctl.h
* /usr/lib/bcc/include/arch/stat.h
* /usr/lib/bcc/include/arch/types.h
* /usr/lib/bcc/include/asm/limits.h
* /usr/lib/bcc/include/asm/types.h
* /usr/lib/bcc/include/assert.h
* /usr/lib/bcc/include/bios.h
* /usr/lib/bcc/include/bsd/bsd.h
* /usr/lib/bcc/include/bsd/errno.h
* /usr/lib/bcc/include/bsd/sgtty.h
* /usr/lib/bcc/include/bsd/signal.h
* /usr/lib/bcc/include/bsd/stdlib.h
* /usr/lib/bcc/include/bsd/sys/ttychars.h
* /usr/lib/bcc/include/bsd/tzfile.h
* /usr/lib/bcc/include/bsd/unistd.h
* /usr/lib/bcc/include/conio.h
* /usr/lib/bcc/include/ctype.h
* /usr/lib/bcc/include/dirent.h
* /usr/lib/bcc/include/dos.h
* /usr/lib/bcc/include/errno.h
* /usr/lib/bcc/include/fcntl.h
* /usr/lib/bcc/include/features.h
* /usr/lib/bcc/include/generic/errno.h
* /usr/lib/bcc/include/generic/fcntl.h
* /usr/lib/bcc/include/generic/types.h
* /usr/lib/bcc/include/getopt.h
* /usr/lib/bcc/include/grp.h
* /usr/lib/bcc/include/limits.h
* /usr/lib/bcc/include/linux/errno.h
* /usr/lib/bcc/include/linux/fcntl.h
* /usr/lib/bcc/include/linux/ioctl.h
* /usr/lib/bcc/include/linux/mman.h
* /usr/lib/bcc/include/linux/resource.h
* /usr/lib/bcc/include/linux/stat.h
* /usr/lib/bcc/include/linux/termios.h
* /usr/lib/bcc/include/linux/types.h
* /usr/lib/bcc/include/linux/utsname.h
* /usr/lib/bcc/include/linux/vm86.h
* /usr/lib/bcc/include/linuxmt/errno.h
* /usr/lib/bcc/include/linuxmt/fcntl.h
* /usr/lib/bcc/include/linuxmt/ioctl.h
* /usr/lib/bcc/include/linuxmt/resource.h
* /usr/lib/bcc/include/linuxmt/stat.h
* /usr/lib/bcc/include/linuxmt/termios.h
* /usr/lib/bcc/include/linuxmt/types.h
* /usr/lib/bcc/include/malloc.h
* /usr/lib/bcc/include/math.h
* /usr/lib/bcc/include/memory.h
* /usr/lib/bcc/include/msdos/errno.h
* /usr/lib/bcc/include/msdos/fcntl.h
* /usr/lib/bcc/include/msdos/types.h
* /usr/lib/bcc/include/paths.h
* /usr/lib/bcc/include/pwd.h
* /usr/lib/bcc/include/regexp.h
* /usr/lib/bcc/include/regmagic.h
* /usr/lib/bcc/include/search.h
* /usr/lib/bcc/include/setjmp.h
* /usr/lib/bcc/include/signal.h
* /usr/lib/bcc/include/stdarg.h
* /usr/lib/bcc/include/stddef.h
* /usr/lib/bcc/include/stdio.h
* /usr/lib/bcc/include/stdlib.h
* /usr/lib/bcc/include/string.h
* /usr/lib/bcc/include/strings.h
* /usr/lib/bcc/include/sys/cdefs.h
* /usr/lib/bcc/include/sys/errno.h
* /usr/lib/bcc/include/sys/fcntl.h
* /usr/lib/bcc/include/sys/file.h
* /usr/lib/bcc/include/sys/ioctl.h
* /usr/lib/bcc/include/sys/mman.h
* /usr/lib/bcc/include/sys/param.h
* /usr/lib/bcc/include/sys/resource.h
* /usr/lib/bcc/include/sys/signal.h
* /usr/lib/bcc/include/sys/socket.h
* /usr/lib/bcc/include/sys/stat.h
* /usr/lib/bcc/include/sys/time.h
* /usr/lib/bcc/include/sys/times.h
* /usr/lib/bcc/include/sys/types.h
* /usr/lib/bcc/include/sys/utsname.h
* /usr/lib/bcc/include/sys/vm86.h
* /usr/lib/bcc/include/sys/wait.h
* /usr/lib/bcc/include/termcap.h
* /usr/lib/bcc/include/termio.h
* /usr/lib/bcc/include/termios.h
* /usr/lib/bcc/include/time.h
* /usr/lib/bcc/include/unistd.h
* /usr/lib/bcc/include/utime.h
* /usr/lib/bcc/include/utmp.h
* /usr/lib/bcc/include/varargs.h
* /usr/lib/bcc/libbcc.a
* /usr/lib/bcc/libbsd.a
* /usr/lib/bcc/libc.a
* /usr/lib/bcc/libc_f.a
* /usr/lib/bcc/libc_s.a
* /usr/lib/bcc/libdos.a
* /usr/lib/bcc/rules.186
* /usr/lib/bcc/rules.386
* /usr/lib/bcc/rules.86
* /usr/lib/bcc/rules.end
* /usr/lib/bcc/rules.i
* /usr/lib/bcc/rules.net
* /usr/lib/bcc/rules.start
* /usr/lib/bcc/unproto
* /usr/share/doc/dev86-0.16.21/COPYING
* /usr/share/doc/dev86-0.16.21/README
* /usr/share/man/man1/bcc.1.gz
* /usr/share/man/man1/elks.1.gz
* /usr/share/man/man1/elksemu.1.gz
