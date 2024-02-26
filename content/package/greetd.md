+++
draft = false
title = "greetd 0.9.0-2"
version = "0.9.0-2"
description = "Generic greeter daemon"
date = "2024-01-14T14:37:52"
aliases = "/packages/220837"
categories = ['apps-extra']
upstreamurl = "https://git.sr.ht/~kennylevinsen/greetd"
arch = "x86_64"
size = "331408"
usize = "1207170"
sha1sum = "3bfe5db6e0d5b2fd0c7fb92266f3418b34c99dc0"
depends = "['libcap-ng', 'pam', 'systemd']"
reverse_depends = "['greetd-qtgreet']"
+++
Generic greeter daemon"

{{< files text="show files" >}}* /etc/greetd/config.toml
* /etc/pam.d/greetd
* /usr/bin/agreety
* /usr/bin/greetd
* /usr/lib/systemd/system/greetd.service
* /usr/lib/sysusers.d/greetd.conf
* /usr/share/doc/greetd-0.9.0/LICENSE
* /usr/share/doc/greetd-0.9.0/README.md
{{< /files >}}