+++
draft = false
title = "iio-sensor-proxy 3.5-3"
version = "3.5-3"
description = "IIO accelerometer sensor to input device proxy"
date = "2024-01-30T10:27:54"
aliases = "/packages/221220"
categories = ['apps']
upstreamurl = "https://gitlab.freedesktop.org/hadess/iio-sensor-proxy"
arch = "x86_64"
size = "44328"
usize = "144475"
sha1sum = "40a939271cdcd8fcf8e6fc66d34b87005e71de1f"
depends = "['glib2', 'libgudev', 'polkit', 'systemd']"
reverse_depends = "['qt5-sensors', 'qt6-sensors']"
+++
IIO accelerometer sensor to input device proxy{{< files text="show files" >}}* /usr/bin/monitor-sensor
* /usr/lib/iio-sensor-proxy/iio-sensor-proxy
* /usr/lib/systemd/system/iio-sensor-proxy.service
* /usr/lib/udev/rules.d/80-iio-sensor-proxy.rules
* /usr/share/dbus-1/system.d/net.hadess.SensorProxy.conf
* /usr/share/doc/iio-sensor-proxy-3.5/COPYING
* /usr/share/doc/iio-sensor-proxy-3.5/NEWS
* /usr/share/doc/iio-sensor-proxy-3.5/README.md
* /usr/share/polkit-1/actions/net.hadess.SensorProxy.policy
{{< /files >}}