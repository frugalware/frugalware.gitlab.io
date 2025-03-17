+++
draft = false
title = "nvme-cli 2.12-1"
version = "2.12-1"
description = "NVMe management command line interface."
date = "2025-03-17T13:20:33"
aliases = "/packages/219154"
categories = ['apps-extra']
upstreamurl = "http://nvmexpress.org/"
arch = "x86_64"
size = "527508"
usize = "1697454"
sha1sum = "e0dcf74808a808bbc4fe02bb789709175e6ee3ac"
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
* /usr/share/doc/nvme-cli-2.12/LICENSE
* /usr/share/doc/nvme-cli-2.12/README.md
* /usr/share/zsh/site-functions/_nvme
