+++
draft = false
title = "libsystemd 255.3-2"
version = "255.3-2"
description = "systemd libs"
date = "2024-02-01T13:22:45"
aliases = "/packages/217590"
categories = ['base']
upstreamurl = "http://www.freedesktop.org/wiki/Software/systemd"
arch = "x86_64"
size = "2657704"
usize = "9230819"
sha1sum = "69404ffdf4a8196570b761147607bedf643c4fc8"
depends = "['bzip2>=1.0.6-6', 'elfutils>=0.167-2', 'libcap>=2.24-4', 'libgcrypt>=1.7.3-2', 'libidn>=1.35', 'libxcrypt', 'lz4>=1.8.1.2-2', 'openssl>=3.0.7', 'p11-kit>=0.24.1', 'xfsprogs-acl>=2.2.52-5', 'xz>=5.2.2-4', 'zlib>=1.2.8-8', 'zstd']"
reverse_depends = "['avahi', 'bluez', 'clamav', 'clightd', 'connman', 'dbus', 'dmraid', 'dosfstools', 'dracut-ykfde', 'efl', 'enlightenment', 'gfs2-utils', 'gnupg2', 'gst1-plugins-good-pulseaudio', 'ibus', 'irqbalance', 'iscsi', 'jack2', 'libcups', 'liblogging', 'libndctl', 'libpulse', 'libratbag', 'libreswan', 'libvlc', 'libvncserver', 'lvm2', 'mariadb', 'modemmanager', 'mpd', 'multipath-tools', 'nvme-cli', 'p11-kit', 'pam', 'pcsc-lite', 'pdns-recursor', 'polkit', 'qt5-base', 'rdma-core', 'samba', 'samba-client', 'sane-backends', 'sddm', 'shadow', 'smartmontools', 'solid', 'speech-dispatcher', 'spice-vdagent', 'strongswan', 'systemd', 'systemd-nspawn', 'systemd-systemctl', 'terminology', 'tor', 'udisks2', 'upower', 'util-linux', 'xdm', 'xf86-video-qxl', 'xorg-server', 'xorg-server-fbdev', 'xorg-server-xephyr']"
+++
systemd libs"

{{< files text="show files" >}}* /etc/ld.so.conf.d/libsystemd.conf
* /usr/lib/libnss_myhostname.so.2
* /usr/lib/libnss_mymachines.so.2
* /usr/lib/libnss_systemd.so.2
* /usr/lib/libsystemd.so
* /usr/lib/libsystemd.so.0
* /usr/lib/libsystemd.so.0.38.0
* /usr/lib/pkgconfig/libsystemd.pc
* /usr/lib/security/pam_systemd.so
* /usr/lib/security/pam_systemd_home.so
* /usr/lib/security/pam_systemd_loadkey.so
* /usr/lib/systemd/libsystemd-core-255.so
* /usr/lib/systemd/libsystemd-shared-255.so
{{< /files >}}