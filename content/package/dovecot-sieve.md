+++
draft = false
title = "dovecot-sieve 0.5.20-1"
version = "0.5.20-1"
date = "2023-07-10T10:04:06"
categories = ['network-extra']
upstreamurl = "https://pigeonhole.dovecot.org/"
arch = "x86_64"
size = "3037357"
usize = "0"
sha1sum = ""
depends = "['dovecot>=2.3.20']"
files = "['usr/', 'usr/bin/', 'usr/bin/sieve-dump', 'usr/bin/sieve-filter', 'usr/bin/sieve-test', 'usr/bin/sievec', 'usr/include/', 'usr/include/dovecot/', 'usr/include/dovecot/sieve/', 'usr/include/dovecot/sieve/edit-mail.h', 'usr/include/dovecot/sieve/mail-raw.h', 'usr/include/dovecot/sieve/pigeonhole-config.h', 'usr/include/dovecot/sieve/pigeonhole-version.h', 'usr/include/dovecot/sieve/rfc2822.h', 'usr/include/dovecot/sieve/sieve-actions.h', 'usr/include/dovecot/sieve/sieve-address-parts.h', 'usr/include/dovecot/sieve/sieve-address-source.h', 'usr/include/dovecot/sieve/sieve-address.h', 'usr/include/dovecot/sieve/sieve-ast.h', 'usr/include/dovecot/sieve/sieve-binary-dumper.h', 'usr/include/dovecot/sieve/sieve-binary-private.h', 'usr/include/dovecot/sieve/sieve-binary.h', 'usr/include/dovecot/sieve/sieve-code-dumper.h', 'usr/include/dovecot/sieve/sieve-code.h', 'usr/include/dovecot/sieve/sieve-commands.h', 'usr/include/dovecot/sieve/sieve-common.h', 'usr/include/dovecot/sieve/sieve-comparators.h', 'usr/include/dovecot/sieve/sieve-config.h', 'usr/include/dovecot/sieve/sieve-dump.h', 'usr/include/dovecot/sieve/sieve-error-private.h', 'usr/include/dovecot/sieve/sieve-error.h', 'usr/include/dovecot/sieve/sieve-execute.h', 'usr/include/dovecot/sieve/sieve-ext-copy.h', 'usr/include/dovecot/sieve/sieve-ext-enotify.h', 'usr/include/dovecot/sieve/sieve-ext-environment.h', 'usr/include/dovecot/sieve/sieve-ext-imap4flags.h', 'usr/include/dovecot/sieve/sieve-ext-mailbox.h', 'usr/include/dovecot/sieve/sieve-ext-variables.h', 'usr/include/dovecot/sieve/sieve-extensions.h', 'usr/include/dovecot/sieve/sieve-generator.h', 'usr/include/dovecot/sieve/sieve-interpreter.h', 'usr/include/dovecot/sieve/sieve-lexer.h', 'usr/include/dovecot/sieve/sieve-limits.h', 'usr/include/dovecot/sieve/sieve-match-types.h', 'usr/include/dovecot/sieve/sieve-match.h', 'usr/include/dovecot/sieve/sieve-message.h', 'usr/include/dovecot/sieve/sieve-objects.h', 'usr/include/dovecot/sieve/sieve-parser.h', 'usr/include/dovecot/sieve/sieve-plugins.h', 'usr/include/dovecot/sieve/sieve-result.h', 'usr/include/dovecot/sieve/sieve-runtime-trace.h', 'usr/include/dovecot/sieve/sieve-runtime.h', 'usr/include/dovecot/sieve/sieve-script-private.h', 'usr/include/dovecot/sieve/sieve-script.h', 'usr/include/dovecot/sieve/sieve-settings.h', 'usr/include/dovecot/sieve/sieve-smtp.h', 'usr/include/dovecot/sieve/sieve-storage-private.h', 'usr/include/dovecot/sieve/sieve-storage.h', 'usr/include/dovecot/sieve/sieve-stringlist.h', 'usr/include/dovecot/sieve/sieve-types.h', 'usr/include/dovecot/sieve/sieve-validator.h', 'usr/include/dovecot/sieve/sieve.h', 'usr/lib/', 'usr/lib/dovecot/', 'usr/lib/dovecot/dovecot/', 'usr/lib/dovecot/dovecot/managesieve', 'usr/lib/dovecot/dovecot/managesieve-login', 'usr/lib/dovecot/libdovecot-sieve.so', 'usr/lib/dovecot/libdovecot-sieve.so.0', 'usr/lib/dovecot/libdovecot-sieve.so.0.0.0', 'usr/lib/dovecot/modules/', 'usr/lib/dovecot/modules/doveadm/', 'usr/lib/dovecot/modules/doveadm/lib10_doveadm_sieve_plugin.so', 'usr/lib/dovecot/modules/lib90_sieve_plugin.so', 'usr/lib/dovecot/modules/lib95_imap_filter_sieve_plugin.so', 'usr/lib/dovecot/modules/lib95_imap_sieve_plugin.so', 'usr/lib/dovecot/modules/settings/', 'usr/lib/dovecot/modules/settings/libmanagesieve_login_settings.so', 'usr/lib/dovecot/modules/settings/libmanagesieve_settings.so', 'usr/lib/dovecot/modules/settings/libpigeonhole_settings.so', 'usr/lib/dovecot/modules/sieve/', 'usr/lib/dovecot/modules/sieve/lib10_sieve_storage_ldap_plugin.so', 'usr/lib/dovecot/modules/sieve/lib90_sieve_extprograms_plugin.so', 'usr/lib/dovecot/modules/sieve/lib90_sieve_imapsieve_plugin.so', 'usr/share/', 'usr/share/aclocal/', 'usr/share/aclocal/dovecot-pigeonhole.m4', 'usr/share/doc/', 'usr/share/doc/dovecot-2.3.20/', 'usr/share/doc/dovecot-2.3.20/example-config/', 'usr/share/doc/dovecot-2.3.20/example-config/conf.d/', 'usr/share/doc/dovecot-2.3.20/example-config/conf.d/20-managesieve.conf', 'usr/share/doc/dovecot-2.3.20/example-config/conf.d/90-sieve-extprograms.conf', 'usr/share/doc/dovecot-2.3.20/example-config/conf.d/90-sieve.conf', 'usr/share/doc/dovecot-2.3.20/example-config/sieve-ldap.conf', 'usr/share/doc/dovecot-2.3.20/sieve/', 'usr/share/doc/dovecot-2.3.20/sieve/extensions/', 'usr/share/doc/dovecot-2.3.20/sieve/extensions/duplicate.txt', 'usr/share/doc/dovecot-2.3.20/sieve/extensions/editheader.txt', 'usr/share/doc/dovecot-2.3.20/sieve/extensions/include.txt', 'usr/share/doc/dovecot-2.3.20/sieve/extensions/spamtest-virustest.txt', 'usr/share/doc/dovecot-2.3.20/sieve/extensions/vacation.txt', 'usr/share/doc/dovecot-2.3.20/sieve/extensions/vnd.dovecot.environment.txt', 'usr/share/doc/dovecot-2.3.20/sieve/extensions/vnd.dovecot.report.txt', 'usr/share/doc/dovecot-2.3.20/sieve/locations/', 'usr/share/doc/dovecot-2.3.20/sieve/locations/dict.txt', 'usr/share/doc/dovecot-2.3.20/sieve/locations/file.txt', 'usr/share/doc/dovecot-2.3.20/sieve/locations/ldap.txt', 'usr/share/doc/dovecot-2.3.20/sieve/plugins/', 'usr/share/doc/dovecot-2.3.20/sieve/plugins/imap_filter_sieve.txt', 'usr/share/doc/dovecot-2.3.20/sieve/plugins/imapsieve.txt', 'usr/share/doc/dovecot-2.3.20/sieve/plugins/sieve_extprograms.txt', 'usr/share/doc/dovecot-sieve-0.5.20/', 'usr/share/doc/dovecot-sieve-0.5.20/AUTHORS', 'usr/share/doc/dovecot-sieve-0.5.20/COPYING', 'usr/share/doc/dovecot-sieve-0.5.20/COPYING.LGPL', 'usr/share/doc/dovecot-sieve-0.5.20/ChangeLog', 'usr/share/doc/dovecot-sieve-0.5.20/INSTALL', 'usr/share/doc/dovecot-sieve-0.5.20/NEWS', 'usr/share/doc/dovecot-sieve-0.5.20/README', 'usr/share/doc/dovecot-sieve-0.5.20/TODO', 'usr/share/man/', 'usr/share/man/man1/', 'usr/share/man/man1/doveadm-sieve.1.gz', 'usr/share/man/man1/sieve-dump.1.gz', 'usr/share/man/man1/sieve-filter.1.gz', 'usr/share/man/man1/sieve-test.1.gz', 'usr/share/man/man1/sievec.1.gz', 'usr/share/man/man1/sieved.1.gz', 'usr/share/man/man7/', 'usr/share/man/man7/pigeonhole.7.gz']"
+++
Sieve Support for Dovecot