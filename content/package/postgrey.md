+++
draft = false
title = "postgrey 1.37-5"
version = "1.37-5"
date = "2024-01-09T14:56:47"
categories = ['network-extra']
upstreamurl = "http://postgrey.schweikert.ch/"
arch = "x86_64"
size = "34516"
usize = "107746"
sha1sum = "46bb9df09c3ebcd53e4cc6a5ffb73da35e472d46"
depends = "['perl>=5.28.2', 'perl-net-server', 'perl-io-multiplex', 'perl-berkeleydb', 'db>=4.7.25', 'postfix>=2.1']"
files = "['etc/', 'etc/postfix/', 'etc/postfix/postgrey_whitelist_clients', 'etc/postfix/postgrey_whitelist_recipients', 'etc/sysconfig/', 'etc/sysconfig/postgrey', 'usr/', 'usr/bin/', 'usr/bin/postgrey', 'usr/bin/postgreyreport', 'usr/lib/', 'usr/lib/systemd/', 'usr/lib/systemd/system/', 'usr/lib/systemd/system/postgrey.service', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/postgrey-1.37/', 'usr/share/doc/postgrey-1.37/COPYING', 'usr/share/doc/postgrey-1.37/Changes', 'usr/share/doc/postgrey-1.37/README', 'usr/share/doc/postgrey-1.37/README.Frugalware', 'usr/share/doc/postgrey-1.37/README.exim', 'usr/share/doc/postgrey-1.37/README.md', 'var/', 'var/spool/', 'var/spool/postfix/', 'var/spool/postfix/postgrey/']"
+++
a Postfix policy server implementing greylisting