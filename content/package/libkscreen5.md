+++
draft = false
title = "libkscreen5 5.27.10-5"
version = "5.27.10-5"
description = "KDE screen management software."
date = "2024-02-19T12:10:02"
aliases = "/packages/218372"
categories = ['plasma']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "231536"
usize = "928256"
sha1sum = "ae6ead5ff3422fdb1d6acaa15d3651b14291fb9b"
depends = "['kconfig>=5.115.0', 'kwayland>=5.115.0', 'libxrandr>=1.5.0-5', 'qt5-x11extras>=5.15.12']"
reverse_depends = "['kscreen5', 'plasma-workspace']"
+++
KDE screen management software.

{{< files text="show files" >}}* /usr/bin/kscreen-doctor
* /usr/include/KF5/KScreen/kscreen/backendmanager_p.h
* /usr/include/KF5/KScreen/KScreen/Config
* /usr/include/KF5/KScreen/kscreen/config.h
* /usr/include/KF5/KScreen/KScreen/ConfigMonitor
* /usr/include/KF5/KScreen/kscreen/configmonitor.h
* /usr/include/KF5/KScreen/KScreen/ConfigOperation
* /usr/include/KF5/KScreen/kscreen/configoperation.h
* /usr/include/KF5/KScreen/KScreen/EDID
* /usr/include/KF5/KScreen/kscreen/edid.h
* /usr/include/KF5/KScreen/KScreen/GetConfigOperation
* /usr/include/KF5/KScreen/kscreen/getconfigoperation.h
* /usr/include/KF5/KScreen/kscreen/kscreen_export.h
* /usr/include/KF5/KScreen/KScreen/Log
* /usr/include/KF5/KScreen/kscreen/log.h
* /usr/include/KF5/KScreen/KScreen/Mode
* /usr/include/KF5/KScreen/kscreen/mode.h
* /usr/include/KF5/KScreen/KScreen/Output
* /usr/include/KF5/KScreen/kscreen/output.h
* /usr/include/KF5/KScreen/KScreen/Screen
* /usr/include/KF5/KScreen/kscreen/screen.h
* /usr/include/KF5/KScreen/KScreen/SetConfigOperation
* /usr/include/KF5/KScreen/kscreen/setconfigoperation.h
* /usr/include/KF5/KScreen/KScreen/Types
* /usr/include/KF5/KScreen/kscreen/types.h
* /usr/include/KF5/KScreen/KScreenDpms/Dpms
* /usr/include/KF5/KScreen/kscreendpms/dpms.h
* /usr/include/KF5/KScreen/kscreendpms/kscreendpms_export.h
* /usr/include/KF5/kscreen_version.h
* /usr/lib/cmake/KF5Screen/KF5ScreenConfig.cmake
* /usr/lib/cmake/KF5Screen/KF5ScreenConfigVersion.cmake
* /usr/lib/cmake/KF5Screen/KF5ScreenTargets-release.cmake
* /usr/lib/cmake/KF5Screen/KF5ScreenTargets.cmake
* /usr/lib/kf5/kf5/kscreen_backend_launcher
* /usr/lib/libKF5Screen.so
* /usr/lib/libKF5Screen.so.5.27.10
* /usr/lib/libKF5Screen.so.8
* /usr/lib/libKF5ScreenDpms.so
* /usr/lib/libKF5ScreenDpms.so.5.27.10
* /usr/lib/libKF5ScreenDpms.so.8
* /usr/lib/pkgconfig/kscreen2.pc
* /usr/lib/qt5/plugins/kf5/kscreen/KSC_Fake.so
* /usr/lib/qt5/plugins/kf5/kscreen/KSC_KWayland.so
* /usr/lib/qt5/plugins/kf5/kscreen/KSC_QScreen.so
* /usr/lib/qt5/plugins/kf5/kscreen/KSC_XRandR.so
* /usr/lib/qt5/plugins/kf5/kscreen/KSC_XRandR11.so
* /usr/lib/systemd/user/plasma-kscreen.service
* /usr/share/dbus-1/services/org.kde.kscreen.service
* /usr/share/doc/libkscreen5-5.27.10/README.md
* /usr/share/locale/ca/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/ca@valencia/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/cs/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/de/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/en_GB/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/es/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/eu/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/fi/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/fr/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/gl/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/id/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/it/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/ja/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/ka/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/ko/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/nl/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/nn/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/pl/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/pt/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/pt_BR/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/ru/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/sk/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/sl/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/sv/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/tr/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/uk/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/zh_CN/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/locale/zh_TW/LC_MESSAGES/libkscreen5_qt.qm
* /usr/share/qlogging-categories5/libkscreen.categories
* /usr/share/qt5/mkspecs/modules/qt_KScreen.pri
* /usr/share/zsh/site-functions/_kscreen-doctor
{{< /files >}}