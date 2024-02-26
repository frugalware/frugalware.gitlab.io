+++
draft = false
title = "libpwquality 1.4.5-3"
version = "1.4.5-3"
description = "A library for password generation and password quality checking"
date = "2024-01-08T08:17:22"
aliases = "/packages/168886"
categories = ['lib']
upstreamurl = "https://github.com/libpwquality/libpwquality"
arch = "x86_64"
size = "93452"
usize = "473853"
sha1sum = "4455d6b2fa2023944d3386265341cc539abcb954"
depends = "['cracklib>=2.9.5-6', 'pam>=1.1.8-4', 'python3']"
reverse_depends = "['calamares-frugalware', 'seahorse', 'zulucrypt']"
+++
A library for password generation and password quality checking"

{{< files text="show files" >}}* /etc/security/pwquality.conf
* /usr/bin/pwmake
* /usr/bin/pwscore
* /usr/include/pwquality.h
* /usr/lib/libpwquality.so
* /usr/lib/libpwquality.so.1
* /usr/lib/libpwquality.so.1.0.2
* /usr/lib/pkgconfig/pwquality.pc
* /usr/lib/python3.12/site-packages/pwquality-1.4.5-py3.12-linux-x86_64.egg/EGG-INFO/dependency_links.txt
* /usr/lib/python3.12/site-packages/pwquality-1.4.5-py3.12-linux-x86_64.egg/EGG-INFO/native_libs.txt
* /usr/lib/python3.12/site-packages/pwquality-1.4.5-py3.12-linux-x86_64.egg/EGG-INFO/not-zip-safe
* /usr/lib/python3.12/site-packages/pwquality-1.4.5-py3.12-linux-x86_64.egg/EGG-INFO/PKG-INFO
* /usr/lib/python3.12/site-packages/pwquality-1.4.5-py3.12-linux-x86_64.egg/EGG-INFO/SOURCES.txt
* /usr/lib/python3.12/site-packages/pwquality-1.4.5-py3.12-linux-x86_64.egg/EGG-INFO/top_level.txt
* /usr/lib/python3.12/site-packages/pwquality-1.4.5-py3.12-linux-x86_64.egg/pwquality.cpython-312-x86_64-linux-gnu.so
* /usr/lib/python3.12/site-packages/pwquality-1.4.5-py3.12-linux-x86_64.egg/pwquality.py
* /usr/lib/python3.12/site-packages/pwquality-1.4.5-py3.12-linux-x86_64.egg/__pycache__/pwquality.cpython-312.pyc
* /usr/lib/security/pam_pwquality.so
* /usr/share/doc/libpwquality-1.4.5/AUTHORS
* /usr/share/doc/libpwquality-1.4.5/ChangeLog
* /usr/share/doc/libpwquality-1.4.5/COPYING
* /usr/share/doc/libpwquality-1.4.5/INSTALL
* /usr/share/doc/libpwquality-1.4.5/NEWS
* /usr/share/doc/libpwquality-1.4.5/README
* /usr/share/locale/ar/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/as/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/az/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/bg/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/bn_IN/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/ca/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/cs/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/da/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/de/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/es/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/eu/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/fa/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/fi/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/fr/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/fur/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/gu/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/he/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/hi/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/hu/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/id/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/it/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/ja/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/ka/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/kk/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/km/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/kn/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/ko/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/ml/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/mr/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/nb/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/nl/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/or/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/pa/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/pl/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/pt/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/ru/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/si/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/sk/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/sq/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/sr/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/sv/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/ta/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/te/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/tr/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/uk/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/ur/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/vi/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/libpwquality.mo
* /usr/share/locale/zu/LC_MESSAGES/libpwquality.mo
* /usr/share/man/man1/pwmake.1.gz
* /usr/share/man/man1/pwscore.1.gz
* /usr/share/man/man3/pwquality.3.gz
* /usr/share/man/man5/pwquality.conf.5.gz
* /usr/share/man/man8/pam_pwquality.8.gz
{{< /files >}}