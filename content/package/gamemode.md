+++
draft = false
title = "gamemode 1.8.1-2"
version = "1.8.1-2"
description = "A daemon/lib combo for Linux that allows games to request a set of optimisations be temporarily applied to the host OS"
date = "2024-01-14T13:18:31"
aliases = "/packages/220069"
categories = ['games-extra']
upstreamurl = "https://github.com/FeralInteractive/gamemode"
arch = "x86_64"
size = "78692"
usize = "320098"
sha1sum = "ad6534737aa4a26b117b4a66f98bee2e00acb37a"
depends = "['inih>=r49', 'polkit', 'systemd']"
+++
A daemon/lib combo for Linux that allows games to request a set of optimisations be temporarily applied to the host OS"

{{< files text="show files" >}}* /etc/limits.d/45-gamemode.conf
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
{{< /files >}}