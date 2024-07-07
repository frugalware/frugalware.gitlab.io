+++
draft = false
title = "nvme-cli 2.9.1-2"
version = "2.9.1-2"
description = "NVMe management command line interface."
date = "2024-07-07T12:51:24"
aliases = "/packages/219154"
categories = ['apps-extra']
upstreamurl = "http://nvmexpress.org/"
arch = "x86_64"
size = "448836"
usize = "1432991"
sha1sum = "62636cf7608d1e5beba161394744bc0f01dc083b"
depends = "['libnvme', 'libsystemd', 'libuuid>=2.40.2']"
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
* /usr/share/doc/nvme-cli-2.9.1/LICENSE
* /usr/share/doc/nvme-cli-2.9.1/README.md
* /usr/share/zsh/site-functions/_nvme
