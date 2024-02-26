+++
draft = false
title = "gtkspell3 3.0.10-3"
version = "3.0.10-3"
description = "On-the-fly spell checking for GtkTextView widgets"
date = "2022-01-24T12:11:58"
aliases = "/packages/184523"
categories = ['xlib']
upstreamurl = "http://gtkspell.sourceforge.net/"
arch = "x86_64"
size = "55544"
usize = "265937"
sha1sum = "8857574ef5e04bba0f96e23deca8141f77d5ecdd"
depends = "['enchant', 'gtk+3>=3.24.0', 'libffi>=3.2.1']"
reverse_depends = "['inkscape', 'poedit']"
+++
On-the-fly spell checking for GtkTextView widgets{{< spoiler text="show files" >}}* /usr/include/gtkspell-3.0/gtkspell/gtkspell.h
* /usr/lib/girepository-1.0/GtkSpell-3.0.typelib
* /usr/lib/libgtkspell3-3.so
* /usr/lib/libgtkspell3-3.so.0
* /usr/lib/libgtkspell3-3.so.0.2.0
* /usr/lib/pkgconfig/gtkspell3-3.0.pc
* /usr/share/doc/gtkspell3-3.0.10/AUTHORS
* /usr/share/doc/gtkspell3-3.0.10/ChangeLog
* /usr/share/doc/gtkspell3-3.0.10/COPYING
* /usr/share/doc/gtkspell3-3.0.10/INSTALL
* /usr/share/doc/gtkspell3-3.0.10/README
* /usr/share/gir-1.0/GtkSpell-3.0.gir
* /usr/share/gtk-doc/html/gtkspell3/annotation-glossary.html
* /usr/share/gtk-doc/html/gtkspell3/api-index-full.html
* /usr/share/gtk-doc/html/gtkspell3/ch02.html
* /usr/share/gtk-doc/html/gtkspell3/chapter-tutorial.html
* /usr/share/gtk-doc/html/gtkspell3/gtkspell3-gtkspell.html
* /usr/share/gtk-doc/html/gtkspell3/gtkspell3.devhelp2
* /usr/share/gtk-doc/html/gtkspell3/home.png
* /usr/share/gtk-doc/html/gtkspell3/index.html
* /usr/share/gtk-doc/html/gtkspell3/left-insensitive.png
* /usr/share/gtk-doc/html/gtkspell3/left.png
* /usr/share/gtk-doc/html/gtkspell3/object-tree.html
* /usr/share/gtk-doc/html/gtkspell3/right-insensitive.png
* /usr/share/gtk-doc/html/gtkspell3/right.png
* /usr/share/gtk-doc/html/gtkspell3/style.css
* /usr/share/gtk-doc/html/gtkspell3/tutorial-advanced.html
* /usr/share/gtk-doc/html/gtkspell3/tutorial-bindings.html
* /usr/share/gtk-doc/html/gtkspell3/tutorial-building.html
* /usr/share/gtk-doc/html/gtkspell3/tutorial-lang.html
* /usr/share/gtk-doc/html/gtkspell3/up-insensitive.png
* /usr/share/gtk-doc/html/gtkspell3/up.png
* /usr/share/locale/af/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/ak/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/ast/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/be/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/ca/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/cs/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/da/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/de/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/el/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/eo/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/es/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/eu/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/ff/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/fi/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/fo/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/fr/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/ga/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/gl/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/he/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/hr/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/hu/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/hy/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/id/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/is/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/it/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/ja/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/ky/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/lg/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/lt/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/lv/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/mn/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/ms/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/nb/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/nl/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/nso/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/pl/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/pt/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/rm/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/ro/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/ru/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/rw/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/sk/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/sl/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/son/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/sq/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/sr/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/st/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/sv/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/th/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/tr/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/uk/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/vi/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/wa/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/zh_HK/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/gtkspell3.mo
* /usr/share/locale/zu/LC_MESSAGES/gtkspell3.mo
* /usr/share/vala/vapi/gtkspell3-3.0.deps
* /usr/share/vala/vapi/gtkspell3-3.0.vapi
{{< /spoiler >}}