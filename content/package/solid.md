+++
draft = false
title = "solid 5.115.0-1"
version = "5.115.0-1"
description = "KDE Desktop hardware abstraction."
date = "2024-02-19T10:12:32"
aliases = "/packages/218411"
categories = ['kf5']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "326228"
usize = "1773475"
sha1sum = "2b325e80e239a3cfbf6386cd7e59dd7d4dbfac06"
depends = "['libimobiledevice', 'libsystemd>=231-6', 'media-player-info', 'qt5-declarative>=5.15.12', 'udisks2>=2.1.7-2', 'upower>=0.99.4-2']"
reverse_depends = "['discover', 'dolphin', 'itinerary', 'kamoso', 'kinfocenter5', 'kio', 'libkcompactdisc', 'smb4k']"
+++
KDE Desktop hardware abstraction."

{{< files text="show files" >}}* /usr/bin/solid-hardware5
* /usr/include/KF5/Solid/Solid/Battery
* /usr/include/KF5/Solid/solid/battery.h
* /usr/include/KF5/Solid/Solid/Block
* /usr/include/KF5/Solid/solid/block.h
* /usr/include/KF5/Solid/Solid/Camera
* /usr/include/KF5/Solid/solid/camera.h
* /usr/include/KF5/Solid/Solid/Device
* /usr/include/KF5/Solid/solid/device.h
* /usr/include/KF5/Solid/Solid/DeviceInterface
* /usr/include/KF5/Solid/solid/deviceinterface.h
* /usr/include/KF5/Solid/Solid/DeviceNotifier
* /usr/include/KF5/Solid/solid/devicenotifier.h
* /usr/include/KF5/Solid/Solid/GenericInterface
* /usr/include/KF5/Solid/solid/genericinterface.h
* /usr/include/KF5/Solid/Solid/NetworkShare
* /usr/include/KF5/Solid/solid/networkshare.h
* /usr/include/KF5/Solid/Solid/OpticalDisc
* /usr/include/KF5/Solid/solid/opticaldisc.h
* /usr/include/KF5/Solid/Solid/OpticalDrive
* /usr/include/KF5/Solid/solid/opticaldrive.h
* /usr/include/KF5/Solid/Solid/PortableMediaPlayer
* /usr/include/KF5/Solid/solid/portablemediaplayer.h
* /usr/include/KF5/Solid/Solid/Predicate
* /usr/include/KF5/Solid/solid/predicate.h
* /usr/include/KF5/Solid/Solid/Processor
* /usr/include/KF5/Solid/solid/processor.h
* /usr/include/KF5/Solid/Solid/SolidNamespace
* /usr/include/KF5/Solid/solid/solidnamespace.h
* /usr/include/KF5/Solid/solid/solid_export.h
* /usr/include/KF5/Solid/Solid/StorageAccess
* /usr/include/KF5/Solid/solid/storageaccess.h
* /usr/include/KF5/Solid/Solid/StorageDrive
* /usr/include/KF5/Solid/solid/storagedrive.h
* /usr/include/KF5/Solid/Solid/StorageVolume
* /usr/include/KF5/Solid/solid/storagevolume.h
* /usr/include/KF5/Solid/solid_version.h
* /usr/lib/cmake/KF5Solid/KF5SolidConfig.cmake
* /usr/lib/cmake/KF5Solid/KF5SolidConfigVersion.cmake
* /usr/lib/cmake/KF5Solid/KF5SolidTargets-release.cmake
* /usr/lib/cmake/KF5Solid/KF5SolidTargets.cmake
* /usr/lib/libKF5Solid.so
* /usr/lib/libKF5Solid.so.5
* /usr/lib/libKF5Solid.so.5.115.0
* /usr/share/doc/solid-5.115.0/README.md
* /usr/share/doc/solid-5.115.0/TODO
* /usr/share/locale/ar/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/az/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/bg/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/bs/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/ca/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/ca@valencia/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/cs/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/da/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/de/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/el/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/en_GB/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/eo/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/es/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/et/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/eu/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/fi/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/fr/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/ga/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/gd/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/gl/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/he/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/hr/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/hu/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/ia/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/id/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/is/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/it/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/ja/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/ka/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/kk/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/km/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/ko/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/lt/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/lv/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/ml/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/mr/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/ms/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/nb/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/nds/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/nl/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/nn/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/pa/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/pl/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/pt/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/pt_BR/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/ro/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/ru/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/se/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/sk/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/sl/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/sr/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/sr@ijekavian/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/sr@latin/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/sv/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/ta/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/tg/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/th/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/tr/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/ug/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/uk/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/zh_CN/LC_MESSAGES/solid5_qt.qm
* /usr/share/locale/zh_TW/LC_MESSAGES/solid5_qt.qm
* /usr/share/qlogging-categories5/solid.categories
* /usr/share/qlogging-categories5/solid.renamecategories
* /usr/share/qt5/mkspecs/modules/qt_Solid.pri
* /usr/share/qt5/qml/org/kde/solid/libsolidextensionplugin.so
* /usr/share/qt5/qml/org/kde/solid/qmldir
{{< /files >}}