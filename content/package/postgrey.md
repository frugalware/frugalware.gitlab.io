+++
draft = false
title = "postgrey 1.37-4"
version = "1.37-4"
date = "2019-04-29T22:37:52"
categories = ['network-extra']
upstreamurl = "http://postgrey.schweikert.ch/"
arch = "x86_64"
size = "34500"
usize = "177379"
sha1sum = "c4f2b178acb1fc18b497d948973177d2585d5b03"
depends = "['perl>=5.28.2', 'perl-net-server', 'perl-io-multiplex', 'perl-berkeleydb', 'db>=4.7.25', 'postfix>=2.1', 'systemd']"
files = "['etc/', 'etc/postfix/', 'etc/postfix/postgrey_whitelist_clients', 'etc/postfix/postgrey_whitelist_recipients', 'etc/sysconfig/', 'etc/sysconfig/postgrey', 'lib/', 'lib/systemd/', 'lib/systemd/system/', 'lib/systemd/system/postgrey.service', 'usr/', 'usr/bin/', 'usr/bin/postgreyreport', 'usr/sbin/', 'usr/sbin/postgrey', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/postgrey-1.37/', 'usr/share/doc/postgrey-1.37/COPYING', 'usr/share/doc/postgrey-1.37/Changes', 'usr/share/doc/postgrey-1.37/README', 'usr/share/doc/postgrey-1.37/README.Frugalware', 'usr/share/doc/postgrey-1.37/README.exim', 'usr/share/doc/postgrey-1.37/README.md', 'var/', 'var/spool/', 'var/spool/postfix/', 'var/spool/postfix/postgrey/']"
+++
a Postfix policy server implementing greylisting