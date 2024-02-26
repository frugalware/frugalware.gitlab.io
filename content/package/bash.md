+++
draft = false
title = "bash 5.2.21-2"
version = "5.2.21-2"
description = "The GNU Bourne Again shell"
date = "2024-01-02T17:16:51"
aliases = "/packages/2347"
categories = ['base']
upstreamurl = "http://tiswww.case.edu/php/chet/bash/bashtop.html"
arch = "x86_64"
size = "1829048"
usize = "9799935"
sha1sum = "cb28fedd1986ecda11fc98358eb409d7186d51eb"
depends = "['glibc>=2.37', 'readline>=8.2']"
reverse_depends = "['autoconf', 'autoconf213', 'automake', 'backupninja', 'bash-completion', 'bzip2', 'coreutils', 'cpio', 'diffutils', 'dosfstools', 'dracut', 'findutils', 'flex', 'gradle', 'gzip', 'kbd', 'keychain', 'less', 'lesspipe', 'libtool', 'lxc', 'lynis', 'make', 'maxima', 'neofetch', 'nvm', 'openresolv', 'os-prober', 'pacman-tools', 'prettyping', 'pulse-autoconf', 'pyenv', 'rpcbind', 'screenfetch', 'scriptlet-core', 'steamtinkerlaunch', 'systemd-swap', 'tar', 'wgetpaste']"
+++
The GNU Bourne Again shell

## Files: 
* /etc/bashrc
* /etc/profile
* /etc/shells
* /etc/skel/.bashrc
* /usr/bin/bash
* /usr/bin/bashbug
* /usr/bin/sh
* /usr/include/bash/alias.h
* /usr/include/bash/array.h
* /usr/include/bash/arrayfunc.h
* /usr/include/bash/assoc.h
* /usr/include/bash/bashansi.h
* /usr/include/bash/bashintl.h
* /usr/include/bash/bashjmp.h
* /usr/include/bash/bashtypes.h
* /usr/include/bash/builtins.h
* /usr/include/bash/builtins/bashgetopt.h
* /usr/include/bash/builtins/builtext.h
* /usr/include/bash/builtins/common.h
* /usr/include/bash/builtins/getopt.h
* /usr/include/bash/command.h
* /usr/include/bash/config-bot.h
* /usr/include/bash/config-top.h
* /usr/include/bash/config.h
* /usr/include/bash/conftypes.h
* /usr/include/bash/dispose_cmd.h
* /usr/include/bash/error.h
* /usr/include/bash/execute_cmd.h
* /usr/include/bash/externs.h
* /usr/include/bash/general.h
* /usr/include/bash/hashlib.h
* /usr/include/bash/include/ansi_stdlib.h
* /usr/include/bash/include/chartypes.h
* /usr/include/bash/include/filecntl.h
* /usr/include/bash/include/gettext.h
* /usr/include/bash/include/maxpath.h
* /usr/include/bash/include/memalloc.h
* /usr/include/bash/include/ocache.h
* /usr/include/bash/include/posixdir.h
* /usr/include/bash/include/posixjmp.h
* /usr/include/bash/include/posixstat.h
* /usr/include/bash/include/posixtime.h
* /usr/include/bash/include/posixwait.h
* /usr/include/bash/include/shmbchar.h
* /usr/include/bash/include/shmbutil.h
* /usr/include/bash/include/shtty.h
* /usr/include/bash/include/stat-time.h
* /usr/include/bash/include/stdc.h
* /usr/include/bash/include/systimes.h
* /usr/include/bash/include/typemax.h
* /usr/include/bash/include/unionwait.h
* /usr/include/bash/jobs.h
* /usr/include/bash/make_cmd.h
* /usr/include/bash/pathnames.h
* /usr/include/bash/quit.h
* /usr/include/bash/shell.h
* /usr/include/bash/sig.h
* /usr/include/bash/siglist.h
* /usr/include/bash/signames.h
* /usr/include/bash/subst.h
* /usr/include/bash/syntax.h
* /usr/include/bash/unwind_prot.h
* /usr/include/bash/variables.h
* /usr/include/bash/version.h
* /usr/include/bash/xmalloc.h
* /usr/include/bash/y.tab.h
* /usr/lib/bash/accept
* /usr/lib/bash/basename
* /usr/lib/bash/csv
* /usr/lib/bash/cut
* /usr/lib/bash/dirname
* /usr/lib/bash/dsv
* /usr/lib/bash/fdflags
* /usr/lib/bash/finfo
* /usr/lib/bash/getconf
* /usr/lib/bash/head
* /usr/lib/bash/id
* /usr/lib/bash/ln
* /usr/lib/bash/loadables.h
* /usr/lib/bash/logname
* /usr/lib/bash/Makefile.inc
* /usr/lib/bash/Makefile.sample
* /usr/lib/bash/mkdir
* /usr/lib/bash/mkfifo
* /usr/lib/bash/mktemp
* /usr/lib/bash/mypid
* /usr/lib/bash/pathchk
* /usr/lib/bash/print
* /usr/lib/bash/printenv
* /usr/lib/bash/push
* /usr/lib/bash/realpath
* /usr/lib/bash/rm
* /usr/lib/bash/rmdir
* /usr/lib/bash/seq
* /usr/lib/bash/setpgid
* /usr/lib/bash/sleep
* /usr/lib/bash/stat
* /usr/lib/bash/strftime
* /usr/lib/bash/sync
* /usr/lib/bash/tee
* /usr/lib/bash/truefalse
* /usr/lib/bash/tty
* /usr/lib/bash/uname
* /usr/lib/bash/unlink
* /usr/lib/bash/whoami
* /usr/lib/pkgconfig/bash.pc
* /usr/share/doc/bash-5.2.21/AUTHORS
* /usr/share/doc/bash-5.2.21/bash.html
* /usr/share/doc/bash-5.2.21/bashref.html
* /usr/share/doc/bash-5.2.21/ChangeLog
* /usr/share/doc/bash-5.2.21/CHANGES
* /usr/share/doc/bash-5.2.21/COMPAT
* /usr/share/doc/bash-5.2.21/COPYING
* /usr/share/doc/bash-5.2.21/FAQ
* /usr/share/doc/bash-5.2.21/INSTALL
* /usr/share/doc/bash-5.2.21/INTRO
* /usr/share/doc/bash-5.2.21/MANIFEST
* /usr/share/doc/bash-5.2.21/NEWS
* /usr/share/doc/bash-5.2.21/POSIX
* /usr/share/doc/bash-5.2.21/RBASH
* /usr/share/doc/bash-5.2.21/README
* /usr/share/info/bash.info.gz
* /usr/share/locale/af/LC_MESSAGES/bash.mo
* /usr/share/locale/bg/LC_MESSAGES/bash.mo
* /usr/share/locale/ca/LC_MESSAGES/bash.mo
* /usr/share/locale/cs/LC_MESSAGES/bash.mo
* /usr/share/locale/da/LC_MESSAGES/bash.mo
* /usr/share/locale/de/LC_MESSAGES/bash.mo
* /usr/share/locale/el/LC_MESSAGES/bash.mo
* /usr/share/locale/en@boldquot/LC_MESSAGES/bash.mo
* /usr/share/locale/en@quot/LC_MESSAGES/bash.mo
* /usr/share/locale/eo/LC_MESSAGES/bash.mo
* /usr/share/locale/es/LC_MESSAGES/bash.mo
* /usr/share/locale/et/LC_MESSAGES/bash.mo
* /usr/share/locale/fi/LC_MESSAGES/bash.mo
* /usr/share/locale/fr/LC_MESSAGES/bash.mo
* /usr/share/locale/ga/LC_MESSAGES/bash.mo
* /usr/share/locale/gl/LC_MESSAGES/bash.mo
* /usr/share/locale/hr/LC_MESSAGES/bash.mo
* /usr/share/locale/hu/LC_MESSAGES/bash.mo
* /usr/share/locale/id/LC_MESSAGES/bash.mo
* /usr/share/locale/it/LC_MESSAGES/bash.mo
* /usr/share/locale/ja/LC_MESSAGES/bash.mo
* /usr/share/locale/ko/LC_MESSAGES/bash.mo
* /usr/share/locale/lt/LC_MESSAGES/bash.mo
* /usr/share/locale/nb/LC_MESSAGES/bash.mo
* /usr/share/locale/nl/LC_MESSAGES/bash.mo
* /usr/share/locale/pl/LC_MESSAGES/bash.mo
* /usr/share/locale/pt/LC_MESSAGES/bash.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/bash.mo
* /usr/share/locale/ro/LC_MESSAGES/bash.mo
* /usr/share/locale/ru/LC_MESSAGES/bash.mo
* /usr/share/locale/sk/LC_MESSAGES/bash.mo
* /usr/share/locale/sl/LC_MESSAGES/bash.mo
* /usr/share/locale/sr/LC_MESSAGES/bash.mo
* /usr/share/locale/sv/LC_MESSAGES/bash.mo
* /usr/share/locale/tr/LC_MESSAGES/bash.mo
* /usr/share/locale/uk/LC_MESSAGES/bash.mo
* /usr/share/locale/vi/LC_MESSAGES/bash.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/bash.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/bash.mo
* /usr/share/man/man1/bash.1.gz
* /usr/share/man/man1/bashbug.1.gz
