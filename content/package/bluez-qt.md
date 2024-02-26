+++
draft = false
title = "bluez-qt 5.115.0-1"
version = "5.115.0-1"
description = "A Qt wrapper for bluez"
date = "2024-02-19T10:01:35"
aliases = "/packages/218255"
categories = ['kf5']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "225292"
usize = "1017792"
sha1sum = "5080a65296ec440533241cb8ecdbe67e44cf5516"
depends = "['qt5-declarative>=5.15.12']"
reverse_depends = "['bluedevil5', 'powerdevil5']"
+++
A Qt wrapper for bluez{{< spoiler text="show files" >}}* /usr/include/KF5/BluezQt/BluezQt/Adapter
* /usr/include/KF5/BluezQt/bluezqt/adapter.h
* /usr/include/KF5/BluezQt/BluezQt/Agent
* /usr/include/KF5/BluezQt/bluezqt/agent.h
* /usr/include/KF5/BluezQt/bluezqt/bluezqt_export.h
* /usr/include/KF5/BluezQt/BluezQt/Device
* /usr/include/KF5/BluezQt/bluezqt/device.h
* /usr/include/KF5/BluezQt/BluezQt/DevicesModel
* /usr/include/KF5/BluezQt/bluezqt/devicesmodel.h
* /usr/include/KF5/BluezQt/BluezQt/GattApplication
* /usr/include/KF5/BluezQt/bluezqt/gattapplication.h
* /usr/include/KF5/BluezQt/BluezQt/GattCharacteristic
* /usr/include/KF5/BluezQt/bluezqt/gattcharacteristic.h
* /usr/include/KF5/BluezQt/BluezQt/GattCharacteristicRemote
* /usr/include/KF5/BluezQt/bluezqt/gattcharacteristicremote.h
* /usr/include/KF5/BluezQt/BluezQt/GattDescriptorRemote
* /usr/include/KF5/BluezQt/bluezqt/gattdescriptorremote.h
* /usr/include/KF5/BluezQt/BluezQt/GattManager
* /usr/include/KF5/BluezQt/bluezqt/gattmanager.h
* /usr/include/KF5/BluezQt/BluezQt/GattService
* /usr/include/KF5/BluezQt/bluezqt/gattservice.h
* /usr/include/KF5/BluezQt/BluezQt/GattServiceRemote
* /usr/include/KF5/BluezQt/bluezqt/gattserviceremote.h
* /usr/include/KF5/BluezQt/BluezQt/InitManagerJob
* /usr/include/KF5/BluezQt/bluezqt/initmanagerjob.h
* /usr/include/KF5/BluezQt/BluezQt/InitObexManagerJob
* /usr/include/KF5/BluezQt/bluezqt/initobexmanagerjob.h
* /usr/include/KF5/BluezQt/BluezQt/Input
* /usr/include/KF5/BluezQt/bluezqt/input.h
* /usr/include/KF5/BluezQt/BluezQt/Job
* /usr/include/KF5/BluezQt/bluezqt/job.h
* /usr/include/KF5/BluezQt/BluezQt/LEAdvertisement
* /usr/include/KF5/BluezQt/bluezqt/leadvertisement.h
* /usr/include/KF5/BluezQt/BluezQt/LEAdvertisingManager
* /usr/include/KF5/BluezQt/bluezqt/leadvertisingmanager.h
* /usr/include/KF5/BluezQt/BluezQt/Manager
* /usr/include/KF5/BluezQt/bluezqt/manager.h
* /usr/include/KF5/BluezQt/BluezQt/Media
* /usr/include/KF5/BluezQt/bluezqt/media.h
* /usr/include/KF5/BluezQt/BluezQt/MediaEndpoint
* /usr/include/KF5/BluezQt/bluezqt/mediaendpoint.h
* /usr/include/KF5/BluezQt/BluezQt/MediaPlayer
* /usr/include/KF5/BluezQt/bluezqt/mediaplayer.h
* /usr/include/KF5/BluezQt/BluezQt/MediaPlayerTrack
* /usr/include/KF5/BluezQt/bluezqt/mediaplayertrack.h
* /usr/include/KF5/BluezQt/BluezQt/MediaTransport
* /usr/include/KF5/BluezQt/bluezqt/mediatransport.h
* /usr/include/KF5/BluezQt/BluezQt/MediaTypes
* /usr/include/KF5/BluezQt/bluezqt/mediatypes.h
* /usr/include/KF5/BluezQt/BluezQt/ObexAgent
* /usr/include/KF5/BluezQt/bluezqt/obexagent.h
* /usr/include/KF5/BluezQt/BluezQt/ObexFileTransfer
* /usr/include/KF5/BluezQt/bluezqt/obexfiletransfer.h
* /usr/include/KF5/BluezQt/BluezQt/ObexFileTransferEntry
* /usr/include/KF5/BluezQt/bluezqt/obexfiletransferentry.h
* /usr/include/KF5/BluezQt/BluezQt/ObexManager
* /usr/include/KF5/BluezQt/bluezqt/obexmanager.h
* /usr/include/KF5/BluezQt/BluezQt/ObexObjectPush
* /usr/include/KF5/BluezQt/bluezqt/obexobjectpush.h
* /usr/include/KF5/BluezQt/BluezQt/ObexSession
* /usr/include/KF5/BluezQt/bluezqt/obexsession.h
* /usr/include/KF5/BluezQt/BluezQt/ObexTransfer
* /usr/include/KF5/BluezQt/bluezqt/obextransfer.h
* /usr/include/KF5/BluezQt/BluezQt/PendingCall
* /usr/include/KF5/BluezQt/bluezqt/pendingcall.h
* /usr/include/KF5/BluezQt/BluezQt/Profile
* /usr/include/KF5/BluezQt/bluezqt/profile.h
* /usr/include/KF5/BluezQt/BluezQt/Request
* /usr/include/KF5/BluezQt/bluezqt/request.h
* /usr/include/KF5/BluezQt/BluezQt/Rfkill
* /usr/include/KF5/BluezQt/bluezqt/rfkill.h
* /usr/include/KF5/BluezQt/BluezQt/Services
* /usr/include/KF5/BluezQt/bluezqt/services.h
* /usr/include/KF5/BluezQt/BluezQt/TPendingCall
* /usr/include/KF5/BluezQt/bluezqt/tpendingcall.h
* /usr/include/KF5/BluezQt/BluezQt/Types
* /usr/include/KF5/BluezQt/bluezqt/types.h
* /usr/include/KF5/BluezQt/bluezqt_version.h
* /usr/lib/cmake/KF5BluezQt/KF5BluezQtConfig.cmake
* /usr/lib/cmake/KF5BluezQt/KF5BluezQtConfigVersion.cmake
* /usr/lib/cmake/KF5BluezQt/KF5BluezQtTargets-release.cmake
* /usr/lib/cmake/KF5BluezQt/KF5BluezQtTargets.cmake
* /usr/lib/libKF5BluezQt.so
* /usr/lib/libKF5BluezQt.so.5.115.0
* /usr/lib/libKF5BluezQt.so.6
* /usr/lib/pkgconfig/KF5BluezQt.pc
* /usr/lib/udev/rules.d/61-kde-bluetooth-rfkill.rules
* /usr/share/doc/bluez-qt-5.115.0/README.md
* /usr/share/qlogging-categories5/bluezqt.categories
* /usr/share/qlogging-categories5/bluezqt.renamecategories
* /usr/share/qt5/mkspecs/modules/qt_BluezQt.pri
* /usr/share/qt5/qml/org/kde/bluezqt/DevicesModel.qml
* /usr/share/qt5/qml/org/kde/bluezqt/libbluezqtextensionplugin.so
* /usr/share/qt5/qml/org/kde/bluezqt/qmldir
{{< /spoiler >}}