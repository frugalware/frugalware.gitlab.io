+++
draft = false
title = "kxmlrpcclient 5.115.0-1"
version = "5.115.0-1"
description = "XML-RPC client library for KDE."
date = "2024-02-19T11:32:46"
aliases = "/packages/218368"
categories = ['kf5']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "37864"
usize = "134634"
sha1sum = "d4cdf9a45682136ddb3c8520080edc1edb7e7152"
depends = "['kio>=5.115.0']"
reverse_depends = "['drkonqi', 'plasma-workspace']"
+++
XML-RPC client library for KDE."

{{< files text="show files" >}}* /usr/include/KF5/KXmlRpcClient/KXmlRpcClient/Client
* /usr/include/KF5/KXmlRpcClient/kxmlrpcclient/client.h
* /usr/include/KF5/KXmlRpcClient/kxmlrpcclient/kxmlrpcclient_export.h
* /usr/include/KF5/KXmlRpcClient/kxmlrpcclient_version.h
* /usr/lib/cmake/KF5XmlRpcClient/KF5XmlRpcClientConfig.cmake
* /usr/lib/cmake/KF5XmlRpcClient/KF5XmlRpcClientConfigVersion.cmake
* /usr/lib/cmake/KF5XmlRpcClient/KF5XmlRpcClientTargets-release.cmake
* /usr/lib/cmake/KF5XmlRpcClient/KF5XmlRpcClientTargets.cmake
* /usr/lib/libKF5XmlRpcClient.so
* /usr/lib/libKF5XmlRpcClient.so.5
* /usr/lib/libKF5XmlRpcClient.so.5.115.0
* /usr/share/doc/kxmlrpcclient-5.115.0/README.md
* /usr/share/locale/ar/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/az/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/be/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/bg/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/bs/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/ca/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/cs/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/da/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/de/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/el/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/en_GB/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/eo/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/es/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/et/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/eu/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/fi/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/fr/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/ga/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/gd/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/gl/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/he/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/hi/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/hne/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/hu/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/ia/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/id/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/it/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/ja/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/ka/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/kk/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/km/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/ko/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/lt/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/lv/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/ml/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/mr/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/nb/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/nds/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/nl/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/nn/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/pa/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/pl/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/pt/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/ro/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/ru/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/se/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/sk/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/sl/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/sq/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/sr/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/sr@ijekavian/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/sv/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/tg/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/tr/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/ug/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/uk/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/libkxmlrpcclient5.mo
* /usr/share/qlogging-categories5/kxmlrpcclient.categories
* /usr/share/qlogging-categories5/kxmlrpcclient.renamecategories
* /usr/share/qt5/mkspecs/modules/qt_KXmlRpcClient.pri
{{< /files >}}