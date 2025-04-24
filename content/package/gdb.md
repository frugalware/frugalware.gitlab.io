+++
draft = false
title = "gdb 16.3-1"
version = "16.3-1"
description = "Gnu Project Debugger"
date = "2025-04-24T08:44:35"
aliases = "/packages/2380"
categories = ['devel']
upstreamurl = "http://www.gnu.org/software/gdb/download/"
arch = "x86_64"
size = "4757480"
usize = "13366546"
sha1sum = "695036414d7851c883f240916a4bff8c7fabcc9b"
depends = "['binutils', 'expat>=2.1.0-6', 'ncurses>=6.0-18', 'python3>=3.13', 'readline>=8.0', 'xxhash']"
reverse_depends = "['python3-pygdbmi', 'qtcreator', 'rr']"
+++
### Description: 
Gnu Project Debugger

### Files: 
* /usr/bin/gcore
* /usr/bin/gdb
* /usr/bin/gdb-add-index
* /usr/bin/gdbserver
* /usr/bin/gstack
* /usr/include/gdb/jit-reader.h
* /usr/lib/libinproctrace.so
* /usr/share/doc/gdb-16.3/ChangeLog
* /usr/share/doc/gdb-16.3/COPYING
* /usr/share/doc/gdb-16.3/COPYING.LIB
* /usr/share/doc/gdb-16.3/COPYING3
* /usr/share/doc/gdb-16.3/COPYING3.LIB
* /usr/share/doc/gdb-16.3/README
* /usr/share/doc/gdb-16.3/README-maintainer-mode
* /usr/share/gdb/python/gdb/command/explore.py
* /usr/share/gdb/python/gdb/command/frame_filters.py
* /usr/share/gdb/python/gdb/command/missing_files.py
* /usr/share/gdb/python/gdb/command/pretty_printers.py
* /usr/share/gdb/python/gdb/command/prompt.py
* /usr/share/gdb/python/gdb/command/type_printers.py
* /usr/share/gdb/python/gdb/command/unwinders.py
* /usr/share/gdb/python/gdb/command/xmethods.py
* /usr/share/gdb/python/gdb/command/__init__.py
* /usr/share/gdb/python/gdb/dap/breakpoint.py
* /usr/share/gdb/python/gdb/dap/bt.py
* /usr/share/gdb/python/gdb/dap/disassemble.py
* /usr/share/gdb/python/gdb/dap/evaluate.py
* /usr/share/gdb/python/gdb/dap/events.py
* /usr/share/gdb/python/gdb/dap/frames.py
* /usr/share/gdb/python/gdb/dap/globalvars.py
* /usr/share/gdb/python/gdb/dap/io.py
* /usr/share/gdb/python/gdb/dap/launch.py
* /usr/share/gdb/python/gdb/dap/locations.py
* /usr/share/gdb/python/gdb/dap/memory.py
* /usr/share/gdb/python/gdb/dap/modules.py
* /usr/share/gdb/python/gdb/dap/next.py
* /usr/share/gdb/python/gdb/dap/pause.py
* /usr/share/gdb/python/gdb/dap/scopes.py
* /usr/share/gdb/python/gdb/dap/server.py
* /usr/share/gdb/python/gdb/dap/sources.py
* /usr/share/gdb/python/gdb/dap/startup.py
* /usr/share/gdb/python/gdb/dap/state.py
* /usr/share/gdb/python/gdb/dap/threads.py
* /usr/share/gdb/python/gdb/dap/typecheck.py
* /usr/share/gdb/python/gdb/dap/varref.py
* /usr/share/gdb/python/gdb/dap/__init__.py
* /usr/share/gdb/python/gdb/disassembler.py
* /usr/share/gdb/python/gdb/FrameDecorator.py
* /usr/share/gdb/python/gdb/FrameIterator.py
* /usr/share/gdb/python/gdb/frames.py
* /usr/share/gdb/python/gdb/function/as_string.py
* /usr/share/gdb/python/gdb/function/caller_is.py
* /usr/share/gdb/python/gdb/function/strfns.py
* /usr/share/gdb/python/gdb/function/__init__.py
* /usr/share/gdb/python/gdb/missing_debug.py
* /usr/share/gdb/python/gdb/missing_files.py
* /usr/share/gdb/python/gdb/missing_objfile.py
* /usr/share/gdb/python/gdb/printer/__init__.py
* /usr/share/gdb/python/gdb/printing.py
* /usr/share/gdb/python/gdb/prompt.py
* /usr/share/gdb/python/gdb/ptwrite.py
* /usr/share/gdb/python/gdb/styling.py
* /usr/share/gdb/python/gdb/types.py
* /usr/share/gdb/python/gdb/unwinder.py
* /usr/share/gdb/python/gdb/xmethod.py
* /usr/share/gdb/python/gdb/__init__.py
* /usr/share/gdb/syscalls/aarch64-linux.xml
* /usr/share/gdb/syscalls/amd64-linux.xml
* /usr/share/gdb/syscalls/arm-linux.xml
* /usr/share/gdb/syscalls/freebsd.xml
* /usr/share/gdb/syscalls/gdb-syscalls.dtd
* /usr/share/gdb/syscalls/i386-linux.xml
* /usr/share/gdb/syscalls/loongarch-linux.xml
* /usr/share/gdb/syscalls/mips-n32-linux.xml
* /usr/share/gdb/syscalls/mips-n64-linux.xml
* /usr/share/gdb/syscalls/mips-o32-linux.xml
* /usr/share/gdb/syscalls/netbsd.xml
* /usr/share/gdb/syscalls/ppc-linux.xml
* /usr/share/gdb/syscalls/ppc64-linux.xml
* /usr/share/gdb/syscalls/s390-linux.xml
* /usr/share/gdb/syscalls/s390x-linux.xml
* /usr/share/gdb/syscalls/sparc-linux.xml
* /usr/share/gdb/syscalls/sparc64-linux.xml
* /usr/share/gdb/system-gdbinit/elinos.py
* /usr/share/gdb/system-gdbinit/wrs-linux.py
* /usr/share/info/annotate.info.gz
* /usr/share/info/gdb.info-1.gz
* /usr/share/info/gdb.info-2.gz
* /usr/share/info/gdb.info-3.gz
* /usr/share/info/gdb.info-4.gz
* /usr/share/info/gdb.info-5.gz
* /usr/share/info/gdb.info-6.gz
* /usr/share/info/gdb.info-7.gz
* /usr/share/info/gdb.info-8.gz
* /usr/share/info/gdb.info-9.gz
* /usr/share/info/gdb.info.gz
* /usr/share/info/stabs.info.gz
* /usr/share/man/man1/gcore.1.gz
* /usr/share/man/man1/gdb-add-index.1.gz
* /usr/share/man/man1/gdb.1.gz
* /usr/share/man/man1/gdbserver.1.gz
* /usr/share/man/man1/gstack.1.gz
* /usr/share/man/man5/gdbinit.5.gz
