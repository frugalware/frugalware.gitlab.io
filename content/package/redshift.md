+++
draft = false
title = "redshift 1.12-7"
version = "1.12-7"
date = "2023-11-02T11:02:45"
categories = ['xapps-extra']
upstreamurl = "http://jonls.dk/redshift/"
arch = "x86_64"
size = "124068"
usize = "570346"
sha1sum = "38c268135b416a9f3085f0dae37ac8f1a642f88b"
depends = "['glib2>=2.46.2-4', 'libdrm', 'libxcb', 'libxxf86vm']"
files = "['usr/', 'usr/bin/', 'usr/bin/redshift', 'usr/lib/', 'usr/lib/systemd/', 'usr/lib/systemd/user/', 'usr/lib/systemd/user/redshift-gtk.service', 'usr/lib/systemd/user/redshift.service', 'usr/share/', 'usr/share/applications/', 'usr/share/applications/redshift.desktop', 'usr/share/doc/', 'usr/share/doc/redshift-1.12/', 'usr/share/doc/redshift-1.12/CONTRIBUTORS', 'usr/share/doc/redshift-1.12/COPYING', 'usr/share/doc/redshift-1.12/LICENSE', 'usr/share/doc/redshift-1.12/NEWS', 'usr/share/doc/redshift-1.12/README', 'usr/share/doc/redshift-1.12/README-colorramp', 'usr/share/doc/redshift-1.12/README.md', 'usr/share/locale/', 'usr/share/locale/ar/', 'usr/share/locale/ar/LC_MESSAGES/', 'usr/share/locale/ar/LC_MESSAGES/redshift.mo', 'usr/share/locale/be/', 'usr/share/locale/be/LC_MESSAGES/', 'usr/share/locale/be/LC_MESSAGES/redshift.mo', 'usr/share/locale/bg/', 'usr/share/locale/bg/LC_MESSAGES/', 'usr/share/locale/bg/LC_MESSAGES/redshift.mo', 'usr/share/locale/ca/', 'usr/share/locale/ca/LC_MESSAGES/', 'usr/share/locale/ca/LC_MESSAGES/redshift.mo', 'usr/share/locale/cs/', 'usr/share/locale/cs/LC_MESSAGES/', 'usr/share/locale/cs/LC_MESSAGES/redshift.mo', 'usr/share/locale/da/', 'usr/share/locale/da/LC_MESSAGES/', 'usr/share/locale/da/LC_MESSAGES/redshift.mo', 'usr/share/locale/de/', 'usr/share/locale/de/LC_MESSAGES/', 'usr/share/locale/de/LC_MESSAGES/redshift.mo', 'usr/share/locale/el/', 'usr/share/locale/el/LC_MESSAGES/', 'usr/share/locale/el/LC_MESSAGES/redshift.mo', 'usr/share/locale/en_GB/', 'usr/share/locale/en_GB/LC_MESSAGES/', 'usr/share/locale/en_GB/LC_MESSAGES/redshift.mo', 'usr/share/locale/es/', 'usr/share/locale/es/LC_MESSAGES/', 'usr/share/locale/es/LC_MESSAGES/redshift.mo', 'usr/share/locale/et/', 'usr/share/locale/et/LC_MESSAGES/', 'usr/share/locale/et/LC_MESSAGES/redshift.mo', 'usr/share/locale/eu/', 'usr/share/locale/eu/LC_MESSAGES/', 'usr/share/locale/eu/LC_MESSAGES/redshift.mo', 'usr/share/locale/fi/', 'usr/share/locale/fi/LC_MESSAGES/', 'usr/share/locale/fi/LC_MESSAGES/redshift.mo', 'usr/share/locale/fr/', 'usr/share/locale/fr/LC_MESSAGES/', 'usr/share/locale/fr/LC_MESSAGES/redshift.mo', 'usr/share/locale/gl/', 'usr/share/locale/gl/LC_MESSAGES/', 'usr/share/locale/gl/LC_MESSAGES/redshift.mo', 'usr/share/locale/he/', 'usr/share/locale/he/LC_MESSAGES/', 'usr/share/locale/he/LC_MESSAGES/redshift.mo', 'usr/share/locale/hi/', 'usr/share/locale/hi/LC_MESSAGES/', 'usr/share/locale/hi/LC_MESSAGES/redshift.mo', 'usr/share/locale/hr/', 'usr/share/locale/hr/LC_MESSAGES/', 'usr/share/locale/hr/LC_MESSAGES/redshift.mo', 'usr/share/locale/hu/', 'usr/share/locale/hu/LC_MESSAGES/', 'usr/share/locale/hu/LC_MESSAGES/redshift.mo', 'usr/share/locale/it/', 'usr/share/locale/it/LC_MESSAGES/', 'usr/share/locale/it/LC_MESSAGES/redshift.mo', 'usr/share/locale/ja/', 'usr/share/locale/ja/LC_MESSAGES/', 'usr/share/locale/ja/LC_MESSAGES/redshift.mo', 'usr/share/locale/ka/', 'usr/share/locale/ka/LC_MESSAGES/', 'usr/share/locale/ka/LC_MESSAGES/redshift.mo', 'usr/share/locale/lt/', 'usr/share/locale/lt/LC_MESSAGES/', 'usr/share/locale/lt/LC_MESSAGES/redshift.mo', 'usr/share/locale/nb/', 'usr/share/locale/nb/LC_MESSAGES/', 'usr/share/locale/nb/LC_MESSAGES/redshift.mo', 'usr/share/locale/nl/', 'usr/share/locale/nl/LC_MESSAGES/', 'usr/share/locale/nl/LC_MESSAGES/redshift.mo', 'usr/share/locale/pl/', 'usr/share/locale/pl/LC_MESSAGES/', 'usr/share/locale/pl/LC_MESSAGES/redshift.mo', 'usr/share/locale/pt/', 'usr/share/locale/pt/LC_MESSAGES/', 'usr/share/locale/pt/LC_MESSAGES/redshift.mo', 'usr/share/locale/pt_BR/', 'usr/share/locale/pt_BR/LC_MESSAGES/', 'usr/share/locale/pt_BR/LC_MESSAGES/redshift.mo', 'usr/share/locale/ro/', 'usr/share/locale/ro/LC_MESSAGES/', 'usr/share/locale/ro/LC_MESSAGES/redshift.mo', 'usr/share/locale/ru/', 'usr/share/locale/ru/LC_MESSAGES/', 'usr/share/locale/ru/LC_MESSAGES/redshift.mo', 'usr/share/locale/sr/', 'usr/share/locale/sr/LC_MESSAGES/', 'usr/share/locale/sr/LC_MESSAGES/redshift.mo', 'usr/share/locale/sv/', 'usr/share/locale/sv/LC_MESSAGES/', 'usr/share/locale/sv/LC_MESSAGES/redshift.mo', 'usr/share/locale/tr/', 'usr/share/locale/tr/LC_MESSAGES/', 'usr/share/locale/tr/LC_MESSAGES/redshift.mo', 'usr/share/locale/uk/', 'usr/share/locale/uk/LC_MESSAGES/', 'usr/share/locale/uk/LC_MESSAGES/redshift.mo', 'usr/share/locale/zh_CN/', 'usr/share/locale/zh_CN/LC_MESSAGES/', 'usr/share/locale/zh_CN/LC_MESSAGES/redshift.mo', 'usr/share/locale/zh_TW/', 'usr/share/locale/zh_TW/LC_MESSAGES/', 'usr/share/locale/zh_TW/LC_MESSAGES/redshift.mo', 'usr/share/man/', 'usr/share/man/man1/', 'usr/share/man/man1/redshift.1.gz']"
+++
Redshift color temperature adjustment.