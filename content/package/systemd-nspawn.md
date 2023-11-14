+++
draft = false
title = "systemd-nspawn 254.6-1"
version = "254.6-1"
date = "2023-11-12T12:05:46"
categories = ['base-extra']
upstreamurl = "http://www.freedesktop.org/wiki/Software/systemd"
arch = "x86_64"
size = "182272"
usize = "411864"
sha1sum = "69bef82015b56f948aa15c7681b7cc95c11f7f38"
depends = "['libseccomp', 'cryptsetup-luks', 'kmod', 'libidn2', 'libsystemd>=254.6']"
files = "['lib/', 'lib/systemd/', 'lib/systemd/system/', 'lib/systemd/system/systemd-nspawn@.service', 'usr/', 'usr/bin/', 'usr/bin/systemd-nspawn', 'usr/lib/', 'usr/lib/tmpfiles.d/', 'usr/lib/tmpfiles.d/systemd-nspawn.conf', 'usr/share/', 'usr/share/bash-completion/', 'usr/share/bash-completion/completions/', 'usr/share/bash-completion/completions/systemd-nspawn', 'usr/share/man/', 'usr/share/man/man1/', 'usr/share/man/man1/systemd-nspawn.1.gz', 'usr/share/man/man5/', 'usr/share/man/man5/systemd.nspawn.5.gz', 'usr/share/zsh/', 'usr/share/zsh/site-functions/', 'usr/share/zsh/site-functions/_systemd-nspawn']"
+++
Spawn a command or OS in a light-weight container.