+++
draft = false
title = "kwallet-pam 5.27.10-6"
version = "5.27.10-6"
description = "KWallet PAM integration"
date = "2024-02-19T12:22:19"
aliases = "/packages/218359"
categories = ['plasma']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "15544"
usize = "32785"
sha1sum = "bb20010749383919ecbfd82c1ad36989f9a5c2f3"
depends = "['kwallet5>=5.115.0', 'libgcrypt>=1.7.3-2', 'pam>=1.1.8-4', 'socat>=1.7.3.1-2']"
+++
KWallet PAM integration"

{{< files text="show files" >}}* /etc/xdg/autostart/pam_kwallet_init.desktop
* /usr/lib/kf5/pam_kwallet_init
* /usr/lib/security/pam_kwallet5.so
* /usr/lib/systemd/user/plasma-kwallet-pam.service
* /usr/share/doc/kwallet-pam-5.27.10/README.txt
{{< /files >}}