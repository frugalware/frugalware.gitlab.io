+++
draft = false
title = "nm-openconnect 1.2.8-1"
version = "1.2.8-1"
date = "2023-03-13T15:52:15"
categories = ['gnome-extra']
upstreamurl = "http://www.gnome.org/"
arch = "x86_64"
size = "506876"
usize = "3082273"
sha1sum = "90783ecfe7d31b5b763470584b9480181b8a859e"
depends = "['nm-connection-editor>=1.1.92', 'libsecret>=0.18.5', 'openconnect', 'gcr-1']"
files = "['etc/', 'etc/dbus-1/', 'etc/dbus-1/system.d/', 'etc/dbus-1/system.d/nm-openconnect-service.conf', 'usr/', 'usr/lib/', 'usr/lib/NetworkManager/', 'usr/lib/NetworkManager/VPN/', 'usr/lib/NetworkManager/VPN/nm-openconnect-service.name', 'usr/lib/NetworkManager/libnm-vpn-plugin-openconnect-editor.so', 'usr/lib/NetworkManager/libnm-vpn-plugin-openconnect.so', 'usr/lib/nm-openconnect/', 'usr/lib/nm-openconnect/nm-openconnect-auth-dialog', 'usr/lib/nm-openconnect/nm-openconnect-service', 'usr/lib/nm-openconnect/nm-openconnect-service-openconnect-helper', 'usr/share/', 'usr/share/appdata/', 'usr/share/appdata/network-manager-openconnect.metainfo.xml', 'usr/share/doc/', 'usr/share/doc/nm-openconnect-1.2.8/', 'usr/share/doc/nm-openconnect-1.2.8/AUTHORS', 'usr/share/doc/nm-openconnect-1.2.8/COPYING', 'usr/share/doc/nm-openconnect-1.2.8/ChangeLog', 'usr/share/doc/nm-openconnect-1.2.8/INSTALL', 'usr/share/doc/nm-openconnect-1.2.8/NEWS', 'usr/share/doc/nm-openconnect-1.2.8/README', 'usr/share/locale/', 'usr/share/locale/ar/', 'usr/share/locale/ar/LC_MESSAGES/', 'usr/share/locale/ar/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/as/', 'usr/share/locale/as/LC_MESSAGES/', 'usr/share/locale/as/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/bg/', 'usr/share/locale/bg/LC_MESSAGES/', 'usr/share/locale/bg/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/bn_IN/', 'usr/share/locale/bn_IN/LC_MESSAGES/', 'usr/share/locale/bn_IN/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/bs/', 'usr/share/locale/bs/LC_MESSAGES/', 'usr/share/locale/bs/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/ca/', 'usr/share/locale/ca/LC_MESSAGES/', 'usr/share/locale/ca/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/ca@valencia/', 'usr/share/locale/ca@valencia/LC_MESSAGES/', 'usr/share/locale/ca@valencia/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/cs/', 'usr/share/locale/cs/LC_MESSAGES/', 'usr/share/locale/cs/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/da/', 'usr/share/locale/da/LC_MESSAGES/', 'usr/share/locale/da/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/de/', 'usr/share/locale/de/LC_MESSAGES/', 'usr/share/locale/de/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/el/', 'usr/share/locale/el/LC_MESSAGES/', 'usr/share/locale/el/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/en_GB/', 'usr/share/locale/en_GB/LC_MESSAGES/', 'usr/share/locale/en_GB/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/eo/', 'usr/share/locale/eo/LC_MESSAGES/', 'usr/share/locale/eo/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/es/', 'usr/share/locale/es/LC_MESSAGES/', 'usr/share/locale/es/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/et/', 'usr/share/locale/et/LC_MESSAGES/', 'usr/share/locale/et/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/eu/', 'usr/share/locale/eu/LC_MESSAGES/', 'usr/share/locale/eu/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/fa/', 'usr/share/locale/fa/LC_MESSAGES/', 'usr/share/locale/fa/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/fi/', 'usr/share/locale/fi/LC_MESSAGES/', 'usr/share/locale/fi/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/fr/', 'usr/share/locale/fr/LC_MESSAGES/', 'usr/share/locale/fr/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/gl/', 'usr/share/locale/gl/LC_MESSAGES/', 'usr/share/locale/gl/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/gu/', 'usr/share/locale/gu/LC_MESSAGES/', 'usr/share/locale/gu/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/he/', 'usr/share/locale/he/LC_MESSAGES/', 'usr/share/locale/he/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/hr/', 'usr/share/locale/hr/LC_MESSAGES/', 'usr/share/locale/hr/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/hu/', 'usr/share/locale/hu/LC_MESSAGES/', 'usr/share/locale/hu/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/id/', 'usr/share/locale/id/LC_MESSAGES/', 'usr/share/locale/id/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/it/', 'usr/share/locale/it/LC_MESSAGES/', 'usr/share/locale/it/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/kn/', 'usr/share/locale/kn/LC_MESSAGES/', 'usr/share/locale/kn/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/ko/', 'usr/share/locale/ko/LC_MESSAGES/', 'usr/share/locale/ko/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/lt/', 'usr/share/locale/lt/LC_MESSAGES/', 'usr/share/locale/lt/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/lv/', 'usr/share/locale/lv/LC_MESSAGES/', 'usr/share/locale/lv/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/mr/', 'usr/share/locale/mr/LC_MESSAGES/', 'usr/share/locale/mr/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/nb/', 'usr/share/locale/nb/LC_MESSAGES/', 'usr/share/locale/nb/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/nl/', 'usr/share/locale/nl/LC_MESSAGES/', 'usr/share/locale/nl/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/or/', 'usr/share/locale/or/LC_MESSAGES/', 'usr/share/locale/or/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/pa/', 'usr/share/locale/pa/LC_MESSAGES/', 'usr/share/locale/pa/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/pl/', 'usr/share/locale/pl/LC_MESSAGES/', 'usr/share/locale/pl/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/pt/', 'usr/share/locale/pt/LC_MESSAGES/', 'usr/share/locale/pt/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/pt_BR/', 'usr/share/locale/pt_BR/LC_MESSAGES/', 'usr/share/locale/pt_BR/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/ro/', 'usr/share/locale/ro/LC_MESSAGES/', 'usr/share/locale/ro/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/ru/', 'usr/share/locale/ru/LC_MESSAGES/', 'usr/share/locale/ru/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/sk/', 'usr/share/locale/sk/LC_MESSAGES/', 'usr/share/locale/sk/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/sl/', 'usr/share/locale/sl/LC_MESSAGES/', 'usr/share/locale/sl/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/sr/', 'usr/share/locale/sr/LC_MESSAGES/', 'usr/share/locale/sr/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/sr@latin/', 'usr/share/locale/sr@latin/LC_MESSAGES/', 'usr/share/locale/sr@latin/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/sv/', 'usr/share/locale/sv/LC_MESSAGES/', 'usr/share/locale/sv/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/ta/', 'usr/share/locale/ta/LC_MESSAGES/', 'usr/share/locale/ta/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/te/', 'usr/share/locale/te/LC_MESSAGES/', 'usr/share/locale/te/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/tg/', 'usr/share/locale/tg/LC_MESSAGES/', 'usr/share/locale/tg/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/tr/', 'usr/share/locale/tr/LC_MESSAGES/', 'usr/share/locale/tr/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/ug/', 'usr/share/locale/ug/LC_MESSAGES/', 'usr/share/locale/ug/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/uk/', 'usr/share/locale/uk/LC_MESSAGES/', 'usr/share/locale/uk/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/vi/', 'usr/share/locale/vi/LC_MESSAGES/', 'usr/share/locale/vi/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/zh_CN/', 'usr/share/locale/zh_CN/LC_MESSAGES/', 'usr/share/locale/zh_CN/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/zh_HK/', 'usr/share/locale/zh_HK/LC_MESSAGES/', 'usr/share/locale/zh_HK/LC_MESSAGES/NetworkManager-openconnect.mo', 'usr/share/locale/zh_TW/', 'usr/share/locale/zh_TW/LC_MESSAGES/', 'usr/share/locale/zh_TW/LC_MESSAGES/NetworkManager-openconnect.mo']"
+++
Open Cisco AnyConnect VPN plugin for Network Manager