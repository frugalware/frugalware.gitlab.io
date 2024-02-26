+++
draft = false
title = "libinput 1.25.0-1"
version = "1.25.0-1"
description = "A library to handle input devices in Wayland compositors and to provide a generic X.Org input driver"
date = "2024-01-17T21:18:50"
aliases = "/packages/201250"
categories = ['x11']
upstreamurl = "https://gitlab.freedesktop.org/libinput/libinput"
arch = "x86_64"
size = "246708"
usize = "1019998"
sha1sum = "d99a4f209cf00086bf4b6aecbd41da1ae05c7db0"
depends = "['libevdev>=1.5.4-2', 'libudev>=242', 'libwacom>=0.29', 'mtdev>=1.1.5-4']"
reverse_depends = "['efl', 'enlightenment', 'libinput-debug-events', 'libinput-gestures', 'qt5-base', 'qt6-base', 'terminology', 'virtualbox', 'weston', 'wlroots', 'xf86-input-libinput']"
+++
A library to handle input devices in Wayland compositors and to provide a generic X.Org input driver{{< spoiler text="show files" >}}* /usr/bin/libinput
* /usr/bin/libinput-list-devices
* /usr/include/libinput.h
* /usr/lib/libinput.so
* /usr/lib/libinput.so.10
* /usr/lib/libinput.so.10.13.0
* /usr/lib/libinput/libinput/libinput-analyze
* /usr/lib/libinput/libinput/libinput-analyze-per-slot-delta
* /usr/lib/libinput/libinput/libinput-analyze-recording
* /usr/lib/libinput/libinput/libinput-analyze-touch-down-state
* /usr/lib/libinput/libinput/libinput-debug-tablet
* /usr/lib/libinput/libinput/libinput-list-devices
* /usr/lib/libinput/libinput/libinput-list-kernel-devices
* /usr/lib/libinput/libinput/libinput-measure
* /usr/lib/libinput/libinput/libinput-measure-fuzz
* /usr/lib/libinput/libinput/libinput-measure-touch-size
* /usr/lib/libinput/libinput/libinput-measure-touchpad-pressure
* /usr/lib/libinput/libinput/libinput-measure-touchpad-size
* /usr/lib/libinput/libinput/libinput-measure-touchpad-tap
* /usr/lib/libinput/libinput/libinput-quirks
* /usr/lib/libinput/libinput/libinput-record
* /usr/lib/libinput/libinput/libinput-replay
* /usr/lib/libinput/libinput/libinput-test
* /usr/lib/pkgconfig/libinput.pc
* /usr/lib/udev/libinput-device-group
* /usr/lib/udev/libinput-fuzz-extract
* /usr/lib/udev/libinput-fuzz-to-zero
* /usr/lib/udev/rules.d/80-libinput-device-groups.rules
* /usr/lib/udev/rules.d/90-libinput-fuzz-override.rules
* /usr/share/doc/libinput-1.25.0/COPYING
* /usr/share/doc/libinput-1.25.0/README.md
* /usr/share/libinput/10-generic-keyboard.quirks
* /usr/share/libinput/10-generic-mouse.quirks
* /usr/share/libinput/10-generic-trackball.quirks
* /usr/share/libinput/30-vendor-a4tech.quirks
* /usr/share/libinput/30-vendor-aiptek.quirks
* /usr/share/libinput/30-vendor-alps.quirks
* /usr/share/libinput/30-vendor-contour.quirks
* /usr/share/libinput/30-vendor-cypress.quirks
* /usr/share/libinput/30-vendor-elantech.quirks
* /usr/share/libinput/30-vendor-glorious.quirks
* /usr/share/libinput/30-vendor-ibm.quirks
* /usr/share/libinput/30-vendor-kensington.quirks
* /usr/share/libinput/30-vendor-logitech.quirks
* /usr/share/libinput/30-vendor-madcatz.quirks
* /usr/share/libinput/30-vendor-microsoft.quirks
* /usr/share/libinput/30-vendor-oracle.quirks
* /usr/share/libinput/30-vendor-qemu.quirks
* /usr/share/libinput/30-vendor-razer.quirks
* /usr/share/libinput/30-vendor-synaptics.quirks
* /usr/share/libinput/30-vendor-trust.quirks
* /usr/share/libinput/30-vendor-vmware.quirks
* /usr/share/libinput/30-vendor-wacom.quirks
* /usr/share/libinput/50-system-acer.quirks
* /usr/share/libinput/50-system-apple.quirks
* /usr/share/libinput/50-system-asus.quirks
* /usr/share/libinput/50-system-chicony.quirks
* /usr/share/libinput/50-system-chuwi.quirks
* /usr/share/libinput/50-system-cyborg.quirks
* /usr/share/libinput/50-system-dell.quirks
* /usr/share/libinput/50-system-framework.quirks
* /usr/share/libinput/50-system-gigabyte.quirks
* /usr/share/libinput/50-system-google.quirks
* /usr/share/libinput/50-system-gpd.quirks
* /usr/share/libinput/50-system-graviton.quirks
* /usr/share/libinput/50-system-hp.quirks
* /usr/share/libinput/50-system-huawei.quirks
* /usr/share/libinput/50-system-lenovo.quirks
* /usr/share/libinput/50-system-pine64.quirks
* /usr/share/libinput/50-system-sony.quirks
* /usr/share/libinput/50-system-starlabs.quirks
* /usr/share/libinput/50-system-system76.quirks
* /usr/share/libinput/50-system-toshiba.quirks
* /usr/share/libinput/50-system-vaio.quirks
* /usr/share/man/man1/libinput-analyze-per-slot-delta.1.gz
* /usr/share/man/man1/libinput-analyze-recording.1.gz
* /usr/share/man/man1/libinput-analyze-touch-down-state.1.gz
* /usr/share/man/man1/libinput-analyze.1.gz
* /usr/share/man/man1/libinput-debug-events.1.gz
* /usr/share/man/man1/libinput-debug-gui.1.gz
* /usr/share/man/man1/libinput-debug-tablet.1.gz
* /usr/share/man/man1/libinput-list-devices.1.gz
* /usr/share/man/man1/libinput-list-kernel-devices.1.gz
* /usr/share/man/man1/libinput-measure-fuzz.1.gz
* /usr/share/man/man1/libinput-measure-touch-size.1.gz
* /usr/share/man/man1/libinput-measure-touchpad-pressure.1.gz
* /usr/share/man/man1/libinput-measure-touchpad-size.1.gz
* /usr/share/man/man1/libinput-measure-touchpad-tap.1.gz
* /usr/share/man/man1/libinput-measure.1.gz
* /usr/share/man/man1/libinput-quirks-list.1.gz
* /usr/share/man/man1/libinput-quirks-validate.1.gz
* /usr/share/man/man1/libinput-quirks.1.gz
* /usr/share/man/man1/libinput-record.1.gz
* /usr/share/man/man1/libinput-replay.1.gz
* /usr/share/man/man1/libinput-test.1.gz
* /usr/share/man/man1/libinput.1.gz
* /usr/share/zsh/site-functions/_libinput
{{< /spoiler >}}