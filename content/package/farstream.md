+++
draft = false
title = "farstream 0.2.9-2"
version = "0.2.9-2"
description = "Farstream - Audio/Video Communications Framework"
date = "2022-01-19T13:53:34"
aliases = "/packages/152998"
categories = ['xlib']
upstreamurl = "http://www.freedesktop.org/wiki/Software/Farstream"
arch = "x86_64"
size = "428276"
usize = "2425806"
sha1sum = "bb7c9833491b6d1c4936e02f45f7d89b6cb7c745"
depends = "['gst1-plugins-base>=1.9.2-2', 'libffi>=3.2.1-2', 'nice>=0.1.16']"
reverse_depends = "['libpurple', 'telepathy-farstream', 'telepathy-qt5']"
+++
Farstream - Audio/Video Communications Framework

{{< files text="show files" >}}* /usr/include/farstream-0.2/farstream/fs-candidate.h
* /usr/include/farstream-0.2/farstream/fs-codec.h
* /usr/include/farstream-0.2/farstream/fs-conference.h
* /usr/include/farstream-0.2/farstream/fs-element-added-notifier.h
* /usr/include/farstream-0.2/farstream/fs-enumtypes.h
* /usr/include/farstream-0.2/farstream/fs-participant.h
* /usr/include/farstream-0.2/farstream/fs-plugin.h
* /usr/include/farstream-0.2/farstream/fs-rtp.h
* /usr/include/farstream-0.2/farstream/fs-session.h
* /usr/include/farstream-0.2/farstream/fs-stream-transmitter.h
* /usr/include/farstream-0.2/farstream/fs-stream.h
* /usr/include/farstream-0.2/farstream/fs-transmitter.h
* /usr/include/farstream-0.2/farstream/fs-utils.h
* /usr/lib/farstream-0.2/libmulticast-transmitter.so
* /usr/lib/farstream-0.2/libnice-transmitter.so
* /usr/lib/farstream-0.2/librawudp-transmitter.so
* /usr/lib/farstream-0.2/libshm-transmitter.so
* /usr/lib/girepository-1.0/Farstream-0.2.typelib
* /usr/lib/gstreamer-1.0/libfsrawconference.so
* /usr/lib/gstreamer-1.0/libfsrtpconference.so
* /usr/lib/gstreamer-1.0/libfsrtpxdata.so
* /usr/lib/gstreamer-1.0/libfsvideoanyrate.so
* /usr/lib/libfarstream-0.2.so
* /usr/lib/libfarstream-0.2.so.5
* /usr/lib/libfarstream-0.2.so.5.1.1
* /usr/lib/pkgconfig/farstream-0.2.pc
* /usr/share/doc/farstream-0.2.9/AUTHORS
* /usr/share/doc/farstream-0.2.9/ChangeLog
* /usr/share/doc/farstream-0.2.9/COPYING
* /usr/share/doc/farstream-0.2.9/INSTALL
* /usr/share/doc/farstream-0.2.9/NEWS
* /usr/share/doc/farstream-0.2.9/README
* /usr/share/farstream/0.2/fsrawconference/default-element-properties
* /usr/share/farstream/0.2/fsrtpconference/default-codec-preferences
* /usr/share/farstream/0.2/fsrtpconference/default-element-properties
* /usr/share/gir-1.0/Farstream-0.2.gir
* /usr/share/gtk-doc/html/farstream-libs-0.2/ch01.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/ch02.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/ch03.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/ch04.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/ch05.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/farstream-libs-0.2.devhelp2
* /usr/share/gtk-doc/html/farstream-libs-0.2/farstream-libs-FsCandidate.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/farstream-libs-FsCodec.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/farstream-libs-FsPlugin.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/farstream-libs-RTP-Specific-types.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/farstream-libs-Utility-functions.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/FsConference.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/FsElementAddedNotifier.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/FsParticipant.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/FsSession.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/FsStream.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/FsStreamTransmitter.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/FsTransmitter.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/home.png
* /usr/share/gtk-doc/html/farstream-libs-0.2/index.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/left-insensitive.png
* /usr/share/gtk-doc/html/farstream-libs-0.2/left.png
* /usr/share/gtk-doc/html/farstream-libs-0.2/pt01.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/pt02.html
* /usr/share/gtk-doc/html/farstream-libs-0.2/right-insensitive.png
* /usr/share/gtk-doc/html/farstream-libs-0.2/right.png
* /usr/share/gtk-doc/html/farstream-libs-0.2/style.css
* /usr/share/gtk-doc/html/farstream-libs-0.2/up-insensitive.png
* /usr/share/gtk-doc/html/farstream-libs-0.2/up.png
* /usr/share/gtk-doc/html/farstream-plugins-0.2/ch01.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/ch02.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-0.2.devhelp2
* /usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-FsMulticastStreamTransmitter.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-FsNiceStreamTransmitter.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-FsRawParticipant.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-FsRawSession.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-FsRawStream.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-FsRawUdpStreamTransmitter.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/farstream-plugins-FsShmStreamTransmitter.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/FsRawConference.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/FsRtpConference.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/FsRtpParticipant.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/FsRtpSession.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/FsRtpStream.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/FsRTPXdataDepay.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/FsRTPXdataPay.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/FsVideoanyrate.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/home.png
* /usr/share/gtk-doc/html/farstream-plugins-0.2/index.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/left-insensitive.png
* /usr/share/gtk-doc/html/farstream-plugins-0.2/left.png
* /usr/share/gtk-doc/html/farstream-plugins-0.2/pt01.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/pt02.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/pt03.html
* /usr/share/gtk-doc/html/farstream-plugins-0.2/right-insensitive.png
* /usr/share/gtk-doc/html/farstream-plugins-0.2/right.png
* /usr/share/gtk-doc/html/farstream-plugins-0.2/style.css
* /usr/share/gtk-doc/html/farstream-plugins-0.2/up-insensitive.png
* /usr/share/gtk-doc/html/farstream-plugins-0.2/up.png
{{< /files >}}