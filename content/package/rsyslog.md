+++
draft = false
title = "rsyslog 8.2312.0-2"
version = "8.2312.0-2"
date = "2024-01-09T20:08:23"
aliases = "/packages/135785"
categories = ['apps-extra']
upstreamurl = "http://www.rsyslog.com/"
arch = "x86_64"
size = "638764"
usize = "2409616"
sha1sum = "7ed58d01ffaaf4f9d2e8a1ac866012f10380065c"
depends = "['curl', 'gnutls>=3.4.8', 'libestr>=0.1.10-4', 'libfastjson>=0.99.8', 'liblogging>=1.0.5-3']"
reverse depends = "['rsyslog-gssapi', 'rsyslog-mysql', 'rsyslog-pgsql', 'rsyslog-snmp', 'rsyslog-udpspoof']"
files = "['/etc/logrotate.d/rsyslog', '/etc/rsyslog.conf', '/usr/bin/rsyslogd', '/usr/lib/rsyslog/fmhash.so', '/usr/lib/rsyslog/fmhttp.so', '/usr/lib/rsyslog/imfile.so', '/usr/lib/rsyslog/imklog.so', '/usr/lib/rsyslog/immark.so', '/usr/lib/rsyslog/imtcp.so', '/usr/lib/rsyslog/imudp.so', '/usr/lib/rsyslog/imuxsock.so', '/usr/lib/rsyslog/lmcry_gcry.so', '/usr/lib/rsyslog/lmnet.so', '/usr/lib/rsyslog/lmnetstrms.so', '/usr/lib/rsyslog/lmnsd_gtls.so', '/usr/lib/rsyslog/lmnsd_ptcp.so', '/usr/lib/rsyslog/lmregexp.so', '/usr/lib/rsyslog/lmtcpclt.so', '/usr/lib/rsyslog/lmtcpsrv.so', '/usr/lib/rsyslog/lmzlibw.so', '/usr/lib/rsyslog/mmexternal.so', '/usr/lib/rsyslog/ommail.so', '/usr/lib/rsyslog/omprog.so', '/usr/lib/rsyslog/omtesting.so', '/usr/lib/rsyslog/omuxsock.so', '/usr/lib/systemd/system/rsyslog.service', '/usr/share/doc/rsyslog-8.2312.0/AUTHORS', '/usr/share/doc/rsyslog-8.2312.0/ChangeLog', '/usr/share/doc/rsyslog-8.2312.0/COPYING', '/usr/share/doc/rsyslog-8.2312.0/COPYING.ASL20', '/usr/share/doc/rsyslog-8.2312.0/COPYING.LESSER', '/usr/share/doc/rsyslog-8.2312.0/INSTALL', '/usr/share/doc/rsyslog-8.2312.0/NEWS', '/usr/share/doc/rsyslog-8.2312.0/README', '/usr/share/doc/rsyslog-8.2312.0/README.md', '/usr/share/man/man5/rsyslog.conf.5.gz', '/usr/share/man/man8/rsyslogd.8.gz']"
+++
Enhanced system logging and kernel message trapping daemon