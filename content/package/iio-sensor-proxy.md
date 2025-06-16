+++
draft = false
title = "iio-sensor-proxy 3.7-1"
version = "3.7-1"
description = "IIO accelerometer sensor to input device proxy"
date = "2025-03-13T09:04:04"
aliases = "/packages/221220"
categories = ['apps']
upstreamurl = "https://gitlab.freedesktop.org/hadess/iio-sensor-proxy"
arch = "x86_64"
size = "47300"
usize = "145280"
sha1sum = "c78b0efc9f92153a9fc79a151c99791588011f38"
depends = "['glib2', 'libgudev', 'polkit', 'systemd']"
reverse_depends = "['qt5-sensors', 'qt6-sensors']"
+++
### Description: 
IIO accelerometer sensor to input device proxy

### Files: 
* /usr/bin/monitor-sensor
* /usr/lib/iio-sensor-proxy/iio-sensor-proxy
* /usr/lib/systemd/system/iio-sensor-proxy.service
* /usr/lib/udev/rules.d/80-iio-sensor-proxy.rules
* /usr/share/dbus-1/system.d/net.hadess.SensorProxy.conf
* /usr/share/doc/iio-sensor-proxy-3.7/COPYING
* /usr/share/doc/iio-sensor-proxy-3.7/NEWS
* /usr/share/doc/iio-sensor-proxy-3.7/README.md
* /usr/share/doc/iio-sensor-proxy-3.7/RELEASE.md
* /usr/share/polkit-1/actions/net.hadess.SensorProxy.policy
