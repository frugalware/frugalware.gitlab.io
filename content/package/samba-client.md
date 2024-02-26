+++
draft = false
title = "samba-client 4.19.5-1"
version = "4.19.5-1"
description = "SMB client tools."
date = "2024-02-23T10:09:13"
aliases = "/packages/15146"
categories = ['network']
upstreamurl = "http://www.samba.org"
arch = "x86_64"
size = "458072"
usize = "1421012"
sha1sum = "78958e895703e94e35ae239d23ed6c572bf0c6f3"
depends = "['libarchive>=3.2.1', 'libkrb5', 'libsmbclient>=4.19.5', 'libsystemd>=231-7', 'libwbclient>=4.19.5', 'popt>=1.16-6', 'readline>=8.0', 'talloc>=2.3.0', 'tdb>=1.4.3-2']"
reverse_depends = "['gvfs-smb', 'kio-extras', 'mpv', 'samba', 'smb4k']"
+++
SMB client tools.

{{< files text="show files" >}}* /usr/bin/net
* /usr/bin/nmblookup
* /usr/bin/smbclient
* /usr/bin/smbspool
* /usr/lib/samba/smbspool_krb5_wrapper
* /usr/share/man/man1/nmblookup.1.gz
* /usr/share/man/man1/smbclient.1.gz
* /usr/share/man/man8/net.8.gz
* /usr/share/man/man8/smbspool.8.gz
{{< /files >}}