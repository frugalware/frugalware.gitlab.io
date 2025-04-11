+++
draft = false
title = "nvme-cli 2.13-1"
version = "2.13-1"
description = "NVMe management command line interface."
date = "2025-04-11T18:07:20"
aliases = "/packages/219154"
categories = ['apps-extra']
upstreamurl = "http://nvmexpress.org/"
arch = "x86_64"
size = "534880"
usize = "1719760"
sha1sum = "8d1b9246280dccb0c7b27d4bfd9f92b20446a80e"
depends = "['libnvme>=1.12', 'libsystemd', 'libuuid>=2.40.2']"
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
* /usr/lib/udev/rules.d/70-nvmf-keys.rules
* /usr/lib/udev/rules.d/71-nvmf-netapp.rules
* /usr/share/bash-completion/completions/nvme
* /usr/share/doc/nvme-cli-2.13/LICENSE
* /usr/share/doc/nvme-cli-2.13/README.md
* /usr/share/zsh/site-functions/_nvme
