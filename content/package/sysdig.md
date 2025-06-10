+++
draft = false
title = "sysdig 0.40.1-20"
version = "0.40.1-20"
description = "Open source system-level exploration and troubleshooting tool"
date = "2025-06-10T14:03:48"
aliases = "/packages/219877"
categories = ['apps-extra']
upstreamurl = "https://www.sysdig.com/"
arch = "x86_64"
size = "406144"
usize = "1367384"
sha1sum = "0bc9b68d8b4fcc27d76614b685aa3b081008bf50"
depends = "['falcosecurity-libs', 'luajit2', 'yaml-cpp']"
+++
### Description: 
Open source system-level exploration and troubleshooting tool

### Files: 
* /usr/bin/csysdig
* /usr/bin/scap-driver-loader
* /usr/bin/sysdig
* /usr/share/bash-completion/completions/sysdig
* /usr/share/doc/sysdig-0.40.1/COPYING
* /usr/share/doc/sysdig-0.40.1/README.md
* /usr/share/man/man8/csysdig.8.gz
* /usr/share/man/man8/sysdig.8.gz
* /usr/share/sysdig/chisels/ansiterminal.lua
* /usr/share/sysdig/chisels/around.lua
* /usr/share/sysdig/chisels/bottlenecks.lua
* /usr/share/sysdig/chisels/common.lua
* /usr/share/sysdig/chisels/COPYING
* /usr/share/sysdig/chisels/dkjson.lua
* /usr/share/sysdig/chisels/echo_fds.lua
* /usr/share/sysdig/chisels/fdbytes_by.lua
* /usr/share/sysdig/chisels/fdcount_by.lua
* /usr/share/sysdig/chisels/fdtime_by.lua
* /usr/share/sysdig/chisels/fileslower.lua
* /usr/share/sysdig/chisels/flame.lua
* /usr/share/sysdig/chisels/http.lua
* /usr/share/sysdig/chisels/httplog.lua
* /usr/share/sysdig/chisels/httptop.lua
* /usr/share/sysdig/chisels/iobytes.lua
* /usr/share/sysdig/chisels/iobytes_file.lua
* /usr/share/sysdig/chisels/iobytes_net.lua
* /usr/share/sysdig/chisels/list_login_shells.lua
* /usr/share/sysdig/chisels/lscontainers.lua
* /usr/share/sysdig/chisels/lsof.lua
* /usr/share/sysdig/chisels/memcachelog.lua
* /usr/share/sysdig/chisels/netlower.lua
* /usr/share/sysdig/chisels/netstat.lua
* /usr/share/sysdig/chisels/proc_exec_time.lua
* /usr/share/sysdig/chisels/ps.lua
* /usr/share/sysdig/chisels/scallslower.lua
* /usr/share/sysdig/chisels/shellshock_detect.lua
* /usr/share/sysdig/chisels/spectrogram.lua
* /usr/share/sysdig/chisels/spy_file.lua
* /usr/share/sysdig/chisels/spy_ip.lua
* /usr/share/sysdig/chisels/spy_logs.lua
* /usr/share/sysdig/chisels/spy_port.lua
* /usr/share/sysdig/chisels/spy_syslog.lua
* /usr/share/sysdig/chisels/spy_users.lua
* /usr/share/sysdig/chisels/statsd.lua
* /usr/share/sysdig/chisels/stderr.lua
* /usr/share/sysdig/chisels/stdin.lua
* /usr/share/sysdig/chisels/stdout.lua
* /usr/share/sysdig/chisels/subsecoffset.lua
* /usr/share/sysdig/chisels/table_generator.lua
* /usr/share/sysdig/chisels/topconns.lua
* /usr/share/sysdig/chisels/topcontainers_cpu.lua
* /usr/share/sysdig/chisels/topcontainers_error.lua
* /usr/share/sysdig/chisels/topcontainers_file.lua
* /usr/share/sysdig/chisels/topcontainers_net.lua
* /usr/share/sysdig/chisels/topfiles_bytes.lua
* /usr/share/sysdig/chisels/topfiles_errors.lua
* /usr/share/sysdig/chisels/topfiles_time.lua
* /usr/share/sysdig/chisels/topports_server.lua
* /usr/share/sysdig/chisels/topprocs_cpu.lua
* /usr/share/sysdig/chisels/topprocs_errors.lua
* /usr/share/sysdig/chisels/topprocs_file.lua
* /usr/share/sysdig/chisels/topprocs_net.lua
* /usr/share/sysdig/chisels/topscalls.lua
* /usr/share/sysdig/chisels/topscalls_time.lua
* /usr/share/sysdig/chisels/tracers_2_statsd.lua
* /usr/share/sysdig/chisels/udp_extract.lua
* /usr/share/sysdig/chisels/v_backlog.lua
* /usr/share/sysdig/chisels/v_connections.lua
* /usr/share/sysdig/chisels/v_containers.lua
* /usr/share/sysdig/chisels/v_containers_errors.lua
* /usr/share/sysdig/chisels/v_cpus.lua
* /usr/share/sysdig/chisels/v_directories.lua
* /usr/share/sysdig/chisels/v_docker_events.lua
* /usr/share/sysdig/chisels/v_errors.lua
* /usr/share/sysdig/chisels/v_files.lua
* /usr/share/sysdig/chisels/v_file_opens.lua
* /usr/share/sysdig/chisels/v_incoming_connections.lua
* /usr/share/sysdig/chisels/v_io_by_type.lua
* /usr/share/sysdig/chisels/v_kubernetes_controllers.lua
* /usr/share/sysdig/chisels/v_kubernetes_deployments.lua
* /usr/share/sysdig/chisels/v_kubernetes_namespaces.lua
* /usr/share/sysdig/chisels/v_kubernetes_pods.lua
* /usr/share/sysdig/chisels/v_kubernetes_replicasets.lua
* /usr/share/sysdig/chisels/v_kubernetes_services.lua
* /usr/share/sysdig/chisels/v_notifications.lua
* /usr/share/sysdig/chisels/v_page_faults.lua
* /usr/share/sysdig/chisels/v_port_bindings.lua
* /usr/share/sysdig/chisels/v_procs.lua
* /usr/share/sysdig/chisels/v_procs_cpu.lua
* /usr/share/sysdig/chisels/v_procs_errors.lua
* /usr/share/sysdig/chisels/v_procs_fd_usage.lua
* /usr/share/sysdig/chisels/v_slow_io.lua
* /usr/share/sysdig/chisels/v_spans_list.lua
* /usr/share/sysdig/chisels/v_spans_summary.lua
* /usr/share/sysdig/chisels/v_spectro_all.lua
* /usr/share/sysdig/chisels/v_spectro_file.lua
* /usr/share/sysdig/chisels/v_sports.lua
* /usr/share/sysdig/chisels/v_spy_syslog.lua
* /usr/share/sysdig/chisels/v_spy_users.lua
* /usr/share/sysdig/chisels/v_spy_users_wsysdig.lua
* /usr/share/sysdig/chisels/v_syscalls.lua
* /usr/share/sysdig/chisels/v_syscall_procs.lua
* /usr/share/sysdig/chisels/v_threads.lua
* /usr/share/sysdig/chisels/wsysdig_summary.lua
* /usr/share/zsh/site-functions/_sysdig
* /usr/share/zsh/vendor-completions/_sysdig
