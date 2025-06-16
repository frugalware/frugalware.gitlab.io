+++
draft = false
title = "gperftools 2.16-1"
version = "2.16-1"
description = "Fast, multi-threaded malloc() and nifty performance analysis tools"
date = "2025-06-16T06:27:28"
aliases = "/packages/222742"
categories = ['lib']
upstreamurl = "https://github.com/gperftools/gperftools"
arch = "x86_64"
size = "576880"
usize = "2381711"
sha1sum = "b95fe3f553d4b03537b8bbe792c9da06ac63e477"
depends = "['libstdc++', 'libunwind']"
reverse_depends = "['libjxl', 'mariadb-libs', 'qemu']"
+++
### Description: 
Fast, multi-threaded malloc() and nifty performance analysis tools

### Files: 
* /usr/bin/pprof
* /usr/bin/pprof-symbolize
* /usr/include/gperftools/heap-checker.h
* /usr/include/gperftools/heap-profiler.h
* /usr/include/gperftools/malloc_extension.h
* /usr/include/gperftools/malloc_extension_c.h
* /usr/include/gperftools/malloc_hook.h
* /usr/include/gperftools/malloc_hook_c.h
* /usr/include/gperftools/nallocx.h
* /usr/include/gperftools/profiler.h
* /usr/include/gperftools/stacktrace.h
* /usr/include/gperftools/tcmalloc.h
* /usr/lib/libprofiler.so
* /usr/lib/libprofiler.so.0
* /usr/lib/libprofiler.so.0.5.13
* /usr/lib/libtcmalloc.so
* /usr/lib/libtcmalloc.so.4
* /usr/lib/libtcmalloc.so.4.5.18
* /usr/lib/libtcmalloc_and_profiler.so
* /usr/lib/libtcmalloc_and_profiler.so.4
* /usr/lib/libtcmalloc_and_profiler.so.4.6.13
* /usr/lib/libtcmalloc_debug.so
* /usr/lib/libtcmalloc_debug.so.4
* /usr/lib/libtcmalloc_debug.so.4.5.18
* /usr/lib/libtcmalloc_minimal.so
* /usr/lib/libtcmalloc_minimal.so.4
* /usr/lib/libtcmalloc_minimal.so.4.5.18
* /usr/lib/libtcmalloc_minimal_debug.so
* /usr/lib/libtcmalloc_minimal_debug.so.4
* /usr/lib/libtcmalloc_minimal_debug.so.4.5.18
* /usr/lib/pkgconfig/libprofiler.pc
* /usr/lib/pkgconfig/libtcmalloc.pc
* /usr/lib/pkgconfig/libtcmalloc_debug.pc
* /usr/lib/pkgconfig/libtcmalloc_minimal.pc
* /usr/lib/pkgconfig/libtcmalloc_minimal_debug.pc
* /usr/share/doc/gperftools-2.16/AUTHORS
* /usr/share/doc/gperftools-2.16/ChangeLog.old
* /usr/share/doc/gperftools-2.16/COPYING
* /usr/share/doc/gperftools-2.16/cpuprofile-fileformat.html
* /usr/share/doc/gperftools-2.16/cpuprofile.html
* /usr/share/doc/gperftools-2.16/designstyle.css
* /usr/share/doc/gperftools-2.16/heap-example1.png
* /usr/share/doc/gperftools-2.16/heapprofile.html
* /usr/share/doc/gperftools-2.16/heap_checker.html
* /usr/share/doc/gperftools-2.16/index.html
* /usr/share/doc/gperftools-2.16/INSTALL
* /usr/share/doc/gperftools-2.16/NEWS
* /usr/share/doc/gperftools-2.16/overview.dot
* /usr/share/doc/gperftools-2.16/overview.gif
* /usr/share/doc/gperftools-2.16/pageheap.dot
* /usr/share/doc/gperftools-2.16/pageheap.gif
* /usr/share/doc/gperftools-2.16/pprof-test-big.gif
* /usr/share/doc/gperftools-2.16/pprof-test.gif
* /usr/share/doc/gperftools-2.16/pprof-vsnprintf-big.gif
* /usr/share/doc/gperftools-2.16/pprof-vsnprintf.gif
* /usr/share/doc/gperftools-2.16/pprof_remote_servers.html
* /usr/share/doc/gperftools-2.16/README
* /usr/share/doc/gperftools-2.16/README_windows.txt
* /usr/share/doc/gperftools-2.16/spanmap.dot
* /usr/share/doc/gperftools-2.16/spanmap.gif
* /usr/share/doc/gperftools-2.16/t-test1.times.txt
* /usr/share/doc/gperftools-2.16/tcmalloc-opspercpusec.vs.threads.1024.bytes.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspercpusec.vs.threads.128.bytes.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspercpusec.vs.threads.131072.bytes.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspercpusec.vs.threads.16384.bytes.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspercpusec.vs.threads.2048.bytes.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspercpusec.vs.threads.256.bytes.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspercpusec.vs.threads.32768.bytes.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspercpusec.vs.threads.4096.bytes.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspercpusec.vs.threads.512.bytes.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspercpusec.vs.threads.64.bytes.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspercpusec.vs.threads.65536.bytes.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspercpusec.vs.threads.8192.bytes.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspersec.vs.size.1.threads.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspersec.vs.size.12.threads.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspersec.vs.size.16.threads.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspersec.vs.size.2.threads.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspersec.vs.size.20.threads.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspersec.vs.size.3.threads.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspersec.vs.size.4.threads.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspersec.vs.size.5.threads.png
* /usr/share/doc/gperftools-2.16/tcmalloc-opspersec.vs.size.8.threads.png
* /usr/share/doc/gperftools-2.16/tcmalloc.html
* /usr/share/doc/gperftools-2.16/threadheap.dot
* /usr/share/doc/gperftools-2.16/threadheap.gif
* /usr/share/man/man1/pprof.1.gz
