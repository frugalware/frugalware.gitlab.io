+++
draft = false
title = "criu 3.19-3"
version = "3.19-3"
description = "Checkpoint/Restore in Userspace tool"
date = "2024-01-09T12:51:03"
aliases = "/packages/200132"
categories = ['apps-extra']
upstreamurl = "http://criu.org"
arch = "x86_64"
size = "642452"
usize = "2194982"
sha1sum = "3fedd80b0938f6db5dd4307dd7ed3cc9798c9435"
depends = "['libbsd', 'libdrm', 'libnet', 'libnl', 'libpthread-stubs', 'nftables', 'protobuf-c', 'python3>=3.11']"
license = "GPL2"
+++
Checkpoint/Restore in Userspace tool

{{< files text="show files" >}}* /usr/bin/compel
* /usr/bin/crit
* /usr/bin/criu
* /usr/bin/criu-ns
* /usr/include/compel/asm/breakpoints.h
* /usr/include/compel/asm/cpu.h
* /usr/include/compel/asm/fpu.h
* /usr/include/compel/asm/infect-types.h
* /usr/include/compel/asm/processor-flags.h
* /usr/include/compel/asm/sigframe.h
* /usr/include/compel/common/compiler.h
* /usr/include/compel/cpu.h
* /usr/include/compel/handle-elf.h
* /usr/include/compel/infect-rpc.h
* /usr/include/compel/infect-util.h
* /usr/include/compel/infect.h
* /usr/include/compel/ksigset.h
* /usr/include/compel/log.h
* /usr/include/compel/loglevels.h
* /usr/include/compel/plugins.h
* /usr/include/compel/plugins/plugin-fds.h
* /usr/include/compel/plugins/shmem.h
* /usr/include/compel/plugins/std.h
* /usr/include/compel/plugins/std/asm/syscall-types.h
* /usr/include/compel/plugins/std/fds.h
* /usr/include/compel/plugins/std/infect.h
* /usr/include/compel/plugins/std/log.h
* /usr/include/compel/plugins/std/string.h
* /usr/include/compel/plugins/std/syscall-64.h
* /usr/include/compel/plugins/std/syscall-codes-64.h
* /usr/include/compel/plugins/std/syscall-codes.h
* /usr/include/compel/plugins/std/syscall-types.h
* /usr/include/compel/plugins/std/syscall.h
* /usr/include/compel/ptrace.h
* /usr/include/compel/sigframe-common.h
* /usr/include/compel/task-state.h
* /usr/include/criu/criu-log.h
* /usr/include/criu/criu-plugin.h
* /usr/include/criu/criu.h
* /usr/include/criu/rpc.pb-c.h
* /usr/include/criu/rpc.proto
* /usr/include/criu/version.h
* /usr/lib/criu/amdgpu_plugin.so
* /usr/lib/criu/compel/scripts/compel-pack.lds.S
* /usr/lib/criu/criu/scripts/systemd-autofs-restart.sh
* /usr/lib/libcompel.so
* /usr/lib/libcompel.so.1
* /usr/lib/libcompel.so.1.0
* /usr/lib/libcriu.so
* /usr/lib/libcriu.so.2
* /usr/lib/libcriu.so.2.0
* /usr/lib/pkgconfig/criu.pc
* /usr/lib/python3.12/site-packages/crit-3.19.dist-info/entry_points.txt
* /usr/lib/python3.12/site-packages/crit-3.19.dist-info/METADATA
* /usr/lib/python3.12/site-packages/crit-3.19.dist-info/RECORD
* /usr/lib/python3.12/site-packages/crit-3.19.dist-info/top_level.txt
* /usr/lib/python3.12/site-packages/crit-3.19.dist-info/WHEEL
* /usr/lib/python3.12/site-packages/crit/version.py
* /usr/lib/python3.12/site-packages/crit/__init__.py
* /usr/lib/python3.12/site-packages/crit/__main__.py
* /usr/lib/python3.12/site-packages/crit/__pycache__/version.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/crit/__pycache__/version.cpython-312.pyc
* /usr/lib/python3.12/site-packages/crit/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/crit/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/crit/__pycache__/__main__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/crit/__pycache__/__main__.cpython-312.pyc
* /usr/share/doc/criu-3.19/COPYING
* /usr/share/doc/criu-3.19/CREDITS
* /usr/share/doc/criu-3.19/INSTALL.md
* /usr/share/doc/criu-3.19/README.md
* /usr/share/man/man1/compel.1.gz
* /usr/share/man/man1/crit.1.gz
* /usr/share/man/man1/criu-amdgpu-plugin.1.gz
* /usr/share/man/man1/criu-ns.1.gz
* /usr/share/man/man8/criu.8.gz
{{< /files >}}