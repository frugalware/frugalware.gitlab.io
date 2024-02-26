+++
draft = false
title = "systemd-remote 255.3-2"
version = "255.3-2"
description = "systemd remote journald"
date = "2024-02-01T13:22:45"
aliases = "/packages/217488"
categories = ['base-extra']
upstreamurl = "http://www.freedesktop.org/wiki/Software/systemd"
arch = "x86_64"
size = "85244"
usize = "194025"
sha1sum = "e7e6a1e395b65038bb110eb54a450caaf9e5bab9"
depends = "['libmicrohttpd>=0.9.58-2', 'lz4>=1.8.1.2-2', 'openssl>=3.0.7', 'systemd=255.3']"
+++
systemd remote journald{{< files text="show files" >}}* /etc/systemd/journal-remote.conf
* /etc/systemd/journal-upload.conf
* /usr/lib/systemd/system/systemd-journal-gatewayd.service
* /usr/lib/systemd/system/systemd-journal-gatewayd.socket
* /usr/lib/systemd/system/systemd-journal-remote.service
* /usr/lib/systemd/system/systemd-journal-remote.socket
* /usr/lib/systemd/system/systemd-journal-upload.service
* /usr/lib/systemd/systemd-journal-gatewayd
* /usr/lib/systemd/systemd-journal-remote
* /usr/lib/systemd/systemd-journal-upload
* /usr/lib/sysusers.d/systemd-remote.conf
* /usr/share/man/man5/journal-remote.conf.5.gz
* /usr/share/man/man5/journal-remote.conf.d.5.gz
* /usr/share/man/man5/journal-upload.conf.5.gz
* /usr/share/man/man5/journal-upload.conf.d.5.gz
* /usr/share/man/man8/systemd-journal-gatewayd.8.gz
* /usr/share/man/man8/systemd-journal-gatewayd.service.8.gz
* /usr/share/man/man8/systemd-journal-gatewayd.socket.8.gz
* /usr/share/man/man8/systemd-journal-remote.8.gz
* /usr/share/man/man8/systemd-journal-remote.service.8.gz
* /usr/share/man/man8/systemd-journal-remote.socket.8.gz
* /usr/share/man/man8/systemd-journal-upload.8.gz
* /usr/share/man/man8/systemd-journal-upload.service.8.gz
* /usr/share/systemd/gatewayd/browse.html
{{< /files >}}