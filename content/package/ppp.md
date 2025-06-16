+++
draft = false
title = "ppp 2.5.2-1"
version = "2.5.2-1"
description = "The PPP (Point-to-Point Protocol) daemon"
date = "2024-12-31T15:26:09"
aliases = "/packages/3298"
categories = ['base']
upstreamurl = "http://www.samba.org/ppp/"
arch = "x86_64"
size = "317896"
usize = "900408"
sha1sum = "bc237eefaef2657be2b6a8f12588988172d12504"
depends = "['glibc>=2.34', 'libpcap', 'libxcrypt', 'openssl>=3.1.0']"
reverse_depends = "['connman', 'modemmanager', 'networkmanager', 'pptp', 'pptpd', 'rp-pppoe']"
+++
### Description: 
The PPP (Point-to-Point Protocol) daemon

### Files: 
* /etc/ppp/chap-secrets.example
* /etc/ppp/eaptls-client.example
* /etc/ppp/eaptls-server.example
* /etc/ppp/ip-down
* /etc/ppp/ip-up
* /etc/ppp/openssl.cnf.example
* /etc/ppp/options.example
* /etc/ppp/pap-secrets.example
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
* /usr/lib/pppd/2.5.2/minconn.so
* /usr/lib/pppd/2.5.2/openl2tp.so
* /usr/lib/pppd/2.5.2/passwordfd.so
* /usr/lib/pppd/2.5.2/pppoatm.so
* /usr/lib/pppd/2.5.2/pppoe.so
* /usr/lib/pppd/2.5.2/pppol2tp.so
* /usr/lib/pppd/2.5.2/radattr.so
* /usr/lib/pppd/2.5.2/radius.so
* /usr/lib/pppd/2.5.2/radrealms.so
* /usr/lib/pppd/2.5.2/winbind.so
* /usr/share/doc/ppp-2.5.2/AUTHORS
* /usr/share/doc/ppp-2.5.2/ChangeLog
* /usr/share/doc/ppp-2.5.2/COPYING
* /usr/share/doc/ppp-2.5.2/FAQ
* /usr/share/doc/ppp-2.5.2/INSTALL
* /usr/share/doc/ppp-2.5.2/NEWS
* /usr/share/doc/ppp-2.5.2/README
* /usr/share/doc/ppp-2.5.2/README.cbcp
* /usr/share/doc/ppp-2.5.2/README.eap-srp
* /usr/share/doc/ppp-2.5.2/README.eap-tls
* /usr/share/doc/ppp-2.5.2/README.linux
* /usr/share/doc/ppp-2.5.2/README.MPPE
* /usr/share/doc/ppp-2.5.2/README.MSCHAP80
* /usr/share/doc/ppp-2.5.2/README.MSCHAP81
* /usr/share/doc/ppp-2.5.2/README.pppoe
* /usr/share/doc/ppp-2.5.2/README.pppol2tp
* /usr/share/doc/ppp-2.5.2/README.pwfd
* /usr/share/doc/ppp-2.5.2/README.sol2
* /usr/share/man/man1/pon.1.gz
* /usr/share/man/man8/chat.8.gz
* /usr/share/man/man8/pppd-radattr.8.gz
* /usr/share/man/man8/pppd-radius.8.gz
* /usr/share/man/man8/pppd.8.gz
* /usr/share/man/man8/pppdump.8.gz
* /usr/share/man/man8/pppoe-discovery.8.gz
* /usr/share/man/man8/pppstats.8.gz
