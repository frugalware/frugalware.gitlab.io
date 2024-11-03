+++
draft = false
title = "compiler-rt 19.1.3-2"
version = "19.1.3-2"
description = "Compiler runtime libraries for clang"
date = "2024-11-03T15:38:40"
aliases = "/packages/219834"
categories = ['devel']
upstreamurl = "http://www.llvm.org"
arch = "x86_64"
size = "2501780"
usize = "21497411"
sha1sum = "9afadb7f10d9118419de846104c941dbcc07e54d"
depends = "[]"
+++
### Description: 
Compiler runtime libraries for clang

### Files: 
* /usr/lib/clang/19/include/sanitizer/allocator_interface.h
* /usr/lib/clang/19/include/sanitizer/asan_interface.h
* /usr/lib/clang/19/include/sanitizer/common_interface_defs.h
* /usr/lib/clang/19/include/sanitizer/coverage_interface.h
* /usr/lib/clang/19/include/sanitizer/dfsan_interface.h
* /usr/lib/clang/19/include/sanitizer/hwasan_interface.h
* /usr/lib/clang/19/include/sanitizer/linux_syscall_hooks.h
* /usr/lib/clang/19/include/sanitizer/lsan_interface.h
* /usr/lib/clang/19/include/sanitizer/memprof_interface.h
* /usr/lib/clang/19/include/sanitizer/msan_interface.h
* /usr/lib/clang/19/include/sanitizer/netbsd_syscall_hooks.h
* /usr/lib/clang/19/include/sanitizer/scudo_interface.h
* /usr/lib/clang/19/include/sanitizer/tsan_interface.h
* /usr/lib/clang/19/include/sanitizer/tsan_interface_atomic.h
* /usr/lib/clang/19/include/sanitizer/ubsan_interface.h
* /usr/lib/clang/19/include/xray/xray_interface.h
* /usr/lib/clang/19/include/xray/xray_log_interface.h
* /usr/lib/clang/19/include/xray/xray_records.h
* /usr/lib/clang/19/lib/i386-frugalware-linux/clang_rt.crtbegin.o
* /usr/lib/clang/19/lib/i386-frugalware-linux/clang_rt.crtend.o
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.asan-preinit.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.asan.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.asan.so
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.asan_cxx.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.asan_static.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.builtins.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.cfi.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.cfi_diag.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.fuzzer.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.fuzzer_interceptors.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.fuzzer_no_main.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.gwp_asan.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.lsan.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.profile.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.safestack.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.scudo_standalone.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.scudo_standalone.so
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.scudo_standalone_cxx.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.stats.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.stats_client.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.ubsan_minimal.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.ubsan_minimal.so
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.ubsan_standalone.a
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.ubsan_standalone.so
* /usr/lib/clang/19/lib/i386-frugalware-linux/libclang_rt.ubsan_standalone_cxx.a
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/clang_rt.crtbegin.o
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/clang_rt.crtend.o
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.asan.a.syms
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.asan.so
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.asan_cxx.a.syms
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.dfsan.a.syms
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.dyndd.so
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.hwasan.a.syms
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.hwasan.so
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.hwasan_aliases.a.syms
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.hwasan_aliases.so
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.hwasan_aliases_cxx.a.syms
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.hwasan_cxx.a.syms
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.memprof.a.syms
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.memprof.so
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.memprof_cxx.a.syms
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.msan.a.syms
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.msan_cxx.a.syms
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.nsan.so
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.scudo_standalone.so
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.tsan.a.syms
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.tsan.so
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.tsan_cxx.a.syms
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.ubsan_minimal.a.syms
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.ubsan_minimal.so
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.ubsan_standalone.a.syms
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.ubsan_standalone.so
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/libclang_rt.ubsan_standalone_cxx.a.syms
* /usr/lib/clang/19/lib/x86_64-frugalware-linux/liborc_rt.a
* /usr/lib/clang/19/share/asan_ignorelist.txt
* /usr/lib/clang/19/share/cfi_ignorelist.txt
* /usr/lib/clang/19/share/dfsan_abilist.txt
* /usr/lib/clang/19/share/hwasan_ignorelist.txt
* /usr/lib/clang/19/share/msan_ignorelist.txt
