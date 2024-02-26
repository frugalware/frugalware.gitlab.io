+++
draft = false
title = "dovecot-sieve 0.5.21-1"
version = "0.5.21-1"
description = "Sieve Support for Dovecot"
date = "2023-12-04T12:54:55"
aliases = "/packages/219810"
categories = ['network-extra']
upstreamurl = "https://pigeonhole.dovecot.org/"
arch = "x86_64"
size = "609736"
usize = "3039081"
sha1sum = "1592ed6e780b5a77a2daf71320fa12bf4a1cafdf"
depends = "['dovecot>=2.3.21']"
+++
Sieve Support for Dovecot{{< files text="show files" >}}* /usr/bin/sieve-dump
* /usr/bin/sieve-filter
* /usr/bin/sieve-test
* /usr/bin/sievec
* /usr/include/dovecot/sieve/edit-mail.h
* /usr/include/dovecot/sieve/mail-raw.h
* /usr/include/dovecot/sieve/pigeonhole-config.h
* /usr/include/dovecot/sieve/pigeonhole-version.h
* /usr/include/dovecot/sieve/rfc2822.h
* /usr/include/dovecot/sieve/sieve-actions.h
* /usr/include/dovecot/sieve/sieve-address-parts.h
* /usr/include/dovecot/sieve/sieve-address-source.h
* /usr/include/dovecot/sieve/sieve-address.h
* /usr/include/dovecot/sieve/sieve-ast.h
* /usr/include/dovecot/sieve/sieve-binary-dumper.h
* /usr/include/dovecot/sieve/sieve-binary-private.h
* /usr/include/dovecot/sieve/sieve-binary.h
* /usr/include/dovecot/sieve/sieve-code-dumper.h
* /usr/include/dovecot/sieve/sieve-code.h
* /usr/include/dovecot/sieve/sieve-commands.h
* /usr/include/dovecot/sieve/sieve-common.h
* /usr/include/dovecot/sieve/sieve-comparators.h
* /usr/include/dovecot/sieve/sieve-config.h
* /usr/include/dovecot/sieve/sieve-dump.h
* /usr/include/dovecot/sieve/sieve-error-private.h
* /usr/include/dovecot/sieve/sieve-error.h
* /usr/include/dovecot/sieve/sieve-execute.h
* /usr/include/dovecot/sieve/sieve-ext-copy.h
* /usr/include/dovecot/sieve/sieve-ext-enotify.h
* /usr/include/dovecot/sieve/sieve-ext-environment.h
* /usr/include/dovecot/sieve/sieve-ext-imap4flags.h
* /usr/include/dovecot/sieve/sieve-ext-mailbox.h
* /usr/include/dovecot/sieve/sieve-ext-variables.h
* /usr/include/dovecot/sieve/sieve-extensions.h
* /usr/include/dovecot/sieve/sieve-generator.h
* /usr/include/dovecot/sieve/sieve-interpreter.h
* /usr/include/dovecot/sieve/sieve-lexer.h
* /usr/include/dovecot/sieve/sieve-limits.h
* /usr/include/dovecot/sieve/sieve-match-types.h
* /usr/include/dovecot/sieve/sieve-match.h
* /usr/include/dovecot/sieve/sieve-message.h
* /usr/include/dovecot/sieve/sieve-objects.h
* /usr/include/dovecot/sieve/sieve-parser.h
* /usr/include/dovecot/sieve/sieve-plugins.h
* /usr/include/dovecot/sieve/sieve-result.h
* /usr/include/dovecot/sieve/sieve-runtime-trace.h
* /usr/include/dovecot/sieve/sieve-runtime.h
* /usr/include/dovecot/sieve/sieve-script-private.h
* /usr/include/dovecot/sieve/sieve-script.h
* /usr/include/dovecot/sieve/sieve-settings.h
* /usr/include/dovecot/sieve/sieve-smtp.h
* /usr/include/dovecot/sieve/sieve-storage-private.h
* /usr/include/dovecot/sieve/sieve-storage.h
* /usr/include/dovecot/sieve/sieve-stringlist.h
* /usr/include/dovecot/sieve/sieve-types.h
* /usr/include/dovecot/sieve/sieve-validator.h
* /usr/include/dovecot/sieve/sieve.h
* /usr/lib/dovecot/dovecot/managesieve
* /usr/lib/dovecot/dovecot/managesieve-login
* /usr/lib/dovecot/libdovecot-sieve.so
* /usr/lib/dovecot/libdovecot-sieve.so.0
* /usr/lib/dovecot/libdovecot-sieve.so.0.0.0
* /usr/lib/dovecot/modules/doveadm/lib10_doveadm_sieve_plugin.so
* /usr/lib/dovecot/modules/lib90_sieve_plugin.so
* /usr/lib/dovecot/modules/lib95_imap_filter_sieve_plugin.so
* /usr/lib/dovecot/modules/lib95_imap_sieve_plugin.so
* /usr/lib/dovecot/modules/settings/libmanagesieve_login_settings.so
* /usr/lib/dovecot/modules/settings/libmanagesieve_settings.so
* /usr/lib/dovecot/modules/settings/libpigeonhole_settings.so
* /usr/lib/dovecot/modules/sieve/lib10_sieve_storage_ldap_plugin.so
* /usr/lib/dovecot/modules/sieve/lib90_sieve_extprograms_plugin.so
* /usr/lib/dovecot/modules/sieve/lib90_sieve_imapsieve_plugin.so
* /usr/share/aclocal/dovecot-pigeonhole.m4
* /usr/share/doc/dovecot-2.3.21/example-config/conf.d/20-managesieve.conf
* /usr/share/doc/dovecot-2.3.21/example-config/conf.d/90-sieve-extprograms.conf
* /usr/share/doc/dovecot-2.3.21/example-config/conf.d/90-sieve.conf
* /usr/share/doc/dovecot-2.3.21/example-config/sieve-ldap.conf
* /usr/share/doc/dovecot-2.3.21/sieve/extensions/duplicate.txt
* /usr/share/doc/dovecot-2.3.21/sieve/extensions/editheader.txt
* /usr/share/doc/dovecot-2.3.21/sieve/extensions/include.txt
* /usr/share/doc/dovecot-2.3.21/sieve/extensions/spamtest-virustest.txt
* /usr/share/doc/dovecot-2.3.21/sieve/extensions/vacation.txt
* /usr/share/doc/dovecot-2.3.21/sieve/extensions/vnd.dovecot.environment.txt
* /usr/share/doc/dovecot-2.3.21/sieve/extensions/vnd.dovecot.report.txt
* /usr/share/doc/dovecot-2.3.21/sieve/locations/dict.txt
* /usr/share/doc/dovecot-2.3.21/sieve/locations/file.txt
* /usr/share/doc/dovecot-2.3.21/sieve/locations/ldap.txt
* /usr/share/doc/dovecot-2.3.21/sieve/plugins/imapsieve.txt
* /usr/share/doc/dovecot-2.3.21/sieve/plugins/imap_filter_sieve.txt
* /usr/share/doc/dovecot-2.3.21/sieve/plugins/sieve_extprograms.txt
* /usr/share/doc/dovecot-sieve-0.5.21/AUTHORS
* /usr/share/doc/dovecot-sieve-0.5.21/ChangeLog
* /usr/share/doc/dovecot-sieve-0.5.21/COPYING
* /usr/share/doc/dovecot-sieve-0.5.21/COPYING.LGPL
* /usr/share/doc/dovecot-sieve-0.5.21/INSTALL
* /usr/share/doc/dovecot-sieve-0.5.21/NEWS
* /usr/share/doc/dovecot-sieve-0.5.21/README
* /usr/share/doc/dovecot-sieve-0.5.21/TODO
* /usr/share/man/man1/doveadm-sieve.1.gz
* /usr/share/man/man1/sieve-dump.1.gz
* /usr/share/man/man1/sieve-filter.1.gz
* /usr/share/man/man1/sieve-test.1.gz
* /usr/share/man/man1/sievec.1.gz
* /usr/share/man/man1/sieved.1.gz
* /usr/share/man/man7/pigeonhole.7.gz
{{< /files >}}