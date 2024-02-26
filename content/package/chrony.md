+++
draft = false
title = "chrony 4.5-2"
version = "4.5-2"
description = "Dial-up friendly NTP daemon and excellent replacement for NTP on desktop systems"
date = "2024-01-07T21:10:55"
aliases = "/packages/136603"
categories = ['network']
upstreamurl = "http://chrony.tuxfamily.org/"
arch = "x86_64"
size = "276188"
usize = "583836"
sha1sum = "5521c38486fdd4a70b3a318769ab1d1da071beae"
depends = "['libcap>=2.24-4', 'nettle>=3.6', 'readline>=8.0']"
reverse_depends = "['networkmanager-dispatcher-chrony']"
+++
Dial-up friendly NTP daemon and excellent replacement for NTP on desktop systems"

{{< files text="show files" >}}* /etc/chrony.conf
* /etc/chrony.keys
* /usr/bin/chronyc
* /usr/bin/chronyd
* /usr/lib/systemd/system/chrony.service
* /usr/share/doc/chrony-4.5/COPYING
* /usr/share/doc/chrony-4.5/FAQ
* /usr/share/doc/chrony-4.5/INSTALL
* /usr/share/doc/chrony-4.5/NEWS
* /usr/share/doc/chrony-4.5/README
* /usr/share/man/man1/chronyc.1.gz
* /usr/share/man/man5/chrony.conf.5.gz
* /usr/share/man/man8/chronyd.8.gz
{{< /files >}}