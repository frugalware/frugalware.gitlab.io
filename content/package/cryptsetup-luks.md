+++
draft = false
title = "cryptsetup-luks 2.7.0-1"
version = "2.7.0-1"
description = "cryptsetup-luks is intended as a complete replacement for the original cryptsetup."
date = "2024-01-24T12:59:25"
aliases = "/packages/14464"
categories = ['base']
upstreamurl = "https://gitlab.com/cryptsetup/cryptsetup"
arch = "x86_64"
size = "738896"
usize = "3056824"
sha1sum = "7250607ff5723af1a6aa1499e02751098a654766"
depends = "['argon2', 'json-c>=0.14', 'libblkid', 'libssh', 'libuuid>=2.31.1-3', 'lvm2-libs>=2.02.177-4', 'openssl>=3.1.0', 'popt>=1.16-9']"
reverse_depends = "['dracut-ykfde', 'kernel-initrd', 'kernel-lts-initrd', 'systemd', 'systemd-nspawn', 'systemd-systemctl', 'volume_key', 'zulucrypt']"
+++
cryptsetup-luks is intended as a complete replacement for the original cryptsetup.

{{< files text="show files" >}}* /usr/bin/cryptsetup
* /usr/bin/cryptsetup-ssh
* /usr/bin/integritysetup
* /usr/bin/veritysetup
* /usr/include/libcryptsetup.h
* /usr/lib/cryptsetup/libcryptsetup-token-ssh.so
* /usr/lib/libcryptsetup.so
* /usr/lib/libcryptsetup.so.12
* /usr/lib/libcryptsetup.so.12.10.0
* /usr/lib/pkgconfig/libcryptsetup.pc
* /usr/share/doc/cryptsetup-luks-2.7.0/AUTHORS
* /usr/share/doc/cryptsetup-luks-2.7.0/COPYING
* /usr/share/doc/cryptsetup-luks-2.7.0/COPYING.LGPL
* /usr/share/doc/cryptsetup-luks-2.7.0/FAQ.md
* /usr/share/doc/cryptsetup-luks-2.7.0/README.Frugalware
* /usr/share/doc/cryptsetup-luks-2.7.0/README.md
* /usr/share/locale/cs/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/da/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/de/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/es/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/fi/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/fr/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/id/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/it/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/ja/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/ka/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/nl/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/pl/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/ro/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/ru/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/sr/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/sv/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/uk/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/vi/LC_MESSAGES/cryptsetup.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/cryptsetup.mo
* /usr/share/man/man8/cryptsetup-benchmark.8.gz
* /usr/share/man/man8/cryptsetup-bitlkDump.8.gz
* /usr/share/man/man8/cryptsetup-bitlkOpen.8.gz
* /usr/share/man/man8/cryptsetup-close.8.gz
* /usr/share/man/man8/cryptsetup-config.8.gz
* /usr/share/man/man8/cryptsetup-convert.8.gz
* /usr/share/man/man8/cryptsetup-create.8.gz
* /usr/share/man/man8/cryptsetup-erase.8.gz
* /usr/share/man/man8/cryptsetup-fvault2Dump.8.gz
* /usr/share/man/man8/cryptsetup-fvault2Open.8.gz
* /usr/share/man/man8/cryptsetup-isLuks.8.gz
* /usr/share/man/man8/cryptsetup-loopaesOpen.8.gz
* /usr/share/man/man8/cryptsetup-luksAddKey.8.gz
* /usr/share/man/man8/cryptsetup-luksChangeKey.8.gz
* /usr/share/man/man8/cryptsetup-luksConvertKey.8.gz
* /usr/share/man/man8/cryptsetup-luksDump.8.gz
* /usr/share/man/man8/cryptsetup-luksErase.8.gz
* /usr/share/man/man8/cryptsetup-luksFormat.8.gz
* /usr/share/man/man8/cryptsetup-luksHeaderBackup.8.gz
* /usr/share/man/man8/cryptsetup-luksHeaderRestore.8.gz
* /usr/share/man/man8/cryptsetup-luksKillSlot.8.gz
* /usr/share/man/man8/cryptsetup-luksOpen.8.gz
* /usr/share/man/man8/cryptsetup-luksRemoveKey.8.gz
* /usr/share/man/man8/cryptsetup-luksResume.8.gz
* /usr/share/man/man8/cryptsetup-luksSuspend.8.gz
* /usr/share/man/man8/cryptsetup-luksUUID.8.gz
* /usr/share/man/man8/cryptsetup-open.8.gz
* /usr/share/man/man8/cryptsetup-plainOpen.8.gz
* /usr/share/man/man8/cryptsetup-reencrypt.8.gz
* /usr/share/man/man8/cryptsetup-refresh.8.gz
* /usr/share/man/man8/cryptsetup-repair.8.gz
* /usr/share/man/man8/cryptsetup-resize.8.gz
* /usr/share/man/man8/cryptsetup-ssh.8.gz
* /usr/share/man/man8/cryptsetup-status.8.gz
* /usr/share/man/man8/cryptsetup-tcryptDump.8.gz
* /usr/share/man/man8/cryptsetup-tcryptOpen.8.gz
* /usr/share/man/man8/cryptsetup-token.8.gz
* /usr/share/man/man8/cryptsetup.8.gz
* /usr/share/man/man8/integritysetup.8.gz
* /usr/share/man/man8/veritysetup.8.gz
{{< /files >}}