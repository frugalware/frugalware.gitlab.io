+++
draft = false
title = "appstream-glib 0.8.2-2"
version = "0.8.2-2"
description = "Library for AppStream metadata"
date = "2023-09-28T14:09:59"
aliases = "/packages/218044"
categories = ['xlib']
upstreamurl = "https://people.freedesktop.org/~hughsient/appstream-glib"
arch = "x86_64"
size = "418832"
usize = "2556521"
sha1sum = "b6a090fa8981cbf2a027486b1dff4dd06605c506"
depends = "['curl', 'gcab>=1.2-2', 'gtk+3>=3.24.7-2', 'json-glib>=1.4.2-3', 'libstemmer', 'libyaml']"
reverse_depends = "['fwupd']"
+++
Library for AppStream metadata{{< spoiler text="show files" >}}* /usr/bin/appstream-builder
* /usr/bin/appstream-compose
* /usr/bin/appstream-util
* /usr/include/libappstream-glib/appstream-glib.h
* /usr/include/libappstream-glib/as-agreement-section.h
* /usr/include/libappstream-glib/as-agreement.h
* /usr/include/libappstream-glib/as-app-builder.h
* /usr/include/libappstream-glib/as-app.h
* /usr/include/libappstream-glib/as-bundle.h
* /usr/include/libappstream-glib/as-checksum.h
* /usr/include/libappstream-glib/as-content-rating.h
* /usr/include/libappstream-glib/as-enums.h
* /usr/include/libappstream-glib/as-format.h
* /usr/include/libappstream-glib/as-icon.h
* /usr/include/libappstream-glib/as-image.h
* /usr/include/libappstream-glib/as-inf.h
* /usr/include/libappstream-glib/as-launchable.h
* /usr/include/libappstream-glib/as-markup.h
* /usr/include/libappstream-glib/as-monitor.h
* /usr/include/libappstream-glib/as-node.h
* /usr/include/libappstream-glib/as-problem.h
* /usr/include/libappstream-glib/as-profile.h
* /usr/include/libappstream-glib/as-provide.h
* /usr/include/libappstream-glib/as-release.h
* /usr/include/libappstream-glib/as-require.h
* /usr/include/libappstream-glib/as-review.h
* /usr/include/libappstream-glib/as-screenshot.h
* /usr/include/libappstream-glib/as-store.h
* /usr/include/libappstream-glib/as-suggest.h
* /usr/include/libappstream-glib/as-tag.h
* /usr/include/libappstream-glib/as-translation.h
* /usr/include/libappstream-glib/as-utils.h
* /usr/include/libappstream-glib/as-version.h
* /usr/lib/asb-plugins-5/libasb_plugin_appdata.so
* /usr/lib/asb-plugins-5/libasb_plugin_desktop.so
* /usr/lib/asb-plugins-5/libasb_plugin_font.so
* /usr/lib/asb-plugins-5/libasb_plugin_gettext.so
* /usr/lib/asb-plugins-5/libasb_plugin_hardcoded.so
* /usr/lib/asb-plugins-5/libasb_plugin_icon.so
* /usr/lib/asb-plugins-5/libasb_plugin_shell_extension.so
* /usr/lib/girepository-1.0/AppStreamGlib-1.0.typelib
* /usr/lib/libappstream-glib.so
* /usr/lib/libappstream-glib.so.8
* /usr/lib/libappstream-glib.so.8.0.10
* /usr/lib/pkgconfig/appstream-glib.pc
* /usr/share/aclocal/appdata-xml.m4
* /usr/share/aclocal/appstream-xml.m4
* /usr/share/bash-completion/completions/appstream-builder
* /usr/share/bash-completion/completions/appstream-util
* /usr/share/doc/appstream-glib-0.8.2/AUTHORS
* /usr/share/doc/appstream-glib-0.8.2/COPYING
* /usr/share/doc/appstream-glib-0.8.2/NEWS
* /usr/share/doc/appstream-glib-0.8.2/README.md
* /usr/share/doc/appstream-glib-0.8.2/RELEASE
* /usr/share/gettext/its/appdata.its
* /usr/share/gettext/its/appdata.loc
* /usr/share/gir-1.0/AppStreamGlib-1.0.gir
* /usr/share/installed-tests/appstream-glib/appdata-validate.test
* /usr/share/installed-tests/appstream-glib/destdir-check.test
* /usr/share/locale/ca/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/cs/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/da/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/de/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/en_GB/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/es/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/fa/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/fi/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/fr/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/fur/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/gl/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/hr/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/hu/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/id/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/it/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/ka/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/ko/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/lt/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/oc/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/pl/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/pt/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/ru/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/sk/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/sl/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/sr/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/sv/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/tr/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/uk/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/appstream-glib.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/appstream-glib.mo
{{< /spoiler >}}