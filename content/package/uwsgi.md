+++
draft = false
title = "uwsgi 2.0.23-1"
version = "2.0.23-1"
date = "2023-11-02T12:28:24"
categories = ['network-extra']
upstreamurl = "http://projects.unbit.it/"
arch = "x86_64"
size = "448808"
usize = "1854987"
sha1sum = "dd658b56ef7480214416b5846006e90127802eaa"
depends = "['zeromq', 'pcre', 'libcap', 'libuuid', 'jansson', 'openssl>=3.1.0', 'libxml2', 'mono']"
license = "GPL2"
files = "['etc/', 'etc/tmpfiles.d/', 'etc/tmpfiles.d/uwsgi.conf', 'lib/', 'lib/systemd/', 'lib/systemd/system/', 'lib/systemd/system/uwsgi@.service', 'lib/systemd/system/uwsgi@.socket', 'usr/', 'usr/bin/', 'usr/bin/uwsgi', 'usr/lib/', 'usr/lib/uwsgi/', 'usr/lib/uwsgi/cache_plugin.so', 'usr/lib/uwsgi/cgi_plugin.so', 'usr/lib/uwsgi/cheaper_backlog2_plugin.so', 'usr/lib/uwsgi/cheaper_busyness_plugin.so', 'usr/lib/uwsgi/clock_realtime_plugin.so', 'usr/lib/uwsgi/dumbloop_plugin.so', 'usr/lib/uwsgi/dummy_plugin.so', 'usr/lib/uwsgi/echo_plugin.so', 'usr/lib/uwsgi/emperor_amqp_plugin.so', 'usr/lib/uwsgi/emperor_zeromq_plugin.so', 'usr/lib/uwsgi/example_plugin.so', 'usr/lib/uwsgi/exception_log_plugin.so', 'usr/lib/uwsgi/fiber_plugin.so', 'usr/lib/uwsgi/greenlet_plugin.so', 'usr/lib/uwsgi/http_plugin.so', 'usr/lib/uwsgi/legion_cache_fetch_plugin.so', 'usr/lib/uwsgi/logcrypto_plugin.so', 'usr/lib/uwsgi/logfile_plugin.so', 'usr/lib/uwsgi/logpipe_plugin.so', 'usr/lib/uwsgi/logsocket_plugin.so', 'usr/lib/uwsgi/msgpack_plugin.so', 'usr/lib/uwsgi/notfound_plugin.so', 'usr/lib/uwsgi/ping_plugin.so', 'usr/lib/uwsgi/pty_plugin.so', 'usr/lib/uwsgi/pypy_plugin.so', 'usr/lib/uwsgi/rbthreads_plugin.so', 'usr/lib/uwsgi/redislog_plugin.so', 'usr/lib/uwsgi/rpc_plugin.so', 'usr/lib/uwsgi/rrdtool_plugin.so', 'usr/lib/uwsgi/rsyslog_plugin.so', 'usr/lib/uwsgi/signal_plugin.so', 'usr/lib/uwsgi/spooler_plugin.so', 'usr/lib/uwsgi/ssi_plugin.so', 'usr/lib/uwsgi/stats_pusher_file_plugin.so', 'usr/lib/uwsgi/stats_pusher_socket_plugin.so', 'usr/lib/uwsgi/stats_pusher_statsd_plugin.so', 'usr/lib/uwsgi/symcall_plugin.so', 'usr/lib/uwsgi/syslog_plugin.so', 'usr/lib/uwsgi/tornado_plugin.so', 'usr/lib/uwsgi/transformation_chunked_plugin.so', 'usr/lib/uwsgi/transformation_gzip_plugin.so', 'usr/lib/uwsgi/transformation_offload_plugin.so', 'usr/lib/uwsgi/transformation_template_plugin.so', 'usr/lib/uwsgi/transformation_tofile_plugin.so', 'usr/lib/uwsgi/transformation_toupper_plugin.so', 'usr/lib/uwsgi/tuntap_plugin.so', 'usr/lib/uwsgi/ugreen_plugin.so', 'usr/lib/uwsgi/xattr_plugin.so', 'usr/lib/uwsgi/zabbix_plugin.so', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/uwsgi-2.0.23/', 'usr/share/doc/uwsgi-2.0.23/CONTRIBUTORS', 'usr/share/doc/uwsgi-2.0.23/LICENSE', 'usr/share/doc/uwsgi-2.0.23/README']"
+++
A fast, self-healing and developer/sysadmin-friendly application container server coded in pure C