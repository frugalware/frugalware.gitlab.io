+++
draft = false
title = "virtualbox-guest-additions 7.0.18-13"
version = "7.0.18-13"
description = "VirtualBox guest Additions"
date = "2024-07-12T11:15:33"
aliases = "/packages/219162"
categories = ['xapps-extra']
upstreamurl = "http://www.virtualbox.org"
arch = "x86_64"
size = "784288"
usize = "3169550"
sha1sum = "d27e2ba1970c648a28b4751c996f56a40496c50a"
depends = "['kernel=6.9.9-1', 'libxcomposite', 'libxdamage', 'libxmu', 'libxrandr', 'mesa-dri-drivers', 'pam', 'xf86-video-vmware']"
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
* /usr/lib/modules/6.9.9-fw1/kernel/misc/vboxguest.ko.zst
* /usr/lib/modules/6.9.9-fw1/kernel/misc/vboxsf.ko.zst
* /usr/lib/security/pam_vbox.so
* /usr/lib/systemd/system/multi-user.target.wants/vboxdrmclient.path
* /usr/lib/systemd/system/multi-user.target.wants/vboxdrmclient.service
* /usr/lib/systemd/system/multi-user.target.wants/vboxservice.service
* /usr/lib/systemd/system/vboxdrmclient.path
* /usr/lib/systemd/system/vboxdrmclient.service
* /usr/lib/systemd/system/vboxservice.service
* /usr/lib/sysusers.d/virtualbox-guest-utils.conf
* /usr/lib/udev/rules.d/60-vboxguest.rules
