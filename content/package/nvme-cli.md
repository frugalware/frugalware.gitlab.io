+++
draft = false
title = "nvme-cli 2.7.1-1"
version = "2.7.1-1"
description = "NVMe management command line interface."
date = "2024-01-14T13:06:47"
aliases = "/packages/219154"
categories = ['apps-extra']
upstreamurl = "http://nvmexpress.org/"
arch = "x86_64"
size = "409728"
usize = "1350192"
sha1sum = "172e43515a8c6c15483e48f5b079dee4142296c1"
depends = "['libnvme', 'libsystemd', 'libuuid']"
+++
NVMe management command line interface.{{< spoiler text="show files" >}}* /etc/nvme/discovery.conf
* /usr/bin/nvme
* /usr/lib/dracut/dracut.conf.d/70-nvmf-autoconnect.conf
* /usr/lib/systemd/system/nvmefc-boot-connections.service
* /usr/lib/systemd/system/nvmf-autoconnect.service
* /usr/lib/systemd/system/nvmf-connect-nbft.service
* /usr/lib/systemd/system/nvmf-connect.target
* /usr/lib/systemd/system/nvmf-connect@.service
* /usr/lib/udev/rules.d/65-persistent-net-nbft.rules
* /usr/lib/udev/rules.d/70-nvmf-autoconnect.rules
* /usr/lib/udev/rules.d/71-nvmf-netapp.rules
* /usr/share/bash-completion/completions/nvme
* /usr/share/doc/nvme-cli-2.7.1/LICENSE
* /usr/share/doc/nvme-cli-2.7.1/README.md
* /usr/share/zsh/site-functions/_nvme
{{< /spoiler >}}