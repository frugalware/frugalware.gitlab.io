+++
draft = false
title = "logcheck 1.4.3-2"
version = "1.4.3-2"
description = "allow a system administrator to view the logfiles under their control"
date = "2024-06-18T14:34:58"
aliases = "/packages/219141"
categories = ['apps-extra']
upstreamurl = "http://logcheck.org/"
arch = "x86_64"
size = "72088"
usize = "380028"
sha1sum = "b7f77f5bbb1b6c5997882483581d8e7f45d54504"
depends = "[]"
+++
### Description: 
allow a system administrator to view the logfiles under their control

### Files: 
* /etc/logcheck/cracking.d/kernel
* /etc/logcheck/cracking.d/rlogind
* /etc/logcheck/cracking.d/rsh
* /etc/logcheck/cracking.d/smartd
* /etc/logcheck/cracking.d/tftpd
* /etc/logcheck/cracking.d/uucico
* /etc/logcheck/ignore.d.paranoid/bind
* /etc/logcheck/ignore.d.paranoid/cron
* /etc/logcheck/ignore.d.paranoid/incron
* /etc/logcheck/ignore.d.paranoid/logcheck
* /etc/logcheck/ignore.d.paranoid/postfix
* /etc/logcheck/ignore.d.paranoid/ppp
* /etc/logcheck/ignore.d.paranoid/pureftp
* /etc/logcheck/ignore.d.paranoid/qpopper
* /etc/logcheck/ignore.d.paranoid/squid
* /etc/logcheck/ignore.d.paranoid/ssh
* /etc/logcheck/ignore.d.paranoid/stunnel
* /etc/logcheck/ignore.d.paranoid/sysklogd
* /etc/logcheck/ignore.d.paranoid/telnetd
* /etc/logcheck/ignore.d.paranoid/tripwire
* /etc/logcheck/ignore.d.paranoid/usb
* /etc/logcheck/ignore.d.server/acpid
* /etc/logcheck/ignore.d.server/amandad
* /etc/logcheck/ignore.d.server/amavisd-new
* /etc/logcheck/ignore.d.server/anacron
* /etc/logcheck/ignore.d.server/anon-proxy
* /etc/logcheck/ignore.d.server/apache
* /etc/logcheck/ignore.d.server/apcupsd
* /etc/logcheck/ignore.d.server/arpwatch
* /etc/logcheck/ignore.d.server/asterisk
* /etc/logcheck/ignore.d.server/automount
* /etc/logcheck/ignore.d.server/bind
* /etc/logcheck/ignore.d.server/bluez-utils
* /etc/logcheck/ignore.d.server/courier
* /etc/logcheck/ignore.d.server/cpqarrayd
* /etc/logcheck/ignore.d.server/cpufreqd
* /etc/logcheck/ignore.d.server/cron
* /etc/logcheck/ignore.d.server/cron-apt
* /etc/logcheck/ignore.d.server/cups-lpd
* /etc/logcheck/ignore.d.server/cvs-pserver
* /etc/logcheck/ignore.d.server/cvsd
* /etc/logcheck/ignore.d.server/cyrus
* /etc/logcheck/ignore.d.server/dcc
* /etc/logcheck/ignore.d.server/ddclient
* /etc/logcheck/ignore.d.server/dhclient
* /etc/logcheck/ignore.d.server/dhcp
* /etc/logcheck/ignore.d.server/dictd
* /etc/logcheck/ignore.d.server/dkfilter
* /etc/logcheck/ignore.d.server/dnsmasq
* /etc/logcheck/ignore.d.server/dovecot
* /etc/logcheck/ignore.d.server/dropbear
* /etc/logcheck/ignore.d.server/dspam
* /etc/logcheck/ignore.d.server/epmd
* /etc/logcheck/ignore.d.server/exim4
* /etc/logcheck/ignore.d.server/fcron
* /etc/logcheck/ignore.d.server/ftpd
* /etc/logcheck/ignore.d.server/git-daemon
* /etc/logcheck/ignore.d.server/gnu-imap4d
* /etc/logcheck/ignore.d.server/gps
* /etc/logcheck/ignore.d.server/grinch
* /etc/logcheck/ignore.d.server/horde3
* /etc/logcheck/ignore.d.server/hplip
* /etc/logcheck/ignore.d.server/hylafax
* /etc/logcheck/ignore.d.server/ikiwiki
* /etc/logcheck/ignore.d.server/imap
* /etc/logcheck/ignore.d.server/imapproxy
* /etc/logcheck/ignore.d.server/imp
* /etc/logcheck/ignore.d.server/imp4
* /etc/logcheck/ignore.d.server/innd
* /etc/logcheck/ignore.d.server/ipppd
* /etc/logcheck/ignore.d.server/isdnlog
* /etc/logcheck/ignore.d.server/isdnutils
* /etc/logcheck/ignore.d.server/jabberd
* /etc/logcheck/ignore.d.server/kernel
* /etc/logcheck/ignore.d.server/klogind
* /etc/logcheck/ignore.d.server/krb5-kdc
* /etc/logcheck/ignore.d.server/libpam-krb5
* /etc/logcheck/ignore.d.server/libpam-mount
* /etc/logcheck/ignore.d.server/logcheck
* /etc/logcheck/ignore.d.server/login
* /etc/logcheck/ignore.d.server/maradns
* /etc/logcheck/ignore.d.server/mldonkey-server
* /etc/logcheck/ignore.d.server/mon
* /etc/logcheck/ignore.d.server/mountd
* /etc/logcheck/ignore.d.server/nagios
* /etc/logcheck/ignore.d.server/netconsole
* /etc/logcheck/ignore.d.server/nfs
* /etc/logcheck/ignore.d.server/nntpcache
* /etc/logcheck/ignore.d.server/nscd
* /etc/logcheck/ignore.d.server/nslcd
* /etc/logcheck/ignore.d.server/openvpn
* /etc/logcheck/ignore.d.server/otrs
* /etc/logcheck/ignore.d.server/passwd
* /etc/logcheck/ignore.d.server/pdns
* /etc/logcheck/ignore.d.server/perdition
* /etc/logcheck/ignore.d.server/policyd
* /etc/logcheck/ignore.d.server/popa3d
* /etc/logcheck/ignore.d.server/postfix
* /etc/logcheck/ignore.d.server/postfix-policyd
* /etc/logcheck/ignore.d.server/ppp
* /etc/logcheck/ignore.d.server/pptpd
* /etc/logcheck/ignore.d.server/procmail
* /etc/logcheck/ignore.d.server/proftpd
* /etc/logcheck/ignore.d.server/pure-ftpd
* /etc/logcheck/ignore.d.server/pureftp
* /etc/logcheck/ignore.d.server/qpopper
* /etc/logcheck/ignore.d.server/rbldnsd
* /etc/logcheck/ignore.d.server/rpc_statd
* /etc/logcheck/ignore.d.server/rsnapshot
* /etc/logcheck/ignore.d.server/rsync
* /etc/logcheck/ignore.d.server/sa-exim
* /etc/logcheck/ignore.d.server/samba
* /etc/logcheck/ignore.d.server/saned
* /etc/logcheck/ignore.d.server/sasl2-bin
* /etc/logcheck/ignore.d.server/saslauthd
* /etc/logcheck/ignore.d.server/schroot
* /etc/logcheck/ignore.d.server/scponly
* /etc/logcheck/ignore.d.server/slapd
* /etc/logcheck/ignore.d.server/smartd
* /etc/logcheck/ignore.d.server/smbd_audit
* /etc/logcheck/ignore.d.server/smokeping
* /etc/logcheck/ignore.d.server/snmpd
* /etc/logcheck/ignore.d.server/snort
* /etc/logcheck/ignore.d.server/spamc
* /etc/logcheck/ignore.d.server/spamd
* /etc/logcheck/ignore.d.server/squid
* /etc/logcheck/ignore.d.server/ssh
* /etc/logcheck/ignore.d.server/stunnel
* /etc/logcheck/ignore.d.server/su
* /etc/logcheck/ignore.d.server/sudo
* /etc/logcheck/ignore.d.server/sympa
* /etc/logcheck/ignore.d.server/syslogd
* /etc/logcheck/ignore.d.server/systemd
* /etc/logcheck/ignore.d.server/systemd-logind
* /etc/logcheck/ignore.d.server/systemd-timesyncd
* /etc/logcheck/ignore.d.server/teapop
* /etc/logcheck/ignore.d.server/telnetd
* /etc/logcheck/ignore.d.server/tftpd
* /etc/logcheck/ignore.d.server/thy
* /etc/logcheck/ignore.d.server/ucd-snmp
* /etc/logcheck/ignore.d.server/upsd
* /etc/logcheck/ignore.d.server/uptimed
* /etc/logcheck/ignore.d.server/userv
* /etc/logcheck/ignore.d.server/vsftpd
* /etc/logcheck/ignore.d.server/watchdog
* /etc/logcheck/ignore.d.server/wu-ftpd
* /etc/logcheck/ignore.d.server/xinetd
* /etc/logcheck/ignore.d.workstation/automount
* /etc/logcheck/ignore.d.workstation/bind
* /etc/logcheck/ignore.d.workstation/bluetooth-alsa
* /etc/logcheck/ignore.d.workstation/bluez-utils
* /etc/logcheck/ignore.d.workstation/bonobo
* /etc/logcheck/ignore.d.workstation/dhcpcd
* /etc/logcheck/ignore.d.workstation/francine
* /etc/logcheck/ignore.d.workstation/gconf
* /etc/logcheck/ignore.d.workstation/gdm
* /etc/logcheck/ignore.d.workstation/hald
* /etc/logcheck/ignore.d.workstation/hcid
* /etc/logcheck/ignore.d.workstation/ifplugd
* /etc/logcheck/ignore.d.workstation/ippl
* /etc/logcheck/ignore.d.workstation/kdm
* /etc/logcheck/ignore.d.workstation/kernel
* /etc/logcheck/ignore.d.workstation/laptop-mode-tools
* /etc/logcheck/ignore.d.workstation/libmtp-runtime
* /etc/logcheck/ignore.d.workstation/libpam-gnome-keyring
* /etc/logcheck/ignore.d.workstation/logcheck
* /etc/logcheck/ignore.d.workstation/login
* /etc/logcheck/ignore.d.workstation/net-acct
* /etc/logcheck/ignore.d.workstation/nntpcache
* /etc/logcheck/ignore.d.workstation/polypaudio
* /etc/logcheck/ignore.d.workstation/postfix
* /etc/logcheck/ignore.d.workstation/ppp
* /etc/logcheck/ignore.d.workstation/proftpd
* /etc/logcheck/ignore.d.workstation/pump
* /etc/logcheck/ignore.d.workstation/sendfile
* /etc/logcheck/ignore.d.workstation/slim
* /etc/logcheck/ignore.d.workstation/squid
* /etc/logcheck/ignore.d.workstation/udev
* /etc/logcheck/ignore.d.workstation/wdm
* /etc/logcheck/ignore.d.workstation/winbind
* /etc/logcheck/ignore.d.workstation/wpasupplicant
* /etc/logcheck/ignore.d.workstation/xdm
* /etc/logcheck/ignore.d.workstation/xlockmore
* /etc/logcheck/logcheck.conf
* /etc/logcheck/logcheck.logfiles
* /etc/logcheck/logcheck.logfiles.d/journal.logfiles
* /etc/logcheck/logcheck.logfiles.d/syslog.logfiles
* /etc/logcheck/violations.d/kernel
* /etc/logcheck/violations.d/logcheck
* /etc/logcheck/violations.d/smartd
* /etc/logcheck/violations.d/su
* /etc/logcheck/violations.d/sudo
* /etc/logcheck/violations.ignore.d/logcheck-su
* /etc/logcheck/violations.ignore.d/logcheck-sudo
* /usr/bin/logcheck-test
* /usr/lib/sysusers.d/logcheck.conf
* /usr/lib/tmpfiles.d/logcheck.conf
* /usr/sbin/logcheck
* /usr/sbin/logtail
* /usr/sbin/logtail2
* /usr/share/doc/logcheck-1.4.3/AUTHORS
* /usr/share/doc/logcheck-1.4.3/CHANGES
* /usr/share/doc/logcheck-1.4.3/CREDITS
* /usr/share/doc/logcheck-1.4.3/INSTALL
* /usr/share/doc/logcheck-1.4.3/LICENSE
* /usr/share/doc/logcheck-1.4.3/TODO
* /usr/share/logtail/detectrotate/10-savelog.dtr
* /usr/share/logtail/detectrotate/20-logrotate.dtr
* /usr/share/logtail/detectrotate/30-logrotate-dateext.dtr
