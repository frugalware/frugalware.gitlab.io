+++
draft = false
title = "ppp 2.5.0-4"
version = "2.5.0-4"
description = "The PPP (Point-to-Point Protocol) daemon"
date = "2024-02-01T14:03:32"
aliases = "/packages/3298"
categories = ['base']
upstreamurl = "http://www.samba.org/ppp/"
arch = "x86_64"
size = "322268"
usize = "1007103"
sha1sum = "793341a1a6f2c3dba652fe235cce0738170ba82f"
depends = "['glibc>=2.34', 'libpcap', 'libxcrypt', 'openssl>=3.1.0']"
reverse_depends = "['connman', 'modemmanager', 'networkmanager', 'pptp', 'pptpd', 'rp-pppoe']"
+++
The PPP (Point-to-Point Protocol) daemon{{< spoiler text="show files" >}}* /etc/ppp/chap-secrets
* /etc/ppp/eaptls-client
* /etc/ppp/eaptls-server
* /etc/ppp/ip-down
* /etc/ppp/ip-up
* /etc/ppp/openssl.cnf
* /etc/ppp/options
* /etc/ppp/pap-secrets
* /usr/bin/chat
* /usr/bin/poff
* /usr/bin/pon
* /usr/bin/pppd
* /usr/bin/pppdump
* /usr/bin/pppoe-discovery
* /usr/bin/pppstats
* /usr/include/pppd/cbcp.h
* /usr/include/pppd/ccp.h
* /usr/include/pppd/chap.h
* /usr/include/pppd/chap_ms.h
* /usr/include/pppd/crypto.h
* /usr/include/pppd/crypto_ms.h
* /usr/include/pppd/eap.h
* /usr/include/pppd/ecp.h
* /usr/include/pppd/eui64.h
* /usr/include/pppd/fsm.h
* /usr/include/pppd/ipcp.h
* /usr/include/pppd/ipv6cp.h
* /usr/include/pppd/lcp.h
* /usr/include/pppd/magic.h
* /usr/include/pppd/mppe.h
* /usr/include/pppd/multilink.h
* /usr/include/pppd/options.h
* /usr/include/pppd/pppd.h
* /usr/include/pppd/pppdconf.h
* /usr/include/pppd/session.h
* /usr/include/pppd/upap.h
* /usr/lib/pkgconfig/pppd.pc
* /usr/lib/pppd/2.5.0/minconn.so
* /usr/lib/pppd/2.5.0/openl2tp.so
* /usr/lib/pppd/2.5.0/passprompt.so
* /usr/lib/pppd/2.5.0/passwordfd.so
* /usr/lib/pppd/2.5.0/pppoatm.so
* /usr/lib/pppd/2.5.0/pppoe.so
* /usr/lib/pppd/2.5.0/pppol2tp.so
* /usr/lib/pppd/2.5.0/radattr.so
* /usr/lib/pppd/2.5.0/radius.so
* /usr/lib/pppd/2.5.0/radrealms.so
* /usr/lib/pppd/2.5.0/winbind.so
* /usr/share/doc/ppp-2.5.0/AUTHORS
* /usr/share/doc/ppp-2.5.0/ChangeLog
* /usr/share/doc/ppp-2.5.0/COPYING
* /usr/share/doc/ppp-2.5.0/FAQ
* /usr/share/doc/ppp-2.5.0/INSTALL
* /usr/share/doc/ppp-2.5.0/NEWS
* /usr/share/doc/ppp-2.5.0/README
* /usr/share/doc/ppp-2.5.0/README.cbcp
* /usr/share/doc/ppp-2.5.0/README.eap-srp
* /usr/share/doc/ppp-2.5.0/README.eap-tls
* /usr/share/doc/ppp-2.5.0/README.linux
* /usr/share/doc/ppp-2.5.0/README.MPPE
* /usr/share/doc/ppp-2.5.0/README.MSCHAP80
* /usr/share/doc/ppp-2.5.0/README.MSCHAP81
* /usr/share/doc/ppp-2.5.0/README.pppoe
* /usr/share/doc/ppp-2.5.0/README.pppol2tp
* /usr/share/doc/ppp-2.5.0/README.pwfd
* /usr/share/doc/ppp-2.5.0/README.sol2
* /usr/share/man/man1/pon.1.gz
* /usr/share/man/man8/chat.8.gz
* /usr/share/man/man8/pppd-radattr.8.gz
* /usr/share/man/man8/pppd-radius.8.gz
* /usr/share/man/man8/pppd.8.gz
* /usr/share/man/man8/pppdump.8.gz
* /usr/share/man/man8/pppoe-discovery.8.gz
* /usr/share/man/man8/pppstats.8.gz
{{< /spoiler >}}