+++
draft = false
title = "gamemode 1.8.1-1"
version = "1.8.1-1"
date = "2023-12-17T13:54:54"
categories = ['games-extra']
upstreamurl = "https://github.com/FeralInteractive/gamemode"
arch = "x86_64"
size = "78716"
usize = "320113"
sha1sum = "0b2a03346f5eb5cc813e2e333afde3b9d487ba44"
depends = "['polkit', 'systemd', 'inih>=r49']"
files = "['etc/', 'etc/limits.d/', 'etc/limits.d/45-gamemode.conf', 'etc/security/', 'etc/security/limits.d/', 'etc/security/limits.d/10-gamemode.conf', 'lib/', 'lib/sysusers.d/', 'lib/sysusers.d/gamemode.conf', 'usr/', 'usr/bin/', 'usr/bin/gamemoded', 'usr/bin/gamemodelist', 'usr/bin/gamemoderun', 'usr/bin/gamemode-simulate-game', 'usr/include/', 'usr/include/gamemode_client.h', 'usr/lib/', 'usr/lib/gamemode/', 'usr/lib/gamemode/cpucorectl', 'usr/lib/gamemode/cpugovctl', 'usr/lib/gamemode/gpuclockctl', 'usr/lib/gamemode/procsysctl', 'usr/lib/libgamemodeauto.so', 'usr/lib/libgamemodeauto.so.0', 'usr/lib/libgamemodeauto.so.0.0.0', 'usr/lib/libgamemode.so', 'usr/lib/libgamemode.so.0', 'usr/lib/libgamemode.so.0.0.0', 'usr/lib/pkgconfig/', 'usr/lib/pkgconfig/gamemode.pc', 'usr/lib/pkgconfig/libgamemodeauto.pc', 'usr/lib/systemd/', 'usr/lib/systemd/user/', 'usr/lib/systemd/user/gamemoded.service', 'usr/lib/sysusers.d/', 'usr/lib/sysusers.d/gamemode.conf', 'usr/share/', 'usr/share/dbus-1/', 'usr/share/dbus-1/services/', 'usr/share/dbus-1/services/com.feralinteractive.GameMode.service', 'usr/share/doc/', 'usr/share/doc/gamemode-1.8.1/', 'usr/share/doc/gamemode-1.8.1/gamemode.ini', 'usr/share/doc/gamemode-1.8.1/README.md', 'usr/share/gamemode/', 'usr/share/gamemode/gamemode.ini', 'usr/share/man/', 'usr/share/man/man1/', 'usr/share/man/man1/gamemodelist.1.gz', 'usr/share/man/man1/gamemoderun.1.gz', 'usr/share/man/man1/gamemode-simulate-game.1.gz', 'usr/share/man/man8/', 'usr/share/man/man8/gamemoded.8.gz', 'usr/share/metainfo/', 'usr/share/metainfo/io.github.feralinteractive.gamemode.metainfo.xml', 'usr/share/polkit-1/', 'usr/share/polkit-1/actions/', 'usr/share/polkit-1/actions/com.feralinteractive.GameMode.policy', 'usr/share/polkit-1/rules.d/', 'usr/share/polkit-1/rules.d/gamemode.rules']"
+++
A daemon/lib combo for Linux that allows games to request a set of optimisations be temporarily applied to the host OS