+++
draft = false
title = "clightd 5.8-4"
version = "5.8-4"
description = "Bus interface to change screen brightness and capture frames from webcam."
date = "2024-01-31T21:54:01"
aliases = "/packages/220476"
categories = ['apps-extra']
upstreamurl = "https://github.com/FedeDP/clightd"
arch = "x86_64"
size = "63396"
usize = "193538"
sha1sum = "2702cb7bed1b230f5072d44982e24e60484b22a4"
depends = "['ddcutil', 'libdrm', 'libiio', 'libjpeg-turbo', 'libmodule', 'libsystemd', 'libusb', 'libx11', 'libxext', 'libxrandr', 'pipewire', 'polkit', 'wayland']"
reverse_depends = "['clight']"
+++
Bus interface to change screen brightness and capture frames from webcam."

{{< files text="show files" >}}* /etc/dbus-1/system.d/org.clightd.clightd.conf
* /usr/lib/clightd/clightd
* /usr/lib/modules-load.d/i2c_clightd.conf
* /usr/lib/systemd/system/clightd.service
* /usr/share/dbus-1/system-services/org.clightd.clightd.service
* /usr/share/doc/clightd-5.8/COPYING
* /usr/share/doc/clightd-5.8/README.md
* /usr/share/polkit-1/actions/org.clightd.clightd.policy
{{< /files >}}