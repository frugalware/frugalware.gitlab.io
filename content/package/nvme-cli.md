+++
draft = false
title = "nvme-cli 2.8-1"
version = "2.8-1"
description = "NVMe management command line interface."
date = "2024-02-27T15:14:16"
aliases = "/packages/219154"
categories = ['apps-extra']
upstreamurl = "http://nvmexpress.org/"
arch = "x86_64"
size = "413500"
usize = "1372547"
sha1sum = "49b0dcc0de7323caadd256456e60ca25e0507b8c"
depends = "['libnvme', 'libsystemd', 'libuuid']"
+++
### Description: 
NVMe management command line interface.

### Files: 
* /etc/nvme/discovery.conf
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
* /usr/share/doc/nvme-cli-2.8/LICENSE
* /usr/share/doc/nvme-cli-2.8/README.md
* /usr/share/zsh/site-functions/_nvme
