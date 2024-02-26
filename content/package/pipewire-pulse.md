+++
draft = false
title = "pipewire-pulse 1.0.3-1"
version = "1.0.3-1"
description = "Pipewire alsa config"
date = "2024-02-03T11:20:37"
aliases = "/packages/220836"
categories = ['xmultimedia-extra']
upstreamurl = "https://pipewire.org/"
arch = "x86_64"
size = "159840"
usize = "482408"
sha1sum = "d9ec480e87b3e0daa6832b83b28a457dd5683344"
depends = "['avahi', 'libpulse', 'wireplumber']"
+++
Pipewire alsa config{{< files text="show files" >}}* /usr/bin/pipewire-pulse
* /usr/lib/pipewire-0.3/libpipewire-module-protocol-pulse.so
* /usr/lib/pipewire-0.3/libpipewire-module-pulse-tunnel.so
* /usr/lib/systemd/user/pipewire-pulse.service
* /usr/lib/systemd/user/pipewire-pulse.socket
* /usr/share/man/man1/pipewire-pulse.1.gz
* /usr/share/pipewire/media-session.d/with-pulseaudio
* /usr/share/pipewire/pipewire-pulse.conf
{{< /files >}}