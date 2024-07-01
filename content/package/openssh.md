+++
draft = false
title = "openssh 9.8-1"
version = "9.8-1"
description = "Secure Shell daemon and clients"
date = "2024-07-01T10:19:37"
aliases = "/packages/2421"
categories = ['network']
upstreamurl = "http://www.openssh.com/"
arch = "x86_64"
size = "1232680"
usize = "5639188"
sha1sum = "5f94727c655b50d0df09ab0502f42da58e7f104a"
depends = "['glibc>=2.35', 'ldns', 'libedit', 'libfido2>=1.10', 'openssl>=3.1', 'pam', 'zlib>=1.2.12']"
reverse_depends = "['autossh', 'gnome-keyring', 'keychain', 'kssh', 'seahorse', 'ssh-contact', 'sshcode']"
+++
### Description: 
Secure Shell daemon and clients

### Files: 
* /etc/pam.d/sshd
* /etc/ssh/moduli
* /etc/ssh/sshd_config
* /etc/ssh/ssh_config
* /usr/bin/findssl.sh
* /usr/bin/scp
* /usr/bin/sftp
* /usr/bin/ssh
* /usr/bin/ssh-add
* /usr/bin/ssh-agent
* /usr/bin/ssh-copy-id
* /usr/bin/ssh-keygen
* /usr/bin/ssh-keyscan
* /usr/bin/sshd
* /usr/bin/sshd-keygen
* /usr/lib/openssh/sftp-server
* /usr/lib/openssh/ssh-askpass
* /usr/lib/openssh/ssh-keysign
* /usr/lib/openssh/ssh-pkcs11-helper
* /usr/lib/openssh/ssh-sk-helper
* /usr/lib/openssh/sshd-session
* /usr/lib/systemd/system/sshd-keygen.service
* /usr/lib/systemd/system/sshd.service
* /usr/lib/systemd/user/ssh-agent.service
* /usr/share/doc/openssh-9.8/ChangeLog
* /usr/share/doc/openssh-9.8/CREDITS
* /usr/share/doc/openssh-9.8/INSTALL
* /usr/share/doc/openssh-9.8/README
* /usr/share/doc/openssh-9.8/README.dns
* /usr/share/doc/openssh-9.8/README.Frugalware
* /usr/share/doc/openssh-9.8/README.md
* /usr/share/doc/openssh-9.8/README.platform
* /usr/share/doc/openssh-9.8/README.privsep
* /usr/share/doc/openssh-9.8/README.tun
* /usr/share/doc/openssh-9.8/TODO
* /usr/share/man/man1/scp.1.gz
* /usr/share/man/man1/sftp.1.gz
* /usr/share/man/man1/ssh-add.1.gz
* /usr/share/man/man1/ssh-agent.1.gz
* /usr/share/man/man1/ssh-copy-id.1.gz
* /usr/share/man/man1/ssh-keygen.1.gz
* /usr/share/man/man1/ssh-keyscan.1.gz
* /usr/share/man/man1/ssh.1.gz
* /usr/share/man/man5/moduli.5.gz
* /usr/share/man/man5/sshd_config.5.gz
* /usr/share/man/man5/ssh_config.5.gz
* /usr/share/man/man8/sftp-server.8.gz
* /usr/share/man/man8/ssh-keysign.8.gz
* /usr/share/man/man8/ssh-pkcs11-helper.8.gz
* /usr/share/man/man8/ssh-sk-helper.8.gz
* /usr/share/man/man8/sshd.8.gz
* /var/empty/.openssh
