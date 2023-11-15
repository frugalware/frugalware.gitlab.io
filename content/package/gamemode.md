+++
draft = false
title = "gamemode 1.7-1"
version = "1.7-1"
date = "2022-08-30T16:59:29"
categories = ['games-extra']
upstreamurl = "https://github.com/FeralInteractive/gamemode"
arch = "x86_64"
size = "71528"
usize = "281134"
sha1sum = "5cba205e5af5bc5bd02492665a468b6c32c722fd"
depends = "['polkit', 'systemd', 'inih>=r49']"
files = "['etc/', 'etc/limits.d/', 'etc/limits.d/45-gamemode.conf', 'etc/security/', 'etc/security/limits.d/', 'etc/security/limits.d/10-gamemode.conf', 'lib/', 'lib/sysusers.d/', 'lib/sysusers.d/gamemode.conf', 'usr/', 'usr/bin/', 'usr/bin/gamemoded', 'usr/bin/gamemodelist', 'usr/bin/gamemoderun', 'usr/bin/gamemode-simulate-game', 'usr/include/', 'usr/include/gamemode_client.h', 'usr/lib/', 'usr/lib/gamemode/', 'usr/lib/gamemode/cpugovctl', 'usr/lib/gamemode/gpuclockctl', 'usr/lib/libgamemodeauto.so', 'usr/lib/libgamemodeauto.so.0', 'usr/lib/libgamemodeauto.so.0.0.0', 'usr/lib/libgamemode.so', 'usr/lib/libgamemode.so.0', 'usr/lib/libgamemode.so.0.0.0', 'usr/lib/pkgconfig/', 'usr/lib/pkgconfig/gamemode.pc', 'usr/lib/pkgconfig/libgamemodeauto.pc', 'usr/lib/systemd/', 'usr/lib/systemd/user/', 'usr/lib/systemd/user/gamemoded.service', 'usr/lib/sysusers.d/', 'usr/lib/sysusers.d/gamemode.conf', 'usr/share/', 'usr/share/dbus-1/', 'usr/share/dbus-1/services/', 'usr/share/dbus-1/services/com.feralinteractive.GameMode.service', 'usr/share/doc/', 'usr/share/doc/gamemode-1.7/', 'usr/share/doc/gamemode-1.7/gamemode.ini', 'usr/share/doc/gamemode-1.7/README.md', 'usr/share/gamemode/', 'usr/share/gamemode/gamemode.ini', 'usr/share/man/', 'usr/share/man/man1/', 'usr/share/man/man1/gamemodelist.1.gz', 'usr/share/man/man1/gamemoderun.1.gz', 'usr/share/man/man1/gamemode-simulate-game.1.gz', 'usr/share/man/man8/', 'usr/share/man/man8/gamemoded.8.gz', 'usr/share/metainfo/', 'usr/share/metainfo/io.github.feralinteractive.gamemode.metainfo.xml', 'usr/share/polkit-1/', 'usr/share/polkit-1/actions/', 'usr/share/polkit-1/actions/com.feralinteractive.GameMode.policy']"
+++
A daemon/lib combo for Linux that allows games to request a set of optimisations be temporarily applied to the host OS