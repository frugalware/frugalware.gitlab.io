+++
draft = false
title = "lib32-libpulse 17.0-7"
version = "17.0-7"
description = "pulseaduio client library (32-bit)"
date = "2025-02-14T15:01:33"
aliases = "/packages/217944"
categories = ['lib32-extra']
upstreamurl = "http://www.freedesktop.org/wiki/Software/PulseAudio/"
arch = "x86_64"
size = "1116604"
usize = "4955160"
sha1sum = "6fed7597aae8782cae820f285971a24fd4a3ff05"
depends = "['lib32-fftw>=3.3.4-4', 'lib32-libasyncns>=0.8-3', 'lib32-libdbus', 'lib32-libsndfile>=1.0.26-2', 'lib32-libtool>=2.4.6-4', 'lib32-libudev', 'lib32-libx11>=1.6.3-4', 'lib32-openssl', 'lib32-orc>=0.4.24-2', 'lib32-speexdsp>=1.2rc3-3', 'lib32-tdb>=1.3.10-2']"
reverse_depends = "['lib32-libmikmod', 'lib32-pipewire', 'steam-native']"
+++
### Description: 
pulseaduio client library (32-bit)

### Files: 
* /usr/i686-frugalware-linux/bin/pa-info
* /usr/i686-frugalware-linux/bin/pacat
* /usr/i686-frugalware-linux/bin/pacmd
* /usr/i686-frugalware-linux/bin/pactl
* /usr/i686-frugalware-linux/bin/padsp
* /usr/i686-frugalware-linux/bin/pamon
* /usr/i686-frugalware-linux/bin/paplay
* /usr/i686-frugalware-linux/bin/parec
* /usr/i686-frugalware-linux/bin/parecord
* /usr/i686-frugalware-linux/bin/pasuspender
* /usr/i686-frugalware-linux/bin/pulseaudio
* /usr/i686-frugalware-linux/bin/qpaeq
* /usr/i686-frugalware-linux/include/pulse/cdecl.h
* /usr/i686-frugalware-linux/include/pulse/channelmap.h
* /usr/i686-frugalware-linux/include/pulse/context.h
* /usr/i686-frugalware-linux/include/pulse/def.h
* /usr/i686-frugalware-linux/include/pulse/direction.h
* /usr/i686-frugalware-linux/include/pulse/error.h
* /usr/i686-frugalware-linux/include/pulse/ext-device-manager.h
* /usr/i686-frugalware-linux/include/pulse/ext-device-restore.h
* /usr/i686-frugalware-linux/include/pulse/ext-stream-restore.h
* /usr/i686-frugalware-linux/include/pulse/format.h
* /usr/i686-frugalware-linux/include/pulse/gccmacro.h
* /usr/i686-frugalware-linux/include/pulse/glib-mainloop.h
* /usr/i686-frugalware-linux/include/pulse/introspect.h
* /usr/i686-frugalware-linux/include/pulse/mainloop-api.h
* /usr/i686-frugalware-linux/include/pulse/mainloop-signal.h
* /usr/i686-frugalware-linux/include/pulse/mainloop.h
* /usr/i686-frugalware-linux/include/pulse/operation.h
* /usr/i686-frugalware-linux/include/pulse/proplist.h
* /usr/i686-frugalware-linux/include/pulse/pulseaudio.h
* /usr/i686-frugalware-linux/include/pulse/rtclock.h
* /usr/i686-frugalware-linux/include/pulse/sample.h
* /usr/i686-frugalware-linux/include/pulse/scache.h
* /usr/i686-frugalware-linux/include/pulse/simple.h
* /usr/i686-frugalware-linux/include/pulse/stream.h
* /usr/i686-frugalware-linux/include/pulse/subscribe.h
* /usr/i686-frugalware-linux/include/pulse/thread-mainloop.h
* /usr/i686-frugalware-linux/include/pulse/timeval.h
* /usr/i686-frugalware-linux/include/pulse/utf8.h
* /usr/i686-frugalware-linux/include/pulse/util.h
* /usr/i686-frugalware-linux/include/pulse/version.h
* /usr/i686-frugalware-linux/include/pulse/volume.h
* /usr/i686-frugalware-linux/include/pulse/xmalloc.h
* /usr/lib32/cmake/PulseAudio/PulseAudioConfig.cmake
* /usr/lib32/cmake/PulseAudio/PulseAudioConfigVersion.cmake
* /usr/lib32/libpulse-mainloop-glib.so
* /usr/lib32/libpulse-mainloop-glib.so.0
* /usr/lib32/libpulse-mainloop-glib.so.0.0.6
* /usr/lib32/libpulse-simple.so
* /usr/lib32/libpulse-simple.so.0
* /usr/lib32/libpulse-simple.so.0.1.1
* /usr/lib32/libpulse.so
* /usr/lib32/libpulse.so.0
* /usr/lib32/libpulse.so.0.24.3
* /usr/lib32/pkgconfig/libpulse-mainloop-glib.pc
* /usr/lib32/pkgconfig/libpulse-simple.pc
* /usr/lib32/pkgconfig/libpulse.pc
* /usr/lib32/pulseaudio/libpulsecommon-17.0.so
* /usr/lib32/pulseaudio/libpulsecore-17.0.so
* /usr/lib32/pulseaudio/libpulsedsp.so
* /usr/lib32/pulseaudio/modules/libalsa-util.so
* /usr/lib32/pulseaudio/modules/libcli.so
* /usr/lib32/pulseaudio/modules/liboss-util.so
* /usr/lib32/pulseaudio/modules/libprotocol-cli.so
* /usr/lib32/pulseaudio/modules/libprotocol-http.so
* /usr/lib32/pulseaudio/modules/libprotocol-native.so
* /usr/lib32/pulseaudio/modules/libprotocol-simple.so
* /usr/lib32/pulseaudio/modules/libraop.so
* /usr/lib32/pulseaudio/modules/librtp.so
* /usr/lib32/pulseaudio/modules/module-allow-passthrough.so
* /usr/lib32/pulseaudio/modules/module-alsa-card.so
* /usr/lib32/pulseaudio/modules/module-alsa-sink.so
* /usr/lib32/pulseaudio/modules/module-alsa-source.so
* /usr/lib32/pulseaudio/modules/module-always-sink.so
* /usr/lib32/pulseaudio/modules/module-always-source.so
* /usr/lib32/pulseaudio/modules/module-augment-properties.so
* /usr/lib32/pulseaudio/modules/module-card-restore.so
* /usr/lib32/pulseaudio/modules/module-cli-protocol-tcp.so
* /usr/lib32/pulseaudio/modules/module-cli-protocol-unix.so
* /usr/lib32/pulseaudio/modules/module-cli.so
* /usr/lib32/pulseaudio/modules/module-combine-sink.so
* /usr/lib32/pulseaudio/modules/module-combine.so
* /usr/lib32/pulseaudio/modules/module-console-kit.so
* /usr/lib32/pulseaudio/modules/module-dbus-protocol.so
* /usr/lib32/pulseaudio/modules/module-default-device-restore.so
* /usr/lib32/pulseaudio/modules/module-detect.so
* /usr/lib32/pulseaudio/modules/module-device-manager.so
* /usr/lib32/pulseaudio/modules/module-device-restore.so
* /usr/lib32/pulseaudio/modules/module-echo-cancel.so
* /usr/lib32/pulseaudio/modules/module-equalizer-sink.so
* /usr/lib32/pulseaudio/modules/module-filter-apply.so
* /usr/lib32/pulseaudio/modules/module-filter-heuristics.so
* /usr/lib32/pulseaudio/modules/module-hal-detect.so
* /usr/lib32/pulseaudio/modules/module-http-protocol-tcp.so
* /usr/lib32/pulseaudio/modules/module-http-protocol-unix.so
* /usr/lib32/pulseaudio/modules/module-intended-roles.so
* /usr/lib32/pulseaudio/modules/module-ladspa-sink.so
* /usr/lib32/pulseaudio/modules/module-loopback.so
* /usr/lib32/pulseaudio/modules/module-match.so
* /usr/lib32/pulseaudio/modules/module-mmkbd-evdev.so
* /usr/lib32/pulseaudio/modules/module-native-protocol-fd.so
* /usr/lib32/pulseaudio/modules/module-native-protocol-tcp.so
* /usr/lib32/pulseaudio/modules/module-native-protocol-unix.so
* /usr/lib32/pulseaudio/modules/module-null-sink.so
* /usr/lib32/pulseaudio/modules/module-null-source.so
* /usr/lib32/pulseaudio/modules/module-oss.so
* /usr/lib32/pulseaudio/modules/module-pipe-sink.so
* /usr/lib32/pulseaudio/modules/module-pipe-source.so
* /usr/lib32/pulseaudio/modules/module-position-event-sounds.so
* /usr/lib32/pulseaudio/modules/module-raop-sink.so
* /usr/lib32/pulseaudio/modules/module-remap-sink.so
* /usr/lib32/pulseaudio/modules/module-remap-source.so
* /usr/lib32/pulseaudio/modules/module-rescue-streams.so
* /usr/lib32/pulseaudio/modules/module-role-cork.so
* /usr/lib32/pulseaudio/modules/module-role-ducking.so
* /usr/lib32/pulseaudio/modules/module-rtp-recv.so
* /usr/lib32/pulseaudio/modules/module-rtp-send.so
* /usr/lib32/pulseaudio/modules/module-rygel-media-server.so
* /usr/lib32/pulseaudio/modules/module-simple-protocol-tcp.so
* /usr/lib32/pulseaudio/modules/module-simple-protocol-unix.so
* /usr/lib32/pulseaudio/modules/module-sine-source.so
* /usr/lib32/pulseaudio/modules/module-sine.so
* /usr/lib32/pulseaudio/modules/module-stream-restore.so
* /usr/lib32/pulseaudio/modules/module-suspend-on-idle.so
* /usr/lib32/pulseaudio/modules/module-switch-on-connect.so
* /usr/lib32/pulseaudio/modules/module-switch-on-port-available.so
* /usr/lib32/pulseaudio/modules/module-systemd-login.so
* /usr/lib32/pulseaudio/modules/module-tunnel-sink-new.so
* /usr/lib32/pulseaudio/modules/module-tunnel-sink.so
* /usr/lib32/pulseaudio/modules/module-tunnel-source-new.so
* /usr/lib32/pulseaudio/modules/module-tunnel-source.so
* /usr/lib32/pulseaudio/modules/module-udev-detect.so
* /usr/lib32/pulseaudio/modules/module-virtual-sink.so
* /usr/lib32/pulseaudio/modules/module-virtual-source.so
* /usr/lib32/pulseaudio/modules/module-virtual-surround-sink.so
* /usr/lib32/pulseaudio/modules/module-volume-restore.so
