+++
draft = false
title = "libreswan 4.12-2"
version = "4.12-2"
date = "2024-01-09T15:22:12"
categories = ['network-extra']
upstreamurl = "http://libreswan.org/"
arch = "x86_64"
size = "1035140"
usize = "4099837"
sha1sum = "58e8dc68d3da000800e98d6f5385408e34fea044"
depends = "['nss', 'unbound>=1.18.0', 'libcap-ng', 'curl', 'ldns>=1.7.1', 'libsystemd', 'libevent>=2.1.11']"
files = "['etc/', 'etc/init.d/', 'etc/init.d/ipsec', 'etc/ipsec.conf', 'etc/ipsec.d/', 'etc/ipsec.d/policies/', 'etc/ipsec.d/policies/block', 'etc/ipsec.d/policies/clear', 'etc/ipsec.d/policies/clear-or-private', 'etc/ipsec.d/policies/portexcludes.conf', 'etc/ipsec.d/policies/private', 'etc/ipsec.d/policies/private-or-clear', 'etc/ipsec.secrets', 'etc/logrotate.d/', 'etc/logrotate.d/libreswan', 'etc/pam.d/', 'etc/pam.d/pluto', 'etc/sysconfig/', 'etc/sysconfig/pluto', 'usr/', 'usr/bin/', 'usr/bin/ipsec', 'usr/lib/', 'usr/lib/ipsec/', 'usr/lib/ipsec/_import_crl', 'usr/lib/ipsec/_plutorun', 'usr/lib/ipsec/_secretcensor', 'usr/lib/ipsec/_stackmanager', 'usr/lib/ipsec/_unbound-hook', 'usr/lib/ipsec/_updown', 'usr/lib/ipsec/_updown.xfrm', 'usr/lib/ipsec/addconn', 'usr/lib/ipsec/algparse', 'usr/lib/ipsec/asn1check', 'usr/lib/ipsec/auto', 'usr/lib/ipsec/barf', 'usr/lib/ipsec/cavp', 'usr/lib/ipsec/dncheck', 'usr/lib/ipsec/ecdsasigkey', 'usr/lib/ipsec/enumcheck', 'usr/lib/ipsec/hunkcheck', 'usr/lib/ipsec/ipcheck', 'usr/lib/ipsec/jambufcheck', 'usr/lib/ipsec/keyidcheck', 'usr/lib/ipsec/letsencrypt', 'usr/lib/ipsec/look', 'usr/lib/ipsec/newhostkey', 'usr/lib/ipsec/pluto', 'usr/lib/ipsec/readwriteconf', 'usr/lib/ipsec/rsasigkey', 'usr/lib/ipsec/setup', 'usr/lib/ipsec/show', 'usr/lib/ipsec/showhostkey', 'usr/lib/ipsec/showroute', 'usr/lib/ipsec/timecheck', 'usr/lib/ipsec/vendoridcheck', 'usr/lib/ipsec/verify', 'usr/lib/ipsec/whack', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/libreswan-4.12/', 'usr/share/doc/libreswan-4.12/CHANGES', 'usr/share/doc/libreswan-4.12/COPYING', 'usr/share/doc/libreswan-4.12/CREDITS', 'usr/share/doc/libreswan-4.12/INSTALL', 'usr/share/doc/libreswan-4.12/LICENSE', 'usr/share/doc/libreswan-4.12/README.md', 'usr/share/doc/libreswan-4.12/README.nss', 'usr/share/doc/libreswan-4.12/README.x509', 'usr/share/doc/libreswan/', 'usr/share/doc/libreswan/ipsec.conf-sample', 'usr/share/doc/libreswan/ipsec.secrets-sample', 'var/', 'var/lib/', 'var/lib/ipsec/', 'var/lib/ipsec/nss/']"
+++
IPsec implementation with IKEv1 and IKEv2 keying protocols