+++
draft = false
title = "avahi 0.8-8"
version = "0.8-8"
description = "A multicast/unicast DNS-SD framework"
date = "2024-01-30T10:38:10"
aliases = "/packages/10021"
categories = ['network']
upstreamurl = "http://www.avahi.org"
arch = "x86_64"
size = "317732"
usize = "1446536"
sha1sum = "3239aab563018849ab8f153e884ef35d2bb74ebf"
depends = "['dbus>=1.10.10-3', 'expat>=2.1.0-6', 'gdbm>=1.15', 'libdaemon>=0.14-4', 'libevent', 'libssp>=9.1.0-3', 'libsystemd>=231-6', 'shadow>=4.2.1-5']"
reverse_depends = "['anyremote', 'cups', 'efl', 'geoclue2', 'kdnssd', 'libcups', 'libiio', 'libvirt', 'mpd', 'mumble', 'murmur', 'pipewire-pulse', 'pulseaudio-avahi', 'remmina', 'telepathy-salut', 'vlc-avahi']"
+++
A multicast/unicast DNS-SD framework{{< files text="show files" >}}* /etc/avahi/avahi-autoipd.action
* /etc/avahi/avahi-daemon.conf
* /etc/avahi/hosts
* /etc/avahi/services/sftp-ssh.service
* /etc/avahi/services/ssh.service
* /etc/dbus-1/system.d/avahi-dbus.conf
* /etc/systemd/system/avahi-daemon.service.d/ad.conf
* /usr/bin/avahi-autoipd
* /usr/bin/avahi-browse
* /usr/bin/avahi-browse-domains
* /usr/bin/avahi-daemon
* /usr/bin/avahi-publish
* /usr/bin/avahi-publish-address
* /usr/bin/avahi-publish-service
* /usr/bin/avahi-resolve
* /usr/bin/avahi-resolve-address
* /usr/bin/avahi-resolve-host-name
* /usr/bin/avahi-set-host-name
* /usr/include/avahi-client/client.h
* /usr/include/avahi-client/lookup.h
* /usr/include/avahi-client/publish.h
* /usr/include/avahi-common/address.h
* /usr/include/avahi-common/alternative.h
* /usr/include/avahi-common/cdecl.h
* /usr/include/avahi-common/defs.h
* /usr/include/avahi-common/domain.h
* /usr/include/avahi-common/error.h
* /usr/include/avahi-common/gccmacro.h
* /usr/include/avahi-common/llist.h
* /usr/include/avahi-common/malloc.h
* /usr/include/avahi-common/rlist.h
* /usr/include/avahi-common/simple-watch.h
* /usr/include/avahi-common/strlst.h
* /usr/include/avahi-common/thread-watch.h
* /usr/include/avahi-common/timeval.h
* /usr/include/avahi-common/watch.h
* /usr/include/avahi-core/core.h
* /usr/include/avahi-core/log.h
* /usr/include/avahi-core/lookup.h
* /usr/include/avahi-core/publish.h
* /usr/include/avahi-core/rr.h
* /usr/include/avahi-libevent/libevent-watch.h
* /usr/lib/libavahi-client.so
* /usr/lib/libavahi-client.so.3
* /usr/lib/libavahi-client.so.3.2.9
* /usr/lib/libavahi-common.so
* /usr/lib/libavahi-common.so.3
* /usr/lib/libavahi-common.so.3.5.4
* /usr/lib/libavahi-core.so
* /usr/lib/libavahi-core.so.7
* /usr/lib/libavahi-core.so.7.1.0
* /usr/lib/libavahi-libevent.so
* /usr/lib/libavahi-libevent.so.1
* /usr/lib/libavahi-libevent.so.1.0.0
* /usr/lib/pkgconfig/avahi-client.pc
* /usr/lib/pkgconfig/avahi-core.pc
* /usr/lib/pkgconfig/avahi-libevent.pc
* /usr/lib/systemd/system/avahi-daemon.service
* /usr/lib/systemd/system/avahi-daemon.socket
* /usr/share/avahi/avahi-service.dtd
* /usr/share/dbus-1/interfaces/org.freedesktop.Avahi.AddressResolver.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.Avahi.DomainBrowser.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.Avahi.EntryGroup.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.Avahi.HostNameResolver.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.Avahi.RecordBrowser.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.Avahi.Server.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.Avahi.ServiceBrowser.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.Avahi.ServiceResolver.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.Avahi.ServiceTypeBrowser.xml
* /usr/share/dbus-1/system-services/org.freedesktop.Avahi.service
* /usr/share/doc/avahi-0.8/ChangeLog
* /usr/share/doc/avahi-0.8/LICENSE
* /usr/share/doc/avahi-0.8/README
* /usr/share/doc/avahi-0.8/README.Frugalware
* /usr/share/locale/ach/LC_MESSAGES/avahi.mo
* /usr/share/locale/ar/LC_MESSAGES/avahi.mo
* /usr/share/locale/bg/LC_MESSAGES/avahi.mo
* /usr/share/locale/ca/LC_MESSAGES/avahi.mo
* /usr/share/locale/cs/LC_MESSAGES/avahi.mo
* /usr/share/locale/da/LC_MESSAGES/avahi.mo
* /usr/share/locale/de/LC_MESSAGES/avahi.mo
* /usr/share/locale/el/LC_MESSAGES/avahi.mo
* /usr/share/locale/en_AU/LC_MESSAGES/avahi.mo
* /usr/share/locale/en_CA/LC_MESSAGES/avahi.mo
* /usr/share/locale/en_GB/LC_MESSAGES/avahi.mo
* /usr/share/locale/en_NZ/LC_MESSAGES/avahi.mo
* /usr/share/locale/eo/LC_MESSAGES/avahi.mo
* /usr/share/locale/es/LC_MESSAGES/avahi.mo
* /usr/share/locale/et/LC_MESSAGES/avahi.mo
* /usr/share/locale/fa/LC_MESSAGES/avahi.mo
* /usr/share/locale/fi/LC_MESSAGES/avahi.mo
* /usr/share/locale/fo/LC_MESSAGES/avahi.mo
* /usr/share/locale/fr/LC_MESSAGES/avahi.mo
* /usr/share/locale/gl/LC_MESSAGES/avahi.mo
* /usr/share/locale/he/LC_MESSAGES/avahi.mo
* /usr/share/locale/hu/LC_MESSAGES/avahi.mo
* /usr/share/locale/id/LC_MESSAGES/avahi.mo
* /usr/share/locale/it/LC_MESSAGES/avahi.mo
* /usr/share/locale/ja/LC_MESSAGES/avahi.mo
* /usr/share/locale/ko/LC_MESSAGES/avahi.mo
* /usr/share/locale/lv/LC_MESSAGES/avahi.mo
* /usr/share/locale/ms/LC_MESSAGES/avahi.mo
* /usr/share/locale/nl/LC_MESSAGES/avahi.mo
* /usr/share/locale/oc/LC_MESSAGES/avahi.mo
* /usr/share/locale/pl/LC_MESSAGES/avahi.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/avahi.mo
* /usr/share/locale/ro/LC_MESSAGES/avahi.mo
* /usr/share/locale/ru/LC_MESSAGES/avahi.mo
* /usr/share/locale/sk/LC_MESSAGES/avahi.mo
* /usr/share/locale/sl/LC_MESSAGES/avahi.mo
* /usr/share/locale/sr/LC_MESSAGES/avahi.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/avahi.mo
* /usr/share/locale/sv/LC_MESSAGES/avahi.mo
* /usr/share/locale/tr/LC_MESSAGES/avahi.mo
* /usr/share/locale/uk/LC_MESSAGES/avahi.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/avahi.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/avahi.mo
* /usr/share/man/man1/avahi-browse-domains.1.gz
* /usr/share/man/man1/avahi-browse.1.gz
* /usr/share/man/man1/avahi-publish-address.1.gz
* /usr/share/man/man1/avahi-publish-service.1.gz
* /usr/share/man/man1/avahi-publish.1.gz
* /usr/share/man/man1/avahi-resolve-address.1.gz
* /usr/share/man/man1/avahi-resolve-host-name.1.gz
* /usr/share/man/man1/avahi-resolve.1.gz
* /usr/share/man/man1/avahi-set-host-name.1.gz
* /usr/share/man/man5/avahi-daemon.conf.5.gz
* /usr/share/man/man5/avahi.hosts.5.gz
* /usr/share/man/man5/avahi.service.5.gz
* /usr/share/man/man8/avahi-autoipd.8.gz
* /usr/share/man/man8/avahi-autoipd.action.8.gz
* /usr/share/man/man8/avahi-daemon.8.gz
{{< /files >}}