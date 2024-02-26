+++
draft = false
title = "libgsf 1.14.52-1"
version = "1.14.52-1"
description = "A library for reading and writing structured files (eg MS OLE and Zip)"
date = "2024-02-05T21:56:48"
aliases = "/packages/3178"
categories = ['xlib']
upstreamurl = "http://www.gnome.org/"
arch = "x86_64"
size = "365124"
usize = "2561770"
sha1sum = "01b7e1dc267de00e791bb7d099ae1bdb3893697e"
depends = "['gdk-pixbuf2>=2.36.11-3', 'libffi>=3.2.1-2', 'libpng>=1.6.25', 'libxml2>=2.9.4-3']"
reverse_depends = "['libextractor', 'libpst', 'libvips']"
+++
A library for reading and writing structured files (eg MS OLE and Zip)

{{< files text="show files" >}}* /usr/bin/gsf
* /usr/bin/gsf-office-thumbnailer
* /usr/bin/gsf-vba-dump
* /usr/include/libgsf-1/gsf/gsf-blob.h
* /usr/include/libgsf-1/gsf/gsf-clip-data.h
* /usr/include/libgsf-1/gsf/gsf-doc-meta-data.h
* /usr/include/libgsf-1/gsf/gsf-docprop-vector.h
* /usr/include/libgsf-1/gsf/gsf-fwd.h
* /usr/include/libgsf-1/gsf/gsf-impl-utils.h
* /usr/include/libgsf-1/gsf/gsf-infile-impl.h
* /usr/include/libgsf-1/gsf/gsf-infile-msole.h
* /usr/include/libgsf-1/gsf/gsf-infile-msvba.h
* /usr/include/libgsf-1/gsf/gsf-infile-stdio.h
* /usr/include/libgsf-1/gsf/gsf-infile-tar.h
* /usr/include/libgsf-1/gsf/gsf-infile-zip.h
* /usr/include/libgsf-1/gsf/gsf-infile.h
* /usr/include/libgsf-1/gsf/gsf-input-bzip.h
* /usr/include/libgsf-1/gsf/gsf-input-gio.h
* /usr/include/libgsf-1/gsf/gsf-input-gzip.h
* /usr/include/libgsf-1/gsf/gsf-input-http.h
* /usr/include/libgsf-1/gsf/gsf-input-impl.h
* /usr/include/libgsf-1/gsf/gsf-input-iochannel.h
* /usr/include/libgsf-1/gsf/gsf-input-memory.h
* /usr/include/libgsf-1/gsf/gsf-input-proxy.h
* /usr/include/libgsf-1/gsf/gsf-input-stdio.h
* /usr/include/libgsf-1/gsf/gsf-input-textline.h
* /usr/include/libgsf-1/gsf/gsf-input.h
* /usr/include/libgsf-1/gsf/gsf-libxml.h
* /usr/include/libgsf-1/gsf/gsf-meta-names.h
* /usr/include/libgsf-1/gsf/gsf-msole-utils.h
* /usr/include/libgsf-1/gsf/gsf-open-pkg-utils.h
* /usr/include/libgsf-1/gsf/gsf-opendoc-utils.h
* /usr/include/libgsf-1/gsf/gsf-outfile-impl.h
* /usr/include/libgsf-1/gsf/gsf-outfile-msole.h
* /usr/include/libgsf-1/gsf/gsf-outfile-stdio.h
* /usr/include/libgsf-1/gsf/gsf-outfile-zip.h
* /usr/include/libgsf-1/gsf/gsf-outfile.h
* /usr/include/libgsf-1/gsf/gsf-output-bzip.h
* /usr/include/libgsf-1/gsf/gsf-output-csv.h
* /usr/include/libgsf-1/gsf/gsf-output-gio.h
* /usr/include/libgsf-1/gsf/gsf-output-gzip.h
* /usr/include/libgsf-1/gsf/gsf-output-iconv.h
* /usr/include/libgsf-1/gsf/gsf-output-impl.h
* /usr/include/libgsf-1/gsf/gsf-output-iochannel.h
* /usr/include/libgsf-1/gsf/gsf-output-memory.h
* /usr/include/libgsf-1/gsf/gsf-output-stdio.h
* /usr/include/libgsf-1/gsf/gsf-output.h
* /usr/include/libgsf-1/gsf/gsf-shared-memory.h
* /usr/include/libgsf-1/gsf/gsf-structured-blob.h
* /usr/include/libgsf-1/gsf/gsf-timestamp.h
* /usr/include/libgsf-1/gsf/gsf-utils.h
* /usr/include/libgsf-1/gsf/gsf.h
* /usr/lib/girepository-1.0/Gsf-1.typelib
* /usr/lib/libgsf-1.so
* /usr/lib/libgsf-1.so.114
* /usr/lib/libgsf-1.so.114.0.52
* /usr/lib/pkgconfig/libgsf-1.pc
* /usr/share/doc/libgsf-1.14.52/AUTHORS
* /usr/share/doc/libgsf-1.14.52/BUGS
* /usr/share/doc/libgsf-1.14.52/ChangeLog
* /usr/share/doc/libgsf-1.14.52/COPYING
* /usr/share/doc/libgsf-1.14.52/HACKING
* /usr/share/doc/libgsf-1.14.52/INSTALL
* /usr/share/doc/libgsf-1.14.52/NEWS
* /usr/share/doc/libgsf-1.14.52/README
* /usr/share/doc/libgsf-1.14.52/TODO
* /usr/share/gir-1.0/Gsf-1.gir
* /usr/share/gtk-doc/html/gsf/annotation-glossary.html
* /usr/share/gtk-doc/html/gsf/api.html
* /usr/share/gtk-doc/html/gsf/dependencies.html
* /usr/share/gtk-doc/html/gsf/gsf-blobs.html
* /usr/share/gtk-doc/html/gsf/gsf-clip-data.html
* /usr/share/gtk-doc/html/gsf/gsf-Compression.html
* /usr/share/gtk-doc/html/gsf/gsf-GIO.html
* /usr/share/gtk-doc/html/gsf/gsf-GIOChannel.html
* /usr/share/gtk-doc/html/gsf/gsf-index.html
* /usr/share/gtk-doc/html/gsf/gsf-Infile-reading-structed-files.html
* /usr/share/gtk-doc/html/gsf/gsf-Input-from-unstructured-files.html
* /usr/share/gtk-doc/html/gsf/gsf-memory.html
* /usr/share/gtk-doc/html/gsf/gsf-metadata.html
* /usr/share/gtk-doc/html/gsf/gsf-MS-OLE2.html
* /usr/share/gtk-doc/html/gsf/gsf-OASIS-Open-Document.html
* /usr/share/gtk-doc/html/gsf/gsf-Outfile-writing-structed-files.html
* /usr/share/gtk-doc/html/gsf/gsf-Output-to-unstructured-files.html
* /usr/share/gtk-doc/html/gsf/gsf-Reading-and-Writing-from-local-files-and-directories.html
* /usr/share/gtk-doc/html/gsf/gsf-Text.html
* /usr/share/gtk-doc/html/gsf/gsf-users.html
* /usr/share/gtk-doc/html/gsf/gsf-Utilities.html
* /usr/share/gtk-doc/html/gsf/gsf-XML-and-libxml.html
* /usr/share/gtk-doc/html/gsf/gsf-Zip.html
* /usr/share/gtk-doc/html/gsf/gsf.devhelp2
* /usr/share/gtk-doc/html/gsf/history.html
* /usr/share/gtk-doc/html/gsf/home.png
* /usr/share/gtk-doc/html/gsf/index.html
* /usr/share/gtk-doc/html/gsf/intro.html
* /usr/share/gtk-doc/html/gsf/io.html
* /usr/share/gtk-doc/html/gsf/left-insensitive.png
* /usr/share/gtk-doc/html/gsf/left.png
* /usr/share/gtk-doc/html/gsf/misc.html
* /usr/share/gtk-doc/html/gsf/parsers.html
* /usr/share/gtk-doc/html/gsf/right-insensitive.png
* /usr/share/gtk-doc/html/gsf/right.png
* /usr/share/gtk-doc/html/gsf/sources.html
* /usr/share/gtk-doc/html/gsf/style.css
* /usr/share/gtk-doc/html/gsf/up-insensitive.png
* /usr/share/gtk-doc/html/gsf/up.png
* /usr/share/locale/as/LC_MESSAGES/libgsf.mo
* /usr/share/locale/bs/LC_MESSAGES/libgsf.mo
* /usr/share/locale/ca/LC_MESSAGES/libgsf.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/libgsf.mo
* /usr/share/locale/cs/LC_MESSAGES/libgsf.mo
* /usr/share/locale/da/LC_MESSAGES/libgsf.mo
* /usr/share/locale/de/LC_MESSAGES/libgsf.mo
* /usr/share/locale/el/LC_MESSAGES/libgsf.mo
* /usr/share/locale/en_GB/LC_MESSAGES/libgsf.mo
* /usr/share/locale/eo/LC_MESSAGES/libgsf.mo
* /usr/share/locale/es/LC_MESSAGES/libgsf.mo
* /usr/share/locale/eu/LC_MESSAGES/libgsf.mo
* /usr/share/locale/fi/LC_MESSAGES/libgsf.mo
* /usr/share/locale/fr/LC_MESSAGES/libgsf.mo
* /usr/share/locale/gl/LC_MESSAGES/libgsf.mo
* /usr/share/locale/he/LC_MESSAGES/libgsf.mo
* /usr/share/locale/hr/LC_MESSAGES/libgsf.mo
* /usr/share/locale/hu/LC_MESSAGES/libgsf.mo
* /usr/share/locale/id/LC_MESSAGES/libgsf.mo
* /usr/share/locale/it/LC_MESSAGES/libgsf.mo
* /usr/share/locale/ja/LC_MESSAGES/libgsf.mo
* /usr/share/locale/ka/LC_MESSAGES/libgsf.mo
* /usr/share/locale/ko/LC_MESSAGES/libgsf.mo
* /usr/share/locale/lt/LC_MESSAGES/libgsf.mo
* /usr/share/locale/lv/LC_MESSAGES/libgsf.mo
* /usr/share/locale/ml/LC_MESSAGES/libgsf.mo
* /usr/share/locale/nb/LC_MESSAGES/libgsf.mo
* /usr/share/locale/nl/LC_MESSAGES/libgsf.mo
* /usr/share/locale/nn/LC_MESSAGES/libgsf.mo
* /usr/share/locale/oc/LC_MESSAGES/libgsf.mo
* /usr/share/locale/pa/LC_MESSAGES/libgsf.mo
* /usr/share/locale/pl/LC_MESSAGES/libgsf.mo
* /usr/share/locale/pt/LC_MESSAGES/libgsf.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/libgsf.mo
* /usr/share/locale/ro/LC_MESSAGES/libgsf.mo
* /usr/share/locale/ru/LC_MESSAGES/libgsf.mo
* /usr/share/locale/sk/LC_MESSAGES/libgsf.mo
* /usr/share/locale/sl/LC_MESSAGES/libgsf.mo
* /usr/share/locale/sr/LC_MESSAGES/libgsf.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/libgsf.mo
* /usr/share/locale/sv/LC_MESSAGES/libgsf.mo
* /usr/share/locale/ta/LC_MESSAGES/libgsf.mo
* /usr/share/locale/tg/LC_MESSAGES/libgsf.mo
* /usr/share/locale/th/LC_MESSAGES/libgsf.mo
* /usr/share/locale/tr/LC_MESSAGES/libgsf.mo
* /usr/share/locale/uk/LC_MESSAGES/libgsf.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/libgsf.mo
* /usr/share/locale/zh_HK/LC_MESSAGES/libgsf.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/libgsf.mo
* /usr/share/man/man1/gsf-office-thumbnailer.1.gz
* /usr/share/man/man1/gsf-vba-dump.1.gz
* /usr/share/man/man1/gsf.1.gz
* /usr/share/thumbnailers/gsf-office.thumbnailer
{{< /files >}}