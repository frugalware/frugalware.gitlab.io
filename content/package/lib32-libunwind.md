+++
draft = false
title = "lib32-libunwind 1.8.1-3"
version = "1.8.1-3"
description = "Portable and efficient C programming interface (API) to determine the call-chain of a program ( 32bit )"
date = "2024-12-20T23:39:42"
aliases = "/packages/219514"
categories = ['lib32-extra']
upstreamurl = "http://www.nongnu.org/libunwind"
arch = "x86_64"
size = "134360"
usize = "721917"
sha1sum = "052f7a745ea743e89a277a346c0d45a2723e6f29"
depends = "['lib32-xz>=5.2.2-4']"
reverse_depends = "['lib32-mesa-dri-drivers']"
+++
### Description: 
Portable and efficient C programming interface (API) to determine the call-chain of a program ( 32bit )

### Files: 
* /usr/i686-frugalware-linux/include/libunwind-common.h
* /usr/i686-frugalware-linux/include/libunwind-coredump.h
* /usr/i686-frugalware-linux/include/libunwind-dynamic.h
* /usr/i686-frugalware-linux/include/libunwind-ptrace.h
* /usr/i686-frugalware-linux/include/libunwind-x86.h
* /usr/i686-frugalware-linux/include/libunwind.h
* /usr/i686-frugalware-linux/include/unwind.h
* /usr/i686-frugalware-linux/libunwind/libunwind/check-namespace.sh
* /usr/i686-frugalware-linux/libunwind/libunwind/crasher
* /usr/i686-frugalware-linux/libunwind/libunwind/forker
* /usr/i686-frugalware-linux/libunwind/libunwind/Gperf-simple
* /usr/i686-frugalware-linux/libunwind/libunwind/Gperf-trace
* /usr/i686-frugalware-linux/libunwind/libunwind/Gtest-bt
* /usr/i686-frugalware-linux/libunwind/libunwind/Gtest-concurrent
* /usr/i686-frugalware-linux/libunwind/libunwind/Gtest-exc
* /usr/i686-frugalware-linux/libunwind/libunwind/Gtest-init
* /usr/i686-frugalware-linux/libunwind/libunwind/Gtest-resume-sig
* /usr/i686-frugalware-linux/libunwind/libunwind/Gtest-resume-sig-rt
* /usr/i686-frugalware-linux/libunwind/libunwind/Gtest-trace
* /usr/i686-frugalware-linux/libunwind/libunwind/Lperf-simple
* /usr/i686-frugalware-linux/libunwind/libunwind/Lperf-trace
* /usr/i686-frugalware-linux/libunwind/libunwind/Lrs-race
* /usr/i686-frugalware-linux/libunwind/libunwind/Ltest-bt
* /usr/i686-frugalware-linux/libunwind/libunwind/Ltest-concurrent
* /usr/i686-frugalware-linux/libunwind/libunwind/Ltest-exc
* /usr/i686-frugalware-linux/libunwind/libunwind/Ltest-init
* /usr/i686-frugalware-linux/libunwind/libunwind/Ltest-init-local-signal
* /usr/i686-frugalware-linux/libunwind/libunwind/Ltest-mem-validate
* /usr/i686-frugalware-linux/libunwind/libunwind/Ltest-nocalloc
* /usr/i686-frugalware-linux/libunwind/libunwind/Ltest-nomalloc
* /usr/i686-frugalware-linux/libunwind/libunwind/Ltest-resume-sig
* /usr/i686-frugalware-linux/libunwind/libunwind/Ltest-resume-sig-rt
* /usr/i686-frugalware-linux/libunwind/libunwind/Ltest-trace
* /usr/i686-frugalware-linux/libunwind/libunwind/Ltest-varargs
* /usr/i686-frugalware-linux/libunwind/libunwind/mapper
* /usr/i686-frugalware-linux/libunwind/libunwind/run-coredump-unwind
* /usr/i686-frugalware-linux/libunwind/libunwind/run-coredump-unwind-mdi
* /usr/i686-frugalware-linux/libunwind/libunwind/run-ptrace-mapper
* /usr/i686-frugalware-linux/libunwind/libunwind/run-ptrace-misc
* /usr/i686-frugalware-linux/libunwind/libunwind/test-async-sig
* /usr/i686-frugalware-linux/libunwind/libunwind/test-coredump-unwind
* /usr/i686-frugalware-linux/libunwind/libunwind/test-flush-cache
* /usr/i686-frugalware-linux/libunwind/libunwind/test-init-remote
* /usr/i686-frugalware-linux/libunwind/libunwind/test-mem
* /usr/i686-frugalware-linux/libunwind/libunwind/test-proc-info
* /usr/i686-frugalware-linux/libunwind/libunwind/test-ptrace
* /usr/i686-frugalware-linux/libunwind/libunwind/test-ptrace-misc
* /usr/i686-frugalware-linux/libunwind/libunwind/test-reg-state
* /usr/i686-frugalware-linux/libunwind/libunwind/test-runner
* /usr/i686-frugalware-linux/libunwind/libunwind/test-setjmp
* /usr/i686-frugalware-linux/libunwind/libunwind/test-static-link
* /usr/i686-frugalware-linux/libunwind/libunwind/test-strerror
* /usr/lib32/libunwind-coredump.so
* /usr/lib32/libunwind-coredump.so.0
* /usr/lib32/libunwind-coredump.so.0.0.0
* /usr/lib32/libunwind-generic.so
* /usr/lib32/libunwind-ptrace.so
* /usr/lib32/libunwind-ptrace.so.0
* /usr/lib32/libunwind-ptrace.so.0.0.0
* /usr/lib32/libunwind-setjmp.so
* /usr/lib32/libunwind-setjmp.so.0
* /usr/lib32/libunwind-setjmp.so.0.0.0
* /usr/lib32/libunwind-x86.so
* /usr/lib32/libunwind-x86.so.8
* /usr/lib32/libunwind-x86.so.8.1.0
* /usr/lib32/libunwind.so
* /usr/lib32/libunwind.so.8
* /usr/lib32/libunwind.so.8.1.0
* /usr/lib32/pkgconfig/libunwind-coredump.pc
* /usr/lib32/pkgconfig/libunwind-generic.pc
* /usr/lib32/pkgconfig/libunwind-ptrace.pc
* /usr/lib32/pkgconfig/libunwind-setjmp.pc
* /usr/lib32/pkgconfig/libunwind.pc
