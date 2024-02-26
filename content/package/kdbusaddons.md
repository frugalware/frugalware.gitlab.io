+++
draft = false
title = "kdbusaddons 5.115.0-1"
version = "5.115.0-1"
description = "Convenience classes for QtDBus."
date = "2024-02-19T10:21:21"
aliases = "/packages/218288"
categories = ['kf5']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "60952"
usize = "226172"
sha1sum = "ccef1093c2ebb6e4d9f6e580cad622a9f2e27d34"
depends = "['qt5-x11extras>=5.15.12']"
reverse_depends = "['akonadi-mime', 'calamares-frugalware', 'dolphin', 'kaccounts-integration', 'kdebugsettings', 'keysmith', 'kmousetool', 'kongress', 'kopete', 'kservice', 'plasma-browser-integration', 'plasma-sdk', 'polkit-kde-agent-1', 'tokodon']"
+++
Convenience classes for QtDBus."

{{< files text="show files" >}}* /usr/bin/kquitapp5
* /usr/include/KF5/KDBusAddons/kdbusaddons_export.h
* /usr/include/KF5/KDBusAddons/kdbusaddons_version.h
* /usr/include/KF5/KDBusAddons/KDBusConnectionPool
* /usr/include/KF5/KDBusAddons/kdbusconnectionpool.h
* /usr/include/KF5/KDBusAddons/KDBusInterProcessLock
* /usr/include/KF5/KDBusAddons/kdbusinterprocesslock.h
* /usr/include/KF5/KDBusAddons/KDBusService
* /usr/include/KF5/KDBusAddons/kdbusservice.h
* /usr/include/KF5/KDBusAddons/KDEDModule
* /usr/include/KF5/KDBusAddons/kdedmodule.h
* /usr/include/KF5/KDBusAddons/KDEInitInterface
* /usr/include/KF5/KDBusAddons/kdeinitinterface.h
* /usr/include/KF5/KDBusAddons/UpdateLaunchEnvironmentJob
* /usr/include/KF5/KDBusAddons/updatelaunchenvironmentjob.h
* /usr/lib/cmake/KF5DBusAddons/KF5dbus.service.in
* /usr/lib/cmake/KF5DBusAddons/KF5DBusAddonsConfig.cmake
* /usr/lib/cmake/KF5DBusAddons/KF5DBusAddonsConfigVersion.cmake
* /usr/lib/cmake/KF5DBusAddons/KF5DBusAddonsMacros.cmake
* /usr/lib/cmake/KF5DBusAddons/KF5DBusAddonsTargets-release.cmake
* /usr/lib/cmake/KF5DBusAddons/KF5DBusAddonsTargets.cmake
* /usr/lib/libKF5DBusAddons.so
* /usr/lib/libKF5DBusAddons.so.5
* /usr/lib/libKF5DBusAddons.so.5.115.0
* /usr/share/doc/kdbusaddons-5.115.0/README.md
* /usr/share/locale/ar/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/az/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/bg/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/bs/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/ca/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/ca@valencia/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/cs/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/da/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/de/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/el/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/en_GB/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/eo/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/es/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/et/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/eu/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/fi/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/fr/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/gd/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/gl/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/hi/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/hu/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/ia/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/id/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/is/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/it/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/ja/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/ka/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/ko/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/lt/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/ml/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/nb/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/nds/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/nl/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/nn/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/pa/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/pl/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/pt/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/pt_BR/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/ro/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/ru/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/se/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/sk/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/sl/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/sr/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/sr@ijekavian/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/sr@latin/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/sv/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/tg/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/tr/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/uk/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/zh_CN/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/locale/zh_TW/LC_MESSAGES/kdbusaddons5_qt.qm
* /usr/share/qlogging-categories5/kdbusaddons.categories
* /usr/share/qlogging-categories5/kdbusaddons.renamecategories
* /usr/share/qt5/mkspecs/modules/qt_KDBusAddons.pri
{{< /files >}}