+++
draft = false
title = "pacman-tools 1.3.5-7"
version = "1.3.5-7"
description = "Tools for developers for managing packages"
date = "2024-01-30T10:03:01"
aliases = "/packages/2424"
categories = ['devel']
upstreamurl = "https://ftp.frugalware.org/pub/other/pacman-tools"
arch = "x86_64"
size = "223084"
usize = "571300"
sha1sum = "9474ec61e19f57b9bbada0bbb9d8e43d296ea599"
depends = "['bash', 'glib2>=2.16.4-2', 'libxml2>=2.6.32-2', 'openssl>=1.0.0', 'pacman-g2>=3.9.0-31', 'perl>=5.34', 'python3', 'shadow', 'wget']"
+++
Tools for developers for managing packages

{{< files text="show files" >}}* /etc/repoman.conf
* /etc/repoman.d/current
* /etc/repoman.d/stable
* /etc/sudoers.d/pacman-tools
* /etc/syncpkgcd/cconfig.py
* /etc/syncpkgd/ctlconfig.py
* /etc/syncpkgd/dconfig.py
* /usr/bin/bumppkg
* /usr/bin/chkdep
* /usr/bin/chkworld
* /usr/bin/chkworld.py
* /usr/bin/darcs-git
* /usr/bin/dg
* /usr/bin/etcconfig
* /usr/bin/fblint
* /usr/bin/fpmdiff
* /usr/bin/fwcpan
* /usr/bin/fwmirror
* /usr/bin/mkpkghtml
* /usr/bin/repoman
* /usr/bin/revdep-rebuild
* /usr/bin/syncpkg-shell
* /usr/bin/syncpkgcd
* /usr/bin/syncpkgd
* /usr/bin/syncpkgdctl
* /usr/bin/wipcheck
* /usr/lib/frugalware/fwmakepkg
* /usr/lib/systemd/system/syncpkgcd.service
* /usr/lib/systemd/system/syncpkgd.service
* /usr/share/doc/pacman-tools-1.3.5/AUTHORS
* /usr/share/doc/pacman-tools-1.3.5/Changelog
* /usr/share/doc/pacman-tools-1.3.5/hooks/README
* /usr/share/doc/pacman-tools-1.3.5/hooks/repoman-upgrade
* /usr/share/doc/pacman-tools-1.3.5/LICENSE
* /usr/share/doc/pacman-tools-1.3.5/NEWS
* /usr/share/doc/pacman-tools-1.3.5/README
* /usr/share/man/man1/bumppkg.1.gz
* /usr/share/man/man1/chkdep.1.gz
* /usr/share/man/man1/chkworld.1.gz
* /usr/share/man/man1/darcs-git.1.gz
* /usr/share/man/man1/etcconfig.1.gz
* /usr/share/man/man1/fblint.1.gz
* /usr/share/man/man1/fpmdiff.1.gz
* /usr/share/man/man1/fwcpan.1.gz
* /usr/share/man/man1/fwmirror.1.gz
* /usr/share/man/man1/mkisorelease.1.gz
* /usr/share/man/man1/mkpkghtml.1.gz
* /usr/share/man/man1/pear-makefb.1.gz
* /usr/share/man/man1/pootle-update.1.gz
* /usr/share/man/man1/repoman.1.gz
* /usr/share/man/man1/revdep-rebuild.1.gz
* /usr/share/man/man1/syncpkg-shell.1.gz
* /usr/share/man/man1/syncpkgcd.1.gz
* /usr/share/man/man1/syncpkgd.1.gz
* /usr/share/man/man1/syncpkgdctl.1.gz
* /usr/share/man/man1/wipcheck.1.gz
* /usr/share/man/man3/aspell.sh.3.gz
* /usr/share/man/man3/atutotools.sh.3.gz
* /usr/share/man/man3/berlios.sh.3.gz
* /usr/share/man/man3/cgit-freedesktop.sh.3.gz
* /usr/share/man/man3/cgit.sh.3.gz
* /usr/share/man/man3/clutter.sh.3.gz
* /usr/share/man/man3/cmake.sh.3.gz
* /usr/share/man/man3/cross32.sh.3.gz
* /usr/share/man/man3/firefox-extension.sh.3.gz
* /usr/share/man/man3/fonts.sh.3.gz
* /usr/share/man/man3/fwmakepkg.3.gz
* /usr/share/man/man3/gem.sh.3.gz
* /usr/share/man/man3/genscriptlet.sh.3.gz
* /usr/share/man/man3/github.sh.3.gz
* /usr/share/man/man3/gnome-look..sh.3.gz
* /usr/share/man/man3/gnome-scriptlet.sh.3.gz
* /usr/share/man/man3/gnome-shell-extension.sh.3.gz
* /usr/share/man/man3/gnome.sh.3.gz
* /usr/share/man/man3/googlecode.sh.3.gz
* /usr/share/man/man3/gtk-apps.sh.3.gz
* /usr/share/man/man3/haskell.sh.3.gz
* /usr/share/man/man3/i18n.sh.3.gz
* /usr/share/man/man3/kde.sh.3.gz
* /usr/share/man/man3/kernel-module.sh.3.gz
* /usr/share/man/man3/kernel-version.sh.3.gz
* /usr/share/man/man3/kernel.sh.3.gz
* /usr/share/man/man3/kf5-version.sh.3.gz
* /usr/share/man/man3/launchpad.sh.3.gz
* /usr/share/man/man3/meson.sh.3.gz
* /usr/share/man/man3/mono.sh.3.gz
* /usr/share/man/man3/mozilla-i18n-regen.sh.3.gz
* /usr/share/man/man3/mozilla-i18n.sh.3.gz
* /usr/share/man/man3/netsurf.sh.3.gz
* /usr/share/man/man3/octave.sh.3.gz
* /usr/share/man/man3/openjava.sh.3.gz
* /usr/share/man/man3/pear.sh.3.gz
* /usr/share/man/man3/pecl.sh.3.gz
* /usr/share/man/man3/perl.sh.3.gz
* /usr/share/man/man3/provider.sh.3.gz
* /usr/share/man/man3/pypi.sh.3.gz
* /usr/share/man/man3/python.sh.3.gz
* /usr/share/man/man3/qt5.sh.3.gz
* /usr/share/man/man3/qt6.sh.3.gz
* /usr/share/man/man3/sawfish-script.sh.3.gz
* /usr/share/man/man3/scm.sh.3.gz
* /usr/share/man/man3/sourceforge.sh.3.gz
* /usr/share/man/man3/systemd.sh.3.gz
* /usr/share/man/man3/texinfo.sh.3.gz
* /usr/share/man/man3/util.sh.3.gz
* /usr/share/man/man3/vim-spell.sh.3.gz
* /usr/share/man/man3/wine.sh.3.gz
* /usr/share/man/man3/xorg.sh.3.gz
* /usr/share/man/man3/xpi.3.gz
* /var/lib/syncpkgd.status
* /var/log/syncpkgcd.log
* /var/log/syncpkgd/daemon.log
{{< /files >}}