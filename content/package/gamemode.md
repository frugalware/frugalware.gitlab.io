+++
draft = false
title = "gamemode 1.8.1-3"
version = "1.8.1-3"
description = "A daemon/lib combo for Linux that allows games to request a set of optimisations be temporarily applied to the host OS"
date = "2024-07-02T13:13:42"
aliases = "/packages/220069"
categories = ['games-extra']
upstreamurl = "https://github.com/FeralInteractive/gamemode"
arch = "x86_64"
size = "79064"
usize = "270634"
sha1sum = "9c06391da81548a97e7618ee130e8f02298e8855"
depends = "['inih>=r49', 'libsystemd', 'polkit']"
+++
### Description: 
A daemon/lib combo for Linux that allows games to request a set of optimisations be temporarily applied to the host OS

### Files: 
* /etc/limits.d/45-gamemode.conf
* /etc/security/limits.d/10-gamemode.conf
* /usr/bin/gamemode-simulate-game
* /usr/bin/gamemoded
* /usr/bin/gamemodelist
* /usr/bin/gamemoderun
* /usr/include/gamemode_client.h
* /usr/lib/gamemode/cpucorectl
* /usr/lib/gamemode/cpugovctl
* /usr/lib/gamemode/gpuclockctl
* /usr/lib/gamemode/procsysctl
* /usr/lib/libgamemode.so
* /usr/lib/libgamemode.so.0
* /usr/lib/libgamemode.so.0.0.0
* /usr/lib/libgamemodeauto.so
* /usr/lib/libgamemodeauto.so.0
* /usr/lib/libgamemodeauto.so.0.0.0
* /usr/lib/pkgconfig/gamemode.pc
* /usr/lib/pkgconfig/libgamemodeauto.pc
* /usr/lib/systemd/user/gamemoded.service
* /usr/lib/sysusers.d/gamemode.conf
* /usr/share/dbus-1/services/com.feralinteractive.GameMode.service
* /usr/share/doc/gamemode-1.8.1/gamemode.ini
* /usr/share/doc/gamemode-1.8.1/README.md
* /usr/share/gamemode/gamemode.ini
* /usr/share/man/man1/gamemode-simulate-game.1.gz
* /usr/share/man/man1/gamemodelist.1.gz
* /usr/share/man/man1/gamemoderun.1.gz
* /usr/share/man/man8/gamemoded.8.gz
* /usr/share/metainfo/io.github.feralinteractive.gamemode.metainfo.xml
* /usr/share/polkit-1/actions/com.feralinteractive.GameMode.policy
* /usr/share/polkit-1/rules.d/gamemode.rules
