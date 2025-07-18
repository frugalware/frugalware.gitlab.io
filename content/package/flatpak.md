+++
draft = false
title = "flatpak 1.16.1-5"
version = "1.16.1-5"
description = "Linux application sandboxing and distribution framework (formerly xdg-app)"
date = "2025-06-25T14:18:49"
aliases = "/packages/220841"
categories = ['apps-extra']
upstreamurl = "https://flatpak.org"
arch = "x86_64"
size = "1620420"
usize = "8403860"
sha1sum = "08bd28ca3d8ac1f7cc41edd25c497ad3c32ff140"
depends = "['appstream>=1.0.0', 'bubblewrap>=0.10.0', 'gdk-pixbuf2', 'json-glib', 'libseccomp', 'ostree', 'polkit', 'socat', 'xdg-dbus-proxy']"
reverse_depends = "['discover', 'flatpak-kcm']"
+++
### Description: 
Linux application sandboxing and distribution framework (formerly xdg-app)

### Files: 
* /etc/profile.d/flatpak.csh
* /etc/profile.d/flatpak.sh
* /usr/bin/flatpak
* /usr/bin/flatpak-bisect
* /usr/bin/flatpak-coredumpctl
* /usr/include/flatpak/flatpak-bundle-ref.h
* /usr/include/flatpak/flatpak-enum-types.h
* /usr/include/flatpak/flatpak-error.h
* /usr/include/flatpak/flatpak-installation.h
* /usr/include/flatpak/flatpak-installed-ref.h
* /usr/include/flatpak/flatpak-instance.h
* /usr/include/flatpak/flatpak-portal-error.h
* /usr/include/flatpak/flatpak-ref.h
* /usr/include/flatpak/flatpak-related-ref.h
* /usr/include/flatpak/flatpak-remote-ref.h
* /usr/include/flatpak/flatpak-remote.h
* /usr/include/flatpak/flatpak-transaction.h
* /usr/include/flatpak/flatpak-version-macros.h
* /usr/include/flatpak/flatpak.h
* /usr/lib/flatpak/flatpak-oci-authenticator
* /usr/lib/flatpak/flatpak-portal
* /usr/lib/flatpak/flatpak-session-helper
* /usr/lib/flatpak/flatpak-system-helper
* /usr/lib/flatpak/flatpak-validate-icon
* /usr/lib/flatpak/revokefs-fuse
* /usr/lib/girepository-1.0/Flatpak-1.0.typelib
* /usr/lib/libflatpak.so
* /usr/lib/libflatpak.so.0
* /usr/lib/libflatpak.so.0.11601.0
* /usr/lib/pkgconfig/flatpak.pc
* /usr/lib/systemd/system-environment-generators/60-flatpak-system-only
* /usr/lib/systemd/system/flatpak-system-helper.service
* /usr/lib/systemd/user-environment-generators/60-flatpak
* /usr/lib/systemd/user/flatpak-oci-authenticator.service
* /usr/lib/systemd/user/flatpak-portal.service
* /usr/lib/systemd/user/flatpak-session-helper.service
* /usr/lib/sysusers.d/flatpak.conf
* /usr/lib/tmpfiles.d/flatpak.conf
* /usr/share/bash-completion/completions/flatpak
* /usr/share/dbus-1/interfaces/org.freedesktop.Flatpak.Authenticator.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.Flatpak.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.portal.Flatpak.xml
* /usr/share/dbus-1/services/org.flatpak.Authenticator.Oci.service
* /usr/share/dbus-1/services/org.freedesktop.Flatpak.service
* /usr/share/dbus-1/services/org.freedesktop.portal.Flatpak.service
* /usr/share/dbus-1/system-services/org.freedesktop.Flatpak.SystemHelper.service
* /usr/share/dbus-1/system.d/org.freedesktop.Flatpak.SystemHelper.conf
* /usr/share/doc/flatpak-1.16.1/COPYING
* /usr/share/doc/flatpak-1.16.1/NEWS
* /usr/share/doc/flatpak-1.16.1/README.md
* /usr/share/doc/flatpak/docbook.css
* /usr/share/doc/flatpak/flatpak-docs.html
* /usr/share/fish/vendor_completions.d/flatpak.fish
* /usr/share/fish/vendor_conf.d/flatpak.fish
* /usr/share/flatpak/triggers/desktop-database.trigger
* /usr/share/flatpak/triggers/gtk-icon-cache.trigger
* /usr/share/flatpak/triggers/mime-database.trigger
* /usr/share/gir-1.0/Flatpak-1.0.gir
* /usr/share/gtk-doc/html/flatpak/annotation-glossary.html
* /usr/share/gtk-doc/html/flatpak/ch01.html
* /usr/share/gtk-doc/html/flatpak/ch02.html
* /usr/share/gtk-doc/html/flatpak/flatpak-Error-codes.html
* /usr/share/gtk-doc/html/flatpak/flatpak-Version-information.html
* /usr/share/gtk-doc/html/flatpak/flatpak.devhelp2
* /usr/share/gtk-doc/html/flatpak/FlatpakBundleRef.html
* /usr/share/gtk-doc/html/flatpak/FlatpakInstallation.html
* /usr/share/gtk-doc/html/flatpak/FlatpakInstalledRef.html
* /usr/share/gtk-doc/html/flatpak/FlatpakInstance.html
* /usr/share/gtk-doc/html/flatpak/FlatpakRef.html
* /usr/share/gtk-doc/html/flatpak/FlatpakRelatedRef.html
* /usr/share/gtk-doc/html/flatpak/FlatpakRemote.html
* /usr/share/gtk-doc/html/flatpak/FlatpakRemoteRef.html
* /usr/share/gtk-doc/html/flatpak/FlatpakTransaction.html
* /usr/share/gtk-doc/html/flatpak/FlatpakTransactionOperation.html
* /usr/share/gtk-doc/html/flatpak/FlatpakTransactionProgress.html
* /usr/share/gtk-doc/html/flatpak/full-api-index.html
* /usr/share/gtk-doc/html/flatpak/gdbus-org.freedesktop.Flatpak.Authenticator.html
* /usr/share/gtk-doc/html/flatpak/gdbus-org.freedesktop.Flatpak.AuthenticatorRequest.html
* /usr/share/gtk-doc/html/flatpak/gdbus-org.freedesktop.Flatpak.Development.html
* /usr/share/gtk-doc/html/flatpak/gdbus-org.freedesktop.Flatpak.SessionHelper.html
* /usr/share/gtk-doc/html/flatpak/gdbus-org.freedesktop.Flatpak.SystemHelper.html
* /usr/share/gtk-doc/html/flatpak/gdbus-org.freedesktop.impl.portal.PermissionStore.html
* /usr/share/gtk-doc/html/flatpak/gdbus-org.freedesktop.portal.Documents.html
* /usr/share/gtk-doc/html/flatpak/gdbus-org.freedesktop.portal.Flatpak.html
* /usr/share/gtk-doc/html/flatpak/gdbus-org.freedesktop.portal.Flatpak.UpdateMonitor.html
* /usr/share/gtk-doc/html/flatpak/home.png
* /usr/share/gtk-doc/html/flatpak/index.html
* /usr/share/gtk-doc/html/flatpak/left-insensitive.png
* /usr/share/gtk-doc/html/flatpak/left.png
* /usr/share/gtk-doc/html/flatpak/object-tree.html
* /usr/share/gtk-doc/html/flatpak/right-insensitive.png
* /usr/share/gtk-doc/html/flatpak/right.png
* /usr/share/gtk-doc/html/flatpak/style.css
* /usr/share/gtk-doc/html/flatpak/up-insensitive.png
* /usr/share/gtk-doc/html/flatpak/up.png
* /usr/share/locale/bg/LC_MESSAGES/flatpak.mo
* /usr/share/locale/cs/LC_MESSAGES/flatpak.mo
* /usr/share/locale/da/LC_MESSAGES/flatpak.mo
* /usr/share/locale/de/LC_MESSAGES/flatpak.mo
* /usr/share/locale/en_GB/LC_MESSAGES/flatpak.mo
* /usr/share/locale/es/LC_MESSAGES/flatpak.mo
* /usr/share/locale/fr/LC_MESSAGES/flatpak.mo
* /usr/share/locale/gl/LC_MESSAGES/flatpak.mo
* /usr/share/locale/hi/LC_MESSAGES/flatpak.mo
* /usr/share/locale/hr/LC_MESSAGES/flatpak.mo
* /usr/share/locale/hu/LC_MESSAGES/flatpak.mo
* /usr/share/locale/id/LC_MESSAGES/flatpak.mo
* /usr/share/locale/ka/LC_MESSAGES/flatpak.mo
* /usr/share/locale/nl/LC_MESSAGES/flatpak.mo
* /usr/share/locale/oc/LC_MESSAGES/flatpak.mo
* /usr/share/locale/pl/LC_MESSAGES/flatpak.mo
* /usr/share/locale/pt/LC_MESSAGES/flatpak.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/flatpak.mo
* /usr/share/locale/ro/LC_MESSAGES/flatpak.mo
* /usr/share/locale/ru/LC_MESSAGES/flatpak.mo
* /usr/share/locale/sk/LC_MESSAGES/flatpak.mo
* /usr/share/locale/sl/LC_MESSAGES/flatpak.mo
* /usr/share/locale/sv/LC_MESSAGES/flatpak.mo
* /usr/share/locale/tr/LC_MESSAGES/flatpak.mo
* /usr/share/locale/uk/LC_MESSAGES/flatpak.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/flatpak.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/flatpak.mo
* /usr/share/man/man1/flatpak-build-bundle.1.gz
* /usr/share/man/man1/flatpak-build-commit-from.1.gz
* /usr/share/man/man1/flatpak-build-export.1.gz
* /usr/share/man/man1/flatpak-build-finish.1.gz
* /usr/share/man/man1/flatpak-build-import-bundle.1.gz
* /usr/share/man/man1/flatpak-build-init.1.gz
* /usr/share/man/man1/flatpak-build-sign.1.gz
* /usr/share/man/man1/flatpak-build-update-repo.1.gz
* /usr/share/man/man1/flatpak-build.1.gz
* /usr/share/man/man1/flatpak-config.1.gz
* /usr/share/man/man1/flatpak-create-usb.1.gz
* /usr/share/man/man1/flatpak-document-export.1.gz
* /usr/share/man/man1/flatpak-document-info.1.gz
* /usr/share/man/man1/flatpak-document-unexport.1.gz
* /usr/share/man/man1/flatpak-documents.1.gz
* /usr/share/man/man1/flatpak-enter.1.gz
* /usr/share/man/man1/flatpak-history.1.gz
* /usr/share/man/man1/flatpak-info.1.gz
* /usr/share/man/man1/flatpak-install.1.gz
* /usr/share/man/man1/flatpak-kill.1.gz
* /usr/share/man/man1/flatpak-list.1.gz
* /usr/share/man/man1/flatpak-make-current.1.gz
* /usr/share/man/man1/flatpak-mask.1.gz
* /usr/share/man/man1/flatpak-override.1.gz
* /usr/share/man/man1/flatpak-permission-remove.1.gz
* /usr/share/man/man1/flatpak-permission-reset.1.gz
* /usr/share/man/man1/flatpak-permission-set.1.gz
* /usr/share/man/man1/flatpak-permission-show.1.gz
* /usr/share/man/man1/flatpak-permissions.1.gz
* /usr/share/man/man1/flatpak-pin.1.gz
* /usr/share/man/man1/flatpak-ps.1.gz
* /usr/share/man/man1/flatpak-remote-add.1.gz
* /usr/share/man/man1/flatpak-remote-delete.1.gz
* /usr/share/man/man1/flatpak-remote-info.1.gz
* /usr/share/man/man1/flatpak-remote-ls.1.gz
* /usr/share/man/man1/flatpak-remote-modify.1.gz
* /usr/share/man/man1/flatpak-remotes.1.gz
* /usr/share/man/man1/flatpak-repair.1.gz
* /usr/share/man/man1/flatpak-repo.1.gz
* /usr/share/man/man1/flatpak-run.1.gz
* /usr/share/man/man1/flatpak-search.1.gz
* /usr/share/man/man1/flatpak-spawn.1.gz
* /usr/share/man/man1/flatpak-uninstall.1.gz
* /usr/share/man/man1/flatpak-update.1.gz
* /usr/share/man/man1/flatpak.1.gz
* /usr/share/man/man5/flatpak-flatpakref.5.gz
* /usr/share/man/man5/flatpak-flatpakrepo.5.gz
* /usr/share/man/man5/flatpak-installation.5.gz
* /usr/share/man/man5/flatpak-metadata.5.gz
* /usr/share/man/man5/flatpak-remote.5.gz
* /usr/share/man/man5/flatpakref.5.gz
* /usr/share/man/man5/flatpakrepo.5.gz
* /usr/share/polkit-1/actions/org.freedesktop.Flatpak.policy
* /usr/share/polkit-1/rules.d/org.freedesktop.Flatpak.rules
* /usr/share/zsh/site-functions/_flatpak
