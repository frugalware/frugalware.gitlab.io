+++
draft = false
title = "saslauthd 2.1.28-7"
version = "2.1.28-7"
description = "sasl authentication server"
date = "2024-02-02T16:49:57"
aliases = "/packages/14986"
categories = ['network']
upstreamurl = "https://cyrusimap.org/"
arch = "x86_64"
size = "31304"
usize = "77544"
sha1sum = "6a7e92dc519c4eb7e6646779078d94bac6c20f76"
depends = "['cyrus-sasl>=2.1.28', 'libkrb5>=1.17-2', 'libxcrypt', 'pam>=1.1.8-4']"
+++
sasl authentication server{{< files text="show files" >}}* /etc/sysconfig/saslauthd
* /usr/bin/saslauthd
* /usr/bin/testsaslauthd
* /usr/lib/systemd/system/saslauthd.service
* /usr/share/man/man8/saslauthd.8.gz
{{< /files >}}