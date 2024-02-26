+++
draft = false
title = "clight 4.10-1"
version = "4.10-1"
description = "A C daemon that turns your webcam into a light sensor. It can also change"
date = "2023-09-08T13:20:35"
aliases = "/packages/220478"
categories = ['apps-extra']
upstreamurl = "https://github.com/FedeDP/clight"
arch = "x86_64"
size = "84224"
usize = "257566"
sha1sum = "cb1aa3066f758fee2ea19f8b54da7d8f2fef5963"
depends = "['clightd', 'geoclue2', 'gsl>=2.7.1', 'hicolor-icon-theme', 'libconfig', 'popt', 'upower']"
reverse_depends = "['clight-gui']"
+++
A C daemon that turns your webcam into a light sensor. It can also change

{{< files text="show files" >}}* /etc/clight/clight.conf
* /etc/clight/modules.conf.d/backlight.conf
* /etc/clight/modules.conf.d/daytime.conf
* /etc/clight/modules.conf.d/dimmer.conf
* /etc/clight/modules.conf.d/dpms.conf
* /etc/clight/modules.conf.d/gamma.conf
* /etc/clight/modules.conf.d/inhibit.conf
* /etc/clight/modules.conf.d/keyboard.conf
* /etc/clight/modules.conf.d/screen.conf
* /etc/clight/modules.conf.d/sensor.conf
* /etc/xdg/autostart/clight.desktop
* /usr/bin/clight
* /usr/include/clight/public.h
* /usr/share/applications/clightc.desktop
* /usr/share/bash-completion/completions/clight
* /usr/share/clight/inhibit_bl.skel
* /usr/share/clight/nightmode.skel
* /usr/share/clight/synctemp_bumblebee.skel
* /usr/share/dbus-1/services/org.clight.clight.service
* /usr/share/doc/clight-4.10/COPYING
* /usr/share/doc/clight-4.10/README.md
* /usr/share/icons/hicolor/scalable/apps/clight.svg
* /usr/share/man/man1/clight.1.gz
* /usr/share/zsh/site-functions/_clight
{{< /files >}}