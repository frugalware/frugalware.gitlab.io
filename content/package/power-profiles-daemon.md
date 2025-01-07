+++
draft = false
title = "power-profiles-daemon 0.23-2"
version = "0.23-2"
description = "Makes power profiles handling available over D-Bus"
date = "2024-12-30T21:04:12"
aliases = "/packages/221428"
categories = ['apps']
upstreamurl = "https://gitlab.freedesktop.org/upower/power-profiles-daemon"
arch = "x86_64"
size = "52056"
usize = "161140"
sha1sum = "34d86f34e5aa651b73ba8ef4e677cc382a73fecb"
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
* /usr/share/doc/power-profiles-daemon-0.23/COPYING
* /usr/share/doc/power-profiles-daemon-0.23/NEWS
* /usr/share/doc/power-profiles-daemon-0.23/README.md
* /usr/share/polkit-1/actions/power-profiles-daemon.policy
