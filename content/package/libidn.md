+++
draft = false
title = "libidn 1.42-1"
version = "1.42-1"
description = "GNU Libidn is an implementation of the Stringprep,Punycode and IDNA specification."
date = "2024-01-18T09:59:43"
aliases = "/packages/4244"
categories = ['base']
upstreamurl = "http://www.gnu.org/software/libidn/"
arch = "x86_64"
size = "251220"
usize = "866139"
sha1sum = "cc1d02bda9f55070aff928edfd8ce96e53765059"
depends = "['glibc>=2.35']"
reverse_depends = "['courier-imap', 'courier-maildrop', 'dirmngr', 'dirmngr-ldap', 'eiskaltdc', 'elinks', 'gloox', 'gmime3', 'gnunet', 'kopete', 'libgadu', 'libgs', 'libgsasl', 'libpurple', 'libsystemd', 'libvlc', 'libvncserver', 'lynx', 'mutt-devel', 'php', 'podofo', 'podofo-0.9', 'whois']"
+++
GNU Libidn is an implementation of the Stringprep,Punycode and IDNA specification.{{< spoiler text="show files" >}}* /usr/bin/idn
* /usr/include/idn-free.h
* /usr/include/idn-int.h
* /usr/include/idna.h
* /usr/include/pr29.h
* /usr/include/punycode.h
* /usr/include/stringprep.h
* /usr/include/tld.h
* /usr/lib/libidn.so
* /usr/lib/libidn.so.12
* /usr/lib/libidn.so.12.6.5
* /usr/lib/pkgconfig/libidn.pc
* /usr/share/doc/libidn-1.42/AUTHORS
* /usr/share/doc/libidn-1.42/ChangeLog
* /usr/share/doc/libidn-1.42/COPYING
* /usr/share/doc/libidn-1.42/COPYING.LESSERv2
* /usr/share/doc/libidn-1.42/COPYING.LESSERv3
* /usr/share/doc/libidn-1.42/COPYINGv2
* /usr/share/doc/libidn-1.42/COPYINGv3
* /usr/share/doc/libidn-1.42/FAQ
* /usr/share/doc/libidn-1.42/INSTALL
* /usr/share/doc/libidn-1.42/NEWS
* /usr/share/doc/libidn-1.42/README
* /usr/share/doc/libidn-1.42/THANKS
* /usr/share/emacs/site-lisp/idna.el
* /usr/share/emacs/site-lisp/punycode.el
* /usr/share/info/libidn-components.png.gz
* /usr/share/info/libidn.info.gz
* /usr/share/locale/cs/LC_MESSAGES/libidn.mo
* /usr/share/locale/da/LC_MESSAGES/libidn.mo
* /usr/share/locale/de/LC_MESSAGES/libidn.mo
* /usr/share/locale/eo/LC_MESSAGES/libidn.mo
* /usr/share/locale/es/LC_MESSAGES/libidn.mo
* /usr/share/locale/fi/LC_MESSAGES/libidn.mo
* /usr/share/locale/fr/LC_MESSAGES/libidn.mo
* /usr/share/locale/hr/LC_MESSAGES/libidn.mo
* /usr/share/locale/hu/LC_MESSAGES/libidn.mo
* /usr/share/locale/id/LC_MESSAGES/libidn.mo
* /usr/share/locale/it/LC_MESSAGES/libidn.mo
* /usr/share/locale/ja/LC_MESSAGES/libidn.mo
* /usr/share/locale/ka/LC_MESSAGES/libidn.mo
* /usr/share/locale/ko/LC_MESSAGES/libidn.mo
* /usr/share/locale/nl/LC_MESSAGES/libidn.mo
* /usr/share/locale/pl/LC_MESSAGES/libidn.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/libidn.mo
* /usr/share/locale/ro/LC_MESSAGES/libidn.mo
* /usr/share/locale/sr/LC_MESSAGES/libidn.mo
* /usr/share/locale/sv/LC_MESSAGES/libidn.mo
* /usr/share/locale/uk/LC_MESSAGES/libidn.mo
* /usr/share/locale/vi/LC_MESSAGES/libidn.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/libidn.mo
* /usr/share/man/man1/idn.1.gz
* /usr/share/man/man3/idna_strerror.3.gz
* /usr/share/man/man3/idna_to_ascii_4i.3.gz
* /usr/share/man/man3/idna_to_ascii_4z.3.gz
* /usr/share/man/man3/idna_to_ascii_8z.3.gz
* /usr/share/man/man3/idna_to_ascii_lz.3.gz
* /usr/share/man/man3/idna_to_unicode_44i.3.gz
* /usr/share/man/man3/idna_to_unicode_4z4z.3.gz
* /usr/share/man/man3/idna_to_unicode_8z4z.3.gz
* /usr/share/man/man3/idna_to_unicode_8z8z.3.gz
* /usr/share/man/man3/idna_to_unicode_8zlz.3.gz
* /usr/share/man/man3/idna_to_unicode_lzlz.3.gz
* /usr/share/man/man3/idn_free.3.gz
* /usr/share/man/man3/pr29_4.3.gz
* /usr/share/man/man3/pr29_4z.3.gz
* /usr/share/man/man3/pr29_8z.3.gz
* /usr/share/man/man3/pr29_strerror.3.gz
* /usr/share/man/man3/punycode_decode.3.gz
* /usr/share/man/man3/punycode_encode.3.gz
* /usr/share/man/man3/punycode_strerror.3.gz
* /usr/share/man/man3/stringprep.3.gz
* /usr/share/man/man3/stringprep_4i.3.gz
* /usr/share/man/man3/stringprep_4zi.3.gz
* /usr/share/man/man3/stringprep_check_version.3.gz
* /usr/share/man/man3/stringprep_convert.3.gz
* /usr/share/man/man3/stringprep_locale_charset.3.gz
* /usr/share/man/man3/stringprep_locale_to_utf8.3.gz
* /usr/share/man/man3/stringprep_profile.3.gz
* /usr/share/man/man3/stringprep_strerror.3.gz
* /usr/share/man/man3/stringprep_ucs4_nfkc_normalize.3.gz
* /usr/share/man/man3/stringprep_ucs4_to_utf8.3.gz
* /usr/share/man/man3/stringprep_unichar_to_utf8.3.gz
* /usr/share/man/man3/stringprep_utf8_nfkc_normalize.3.gz
* /usr/share/man/man3/stringprep_utf8_to_locale.3.gz
* /usr/share/man/man3/stringprep_utf8_to_ucs4.3.gz
* /usr/share/man/man3/stringprep_utf8_to_unichar.3.gz
* /usr/share/man/man3/tld_check_4.3.gz
* /usr/share/man/man3/tld_check_4t.3.gz
* /usr/share/man/man3/tld_check_4tz.3.gz
* /usr/share/man/man3/tld_check_4z.3.gz
* /usr/share/man/man3/tld_check_8z.3.gz
* /usr/share/man/man3/tld_check_lz.3.gz
* /usr/share/man/man3/tld_default_table.3.gz
* /usr/share/man/man3/tld_get_4.3.gz
* /usr/share/man/man3/tld_get_4z.3.gz
* /usr/share/man/man3/tld_get_table.3.gz
* /usr/share/man/man3/tld_get_z.3.gz
* /usr/share/man/man3/tld_strerror.3.gz
{{< /spoiler >}}