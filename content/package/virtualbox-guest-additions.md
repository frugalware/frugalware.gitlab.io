+++
draft = false
title = "virtualbox-guest-additions 7.1.8-3"
version = "7.1.8-3"
description = "VirtualBox guest Additions"
date = "2025-04-26T12:16:45"
aliases = "/packages/219162"
categories = ['xapps-extra']
upstreamurl = "http://www.virtualbox.org"
arch = "x86_64"
size = "854312"
usize = "3418229"
sha1sum = "95eca575a7f2332ed163fff62b94a0b8532c5b23"
depends = "['kernel=6.14.4-1', 'libxcomposite', 'libxdamage', 'libxmu', 'libxrandr', 'mesa-dri-drivers', 'pam', 'xf86-video-vmware']"
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
* /usr/lib/modules/6.14.4-fw1/kernel/misc/vboxguest.ko.zst
* /usr/lib/modules/6.14.4-fw1/kernel/misc/vboxsf.ko.zst
* /usr/lib/security/pam_vbox.so
* /usr/lib/systemd/system/multi-user.target.wants/vboxdrmclient.path
* /usr/lib/systemd/system/multi-user.target.wants/vboxdrmclient.service
* /usr/lib/systemd/system/multi-user.target.wants/vboxservice.service
* /usr/lib/systemd/system/vboxdrmclient.path
* /usr/lib/systemd/system/vboxdrmclient.service
* /usr/lib/systemd/system/vboxservice.service
* /usr/lib/sysusers.d/virtualbox-guest-utils.conf
* /usr/lib/udev/rules.d/60-vboxguest.rules
