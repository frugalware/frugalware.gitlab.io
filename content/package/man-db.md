+++
draft = false
title = "man-db 2.12.0-3"
version = "2.12.0-3"
description = "A utility for reading man pages"
date = "2024-01-02T12:17:58"
aliases = "/packages/118506"
categories = ['base']
upstreamurl = "http://www.nongnu.org/man-db/"
arch = "x86_64"
size = "498012"
usize = "2149167"
sha1sum = "1ef8c0ee534f20c53a0f3f447ecfcff3b96b2beb"
depends = "['gdbm>=1.15', 'groff>=1.22.3-4', 'less>=481-4', 'libpipeline>=1.4.1-5', 'zlib>=1.2.12']"
reverse_depends = "['man2html']"
+++
A utility for reading man pages

{{< files text="show files" >}}* /etc/cron.daily/man-db
* /etc/man_db.conf
* /etc/profile.d/man-colors.sh
* /etc/profile.d/man.sh
* /usr/bin/accessdb
* /usr/bin/apropos
* /usr/bin/catman
* /usr/bin/convert-mans
* /usr/bin/lexgrog
* /usr/bin/man
* /usr/bin/man-recode
* /usr/bin/mandb
* /usr/bin/manpath
* /usr/bin/whatis
* /usr/lib/man-db/globbing
* /usr/lib/man-db/libman-2.12.0.so
* /usr/lib/man-db/libman.so
* /usr/lib/man-db/libmandb-2.12.0.so
* /usr/lib/man-db/libmandb.so
* /usr/lib/man-db/manconv
* /usr/lib/man-db/zsoelim
* /usr/lib/systemd/system/man-db.service
* /usr/lib/systemd/system/man-db.timer
* /usr/lib/sysusers.d/man-db.conf
* /usr/lib/tmpfiles.d/man-db.conf
* /usr/share/doc/man-db-2.12.0/ChangeLog
* /usr/share/doc/man-db-2.12.0/COPYING
* /usr/share/doc/man-db-2.12.0/FAQ
* /usr/share/doc/man-db-2.12.0/man-db-manual.ps
* /usr/share/doc/man-db-2.12.0/man-db-manual.txt
* /usr/share/doc/man-db-2.12.0/README.Frugalware
* /usr/share/doc/man-db-2.12.0/README.md
* /usr/share/locale/af/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/ast/LC_MESSAGES/man-db.mo
* /usr/share/locale/be/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/bg/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/ca/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/ca/LC_MESSAGES/man-db.mo
* /usr/share/locale/cs/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/cs/LC_MESSAGES/man-db.mo
* /usr/share/locale/da/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/da/LC_MESSAGES/man-db.mo
* /usr/share/locale/de/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/de/LC_MESSAGES/man-db.mo
* /usr/share/locale/el/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/eo/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/eo/LC_MESSAGES/man-db.mo
* /usr/share/locale/es/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/es/LC_MESSAGES/man-db.mo
* /usr/share/locale/et/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/eu/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/fi/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/fi/LC_MESSAGES/man-db.mo
* /usr/share/locale/fr/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/fr/LC_MESSAGES/man-db.mo
* /usr/share/locale/ga/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/gl/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/hu/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/id/LC_MESSAGES/man-db.mo
* /usr/share/locale/it/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/it/LC_MESSAGES/man-db.mo
* /usr/share/locale/ja/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/ja/LC_MESSAGES/man-db.mo
* /usr/share/locale/ka/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/ka/LC_MESSAGES/man-db.mo
* /usr/share/locale/ko/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/ko/LC_MESSAGES/man-db.mo
* /usr/share/locale/ms/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/nb/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/nl/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/nl/LC_MESSAGES/man-db.mo
* /usr/share/locale/pl/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/pl/LC_MESSAGES/man-db.mo
* /usr/share/locale/pt/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/pt/LC_MESSAGES/man-db.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/man-db.mo
* /usr/share/locale/ro/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/ro/LC_MESSAGES/man-db.mo
* /usr/share/locale/ru/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/ru/LC_MESSAGES/man-db.mo
* /usr/share/locale/rw/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/sk/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/sl/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/sr/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/sr/LC_MESSAGES/man-db.mo
* /usr/share/locale/sv/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/sv/LC_MESSAGES/man-db.mo
* /usr/share/locale/tr/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/tr/LC_MESSAGES/man-db.mo
* /usr/share/locale/uk/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/vi/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/vi/LC_MESSAGES/man-db.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/man-db.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/man-db-gnulib.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/man-db.mo
* /usr/share/man/it/man1/apropos.1.gz
* /usr/share/man/it/man1/man.1.gz
* /usr/share/man/it/man1/manpath.1.gz
* /usr/share/man/it/man1/whatis.1.gz
* /usr/share/man/it/man1/zsoelim.1.gz
* /usr/share/man/it/man5/manpath.5.gz
* /usr/share/man/it/man8/accessdb.8.gz
* /usr/share/man/it/man8/catman.8.gz
* /usr/share/man/it/man8/mandb.8.gz
* /usr/share/man/man1/apropos.1.gz
* /usr/share/man/man1/lexgrog.1.gz
* /usr/share/man/man1/man-recode.1.gz
* /usr/share/man/man1/man.1.gz
* /usr/share/man/man1/manconv.1.gz
* /usr/share/man/man1/manpath.1.gz
* /usr/share/man/man1/whatis.1.gz
* /usr/share/man/man1/zsoelim.1.gz
* /usr/share/man/man5/manpath.5.gz
* /usr/share/man/man8/accessdb.8.gz
* /usr/share/man/man8/catman.8.gz
* /usr/share/man/man8/mandb.8.gz
{{< /files >}}