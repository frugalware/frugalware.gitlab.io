+++
draft = false
title = "psmisc 23.6-1"
version = "23.6-1"
description = "Miscellaneous procfs tools"
date = "2022-12-19T10:00:19"
aliases = "/packages/2434"
categories = ['base']
upstreamurl = "https://sourceforge.net/projects/psmisc"
arch = "x86_64"
size = "258664"
usize = "802776"
sha1sum = "0326a20aae802471e793428615a03854d66adf3f"
depends = "['ncurses>=6.1-2']"
reverse_depends = "['dcron', 'scriptlet-core']"
+++
Miscellaneous procfs tools{{< spoiler text="show files" >}}* /usr/bin/fuser
* /usr/bin/killall
* /usr/bin/peekfd
* /usr/bin/prtstat
* /usr/bin/pslog
* /usr/bin/pstree
* /usr/bin/pstree.x11
* /usr/share/doc/psmisc-23.6/AUTHORS
* /usr/share/doc/psmisc-23.6/ChangeLog
* /usr/share/doc/psmisc-23.6/COPYING
* /usr/share/doc/psmisc-23.6/NEWS
* /usr/share/doc/psmisc-23.6/README
* /usr/share/doc/psmisc-23.6/README.md
* /usr/share/locale/bg/LC_MESSAGES/psmisc.mo
* /usr/share/locale/ca/LC_MESSAGES/psmisc.mo
* /usr/share/locale/cs/LC_MESSAGES/psmisc.mo
* /usr/share/locale/da/LC_MESSAGES/psmisc.mo
* /usr/share/locale/de/LC_MESSAGES/psmisc.mo
* /usr/share/locale/el/LC_MESSAGES/psmisc.mo
* /usr/share/locale/eo/LC_MESSAGES/psmisc.mo
* /usr/share/locale/es/LC_MESSAGES/psmisc.mo
* /usr/share/locale/eu/LC_MESSAGES/psmisc.mo
* /usr/share/locale/fi/LC_MESSAGES/psmisc.mo
* /usr/share/locale/fr/LC_MESSAGES/psmisc.mo
* /usr/share/locale/hr/LC_MESSAGES/psmisc.mo
* /usr/share/locale/hu/LC_MESSAGES/psmisc.mo
* /usr/share/locale/id/LC_MESSAGES/psmisc.mo
* /usr/share/locale/it/LC_MESSAGES/psmisc.mo
* /usr/share/locale/ja/LC_MESSAGES/psmisc.mo
* /usr/share/locale/nb/LC_MESSAGES/psmisc.mo
* /usr/share/locale/nl/LC_MESSAGES/psmisc.mo
* /usr/share/locale/pl/LC_MESSAGES/psmisc.mo
* /usr/share/locale/pt/LC_MESSAGES/psmisc.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/psmisc.mo
* /usr/share/locale/ro/LC_MESSAGES/psmisc.mo
* /usr/share/locale/ru/LC_MESSAGES/psmisc.mo
* /usr/share/locale/sr/LC_MESSAGES/psmisc.mo
* /usr/share/locale/sv/LC_MESSAGES/psmisc.mo
* /usr/share/locale/uk/LC_MESSAGES/psmisc.mo
* /usr/share/locale/vi/LC_MESSAGES/psmisc.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/psmisc.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/psmisc.mo
* /usr/share/man/da/man1/prtstat.1.gz
* /usr/share/man/da/man1/pslog.1.gz
* /usr/share/man/de/man1/fuser.1.gz
* /usr/share/man/de/man1/killall.1.gz
* /usr/share/man/de/man1/peekfd.1.gz
* /usr/share/man/de/man1/prtstat.1.gz
* /usr/share/man/de/man1/pslog.1.gz
* /usr/share/man/de/man1/pstree.1.gz
* /usr/share/man/fr/man1/fuser.1.gz
* /usr/share/man/fr/man1/killall.1.gz
* /usr/share/man/fr/man1/peekfd.1.gz
* /usr/share/man/fr/man1/prtstat.1.gz
* /usr/share/man/fr/man1/pslog.1.gz
* /usr/share/man/fr/man1/pstree.1.gz
* /usr/share/man/hr/man1/fuser.1.gz
* /usr/share/man/hr/man1/killall.1.gz
* /usr/share/man/hr/man1/peekfd.1.gz
* /usr/share/man/hr/man1/prtstat.1.gz
* /usr/share/man/hr/man1/pslog.1.gz
* /usr/share/man/hr/man1/pstree.1.gz
* /usr/share/man/ko/man1/fuser.1.gz
* /usr/share/man/ko/man1/killall.1.gz
* /usr/share/man/ko/man1/peekfd.1.gz
* /usr/share/man/ko/man1/prtstat.1.gz
* /usr/share/man/ko/man1/pslog.1.gz
* /usr/share/man/ko/man1/pstree.1.gz
* /usr/share/man/man1/fuser.1.gz
* /usr/share/man/man1/killall.1.gz
* /usr/share/man/man1/peekfd.1.gz
* /usr/share/man/man1/prtstat.1.gz
* /usr/share/man/man1/pslog.1.gz
* /usr/share/man/man1/pstree.1.gz
* /usr/share/man/pt_BR/man1/fuser.1.gz
* /usr/share/man/pt_BR/man1/killall.1.gz
* /usr/share/man/pt_BR/man1/peekfd.1.gz
* /usr/share/man/pt_BR/man1/prtstat.1.gz
* /usr/share/man/pt_BR/man1/pslog.1.gz
* /usr/share/man/pt_BR/man1/pstree.1.gz
* /usr/share/man/ro/man1/fuser.1.gz
* /usr/share/man/ro/man1/killall.1.gz
* /usr/share/man/ro/man1/peekfd.1.gz
* /usr/share/man/ro/man1/prtstat.1.gz
* /usr/share/man/ro/man1/pslog.1.gz
* /usr/share/man/ro/man1/pstree.1.gz
* /usr/share/man/ru/man1/fuser.1.gz
* /usr/share/man/ru/man1/killall.1.gz
* /usr/share/man/ru/man1/peekfd.1.gz
* /usr/share/man/ru/man1/prtstat.1.gz
* /usr/share/man/ru/man1/pslog.1.gz
* /usr/share/man/ru/man1/pstree.1.gz
* /usr/share/man/sr/man1/fuser.1.gz
* /usr/share/man/sr/man1/killall.1.gz
* /usr/share/man/sr/man1/peekfd.1.gz
* /usr/share/man/sr/man1/prtstat.1.gz
* /usr/share/man/sr/man1/pslog.1.gz
* /usr/share/man/sr/man1/pstree.1.gz
* /usr/share/man/sv/man1/fuser.1.gz
* /usr/share/man/sv/man1/killall.1.gz
* /usr/share/man/sv/man1/peekfd.1.gz
* /usr/share/man/sv/man1/prtstat.1.gz
* /usr/share/man/sv/man1/pslog.1.gz
* /usr/share/man/sv/man1/pstree.1.gz
* /usr/share/man/uk/man1/fuser.1.gz
* /usr/share/man/uk/man1/killall.1.gz
* /usr/share/man/uk/man1/peekfd.1.gz
* /usr/share/man/uk/man1/prtstat.1.gz
* /usr/share/man/uk/man1/pslog.1.gz
* /usr/share/man/uk/man1/pstree.1.gz
{{< /spoiler >}}