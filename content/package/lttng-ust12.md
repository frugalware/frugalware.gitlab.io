+++
draft = false
title = "lttng-ust12 2.12.10-1"
version = "2.12.10-1"
description = "Userspace tracing library for LTTng"
date = "2024-07-22T15:35:48"
aliases = "/packages/221545"
categories = ['devel-extra']
upstreamurl = "http://www.lttng.org"
arch = "x86_64"
size = "275392"
usize = "1255696"
sha1sum = "8e67985d19b7119cd5a0a289fbd4d411435b87c5"
depends = "['liburcu>=0.7.2', 'numactl', 'util-linux']"
reverse_depends = "['duplicati']"
+++
### Description: 
Userspace tracing library for LTTng

### Files: 
* /usr/bin/lttng-gen-tp
* /usr/include/lttng/align.h
* /usr/include/lttng/bug.h
* /usr/include/lttng/lttng-ust-tracef.h
* /usr/include/lttng/lttng-ust-tracelog.h
* /usr/include/lttng/ringbuffer-abi.h
* /usr/include/lttng/ringbuffer-config.h
* /usr/include/lttng/tracef.h
* /usr/include/lttng/tracelog.h
* /usr/include/lttng/tracepoint-event.h
* /usr/include/lttng/tracepoint-rcu.h
* /usr/include/lttng/tracepoint-types.h
* /usr/include/lttng/tracepoint.h
* /usr/include/lttng/ust-abi.h
* /usr/include/lttng/ust-clock.h
* /usr/include/lttng/ust-compiler.h
* /usr/include/lttng/ust-config.h
* /usr/include/lttng/ust-ctl.h
* /usr/include/lttng/ust-elf.h
* /usr/include/lttng/ust-endian.h
* /usr/include/lttng/ust-error.h
* /usr/include/lttng/ust-events.h
* /usr/include/lttng/ust-getcpu.h
* /usr/include/lttng/ust-tracepoint-event-nowrite.h
* /usr/include/lttng/ust-tracepoint-event-reset.h
* /usr/include/lttng/ust-tracepoint-event-write.h
* /usr/include/lttng/ust-tracepoint-event.h
* /usr/include/lttng/ust-tracer.h
* /usr/include/lttng/ust-version.h
* /usr/include/lttng/ust.h
* /usr/lib/liblttng-ust-ctl.so
* /usr/lib/liblttng-ust-ctl.so.4
* /usr/lib/liblttng-ust-ctl.so.4.0.0
* /usr/lib/liblttng-ust-cyg-profile-fast.so
* /usr/lib/liblttng-ust-cyg-profile-fast.so.0
* /usr/lib/liblttng-ust-cyg-profile-fast.so.0.0.0
* /usr/lib/liblttng-ust-cyg-profile.so
* /usr/lib/liblttng-ust-cyg-profile.so.0
* /usr/lib/liblttng-ust-cyg-profile.so.0.0.0
* /usr/lib/liblttng-ust-dl.so
* /usr/lib/liblttng-ust-dl.so.0
* /usr/lib/liblttng-ust-dl.so.0.0.0
* /usr/lib/liblttng-ust-fd.so
* /usr/lib/liblttng-ust-fd.so.0
* /usr/lib/liblttng-ust-fd.so.0.0.0
* /usr/lib/liblttng-ust-fork.so
* /usr/lib/liblttng-ust-fork.so.0
* /usr/lib/liblttng-ust-fork.so.0.0.0
* /usr/lib/liblttng-ust-libc-wrapper.so
* /usr/lib/liblttng-ust-libc-wrapper.so.0
* /usr/lib/liblttng-ust-libc-wrapper.so.0.0.0
* /usr/lib/liblttng-ust-pthread-wrapper.so
* /usr/lib/liblttng-ust-pthread-wrapper.so.0
* /usr/lib/liblttng-ust-pthread-wrapper.so.0.0.0
* /usr/lib/liblttng-ust-tracepoint.so
* /usr/lib/liblttng-ust-tracepoint.so.0
* /usr/lib/liblttng-ust-tracepoint.so.0.0.0
* /usr/lib/liblttng-ust.so
* /usr/lib/liblttng-ust.so.0
* /usr/lib/liblttng-ust.so.0.0.0
* /usr/lib/pkgconfig/lttng-ust-ctl.pc
* /usr/lib/pkgconfig/lttng-ust.pc
* /usr/share/doc/lttng-ust12-2.12.10/ChangeLog
* /usr/share/doc/lttng-ust12-2.12.10/COPYING
* /usr/share/doc/lttng-ust12-2.12.10/examples/clock-override/lttng-ust-clock-override-example.c
* /usr/share/doc/lttng-ust12-2.12.10/examples/clock-override/Makefile
* /usr/share/doc/lttng-ust12-2.12.10/examples/clock-override/README
* /usr/share/doc/lttng-ust12-2.12.10/examples/clock-override/run-clock-override
* /usr/share/doc/lttng-ust12-2.12.10/examples/cmake-multiple-shared-libraries/aligner-lib.cpp
* /usr/share/doc/lttng-ust12-2.12.10/examples/cmake-multiple-shared-libraries/aligner-lib.h
* /usr/share/doc/lttng-ust12-2.12.10/examples/cmake-multiple-shared-libraries/aligner.cpp
* /usr/share/doc/lttng-ust12-2.12.10/examples/cmake-multiple-shared-libraries/CMakeLists.txt
* /usr/share/doc/lttng-ust12-2.12.10/examples/cmake-multiple-shared-libraries/FindLTTngUST.cmake
* /usr/share/doc/lttng-ust12-2.12.10/examples/cmake-multiple-shared-libraries/README.md
* /usr/share/doc/lttng-ust12-2.12.10/examples/cmake-multiple-shared-libraries/tester-lib.cpp
* /usr/share/doc/lttng-ust12-2.12.10/examples/cmake-multiple-shared-libraries/tester-lib.h
* /usr/share/doc/lttng-ust12-2.12.10/examples/cmake-multiple-shared-libraries/tester.cpp
* /usr/share/doc/lttng-ust12-2.12.10/examples/cmake-multiple-shared-libraries/trace.sh
* /usr/share/doc/lttng-ust12-2.12.10/examples/cmake-multiple-shared-libraries/tracepoint-provider.cpp
* /usr/share/doc/lttng-ust12-2.12.10/examples/cmake-multiple-shared-libraries/tracepoint-provider.h
* /usr/share/doc/lttng-ust12-2.12.10/examples/demo-tracef/demo-tracef.c
* /usr/share/doc/lttng-ust12-2.12.10/examples/demo-tracef/Makefile
* /usr/share/doc/lttng-ust12-2.12.10/examples/demo-tracef/README
* /usr/share/doc/lttng-ust12-2.12.10/examples/demo-tracelog/demo-tracelog.c
* /usr/share/doc/lttng-ust12-2.12.10/examples/demo-tracelog/Makefile
* /usr/share/doc/lttng-ust12-2.12.10/examples/demo-tracelog/README
* /usr/share/doc/lttng-ust12-2.12.10/examples/demo/demo-trace
* /usr/share/doc/lttng-ust12-2.12.10/examples/demo/demo.c
* /usr/share/doc/lttng-ust12-2.12.10/examples/demo/Makefile
* /usr/share/doc/lttng-ust12-2.12.10/examples/demo/README
* /usr/share/doc/lttng-ust12-2.12.10/examples/demo/tp.c
* /usr/share/doc/lttng-ust12-2.12.10/examples/demo/tp2.c
* /usr/share/doc/lttng-ust12-2.12.10/examples/demo/tp3.c
* /usr/share/doc/lttng-ust12-2.12.10/examples/demo/ust_tests_demo.h
* /usr/share/doc/lttng-ust12-2.12.10/examples/demo/ust_tests_demo2.h
* /usr/share/doc/lttng-ust12-2.12.10/examples/demo/ust_tests_demo3.h
* /usr/share/doc/lttng-ust12-2.12.10/examples/easy-ust/Makefile
* /usr/share/doc/lttng-ust12-2.12.10/examples/easy-ust/sample.c
* /usr/share/doc/lttng-ust12-2.12.10/examples/easy-ust/sample_component_provider.h
* /usr/share/doc/lttng-ust12-2.12.10/examples/easy-ust/tp.c
* /usr/share/doc/lttng-ust12-2.12.10/examples/gen-tp/Makefile
* /usr/share/doc/lttng-ust12-2.12.10/examples/gen-tp/sample.c
* /usr/share/doc/lttng-ust12-2.12.10/examples/gen-tp/sample_tracepoint.tp
* /usr/share/doc/lttng-ust12-2.12.10/examples/getcpu-override/lttng-ust-getcpu-override-example.c
* /usr/share/doc/lttng-ust12-2.12.10/examples/getcpu-override/Makefile
* /usr/share/doc/lttng-ust12-2.12.10/examples/getcpu-override/README
* /usr/share/doc/lttng-ust12-2.12.10/examples/getcpu-override/run-getcpu-override
* /usr/share/doc/lttng-ust12-2.12.10/examples/hello-static-lib/hello.c
* /usr/share/doc/lttng-ust12-2.12.10/examples/hello-static-lib/Makefile
* /usr/share/doc/lttng-ust12-2.12.10/examples/hello-static-lib/README
* /usr/share/doc/lttng-ust12-2.12.10/examples/hello-static-lib/tp.c
* /usr/share/doc/lttng-ust12-2.12.10/examples/hello-static-lib/ust_tests_hello.h
* /usr/share/doc/lttng-ust12-2.12.10/examples/README
* /usr/share/doc/lttng-ust12-2.12.10/java-agent.txt
* /usr/share/doc/lttng-ust12-2.12.10/LICENSE
* /usr/share/doc/lttng-ust12-2.12.10/README.md
* /usr/share/man/man1/lttng-gen-tp.1.gz
* /usr/share/man/man3/do_tracepoint.3.gz
* /usr/share/man/man3/lttng-ust-cyg-profile.3.gz
* /usr/share/man/man3/lttng-ust-dl.3.gz
* /usr/share/man/man3/lttng-ust.3.gz
* /usr/share/man/man3/tracef.3.gz
* /usr/share/man/man3/tracelog.3.gz
* /usr/share/man/man3/tracepoint.3.gz
* /usr/share/man/man3/tracepoint_enabled.3.gz
