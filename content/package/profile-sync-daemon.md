+++
draft = false
title = "profile-sync-daemon 6.50-1"
version = "6.50-1"
date = "2023-11-19T13:57:47"
categories = ['apps-extra']
upstreamurl = "https://github.com/graysky2/profile-sync-daemon"
arch = "x86_64"
size = "20104"
usize = "50513"
sha1sum = "5dbbe29a724efda52dd8aa1c659bfea333499164"
depends = "['procps-ng', 'rsync', 'systemd', 'findutils']"
files = "['usr/', 'usr/bin/', 'usr/bin/profile-sync-daemon', 'usr/bin/psd', 'usr/bin/psd-overlay-helper', 'usr/bin/psd-suspend-sync', 'usr/lib/', 'usr/lib/systemd/', 'usr/lib/systemd/user/', 'usr/lib/systemd/user/psd-resync.service', 'usr/lib/systemd/user/psd-resync.timer', 'usr/lib/systemd/user/psd.service', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/profile-sync-daemon-6.50/', 'usr/share/doc/profile-sync-daemon-6.50/INSTALL', 'usr/share/doc/profile-sync-daemon-6.50/LICENSE', 'usr/share/doc/profile-sync-daemon-6.50/README.md', 'usr/share/man/', 'usr/share/man/man1/', 'usr/share/man/man1/profile-sync-daemon.1.gz', 'usr/share/man/man1/psd-overlay-helper.1.gz', 'usr/share/man/man1/psd.1.gz', 'usr/share/psd/', 'usr/share/psd/browsers/', 'usr/share/psd/browsers/chromium', 'usr/share/psd/browsers/chromium-dev', 'usr/share/psd/browsers/conkeror.mozdev.org', 'usr/share/psd/browsers/epiphany', 'usr/share/psd/browsers/falkon', 'usr/share/psd/browsers/firefox', 'usr/share/psd/browsers/firefox-trunk', 'usr/share/psd/browsers/google-chrome', 'usr/share/psd/browsers/google-chrome-beta', 'usr/share/psd/browsers/google-chrome-unstable', 'usr/share/psd/browsers/heftig-aurora', 'usr/share/psd/browsers/icecat', 'usr/share/psd/browsers/inox', 'usr/share/psd/browsers/luakit', 'usr/share/psd/browsers/midori', 'usr/share/psd/browsers/opera', 'usr/share/psd/browsers/opera-beta', 'usr/share/psd/browsers/opera-developer', 'usr/share/psd/browsers/opera-legacy', 'usr/share/psd/browsers/opera-next', 'usr/share/psd/browsers/otter-browser', 'usr/share/psd/browsers/palemoon', 'usr/share/psd/browsers/qupzilla', 'usr/share/psd/browsers/qutebrowser', 'usr/share/psd/browsers/rekonq', 'usr/share/psd/browsers/seamonkey', 'usr/share/psd/browsers/surf', 'usr/share/psd/browsers/vivaldi', 'usr/share/psd/browsers/vivaldi-snapshot', 'usr/share/psd/contrib/', 'usr/share/psd/contrib/brave', 'usr/share/psd/contrib/microsoft-edge', 'usr/share/psd/contrib/microsoft-edge-beta', 'usr/share/psd/contrib/vscode', 'usr/share/psd/psd.conf', 'usr/share/zsh/', 'usr/share/zsh/site-functions/', 'usr/share/zsh/site-functions/_psd']"
+++
Syncs browser profiles to tmpfs reducing SSD/HDD calls and speeding-up browsers.