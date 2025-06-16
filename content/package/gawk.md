+++
draft = false
title = "gawk 5.3.2-1"
version = "5.3.2-1"
description = "Gnu version of awk"
date = "2025-04-02T11:49:00"
aliases = "/packages/2378"
categories = ['base']
upstreamurl = "http://www.gnu.org/software/gawk/"
arch = "x86_64"
size = "1489148"
usize = "3881746"
sha1sum = "787f2f8d14f5b14a769035b01562d064635d1ed0"
depends = "['mpfr>=4.0.2-3', 'ncurses>=6.1', 'readline>=8.0-3']"
reverse_depends = "['autoconf', 'backupninja', 'go', 'inxi', 'parted', 'prettyping', 'quilt', 'texinfo']"
+++
### Description: 
Gnu version of awk

### Files: 
* /etc/profile.d/gawk.csh
* /etc/profile.d/gawk.sh
* /usr/bin/awk
* /usr/bin/gawk
* /usr/bin/gawk-5.3.2
* /usr/bin/gawkbug
* /usr/include/gawkapi.h
* /usr/lib/gawk/awk/grcat
* /usr/lib/gawk/awk/pwcat
* /usr/lib/gawk/filefuncs.so
* /usr/lib/gawk/fnmatch.so
* /usr/lib/gawk/fork.so
* /usr/lib/gawk/inplace.so
* /usr/lib/gawk/intdiv.so
* /usr/lib/gawk/ordchr.so
* /usr/lib/gawk/readdir.so
* /usr/lib/gawk/readfile.so
* /usr/lib/gawk/revoutput.so
* /usr/lib/gawk/revtwoway.so
* /usr/lib/gawk/rwarray.so
* /usr/lib/gawk/time.so
* /usr/share/awk/assert.awk
* /usr/share/awk/bits2str.awk
* /usr/share/awk/cliff_rand.awk
* /usr/share/awk/ctime.awk
* /usr/share/awk/ftrans.awk
* /usr/share/awk/getopt.awk
* /usr/share/awk/gettime.awk
* /usr/share/awk/group.awk
* /usr/share/awk/have_mpfr.awk
* /usr/share/awk/inplace.awk
* /usr/share/awk/intdiv0.awk
* /usr/share/awk/isnumeric.awk
* /usr/share/awk/join.awk
* /usr/share/awk/libintl.awk
* /usr/share/awk/noassign.awk
* /usr/share/awk/ns_passwd.awk
* /usr/share/awk/ord.awk
* /usr/share/awk/passwd.awk
* /usr/share/awk/processarray.awk
* /usr/share/awk/quicksort.awk
* /usr/share/awk/readable.awk
* /usr/share/awk/readfile.awk
* /usr/share/awk/rewind.awk
* /usr/share/awk/round.awk
* /usr/share/awk/shellquote.awk
* /usr/share/awk/strtonum.awk
* /usr/share/awk/tocsv.awk
* /usr/share/awk/walkarray.awk
* /usr/share/awk/zerofile.awk
* /usr/share/doc/gawk-5.3.2/AUTHORS
* /usr/share/doc/gawk-5.3.2/ChangeLog
* /usr/share/doc/gawk-5.3.2/COPYING
* /usr/share/doc/gawk-5.3.2/INSTALL
* /usr/share/doc/gawk-5.3.2/NEWS
* /usr/share/doc/gawk-5.3.2/README
* /usr/share/doc/gawk-5.3.2/TODO
* /usr/share/info/gawk.info.gz
* /usr/share/info/gawkinet.info.gz
* /usr/share/info/gawkworkflow.info.gz
* /usr/share/info/gawk_api-figure1.png.gz
* /usr/share/info/gawk_api-figure2.png.gz
* /usr/share/info/gawk_api-figure3.png.gz
* /usr/share/info/gawk_array-elements.png.gz
* /usr/share/info/gawk_general-program.png.gz
* /usr/share/info/gawk_process-flow.png.gz
* /usr/share/info/gawk_statist.jpg.gz
* /usr/share/info/pm-gawk.info.gz
* /usr/share/locale/bg/LC_MESSAGES/gawk.mo
* /usr/share/locale/ca/LC_MESSAGES/gawk.mo
* /usr/share/locale/da/LC_MESSAGES/gawk.mo
* /usr/share/locale/de/LC_MESSAGES/gawk.mo
* /usr/share/locale/es/LC_MESSAGES/gawk.mo
* /usr/share/locale/fi/LC_MESSAGES/gawk.mo
* /usr/share/locale/fr/LC_MESSAGES/gawk.mo
* /usr/share/locale/id/LC_MESSAGES/gawk.mo
* /usr/share/locale/it/LC_MESSAGES/gawk.mo
* /usr/share/locale/ja/LC_MESSAGES/gawk.mo
* /usr/share/locale/ka/LC_MESSAGES/gawk.mo
* /usr/share/locale/ko/LC_MESSAGES/gawk.mo
* /usr/share/locale/ms/LC_MESSAGES/gawk.mo
* /usr/share/locale/nl/LC_MESSAGES/gawk.mo
* /usr/share/locale/pl/LC_MESSAGES/gawk.mo
* /usr/share/locale/pt/LC_MESSAGES/gawk.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/gawk.mo
* /usr/share/locale/ro/LC_MESSAGES/gawk.mo
* /usr/share/locale/sr/LC_MESSAGES/gawk.mo
* /usr/share/locale/sv/LC_MESSAGES/gawk.mo
* /usr/share/locale/tr/LC_MESSAGES/gawk.mo
* /usr/share/locale/uk/LC_MESSAGES/gawk.mo
* /usr/share/locale/vi/LC_MESSAGES/gawk.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/gawk.mo
* /usr/share/man/man1/gawk.1.gz
* /usr/share/man/man1/gawkbug.1.gz
* /usr/share/man/man1/pm-gawk.1.gz
* /usr/share/man/man3/filefuncs.3am.gz
* /usr/share/man/man3/fnmatch.3am.gz
* /usr/share/man/man3/fork.3am.gz
* /usr/share/man/man3/inplace.3am.gz
* /usr/share/man/man3/ordchr.3am.gz
* /usr/share/man/man3/readdir.3am.gz
* /usr/share/man/man3/readfile.3am.gz
* /usr/share/man/man3/revoutput.3am.gz
* /usr/share/man/man3/revtwoway.3am.gz
* /usr/share/man/man3/rwarray.3am.gz
* /usr/share/man/man3/time.3am.gz
