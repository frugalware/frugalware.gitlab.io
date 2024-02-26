+++
draft = false
title = "systemd-nspawn 255.3-2"
version = "255.3-2"
description = "Spawn a command or OS in a light-weight container."
date = "2024-02-01T13:22:45"
aliases = "/packages/219953"
categories = ['base-extra']
upstreamurl = "http://www.freedesktop.org/wiki/Software/systemd"
arch = "x86_64"
size = "182680"
usize = "412201"
sha1sum = "94e8b2c20eca5c53779b64673ce50db31ffdac13"
depends = "['cryptsetup-luks', 'kmod', 'libidn2', 'libseccomp', 'libsystemd>=255.3']"
+++
Spawn a command or OS in a light-weight container."

{{< files text="show files" >}}* /usr/bin/systemd-nspawn
* /usr/lib/systemd/system/systemd-nspawn@.service
* /usr/lib/tmpfiles.d/systemd-nspawn.conf
* /usr/share/bash-completion/completions/systemd-nspawn
* /usr/share/man/man1/systemd-nspawn.1.gz
* /usr/share/man/man5/systemd.nspawn.5.gz
* /usr/share/zsh/site-functions/_systemd-nspawn
{{< /files >}}