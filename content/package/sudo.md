+++
draft = false
title = "sudo 1.9.16-1"
version = "1.9.16-1"
description = "Give limited root privileges to certain users"
date = "2024-09-06T08:46:22"
aliases = "/packages/3346"
categories = ['base']
upstreamurl = "http://www.sudo.ws/"
arch = "x86_64"
size = "1857376"
usize = "8179702"
sha1sum = "e1b9827982dea46eb239f5de1800c9986b19081b"
depends = "['glibc>=2.34', 'libxcrypt', 'openssl>=3.1.0']"
reverse_depends = "['inxi']"
+++
### Description: 
Give limited root privileges to certain users

### Files: 
* /etc/sudo.conf
* /etc/sudoers
* /etc/sudoers.d/.sudo
* /etc/sudoers.dist
* /etc/sudo_logsrvd.conf
* /usr/bin/cvtsudoers
* /usr/bin/sudo
* /usr/bin/sudoedit
* /usr/bin/sudoreplay
* /usr/bin/sudo_logsrvd
* /usr/bin/sudo_sendlog
* /usr/bin/visudo
* /usr/include/sudo_plugin.h
* /usr/lib/sudo/libsudo_util.so
* /usr/lib/sudo/libsudo_util.so.0
* /usr/lib/sudo/libsudo_util.so.0.0.0
* /usr/lib/sudo/sudo/audit_json.so
* /usr/lib/sudo/sudo/group_file.so
* /usr/lib/sudo/sudo/sudoers.so
* /usr/lib/sudo/sudo/sudo_intercept.so
* /usr/lib/sudo/sudo/sudo_noexec.so
* /usr/lib/sudo/sudo/system_group.so
* /usr/lib/tmpfiles.d/sudo.conf
* /usr/share/doc/sudo-1.9.16/ChangeLog
* /usr/share/doc/sudo-1.9.16/CONTRIBUTING.md
* /usr/share/doc/sudo-1.9.16/CONTRIBUTORS.md
* /usr/share/doc/sudo-1.9.16/examples/cvtsudoers.conf
* /usr/share/doc/sudo-1.9.16/examples/pam.conf
* /usr/share/doc/sudo-1.9.16/examples/sudo.conf
* /usr/share/doc/sudo-1.9.16/examples/sudoers
* /usr/share/doc/sudo-1.9.16/examples/sudo_logsrvd.conf
* /usr/share/doc/sudo-1.9.16/examples/syslog.conf
* /usr/share/doc/sudo-1.9.16/HISTORY.md
* /usr/share/doc/sudo-1.9.16/INSTALL.configure
* /usr/share/doc/sudo-1.9.16/INSTALL.md
* /usr/share/doc/sudo-1.9.16/LICENSE.md
* /usr/share/doc/sudo-1.9.16/MANIFEST
* /usr/share/doc/sudo-1.9.16/NEWS
* /usr/share/doc/sudo-1.9.16/README.LDAP.md
* /usr/share/doc/sudo-1.9.16/README.md
* /usr/share/doc/sudo-1.9.16/SECURITY.md
* /usr/share/doc/sudo-1.9.16/TROUBLESHOOTING.md
* /usr/share/doc/sudo-1.9.16/UPGRADE.md
* /usr/share/locale/ast/LC_MESSAGES/sudo.mo
* /usr/share/locale/ast/LC_MESSAGES/sudoers.mo
* /usr/share/locale/ca/LC_MESSAGES/sudo.mo
* /usr/share/locale/ca/LC_MESSAGES/sudoers.mo
* /usr/share/locale/cs/LC_MESSAGES/sudo.mo
* /usr/share/locale/cs/LC_MESSAGES/sudoers.mo
* /usr/share/locale/da/LC_MESSAGES/sudo.mo
* /usr/share/locale/da/LC_MESSAGES/sudoers.mo
* /usr/share/locale/de/LC_MESSAGES/sudo.mo
* /usr/share/locale/de/LC_MESSAGES/sudoers.mo
* /usr/share/locale/el/LC_MESSAGES/sudoers.mo
* /usr/share/locale/eo/LC_MESSAGES/sudo.mo
* /usr/share/locale/eo/LC_MESSAGES/sudoers.mo
* /usr/share/locale/es/LC_MESSAGES/sudo.mo
* /usr/share/locale/es/LC_MESSAGES/sudoers.mo
* /usr/share/locale/eu/LC_MESSAGES/sudo.mo
* /usr/share/locale/eu/LC_MESSAGES/sudoers.mo
* /usr/share/locale/fa/LC_MESSAGES/sudo.mo
* /usr/share/locale/fi/LC_MESSAGES/sudo.mo
* /usr/share/locale/fi/LC_MESSAGES/sudoers.mo
* /usr/share/locale/fr/LC_MESSAGES/sudo.mo
* /usr/share/locale/fr/LC_MESSAGES/sudoers.mo
* /usr/share/locale/fur/LC_MESSAGES/sudo.mo
* /usr/share/locale/fur/LC_MESSAGES/sudoers.mo
* /usr/share/locale/gl/LC_MESSAGES/sudo.mo
* /usr/share/locale/hr/LC_MESSAGES/sudo.mo
* /usr/share/locale/hr/LC_MESSAGES/sudoers.mo
* /usr/share/locale/hu/LC_MESSAGES/sudo.mo
* /usr/share/locale/hu/LC_MESSAGES/sudoers.mo
* /usr/share/locale/id/LC_MESSAGES/sudo.mo
* /usr/share/locale/id/LC_MESSAGES/sudoers.mo
* /usr/share/locale/it/LC_MESSAGES/sudo.mo
* /usr/share/locale/it/LC_MESSAGES/sudoers.mo
* /usr/share/locale/ja/LC_MESSAGES/sudo.mo
* /usr/share/locale/ja/LC_MESSAGES/sudoers.mo
* /usr/share/locale/ka/LC_MESSAGES/sudo.mo
* /usr/share/locale/ka/LC_MESSAGES/sudoers.mo
* /usr/share/locale/ko/LC_MESSAGES/sudo.mo
* /usr/share/locale/ko/LC_MESSAGES/sudoers.mo
* /usr/share/locale/lt/LC_MESSAGES/sudoers.mo
* /usr/share/locale/nb/LC_MESSAGES/sudo.mo
* /usr/share/locale/nb/LC_MESSAGES/sudoers.mo
* /usr/share/locale/nl/LC_MESSAGES/sudo.mo
* /usr/share/locale/nl/LC_MESSAGES/sudoers.mo
* /usr/share/locale/nn/LC_MESSAGES/sudo.mo
* /usr/share/locale/pl/LC_MESSAGES/sudo.mo
* /usr/share/locale/pl/LC_MESSAGES/sudoers.mo
* /usr/share/locale/pt/LC_MESSAGES/sudo.mo
* /usr/share/locale/pt/LC_MESSAGES/sudoers.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/sudo.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/sudoers.mo
* /usr/share/locale/ro/LC_MESSAGES/sudo.mo
* /usr/share/locale/ro/LC_MESSAGES/sudoers.mo
* /usr/share/locale/ru/LC_MESSAGES/sudo.mo
* /usr/share/locale/ru/LC_MESSAGES/sudoers.mo
* /usr/share/locale/sk/LC_MESSAGES/sudo.mo
* /usr/share/locale/sk/LC_MESSAGES/sudoers.mo
* /usr/share/locale/sl/LC_MESSAGES/sudo.mo
* /usr/share/locale/sl/LC_MESSAGES/sudoers.mo
* /usr/share/locale/sq/LC_MESSAGES/sudo.mo
* /usr/share/locale/sr/LC_MESSAGES/sudo.mo
* /usr/share/locale/sr/LC_MESSAGES/sudoers.mo
* /usr/share/locale/sv/LC_MESSAGES/sudo.mo
* /usr/share/locale/sv/LC_MESSAGES/sudoers.mo
* /usr/share/locale/tr/LC_MESSAGES/sudo.mo
* /usr/share/locale/tr/LC_MESSAGES/sudoers.mo
* /usr/share/locale/uk/LC_MESSAGES/sudo.mo
* /usr/share/locale/uk/LC_MESSAGES/sudoers.mo
* /usr/share/locale/vi/LC_MESSAGES/sudo.mo
* /usr/share/locale/vi/LC_MESSAGES/sudoers.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/sudo.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/sudoers.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/sudo.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/sudoers.mo
* /usr/share/man/man1/cvtsudoers.1.gz
* /usr/share/man/man5/sudo.conf.5.gz
* /usr/share/man/man5/sudoers.5.gz
* /usr/share/man/man5/sudoers_timestamp.5.gz
* /usr/share/man/man5/sudo_logsrv.proto.5.gz
* /usr/share/man/man5/sudo_logsrvd.conf.5.gz
* /usr/share/man/man5/sudo_plugin.5.gz
* /usr/share/man/man8/sudo.8.gz
* /usr/share/man/man8/sudoedit.8.gz
* /usr/share/man/man8/sudoreplay.8.gz
* /usr/share/man/man8/sudo_logsrvd.8.gz
* /usr/share/man/man8/sudo_sendlog.8.gz
* /usr/share/man/man8/visudo.8.gz
