+++
draft = false
title = "postgrey 1.37-5"
version = "1.37-5"
description = "a Postfix policy server implementing greylisting"
date = "2024-01-09T14:56:47"
aliases = "/packages/23447"
categories = ['network-extra']
upstreamurl = "http://postgrey.schweikert.ch/"
arch = "x86_64"
size = "34516"
usize = "107746"
sha1sum = "46bb9df09c3ebcd53e4cc6a5ffb73da35e472d46"
depends = "['db>=4.7.25', 'perl>=5.28.2', 'perl-berkeleydb', 'perl-io-multiplex', 'perl-net-server', 'postfix>=2.1']"
+++
a Postfix policy server implementing greylisting"

{{< files text="show files" >}}* /etc/postfix/postgrey_whitelist_clients
* /etc/postfix/postgrey_whitelist_recipients
* /etc/sysconfig/postgrey
* /usr/bin/postgrey
* /usr/bin/postgreyreport
* /usr/lib/systemd/system/postgrey.service
* /usr/share/doc/postgrey-1.37/Changes
* /usr/share/doc/postgrey-1.37/COPYING
* /usr/share/doc/postgrey-1.37/README
* /usr/share/doc/postgrey-1.37/README.exim
* /usr/share/doc/postgrey-1.37/README.Frugalware
* /usr/share/doc/postgrey-1.37/README.md
{{< /files >}}