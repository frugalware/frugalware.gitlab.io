+++
draft = false
title = "openucx 1.18.0-2"
version = "1.18.0-2"
description = "Unified Communication X"
date = "2025-02-05T14:48:27"
aliases = "/packages/220865"
categories = ['network-extra']
upstreamurl = "http://www.openucx.org"
arch = "x86_64"
size = "1461824"
usize = "5055840"
sha1sum = "b91b6b8177768358f44302f2e47a0c2f70a7b04d"
depends = "['binutils>=2.44', 'libgomp', 'numactl', 'rdma-core']"
reverse_depends = "['cuda-tools']"
+++
### Description: 
Unified Communication X

### Files: 
* /etc/ucx/ucx.conf
* /usr/bin/io_demo
* /usr/bin/ucx_info
* /usr/bin/ucx_perftest
* /usr/bin/ucx_perftest_daemon
* /usr/bin/ucx_read_profile
* /usr/include/ucm/api/ucm.h
* /usr/include/ucp/api/ucp.h
* /usr/include/ucp/api/ucp_compat.h
* /usr/include/ucp/api/ucp_def.h
* /usr/include/ucp/api/ucp_version.h
* /usr/include/ucs/algorithm/crc.h
* /usr/include/ucs/algorithm/qsort_r.h
* /usr/include/ucs/algorithm/string_distance.h
* /usr/include/ucs/arch/aarch64/bitops.h
* /usr/include/ucs/arch/aarch64/global_opts.h
* /usr/include/ucs/arch/atomic.h
* /usr/include/ucs/arch/bitops.h
* /usr/include/ucs/arch/generic/atomic.h
* /usr/include/ucs/arch/global_opts.h
* /usr/include/ucs/arch/ppc64/bitops.h
* /usr/include/ucs/arch/ppc64/global_opts.h
* /usr/include/ucs/arch/rv64/bitops.h
* /usr/include/ucs/arch/rv64/global_opts.h
* /usr/include/ucs/arch/x86_64/atomic.h
* /usr/include/ucs/arch/x86_64/bitops.h
* /usr/include/ucs/arch/x86_64/global_opts.h
* /usr/include/ucs/async/async_fwd.h
* /usr/include/ucs/config/global_opts.h
* /usr/include/ucs/config/ini.h
* /usr/include/ucs/config/parser.h
* /usr/include/ucs/config/types.h
* /usr/include/ucs/datastruct/array.h
* /usr/include/ucs/datastruct/callbackq.h
* /usr/include/ucs/datastruct/callbackq_compat.h
* /usr/include/ucs/datastruct/hlist.h
* /usr/include/ucs/datastruct/khash.h
* /usr/include/ucs/datastruct/linear_func.h
* /usr/include/ucs/datastruct/list.h
* /usr/include/ucs/datastruct/mpool.h
* /usr/include/ucs/datastruct/mpool_set.h
* /usr/include/ucs/datastruct/pgtable.h
* /usr/include/ucs/datastruct/piecewise_func.h
* /usr/include/ucs/datastruct/queue_types.h
* /usr/include/ucs/datastruct/strided_alloc.h
* /usr/include/ucs/datastruct/string_buffer.h
* /usr/include/ucs/datastruct/string_set.h
* /usr/include/ucs/debug/debug.h
* /usr/include/ucs/debug/log_def.h
* /usr/include/ucs/debug/memtrack.h
* /usr/include/ucs/memory/memory_type.h
* /usr/include/ucs/memory/memtype_cache.h
* /usr/include/ucs/memory/numa.h
* /usr/include/ucs/memory/rcache.h
* /usr/include/ucs/profile/profile_defs.h
* /usr/include/ucs/profile/profile_off.h
* /usr/include/ucs/profile/profile_on.h
* /usr/include/ucs/stats/libstats.h
* /usr/include/ucs/stats/stats_fwd.h
* /usr/include/ucs/sys/compiler_def.h
* /usr/include/ucs/sys/event_set.h
* /usr/include/ucs/sys/math.h
* /usr/include/ucs/sys/preprocessor.h
* /usr/include/ucs/sys/sock.h
* /usr/include/ucs/sys/string.h
* /usr/include/ucs/sys/stubs.h
* /usr/include/ucs/sys/topo/base/topo.h
* /usr/include/ucs/sys/uid.h
* /usr/include/ucs/time/time_def.h
* /usr/include/ucs/type/class.h
* /usr/include/ucs/type/cpu_set.h
* /usr/include/ucs/type/init_once.h
* /usr/include/ucs/type/param.h
* /usr/include/ucs/type/spinlock.h
* /usr/include/ucs/type/status.h
* /usr/include/ucs/type/thread_mode.h
* /usr/include/ucs/vfs/base/vfs_cb.h
* /usr/include/ucs/vfs/base/vfs_obj.h
* /usr/include/uct/api/tl.h
* /usr/include/uct/api/uct.h
* /usr/include/uct/api/uct_def.h
* /usr/include/uct/api/version.h
* /usr/lib/cmake/ucx/ucx-config-version.cmake
* /usr/lib/cmake/ucx/ucx-config.cmake
* /usr/lib/cmake/ucx/ucx-targets.cmake
* /usr/lib/libucm.so
* /usr/lib/libucm.so.0
* /usr/lib/libucm.so.0.0.0
* /usr/lib/libucp.so
* /usr/lib/libucp.so.0
* /usr/lib/libucp.so.0.0.0
* /usr/lib/libucs.so
* /usr/lib/libucs.so.0
* /usr/lib/libucs.so.0.0.0
* /usr/lib/libucs_signal.so
* /usr/lib/libucs_signal.so.0
* /usr/lib/libucs_signal.so.0.0.0
* /usr/lib/libuct.so
* /usr/lib/libuct.so.0
* /usr/lib/libuct.so.0.0.0
* /usr/lib/pkgconfig/ucx-cma.pc
* /usr/lib/pkgconfig/ucx-ib-mlx5.pc
* /usr/lib/pkgconfig/ucx-ib.pc
* /usr/lib/pkgconfig/ucx-rdmacm.pc
* /usr/lib/pkgconfig/ucx-ucs.pc
* /usr/lib/pkgconfig/ucx-uct.pc
* /usr/lib/pkgconfig/ucx.pc
* /usr/lib/ucx/libuct_cma.so
* /usr/lib/ucx/libuct_cma.so.0
* /usr/lib/ucx/libuct_cma.so.0.0.0
* /usr/lib/ucx/libuct_ib.so
* /usr/lib/ucx/libuct_ib.so.0
* /usr/lib/ucx/libuct_ib.so.0.0.0
* /usr/lib/ucx/libuct_ib_mlx5.so
* /usr/lib/ucx/libuct_ib_mlx5.so.0
* /usr/lib/ucx/libuct_ib_mlx5.so.0.0.0
* /usr/lib/ucx/libuct_rdmacm.so
* /usr/lib/ucx/libuct_rdmacm.so.0
* /usr/lib/ucx/libuct_rdmacm.so.0.0.0
* /usr/lib/ucx/libucx_perftest_mad.so
* /usr/lib/ucx/libucx_perftest_mad.so.0
* /usr/lib/ucx/libucx_perftest_mad.so.0.0.0
* /usr/share/doc/openucx-1.18.0/AUTHORS
* /usr/share/doc/openucx-1.18.0/LICENSE
* /usr/share/doc/openucx-1.18.0/NEWS
* /usr/share/doc/openucx-1.18.0/README
* /usr/share/doc/openucx-1.18.0/README.md
* /usr/share/ucx/examples/hello_world_util.h
* /usr/share/ucx/examples/ucp_client_server.c
* /usr/share/ucx/examples/ucp_hello_world.c
* /usr/share/ucx/examples/ucp_util.h
* /usr/share/ucx/examples/uct_hello_world.c
* /usr/share/ucx/perftest/msg_pow2
* /usr/share/ucx/perftest/msg_pow2_large
* /usr/share/ucx/perftest/README
* /usr/share/ucx/perftest/test_types_ucp
* /usr/share/ucx/perftest/test_types_ucp_amo
* /usr/share/ucx/perftest/test_types_ucp_rma
* /usr/share/ucx/perftest/test_types_uct
* /usr/share/ucx/perftest/transports
