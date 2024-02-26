+++
draft = false
title = "ipset 7.19-1"
version = "7.19-1"
description = "An administration tool for IP sets."
date = "2024-01-15T13:36:54"
aliases = "/packages/219291"
categories = ['network-extra']
upstreamurl = "http://ipset.netfilter.org/index.html"
arch = "x86_64"
size = "107404"
usize = "630708"
sha1sum = "05441097806e98d198480597f7d1aa674f26ec0d"
depends = "['iptables', 'libmnl']"
reverse_depends = "['fail2ban']"
+++
An administration tool for IP sets.{{< files text="show files" >}}* /etc/bash_completion.d/ipset
* /usr/bin/ipset
* /usr/bin/ipset-translate
* /usr/include/libipset/args.h
* /usr/include/libipset/data.h
* /usr/include/libipset/errcode.h
* /usr/include/libipset/ipset.h
* /usr/include/libipset/linux_ip_set.h
* /usr/include/libipset/linux_ip_set_bitmap.h
* /usr/include/libipset/linux_ip_set_hash.h
* /usr/include/libipset/linux_ip_set_list.h
* /usr/include/libipset/mnl.h
* /usr/include/libipset/nfproto.h
* /usr/include/libipset/nf_inet_addr.h
* /usr/include/libipset/parse.h
* /usr/include/libipset/pfxlen.h
* /usr/include/libipset/print.h
* /usr/include/libipset/session.h
* /usr/include/libipset/transport.h
* /usr/include/libipset/types.h
* /usr/include/libipset/utils.h
* /usr/include/libipset/xlate.h
* /usr/lib/ipset/ipset_bitmap_ip.so
* /usr/lib/ipset/ipset_bitmap_ipmac.so
* /usr/lib/ipset/ipset_bitmap_port.so
* /usr/lib/ipset/ipset_hash_ip.so
* /usr/lib/ipset/ipset_hash_ipmac.so
* /usr/lib/ipset/ipset_hash_ipmark.so
* /usr/lib/ipset/ipset_hash_ipport.so
* /usr/lib/ipset/ipset_hash_ipportip.so
* /usr/lib/ipset/ipset_hash_ipportnet.so
* /usr/lib/ipset/ipset_hash_mac.so
* /usr/lib/ipset/ipset_hash_net.so
* /usr/lib/ipset/ipset_hash_netiface.so
* /usr/lib/ipset/ipset_hash_netnet.so
* /usr/lib/ipset/ipset_hash_netport.so
* /usr/lib/ipset/ipset_hash_netportnet.so
* /usr/lib/ipset/ipset_list_set.so
* /usr/lib/libipset.so
* /usr/lib/libipset.so.13
* /usr/lib/libipset.so.13.4.0
* /usr/lib/pkgconfig/libipset.pc
* /usr/share/doc/ipset-7.19/ChangeLog
* /usr/share/doc/ipset-7.19/COPYING
* /usr/share/doc/ipset-7.19/INSTALL
* /usr/share/doc/ipset-7.19/README
* /usr/share/man/man3/libipset.3.gz
* /usr/share/man/man8/ipset-translate.8.gz
* /usr/share/man/man8/ipset.8.gz
{{< /files >}}