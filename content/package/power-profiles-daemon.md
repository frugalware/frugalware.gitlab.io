+++
draft = false
title = "power-profiles-daemon 0.22-1"
version = "0.22-1"
description = "Makes power profiles handling available over D-Bus"
date = "2024-09-05T21:20:48"
aliases = "/packages/221428"
categories = ['apps']
upstreamurl = "https://gitlab.freedesktop.org/upower/power-profiles-daemon"
arch = "x86_64"
size = "51132"
usize = "160818"
sha1sum = "7d8d4a68778ec1a758c0564af90c22e734211327"
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
* /usr/share/doc/power-profiles-daemon-0.22/COPYING
* /usr/share/doc/power-profiles-daemon-0.22/NEWS
* /usr/share/doc/power-profiles-daemon-0.22/README.md
* /usr/share/polkit-1/actions/power-profiles-daemon.policy
