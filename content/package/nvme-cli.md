+++
draft = false
title = "nvme-cli 2.14-1"
version = "2.14-1"
description = "NVMe management command line interface."
date = "2025-05-23T12:42:06"
aliases = "/packages/219154"
categories = ['apps-extra']
upstreamurl = "http://nvmexpress.org/"
arch = "x86_64"
size = "547064"
usize = "1768352"
sha1sum = "0d9ea71208b375eee74cdc354bcfb8e0dd7e4c40"
depends = "['libnvme>=1.14', 'libsystemd', 'libuuid>=2.40.2']"
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
* /usr/lib/udev/rules.d/71-nvmf-vastdata.rules
* /usr/share/bash-completion/completions/nvme
* /usr/share/doc/nvme-cli-2.14/LICENSE
* /usr/share/doc/nvme-cli-2.14/README.md
* /usr/share/zsh/site-functions/_nvme
