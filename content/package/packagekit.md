+++
draft = false
title = "packagekit 1.2.8-2"
version = "1.2.8-2"
description = "A system designed to make installation and updates of packages easier"
date = "2024-01-30T10:38:03"
aliases = "/packages/217762"
categories = ['apps-extra']
upstreamurl = "http://www.packagekit.org/"
arch = "x86_64"
size = "606196"
usize = "4383645"
sha1sum = "56af4f930a46d0386744bda9865acccfac3c8df3"
depends = "['bash-completion', 'gst1-plugins-base', 'networkmanager>=1.4.0-2', 'packagekit-glib', 'pango', 'polkit>=0.113-9', 'python3>=3.11']"
+++
A system designed to make installation and updates of packages easier

{{< files text="show files" >}}* /etc/cron.daily/packagekit-background.cron
* /etc/PackageKit/CommandNotFound.conf
* /etc/PackageKit/PackageKit.conf
* /etc/PackageKit/Vendor.conf
* /etc/profile.d/PackageKit.sh
* /etc/sysconfig/packagekit-background
* /usr/bin/pkcon
* /usr/bin/pkmon
* /usr/lib/girepository-1.0/PackageKitGlib-1.0.typelib
* /usr/lib/gnome-settings-daemon-3.0/gtk-modules/pk-gtk-module.desktop
* /usr/lib/gtk-3.0/modules/libpk-gtk-module.so
* /usr/lib/packagekit-backend/libpk_backend_dummy.so
* /usr/lib/packagekit-backend/libpk_backend_test_fail.so
* /usr/lib/packagekit-backend/libpk_backend_test_nop.so
* /usr/lib/packagekit-backend/libpk_backend_test_spawn.so
* /usr/lib/packagekit-backend/libpk_backend_test_succeed.so
* /usr/lib/packagekit-backend/libpk_backend_test_thread.so
* /usr/lib/packagekit/packagekit-direct
* /usr/lib/packagekit/packagekitd
* /usr/lib/packagekit/pk-command-not-found
* /usr/lib/packagekit/pk-gstreamer-install
* /usr/lib/packagekit/pk-offline-update
* /usr/lib/python3.12/site-packages/packagekit/backend.py
* /usr/lib/python3.12/site-packages/packagekit/enums.py
* /usr/lib/python3.12/site-packages/packagekit/filter.py
* /usr/lib/python3.12/site-packages/packagekit/misc.py
* /usr/lib/python3.12/site-packages/packagekit/package.py
* /usr/lib/python3.12/site-packages/packagekit/progress.py
* /usr/lib/python3.12/site-packages/packagekit/__init__.py
* /usr/lib/python3.12/site-packages/packagekit/__pycache__/backend.cpython-312.pyc
* /usr/lib/python3.12/site-packages/packagekit/__pycache__/enums.cpython-312.pyc
* /usr/lib/python3.12/site-packages/packagekit/__pycache__/filter.cpython-312.pyc
* /usr/lib/python3.12/site-packages/packagekit/__pycache__/misc.cpython-312.pyc
* /usr/lib/python3.12/site-packages/packagekit/__pycache__/package.cpython-312.pyc
* /usr/lib/python3.12/site-packages/packagekit/__pycache__/progress.cpython-312.pyc
* /usr/lib/python3.12/site-packages/packagekit/__pycache__/__init__.cpython-312.pyc
* /usr/lib/systemd/system/packagekit-offline-update.service
* /usr/lib/systemd/system/packagekit.service
* /usr/lib/systemd/system/system-update.target.wants/packagekit-offline-update.service
* /usr/share/bash-completion/completions/pkcon
* /usr/share/dbus-1/interfaces/org.freedesktop.PackageKit.Transaction.xml
* /usr/share/dbus-1/interfaces/org.freedesktop.PackageKit.xml
* /usr/share/dbus-1/system-services/org.freedesktop.PackageKit.service
* /usr/share/dbus-1/system.d/org.freedesktop.PackageKit.conf
* /usr/share/doc/packagekit-1.2.8/AUTHORS
* /usr/share/doc/packagekit-1.2.8/COPYING
* /usr/share/doc/packagekit-1.2.8/HACKING
* /usr/share/doc/packagekit-1.2.8/NEWS
* /usr/share/doc/packagekit-1.2.8/README
* /usr/share/doc/packagekit-1.2.8/RELEASE
* /usr/share/gir-1.0/PackageKitGlib-1.0.gir
* /usr/share/locale/ar/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/as/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/ast/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/az/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/bg/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/bn_IN/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/br/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/ca/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/cs/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/cy/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/da/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/de/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/el/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/en_GB/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/eo/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/es/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/eu/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/fa/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/fi/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/fo/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/fr/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/ga/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/gl/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/gu/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/he/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/hi/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/hr/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/hu/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/ia/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/id/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/it/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/ja/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/ka/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/kk/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/kn/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/ko/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/lt/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/lv/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/ml/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/mr/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/ms/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/nb/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/nl/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/nn/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/oc/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/or/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/pa/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/pl/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/pt/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/ro/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/ru/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/si/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/sk/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/sl/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/sq/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/sr/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/sv/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/ta/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/te/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/th/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/tr/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/uk/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/vi/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/wa/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/zh_HK/LC_MESSAGES/PackageKit.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/PackageKit.mo
* /usr/share/man/man1/pkcon.1.gz
* /usr/share/man/man1/pkmon.1.gz
* /usr/share/metainfo/org.freedesktop.packagekit.metainfo.xml
* /usr/share/PackageKit/helpers/test_spawn/search-name.sh
* /usr/share/PackageKit/pk-upgrade-distro.sh
* /usr/share/polkit-1/actions/org.freedesktop.packagekit.policy
* /usr/share/polkit-1/rules.d/org.freedesktop.packagekit.rules
* /usr/share/vala/vapi/packagekit-glib2.deps
* /usr/share/vala/vapi/packagekit-glib2.vapi
* /var/lib/PackageKit/transactions.db
{{< /files >}}