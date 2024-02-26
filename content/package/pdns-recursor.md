+++
draft = false
title = "pdns-recursor 4.9.2-2"
version = "4.9.2-2"
description = "Power DNS recursor"
date = "2024-01-09T10:52:29"
aliases = "/packages/9792"
categories = ['network-extra']
upstreamurl = "http://www.powerdns.com/"
arch = "x86_64"
size = "1743612"
usize = "6293886"
sha1sum = "ae1d122f18d53f93869c40c821a96542cbaacfa2"
depends = "['curl', 'libboost>=1.83.0', 'libsodium>=1.0.19', 'libstdc++>=12.2', 'libsystemd', 'lua', 'luajit2', 'openssl>=3.1.0', 'protobuf>=3.16.0']"
+++
Power DNS recursor{{< spoiler text="show files" >}}* /etc/powerdns/recursor.conf
* /etc/powerdns/recursor.conf-dist
* /usr/bin/pdns_recursor
* /usr/bin/rec_control
* /usr/lib/systemd/system/pdns-recursor.service
* /usr/lib/systemd/system/pdns-recursor@.service
* /usr/share/doc/pdns-recursor-4.9.2/COPYING
* /usr/share/doc/pdns-recursor-4.9.2/README
* /usr/share/man/man1/pdns_recursor.1.gz
* /usr/share/man/man1/rec_control.1.gz
{{< /spoiler >}}