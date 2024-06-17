+++
draft = false
title = "libpulse 17.0-4"
version = "17.0-4"
description = "pulseaduio client library"
date = "2024-06-17T14:33:04"
aliases = "/packages/136453"
categories = ['xmultimedia']
upstreamurl = "http://www.freedesktop.org/wiki/Software/PulseAudio/"
arch = "x86_64"
size = "1220716"
usize = "4811570"
sha1sum = "2f9cad5502e90ce70eae3e569cdcabd77d959422"
depends = "['alsa-lib', 'dbus>=1.10.10-4', 'fftw>=3.3.4-4', 'flac', 'libasyncns>=0.8-3', 'libogg', 'libsm', 'libsndfile>=1.0.26-2', 'libsystemd>=242-3', 'libtool>=2.4.6-4', 'libudev>=242-3', 'libvorbis', 'libx11>=1.6.3-4', 'libxtst', 'orc>=0.4.24-2', 'soxr', 'speexdsp>=1.2rc3-3', 'tdb>=1.3.10-2', 'webrtc-audio-processing']"
reverse_depends = "['alsa-plugin-pulseaudio', 'chromium-browser', 'conky', 'efl', 'enlightenment', 'ffmpeg', 'ffmpeg4.4', 'firefox', 'fluidsynth', 'gst1-plugins-good-pulseaudio', 'gtk-vnc', 'guvcview', 'i3status', 'libao-pulse', 'libcanberra-pulseaudio', 'libmikmod', 'libopenmpt', 'mencoder', 'mplayer', 'mpv', 'openjre', 'pavucontrol-qt', 'pcaudiolib', 'phonon-qt5', 'phonon-qt6', 'pipewire-pulse', 'pocketsphinx', 'pulse-autoconf', 'pulseaudio', 'pulseaudio-qt', 'python3-pulsectl', 'qt5-multimedia', 'sdlmame', 'sox', 'speech-dispatcher', 'spice-glib', 'terminology', 'thunderbird', 'virtualbox', 'vlc-pulseaudio', 'wine', 'wine-devel']"
+++
### Description: 
pulseaduio client library

### Files: 
* /etc/pulse/client.conf
* /usr/include/pulse/cdecl.h
* /usr/include/pulse/channelmap.h
* /usr/include/pulse/context.h
* /usr/include/pulse/def.h
* /usr/include/pulse/direction.h
* /usr/include/pulse/error.h
* /usr/include/pulse/ext-device-manager.h
* /usr/include/pulse/ext-device-restore.h
* /usr/include/pulse/ext-stream-restore.h
* /usr/include/pulse/format.h
* /usr/include/pulse/gccmacro.h
* /usr/include/pulse/glib-mainloop.h
* /usr/include/pulse/introspect.h
* /usr/include/pulse/mainloop-api.h
* /usr/include/pulse/mainloop-signal.h
* /usr/include/pulse/mainloop.h
* /usr/include/pulse/operation.h
* /usr/include/pulse/proplist.h
* /usr/include/pulse/pulseaudio.h
* /usr/include/pulse/rtclock.h
* /usr/include/pulse/sample.h
* /usr/include/pulse/scache.h
* /usr/include/pulse/simple.h
* /usr/include/pulse/stream.h
* /usr/include/pulse/subscribe.h
* /usr/include/pulse/thread-mainloop.h
* /usr/include/pulse/timeval.h
* /usr/include/pulse/utf8.h
* /usr/include/pulse/util.h
* /usr/include/pulse/version.h
* /usr/include/pulse/volume.h
* /usr/include/pulse/xmalloc.h
* /usr/lib/cmake/PulseAudio/PulseAudioConfig.cmake
* /usr/lib/cmake/PulseAudio/PulseAudioConfigVersion.cmake
* /usr/lib/libpulse-mainloop-glib.so
* /usr/lib/libpulse-mainloop-glib.so.0
* /usr/lib/libpulse-mainloop-glib.so.0.0.6
* /usr/lib/libpulse-simple.so
* /usr/lib/libpulse-simple.so.0
* /usr/lib/libpulse-simple.so.0.1.1
* /usr/lib/libpulse.so
* /usr/lib/libpulse.so.0
* /usr/lib/libpulse.so.0.24.3
* /usr/lib/pkgconfig/libpulse-mainloop-glib.pc
* /usr/lib/pkgconfig/libpulse-simple.pc
* /usr/lib/pkgconfig/libpulse.pc
* /usr/lib/pulseaudio/libpulsecommon-17.0.so
* /usr/lib/pulseaudio/libpulsecore-17.0.so
* /usr/lib/pulseaudio/libpulsedsp.so
* /usr/lib/pulseaudio/modules/libalsa-util.so
* /usr/lib/pulseaudio/modules/libbluez5-util.so
* /usr/lib/pulseaudio/modules/libcli.so
* /usr/lib/pulseaudio/modules/liboss-util.so
* /usr/lib/pulseaudio/modules/libprotocol-cli.so
* /usr/lib/pulseaudio/modules/libprotocol-http.so
* /usr/lib/pulseaudio/modules/libprotocol-native.so
* /usr/lib/pulseaudio/modules/libprotocol-simple.so
* /usr/lib/pulseaudio/modules/librtp.so
* /usr/lib/pulseaudio/modules/module-allow-passthrough.so
* /usr/lib/pulseaudio/modules/module-alsa-card.so
* /usr/lib/pulseaudio/modules/module-alsa-sink.so
* /usr/lib/pulseaudio/modules/module-alsa-source.so
* /usr/lib/pulseaudio/modules/module-always-sink.so
* /usr/lib/pulseaudio/modules/module-always-source.so
* /usr/lib/pulseaudio/modules/module-augment-properties.so
* /usr/lib/pulseaudio/modules/module-bluetooth-discover.so
* /usr/lib/pulseaudio/modules/module-bluetooth-policy.so
* /usr/lib/pulseaudio/modules/module-bluez5-device.so
* /usr/lib/pulseaudio/modules/module-bluez5-discover.so
* /usr/lib/pulseaudio/modules/module-card-restore.so
* /usr/lib/pulseaudio/modules/module-cli-protocol-tcp.so
* /usr/lib/pulseaudio/modules/module-cli-protocol-unix.so
* /usr/lib/pulseaudio/modules/module-cli.so
* /usr/lib/pulseaudio/modules/module-combine-sink.so
* /usr/lib/pulseaudio/modules/module-combine.so
* /usr/lib/pulseaudio/modules/module-console-kit.so
* /usr/lib/pulseaudio/modules/module-dbus-protocol.so
* /usr/lib/pulseaudio/modules/module-default-device-restore.so
* /usr/lib/pulseaudio/modules/module-detect.so
* /usr/lib/pulseaudio/modules/module-device-manager.so
* /usr/lib/pulseaudio/modules/module-device-restore.so
* /usr/lib/pulseaudio/modules/module-echo-cancel.so
* /usr/lib/pulseaudio/modules/module-equalizer-sink.so
* /usr/lib/pulseaudio/modules/module-filter-apply.so
* /usr/lib/pulseaudio/modules/module-filter-heuristics.so
* /usr/lib/pulseaudio/modules/module-gsettings.so
* /usr/lib/pulseaudio/modules/module-hal-detect.so
* /usr/lib/pulseaudio/modules/module-http-protocol-tcp.so
* /usr/lib/pulseaudio/modules/module-http-protocol-unix.so
* /usr/lib/pulseaudio/modules/module-intended-roles.so
* /usr/lib/pulseaudio/modules/module-ladspa-sink.so
* /usr/lib/pulseaudio/modules/module-loopback.so
* /usr/lib/pulseaudio/modules/module-match.so
* /usr/lib/pulseaudio/modules/module-mmkbd-evdev.so
* /usr/lib/pulseaudio/modules/module-native-protocol-fd.so
* /usr/lib/pulseaudio/modules/module-native-protocol-tcp.so
* /usr/lib/pulseaudio/modules/module-native-protocol-unix.so
* /usr/lib/pulseaudio/modules/module-null-sink.so
* /usr/lib/pulseaudio/modules/module-null-source.so
* /usr/lib/pulseaudio/modules/module-oss.so
* /usr/lib/pulseaudio/modules/module-pipe-sink.so
* /usr/lib/pulseaudio/modules/module-pipe-source.so
* /usr/lib/pulseaudio/modules/module-position-event-sounds.so
* /usr/lib/pulseaudio/modules/module-remap-sink.so
* /usr/lib/pulseaudio/modules/module-remap-source.so
* /usr/lib/pulseaudio/modules/module-rescue-streams.so
* /usr/lib/pulseaudio/modules/module-role-cork.so
* /usr/lib/pulseaudio/modules/module-role-ducking.so
* /usr/lib/pulseaudio/modules/module-rtp-recv.so
* /usr/lib/pulseaudio/modules/module-rtp-send.so
* /usr/lib/pulseaudio/modules/module-rygel-media-server.so
* /usr/lib/pulseaudio/modules/module-simple-protocol-tcp.so
* /usr/lib/pulseaudio/modules/module-simple-protocol-unix.so
* /usr/lib/pulseaudio/modules/module-sine-source.so
* /usr/lib/pulseaudio/modules/module-sine.so
* /usr/lib/pulseaudio/modules/module-stream-restore.so
* /usr/lib/pulseaudio/modules/module-suspend-on-idle.so
* /usr/lib/pulseaudio/modules/module-switch-on-connect.so
* /usr/lib/pulseaudio/modules/module-switch-on-port-available.so
* /usr/lib/pulseaudio/modules/module-systemd-login.so
* /usr/lib/pulseaudio/modules/module-tunnel-sink-new.so
* /usr/lib/pulseaudio/modules/module-tunnel-sink.so
* /usr/lib/pulseaudio/modules/module-tunnel-source-new.so
* /usr/lib/pulseaudio/modules/module-tunnel-source.so
* /usr/lib/pulseaudio/modules/module-udev-detect.so
* /usr/lib/pulseaudio/modules/module-virtual-sink.so
* /usr/lib/pulseaudio/modules/module-virtual-source.so
* /usr/lib/pulseaudio/modules/module-virtual-surround-sink.so
* /usr/lib/pulseaudio/modules/module-volume-restore.so
* /usr/lib/pulseaudio/pulse/gsettings-helper
* /usr/lib/systemd/system/pulseaudio-x11.service
* /usr/lib/systemd/system/pulseaudio.service
* /usr/lib/systemd/system/pulseaudio.socket
* /usr/lib/systemd/user/pulseaudio-x11.service
* /usr/lib/systemd/user/pulseaudio.service
* /usr/lib/systemd/user/pulseaudio.socket
* /usr/lib/sysusers.d/pulseaudio.conf
* /usr/lib/udev/rules.d/90-pulseaudio.rules
* /usr/share/man/man5/default.pa.5.gz
* /usr/share/man/man5/pulse-cli-syntax.5.gz
* /usr/share/man/man5/pulse-client.conf.5.gz
* /usr/share/man/man5/pulse-daemon.conf.5.gz
