+++
draft = false
title = "kdnssd 5.115.0-1"
version = "5.115.0-1"
description = "Zeroconf Support for KDE."
date = "2024-02-19T10:17:03"
aliases = "/packages/218304"
categories = ['kf5']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "70488"
usize = "248431"
sha1sum = "6133ee1d375c18df6fb87c5c22297dfd22c1a1d4"
depends = "['avahi>=0.6.31-9', 'qt5-base>=5.15.12']"
reverse_depends = "['kio-extras', 'kio-zeroconf', 'knotes', 'kopete', 'krdc', 'krfb', 'libkdegames', 'smb4k']"
+++
Zeroconf Support for KDE.

{{< files text="show files" >}}* /usr/include/KF5/KDNSSD/DNSSD/DomainBrowser
* /usr/include/KF5/KDNSSD/dnssd/domainbrowser.h
* /usr/include/KF5/KDNSSD/DNSSD/DomainModel
* /usr/include/KF5/KDNSSD/dnssd/domainmodel.h
* /usr/include/KF5/KDNSSD/DNSSD/PublicService
* /usr/include/KF5/KDNSSD/dnssd/publicservice.h
* /usr/include/KF5/KDNSSD/DNSSD/RemoteService
* /usr/include/KF5/KDNSSD/dnssd/remoteservice.h
* /usr/include/KF5/KDNSSD/DNSSD/ServiceBase
* /usr/include/KF5/KDNSSD/dnssd/servicebase.h
* /usr/include/KF5/KDNSSD/DNSSD/ServiceBrowser
* /usr/include/KF5/KDNSSD/dnssd/servicebrowser.h
* /usr/include/KF5/KDNSSD/DNSSD/ServiceModel
* /usr/include/KF5/KDNSSD/dnssd/servicemodel.h
* /usr/include/KF5/KDNSSD/DNSSD/ServiceTypeBrowser
* /usr/include/KF5/KDNSSD/dnssd/servicetypebrowser.h
* /usr/include/KF5/KDNSSD/KDNSSD/DomainBrowser
* /usr/include/KF5/KDNSSD/kdnssd/domainbrowser.h
* /usr/include/KF5/KDNSSD/KDNSSD/DomainModel
* /usr/include/KF5/KDNSSD/kdnssd/domainmodel.h
* /usr/include/KF5/KDNSSD/kdnssd/kdnssd_export.h
* /usr/include/KF5/KDNSSD/KDNSSD/PublicService
* /usr/include/KF5/KDNSSD/kdnssd/publicservice.h
* /usr/include/KF5/KDNSSD/KDNSSD/RemoteService
* /usr/include/KF5/KDNSSD/kdnssd/remoteservice.h
* /usr/include/KF5/KDNSSD/KDNSSD/ServiceBase
* /usr/include/KF5/KDNSSD/kdnssd/servicebase.h
* /usr/include/KF5/KDNSSD/KDNSSD/ServiceBrowser
* /usr/include/KF5/KDNSSD/kdnssd/servicebrowser.h
* /usr/include/KF5/KDNSSD/KDNSSD/ServiceModel
* /usr/include/KF5/KDNSSD/kdnssd/servicemodel.h
* /usr/include/KF5/KDNSSD/KDNSSD/ServiceTypeBrowser
* /usr/include/KF5/KDNSSD/kdnssd/servicetypebrowser.h
* /usr/include/KF5/KDNSSD/kdnssd_version.h
* /usr/lib/cmake/KF5DNSSD/KF5DNSSDConfig.cmake
* /usr/lib/cmake/KF5DNSSD/KF5DNSSDConfigVersion.cmake
* /usr/lib/cmake/KF5DNSSD/KF5DNSSDTargets-release.cmake
* /usr/lib/cmake/KF5DNSSD/KF5DNSSDTargets.cmake
* /usr/lib/libKF5DNSSD.so
* /usr/lib/libKF5DNSSD.so.5
* /usr/lib/libKF5DNSSD.so.5.115.0
* /usr/share/doc/kdnssd-5.115.0/README.md
* /usr/share/locale/af/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/ar/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/as/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/az/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/be/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/be@latin/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/bg/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/bn/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/bn_IN/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/br/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/bs/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/ca/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/ca@valencia/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/crh/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/cs/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/csb/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/cy/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/da/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/de/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/el/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/en_GB/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/eo/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/es/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/et/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/eu/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/fa/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/fi/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/fr/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/fy/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/ga/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/gd/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/gl/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/gu/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/ha/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/he/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/hi/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/hne/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/hr/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/hsb/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/hu/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/hy/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/ia/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/id/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/is/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/it/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/ja/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/ka/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/kk/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/km/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/kn/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/ko/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/ku/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/lb/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/lt/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/lv/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/mai/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/mk/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/ml/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/mr/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/ms/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/nb/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/nds/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/ne/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/nl/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/nn/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/oc/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/or/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/pa/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/pl/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/ps/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/pt/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/pt_BR/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/ro/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/ru/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/se/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/si/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/sk/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/sl/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/sq/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/sr/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/sr@ijekavian/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/sr@latin/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/sv/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/ta/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/te/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/tg/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/th/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/tr/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/tt/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/ug/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/uk/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/uz/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/uz@cyrillic/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/vi/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/wa/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/xh/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/zh_CN/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/zh_HK/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/locale/zh_TW/LC_MESSAGES/kdnssd5_qt.qm
* /usr/share/qt5/mkspecs/modules/qt_KDNSSD.pri
{{< /files >}}