+++
draft = false
title = "guvcview 2.0.6-4"
version = "2.0.6-4"
description = "A video viewer and capturer for the linux uvc driver"
date = "2023-03-01T12:09:21"
aliases = "/packages/220086"
categories = ['xapps-extra']
upstreamurl = "https://sourceforge.net/projects/guvcview"
arch = "x86_64"
size = "295884"
usize = "1091883"
sha1sum = "2215af0c45d118b68699852f5def5aff0533a549"
depends = "['ffmpeg>=6.0', 'gsl>=2.7.1', 'libogg', 'libpulse>=6.0', 'libraw1394', 'libxau>=1.0.4-1', 'libxdamage>=1.1.1-3', 'libxdmcp', 'libxext>=1.0.5-3', 'libxml2>=2.7.8', 'portaudio', 'sdl2', 'systemd>=188', 'twolame']"
+++
A video viewer and capturer for the linux uvc driver

{{< files text="show files" >}}* /usr/bin/guvcview
* /usr/include/guvcview-2/libgviewaudio/gviewaudio.h
* /usr/include/guvcview-2/libgviewencoder/gviewencoder.h
* /usr/include/guvcview-2/libgviewrender/gviewrender.h
* /usr/include/guvcview-2/libgviewv4l2core/gview.h
* /usr/include/guvcview-2/libgviewv4l2core/gviewv4l2core.h
* /usr/lib/libgviewaudio-2.0.so.2
* /usr/lib/libgviewaudio-2.0.so.2.0.0
* /usr/lib/libgviewaudio.so
* /usr/lib/libgviewencoder-2.0.so.2
* /usr/lib/libgviewencoder-2.0.so.2.0.0
* /usr/lib/libgviewencoder.so
* /usr/lib/libgviewrender-2.0.so.2
* /usr/lib/libgviewrender-2.0.so.2.0.0
* /usr/lib/libgviewrender.so
* /usr/lib/libgviewv4l2core-2.0.so.2
* /usr/lib/libgviewv4l2core-2.0.so.2.0.0
* /usr/lib/libgviewv4l2core.so
* /usr/lib/pkgconfig/libgviewaudio.pc
* /usr/lib/pkgconfig/libgviewencoder.pc
* /usr/lib/pkgconfig/libgviewrender.pc
* /usr/lib/pkgconfig/libgviewv4l2core.pc
* /usr/share/appdata/guvcview.appdata.xml
* /usr/share/applications/guvcview.desktop
* /usr/share/doc/guvcview-2.0.6/AUTHORS
* /usr/share/doc/guvcview-2.0.6/ChangeLog
* /usr/share/doc/guvcview-2.0.6/COPYING
* /usr/share/doc/guvcview-2.0.6/INSTALL
* /usr/share/doc/guvcview-2.0.6/README.md
* /usr/share/doc/guvcview/AUTHORS
* /usr/share/doc/guvcview/ChangeLog
* /usr/share/doc/guvcview/COPYING
* /usr/share/doc/guvcview/INSTALL
* /usr/share/doc/guvcview/README.md
* /usr/share/locale/bg/LC_MESSAGES/guvcview.mo
* /usr/share/locale/bg/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/bs/LC_MESSAGES/guvcview.mo
* /usr/share/locale/bs/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/cs/LC_MESSAGES/guvcview.mo
* /usr/share/locale/cs/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/da/LC_MESSAGES/guvcview.mo
* /usr/share/locale/da/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/de/LC_MESSAGES/guvcview.mo
* /usr/share/locale/de/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/en_AU/LC_MESSAGES/guvcview.mo
* /usr/share/locale/en_AU/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/es/LC_MESSAGES/guvcview.mo
* /usr/share/locale/es/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/eu/LC_MESSAGES/guvcview.mo
* /usr/share/locale/eu/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/fo/LC_MESSAGES/guvcview.mo
* /usr/share/locale/fo/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/fr/LC_MESSAGES/guvcview.mo
* /usr/share/locale/fr/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/gl/LC_MESSAGES/guvcview.mo
* /usr/share/locale/gl/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/he/LC_MESSAGES/guvcview.mo
* /usr/share/locale/he/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/hr/LC_MESSAGES/guvcview.mo
* /usr/share/locale/hr/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/it/LC_MESSAGES/guvcview.mo
* /usr/share/locale/it/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/ja/LC_MESSAGES/guvcview.mo
* /usr/share/locale/ja/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/lv/LC_MESSAGES/guvcview.mo
* /usr/share/locale/lv/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/nl/LC_MESSAGES/guvcview.mo
* /usr/share/locale/nl/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/pl/LC_MESSAGES/guvcview.mo
* /usr/share/locale/pl/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/pt/LC_MESSAGES/guvcview.mo
* /usr/share/locale/pt/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/guvcview.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/ru/LC_MESSAGES/guvcview.mo
* /usr/share/locale/ru/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/si/LC_MESSAGES/guvcview.mo
* /usr/share/locale/si/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/sr/LC_MESSAGES/guvcview.mo
* /usr/share/locale/sr/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/tr/LC_MESSAGES/guvcview.mo
* /usr/share/locale/tr/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/uk/LC_MESSAGES/guvcview.mo
* /usr/share/locale/uk/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/guvcview.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/gview_v4l2core.mo
* /usr/share/man/man1/guvcview.1.gz
* /usr/share/menu/guvcview
* /usr/share/pixmaps/guvcview/audio_controls.png
* /usr/share/pixmaps/guvcview/camera.png
* /usr/share/pixmaps/guvcview/close.png
* /usr/share/pixmaps/guvcview/guvcview.png
* /usr/share/pixmaps/guvcview/image_controls.png
* /usr/share/pixmaps/guvcview/movie.png
* /usr/share/pixmaps/guvcview/video_controls.png
{{< /files >}}