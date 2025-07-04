+++
draft = false
title = "bash 5.3-1"
version = "5.3-1"
description = "The GNU Bourne Again shell"
date = "2025-07-04T09:42:23"
aliases = "/packages/2347"
categories = ['base']
upstreamurl = "http://tiswww.case.edu/php/chet/bash/bashtop.html"
arch = "x86_64"
size = "1314620"
usize = "4761987"
sha1sum = "f56e8a7edef00f76e553b6f8adc3703b88170d29"
depends = "['glibc>=2.37', 'readline>=8.3']"
reverse_depends = "['autoconf', 'automake', 'backupninja', 'bash-completion', 'bzip2', 'coreutils', 'cpio', 'diffutils', 'dosfstools', 'dracut', 'findutils', 'flex', 'gradle', 'gzip', 'kbd', 'keychain', 'less', 'lesspipe', 'libtool', 'lxc', 'lynis', 'make', 'maxima', 'neofetch', 'nvm', 'openresolv', 'os-prober', 'pacman-tools', 'prettyping', 'pulse-autoconf', 'pyenv', 'rpcbind', 'screenfetch', 'scriptlet-core', 'steamtinkerlaunch', 'systemd-swap', 'tar', 'wgetpaste']"
+++
### Description: 
The GNU Bourne Again shell

### Files: 
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
* /usr/include/bash/include/posixselect.h
* /usr/include/bash/include/posixstat.h
* /usr/include/bash/include/posixtime.h
* /usr/include/bash/include/posixwait.h
* /usr/include/bash/include/shmbchar.h
* /usr/include/bash/include/shmbutil.h
* /usr/include/bash/include/shtty.h
* /usr/include/bash/include/stat-time.h
* /usr/include/bash/include/stdc.h
* /usr/include/bash/include/systimes.h
* /usr/include/bash/include/timer.h
* /usr/include/bash/include/typemax.h
* /usr/include/bash/include/unionwait.h
* /usr/include/bash/include/unlocked-io.h
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
* /usr/lib/bash/chmod
* /usr/lib/bash/csv
* /usr/lib/bash/cut
* /usr/lib/bash/dirname
* /usr/lib/bash/dsv
* /usr/lib/bash/fdflags
* /usr/lib/bash/finfo
* /usr/lib/bash/fltexpr
* /usr/lib/bash/getconf
* /usr/lib/bash/head
* /usr/lib/bash/id
* /usr/lib/bash/kv
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
* /usr/lib/bash/strptime
* /usr/lib/bash/sync
* /usr/lib/bash/tee
* /usr/lib/bash/truefalse
* /usr/lib/bash/tty
* /usr/lib/bash/uname
* /usr/lib/bash/unlink
* /usr/lib/bash/whoami
* /usr/lib/pkgconfig/bash.pc
* /usr/share/doc/bash-5.3/AUTHORS
* /usr/share/doc/bash-5.3/bash.html
* /usr/share/doc/bash-5.3/bashref.html
* /usr/share/doc/bash-5.3/ChangeLog
* /usr/share/doc/bash-5.3/CHANGES
* /usr/share/doc/bash-5.3/COMPAT
* /usr/share/doc/bash-5.3/COPYING
* /usr/share/doc/bash-5.3/FAQ
* /usr/share/doc/bash-5.3/INSTALL
* /usr/share/doc/bash-5.3/INTRO
* /usr/share/doc/bash-5.3/MANIFEST
* /usr/share/doc/bash-5.3/NEWS
* /usr/share/doc/bash-5.3/POSIX
* /usr/share/doc/bash-5.3/RBASH
* /usr/share/doc/bash-5.3/README
* /usr/share/info/bash.info.gz
* /usr/share/man/man1/bash.1.gz
* /usr/share/man/man1/bashbug.1.gz
