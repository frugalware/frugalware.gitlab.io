+++
draft = false
title = "openbox 3.6.1-6"
version = "3.6.1-6"
description = "A standards compliant, fast, light-weight, extensible window manager."
date = "2022-12-10T19:18:04"
aliases = "/packages/3269"
categories = ['x11-extra']
upstreamurl = "http://openbox.org"
arch = "x86_64"
size = "340572"
usize = "1299823"
sha1sum = "154fd00ee073098403d3c0098a04eec4c162b9d2"
depends = "['imlib2>=1.4.7-3', 'libffi>=3.2.1', 'libpng>=1.6.20', 'librsvg>=2.40.13', 'libsm>=1.2.2-2', 'libxcursor>=1.1.14-2', 'libxinerama>=1.1.3-2', 'libxrandr>=1.5.0-4', 'openbox-frugalware', 'python3', 'startup-notification>=0.12-3', 'xorg-server>=1.18.0']"
reverse_depends = "['obconf']"
+++
A standards compliant, fast, light-weight, extensible window manager.

{{< files text="show files" >}}* /etc/X11/sessions/openbox-kde.desktop
* /etc/X11/sessions/openbox.desktop
* /etc/xdg/openbox/autostart
* /etc/xdg/openbox/environment
* /etc/xdg/openbox/menu.xml
* /etc/xdg/openbox/rc.xml
* /usr/bin/gdm-control
* /usr/bin/obxprop
* /usr/bin/openbox
* /usr/bin/openbox-kde-session
* /usr/bin/openbox-session
* /usr/include/openbox/3.6/obrender/color.h
* /usr/include/openbox/3.6/obrender/font.h
* /usr/include/openbox/3.6/obrender/geom.h
* /usr/include/openbox/3.6/obrender/gradient.h
* /usr/include/openbox/3.6/obrender/image.h
* /usr/include/openbox/3.6/obrender/instance.h
* /usr/include/openbox/3.6/obrender/mask.h
* /usr/include/openbox/3.6/obrender/render.h
* /usr/include/openbox/3.6/obrender/theme.h
* /usr/include/openbox/3.6/obrender/version.h
* /usr/include/openbox/3.6/obt/display.h
* /usr/include/openbox/3.6/obt/keyboard.h
* /usr/include/openbox/3.6/obt/link.h
* /usr/include/openbox/3.6/obt/paths.h
* /usr/include/openbox/3.6/obt/prop.h
* /usr/include/openbox/3.6/obt/signal.h
* /usr/include/openbox/3.6/obt/util.h
* /usr/include/openbox/3.6/obt/version.h
* /usr/include/openbox/3.6/obt/xml.h
* /usr/include/openbox/3.6/obt/xqueue.h
* /usr/lib/libobrender.so
* /usr/lib/libobrender.so.32
* /usr/lib/libobrender.so.32.0.0
* /usr/lib/libobt.so
* /usr/lib/libobt.so.2
* /usr/lib/libobt.so.2.0.2
* /usr/lib/openbox/openbox-autostart
* /usr/lib/openbox/openbox-xdg-autostart
* /usr/lib/pkgconfig/obrender-3.5.pc
* /usr/lib/pkgconfig/obt-3.5.pc
* /usr/share/applications/openbox.desktop
* /usr/share/doc/openbox-3.6.1/AUTHORS
* /usr/share/doc/openbox-3.6.1/CHANGELOG
* /usr/share/doc/openbox-3.6.1/COMPLIANCE
* /usr/share/doc/openbox-3.6.1/COPYING
* /usr/share/doc/openbox-3.6.1/menu.xsd
* /usr/share/doc/openbox-3.6.1/rc-mouse-focus.xml
* /usr/share/doc/openbox-3.6.1/rc.xsd
* /usr/share/doc/openbox-3.6.1/README
* /usr/share/doc/openbox-3.6.1/xbm/bullet.xbm
* /usr/share/doc/openbox-3.6.1/xbm/close.xbm
* /usr/share/doc/openbox-3.6.1/xbm/desk.xbm
* /usr/share/doc/openbox-3.6.1/xbm/desk_toggled.xbm
* /usr/share/doc/openbox-3.6.1/xbm/iconify.xbm
* /usr/share/doc/openbox-3.6.1/xbm/max.xbm
* /usr/share/doc/openbox-3.6.1/xbm/max_toggled.xbm
* /usr/share/doc/openbox-3.6.1/xbm/shade.xbm
* /usr/share/doc/openbox-3.6.1/xbm/shade_toggled.xbm
* /usr/share/gnome-session/sessions/openbox-gnome-fallback.session
* /usr/share/gnome-session/sessions/openbox-gnome.session
* /usr/share/locale/af/LC_MESSAGES/openbox.mo
* /usr/share/locale/ar/LC_MESSAGES/openbox.mo
* /usr/share/locale/be/LC_MESSAGES/openbox.mo
* /usr/share/locale/bn_IN/LC_MESSAGES/openbox.mo
* /usr/share/locale/ca/LC_MESSAGES/openbox.mo
* /usr/share/locale/cs/LC_MESSAGES/openbox.mo
* /usr/share/locale/da/LC_MESSAGES/openbox.mo
* /usr/share/locale/de/LC_MESSAGES/openbox.mo
* /usr/share/locale/en@boldquot/LC_MESSAGES/openbox.mo
* /usr/share/locale/en@quot/LC_MESSAGES/openbox.mo
* /usr/share/locale/es/LC_MESSAGES/openbox.mo
* /usr/share/locale/et/LC_MESSAGES/openbox.mo
* /usr/share/locale/eu/LC_MESSAGES/openbox.mo
* /usr/share/locale/fi/LC_MESSAGES/openbox.mo
* /usr/share/locale/fr/LC_MESSAGES/openbox.mo
* /usr/share/locale/gl_ES/LC_MESSAGES/openbox.mo
* /usr/share/locale/he/LC_MESSAGES/openbox.mo
* /usr/share/locale/hr/LC_MESSAGES/openbox.mo
* /usr/share/locale/hu/LC_MESSAGES/openbox.mo
* /usr/share/locale/ia/LC_MESSAGES/openbox.mo
* /usr/share/locale/it/LC_MESSAGES/openbox.mo
* /usr/share/locale/ja/LC_MESSAGES/openbox.mo
* /usr/share/locale/lt/LC_MESSAGES/openbox.mo
* /usr/share/locale/lv/LC_MESSAGES/openbox.mo
* /usr/share/locale/nl/LC_MESSAGES/openbox.mo
* /usr/share/locale/no/LC_MESSAGES/openbox.mo
* /usr/share/locale/pl/LC_MESSAGES/openbox.mo
* /usr/share/locale/pt/LC_MESSAGES/openbox.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/openbox.mo
* /usr/share/locale/ro/LC_MESSAGES/openbox.mo
* /usr/share/locale/ru/LC_MESSAGES/openbox.mo
* /usr/share/locale/sk/LC_MESSAGES/openbox.mo
* /usr/share/locale/sr/LC_MESSAGES/openbox.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/openbox.mo
* /usr/share/locale/sv/LC_MESSAGES/openbox.mo
* /usr/share/locale/tr/LC_MESSAGES/openbox.mo
* /usr/share/locale/uk/LC_MESSAGES/openbox.mo
* /usr/share/locale/vi/LC_MESSAGES/openbox.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/openbox.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/openbox.mo
* /usr/share/man/man1/obxprop.1.gz
* /usr/share/man/man1/openbox-kde-session.1.gz
* /usr/share/man/man1/openbox-session.1.gz
* /usr/share/man/man1/openbox.1.gz
* /usr/share/pixmaps/openbox.png
* /usr/share/themes/Artwiz-boxed/openbox-3/themerc
* /usr/share/themes/Bear2/openbox-3/close.xbm
* /usr/share/themes/Bear2/openbox-3/close_pressed.xbm
* /usr/share/themes/Bear2/openbox-3/desk.xbm
* /usr/share/themes/Bear2/openbox-3/desk_toggled.xbm
* /usr/share/themes/Bear2/openbox-3/iconify.xbm
* /usr/share/themes/Bear2/openbox-3/iconify_pressed.xbm
* /usr/share/themes/Bear2/openbox-3/max.xbm
* /usr/share/themes/Bear2/openbox-3/max_pressed.xbm
* /usr/share/themes/Bear2/openbox-3/max_toggled.xbm
* /usr/share/themes/Bear2/openbox-3/shade.xbm
* /usr/share/themes/Bear2/openbox-3/shade_pressed.xbm
* /usr/share/themes/Bear2/openbox-3/themerc
* /usr/share/themes/Clearlooks-3.4/openbox-3/themerc
* /usr/share/themes/Clearlooks-Olive/openbox-3/themerc
* /usr/share/themes/Clearlooks/openbox-3/themerc
* /usr/share/themes/Mikachu/openbox-3/bullet.xbm
* /usr/share/themes/Mikachu/openbox-3/close.xbm
* /usr/share/themes/Mikachu/openbox-3/desk.xbm
* /usr/share/themes/Mikachu/openbox-3/iconify.xbm
* /usr/share/themes/Mikachu/openbox-3/max.xbm
* /usr/share/themes/Mikachu/openbox-3/themerc
* /usr/share/themes/Natura/openbox-3/close.xbm
* /usr/share/themes/Natura/openbox-3/close_hover.xbm
* /usr/share/themes/Natura/openbox-3/desk.xbm
* /usr/share/themes/Natura/openbox-3/desk_hover.xbm
* /usr/share/themes/Natura/openbox-3/desk_toggled.xbm
* /usr/share/themes/Natura/openbox-3/iconify.xbm
* /usr/share/themes/Natura/openbox-3/iconify_hover.xbm
* /usr/share/themes/Natura/openbox-3/max.xbm
* /usr/share/themes/Natura/openbox-3/max_hover.xbm
* /usr/share/themes/Natura/openbox-3/max_toggled.xbm
* /usr/share/themes/Natura/openbox-3/shade.xbm
* /usr/share/themes/Natura/openbox-3/shade_hover.xbm
* /usr/share/themes/Natura/openbox-3/themerc
* /usr/share/themes/Onyx-Citrus/openbox-3/themerc
* /usr/share/themes/Onyx/openbox-3/themerc
* /usr/share/themes/Orang/openbox-3/themerc
* /usr/share/themes/Syscrash/openbox-3/max.xbm
* /usr/share/themes/Syscrash/openbox-3/max_disabled.xbm
* /usr/share/themes/Syscrash/openbox-3/max_pressed.xbm
* /usr/share/themes/Syscrash/openbox-3/max_toggled.xbm
* /usr/share/themes/Syscrash/openbox-3/themerc
* /usr/share/xsessions/openbox-kde.desktop
* /usr/share/xsessions/openbox.desktop
{{< /files >}}