+++
draft = false
title = "xdg-desktop-portal 1.20.3-2"
version = "1.20.3-2"
description = "Desktop integration portals for sandboxed apps"
date = "2025-06-24T06:55:52"
aliases = "/packages/220846"
categories = ['lib']
upstreamurl = "https://github.com/flatpak/xdg-desktop-portal"
arch = "x86_64"
size = "361640"
usize = "1822044"
sha1sum = "a36b27386c86628f60ef168c728a336978da4ccb"
depends = "['fuse3>=3.17.1', 'geoclue2', 'glib2', 'gst1-plugins-base', 'libportal', 'pipewire', 'rtkit', 'systemd']"
reverse_depends = "['plasma-wayland-session', 'xdg-desktop-portal-gtk']"
+++
### Description: 
Desktop integration portals for sandboxed apps

### Files: 
* /usr/lib/systemd/user/xdg-desktop-portal-rewrite-launchers.service
* /usr/lib/systemd/user/xdg-desktop-portal.service
* /usr/lib/systemd/user/xdg-document-portal.service
* /usr/lib/systemd/user/xdg-permission-store.service
* /usr/lib/xdg-desktop-portal/xdg-desktop-portal
* /usr/lib/xdg-desktop-portal/xdg-desktop-portal-rewrite-launchers
* /usr/lib/xdg-desktop-portal/xdg-desktop-portal-validate-icon
* /usr/lib/xdg-desktop-portal/xdg-desktop-portal-validate-sound
* /usr/lib/xdg-desktop-portal/xdg-document-portal
* /usr/lib/xdg-desktop-portal/xdg-permission-store
* /usr/share/dbus-1/interfaces/org.freedesktop.host.portal.Registry.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Access.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Account.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.AppChooser.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Background.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Clipboard.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.DynamicLauncher.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Email.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.FileChooser.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.GlobalShortcuts.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Inhibit.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.InputCapture.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Lockdown.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Notification.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.PermissionStore.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Print.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.RemoteDesktop.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Request.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.ScreenCast.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Screenshot.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Secret.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Session.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Settings.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Usb.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.impl.portal.Wallpaper.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Account.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Background.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Camera.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Clipboard.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Documents.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.DynamicLauncher.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Email.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.FileChooser.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.FileTransfer.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.GameMode.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.GlobalShortcuts.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Inhibit.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.InputCapture.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Location.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.MemoryMonitor.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.NetworkMonitor.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Notification.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.OpenURI.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.PowerProfileMonitor.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Print.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.ProxyResolver.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Realtime.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.RemoteDesktop.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Request.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.ScreenCast.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Screenshot.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Secret.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Session.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Settings.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Trash.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Usb.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Wallpaper.xml
* /usr/share/dbus-1/services/org.freedesktop.impl.portal.PermissionStore.service
* /usr/share/dbus-1/services/org.freedesktop.portal.Desktop.service
* /usr/share/dbus-1/services/org.freedesktop.portal.Documents.service
* /usr/share/doc/xdg-desktop-portal-1.20.3/COPYING
* /usr/share/doc/xdg-desktop-portal-1.20.3/README.md
* /usr/share/doc/xdg-desktop-portal-1.20.3/RELEASE_HOWTO.md
* /usr/share/locale/be/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/bg/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/ca/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/cs/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/da/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/de/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/en_GB/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/es/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/fr/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/gl/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/he/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/hi/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/hr/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/hu/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/id/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/ie/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/it/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/ja/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/ka/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/lt/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/nl/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/oc/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/pl/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/pt/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/ro/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/ru/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/sk/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/sl/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/sr/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/sv/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/tr/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/uk/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/xdg-desktop-portal.mo
* /usr/share/man/man5/portals.conf.5.gz
* /usr/share/pkgconfig/xdg-desktop-portal.pc
