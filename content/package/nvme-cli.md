+++
draft = false
title = "nvme-cli 2.10.2-1"
version = "2.10.2-1"
description = "NVMe management command line interface."
date = "2024-08-07T19:54:54"
aliases = "/packages/219154"
categories = ['apps-extra']
upstreamurl = "http://nvmexpress.org/"
arch = "x86_64"
size = "479952"
usize = "1539089"
sha1sum = "18f326d85e7dd2b71c96cc5483c3074e9d95e5c8"
depends = "['libnvme>=1.10', 'libsystemd', 'libuuid>=2.40.2']"
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
* /usr/share/doc/nvme-cli-2.10.2/LICENSE
* /usr/share/doc/nvme-cli-2.10.2/README.md
* /usr/share/zsh/site-functions/_nvme
