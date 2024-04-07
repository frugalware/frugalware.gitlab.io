+++
draft = false
title = "clightd 5.9-1"
version = "5.9-1"
description = "Bus interface to change screen brightness and capture frames from webcam."
date = "2024-04-07T17:22:43"
aliases = "/packages/220476"
categories = ['apps-extra']
upstreamurl = "https://github.com/FedeDP/clightd"
arch = "x86_64"
size = "64544"
usize = "197634"
sha1sum = "9df9bcd602d5700fbc13209823e59a5f1f936b50"
depends = "['ddcutil', 'libdrm', 'libiio', 'libjpeg-turbo', 'libmodule', 'libsystemd', 'libusb', 'libx11', 'libxext', 'libxrandr', 'pipewire', 'polkit', 'wayland']"
reverse_depends = "['clight']"
+++
### Description: 
Bus interface to change screen brightness and capture frames from webcam.

### Files: 
* /etc/dbus-1/system.d/org.clightd.clightd.conf
* /usr/lib/clightd/clightd
* /usr/lib/modules-load.d/i2c_clightd.conf
* /usr/lib/systemd/system/clightd.service
* /usr/share/dbus-1/system-services/org.clightd.clightd.service
* /usr/share/doc/clightd-5.9/COPYING
* /usr/share/doc/clightd-5.9/README.md
* /usr/share/polkit-1/actions/org.clightd.clightd.policy
