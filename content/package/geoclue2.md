+++
draft = false
title = "geoclue2 2.7.1-3"
version = "2.7.1-3"
description = "A D-Bus service that provides location information"
date = "2024-01-30T11:51:04"
aliases = "/packages/200119"
categories = ['xlib']
upstreamurl = "https://gitlab.freedesktop.org/geoclue/geoclue/-/wikis/home"
arch = "x86_64"
size = "209760"
usize = "1630069"
sha1sum = "4c19b682199dcfe34af7b9edc3e864e0bc7823f7"
depends = "['avahi>=0.6.31-9', 'avahi-glib>=0.6.31-9', 'json-glib>=1.4.2-3', 'libnotify', 'libsoup3', 'modemmanager>=1.6.2']"
reverse_depends = "['clight', 'xdg-desktop-portal']"
+++
### Description: 
A D-Bus service that provides location information

### Files: 
* /etc/geoclue/geoclue.conf
* /etc/xdg/autostart/geoclue-demo-agent.desktop
* /usr/include/libgeoclue-2.0/gclue-client.h
* /usr/include/libgeoclue-2.0/gclue-enum-types.h
* /usr/include/libgeoclue-2.0/gclue-enums.h
* /usr/include/libgeoclue-2.0/gclue-helpers.h
* /usr/include/libgeoclue-2.0/gclue-location.h
* /usr/include/libgeoclue-2.0/gclue-manager.h
* /usr/include/libgeoclue-2.0/gclue-simple.h
* /usr/include/libgeoclue-2.0/geoclue.h
* /usr/lib/geoclue2/geoclue
* /usr/lib/geoclue2/geoclue-2.0/demos/agent
* /usr/lib/geoclue2/geoclue-2.0/demos/where-am-i
* /usr/lib/girepository-1.0/Geoclue-2.0.typelib
* /usr/lib/libgeoclue-2.so
* /usr/lib/libgeoclue-2.so.0
* /usr/lib/libgeoclue-2.so.0.0.0
* /usr/lib/pkgconfig/geoclue-2.0.pc
* /usr/lib/pkgconfig/libgeoclue-2.0.pc
* /usr/lib/systemd/system/geoclue.service
* /usr/lib/sysusers.d/geoclue.conf
* /usr/lib/tmpfiles.de/geoclue.conf
* /usr/share/applications/geoclue-demo-agent.desktop
* /usr/share/applications/geoclue-where-am-i.desktop
* /usr/share/dbus-1/interfaces/org.freedesktop.GeoClue2.Agent.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.GeoClue2.Client.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.GeoClue2.Location.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.GeoClue2.Manager.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.GeoClue2.xml
* /usr/share/dbus-1/system-services/org.freedesktop.GeoClue2.service
* /usr/share/dbus-1/system.d/org.freedesktop.GeoClue2.Agent.conf
* /usr/share/dbus-1/system.d/org.freedesktop.GeoClue2.conf
* /usr/share/doc/geoclue2-2.7.1/COPYING
* /usr/share/doc/geoclue2-2.7.1/COPYING.LIB
* /usr/share/doc/geoclue2-2.7.1/NEWS
* /usr/share/doc/geoclue2-2.7.1/README.md
* /usr/share/gir-1.0/Geoclue-2.0.gir
* /usr/share/gtk-doc/html/geoclue/gdbus-org.freedesktop.GeoClue2.Agent.html
* /usr/share/gtk-doc/html/geoclue/gdbus-org.freedesktop.GeoClue2.Client.html
* /usr/share/gtk-doc/html/geoclue/gdbus-org.freedesktop.GeoClue2.Location.html
* /usr/share/gtk-doc/html/geoclue/gdbus-org.freedesktop.GeoClue2.Manager.html
* /usr/share/gtk-doc/html/geoclue/geoclue-gclue-enums.html
* /usr/share/gtk-doc/html/geoclue/home.png
* /usr/share/gtk-doc/html/geoclue/index.html
* /usr/share/gtk-doc/html/geoclue/ix01.html
* /usr/share/gtk-doc/html/geoclue/left-insensitive.png
* /usr/share/gtk-doc/html/geoclue/left.png
* /usr/share/gtk-doc/html/geoclue/license.html
* /usr/share/gtk-doc/html/geoclue/ref-agent-dbus.html
* /usr/share/gtk-doc/html/geoclue/ref-dbus.html
* /usr/share/gtk-doc/html/geoclue/right-insensitive.png
* /usr/share/gtk-doc/html/geoclue/right.png
* /usr/share/gtk-doc/html/geoclue/style.css
* /usr/share/gtk-doc/html/geoclue/up-insensitive.png
* /usr/share/gtk-doc/html/geoclue/up.png
* /usr/share/gtk-doc/html/libgeoclue/annotation-glossary.html
* /usr/share/gtk-doc/html/libgeoclue/ch01.html
* /usr/share/gtk-doc/html/libgeoclue/ch02.html
* /usr/share/gtk-doc/html/libgeoclue/ch03.html
* /usr/share/gtk-doc/html/libgeoclue/ch04.html
* /usr/share/gtk-doc/html/libgeoclue/ch05.html
* /usr/share/gtk-doc/html/libgeoclue/GClueClient.html
* /usr/share/gtk-doc/html/libgeoclue/GClueClientProxy.html
* /usr/share/gtk-doc/html/libgeoclue/GClueLocation.html
* /usr/share/gtk-doc/html/libgeoclue/GClueLocationProxy.html
* /usr/share/gtk-doc/html/libgeoclue/GClueManager.html
* /usr/share/gtk-doc/html/libgeoclue/GClueManagerProxy.html
* /usr/share/gtk-doc/html/libgeoclue/GClueSimple.html
* /usr/share/gtk-doc/html/libgeoclue/home.png
* /usr/share/gtk-doc/html/libgeoclue/index.html
* /usr/share/gtk-doc/html/libgeoclue/ix01.html
* /usr/share/gtk-doc/html/libgeoclue/left-insensitive.png
* /usr/share/gtk-doc/html/libgeoclue/left.png
* /usr/share/gtk-doc/html/libgeoclue/libgeoclue-gclue-enums.html
* /usr/share/gtk-doc/html/libgeoclue/license.html
* /usr/share/gtk-doc/html/libgeoclue/right-insensitive.png
* /usr/share/gtk-doc/html/libgeoclue/right.png
* /usr/share/gtk-doc/html/libgeoclue/style.css
* /usr/share/gtk-doc/html/libgeoclue/up-insensitive.png
* /usr/share/gtk-doc/html/libgeoclue/up.png
* /usr/share/man/man5/geoclue.5.gz
* /usr/share/polkit-1/rules.d/org.freedesktop.GeoClue2.rules
* /usr/share/vala/vapi/libgeoclue-2.0.deps
* /usr/share/vala/vapi/libgeoclue-2.0.vapi
