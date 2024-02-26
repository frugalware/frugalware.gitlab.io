+++
draft = false
title = "proftpd 1.3.8b-3"
version = "1.3.8b-3"
description = "Highly configurable GPL-licensed FTP server software"
date = "2024-02-02T15:05:38"
aliases = "/packages/3300"
categories = ['network-extra']
upstreamurl = "http://www.proftpd.org/"
arch = "x86_64"
size = "999660"
usize = "4580595"
sha1sum = "56e2cca07742caa46fc855903dc1ff6999a78c2f"
depends = "['libldap>=2.6.2', 'mariadb-libs>=10.3.14', 'ncurses>=6.0-12', 'openssl>=3.1.0']"
+++
Highly configurable GPL-licensed FTP server software{{< spoiler text="show files" >}}* /etc/ftpusers
* /etc/proftpd.conf
* /usr/bin/ftpasswd
* /usr/bin/ftpcount
* /usr/bin/ftpdctl
* /usr/bin/ftpmail
* /usr/bin/ftpquota
* /usr/bin/ftpscrub
* /usr/bin/ftpshut
* /usr/bin/ftptop
* /usr/bin/ftpwho
* /usr/bin/in.proftpd
* /usr/bin/proftpd
* /usr/bin/prxs
* /usr/include/proftpd/acconfig.h
* /usr/include/proftpd/ascii.h
* /usr/include/proftpd/auth.h
* /usr/include/proftpd/base.h
* /usr/include/proftpd/bindings.h
* /usr/include/proftpd/buildstamp.h
* /usr/include/proftpd/ccan-json.h
* /usr/include/proftpd/child.h
* /usr/include/proftpd/class.h
* /usr/include/proftpd/cmd.h
* /usr/include/proftpd/compat.h
* /usr/include/proftpd/conf.h
* /usr/include/proftpd/config.h
* /usr/include/proftpd/configdb.h
* /usr/include/proftpd/ctrls.h
* /usr/include/proftpd/data.h
* /usr/include/proftpd/default_paths.h
* /usr/include/proftpd/dirtree.h
* /usr/include/proftpd/display.h
* /usr/include/proftpd/encode.h
* /usr/include/proftpd/env.h
* /usr/include/proftpd/error.h
* /usr/include/proftpd/event.h
* /usr/include/proftpd/expr.h
* /usr/include/proftpd/feat.h
* /usr/include/proftpd/filter.h
* /usr/include/proftpd/fsio.h
* /usr/include/proftpd/ftp.h
* /usr/include/proftpd/glibc-glob.h
* /usr/include/proftpd/hanson-tpl.h
* /usr/include/proftpd/help.h
* /usr/include/proftpd/ident.h
* /usr/include/proftpd/inet.h
* /usr/include/proftpd/jot.h
* /usr/include/proftpd/json.h
* /usr/include/proftpd/lastlog.h
* /usr/include/proftpd/log.h
* /usr/include/proftpd/logfmt.h
* /usr/include/proftpd/Make.rules
* /usr/include/proftpd/memcache.h
* /usr/include/proftpd/mkhome.h
* /usr/include/proftpd/modules.h
* /usr/include/proftpd/mod_ctrls.h
* /usr/include/proftpd/mod_quotatab.h
* /usr/include/proftpd/mod_sql.h
* /usr/include/proftpd/mod_tls.h
* /usr/include/proftpd/netacl.h
* /usr/include/proftpd/netaddr.h
* /usr/include/proftpd/netio.h
* /usr/include/proftpd/openbsd-blowfish.h
* /usr/include/proftpd/options.h
* /usr/include/proftpd/os.h
* /usr/include/proftpd/parser.h
* /usr/include/proftpd/pidfile.h
* /usr/include/proftpd/pool.h
* /usr/include/proftpd/pr-syslog.h
* /usr/include/proftpd/privs.h
* /usr/include/proftpd/proctitle.h
* /usr/include/proftpd/proftpd.h
* /usr/include/proftpd/random.h
* /usr/include/proftpd/redis.h
* /usr/include/proftpd/regexp.h
* /usr/include/proftpd/response.h
* /usr/include/proftpd/rlimit.h
* /usr/include/proftpd/scoreboard.h
* /usr/include/proftpd/session.h
* /usr/include/proftpd/sets.h
* /usr/include/proftpd/signals.h
* /usr/include/proftpd/stash.h
* /usr/include/proftpd/str.h
* /usr/include/proftpd/support.h
* /usr/include/proftpd/table.h
* /usr/include/proftpd/throttle.h
* /usr/include/proftpd/timers.h
* /usr/include/proftpd/trace.h
* /usr/include/proftpd/utf8.h
* /usr/include/proftpd/var.h
* /usr/include/proftpd/version.h
* /usr/include/proftpd/xferlog.h
* /usr/lib/pkgconfig/proftpd.pc
* /usr/lib/systemd/system/proftpd.service
* /usr/share/doc/proftpd-1.3.8b/ChangeLog
* /usr/share/doc/proftpd-1.3.8b/COPYING
* /usr/share/doc/proftpd-1.3.8b/CREDITS
* /usr/share/doc/proftpd-1.3.8b/INSTALL
* /usr/share/doc/proftpd-1.3.8b/NEWS
* /usr/share/doc/proftpd-1.3.8b/README.AIX
* /usr/share/doc/proftpd-1.3.8b/README.cygwin
* /usr/share/doc/proftpd-1.3.8b/README.FreeBSD
* /usr/share/doc/proftpd-1.3.8b/README.LDAP
* /usr/share/doc/proftpd-1.3.8b/README.md
* /usr/share/doc/proftpd-1.3.8b/README.modules
* /usr/share/doc/proftpd-1.3.8b/README.ports
* /usr/share/doc/proftpd-1.3.8b/README.Solaris2.5x
* /usr/share/doc/proftpd-1.3.8b/README.Unixware
* /usr/share/doc/proftpd-1.3.8b/RELEASE_NOTES
* /usr/share/man/man1/ftpasswd.1.gz
* /usr/share/man/man1/ftpcount.1.gz
* /usr/share/man/man1/ftpmail.1.gz
* /usr/share/man/man1/ftpquota.1.gz
* /usr/share/man/man1/ftptop.1.gz
* /usr/share/man/man1/ftpwho.1.gz
* /usr/share/man/man5/proftpd.conf.5.gz
* /usr/share/man/man5/xferlog.5.gz
* /usr/share/man/man8/ftpdctl.8.gz
* /usr/share/man/man8/ftpscrub.8.gz
* /usr/share/man/man8/ftpshut.8.gz
* /usr/share/man/man8/proftpd.8.gz
{{< /spoiler >}}