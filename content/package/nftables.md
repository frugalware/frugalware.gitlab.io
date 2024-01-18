+++
draft = false
title = "nftables 1.0.9-1"
version = "1.0.9-1"
date = "2024-01-09T12:20:53"
categories = ['network-extra']
upstreamurl = "http://netfilter.org/projects/nftables/index.html"
arch = "x86_64"
size = "340272"
usize = "990218"
sha1sum = "267a8cfab08e66203654fb4766f74867f6c5095a"
depends = "['libmnl', 'libnftnl>=1.2.1', 'readline>=8.0', 'gmp', 'glibc>=2.34', 'ncurses', 'libedit', 'python3']"
files = "['etc/', 'etc/nftables.conf', 'usr/', 'usr/bin/', 'usr/bin/nft', 'usr/include/', 'usr/include/nftables/', 'usr/include/nftables/libnftables.h', 'usr/lib/', 'usr/lib/libnftables.so', 'usr/lib/libnftables.so.1', 'usr/lib/libnftables.so.1.1.0', 'usr/lib/pkgconfig/', 'usr/lib/pkgconfig/libnftables.pc', 'usr/lib/systemd/', 'usr/lib/systemd/system/', 'usr/lib/systemd/system/nftables.service', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/nftables-1.0.9/', 'usr/share/doc/nftables-1.0.9/COPYING', 'usr/share/doc/nftables-1.0.9/INSTALL', 'usr/share/doc/nftables-1.0.9/examples/', 'usr/share/doc/nftables-1.0.9/examples/ct_helpers.nft', 'usr/share/doc/nftables-1.0.9/examples/load_balancing.nft', 'usr/share/doc/nftables-1.0.9/examples/secmark.nft', 'usr/share/doc/nftables-1.0.9/examples/sets_and_maps.nft', 'usr/share/man/', 'usr/share/man/man3/', 'usr/share/man/man3/libnftables.3.gz', 'usr/share/man/man5/', 'usr/share/man/man5/libnftables-json.5.gz', 'usr/share/man/man8/', 'usr/share/man/man8/nft.8.gz', 'usr/share/nftables/', 'usr/share/nftables/all-in-one.nft', 'usr/share/nftables/arp-filter.nft', 'usr/share/nftables/bridge-filter.nft', 'usr/share/nftables/inet-filter.nft', 'usr/share/nftables/inet-nat.nft', 'usr/share/nftables/ipv4-filter.nft', 'usr/share/nftables/ipv4-mangle.nft', 'usr/share/nftables/ipv4-nat.nft', 'usr/share/nftables/ipv4-raw.nft', 'usr/share/nftables/ipv6-filter.nft', 'usr/share/nftables/ipv6-mangle.nft', 'usr/share/nftables/ipv6-nat.nft', 'usr/share/nftables/ipv6-raw.nft', 'usr/share/nftables/netdev-ingress.nft', 'usr/share/nftables/osf/', 'usr/share/nftables/osf/pf.os']"
+++
Replacement for the popular {ip,ip6,arp,eb} tables.