+++
draft = false
title = "gnome-keyring 42.1-2"
version = "42.1-2"
description = "Password and keyring managing daemon for GNOME"
date = "2024-01-06T14:52:33"
aliases = "/packages/220428"
categories = ['gnome']
upstreamurl = "http://www.gnome.org/"
arch = "x86_64"
size = "944020"
usize = "5038474"
sha1sum = "e4315e436f936ab6f2a474a62b896301b287266e"
depends = "['gcr>=4.0.0', 'gcr-1', 'openssh']"
+++
Password and keyring managing daemon for GNOME"

{{< files text="show files" >}}* /etc/xdg/autostart/gnome-keyring-pkcs11.desktop
* /etc/xdg/autostart/gnome-keyring-secrets.desktop
* /etc/xdg/autostart/gnome-keyring-ssh.desktop
* /usr/bin/gnome-keyring
* /usr/bin/gnome-keyring-3
* /usr/bin/gnome-keyring-daemon
* /usr/lib/gnome-keyring/devel/gkm-gnome2-store-standalone.so
* /usr/lib/gnome-keyring/devel/gkm-secret-store-standalone.so
* /usr/lib/gnome-keyring/devel/gkm-ssh-store-standalone.so
* /usr/lib/gnome-keyring/devel/gkm-xdg-store-standalone.so
* /usr/lib/pkcs11/gnome-keyring-pkcs11.so
* /usr/lib/security/pam_gnome_keyring.so
* /usr/share/dbus-1/services/org.freedesktop.impl.portal.Secret.service
* /usr/share/dbus-1/services/org.freedesktop.secrets.service
* /usr/share/dbus-1/services/org.gnome.keyring.service
* /usr/share/doc/gnome-keyring-42.1/AUTHORS
* /usr/share/doc/gnome-keyring-42.1/ChangeLog
* /usr/share/doc/gnome-keyring-42.1/COPYING
* /usr/share/doc/gnome-keyring-42.1/COPYING.LIB
* /usr/share/doc/gnome-keyring-42.1/HACKING
* /usr/share/doc/gnome-keyring-42.1/INSTALL
* /usr/share/doc/gnome-keyring-42.1/NEWS
* /usr/share/doc/gnome-keyring-42.1/README
* /usr/share/GConf/gsettings/org.gnome.crypto.cache.convert
* /usr/share/glib-2.0/schemas/org.gnome.crypto.cache.gschema.xml
* /usr/share/locale/af/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/ar/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/as/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/ast/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/az/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/be/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/be@latin/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/bg/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/bn/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/bn_IN/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/bs/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/ca/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/ckb/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/cs/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/cy/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/da/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/de/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/dz/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/el/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/en@shaw/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/en_CA/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/en_GB/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/eo/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/es/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/et/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/eu/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/fa/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/fi/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/fr/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/fur/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/ga/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/gd/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/gl/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/gu/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/he/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/hi/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/hr/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/hu/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/id/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/is/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/it/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/ja/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/ka/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/kk/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/km/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/kn/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/ko/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/lt/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/lv/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/mai/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/mg/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/mjw/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/mk/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/ml/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/mn/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/mr/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/ms/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/nb/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/ne/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/nl/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/nn/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/oc/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/or/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/pa/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/pl/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/pt/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/ro/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/ru/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/rw/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/si/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/sk/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/sl/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/sq/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/sr/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/sv/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/ta/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/te/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/tg/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/th/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/tr/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/ug/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/uk/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/vi/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/xh/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/zh_HK/LC_MESSAGES/gnome-keyring.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/gnome-keyring.mo
* /usr/share/man/man1/gnome-keyring-3.1.gz
* /usr/share/man/man1/gnome-keyring-daemon.1.gz
* /usr/share/man/man1/gnome-keyring.1.gz
* /usr/share/p11-kit/modules/gnome-keyring.module
* /usr/share/xdg-desktop-portal/portals/gnome-keyring.portal
{{< /files >}}