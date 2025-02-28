+++
draft = false
title = "dbus 1.16.2-1"
version = "1.16.2-1"
description = "A message bus system"
date = "2025-02-28T09:23:28"
aliases = "/packages/2961"
categories = ['base']
upstreamurl = "http://freedesktop.org/wiki/Software/dbus"
arch = "x86_64"
size = "499096"
usize = "1625218"
sha1sum = "910d69b0ffeeb788be5ff7af4b410eb928f75d25"
depends = "['expat>=2.1.0-5', 'libsystemd>=242', 'scriptlet-core']"
reverse_depends = "['at-spi2-core', 'avahi', 'bluez', 'cef', 'cups', 'dbus-c++', 'dbus-glib', 'dbus-x11', 'dnsmasq', 'efl', 'enlightenment', 'gvfs', 'hexchat', 'inkscape', 'jack2', 'kdbus', 'kitty', 'libatspi', 'libnvme', 'libpcap', 'libproxy', 'libpulse', 'libvlc', 'lumina-desktop', 'mp3splt-gtk', 'pulseaudio', 'pulseaudio-bluetooth', 'qt5-base', 'rtkit', 'systemd', 'terminology', 'threema-desktop', 'whalebird', 'wireshark', 'wpa_supplicant', 'xorg-server']"
+++
### Description: 
A message bus system

### Files: 
* /etc/dbus-1/session.conf
* /etc/dbus-1/system.conf
* /usr/bin/dbus-cleanup-sockets
* /usr/bin/dbus-daemon
* /usr/bin/dbus-monitor
* /usr/bin/dbus-run-session
* /usr/bin/dbus-send
* /usr/bin/dbus-test-tool
* /usr/bin/dbus-update-activation-environment
* /usr/bin/dbus-uuidgen
* /usr/include/dbus-1.0/dbus/dbus-address.h
* /usr/include/dbus-1.0/dbus/dbus-arch-deps.h
* /usr/include/dbus-1.0/dbus/dbus-bus.h
* /usr/include/dbus-1.0/dbus/dbus-connection.h
* /usr/include/dbus-1.0/dbus/dbus-errors.h
* /usr/include/dbus-1.0/dbus/dbus-macros.h
* /usr/include/dbus-1.0/dbus/dbus-memory.h
* /usr/include/dbus-1.0/dbus/dbus-message.h
* /usr/include/dbus-1.0/dbus/dbus-misc.h
* /usr/include/dbus-1.0/dbus/dbus-pending-call.h
* /usr/include/dbus-1.0/dbus/dbus-protocol.h
* /usr/include/dbus-1.0/dbus/dbus-server.h
* /usr/include/dbus-1.0/dbus/dbus-shared.h
* /usr/include/dbus-1.0/dbus/dbus-signature.h
* /usr/include/dbus-1.0/dbus/dbus-syntax.h
* /usr/include/dbus-1.0/dbus/dbus-threads.h
* /usr/include/dbus-1.0/dbus/dbus-types.h
* /usr/include/dbus-1.0/dbus/dbus.h
* /usr/lib/cmake/DBus1/DBus1Config.cmake
* /usr/lib/cmake/DBus1/DBus1ConfigVersion.cmake
* /usr/lib/dbus-1.0/include/dbus/dbus-arch-deps.h
* /usr/lib/dbus/dbus-daemon-launch-helper
* /usr/lib/libdbus-1.so
* /usr/lib/libdbus-1.so.3
* /usr/lib/libdbus-1.so.3.38.3
* /usr/lib/pkgconfig/dbus-1.pc
* /usr/lib/systemd/system/dbus.service
* /usr/lib/systemd/system/dbus.socket
* /usr/lib/systemd/system/multi-user.target.wants/dbus.service
* /usr/lib/systemd/system/sockets.target.wants/dbus.socket
* /usr/lib/systemd/user/dbus.service
* /usr/lib/systemd/user/dbus.socket
* /usr/lib/systemd/user/sockets.target.wants/dbus.socket
* /usr/lib/sysusers.d/dbus.conf
* /usr/lib/tmpfiles.d/dbus.conf
* /usr/share/dbus-1/session.conf
* /usr/share/dbus-1/system.conf
* /usr/share/doc/dbus-1.16.2/AUTHORS
* /usr/share/doc/dbus-1.16.2/COPYING
* /usr/share/doc/dbus-1.16.2/INSTALL
* /usr/share/doc/dbus-1.16.2/NEWS
* /usr/share/doc/dbus-1.16.2/README
* /usr/share/doc/dbus-1.16.2/README.cmake
* /usr/share/doc/dbus-1.16.2/README.cygwin
* /usr/share/doc/dbus-1.16.2/README.launchd
* /usr/share/doc/dbus-1.16.2/README.valgrind
* /usr/share/doc/dbus-1.16.2/README.win
* /usr/share/doc/dbus-1.16.2/README.wince
* /usr/share/doc/dbus/dbus-cleanup-sockets.1.html
* /usr/share/doc/dbus/dbus-daemon.1.html
* /usr/share/doc/dbus/dbus-faq.html
* /usr/share/doc/dbus/dbus-launch.1.html
* /usr/share/doc/dbus/dbus-monitor.1.html
* /usr/share/doc/dbus/dbus-run-session.1.html
* /usr/share/doc/dbus/dbus-send.1.html
* /usr/share/doc/dbus/dbus-specification.html
* /usr/share/doc/dbus/dbus-test-plan.html
* /usr/share/doc/dbus/dbus-test-tool.1.html
* /usr/share/doc/dbus/dbus-tutorial.html
* /usr/share/doc/dbus/dbus-update-activation-environment.1.html
* /usr/share/doc/dbus/dbus-uuidgen.1.html
* /usr/share/doc/dbus/diagram.png
* /usr/share/doc/dbus/diagram.svg
* /usr/share/doc/dbus/examples/example-session-disable-stats.conf
* /usr/share/doc/dbus/examples/example-system-enable-stats.conf
* /usr/share/doc/dbus/examples/example-system-hardening-without-traditional-activation.conf
* /usr/share/doc/dbus/examples/GetAllMatchRules.py
* /usr/share/doc/dbus/index.html
* /usr/share/doc/dbus/system-activation.txt
* /usr/share/man/man1/dbus-cleanup-sockets.1.gz
* /usr/share/man/man1/dbus-daemon.1.gz
* /usr/share/man/man1/dbus-launch.1.gz
* /usr/share/man/man1/dbus-monitor.1.gz
* /usr/share/man/man1/dbus-run-session.1.gz
* /usr/share/man/man1/dbus-send.1.gz
* /usr/share/man/man1/dbus-test-tool.1.gz
* /usr/share/man/man1/dbus-update-activation-environment.1.gz
* /usr/share/man/man1/dbus-uuidgen.1.gz
* /usr/share/xml/dbus-1/busconfig.dtd
* /usr/share/xml/dbus-1/catalog.xml
* /usr/share/xml/dbus-1/introspect.dtd
