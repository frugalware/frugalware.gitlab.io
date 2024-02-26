+++
draft = false
title = "libsoup 2.74.3-1"
version = "2.74.3-1"
description = "An HTTP library implementation in C"
date = "2022-10-16T13:11:09"
aliases = "/packages/3198"
categories = ['lib']
upstreamurl = "http://www.gnome.org/"
arch = "x86_64"
size = "480308"
usize = "2970370"
sha1sum = "493631b8d9019aed583f41c4e9b1644b39085dc0"
depends = "['glib-networking>=2.60.0', 'glib2>=2.60.0', 'libffi>=3.2.1-2', 'libkrb5', 'libpsl', 'libxml2>=2.9.4-3', 'sqlite3>=3.9.2-4', 'zlib>=1.2.12']"
reverse_depends = "['gst1-plugins-good-libsoup', 'inkscape', 'strongswan', 'telepathy-gabble', 'telepathy-salut', 'tootle']"
+++
An HTTP library implementation in C"

{{< files text="show files" >}}* /usr/include/libsoup-2.4/libsoup/soup-address.h
* /usr/include/libsoup-2.4/libsoup/soup-auth-domain-basic.h
* /usr/include/libsoup-2.4/libsoup/soup-auth-domain-digest.h
* /usr/include/libsoup-2.4/libsoup/soup-auth-domain.h
* /usr/include/libsoup-2.4/libsoup/soup-auth-manager.h
* /usr/include/libsoup-2.4/libsoup/soup-auth.h
* /usr/include/libsoup-2.4/libsoup/soup-autocleanups.h
* /usr/include/libsoup-2.4/libsoup/soup-cache.h
* /usr/include/libsoup-2.4/libsoup/soup-content-decoder.h
* /usr/include/libsoup-2.4/libsoup/soup-content-sniffer.h
* /usr/include/libsoup-2.4/libsoup/soup-cookie-jar-db.h
* /usr/include/libsoup-2.4/libsoup/soup-cookie-jar-text.h
* /usr/include/libsoup-2.4/libsoup/soup-cookie-jar.h
* /usr/include/libsoup-2.4/libsoup/soup-cookie.h
* /usr/include/libsoup-2.4/libsoup/soup-date.h
* /usr/include/libsoup-2.4/libsoup/soup-enum-types.h
* /usr/include/libsoup-2.4/libsoup/soup-form.h
* /usr/include/libsoup-2.4/libsoup/soup-headers.h
* /usr/include/libsoup-2.4/libsoup/soup-hsts-enforcer-db.h
* /usr/include/libsoup-2.4/libsoup/soup-hsts-enforcer.h
* /usr/include/libsoup-2.4/libsoup/soup-hsts-policy.h
* /usr/include/libsoup-2.4/libsoup/soup-logger.h
* /usr/include/libsoup-2.4/libsoup/soup-message-body.h
* /usr/include/libsoup-2.4/libsoup/soup-message-headers.h
* /usr/include/libsoup-2.4/libsoup/soup-message.h
* /usr/include/libsoup-2.4/libsoup/soup-method.h
* /usr/include/libsoup-2.4/libsoup/soup-misc.h
* /usr/include/libsoup-2.4/libsoup/soup-multipart-input-stream.h
* /usr/include/libsoup-2.4/libsoup/soup-multipart.h
* /usr/include/libsoup-2.4/libsoup/soup-password-manager.h
* /usr/include/libsoup-2.4/libsoup/soup-portability.h
* /usr/include/libsoup-2.4/libsoup/soup-proxy-resolver-default.h
* /usr/include/libsoup-2.4/libsoup/soup-proxy-resolver.h
* /usr/include/libsoup-2.4/libsoup/soup-proxy-uri-resolver.h
* /usr/include/libsoup-2.4/libsoup/soup-request-data.h
* /usr/include/libsoup-2.4/libsoup/soup-request-file.h
* /usr/include/libsoup-2.4/libsoup/soup-request-http.h
* /usr/include/libsoup-2.4/libsoup/soup-request.h
* /usr/include/libsoup-2.4/libsoup/soup-requester.h
* /usr/include/libsoup-2.4/libsoup/soup-server.h
* /usr/include/libsoup-2.4/libsoup/soup-session-async.h
* /usr/include/libsoup-2.4/libsoup/soup-session-feature.h
* /usr/include/libsoup-2.4/libsoup/soup-session-sync.h
* /usr/include/libsoup-2.4/libsoup/soup-session.h
* /usr/include/libsoup-2.4/libsoup/soup-socket.h
* /usr/include/libsoup-2.4/libsoup/soup-status.h
* /usr/include/libsoup-2.4/libsoup/soup-tld.h
* /usr/include/libsoup-2.4/libsoup/soup-types.h
* /usr/include/libsoup-2.4/libsoup/soup-uri.h
* /usr/include/libsoup-2.4/libsoup/soup-value-utils.h
* /usr/include/libsoup-2.4/libsoup/soup-version.h
* /usr/include/libsoup-2.4/libsoup/soup-websocket-connection.h
* /usr/include/libsoup-2.4/libsoup/soup-websocket-extension-deflate.h
* /usr/include/libsoup-2.4/libsoup/soup-websocket-extension-manager.h
* /usr/include/libsoup-2.4/libsoup/soup-websocket-extension.h
* /usr/include/libsoup-2.4/libsoup/soup-websocket.h
* /usr/include/libsoup-2.4/libsoup/soup-xmlrpc-old.h
* /usr/include/libsoup-2.4/libsoup/soup-xmlrpc.h
* /usr/include/libsoup-2.4/libsoup/soup.h
* /usr/include/libsoup-gnome-2.4/libsoup/soup-cookie-jar-sqlite.h
* /usr/include/libsoup-gnome-2.4/libsoup/soup-gnome-features.h
* /usr/include/libsoup-gnome-2.4/libsoup/soup-gnome.h
* /usr/lib/girepository-1.0/Soup-2.4.typelib
* /usr/lib/girepository-1.0/SoupGNOME-2.4.typelib
* /usr/lib/libsoup-2.4.so
* /usr/lib/libsoup-2.4.so.1
* /usr/lib/libsoup-2.4.so.1.11.2
* /usr/lib/libsoup-gnome-2.4.so
* /usr/lib/libsoup-gnome-2.4.so.1
* /usr/lib/libsoup-gnome-2.4.so.1.11.2
* /usr/lib/pkgconfig/libsoup-2.4.pc
* /usr/lib/pkgconfig/libsoup-gnome-2.4.pc
* /usr/share/doc/libsoup-2.74.3/AUTHORS
* /usr/share/doc/libsoup-2.74.3/COPYING
* /usr/share/doc/libsoup-2.74.3/HACKING
* /usr/share/doc/libsoup-2.74.3/NEWS
* /usr/share/doc/libsoup-2.74.3/README
* /usr/share/doc/libsoup-2.74.3/README.msvc
* /usr/share/gir-1.0/Soup-2.4.gir
* /usr/share/gir-1.0/SoupGNOME-2.4.gir
* /usr/share/locale/an/LC_MESSAGES/libsoup.mo
* /usr/share/locale/as/LC_MESSAGES/libsoup.mo
* /usr/share/locale/be/LC_MESSAGES/libsoup.mo
* /usr/share/locale/bg/LC_MESSAGES/libsoup.mo
* /usr/share/locale/bn_IN/LC_MESSAGES/libsoup.mo
* /usr/share/locale/bs/LC_MESSAGES/libsoup.mo
* /usr/share/locale/ca/LC_MESSAGES/libsoup.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/libsoup.mo
* /usr/share/locale/cs/LC_MESSAGES/libsoup.mo
* /usr/share/locale/da/LC_MESSAGES/libsoup.mo
* /usr/share/locale/de/LC_MESSAGES/libsoup.mo
* /usr/share/locale/el/LC_MESSAGES/libsoup.mo
* /usr/share/locale/en_GB/LC_MESSAGES/libsoup.mo
* /usr/share/locale/eo/LC_MESSAGES/libsoup.mo
* /usr/share/locale/es/LC_MESSAGES/libsoup.mo
* /usr/share/locale/et/LC_MESSAGES/libsoup.mo
* /usr/share/locale/eu/LC_MESSAGES/libsoup.mo
* /usr/share/locale/fa/LC_MESSAGES/libsoup.mo
* /usr/share/locale/fi/LC_MESSAGES/libsoup.mo
* /usr/share/locale/fr/LC_MESSAGES/libsoup.mo
* /usr/share/locale/fur/LC_MESSAGES/libsoup.mo
* /usr/share/locale/gd/LC_MESSAGES/libsoup.mo
* /usr/share/locale/gl/LC_MESSAGES/libsoup.mo
* /usr/share/locale/gu/LC_MESSAGES/libsoup.mo
* /usr/share/locale/he/LC_MESSAGES/libsoup.mo
* /usr/share/locale/hi/LC_MESSAGES/libsoup.mo
* /usr/share/locale/hr/LC_MESSAGES/libsoup.mo
* /usr/share/locale/hu/LC_MESSAGES/libsoup.mo
* /usr/share/locale/id/LC_MESSAGES/libsoup.mo
* /usr/share/locale/it/LC_MESSAGES/libsoup.mo
* /usr/share/locale/ja/LC_MESSAGES/libsoup.mo
* /usr/share/locale/kn/LC_MESSAGES/libsoup.mo
* /usr/share/locale/ko/LC_MESSAGES/libsoup.mo
* /usr/share/locale/lt/LC_MESSAGES/libsoup.mo
* /usr/share/locale/lv/LC_MESSAGES/libsoup.mo
* /usr/share/locale/ml/LC_MESSAGES/libsoup.mo
* /usr/share/locale/mr/LC_MESSAGES/libsoup.mo
* /usr/share/locale/ms/LC_MESSAGES/libsoup.mo
* /usr/share/locale/nb/LC_MESSAGES/libsoup.mo
* /usr/share/locale/ne/LC_MESSAGES/libsoup.mo
* /usr/share/locale/nl/LC_MESSAGES/libsoup.mo
* /usr/share/locale/oc/LC_MESSAGES/libsoup.mo
* /usr/share/locale/or/LC_MESSAGES/libsoup.mo
* /usr/share/locale/pa/LC_MESSAGES/libsoup.mo
* /usr/share/locale/pl/LC_MESSAGES/libsoup.mo
* /usr/share/locale/pt/LC_MESSAGES/libsoup.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/libsoup.mo
* /usr/share/locale/ro/LC_MESSAGES/libsoup.mo
* /usr/share/locale/ru/LC_MESSAGES/libsoup.mo
* /usr/share/locale/sk/LC_MESSAGES/libsoup.mo
* /usr/share/locale/sl/LC_MESSAGES/libsoup.mo
* /usr/share/locale/sr/LC_MESSAGES/libsoup.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/libsoup.mo
* /usr/share/locale/sv/LC_MESSAGES/libsoup.mo
* /usr/share/locale/ta/LC_MESSAGES/libsoup.mo
* /usr/share/locale/te/LC_MESSAGES/libsoup.mo
* /usr/share/locale/tg/LC_MESSAGES/libsoup.mo
* /usr/share/locale/th/LC_MESSAGES/libsoup.mo
* /usr/share/locale/tr/LC_MESSAGES/libsoup.mo
* /usr/share/locale/ug/LC_MESSAGES/libsoup.mo
* /usr/share/locale/uk/LC_MESSAGES/libsoup.mo
* /usr/share/locale/uz@cyrillic/LC_MESSAGES/libsoup.mo
* /usr/share/locale/vi/LC_MESSAGES/libsoup.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/libsoup.mo
* /usr/share/locale/zh_HK/LC_MESSAGES/libsoup.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/libsoup.mo
* /usr/share/vala/vapi/libsoup-2.4.deps
* /usr/share/vala/vapi/libsoup-2.4.vapi
{{< /files >}}