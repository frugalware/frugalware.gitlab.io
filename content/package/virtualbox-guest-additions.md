+++
draft = false
title = "virtualbox-guest-additions 7.0.16-2"
version = "7.0.16-2"
description = "VirtualBox guest Additions"
date = "2024-04-29T12:19:33"
aliases = "/packages/219162"
categories = ['xapps-extra']
upstreamurl = "http://www.virtualbox.org"
arch = "x86_64"
size = "750164"
usize = "3125804"
sha1sum = "f4fc53b5d32dff1c9b70948ef629ccbc95b8bc4c"
depends = "['kernel=6.8.8-1', 'libxcomposite', 'libxdamage', 'libxmu', 'libxrandr', 'mesa-dri-drivers', 'pam', 'xf86-video-vmware']"
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
* /usr/lib/modules/6.8.8-fw1/kernel/misc/vboxguest.ko.zst
* /usr/lib/modules/6.8.8-fw1/kernel/misc/vboxsf.ko.zst
* /usr/lib/security/pam_vbox.so
* /usr/lib/systemd/system/multi-user.target.wants/vboxdrmclient.path
* /usr/lib/systemd/system/multi-user.target.wants/vboxdrmclient.service
* /usr/lib/systemd/system/multi-user.target.wants/vboxservice.service
* /usr/lib/systemd/system/vboxdrmclient.path
* /usr/lib/systemd/system/vboxdrmclient.service
* /usr/lib/systemd/system/vboxservice.service
* /usr/lib/sysusers.d/virtualbox-guest-utils.conf
* /usr/lib/udev/rules.d/60-vboxguest.rules
