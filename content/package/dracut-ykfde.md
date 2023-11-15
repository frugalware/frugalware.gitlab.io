+++
draft = false
title = "dracut-ykfde 0.7.9-1"
version = "0.7.9-1"
date = "2022-12-20T08:39:08"
categories = ['base-extra']
upstreamurl = "https://github.com/eworm-de/mkinitcpio-ykfde"
arch = "x86_64"
size = "30380"
usize = "154037"
sha1sum = "f9c30c585c8af98421a3d4a1877f6a7da9ab9f3c"
depends = "['iniparser>=4.0-2', 'keyutils', 'libyubikey', 'yubikey-personalization', 'cryptsetup-luks>=2.0.1', 'libarchive', 'libsystemd']"
files = "['etc/', 'etc/ykfde.conf', 'etc/ykfde.d/', 'etc/ykfde.d/.gitignore', 'lib/', 'lib/systemd/', 'lib/systemd/system/', 'lib/systemd/system/ykfde-2f.service', 'lib/systemd/system/ykfde-worker.service', 'lib/systemd/system/ykfde.service', 'usr/', 'usr/bin/', 'usr/bin/ykfde', 'usr/bin/ykfde-cpio', 'usr/lib/', 'usr/lib/dracut/', 'usr/lib/dracut/modules.d/', 'usr/lib/dracut/modules.d/90ykfde/', 'usr/lib/dracut/modules.d/90ykfde/20-ykfde.rules', 'usr/lib/dracut/modules.d/90ykfde/module-setup.sh', 'usr/lib/dracut/modules.d/90ykfde/parse-mod.sh', 'usr/lib/dracut/modules.d/90ykfde/ykfde.sh', 'usr/lib/systemd/', 'usr/lib/ykfde/', 'usr/lib/ykfde/worker', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/dracut-ykfde-0.7.9/', 'usr/share/doc/dracut-ykfde-0.7.9/COPYING.md', 'usr/share/doc/dracut-ykfde-0.7.9/README-dracut.html', 'usr/share/doc/dracut-ykfde-0.7.9/README-dracut.md', 'usr/share/doc/dracut-ykfde-0.7.9/README-mkinitcpio.html', 'usr/share/doc/dracut-ykfde-0.7.9/README-mkinitcpio.md', 'usr/share/doc/dracut-ykfde-0.7.9/README.html', 'usr/share/doc/dracut-ykfde-0.7.9/README.md', 'usr/share/doc/ykfde/', 'usr/share/doc/ykfde/README-dracut.html', 'usr/share/doc/ykfde/README-dracut.md', 'usr/share/doc/ykfde/README-mkinitcpio.html', 'usr/share/doc/ykfde/README-mkinitcpio.md', 'usr/share/doc/ykfde/README.html', 'usr/share/doc/ykfde/README.md']"
+++
Full disk encryption with Yubikey (Yubico key) for dracut