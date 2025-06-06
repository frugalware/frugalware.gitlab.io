+++
draft = false
title = "spdlog 1.15.3-1"
version = "1.15.3-1"
description = "Very fast, header-only/compiled, C++ logging library"
date = "2025-05-12T08:16:12"
aliases = "/packages/220551"
categories = ['lib']
upstreamurl = "https://github.com/gabime/spdlog"
arch = "x86_64"
size = "148676"
usize = "719932"
sha1sum = "f7089ea7ff5f131bdb5688e98c9c7a10ada53251"
depends = "['fmtlib>=11.1.1']"
reverse_depends = "['cryfs', 'level-zero']"
+++
### Description: 
Very fast, header-only/compiled, C++ logging library

### Files: 
* /usr/include/spdlog/async.h
* /usr/include/spdlog/async_logger-inl.h
* /usr/include/spdlog/async_logger.h
* /usr/include/spdlog/cfg/argv.h
* /usr/include/spdlog/cfg/env.h
* /usr/include/spdlog/cfg/helpers-inl.h
* /usr/include/spdlog/cfg/helpers.h
* /usr/include/spdlog/common-inl.h
* /usr/include/spdlog/common.h
* /usr/include/spdlog/details/backtracer-inl.h
* /usr/include/spdlog/details/backtracer.h
* /usr/include/spdlog/details/circular_q.h
* /usr/include/spdlog/details/console_globals.h
* /usr/include/spdlog/details/file_helper-inl.h
* /usr/include/spdlog/details/file_helper.h
* /usr/include/spdlog/details/fmt_helper.h
* /usr/include/spdlog/details/log_msg-inl.h
* /usr/include/spdlog/details/log_msg.h
* /usr/include/spdlog/details/log_msg_buffer-inl.h
* /usr/include/spdlog/details/log_msg_buffer.h
* /usr/include/spdlog/details/mpmc_blocking_q.h
* /usr/include/spdlog/details/null_mutex.h
* /usr/include/spdlog/details/os-inl.h
* /usr/include/spdlog/details/os.h
* /usr/include/spdlog/details/periodic_worker-inl.h
* /usr/include/spdlog/details/periodic_worker.h
* /usr/include/spdlog/details/registry-inl.h
* /usr/include/spdlog/details/registry.h
* /usr/include/spdlog/details/synchronous_factory.h
* /usr/include/spdlog/details/tcp_client-windows.h
* /usr/include/spdlog/details/tcp_client.h
* /usr/include/spdlog/details/thread_pool-inl.h
* /usr/include/spdlog/details/thread_pool.h
* /usr/include/spdlog/details/udp_client-windows.h
* /usr/include/spdlog/details/udp_client.h
* /usr/include/spdlog/details/windows_include.h
* /usr/include/spdlog/fmt/bin_to_hex.h
* /usr/include/spdlog/fmt/chrono.h
* /usr/include/spdlog/fmt/compile.h
* /usr/include/spdlog/fmt/fmt.h
* /usr/include/spdlog/fmt/ostr.h
* /usr/include/spdlog/fmt/ranges.h
* /usr/include/spdlog/fmt/std.h
* /usr/include/spdlog/fmt/xchar.h
* /usr/include/spdlog/formatter.h
* /usr/include/spdlog/fwd.h
* /usr/include/spdlog/logger-inl.h
* /usr/include/spdlog/logger.h
* /usr/include/spdlog/mdc.h
* /usr/include/spdlog/pattern_formatter-inl.h
* /usr/include/spdlog/pattern_formatter.h
* /usr/include/spdlog/sinks/android_sink.h
* /usr/include/spdlog/sinks/ansicolor_sink-inl.h
* /usr/include/spdlog/sinks/ansicolor_sink.h
* /usr/include/spdlog/sinks/base_sink-inl.h
* /usr/include/spdlog/sinks/base_sink.h
* /usr/include/spdlog/sinks/basic_file_sink-inl.h
* /usr/include/spdlog/sinks/basic_file_sink.h
* /usr/include/spdlog/sinks/callback_sink.h
* /usr/include/spdlog/sinks/daily_file_sink.h
* /usr/include/spdlog/sinks/dist_sink.h
* /usr/include/spdlog/sinks/dup_filter_sink.h
* /usr/include/spdlog/sinks/hourly_file_sink.h
* /usr/include/spdlog/sinks/kafka_sink.h
* /usr/include/spdlog/sinks/mongo_sink.h
* /usr/include/spdlog/sinks/msvc_sink.h
* /usr/include/spdlog/sinks/null_sink.h
* /usr/include/spdlog/sinks/ostream_sink.h
* /usr/include/spdlog/sinks/qt_sinks.h
* /usr/include/spdlog/sinks/ringbuffer_sink.h
* /usr/include/spdlog/sinks/rotating_file_sink-inl.h
* /usr/include/spdlog/sinks/rotating_file_sink.h
* /usr/include/spdlog/sinks/sink-inl.h
* /usr/include/spdlog/sinks/sink.h
* /usr/include/spdlog/sinks/stdout_color_sinks-inl.h
* /usr/include/spdlog/sinks/stdout_color_sinks.h
* /usr/include/spdlog/sinks/stdout_sinks-inl.h
* /usr/include/spdlog/sinks/stdout_sinks.h
* /usr/include/spdlog/sinks/syslog_sink.h
* /usr/include/spdlog/sinks/systemd_sink.h
* /usr/include/spdlog/sinks/tcp_sink.h
* /usr/include/spdlog/sinks/udp_sink.h
* /usr/include/spdlog/sinks/wincolor_sink-inl.h
* /usr/include/spdlog/sinks/wincolor_sink.h
* /usr/include/spdlog/sinks/win_eventlog_sink.h
* /usr/include/spdlog/spdlog-inl.h
* /usr/include/spdlog/spdlog.h
* /usr/include/spdlog/stopwatch.h
* /usr/include/spdlog/tweakme.h
* /usr/include/spdlog/version.h
* /usr/lib/cmake/spdlog/spdlogConfig.cmake
* /usr/lib/cmake/spdlog/spdlogConfigTargets-release.cmake
* /usr/lib/cmake/spdlog/spdlogConfigTargets.cmake
* /usr/lib/cmake/spdlog/spdlogConfigVersion.cmake
* /usr/lib/libspdlog.so
* /usr/lib/libspdlog.so.1.15
* /usr/lib/libspdlog.so.1.15.3
* /usr/lib/pkgconfig/spdlog.pc
* /usr/share/doc/spdlog-1.15.3/INSTALL
* /usr/share/doc/spdlog-1.15.3/LICENSE
* /usr/share/doc/spdlog-1.15.3/README.md
