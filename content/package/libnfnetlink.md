+++
draft = false
title = "libnfnetlink 1.0.2-1"
version = "1.0.2-1"
date = "2023-02-24T19:31:56"
aliases = "/packages/219292"
categories = ['lib-extra']
upstreamurl = "http://netfilter.org/projects/libnfnetlink/index.html"
arch = "x86_64"
size = "21628"
usize = "62947"
sha1sum = "eb30c1d515ae4791a362d2e9b5fa326d38e33680"
depends = "['glibc>=2.29-6']"
reverse depends = "['libnetfilter_conntrack', 'libnetfilter_cthelper', 'libnetfilter_cttimeout', 'libnetfilter_log', 'libnetfilter_queue']"
files = "['/usr/include/libnfnetlink/libnfnetlink.h', '/usr/include/libnfnetlink/linux_nfnetlink.h', '/usr/include/libnfnetlink/linux_nfnetlink_compat.h', '/usr/lib/libnfnetlink.so', '/usr/lib/libnfnetlink.so.0', '/usr/lib/libnfnetlink.so.0.2.0', '/usr/lib/pkgconfig/libnfnetlink.pc', '/usr/share/doc/libnfnetlink-1.0.2/COPYING', '/usr/share/doc/libnfnetlink-1.0.2/README']"
+++
A low-level library for netfilter related kernel/userspace communication