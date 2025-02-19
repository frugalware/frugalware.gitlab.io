+++
draft = false
title = "power-profiles-daemon 0.30-1"
version = "0.30-1"
description = "Makes power profiles handling available over D-Bus"
date = "2025-02-19T09:30:44"
aliases = "/packages/221428"
categories = ['apps']
upstreamurl = "https://gitlab.freedesktop.org/upower/power-profiles-daemon"
arch = "x86_64"
size = "55104"
usize = "173133"
sha1sum = "6c20d14c4abab983d36b74d7d60cbe0cb4d40375"
depends = "['libsystemd', 'polkit', 'upower']"
reverse_depends = "['powerdevil']"
+++
### Description: 
Makes power profiles handling available over D-Bus

### Files: 
* /usr/bin/powerprofilesctl
* /usr/lib/power-profiles-daemon/power-profiles-daemon
* /usr/lib/systemd/system/power-profiles-daemon.service
* /usr/share/dbus-1/system-services/net.hadess.PowerProfiles.service
* /usr/share/dbus-1/system-services/org.freedesktop.UPower.PowerProfiles.service
* /usr/share/dbus-1/system.d/net.hadess.PowerProfiles.conf
* /usr/share/dbus-1/system.d/org.freedesktop.UPower.PowerProfiles.conf
* /usr/share/doc/power-profiles-daemon-0.30/COPYING
* /usr/share/doc/power-profiles-daemon-0.30/NEWS
* /usr/share/doc/power-profiles-daemon-0.30/README.md
* /usr/share/polkit-1/actions/power-profiles-daemon.policy
