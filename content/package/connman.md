+++
draft = false
title = "connman 1.44-1"
version = "1.44-1"
description = "open source connection manager"
date = "2025-04-01T14:24:23"
aliases = "/packages/74582"
categories = ['network-extra']
upstreamurl = "http://connman.net/"
arch = "x86_64"
size = "561632"
usize = "1782121"
sha1sum = "39ce334b066e5e430a211f7a7ef0d3a5e1443b88"
depends = "['dhclient>=4.3.3', 'gnutls>=3.4.2', 'iptables>=1.6.1', 'libsystemd>=229', 'openvpn>=2.3.10', 'polkit', 'ppp>=2.4.7-2', 'readline>=8.0', 'wireless_tools', 'wpa_supplicant']"
reverse_depends = "['econnman']"
+++
### Description: 
open source connection manager

### Files: 
* /usr/bin/connman-vpnd
* /usr/bin/connmanctl
* /usr/bin/connmand
* /usr/bin/connmand-wait-online
* /usr/include/connman/acd.h
* /usr/include/connman/agent.h
* /usr/include/connman/device.h
* /usr/include/connman/inet.h
* /usr/include/connman/inotify.h
* /usr/include/connman/ipaddress.h
* /usr/include/connman/ipconfig.h
* /usr/include/connman/log.h
* /usr/include/connman/machine.h
* /usr/include/connman/network.h
* /usr/include/connman/notifier.h
* /usr/include/connman/peer.h
* /usr/include/connman/plugin.h
* /usr/include/connman/provision.h
* /usr/include/connman/resolver.h
* /usr/include/connman/service.h
* /usr/include/connman/session.h
* /usr/include/connman/storage.h
* /usr/include/connman/tethering.h
* /usr/include/connman/version.h
* /usr/lib/connman/plugins-vpn/l2tp.so
* /usr/lib/connman/plugins-vpn/openvpn.so
* /usr/lib/connman/plugins-vpn/pptp.so
* /usr/lib/connman/plugins-vpn/wireguard.so
* /usr/lib/connman/plugins/hh2serial-gps.so
* /usr/lib/connman/plugins/iospm.so
* /usr/lib/connman/plugins/session_policy_local.so
* /usr/lib/connman/plugins/tist.so
* /usr/lib/connman/scripts/libppp-plugin.so
* /usr/lib/connman/scripts/openvpn-script
* /usr/lib/pkgconfig/connman.pc
* /usr/lib/systemd/system/connman-vpn.service
* /usr/lib/systemd/system/connman-wait-online.service
* /usr/lib/systemd/system/connman.service
* /usr/lib/tmpfiles.d/connman_resolvconf.conf
* /usr/share/dbus-1/system-services/net.connman.vpn.service
* /usr/share/dbus-1/system.d/connman-nmcompat.conf
* /usr/share/dbus-1/system.d/connman-vpn-dbus.conf
* /usr/share/dbus-1/system.d/connman.conf
* /usr/share/doc/connman-1.44/AUTHORS
* /usr/share/doc/connman-1.44/ChangeLog
* /usr/share/doc/connman-1.44/COPYING
* /usr/share/doc/connman-1.44/INSTALL
* /usr/share/doc/connman-1.44/README
* /usr/share/doc/connman-1.44/TODO
* /usr/share/man/man1/connmanctl.1.gz
* /usr/share/man/man5/connman-service.config.5.gz
* /usr/share/man/man5/connman-vpn-provider.config.5.gz
* /usr/share/man/man5/connman-vpn.conf.5.gz
* /usr/share/man/man5/connman.conf.5.gz
* /usr/share/man/man8/connman-vpn.8.gz
* /usr/share/man/man8/connman.8.gz
* /usr/share/polkit-1/actions/net.connman.policy
* /usr/share/polkit-1/actions/net.connman.vpn.policy
