+++
draft = false
title = "wget2 2.1.0-1"
version = "2.1.0-1"
date = "2023-09-07T17:42:01"
categories = ['network']
upstreamurl = "https://gitlab.com/gnuwget/wget2"
arch = "x86_64"
size = "452268"
usize = "2183357"
sha1sum = "ba5b92525fcacc7a8ceebbda7904f3626b607211"
depends = "['zstd', 'brotli', 'nghttp2', 'libpsl', 'openssl', 'pcre2', 'gpgme']"
files = "['etc/', 'etc/wgetrc', 'usr/', 'usr/bin/', 'usr/bin/wget2', 'usr/bin/wget2_noinstall', 'usr/include/', 'usr/include/wget.h', 'usr/include/wgetver.h', 'usr/lib/', 'usr/lib/libwget.so', 'usr/lib/libwget.so.2', 'usr/lib/libwget.so.2.0.0', 'usr/lib/pkgconfig/', 'usr/lib/pkgconfig/libwget.pc', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/wget2-2.1.0/', 'usr/share/doc/wget2-2.1.0/AUTHORS', 'usr/share/doc/wget2-2.1.0/COPYING', 'usr/share/doc/wget2-2.1.0/COPYING.LESSER', 'usr/share/doc/wget2-2.1.0/ChangeLog', 'usr/share/doc/wget2-2.1.0/INSTALL', 'usr/share/doc/wget2-2.1.0/NEWS', 'usr/share/doc/wget2-2.1.0/README', 'usr/share/doc/wget2-2.1.0/README.md', 'usr/share/locale/', 'usr/share/locale/ca/', 'usr/share/locale/ca/LC_MESSAGES/', 'usr/share/locale/ca/LC_MESSAGES/wget2.mo', 'usr/share/locale/cs/', 'usr/share/locale/cs/LC_MESSAGES/', 'usr/share/locale/cs/LC_MESSAGES/wget2.mo', 'usr/share/locale/de/', 'usr/share/locale/de/LC_MESSAGES/', 'usr/share/locale/de/LC_MESSAGES/wget2.mo', 'usr/share/locale/eo/', 'usr/share/locale/eo/LC_MESSAGES/', 'usr/share/locale/eo/LC_MESSAGES/wget2.mo', 'usr/share/locale/es/', 'usr/share/locale/es/LC_MESSAGES/', 'usr/share/locale/es/LC_MESSAGES/wget2.mo', 'usr/share/locale/et/', 'usr/share/locale/et/LC_MESSAGES/', 'usr/share/locale/et/LC_MESSAGES/wget2.mo', 'usr/share/locale/fi/', 'usr/share/locale/fi/LC_MESSAGES/', 'usr/share/locale/fi/LC_MESSAGES/wget2.mo', 'usr/share/locale/fr/', 'usr/share/locale/fr/LC_MESSAGES/', 'usr/share/locale/fr/LC_MESSAGES/wget2.mo', 'usr/share/locale/ga/', 'usr/share/locale/ga/LC_MESSAGES/', 'usr/share/locale/ga/LC_MESSAGES/wget2.mo', 'usr/share/locale/hr/', 'usr/share/locale/hr/LC_MESSAGES/', 'usr/share/locale/hr/LC_MESSAGES/wget2.mo', 'usr/share/locale/hu/', 'usr/share/locale/hu/LC_MESSAGES/', 'usr/share/locale/hu/LC_MESSAGES/wget2.mo', 'usr/share/locale/id/', 'usr/share/locale/id/LC_MESSAGES/', 'usr/share/locale/id/LC_MESSAGES/wget2.mo', 'usr/share/locale/it/', 'usr/share/locale/it/LC_MESSAGES/', 'usr/share/locale/it/LC_MESSAGES/wget2.mo', 'usr/share/locale/ja/', 'usr/share/locale/ja/LC_MESSAGES/', 'usr/share/locale/ja/LC_MESSAGES/wget2.mo', 'usr/share/locale/nb/', 'usr/share/locale/nb/LC_MESSAGES/', 'usr/share/locale/nb/LC_MESSAGES/wget2.mo', 'usr/share/locale/nl/', 'usr/share/locale/nl/LC_MESSAGES/', 'usr/share/locale/nl/LC_MESSAGES/wget2.mo', 'usr/share/locale/pl/', 'usr/share/locale/pl/LC_MESSAGES/', 'usr/share/locale/pl/LC_MESSAGES/wget2.mo', 'usr/share/locale/pt_BR/', 'usr/share/locale/pt_BR/LC_MESSAGES/', 'usr/share/locale/pt_BR/LC_MESSAGES/wget2.mo', 'usr/share/locale/ro/', 'usr/share/locale/ro/LC_MESSAGES/', 'usr/share/locale/ro/LC_MESSAGES/wget2.mo', 'usr/share/locale/ru/', 'usr/share/locale/ru/LC_MESSAGES/', 'usr/share/locale/ru/LC_MESSAGES/wget2.mo', 'usr/share/locale/sk/', 'usr/share/locale/sk/LC_MESSAGES/', 'usr/share/locale/sk/LC_MESSAGES/wget2.mo', 'usr/share/locale/sr/', 'usr/share/locale/sr/LC_MESSAGES/', 'usr/share/locale/sr/LC_MESSAGES/wget2.mo', 'usr/share/locale/sv/', 'usr/share/locale/sv/LC_MESSAGES/', 'usr/share/locale/sv/LC_MESSAGES/wget2.mo', 'usr/share/locale/tr/', 'usr/share/locale/tr/LC_MESSAGES/', 'usr/share/locale/tr/LC_MESSAGES/wget2.mo', 'usr/share/locale/uk/', 'usr/share/locale/uk/LC_MESSAGES/', 'usr/share/locale/uk/LC_MESSAGES/wget2.mo', 'usr/share/locale/vi/', 'usr/share/locale/vi/LC_MESSAGES/', 'usr/share/locale/vi/LC_MESSAGES/wget2.mo', 'usr/share/locale/zh_CN/', 'usr/share/locale/zh_CN/LC_MESSAGES/', 'usr/share/locale/zh_CN/LC_MESSAGES/wget2.mo', 'usr/share/man/', 'usr/share/man/man3/', 'usr/share/man/man3/libwget-base64.3.gz', 'usr/share/man/man3/libwget-bitmap.3.gz', 'usr/share/man/man3/libwget-console.3.gz', 'usr/share/man/man3/libwget-dns-caching.3.gz', 'usr/share/man/man3/libwget-dns.3.gz', 'usr/share/man/man3/libwget-error.3.gz', 'usr/share/man/man3/libwget-hash.3.gz', 'usr/share/man/man3/libwget-hashmap.3.gz', 'usr/share/man/man3/libwget-io.3.gz', 'usr/share/man/man3/libwget-ip.3.gz', 'usr/share/man/man3/libwget-list.3.gz', 'usr/share/man/man3/libwget-mem.3.gz', 'usr/share/man/man3/libwget-net.3.gz', 'usr/share/man/man3/libwget-parse_atom.3.gz', 'usr/share/man/man3/libwget-parse_sitemap.3.gz', 'usr/share/man/man3/libwget-printf.3.gz', 'usr/share/man/man3/libwget-random.3.gz', 'usr/share/man/man3/libwget-robots.3.gz', 'usr/share/man/man3/libwget-stringmap.3.gz', 'usr/share/man/man3/libwget-thread.3.gz', 'usr/share/man/man3/libwget-utils.3.gz', 'usr/share/man/man3/libwget-vector.3.gz', 'usr/share/man/man3/libwget-xalloc.3.gz', 'usr/share/man/man3/libwget-xml.3.gz']"
+++
A network utility to retrieve files from the Web