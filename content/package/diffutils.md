+++
draft = false
title = "diffutils 3.10-1"
version = "3.10-1"
date = "2023-05-22T14:29:30"
categories = ['base', 'devel-core']
upstreamurl = "http://www.gnu.org/software/diffutils"
arch = "x86_64"
size = "1846103"
usize = "0"
sha1sum = ""
depends = "['glibc>=2.35', 'bash>=4.3_042-5']"
files = "['usr/', 'usr/bin/', 'usr/bin/cmp', 'usr/bin/diff', 'usr/bin/diff3', 'usr/bin/sdiff', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/diffutils-3.10/', 'usr/share/doc/diffutils-3.10/AUTHORS', 'usr/share/doc/diffutils-3.10/COPYING', 'usr/share/doc/diffutils-3.10/ChangeLog', 'usr/share/doc/diffutils-3.10/INSTALL', 'usr/share/doc/diffutils-3.10/NEWS', 'usr/share/doc/diffutils-3.10/README', 'usr/share/doc/diffutils-3.10/THANKS', 'usr/share/doc/diffutils-3.10/TODO', 'usr/share/info/', 'usr/share/info/diffutils.info.gz', 'usr/share/locale/', 'usr/share/locale/bg/', 'usr/share/locale/bg/LC_MESSAGES/', 'usr/share/locale/bg/LC_MESSAGES/diffutils.mo', 'usr/share/locale/ca/', 'usr/share/locale/ca/LC_MESSAGES/', 'usr/share/locale/ca/LC_MESSAGES/diffutils.mo', 'usr/share/locale/cs/', 'usr/share/locale/cs/LC_MESSAGES/', 'usr/share/locale/cs/LC_MESSAGES/diffutils.mo', 'usr/share/locale/da/', 'usr/share/locale/da/LC_MESSAGES/', 'usr/share/locale/da/LC_MESSAGES/diffutils.mo', 'usr/share/locale/de/', 'usr/share/locale/de/LC_MESSAGES/', 'usr/share/locale/de/LC_MESSAGES/diffutils.mo', 'usr/share/locale/el/', 'usr/share/locale/el/LC_MESSAGES/', 'usr/share/locale/el/LC_MESSAGES/diffutils.mo', 'usr/share/locale/eo/', 'usr/share/locale/eo/LC_MESSAGES/', 'usr/share/locale/eo/LC_MESSAGES/diffutils.mo', 'usr/share/locale/es/', 'usr/share/locale/es/LC_MESSAGES/', 'usr/share/locale/es/LC_MESSAGES/diffutils.mo', 'usr/share/locale/fi/', 'usr/share/locale/fi/LC_MESSAGES/', 'usr/share/locale/fi/LC_MESSAGES/diffutils.mo', 'usr/share/locale/fr/', 'usr/share/locale/fr/LC_MESSAGES/', 'usr/share/locale/fr/LC_MESSAGES/diffutils.mo', 'usr/share/locale/ga/', 'usr/share/locale/ga/LC_MESSAGES/', 'usr/share/locale/ga/LC_MESSAGES/diffutils.mo', 'usr/share/locale/gl/', 'usr/share/locale/gl/LC_MESSAGES/', 'usr/share/locale/gl/LC_MESSAGES/diffutils.mo', 'usr/share/locale/he/', 'usr/share/locale/he/LC_MESSAGES/', 'usr/share/locale/he/LC_MESSAGES/diffutils.mo', 'usr/share/locale/hr/', 'usr/share/locale/hr/LC_MESSAGES/', 'usr/share/locale/hr/LC_MESSAGES/diffutils.mo', 'usr/share/locale/hu/', 'usr/share/locale/hu/LC_MESSAGES/', 'usr/share/locale/hu/LC_MESSAGES/diffutils.mo', 'usr/share/locale/id/', 'usr/share/locale/id/LC_MESSAGES/', 'usr/share/locale/id/LC_MESSAGES/diffutils.mo', 'usr/share/locale/it/', 'usr/share/locale/it/LC_MESSAGES/', 'usr/share/locale/it/LC_MESSAGES/diffutils.mo', 'usr/share/locale/ja/', 'usr/share/locale/ja/LC_MESSAGES/', 'usr/share/locale/ja/LC_MESSAGES/diffutils.mo', 'usr/share/locale/ka/', 'usr/share/locale/ka/LC_MESSAGES/', 'usr/share/locale/ka/LC_MESSAGES/diffutils.mo', 'usr/share/locale/ko/', 'usr/share/locale/ko/LC_MESSAGES/', 'usr/share/locale/ko/LC_MESSAGES/diffutils.mo', 'usr/share/locale/lv/', 'usr/share/locale/lv/LC_MESSAGES/', 'usr/share/locale/lv/LC_MESSAGES/diffutils.mo', 'usr/share/locale/ms/', 'usr/share/locale/ms/LC_MESSAGES/', 'usr/share/locale/ms/LC_MESSAGES/diffutils.mo', 'usr/share/locale/nb/', 'usr/share/locale/nb/LC_MESSAGES/', 'usr/share/locale/nb/LC_MESSAGES/diffutils.mo', 'usr/share/locale/nl/', 'usr/share/locale/nl/LC_MESSAGES/', 'usr/share/locale/nl/LC_MESSAGES/diffutils.mo', 'usr/share/locale/pl/', 'usr/share/locale/pl/LC_MESSAGES/', 'usr/share/locale/pl/LC_MESSAGES/diffutils.mo', 'usr/share/locale/pt/', 'usr/share/locale/pt/LC_MESSAGES/', 'usr/share/locale/pt/LC_MESSAGES/diffutils.mo', 'usr/share/locale/pt_BR/', 'usr/share/locale/pt_BR/LC_MESSAGES/', 'usr/share/locale/pt_BR/LC_MESSAGES/diffutils.mo', 'usr/share/locale/ro/', 'usr/share/locale/ro/LC_MESSAGES/', 'usr/share/locale/ro/LC_MESSAGES/diffutils.mo', 'usr/share/locale/ru/', 'usr/share/locale/ru/LC_MESSAGES/', 'usr/share/locale/ru/LC_MESSAGES/diffutils.mo', 'usr/share/locale/sr/', 'usr/share/locale/sr/LC_MESSAGES/', 'usr/share/locale/sr/LC_MESSAGES/diffutils.mo', 'usr/share/locale/sv/', 'usr/share/locale/sv/LC_MESSAGES/', 'usr/share/locale/sv/LC_MESSAGES/diffutils.mo', 'usr/share/locale/tr/', 'usr/share/locale/tr/LC_MESSAGES/', 'usr/share/locale/tr/LC_MESSAGES/diffutils.mo', 'usr/share/locale/uk/', 'usr/share/locale/uk/LC_MESSAGES/', 'usr/share/locale/uk/LC_MESSAGES/diffutils.mo', 'usr/share/locale/vi/', 'usr/share/locale/vi/LC_MESSAGES/', 'usr/share/locale/vi/LC_MESSAGES/diffutils.mo', 'usr/share/locale/zh_CN/', 'usr/share/locale/zh_CN/LC_MESSAGES/', 'usr/share/locale/zh_CN/LC_MESSAGES/diffutils.mo', 'usr/share/locale/zh_TW/', 'usr/share/locale/zh_TW/LC_MESSAGES/', 'usr/share/locale/zh_TW/LC_MESSAGES/diffutils.mo', 'usr/share/man/', 'usr/share/man/man1/', 'usr/share/man/man1/cmp.1.gz', 'usr/share/man/man1/diff.1.gz', 'usr/share/man/man1/diff3.1.gz', 'usr/share/man/man1/sdiff.1.gz']"
+++
Utility programs used for creating patch files