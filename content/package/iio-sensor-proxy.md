+++
draft = false
title = "iio-sensor-proxy 3.6-1"
version = "3.6-1"
description = "IIO accelerometer sensor to input device proxy"
date = "2025-01-23T09:14:47"
aliases = "/packages/221220"
categories = ['apps']
upstreamurl = "https://gitlab.freedesktop.org/hadess/iio-sensor-proxy"
arch = "x86_64"
size = "47020"
usize = "144939"
sha1sum = "2d57ed37d3a44abf28904d17f0c507651cff8315"
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
* /usr/share/doc/iio-sensor-proxy-3.6/COPYING
* /usr/share/doc/iio-sensor-proxy-3.6/NEWS
* /usr/share/doc/iio-sensor-proxy-3.6/README.md
* /usr/share/doc/iio-sensor-proxy-3.6/RELEASE.md
* /usr/share/polkit-1/actions/net.hadess.SensorProxy.policy
