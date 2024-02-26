+++
draft = false
title = "sysstat 12.7.5-1"
version = "12.7.5-1"
description = "A collection of performance monitoring tools for Linux"
date = "2024-01-15T19:55:31"
aliases = "/packages/218626"
categories = ['base-extra']
upstreamurl = "http://sebastien.godard.pagesperso-orange.fr/"
arch = "x86_64"
size = "426952"
usize = "1682241"
sha1sum = "749d48623754db78d18ceebc844e982f63361783"
depends = "['lmsensors>=3.5.0']"
reverse_depends = "['lumina-desktop']"
+++
A collection of performance monitoring tools for Linux

{{< files text="show files" >}}* /etc/sysconfig/sysstat
* /etc/sysconfig/sysstat.ioconf
* /usr/bin/cifsiostat
* /usr/bin/iostat
* /usr/bin/mpstat
* /usr/bin/pidstat
* /usr/bin/sadf
* /usr/bin/sar
* /usr/bin/tapestat
* /usr/lib/sa/sa1
* /usr/lib/sa/sa2
* /usr/lib/sa/sadc
* /usr/lib/systemd/system-sleep/sysstat.sleep
* /usr/lib/systemd/system/sysstat-collect.service
* /usr/lib/systemd/system/sysstat-collect.timer
* /usr/lib/systemd/system/sysstat-rotate.service
* /usr/lib/systemd/system/sysstat-rotate.timer
* /usr/lib/systemd/system/sysstat-summary.service
* /usr/lib/systemd/system/sysstat-summary.timer
* /usr/lib/systemd/system/sysstat.service
* /usr/share/doc/sysstat-12.7.5/CHANGES
* /usr/share/doc/sysstat-12.7.5/COPYING
* /usr/share/doc/sysstat-12.7.5/CREDITS
* /usr/share/doc/sysstat-12.7.5/FAQ.md
* /usr/share/doc/sysstat-12.7.5/INSTALL
* /usr/share/doc/sysstat-12.7.5/README.md
* /usr/share/locale/af/LC_MESSAGES/sysstat.mo
* /usr/share/locale/be/LC_MESSAGES/sysstat.mo
* /usr/share/locale/cs/LC_MESSAGES/sysstat.mo
* /usr/share/locale/da/LC_MESSAGES/sysstat.mo
* /usr/share/locale/de/LC_MESSAGES/sysstat.mo
* /usr/share/locale/eo/LC_MESSAGES/sysstat.mo
* /usr/share/locale/es/LC_MESSAGES/sysstat.mo
* /usr/share/locale/eu/LC_MESSAGES/sysstat.mo
* /usr/share/locale/fi/LC_MESSAGES/sysstat.mo
* /usr/share/locale/fr/LC_MESSAGES/sysstat.mo
* /usr/share/locale/fur/LC_MESSAGES/sysstat.mo
* /usr/share/locale/gl/LC_MESSAGES/sysstat.mo
* /usr/share/locale/hr/LC_MESSAGES/sysstat.mo
* /usr/share/locale/hu/LC_MESSAGES/sysstat.mo
* /usr/share/locale/id/LC_MESSAGES/sysstat.mo
* /usr/share/locale/it/LC_MESSAGES/sysstat.mo
* /usr/share/locale/ja/LC_MESSAGES/sysstat.mo
* /usr/share/locale/ka/LC_MESSAGES/sysstat.mo
* /usr/share/locale/ko/LC_MESSAGES/sysstat.mo
* /usr/share/locale/ky/LC_MESSAGES/sysstat.mo
* /usr/share/locale/lv/LC_MESSAGES/sysstat.mo
* /usr/share/locale/mt/LC_MESSAGES/sysstat.mo
* /usr/share/locale/nb/LC_MESSAGES/sysstat.mo
* /usr/share/locale/nl/LC_MESSAGES/sysstat.mo
* /usr/share/locale/nn/LC_MESSAGES/sysstat.mo
* /usr/share/locale/pl/LC_MESSAGES/sysstat.mo
* /usr/share/locale/pt/LC_MESSAGES/sysstat.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/sysstat.mo
* /usr/share/locale/ro/LC_MESSAGES/sysstat.mo
* /usr/share/locale/ru/LC_MESSAGES/sysstat.mo
* /usr/share/locale/sk/LC_MESSAGES/sysstat.mo
* /usr/share/locale/sr/LC_MESSAGES/sysstat.mo
* /usr/share/locale/sv/LC_MESSAGES/sysstat.mo
* /usr/share/locale/tr/LC_MESSAGES/sysstat.mo
* /usr/share/locale/uk/LC_MESSAGES/sysstat.mo
* /usr/share/locale/vi/LC_MESSAGES/sysstat.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/sysstat.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/sysstat.mo
* /usr/share/man/man1/cifsiostat.1.xz.gz
* /usr/share/man/man1/iostat.1.xz.gz
* /usr/share/man/man1/mpstat.1.xz.gz
* /usr/share/man/man1/pidstat.1.xz.gz
* /usr/share/man/man1/sadf.1.xz.gz
* /usr/share/man/man1/sar.1.xz.gz
* /usr/share/man/man1/tapestat.1.xz.gz
* /usr/share/man/man5/sysstat.5.xz.gz
* /usr/share/man/man8/sa1.8.xz.gz
* /usr/share/man/man8/sa2.8.xz.gz
* /usr/share/man/man8/sadc.8.xz.gz
{{< /files >}}