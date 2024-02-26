+++
draft = false
title = "gconf 3.2.6-9"
version = "3.2.6-9"
description = "A configuration database system for GNOME"
date = "2022-07-25T18:41:03"
aliases = "/packages/3020"
categories = ['compat-extra']
upstreamurl = "http://www.gnome.org/"
arch = "x86_64"
size = "1173340"
usize = "9121582"
sha1sum = "4e1c30f47b15b2db29f8a8d7bbafb535532db543"
depends = "['dbus-glib>=0.104-3', 'libffi>=3.2.1', 'polkit>=0.113-5']"
reverse_depends = "['cpod']"
+++
### Description: 
A configuration database system for GNOME

### Files: 
* /etc/dbus-1/system.d/org.gnome.GConf.Defaults.conf
* /etc/gconf/2/evoldap.conf
* /etc/gconf/2/path
* /etc/xdg/autostart/gsettings-data-convert.desktop
* /usr/bin/gconf-merge-tree
* /usr/bin/gconftool-2
* /usr/bin/gsettings-data-convert
* /usr/bin/gsettings-schema-convert
* /usr/include/gconf/2/gconf/gconf-changeset.h
* /usr/include/gconf/2/gconf/gconf-client.h
* /usr/include/gconf/2/gconf/gconf-engine.h
* /usr/include/gconf/2/gconf/gconf-enum-types.h
* /usr/include/gconf/2/gconf/gconf-error.h
* /usr/include/gconf/2/gconf/gconf-listeners.h
* /usr/include/gconf/2/gconf/gconf-schema.h
* /usr/include/gconf/2/gconf/gconf-value.h
* /usr/include/gconf/2/gconf/gconf.h
* /usr/lib/GConf/2/libgconfbackend-evoldap.so
* /usr/lib/GConf/2/libgconfbackend-oldxml.so
* /usr/lib/GConf/2/libgconfbackend-xml.so
* /usr/lib/gconf/gconf-defaults-mechanism
* /usr/lib/gconf/gconfd-2
* /usr/lib/gio/modules/libgsettingsgconfbackend.so
* /usr/lib/girepository-1.0/GConf-2.0.typelib
* /usr/lib/libgconf-2.so
* /usr/lib/libgconf-2.so.4
* /usr/lib/libgconf-2.so.4.1.5
* /usr/lib/pkgconfig/gconf-2.0.pc
* /usr/share/aclocal/gconf-2.m4
* /usr/share/dbus-1/services/org.gnome.GConf.service
* /usr/share/dbus-1/system-services/org.gnome.GConf.Defaults.service
* /usr/share/doc/gconf-3.2.6/AUTHORS
* /usr/share/doc/gconf-3.2.6/ChangeLog
* /usr/share/doc/gconf-3.2.6/COPYING
* /usr/share/doc/gconf-3.2.6/INSTALL
* /usr/share/doc/gconf-3.2.6/NEWS
* /usr/share/doc/gconf-3.2.6/README
* /usr/share/doc/gconf-3.2.6/TODO
* /usr/share/GConf/schema/evoldap.schema
* /usr/share/gir-1.0/GConf-2.0.gir
* /usr/share/gtk-doc/html/gconf/ch01.html
* /usr/share/gtk-doc/html/gconf/gconf-gconf-backend.html
* /usr/share/gtk-doc/html/gconf/gconf-gconf-changeset.html
* /usr/share/gtk-doc/html/gconf/gconf-gconf-client.html
* /usr/share/gtk-doc/html/gconf/gconf-gconf-engine.html
* /usr/share/gtk-doc/html/gconf/gconf-gconf-error.html
* /usr/share/gtk-doc/html/gconf/gconf-gconf-internals.html
* /usr/share/gtk-doc/html/gconf/gconf-gconf-listeners.html
* /usr/share/gtk-doc/html/gconf/gconf-gconf-locale.html
* /usr/share/gtk-doc/html/gconf/gconf-gconf-schema.html
* /usr/share/gtk-doc/html/gconf/gconf-gconf-sources.html
* /usr/share/gtk-doc/html/gconf/gconf-gconf-value.html
* /usr/share/gtk-doc/html/gconf/gconf-gconf.html
* /usr/share/gtk-doc/html/gconf/gconf.devhelp2
* /usr/share/gtk-doc/html/gconf/home.png
* /usr/share/gtk-doc/html/gconf/index.html
* /usr/share/gtk-doc/html/gconf/index.sgml
* /usr/share/gtk-doc/html/gconf/left.png
* /usr/share/gtk-doc/html/gconf/right.png
* /usr/share/gtk-doc/html/gconf/style.css
* /usr/share/gtk-doc/html/gconf/up.png
* /usr/share/locale/am/LC_MESSAGES/GConf2.mo
* /usr/share/locale/ar/LC_MESSAGES/GConf2.mo
* /usr/share/locale/as/LC_MESSAGES/GConf2.mo
* /usr/share/locale/ast/LC_MESSAGES/GConf2.mo
* /usr/share/locale/az/LC_MESSAGES/GConf2.mo
* /usr/share/locale/be/LC_MESSAGES/GConf2.mo
* /usr/share/locale/bg/LC_MESSAGES/GConf2.mo
* /usr/share/locale/bn/LC_MESSAGES/GConf2.mo
* /usr/share/locale/bn_IN/LC_MESSAGES/GConf2.mo
* /usr/share/locale/bs/LC_MESSAGES/GConf2.mo
* /usr/share/locale/ca/LC_MESSAGES/GConf2.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/GConf2.mo
* /usr/share/locale/cs/LC_MESSAGES/GConf2.mo
* /usr/share/locale/cy/LC_MESSAGES/GConf2.mo
* /usr/share/locale/da/LC_MESSAGES/GConf2.mo
* /usr/share/locale/de/LC_MESSAGES/GConf2.mo
* /usr/share/locale/dz/LC_MESSAGES/GConf2.mo
* /usr/share/locale/el/LC_MESSAGES/GConf2.mo
* /usr/share/locale/en@shaw/LC_MESSAGES/GConf2.mo
* /usr/share/locale/en_CA/LC_MESSAGES/GConf2.mo
* /usr/share/locale/en_GB/LC_MESSAGES/GConf2.mo
* /usr/share/locale/eo/LC_MESSAGES/GConf2.mo
* /usr/share/locale/es/LC_MESSAGES/GConf2.mo
* /usr/share/locale/et/LC_MESSAGES/GConf2.mo
* /usr/share/locale/eu/LC_MESSAGES/GConf2.mo
* /usr/share/locale/fa/LC_MESSAGES/GConf2.mo
* /usr/share/locale/fi/LC_MESSAGES/GConf2.mo
* /usr/share/locale/fr/LC_MESSAGES/GConf2.mo
* /usr/share/locale/ga/LC_MESSAGES/GConf2.mo
* /usr/share/locale/gl/LC_MESSAGES/GConf2.mo
* /usr/share/locale/gu/LC_MESSAGES/GConf2.mo
* /usr/share/locale/he/LC_MESSAGES/GConf2.mo
* /usr/share/locale/hi/LC_MESSAGES/GConf2.mo
* /usr/share/locale/hr/LC_MESSAGES/GConf2.mo
* /usr/share/locale/hu/LC_MESSAGES/GConf2.mo
* /usr/share/locale/hy/LC_MESSAGES/GConf2.mo
* /usr/share/locale/id/LC_MESSAGES/GConf2.mo
* /usr/share/locale/is/LC_MESSAGES/GConf2.mo
* /usr/share/locale/it/LC_MESSAGES/GConf2.mo
* /usr/share/locale/ja/LC_MESSAGES/GConf2.mo
* /usr/share/locale/ka/LC_MESSAGES/GConf2.mo
* /usr/share/locale/km/LC_MESSAGES/GConf2.mo
* /usr/share/locale/kn/LC_MESSAGES/GConf2.mo
* /usr/share/locale/ko/LC_MESSAGES/GConf2.mo
* /usr/share/locale/ku/LC_MESSAGES/GConf2.mo
* /usr/share/locale/lt/LC_MESSAGES/GConf2.mo
* /usr/share/locale/lv/LC_MESSAGES/GConf2.mo
* /usr/share/locale/mai/LC_MESSAGES/GConf2.mo
* /usr/share/locale/mg/LC_MESSAGES/GConf2.mo
* /usr/share/locale/mk/LC_MESSAGES/GConf2.mo
* /usr/share/locale/ml/LC_MESSAGES/GConf2.mo
* /usr/share/locale/mn/LC_MESSAGES/GConf2.mo
* /usr/share/locale/mr/LC_MESSAGES/GConf2.mo
* /usr/share/locale/ms/LC_MESSAGES/GConf2.mo
* /usr/share/locale/nb/LC_MESSAGES/GConf2.mo
* /usr/share/locale/ne/LC_MESSAGES/GConf2.mo
* /usr/share/locale/nl/LC_MESSAGES/GConf2.mo
* /usr/share/locale/nn/LC_MESSAGES/GConf2.mo
* /usr/share/locale/oc/LC_MESSAGES/GConf2.mo
* /usr/share/locale/or/LC_MESSAGES/GConf2.mo
* /usr/share/locale/pa/LC_MESSAGES/GConf2.mo
* /usr/share/locale/pl/LC_MESSAGES/GConf2.mo
* /usr/share/locale/pt/LC_MESSAGES/GConf2.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/GConf2.mo
* /usr/share/locale/ro/LC_MESSAGES/GConf2.mo
* /usr/share/locale/ru/LC_MESSAGES/GConf2.mo
* /usr/share/locale/rw/LC_MESSAGES/GConf2.mo
* /usr/share/locale/si/LC_MESSAGES/GConf2.mo
* /usr/share/locale/sk/LC_MESSAGES/GConf2.mo
* /usr/share/locale/sl/LC_MESSAGES/GConf2.mo
* /usr/share/locale/sq/LC_MESSAGES/GConf2.mo
* /usr/share/locale/sr/LC_MESSAGES/GConf2.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/GConf2.mo
* /usr/share/locale/sv/LC_MESSAGES/GConf2.mo
* /usr/share/locale/ta/LC_MESSAGES/GConf2.mo
* /usr/share/locale/te/LC_MESSAGES/GConf2.mo
* /usr/share/locale/th/LC_MESSAGES/GConf2.mo
* /usr/share/locale/tr/LC_MESSAGES/GConf2.mo
* /usr/share/locale/ug/LC_MESSAGES/GConf2.mo
* /usr/share/locale/uk/LC_MESSAGES/GConf2.mo
* /usr/share/locale/vi/LC_MESSAGES/GConf2.mo
* /usr/share/locale/xh/LC_MESSAGES/GConf2.mo
* /usr/share/locale/yi/LC_MESSAGES/GConf2.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/GConf2.mo
* /usr/share/locale/zh_HK/LC_MESSAGES/GConf2.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/GConf2.mo
* /usr/share/man/man1/gconftool-2.1.gz
* /usr/share/man/man1/gsettings-data-convert.1.gz
* /usr/share/man/man1/gsettings-schema-convert.1.gz
* /usr/share/polkit-1/actions/org.gnome.gconf.defaults.policy
* /usr/share/sgml/gconf/gconf-1.0.dtd
