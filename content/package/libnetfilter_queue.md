+++
draft = false
title = "libnetfilter_queue 1.0.5-2"
version = "1.0.5-2"
description = "A userspace library that provides the programming interface to packets that have been queued by the kernel packet filter."
date = "2022-02-08T21:28:18"
aliases = "/packages/219296"
categories = ['lib-extra']
upstreamurl = "http://netfilter.org/projects/libnetfilter_queue/index.html"
arch = "x86_64"
size = "19704"
usize = "60604"
sha1sum = "46b869d5d78d454d8acbe207c3a50f9362cfa1f1"
depends = "['libmnl', 'libnfnetlink']"
reverse_depends = "['conntrack-tools']"
+++
A userspace library that provides the programming interface to packets that have been queued by the kernel packet filter.{{< files text="show files" >}}* /usr/include/libnetfilter_queue/libnetfilter_queue.h
* /usr/include/libnetfilter_queue/libnetfilter_queue_ipv4.h
* /usr/include/libnetfilter_queue/libnetfilter_queue_ipv6.h
* /usr/include/libnetfilter_queue/libnetfilter_queue_tcp.h
* /usr/include/libnetfilter_queue/libnetfilter_queue_udp.h
* /usr/include/libnetfilter_queue/linux_nfnetlink_queue.h
* /usr/include/libnetfilter_queue/pktbuff.h
* /usr/lib/libnetfilter_queue.so
* /usr/lib/libnetfilter_queue.so.1
* /usr/lib/libnetfilter_queue.so.1.5.0
* /usr/lib/pkgconfig/libnetfilter_queue.pc
* /usr/share/doc/libnetfilter_queue-1.0.5/COPYING
{{< /files >}}