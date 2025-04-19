+++
draft = false
title = "virtualbox-guest-additions 7.1.8-1"
version = "7.1.8-1"
description = "VirtualBox guest Additions"
date = "2025-04-19T14:16:09"
aliases = "/packages/219162"
categories = ['xapps-extra']
upstreamurl = "http://www.virtualbox.org"
arch = "x86_64"
size = "855584"
usize = "3418242"
sha1sum = "e1c800e626dbe890c90d230e3219e8f02c760b96"
depends = "['kernel=6.14.2-1', 'libxcomposite', 'libxdamage', 'libxmu', 'libxrandr', 'mesa-dri-drivers', 'pam', 'xf86-video-vmware']"
+++
### Description: 
VirtualBox guest Additions

### Files: 
* /etc/xdg/autostart/vboxclient.desktop
* /usr/bin/mount.vboxsf
* /usr/bin/VBoxClient
* /usr/bin/VBoxClient-all
* /usr/bin/VBoxControl
* /usr/bin/VBoxDRMClient
* /usr/bin/VBoxService
* /usr/lib/modules/6.14.2-fw1/kernel/misc/vboxguest.ko.zst
* /usr/lib/modules/6.14.2-fw1/kernel/misc/vboxsf.ko.zst
* /usr/lib/security/pam_vbox.so
* /usr/lib/systemd/system/multi-user.target.wants/vboxdrmclient.path
* /usr/lib/systemd/system/multi-user.target.wants/vboxdrmclient.service
* /usr/lib/systemd/system/multi-user.target.wants/vboxservice.service
* /usr/lib/systemd/system/vboxdrmclient.path
* /usr/lib/systemd/system/vboxdrmclient.service
* /usr/lib/systemd/system/vboxservice.service
* /usr/lib/sysusers.d/virtualbox-guest-utils.conf
* /usr/lib/udev/rules.d/60-vboxguest.rules
