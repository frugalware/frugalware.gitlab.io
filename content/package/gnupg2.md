+++
draft = false
title = "gnupg2 2.4.4-1"
version = "2.4.4-1"
description = "GnuPG2 is the new modularized version of GnuPG supporting OpenPGP and S/MIME"
date = "2024-01-26T14:12:34"
aliases = "/packages/14925"
categories = ['apps']
upstreamurl = "https://www.gnupg.org"
arch = "x86_64"
size = "2705200"
usize = "10794011"
sha1sum = "5fb6664697097b698f5d1983358d98606599880f"
depends = "['libassuan>=2.5.1-2', 'libksba>=1.3.5-2', 'libsystemd>=231-22', 'libusb>=0.1.5-4', 'ncurses>=6.0-12', 'npth>=1.5-2', 'readline>=8.0', 'sqlite3>=3.9.2-4']"
reverse_depends = "['kernel-initrd', 'kernel-lts-initrd', 'qca-gnupg']"
+++
GnuPG2 is the new modularized version of GnuPG supporting OpenPGP and S/MIME{{< spoiler text="show files" >}}* /usr/bin/addgnupghome
* /usr/bin/applygnupgdefaults
* /usr/bin/dirmngr-client
* /usr/bin/gpg
* /usr/bin/gpg-card
* /usr/bin/gpg-wks-client
* /usr/bin/gpg-wks-server
* /usr/bin/gpgconf
* /usr/bin/gpgparsemail
* /usr/bin/gpgscm
* /usr/bin/gpgsm
* /usr/bin/gpgsplit
* /usr/bin/gpgtar
* /usr/bin/kbxutil
* /usr/bin/watchgnupg
* /usr/lib/gnupg2/gpg-auth
* /usr/lib/gnupg2/gpg-check-pattern
* /usr/lib/gnupg2/gpg-pair-tool
* /usr/lib/gnupg2/gpg-wks-client
* /usr/lib/gnupg2/keyboxd
* /usr/lib/gnupg2/scdaemon
* /usr/share/doc/gnupg2-2.4.4/AUTHORS
* /usr/share/doc/gnupg2-2.4.4/ChangeLog
* /usr/share/doc/gnupg2-2.4.4/COPYING
* /usr/share/doc/gnupg2-2.4.4/COPYING.CC0
* /usr/share/doc/gnupg2-2.4.4/COPYING.GPL2
* /usr/share/doc/gnupg2-2.4.4/COPYING.LGPL21
* /usr/share/doc/gnupg2-2.4.4/COPYING.LGPL3
* /usr/share/doc/gnupg2-2.4.4/COPYING.other
* /usr/share/doc/gnupg2-2.4.4/DCO
* /usr/share/doc/gnupg2-2.4.4/DETAILS
* /usr/share/doc/gnupg2-2.4.4/examples/common.conf
* /usr/share/doc/gnupg2-2.4.4/examples/gpgconf.conf
* /usr/share/doc/gnupg2-2.4.4/examples/gpgconf.rnames
* /usr/share/doc/gnupg2-2.4.4/examples/pwpattern.list
* /usr/share/doc/gnupg2-2.4.4/examples/qualified.txt
* /usr/share/doc/gnupg2-2.4.4/examples/README
* /usr/share/doc/gnupg2-2.4.4/examples/scd-event
* /usr/share/doc/gnupg2-2.4.4/examples/trustlist.txt
* /usr/share/doc/gnupg2-2.4.4/FAQ
* /usr/share/doc/gnupg2-2.4.4/HACKING
* /usr/share/doc/gnupg2-2.4.4/INSTALL
* /usr/share/doc/gnupg2-2.4.4/KEYSERVER
* /usr/share/doc/gnupg2-2.4.4/NEWS
* /usr/share/doc/gnupg2-2.4.4/OpenPGP
* /usr/share/doc/gnupg2-2.4.4/README
* /usr/share/doc/gnupg2-2.4.4/README.GIT
* /usr/share/doc/gnupg2-2.4.4/THANKS
* /usr/share/doc/gnupg2-2.4.4/TODO
* /usr/share/doc/gnupg2-2.4.4/TRANSLATE
* /usr/share/doc/gnupg2-2.4.4/VERSION
* /usr/share/gnupg/distsigkey.gpg
* /usr/share/gnupg/help.be.txt
* /usr/share/gnupg/help.ca.txt
* /usr/share/gnupg/help.cs.txt
* /usr/share/gnupg/help.da.txt
* /usr/share/gnupg/help.de.txt
* /usr/share/gnupg/help.el.txt
* /usr/share/gnupg/help.eo.txt
* /usr/share/gnupg/help.es.txt
* /usr/share/gnupg/help.et.txt
* /usr/share/gnupg/help.fi.txt
* /usr/share/gnupg/help.fr.txt
* /usr/share/gnupg/help.gl.txt
* /usr/share/gnupg/help.hu.txt
* /usr/share/gnupg/help.id.txt
* /usr/share/gnupg/help.it.txt
* /usr/share/gnupg/help.ja.txt
* /usr/share/gnupg/help.nb.txt
* /usr/share/gnupg/help.pl.txt
* /usr/share/gnupg/help.pt.txt
* /usr/share/gnupg/help.pt_BR.txt
* /usr/share/gnupg/help.ro.txt
* /usr/share/gnupg/help.ru.txt
* /usr/share/gnupg/help.sk.txt
* /usr/share/gnupg/help.sv.txt
* /usr/share/gnupg/help.tr.txt
* /usr/share/gnupg/help.txt
* /usr/share/gnupg/help.zh_CN.txt
* /usr/share/gnupg/help.zh_TW.txt
* /usr/share/gnupg/sks-keyservers.netCA.pem
* /usr/share/info/gnupg.info-1.gz
* /usr/share/info/gnupg.info-2.gz
* /usr/share/info/gnupg.info-3.gz
* /usr/share/info/gnupg.info.gz
* /usr/share/locale/ca/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/cs/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/da/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/de/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/el/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/en@boldquot/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/en@quot/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/eo/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/es/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/et/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/fi/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/fr/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/gl/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/hu/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/id/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/it/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/ja/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/nb/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/pl/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/pt/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/ro/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/ru/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/sk/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/sv/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/tr/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/uk/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/gnupg2.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/gnupg2.mo
* /usr/share/man/man1/dirmngr-client.1.gz
* /usr/share/man/man1/gpg-agent.1.gz
* /usr/share/man/man1/gpg-card.1.gz
* /usr/share/man/man1/gpg-check-pattern.1.gz
* /usr/share/man/man1/gpg-connect-agent.1.gz
* /usr/share/man/man1/gpg-preset-passphrase.1.gz
* /usr/share/man/man1/gpg-wks-client.1.gz
* /usr/share/man/man1/gpg-wks-server.1.gz
* /usr/share/man/man1/gpg.1
* /usr/share/man/man1/gpg.1.gz
* /usr/share/man/man1/gpgconf.1.gz
* /usr/share/man/man1/gpgparsemail.1.gz
* /usr/share/man/man1/gpgsm.1.gz
* /usr/share/man/man1/gpgtar.1.gz
* /usr/share/man/man1/gpgv.1.gz
* /usr/share/man/man1/scdaemon.1.gz
* /usr/share/man/man1/watchgnupg.1.gz
* /usr/share/man/man7/gnupg.7.gz
* /usr/share/man/man8/addgnupghome.8.gz
* /usr/share/man/man8/applygnupgdefaults.8.gz
* /usr/share/man/man8/dirmngr.8.gz
{{< /spoiler >}}