+++
draft = false
title = "aspell 0.60.8.1-1"
version = "0.60.8.1-1"
description = "A spell checker designed to eventually replace Ispell"
date = "2024-01-23T14:35:24"
aliases = "/packages/2919"
categories = ['apps']
upstreamurl = "http://aspell.net/"
arch = "x86_64"
size = "647884"
usize = "3527142"
sha1sum = "3dc93e73a151d6f3e23625cb70da7e73b010d09a"
depends = "['libstdc++>=11.2', 'ncurses>=6.0-18']"
reverse_depends = "['aspell-bg', 'aspell-ca', 'aspell-cs', 'aspell-da', 'aspell-de', 'aspell-en', 'aspell-fo', 'aspell-ga', 'aspell-gd', 'aspell-id', 'aspell-it', 'aspell-ru', 'aspell-tn', 'aspell6-de', 'aspell6-de-alt', 'aspell6-en', 'eiskaltdc', 'enchant', 'gtkspell', 'lyx', 'mcabber', 'sonnet-plugin-aspell']"
+++
A spell checker designed to eventually replace Ispell{{< files text="show files" >}}* /etc/aspell/aspell.conf
* /usr/bin/aspell
* /usr/bin/aspell-import
* /usr/bin/ispell
* /usr/bin/precat
* /usr/bin/preunzip
* /usr/bin/prezip
* /usr/bin/prezip-bin
* /usr/bin/pspell-config
* /usr/bin/run-with-aspell
* /usr/bin/word-list-compress
* /usr/include/aspell.h
* /usr/include/pspell/pspell.h
* /usr/lib/aspell-0.60/ccpp.amf
* /usr/lib/aspell-0.60/comment.amf
* /usr/lib/aspell-0.60/context-filter.info
* /usr/lib/aspell-0.60/context-filter.so
* /usr/lib/aspell-0.60/cp1250.cmap
* /usr/lib/aspell-0.60/cp1250.cset
* /usr/lib/aspell-0.60/cp1251.cmap
* /usr/lib/aspell-0.60/cp1251.cset
* /usr/lib/aspell-0.60/cp1252.cmap
* /usr/lib/aspell-0.60/cp1252.cset
* /usr/lib/aspell-0.60/cp1253.cmap
* /usr/lib/aspell-0.60/cp1253.cset
* /usr/lib/aspell-0.60/cp1254.cmap
* /usr/lib/aspell-0.60/cp1254.cset
* /usr/lib/aspell-0.60/cp1255.cmap
* /usr/lib/aspell-0.60/cp1255.cset
* /usr/lib/aspell-0.60/cp1256.cmap
* /usr/lib/aspell-0.60/cp1256.cset
* /usr/lib/aspell-0.60/cp1257.cmap
* /usr/lib/aspell-0.60/cp1257.cset
* /usr/lib/aspell-0.60/cp1258.cmap
* /usr/lib/aspell-0.60/cp1258.cset
* /usr/lib/aspell-0.60/dvorak.kbd
* /usr/lib/aspell-0.60/email-filter.info
* /usr/lib/aspell-0.60/email-filter.so
* /usr/lib/aspell-0.60/email.amf
* /usr/lib/aspell-0.60/html-filter.info
* /usr/lib/aspell-0.60/html.amf
* /usr/lib/aspell-0.60/iso-8859-1.cmap
* /usr/lib/aspell-0.60/iso-8859-1.cset
* /usr/lib/aspell-0.60/iso-8859-10.cmap
* /usr/lib/aspell-0.60/iso-8859-10.cset
* /usr/lib/aspell-0.60/iso-8859-11.cmap
* /usr/lib/aspell-0.60/iso-8859-11.cset
* /usr/lib/aspell-0.60/iso-8859-13.cmap
* /usr/lib/aspell-0.60/iso-8859-13.cset
* /usr/lib/aspell-0.60/iso-8859-14.cmap
* /usr/lib/aspell-0.60/iso-8859-14.cset
* /usr/lib/aspell-0.60/iso-8859-15.cmap
* /usr/lib/aspell-0.60/iso-8859-15.cset
* /usr/lib/aspell-0.60/iso-8859-16.cmap
* /usr/lib/aspell-0.60/iso-8859-16.cset
* /usr/lib/aspell-0.60/iso-8859-2.cmap
* /usr/lib/aspell-0.60/iso-8859-2.cset
* /usr/lib/aspell-0.60/iso-8859-3.cmap
* /usr/lib/aspell-0.60/iso-8859-3.cset
* /usr/lib/aspell-0.60/iso-8859-4.cmap
* /usr/lib/aspell-0.60/iso-8859-4.cset
* /usr/lib/aspell-0.60/iso-8859-5.cmap
* /usr/lib/aspell-0.60/iso-8859-5.cset
* /usr/lib/aspell-0.60/iso-8859-6.cmap
* /usr/lib/aspell-0.60/iso-8859-6.cset
* /usr/lib/aspell-0.60/iso-8859-7.cmap
* /usr/lib/aspell-0.60/iso-8859-7.cset
* /usr/lib/aspell-0.60/iso-8859-8.cmap
* /usr/lib/aspell-0.60/iso-8859-8.cset
* /usr/lib/aspell-0.60/iso-8859-9.cmap
* /usr/lib/aspell-0.60/iso-8859-9.cset
* /usr/lib/aspell-0.60/ispell
* /usr/lib/aspell-0.60/koi8-r.cmap
* /usr/lib/aspell-0.60/koi8-r.cset
* /usr/lib/aspell-0.60/koi8-u.cmap
* /usr/lib/aspell-0.60/koi8-u.cset
* /usr/lib/aspell-0.60/markdown-filter.info
* /usr/lib/aspell-0.60/markdown-filter.so
* /usr/lib/aspell-0.60/markdown.amf
* /usr/lib/aspell-0.60/none.amf
* /usr/lib/aspell-0.60/nroff-filter.info
* /usr/lib/aspell-0.60/nroff-filter.so
* /usr/lib/aspell-0.60/nroff.amf
* /usr/lib/aspell-0.60/perl.amf
* /usr/lib/aspell-0.60/sgml-filter.info
* /usr/lib/aspell-0.60/sgml-filter.so
* /usr/lib/aspell-0.60/sgml.amf
* /usr/lib/aspell-0.60/spell
* /usr/lib/aspell-0.60/split.kbd
* /usr/lib/aspell-0.60/standard.kbd
* /usr/lib/aspell-0.60/tex-filter.info
* /usr/lib/aspell-0.60/tex-filter.so
* /usr/lib/aspell-0.60/tex.amf
* /usr/lib/aspell-0.60/texinfo-filter.info
* /usr/lib/aspell-0.60/texinfo-filter.so
* /usr/lib/aspell-0.60/texinfo.amf
* /usr/lib/aspell-0.60/url.amf
* /usr/lib/libaspell.so
* /usr/lib/libaspell.so.15
* /usr/lib/libaspell.so.15.3.1
* /usr/lib/libpspell.so
* /usr/lib/libpspell.so.15
* /usr/lib/libpspell.so.15.3.1
* /usr/share/doc/aspell-0.60.8.1/COPYING
* /usr/share/doc/aspell-0.60.8.1/README
* /usr/share/doc/aspell-0.60.8.1/TODO
* /usr/share/info/aspell-dev.info.gz
* /usr/share/info/aspell.info.gz
* /usr/share/locale/ast/LC_MESSAGES/aspell.mo
* /usr/share/locale/be/LC_MESSAGES/aspell.mo
* /usr/share/locale/ca/LC_MESSAGES/aspell.mo
* /usr/share/locale/cs/LC_MESSAGES/aspell.mo
* /usr/share/locale/da/LC_MESSAGES/aspell.mo
* /usr/share/locale/de/LC_MESSAGES/aspell.mo
* /usr/share/locale/en_GB/LC_MESSAGES/aspell.mo
* /usr/share/locale/eo/LC_MESSAGES/aspell.mo
* /usr/share/locale/es/LC_MESSAGES/aspell.mo
* /usr/share/locale/fi/LC_MESSAGES/aspell.mo
* /usr/share/locale/fr/LC_MESSAGES/aspell.mo
* /usr/share/locale/fur/LC_MESSAGES/aspell.mo
* /usr/share/locale/ga/LC_MESSAGES/aspell.mo
* /usr/share/locale/hr/LC_MESSAGES/aspell.mo
* /usr/share/locale/hu/LC_MESSAGES/aspell.mo
* /usr/share/locale/id/LC_MESSAGES/aspell.mo
* /usr/share/locale/it/LC_MESSAGES/aspell.mo
* /usr/share/locale/ja/LC_MESSAGES/aspell.mo
* /usr/share/locale/ka/LC_MESSAGES/aspell.mo
* /usr/share/locale/mn/LC_MESSAGES/aspell.mo
* /usr/share/locale/ms/LC_MESSAGES/aspell.mo
* /usr/share/locale/nl/LC_MESSAGES/aspell.mo
* /usr/share/locale/pl/LC_MESSAGES/aspell.mo
* /usr/share/locale/pt/LC_MESSAGES/aspell.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/aspell.mo
* /usr/share/locale/ro/LC_MESSAGES/aspell.mo
* /usr/share/locale/ru/LC_MESSAGES/aspell.mo
* /usr/share/locale/rw/LC_MESSAGES/aspell.mo
* /usr/share/locale/sk/LC_MESSAGES/aspell.mo
* /usr/share/locale/sl/LC_MESSAGES/aspell.mo
* /usr/share/locale/sq/LC_MESSAGES/aspell.mo
* /usr/share/locale/sr/LC_MESSAGES/aspell.mo
* /usr/share/locale/sv/LC_MESSAGES/aspell.mo
* /usr/share/locale/tg/LC_MESSAGES/aspell.mo
* /usr/share/locale/uk/LC_MESSAGES/aspell.mo
* /usr/share/locale/vi/LC_MESSAGES/aspell.mo
* /usr/share/locale/wa/LC_MESSAGES/aspell.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/aspell.mo
* /usr/share/man/man1/aspell-import.1.gz
* /usr/share/man/man1/aspell.1.gz
* /usr/share/man/man1/prezip-bin.1.gz
* /usr/share/man/man1/pspell-config.1.gz
* /usr/share/man/man1/run-with-aspell.1.gz
* /usr/share/man/man1/word-list-compress.1.gz
{{< /files >}}