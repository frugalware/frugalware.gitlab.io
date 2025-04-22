+++
draft = false
title = "nftables 1.1.3-1"
version = "1.1.3-1"
description = "Replacement for the popular {ip,ip6,arp,eb} tables."
date = "2025-04-22T20:57:12"
aliases = "/packages/219298"
categories = ['network-extra']
upstreamurl = "http://netfilter.org/projects/nftables/index.html"
arch = "x86_64"
size = "360192"
usize = "1031430"
sha1sum = "1d7693e080ef0af17b57302826e43670b742e75c"
depends = "['glibc>=2.34', 'gmp', 'libedit', 'libmnl', 'libnftnl>=1.2.1', 'ncurses', 'python3', 'readline>=8.0']"
reverse_depends = "['criu']"
+++
### Description: 
Replacement for the popular {ip,ip6,arp,eb} tables.

### Files: 
* /etc/nftables.conf
* /usr/bin/nft
* /usr/include/nftables/libnftables.h
* /usr/lib/libnftables.so
* /usr/lib/libnftables.so.1
* /usr/lib/libnftables.so.1.1.0
* /usr/lib/pkgconfig/libnftables.pc
* /usr/lib/systemd/system/nftables.service
* /usr/share/doc/nftables-1.1.3/COPYING
* /usr/share/doc/nftables-1.1.3/examples/ct_helpers.nft
* /usr/share/doc/nftables-1.1.3/examples/load_balancing.nft
* /usr/share/doc/nftables-1.1.3/examples/secmark.nft
* /usr/share/doc/nftables-1.1.3/examples/sets_and_maps.nft
* /usr/share/doc/nftables-1.1.3/INSTALL
* /usr/share/man/man3/libnftables.3.gz
* /usr/share/man/man5/libnftables-json.5.gz
* /usr/share/man/man8/nft.8.gz
* /usr/share/nftables/all-in-one.nft
* /usr/share/nftables/arp-filter.nft
* /usr/share/nftables/bridge-filter.nft
* /usr/share/nftables/inet-filter.nft
* /usr/share/nftables/inet-nat.nft
* /usr/share/nftables/ipv4-filter.nft
* /usr/share/nftables/ipv4-mangle.nft
* /usr/share/nftables/ipv4-nat.nft
* /usr/share/nftables/ipv4-raw.nft
* /usr/share/nftables/ipv6-filter.nft
* /usr/share/nftables/ipv6-mangle.nft
* /usr/share/nftables/ipv6-nat.nft
* /usr/share/nftables/ipv6-raw.nft
* /usr/share/nftables/netdev-ingress.nft
* /usr/share/nftables/osf/pf.os
