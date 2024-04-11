+++
draft = false
title = "power-profiles-daemon 0.21-2"
version = "0.21-2"
description = "Makes power profiles handling available over D-Bus"
date = "2024-04-11T09:46:22"
aliases = "/packages/221428"
categories = ['apps']
upstreamurl = "https://gitlab.freedesktop.org/upower/power-profiles-daemon"
arch = "x86_64"
size = "48944"
usize = "157986"
sha1sum = "b2c99f0ae9705fd1e3de1f31dd5f2e6dda8f5be6"
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
* /usr/share/doc/power-profiles-daemon-0.21/COPYING
* /usr/share/doc/power-profiles-daemon-0.21/NEWS
* /usr/share/doc/power-profiles-daemon-0.21/README.md
* /usr/share/polkit-1/actions/power-profiles-daemon.policy
