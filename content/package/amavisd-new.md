+++
draft = false
title = "amavisd-new 2.11.1-3"
version = "2.11.1-3"
date = "2024-01-08T21:36:05"
categories = ['network-extra']
upstreamurl = "https://amavisd.de.postfix.org"
arch = "x86_64"
size = "601928"
usize = "2662395"
sha1sum = "84565a25025e66035ea613c35df212a9168a693c"
depends = "['perl-archive-zip', 'perl-berkeleydb', 'perl-convert-tnef', 'perl-convert-uulib', 'perl-io-stringy', 'perl-mailtools', 'perl-mime-tools', 'perl-net-server', 'perl-unix-syslog', 'spamassassin', 'systemd', 'perl-convert-binhex']"
files = "['etc/', 'etc/amavis/', 'etc/amavis/10-amavisconf', 'etc/amavis/20-userconf', 'etc/tmpfiles.d/', 'etc/tmpfiles.d/amavisd-new.conf', 'usr/', 'usr/bin/', 'usr/bin/amavisd', 'usr/bin/amavisd-agent', 'usr/bin/amavisd-nanny', 'usr/lib/', 'usr/lib/amavisd-new/', 'usr/lib/amavisd-new/amavisd-wrapper', 'usr/lib/systemd/', 'usr/lib/systemd/system/', 'usr/lib/systemd/system/amavisd-new.service', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/amavisd-new-2.11.1/', 'usr/share/doc/amavisd-new-2.11.1/AAAREADME.first', 'usr/share/doc/amavisd-new-2.11.1/INSTALL', 'usr/share/doc/amavisd-new-2.11.1/LICENSE', 'usr/share/doc/amavisd-new-2.11.1/MANIFEST', 'usr/share/doc/amavisd-new-2.11.1/README.Frugalware', 'usr/share/doc/amavisd-new-2.11.1/RELEASE_NOTES', 'usr/share/doc/amavisd-new-2.11.1/TODO', 'usr/share/doc/amavisd-new-2.11.1/examples/', 'usr/share/doc/amavisd-new-2.11.1/examples/amavisd-release', 'usr/share/doc/amavisd-new-2.11.1/examples/amavisd.conf-default', 'usr/share/doc/amavisd-new-2.11.1/ldap/', 'usr/share/doc/amavisd-new-2.11.1/ldap/amavis.schema', 'usr/share/doc/amavisd-new-2.11.1/sample-messages/', 'usr/share/doc/amavisd-new-2.11.1/sample-messages/README', 'usr/share/doc/amavisd-new-2.11.1/sample-messages/sample.tar.gz.compl', 'var/', 'var/lib/', 'var/lib/amavis/', 'var/lib/amavis/db/', 'var/lib/amavis/helpers/', 'var/lib/amavis/home/', 'var/lib/amavis/quarantine/', 'var/lib/amavis/tmp/', 'var/lib/amavis/var/']"
+++
Amavisd-new is a high-performance interface between mailer (MTA) and content checkers