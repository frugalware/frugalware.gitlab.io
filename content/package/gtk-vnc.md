+++
draft = false
title = "gtk-vnc 1.3.1-1"
version = "1.3.1-1"
date = "2023-03-13T09:05:33"
categories = ['gnome']
upstreamurl = "http://www.gnome.org/"
arch = "x86_64"
size = "183960"
usize = "1075762"
sha1sum = "3796515b7b170d472f84789df4df9a355be7d8bd"
depends = "['gtk+3>=3.24.0', 'libgcrypt>=1.7.3-2', 'libpulse>=9.0-2', 'cyrus-sasl', 'python3']"
files = "['usr/', 'usr/bin/', 'usr/bin/gvnccapture', 'usr/include/', 'usr/include/gtk-vnc-2.0/', 'usr/include/gtk-vnc-2.0/gtk-vnc.h', 'usr/include/gtk-vnc-2.0/vnccairoframebuffer.h', 'usr/include/gtk-vnc-2.0/vncdisplayenums.h', 'usr/include/gtk-vnc-2.0/vncdisplay.h', 'usr/include/gtk-vnc-2.0/vncgrabsequence.h', 'usr/include/gvnc-1.0/', 'usr/include/gvnc-1.0/gvnc.h', 'usr/include/gvnc-1.0/vncaudioformat.h', 'usr/include/gvnc-1.0/vncaudio.h', 'usr/include/gvnc-1.0/vncaudiosample.h', 'usr/include/gvnc-1.0/vncbaseaudio.h', 'usr/include/gvnc-1.0/vncbaseframebuffer.h', 'usr/include/gvnc-1.0/vnccolormap.h', 'usr/include/gvnc-1.0/vncconnectionenums.h', 'usr/include/gvnc-1.0/vncconnection.h', 'usr/include/gvnc-1.0/vnccursor.h', 'usr/include/gvnc-1.0/vncframebuffer.h', 'usr/include/gvnc-1.0/vncpixelformat.h', 'usr/include/gvnc-1.0/vncutil.h', 'usr/include/gvnc-1.0/vncversion.h', 'usr/include/gvncpulse-1.0/', 'usr/include/gvncpulse-1.0/gvncpulse.h', 'usr/include/gvncpulse-1.0/vncaudiopulse.h', 'usr/lib/', 'usr/lib/girepository-1.0/', 'usr/lib/girepository-1.0/GtkVnc-2.0.typelib', 'usr/lib/girepository-1.0/GVnc-1.0.typelib', 'usr/lib/girepository-1.0/GVncPulse-1.0.typelib', 'usr/lib/libgtk-vnc-2.0.so', 'usr/lib/libgtk-vnc-2.0.so.0', 'usr/lib/libgtk-vnc-2.0.so.0.0.2', 'usr/lib/libgvnc-1.0.so', 'usr/lib/libgvnc-1.0.so.0', 'usr/lib/libgvnc-1.0.so.0.0.1', 'usr/lib/libgvncpulse-1.0.so', 'usr/lib/libgvncpulse-1.0.so.0', 'usr/lib/libgvncpulse-1.0.so.0.0.1', 'usr/lib/pkgconfig/', 'usr/lib/pkgconfig/gtk-vnc-2.0.pc', 'usr/lib/pkgconfig/gvnc-1.0.pc', 'usr/lib/pkgconfig/gvncpulse-1.0.pc', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/gtk-vnc-1.3.1/', 'usr/share/doc/gtk-vnc-1.3.1/AUTHORS', 'usr/share/doc/gtk-vnc-1.3.1/ChangeLog', 'usr/share/doc/gtk-vnc-1.3.1/COPYING.LIB', 'usr/share/doc/gtk-vnc-1.3.1/NEWS', 'usr/share/doc/gtk-vnc-1.3.1/README', 'usr/share/gir-1.0/', 'usr/share/gir-1.0/GtkVnc-2.0.gir', 'usr/share/gir-1.0/GVnc-1.0.gir', 'usr/share/gir-1.0/GVncPulse-1.0.gir', 'usr/share/locale/', 'usr/share/locale/bs/', 'usr/share/locale/bs/LC_MESSAGES/', 'usr/share/locale/bs/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/ca/', 'usr/share/locale/ca/LC_MESSAGES/', 'usr/share/locale/ca/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/ca@valencia/', 'usr/share/locale/ca@valencia/LC_MESSAGES/', 'usr/share/locale/ca@valencia/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/cs/', 'usr/share/locale/cs/LC_MESSAGES/', 'usr/share/locale/cs/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/da/', 'usr/share/locale/da/LC_MESSAGES/', 'usr/share/locale/da/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/de/', 'usr/share/locale/de/LC_MESSAGES/', 'usr/share/locale/de/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/el/', 'usr/share/locale/el/LC_MESSAGES/', 'usr/share/locale/el/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/en_GB/', 'usr/share/locale/en_GB/LC_MESSAGES/', 'usr/share/locale/en_GB/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/eo/', 'usr/share/locale/eo/LC_MESSAGES/', 'usr/share/locale/eo/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/es/', 'usr/share/locale/es/LC_MESSAGES/', 'usr/share/locale/es/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/eu/', 'usr/share/locale/eu/LC_MESSAGES/', 'usr/share/locale/eu/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/fa/', 'usr/share/locale/fa/LC_MESSAGES/', 'usr/share/locale/fa/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/fr/', 'usr/share/locale/fr/LC_MESSAGES/', 'usr/share/locale/fr/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/fur/', 'usr/share/locale/fur/LC_MESSAGES/', 'usr/share/locale/fur/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/gd/', 'usr/share/locale/gd/LC_MESSAGES/', 'usr/share/locale/gd/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/gl/', 'usr/share/locale/gl/LC_MESSAGES/', 'usr/share/locale/gl/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/guc/', 'usr/share/locale/guc/LC_MESSAGES/', 'usr/share/locale/guc/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/he/', 'usr/share/locale/he/LC_MESSAGES/', 'usr/share/locale/he/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/hr/', 'usr/share/locale/hr/LC_MESSAGES/', 'usr/share/locale/hr/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/hu/', 'usr/share/locale/hu/LC_MESSAGES/', 'usr/share/locale/hu/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/id/', 'usr/share/locale/id/LC_MESSAGES/', 'usr/share/locale/id/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/it/', 'usr/share/locale/it/LC_MESSAGES/', 'usr/share/locale/it/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/ja/', 'usr/share/locale/ja/LC_MESSAGES/', 'usr/share/locale/ja/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/ka/', 'usr/share/locale/ka/LC_MESSAGES/', 'usr/share/locale/ka/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/ko/', 'usr/share/locale/ko/LC_MESSAGES/', 'usr/share/locale/ko/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/lt/', 'usr/share/locale/lt/LC_MESSAGES/', 'usr/share/locale/lt/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/lv/', 'usr/share/locale/lv/LC_MESSAGES/', 'usr/share/locale/lv/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/nb/', 'usr/share/locale/nb/LC_MESSAGES/', 'usr/share/locale/nb/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/nds/', 'usr/share/locale/nds/LC_MESSAGES/', 'usr/share/locale/nds/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/nl/', 'usr/share/locale/nl/LC_MESSAGES/', 'usr/share/locale/nl/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/oc/', 'usr/share/locale/oc/LC_MESSAGES/', 'usr/share/locale/oc/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/pa/', 'usr/share/locale/pa/LC_MESSAGES/', 'usr/share/locale/pa/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/pl/', 'usr/share/locale/pl/LC_MESSAGES/', 'usr/share/locale/pl/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/pt/', 'usr/share/locale/pt_BR/', 'usr/share/locale/pt_BR/LC_MESSAGES/', 'usr/share/locale/pt_BR/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/pt/LC_MESSAGES/', 'usr/share/locale/pt/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/ro/', 'usr/share/locale/ro/LC_MESSAGES/', 'usr/share/locale/ro/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/ru/', 'usr/share/locale/ru/LC_MESSAGES/', 'usr/share/locale/ru/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/sk/', 'usr/share/locale/sk/LC_MESSAGES/', 'usr/share/locale/sk/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/sl/', 'usr/share/locale/sl/LC_MESSAGES/', 'usr/share/locale/sl/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/sr/', 'usr/share/locale/sr@latin/', 'usr/share/locale/sr@latin/LC_MESSAGES/', 'usr/share/locale/sr@latin/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/sr/LC_MESSAGES/', 'usr/share/locale/sr/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/sv/', 'usr/share/locale/sv/LC_MESSAGES/', 'usr/share/locale/sv/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/te/', 'usr/share/locale/te/LC_MESSAGES/', 'usr/share/locale/te/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/tg/', 'usr/share/locale/tg/LC_MESSAGES/', 'usr/share/locale/tg/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/th/', 'usr/share/locale/th/LC_MESSAGES/', 'usr/share/locale/th/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/tr/', 'usr/share/locale/tr/LC_MESSAGES/', 'usr/share/locale/tr/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/uk/', 'usr/share/locale/uk/LC_MESSAGES/', 'usr/share/locale/uk/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/zh_CN/', 'usr/share/locale/zh_CN/LC_MESSAGES/', 'usr/share/locale/zh_CN/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/zh_HK/', 'usr/share/locale/zh_HK/LC_MESSAGES/', 'usr/share/locale/zh_HK/LC_MESSAGES/gtk-vnc.mo', 'usr/share/locale/zh_TW/', 'usr/share/locale/zh_TW/LC_MESSAGES/', 'usr/share/locale/zh_TW/LC_MESSAGES/gtk-vnc.mo', 'usr/share/man/', 'usr/share/man/man1/', 'usr/share/man/man1/gvnccapture.1.gz', 'usr/share/vala/', 'usr/share/vala/vapi/', 'usr/share/vala/vapi/gtk-vnc-2.0.deps', 'usr/share/vala/vapi/gtk-vnc-2.0.vapi', 'usr/share/vala/vapi/gvnc-1.0.deps', 'usr/share/vala/vapi/gvnc-1.0.vapi', 'usr/share/vala/vapi/gvncpulse-1.0.deps', 'usr/share/vala/vapi/gvncpulse-1.0.vapi']"
+++
VNC viewer wigdet for GTK+