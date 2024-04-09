+++
draft = false
title = "power-profiles-daemon 0.21-1"
version = "0.21-1"
description = "Makes power profiles handling available over D-Bus"
date = "2024-04-09T12:19:48"
aliases = "/packages/221428"
categories = ['apps-extra']
upstreamurl = "https://gitlab.freedesktop.org/upower/power-profiles-daemon"
arch = "x86_64"
size = "48692"
usize = "157986"
sha1sum = "f8e5eee85da791c42cf74e0023bafa0d6ec0ef8a"
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
