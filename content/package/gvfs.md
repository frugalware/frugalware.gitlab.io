+++
draft = false
title = "gvfs 1.52.0-1"
version = "1.52.0-1"
description = "gvfs is a userspace virtual filesystem designed to work with the i/o abstractions of gio."
date = "2023-09-29T09:04:32"
aliases = "/packages/49980"
categories = ['xapps-extra']
upstreamurl = "http://www.gnome.org/"
arch = "x86_64"
size = "914540"
usize = "5503779"
sha1sum = "97e38a315a732319729d8593c344c789ce56d27a"
depends = "['avahi-glib>=0.6.31-9', 'dbus>=1.10.10-4', 'gcr-1>=3.28.0', 'glib2>=2.56.0', 'gsettings-desktop-schemas', 'gtk+3>=3.22.29', 'libarchive>=3.2.1', 'libbluray', 'libcdio>=2.1.0', 'libcdio-paranoia>=10.2+0.93+1-3', 'libsecret>=0.18.5-5', 'libsoup3', 'udisks2>=2.7.6']"
reverse_depends = "['gvfs-apple', 'gvfs-fuse', 'gvfs-gphoto2', 'gvfs-mtp', 'gvfs-smb']"
+++
gvfs is a userspace virtual filesystem designed to work with the i/o abstractions of gio.{{< spoiler text="show files" >}}* /etc/ld.so.conf.d/gvfs.conf
* /usr/include/gvfs-client/gvfs/gvfsurimapper.h
* /usr/include/gvfs-client/gvfs/gvfsuriutils.h
* /usr/lib/gio/modules/libgioremote-volume-monitor.so
* /usr/lib/gio/modules/libgvfsdbus.so
* /usr/lib/gvfs/gvfs-udisks2-volume-monitor
* /usr/lib/gvfs/gvfsd
* /usr/lib/gvfs/gvfsd-admin
* /usr/lib/gvfs/gvfsd-afp
* /usr/lib/gvfs/gvfsd-afp-browse
* /usr/lib/gvfs/gvfsd-archive
* /usr/lib/gvfs/gvfsd-burn
* /usr/lib/gvfs/gvfsd-cdda
* /usr/lib/gvfs/gvfsd-computer
* /usr/lib/gvfs/gvfsd-dav
* /usr/lib/gvfs/gvfsd-dnssd
* /usr/lib/gvfs/gvfsd-ftp
* /usr/lib/gvfs/gvfsd-http
* /usr/lib/gvfs/gvfsd-localtest
* /usr/lib/gvfs/gvfsd-metadata
* /usr/lib/gvfs/gvfsd-network
* /usr/lib/gvfs/gvfsd-recent
* /usr/lib/gvfs/gvfsd-sftp
* /usr/lib/gvfs/gvfsd-trash
* /usr/lib/gvfs/libgvfscommon.so
* /usr/lib/gvfs/libgvfsdaemon.so
* /usr/lib/systemd/user/gvfs-afc-volume-monitor.service
* /usr/lib/systemd/user/gvfs-daemon.service
* /usr/lib/systemd/user/gvfs-gphoto2-volume-monitor.service
* /usr/lib/systemd/user/gvfs-metadata.service
* /usr/lib/systemd/user/gvfs-udisks2-volume-monitor.service
* /usr/lib/tmpfiles.d/gvfsd-fuse-tmpfiles.conf
* /usr/share/dbus-1/services/org.gtk.vfs.Daemon.service
* /usr/share/dbus-1/services/org.gtk.vfs.Metadata.service
* /usr/share/dbus-1/services/org.gtk.vfs.UDisks2VolumeMonitor.service
* /usr/share/doc/gvfs-1.52.0/COPYING
* /usr/share/doc/gvfs-1.52.0/NEWS
* /usr/share/doc/gvfs-1.52.0/README.md
* /usr/share/GConf/gsettings/gvfs-dns-sd.convert
* /usr/share/GConf/gsettings/gvfs-smb.convert
* /usr/share/glib-2.0/schemas/org.gnome.system.dns_sd.gschema.xml
* /usr/share/glib-2.0/schemas/org.gnome.system.gvfs.enums.xml
* /usr/share/glib-2.0/schemas/org.gnome.system.smb.gschema.xml
* /usr/share/gvfs/mounts/admin.mount
* /usr/share/gvfs/mounts/afp-browse.mount
* /usr/share/gvfs/mounts/afp.mount
* /usr/share/gvfs/mounts/archive.mount
* /usr/share/gvfs/mounts/burn.mount
* /usr/share/gvfs/mounts/cdda.mount
* /usr/share/gvfs/mounts/computer.mount
* /usr/share/gvfs/mounts/dav+sd.mount
* /usr/share/gvfs/mounts/dav.mount
* /usr/share/gvfs/mounts/dns-sd.mount
* /usr/share/gvfs/mounts/ftp.mount
* /usr/share/gvfs/mounts/ftpis.mount
* /usr/share/gvfs/mounts/ftps.mount
* /usr/share/gvfs/mounts/http.mount
* /usr/share/gvfs/mounts/localtest.mount
* /usr/share/gvfs/mounts/network.mount
* /usr/share/gvfs/mounts/recent.mount
* /usr/share/gvfs/mounts/sftp.mount
* /usr/share/gvfs/mounts/trash.mount
* /usr/share/gvfs/remote-volume-monitors/udisks2.monitor
* /usr/share/locale/ab/LC_MESSAGES/gvfs.mo
* /usr/share/locale/af/LC_MESSAGES/gvfs.mo
* /usr/share/locale/ar/LC_MESSAGES/gvfs.mo
* /usr/share/locale/as/LC_MESSAGES/gvfs.mo
* /usr/share/locale/ast/LC_MESSAGES/gvfs.mo
* /usr/share/locale/be/LC_MESSAGES/gvfs.mo
* /usr/share/locale/be@latin/LC_MESSAGES/gvfs.mo
* /usr/share/locale/bg/LC_MESSAGES/gvfs.mo
* /usr/share/locale/bn/LC_MESSAGES/gvfs.mo
* /usr/share/locale/bn_IN/LC_MESSAGES/gvfs.mo
* /usr/share/locale/bs/LC_MESSAGES/gvfs.mo
* /usr/share/locale/ca/LC_MESSAGES/gvfs.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/gvfs.mo
* /usr/share/locale/cs/LC_MESSAGES/gvfs.mo
* /usr/share/locale/da/LC_MESSAGES/gvfs.mo
* /usr/share/locale/de/LC_MESSAGES/gvfs.mo
* /usr/share/locale/el/LC_MESSAGES/gvfs.mo
* /usr/share/locale/en@shaw/LC_MESSAGES/gvfs.mo
* /usr/share/locale/en_GB/LC_MESSAGES/gvfs.mo
* /usr/share/locale/eo/LC_MESSAGES/gvfs.mo
* /usr/share/locale/es/LC_MESSAGES/gvfs.mo
* /usr/share/locale/et/LC_MESSAGES/gvfs.mo
* /usr/share/locale/eu/LC_MESSAGES/gvfs.mo
* /usr/share/locale/fa/LC_MESSAGES/gvfs.mo
* /usr/share/locale/fi/LC_MESSAGES/gvfs.mo
* /usr/share/locale/fr/LC_MESSAGES/gvfs.mo
* /usr/share/locale/fur/LC_MESSAGES/gvfs.mo
* /usr/share/locale/ga/LC_MESSAGES/gvfs.mo
* /usr/share/locale/gl/LC_MESSAGES/gvfs.mo
* /usr/share/locale/gu/LC_MESSAGES/gvfs.mo
* /usr/share/locale/he/LC_MESSAGES/gvfs.mo
* /usr/share/locale/hi/LC_MESSAGES/gvfs.mo
* /usr/share/locale/hr/LC_MESSAGES/gvfs.mo
* /usr/share/locale/hu/LC_MESSAGES/gvfs.mo
* /usr/share/locale/id/LC_MESSAGES/gvfs.mo
* /usr/share/locale/ie/LC_MESSAGES/gvfs.mo
* /usr/share/locale/it/LC_MESSAGES/gvfs.mo
* /usr/share/locale/ja/LC_MESSAGES/gvfs.mo
* /usr/share/locale/ka/LC_MESSAGES/gvfs.mo
* /usr/share/locale/kk/LC_MESSAGES/gvfs.mo
* /usr/share/locale/kn/LC_MESSAGES/gvfs.mo
* /usr/share/locale/ko/LC_MESSAGES/gvfs.mo
* /usr/share/locale/ku/LC_MESSAGES/gvfs.mo
* /usr/share/locale/lt/LC_MESSAGES/gvfs.mo
* /usr/share/locale/lv/LC_MESSAGES/gvfs.mo
* /usr/share/locale/mai/LC_MESSAGES/gvfs.mo
* /usr/share/locale/mk/LC_MESSAGES/gvfs.mo
* /usr/share/locale/ml/LC_MESSAGES/gvfs.mo
* /usr/share/locale/mr/LC_MESSAGES/gvfs.mo
* /usr/share/locale/ms/LC_MESSAGES/gvfs.mo
* /usr/share/locale/nb/LC_MESSAGES/gvfs.mo
* /usr/share/locale/nds/LC_MESSAGES/gvfs.mo
* /usr/share/locale/ne/LC_MESSAGES/gvfs.mo
* /usr/share/locale/nl/LC_MESSAGES/gvfs.mo
* /usr/share/locale/nn/LC_MESSAGES/gvfs.mo
* /usr/share/locale/oc/LC_MESSAGES/gvfs.mo
* /usr/share/locale/or/LC_MESSAGES/gvfs.mo
* /usr/share/locale/pa/LC_MESSAGES/gvfs.mo
* /usr/share/locale/pl/LC_MESSAGES/gvfs.mo
* /usr/share/locale/pt/LC_MESSAGES/gvfs.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/gvfs.mo
* /usr/share/locale/ro/LC_MESSAGES/gvfs.mo
* /usr/share/locale/ru/LC_MESSAGES/gvfs.mo
* /usr/share/locale/sk/LC_MESSAGES/gvfs.mo
* /usr/share/locale/sl/LC_MESSAGES/gvfs.mo
* /usr/share/locale/sq/LC_MESSAGES/gvfs.mo
* /usr/share/locale/sr/LC_MESSAGES/gvfs.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/gvfs.mo
* /usr/share/locale/sv/LC_MESSAGES/gvfs.mo
* /usr/share/locale/ta/LC_MESSAGES/gvfs.mo
* /usr/share/locale/te/LC_MESSAGES/gvfs.mo
* /usr/share/locale/tg/LC_MESSAGES/gvfs.mo
* /usr/share/locale/th/LC_MESSAGES/gvfs.mo
* /usr/share/locale/tr/LC_MESSAGES/gvfs.mo
* /usr/share/locale/ug/LC_MESSAGES/gvfs.mo
* /usr/share/locale/uk/LC_MESSAGES/gvfs.mo
* /usr/share/locale/vi/LC_MESSAGES/gvfs.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/gvfs.mo
* /usr/share/locale/zh_HK/LC_MESSAGES/gvfs.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/gvfs.mo
* /usr/share/polkit-1/actions/org.gtk.vfs.file-operations.policy
* /usr/share/polkit-1/rules.d/org.gtk.vfs.file-operations.rules
{{< /spoiler >}}