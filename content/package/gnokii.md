+++
draft = false
title = "gnokii 0.6.31-14"
version = "0.6.31-14"
description = "Tools and user space driver for use with mobile phones"
date = "2024-01-30T10:41:06"
aliases = "/packages/3613"
categories = ['xapps']
upstreamurl = "https://www.gnokii.org"
arch = "x86_64"
size = "584504"
usize = "2285412"
sha1sum = "5d9aaa51faf3cde610de78555a16e64510926805"
depends = "['bluez>=5.49-2', 'libusb>=0.1.5-4', 'ncurses>=6.0-12', 'readline>=8.0']"
reverse_depends = "['gnokii-gui', 'gnokii-mysql', 'gnokii-pq']"
+++
Tools and user space driver for use with mobile phones

{{< files text="show files" >}}* /etc/gnokiirc
* /usr/bin/gnokii
* /usr/bin/gnokiid
* /usr/bin/mgnokiidev
* /usr/bin/sendsms
* /usr/bin/smsd
* /usr/include/gnokii.h
* /usr/include/gnokii/bitmaps.h
* /usr/include/gnokii/call.h
* /usr/include/gnokii/common.h
* /usr/include/gnokii/data.h
* /usr/include/gnokii/encoding.h
* /usr/include/gnokii/error.h
* /usr/include/gnokii/mms.h
* /usr/include/gnokii/networks.h
* /usr/include/gnokii/ringtones.h
* /usr/include/gnokii/rlp-common.h
* /usr/include/gnokii/sms.h
* /usr/include/gnokii/statemachine.h
* /usr/include/gnokii/virtmodem.h
* /usr/include/gnokii/wappush.h
* /usr/lib/libgnokii.la
* /usr/lib/libgnokii.so
* /usr/lib/libgnokii.so.7
* /usr/lib/libgnokii.so.7.0.0
* /usr/lib/pkgconfig/gnokii.pc
* /usr/lib/smsd/libsmsd_file.la
* /usr/lib/smsd/libsmsd_file.so
* /usr/lib/smsd/libsmsd_sqlite.la
* /usr/lib/smsd/libsmsd_sqlite.so
* /usr/share/doc/gnokii-0.6.31/ChangeLog
* /usr/share/doc/gnokii-0.6.31/COPYING
* /usr/share/doc/gnokii-0.6.31/COPYRIGHT
* /usr/share/doc/gnokii-0.6.31/INSTALL
* /usr/share/doc/gnokii-0.6.31/NEWS
* /usr/share/doc/gnokii-0.6.31/TODO
* /usr/share/doc/gnokii/Bugs
* /usr/share/doc/gnokii/CodingStyle
* /usr/share/doc/gnokii/CREDITS
* /usr/share/doc/gnokii/DataCalls-QuickStart
* /usr/share/doc/gnokii/FAQ
* /usr/share/doc/gnokii/gettext-howto
* /usr/share/doc/gnokii/gnokii-hackers-howto
* /usr/share/doc/gnokii/gnokii-ir-howto
* /usr/share/doc/gnokii/gnokii-IrDA-Linux
* /usr/share/doc/gnokii/gnokii.nol
* /usr/share/doc/gnokii/KNOWN_BUGS
* /usr/share/doc/gnokii/logos.txt
* /usr/share/doc/gnokii/protocol/dancall.txt
* /usr/share/doc/gnokii/protocol/gnokiid-at.txt
* /usr/share/doc/gnokii/protocol/nk2110.txt
* /usr/share/doc/gnokii/protocol/nk3110.txt
* /usr/share/doc/gnokii/protocol/nk6110.txt
* /usr/share/doc/gnokii/protocol/nk6160.txt
* /usr/share/doc/gnokii/protocol/nk6185.txt
* /usr/share/doc/gnokii/protocol/nk640.txt
* /usr/share/doc/gnokii/protocol/nk6510.txt
* /usr/share/doc/gnokii/protocol/nk7110.txt
* /usr/share/doc/gnokii/protocol/nokia.txt
* /usr/share/doc/gnokii/README
* /usr/share/doc/gnokii/README-2110
* /usr/share/doc/gnokii/README-3810
* /usr/share/doc/gnokii/README-6110
* /usr/share/doc/gnokii/README-6510
* /usr/share/doc/gnokii/README-7110
* /usr/share/doc/gnokii/README-dancall
* /usr/share/doc/gnokii/README-DKU2
* /usr/share/doc/gnokii/README-ericsson
* /usr/share/doc/gnokii/README-MacOSX
* /usr/share/doc/gnokii/README-PCSC
* /usr/share/doc/gnokii/README-siemens
* /usr/share/doc/gnokii/README-Symbian
* /usr/share/doc/gnokii/README-WINDOWS
* /usr/share/doc/gnokii/README.libsms
* /usr/share/doc/gnokii/ringtones.txt
* /usr/share/doc/gnokii/sample/45-nokiadku2.rules
* /usr/share/doc/gnokii/sample/gnokiirc
* /usr/share/doc/gnokii/sample/logo/bronto.xpm
* /usr/share/doc/gnokii/sample/logo/gnokii.xpm
* /usr/share/doc/gnokii/sample/logo/gnokiiop.xpm
* /usr/share/doc/gnokii/sample/logo/horse.xpm
* /usr/share/doc/gnokii/sample/logo/horse2.xpm
* /usr/share/doc/gnokii/sample/logo/pacman.xpm
* /usr/share/doc/gnokii/sample/magic
* /usr/share/doc/gnokii/sample/ppp/cimd-connect
* /usr/share/doc/gnokii/sample/ppp/options
* /usr/share/doc/gnokii/sample/ppp/pap-secrets
* /usr/share/doc/gnokii/sample/ppp/ppp-6210-modem
* /usr/share/doc/gnokii/sample/ppp/ppp-FILES
* /usr/share/doc/gnokii/sample/ppp/ppp-gnokii
* /usr/share/doc/gnokii/sample/ppp/ppp-hscsd
* /usr/share/doc/gnokii/sample/ppp/ppp-on
* /usr/share/doc/gnokii/sample/ringtone/star.imelody
* /usr/share/doc/gnokii/sample/ringtone/star.rtttl
* /usr/share/doc/gnokii/sample/vCalendar/test.vcs
* /usr/share/locale/de/LC_MESSAGES/gnokii.mo
* /usr/share/locale/fi/LC_MESSAGES/gnokii.mo
* /usr/share/locale/fr/LC_MESSAGES/gnokii.mo
* /usr/share/locale/it/LC_MESSAGES/gnokii.mo
* /usr/share/locale/pl/LC_MESSAGES/gnokii.mo
* /usr/share/locale/pt/LC_MESSAGES/gnokii.mo
* /usr/share/locale/sv/LC_MESSAGES/gnokii.mo
* /usr/share/man/man1/gnokii.1.gz
* /usr/share/man/man1/sendsms.1.gz
* /usr/share/man/man1/xgnokii.1x.gz
* /usr/share/man/man8/gnokiid.8.gz
* /usr/share/man/man8/mgnokiidev.8.gz
* /usr/share/man/man8/smsd.8.gz
{{< /files >}}