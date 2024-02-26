+++
draft = false
title = "kio-fuse 5.1.0-1"
version = "5.1.0-1"
description = "FUSE interface for KIO"
date = "2023-12-10T12:34:28"
aliases = "/packages/220906"
categories = ['kde5']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "63336"
usize = "188473"
sha1sum = "a4b4fb5b18161eb0d6db1ade7b97cd66c39fa6b1"
depends = "['fuse3', 'kio>=5.112.0']"
reverse_depends = "['xdg-desktop-portal-kde']"
+++
FUSE interface for KIO

{{< files text="show files" >}}* /usr/lib/kf5/kio-fuse
* /usr/lib/systemd/user/kio-fuse.service
* /usr/lib/tmpfiles.d/kio-fuse-tmpfiles.conf
* /usr/share/dbus-1/services/org.kde.KIOFuse.service
* /usr/share/doc/kio-fuse-5.1.0/README.md
* /usr/share/doc/kio-fuse-5.1.0/TODO
{{< /files >}}