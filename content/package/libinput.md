+++
draft = false
title = "libinput 1.24.0-1"
version = "1.24.0-1"
date = "2023-08-25T11:20:41"
categories = ['x11', 'xorg-core', 'xorg-libs']
upstreamurl = "https://gitlab.freedesktop.org/libinput/libinput"
arch = "x86_64"
size = "246312"
usize = "1018101"
sha1sum = "522176f3de78d05a1081e048941e93c1b32ee95a"
depends = "['mtdev>=1.1.5-4', 'libevdev>=1.5.4-2', 'libudev>=242', 'libwacom>=0.29']"
files = "['etc/', 'etc/libinput/', 'lib/', 'lib/udev/', 'lib/udev/libinput-device-group', 'lib/udev/libinput-fuzz-extract', 'lib/udev/libinput-fuzz-to-zero', 'lib/udev/rules.d/', 'lib/udev/rules.d/80-libinput-device-groups.rules', 'lib/udev/rules.d/90-libinput-fuzz-override.rules', 'usr/', 'usr/bin/', 'usr/bin/libinput', 'usr/bin/libinput-list-devices', 'usr/include/', 'usr/include/libinput.h', 'usr/lib/', 'usr/lib/libinput/', 'usr/lib/libinput/libinput/', 'usr/lib/libinput/libinput/libinput-analyze', 'usr/lib/libinput/libinput/libinput-analyze-per-slot-delta', 'usr/lib/libinput/libinput/libinput-analyze-recording', 'usr/lib/libinput/libinput/libinput-analyze-touch-down-state', 'usr/lib/libinput/libinput/libinput-debug-tablet', 'usr/lib/libinput/libinput/libinput-list-devices', 'usr/lib/libinput/libinput/libinput-list-kernel-devices', 'usr/lib/libinput/libinput/libinput-measure', 'usr/lib/libinput/libinput/libinput-measure-fuzz', 'usr/lib/libinput/libinput/libinput-measure-touchpad-pressure', 'usr/lib/libinput/libinput/libinput-measure-touchpad-size', 'usr/lib/libinput/libinput/libinput-measure-touchpad-tap', 'usr/lib/libinput/libinput/libinput-measure-touch-size', 'usr/lib/libinput/libinput/libinput-quirks', 'usr/lib/libinput/libinput/libinput-record', 'usr/lib/libinput/libinput/libinput-replay', 'usr/lib/libinput/libinput/libinput-test', 'usr/lib/libinput.so', 'usr/lib/libinput.so.10', 'usr/lib/libinput.so.10.13.0', 'usr/lib/pkgconfig/', 'usr/lib/pkgconfig/libinput.pc', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/libinput-1.24.0/', 'usr/share/doc/libinput-1.24.0/COPYING', 'usr/share/doc/libinput-1.24.0/README.md', 'usr/share/libinput/', 'usr/share/libinput/10-generic-keyboard.quirks', 'usr/share/libinput/10-generic-mouse.quirks', 'usr/share/libinput/10-generic-trackball.quirks', 'usr/share/libinput/30-vendor-a4tech.quirks', 'usr/share/libinput/30-vendor-aiptek.quirks', 'usr/share/libinput/30-vendor-alps.quirks', 'usr/share/libinput/30-vendor-contour.quirks', 'usr/share/libinput/30-vendor-cypress.quirks', 'usr/share/libinput/30-vendor-elantech.quirks', 'usr/share/libinput/30-vendor-glorious.quirks', 'usr/share/libinput/30-vendor-ibm.quirks', 'usr/share/libinput/30-vendor-kensington.quirks', 'usr/share/libinput/30-vendor-logitech.quirks', 'usr/share/libinput/30-vendor-madcatz.quirks', 'usr/share/libinput/30-vendor-microsoft.quirks', 'usr/share/libinput/30-vendor-razer.quirks', 'usr/share/libinput/30-vendor-synaptics.quirks', 'usr/share/libinput/30-vendor-trust.quirks', 'usr/share/libinput/30-vendor-vmware.quirks', 'usr/share/libinput/30-vendor-wacom.quirks', 'usr/share/libinput/50-framework.quirks', 'usr/share/libinput/50-system-acer.quirks', 'usr/share/libinput/50-system-apple.quirks', 'usr/share/libinput/50-system-asus.quirks', 'usr/share/libinput/50-system-chicony.quirks', 'usr/share/libinput/50-system-chuwi.quirks', 'usr/share/libinput/50-system-cyborg.quirks', 'usr/share/libinput/50-system-dell.quirks', 'usr/share/libinput/50-system-gigabyte.quirks', 'usr/share/libinput/50-system-google.quirks', 'usr/share/libinput/50-system-gpd.quirks', 'usr/share/libinput/50-system-hp.quirks', 'usr/share/libinput/50-system-huawei.quirks', 'usr/share/libinput/50-system-lenovo.quirks', 'usr/share/libinput/50-system-pine64.quirks', 'usr/share/libinput/50-system-sony.quirks', 'usr/share/libinput/50-system-starlabs.quirks', 'usr/share/libinput/50-system-system76.quirks', 'usr/share/libinput/50-system-toshiba.quirks', 'usr/share/libinput/50-system-vaio.quirks', 'usr/share/man/', 'usr/share/man/man1/', 'usr/share/man/man1/libinput.1.gz', 'usr/share/man/man1/libinput-analyze.1.gz', 'usr/share/man/man1/libinput-analyze-per-slot-delta.1.gz', 'usr/share/man/man1/libinput-analyze-recording.1.gz', 'usr/share/man/man1/libinput-analyze-touch-down-state.1.gz', 'usr/share/man/man1/libinput-debug-events.1.gz', 'usr/share/man/man1/libinput-debug-gui.1.gz', 'usr/share/man/man1/libinput-debug-tablet.1.gz', 'usr/share/man/man1/libinput-list-devices.1.gz', 'usr/share/man/man1/libinput-list-kernel-devices.1.gz', 'usr/share/man/man1/libinput-measure.1.gz', 'usr/share/man/man1/libinput-measure-fuzz.1.gz', 'usr/share/man/man1/libinput-measure-touchpad-pressure.1.gz', 'usr/share/man/man1/libinput-measure-touchpad-size.1.gz', 'usr/share/man/man1/libinput-measure-touchpad-tap.1.gz', 'usr/share/man/man1/libinput-measure-touch-size.1.gz', 'usr/share/man/man1/libinput-quirks.1.gz', 'usr/share/man/man1/libinput-quirks-list.1.gz', 'usr/share/man/man1/libinput-quirks-validate.1.gz', 'usr/share/man/man1/libinput-record.1.gz', 'usr/share/man/man1/libinput-replay.1.gz', 'usr/share/man/man1/libinput-test.1.gz', 'usr/share/zsh/', 'usr/share/zsh/site-functions/', 'usr/share/zsh/site-functions/_libinput']"
+++
A library to handle input devices in Wayland compositors and to provide a generic X.Org input driver