+++
draft = false
title = "upower 1.90.2-3"
version = "1.90.2-3"
description = "upower provides a daemon, API and command line tools for managing power devices attached to the system."
date = "2024-01-06T15:12:39"
aliases = "/packages/103197"
categories = ['xapps']
upstreamurl = "http://upower.freedesktop.org"
arch = "x86_64"
size = "167656"
usize = "1032219"
sha1sum = "35d88e3010905a5fddac0bd52fadaa9e217e665d"
depends = "['dbus-glib>=0.108-3', 'libgudev>=230-7', 'libimobiledevice>=1.3.0', 'libsystemd>=231-6', 'libusb1>=1.0.20-5']"
reverse_depends = "['clight', 'mixxx', 'solid']"
+++
upower provides a daemon, API and command line tools for managing power devices attached to the system."

{{< files text="show files" >}}* /etc/UPower/UPower.conf
* /usr/bin/upower
* /usr/include/libupower-glib/up-autocleanups.h
* /usr/include/libupower-glib/up-client.h
* /usr/include/libupower-glib/up-device.h
* /usr/include/libupower-glib/up-history-item.h
* /usr/include/libupower-glib/up-stats-item.h
* /usr/include/libupower-glib/up-types.h
* /usr/include/libupower-glib/up-version.h
* /usr/include/libupower-glib/upower.h
* /usr/lib/girepository-1.0/UPowerGlib-1.0.typelib
* /usr/lib/libupower-glib.so
* /usr/lib/libupower-glib.so.3
* /usr/lib/libupower-glib.so.3.1.0
* /usr/lib/pkgconfig/upower-glib.pc
* /usr/lib/systemd/system/upower.service
* /usr/lib/udev/hwdb.d/95-upower-hid.hwdb
* /usr/lib/udev/rules.d/95-upower-hid.rules
* /usr/lib/udev/rules.d/95-upower-wup.rules
* /usr/lib/upower/upower/integration-test.py
* /usr/lib/upower/upower/output_checker.py
* /usr/lib/upower/upower/tests/logitech-g903.device
* /usr/lib/upower/upower/tests/steelseries-headset.device
* /usr/lib/upower/upower/tests/usb-headset.device
* /usr/lib/upower/upower/tests/wacom-bluetooth-active.device
* /usr/lib/upower/upower/tests/wacom-dongle-active.device
* /usr/lib/upower/upower/tests/wacom-dongle-waiting.device
* /usr/lib/upower/upower/tests/wacom-pen-digitiser.device
* /usr/lib/upower/upowerd
* /usr/share/dbus-1/interfaces/org.freedesktop.UPower.Device.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.UPower.KbdBacklight.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.UPower.xml
* /usr/share/dbus-1/system-services/org.freedesktop.UPower.service
* /usr/share/dbus-1/system.d/org.freedesktop.UPower.conf
* /usr/share/doc/upower-1.90.2/AUTHORS
* /usr/share/doc/upower-1.90.2/COPYING
* /usr/share/doc/upower-1.90.2/HACKING
* /usr/share/doc/upower-1.90.2/NEWS
* /usr/share/doc/upower-1.90.2/README
* /usr/share/doc/upower-1.90.2/RELEASE
* /usr/share/gir-1.0/UPowerGlib-1.0.gir
* /usr/share/gtk-doc/html/UPower/annotation-glossary.html
* /usr/share/gtk-doc/html/UPower/Device.html
* /usr/share/gtk-doc/html/UPower/home.png
* /usr/share/gtk-doc/html/UPower/index.html
* /usr/share/gtk-doc/html/UPower/ix01.html
* /usr/share/gtk-doc/html/UPower/KbdBacklight.html
* /usr/share/gtk-doc/html/UPower/left-insensitive.png
* /usr/share/gtk-doc/html/UPower/left.png
* /usr/share/gtk-doc/html/UPower/libupower-glib-helpers.html
* /usr/share/gtk-doc/html/UPower/libupower-glib.html
* /usr/share/gtk-doc/html/UPower/license.html
* /usr/share/gtk-doc/html/UPower/ref-dbus.html
* /usr/share/gtk-doc/html/UPower/right-insensitive.png
* /usr/share/gtk-doc/html/UPower/right.png
* /usr/share/gtk-doc/html/UPower/style.css
* /usr/share/gtk-doc/html/UPower/tools-fileformats.html
* /usr/share/gtk-doc/html/UPower/up-insensitive.png
* /usr/share/gtk-doc/html/UPower/up.png
* /usr/share/gtk-doc/html/UPower/UpClient.html
* /usr/share/gtk-doc/html/UPower/UpDevice.html
* /usr/share/gtk-doc/html/UPower/UpHistoryItem.html
* /usr/share/gtk-doc/html/UPower/UPower-up-types.html
* /usr/share/gtk-doc/html/UPower/upower.1.html
* /usr/share/gtk-doc/html/UPower/UPower.7.html
* /usr/share/gtk-doc/html/UPower/UPower.html
* /usr/share/gtk-doc/html/UPower/upowerd.8.html
* /usr/share/gtk-doc/html/UPower/UpStatsItem.html
* /usr/share/installed-tests/upower/upower-integration.test
* /usr/share/locale/fr/LC_MESSAGES/upower.mo
* /usr/share/locale/it/LC_MESSAGES/upower.mo
* /usr/share/locale/pl/LC_MESSAGES/upower.mo
* /usr/share/locale/sv/LC_MESSAGES/upower.mo
* /usr/share/man/man1/upower.1.gz
* /usr/share/man/man7/UPower.7.gz
* /usr/share/man/man8/upowerd.8.gz
{{< /files >}}