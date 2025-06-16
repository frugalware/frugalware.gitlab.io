+++
draft = false
title = "compiler-rt 20.1.7-1"
version = "20.1.7-1"
description = "Compiler runtime libraries for clang"
date = "2025-06-15T20:27:44"
aliases = "/packages/219834"
categories = ['devel']
upstreamurl = "http://www.llvm.org"
arch = "x86_64"
size = "2638452"
usize = "22183564"
sha1sum = "0c478c34824554fecd8b282726d78d8884e98b36"
depends = "[]"
+++
### Description: 
Compiler runtime libraries for clang

### Files: 
* /usr/lib/clang/20/include/sanitizer/allocator_interface.h
* /usr/lib/clang/20/include/sanitizer/asan_interface.h
* /usr/lib/clang/20/include/sanitizer/common_interface_defs.h
* /usr/lib/clang/20/include/sanitizer/coverage_interface.h
* /usr/lib/clang/20/include/sanitizer/dfsan_interface.h
* /usr/lib/clang/20/include/sanitizer/hwasan_interface.h
* /usr/lib/clang/20/include/sanitizer/linux_syscall_hooks.h
* /usr/lib/clang/20/include/sanitizer/lsan_interface.h
* /usr/lib/clang/20/include/sanitizer/memprof_interface.h
* /usr/lib/clang/20/include/sanitizer/msan_interface.h
* /usr/lib/clang/20/include/sanitizer/netbsd_syscall_hooks.h
* /usr/lib/clang/20/include/sanitizer/rtsan_interface.h
* /usr/lib/clang/20/include/sanitizer/scudo_interface.h
* /usr/lib/clang/20/include/sanitizer/tsan_interface.h
* /usr/lib/clang/20/include/sanitizer/tsan_interface_atomic.h
* /usr/lib/clang/20/include/sanitizer/ubsan_interface.h
* /usr/lib/clang/20/include/xray/xray_interface.h
* /usr/lib/clang/20/include/xray/xray_log_interface.h
* /usr/lib/clang/20/include/xray/xray_records.h
* /usr/lib/clang/20/lib/i386-frugalware-linux/clang_rt.crtbegin.o
* /usr/lib/clang/20/lib/i386-frugalware-linux/clang_rt.crtend.o
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.asan-preinit.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.asan.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.asan.so
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.asan_cxx.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.asan_static.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.builtins.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.cfi.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.cfi_diag.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.fuzzer.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.fuzzer_interceptors.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.fuzzer_no_main.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.gwp_asan.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.lsan.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.profile.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.safestack.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.scudo_standalone.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.scudo_standalone.so
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.scudo_standalone_cxx.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.stats.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.stats_client.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.ubsan_minimal.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.ubsan_minimal.so
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.ubsan_standalone.a
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.ubsan_standalone.so
* /usr/lib/clang/20/lib/i386-frugalware-linux/libclang_rt.ubsan_standalone_cxx.a
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/clang_rt.crtbegin.o
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/clang_rt.crtend.o
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.asan.a.syms
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.asan.so
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.asan_cxx.a.syms
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.dfsan.a.syms
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.dyndd.so
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.hwasan.a.syms
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.hwasan.so
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.hwasan_aliases.a.syms
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.hwasan_aliases.so
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.hwasan_aliases_cxx.a.syms
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.hwasan_cxx.a.syms
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.memprof.a.syms
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.memprof.so
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.memprof_cxx.a.syms
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.msan.a.syms
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.msan_cxx.a.syms
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.nsan.so
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.scudo_standalone.so
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.tsan.a.syms
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.tsan.so
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.tsan_cxx.a.syms
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.ubsan_minimal.a.syms
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.ubsan_minimal.so
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.ubsan_standalone.a.syms
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.ubsan_standalone.so
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/libclang_rt.ubsan_standalone_cxx.a.syms
* /usr/lib/clang/20/lib/x86_64-frugalware-linux/liborc_rt.a
* /usr/lib/clang/20/share/asan_ignorelist.txt
* /usr/lib/clang/20/share/cfi_ignorelist.txt
* /usr/lib/clang/20/share/dfsan_abilist.txt
* /usr/lib/clang/20/share/hwasan_ignorelist.txt
* /usr/lib/clang/20/share/msan_ignorelist.txt
