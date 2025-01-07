+++
draft = false
title = "clightd 5.9-2"
version = "5.9-2"
description = "Bus interface to change screen brightness and capture frames from webcam."
date = "2024-05-17T11:50:48"
aliases = "/packages/220476"
categories = ['apps-extra']
upstreamurl = "https://github.com/FedeDP/clightd"
arch = "x86_64"
size = "64772"
usize = "197634"
sha1sum = "12b9f60ad06f4441ca4c3caed7ec6cbc2b5f5263"
depends = "['ddcutil', 'libdrm', 'libiio', 'libjpeg-turbo', 'libmodule', 'libsystemd', 'libusb1', 'libx11', 'libxext', 'libxrandr', 'pipewire', 'polkit', 'wayland']"
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
