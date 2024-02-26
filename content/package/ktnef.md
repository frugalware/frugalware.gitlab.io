+++
draft = false
title = "ktnef 23.08.5-1"
version = "23.08.5-1"
description = "Desc: C++ API for the handling of TNEF data."
date = "2024-02-19T23:27:48"
aliases = "/packages/218356"
categories = ['kde5']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "122084"
usize = "665661"
sha1sum = "48132782e5f19628311674fcc4d4662ac7b7c4e8"
depends = "['kcalutils>=23.08.5', 'kcontacts>=5.115.0']"
reverse_depends = "['kdepim-addons', 'kmail']"
+++
Desc: C++ API for the handling of TNEF data.

{{< files text="show files" >}}* /usr/include/KPim5/KTNEF/KTNEF/Formatter
* /usr/include/KPim5/KTNEF/ktnef/formatter.h
* /usr/include/KPim5/KTNEF/KTNEF/KTNEFAttach
* /usr/include/KPim5/KTNEF/ktnef/ktnefattach.h
* /usr/include/KPim5/KTNEF/KTNEF/KTNEFDefs
* /usr/include/KPim5/KTNEF/ktnef/ktnefdefs.h
* /usr/include/KPim5/KTNEF/KTNEF/KTNEFMessage
* /usr/include/KPim5/KTNEF/ktnef/ktnefmessage.h
* /usr/include/KPim5/KTNEF/KTNEF/KTNEFParser
* /usr/include/KPim5/KTNEF/ktnef/ktnefparser.h
* /usr/include/KPim5/KTNEF/KTNEF/KTNEFProperty
* /usr/include/KPim5/KTNEF/ktnef/ktnefproperty.h
* /usr/include/KPim5/KTNEF/KTNEF/KTNEFPropertySet
* /usr/include/KPim5/KTNEF/ktnef/ktnefpropertyset.h
* /usr/include/KPim5/KTNEF/KTNEF/KTNEFWriter
* /usr/include/KPim5/KTNEF/ktnef/ktnefwriter.h
* /usr/include/KPim5/KTNEF/ktnef/ktnef_export.h
* /usr/include/KPim5/KTNEF/ktnef_version.h
* /usr/lib/cmake/KPim5Tnef/KPim5TnefConfig.cmake
* /usr/lib/cmake/KPim5Tnef/KPim5TnefConfigVersion.cmake
* /usr/lib/cmake/KPim5Tnef/KPim5TnefTargets-release.cmake
* /usr/lib/cmake/KPim5Tnef/KPim5TnefTargets.cmake
* /usr/lib/libKPim5Tnef.so
* /usr/lib/libKPim5Tnef.so.5
* /usr/lib/libKPim5Tnef.so.5.24.5
* /usr/share/doc/ktnef-23.08.5/AUTHORS
* /usr/share/locale/ar/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/be/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/bs/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/ca/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/cs/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/da/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/de/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/el/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/en_GB/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/eo/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/es/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/et/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/eu/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/fi/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/fr/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/ga/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/gl/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/hi/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/hne/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/hu/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/ia/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/it/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/ja/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/ka/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/kk/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/km/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/ko/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/lt/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/lv/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/mai/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/mr/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/nb/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/nds/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/nl/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/nn/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/pa/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/pl/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/pt/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/ro/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/ru/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/se/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/sk/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/sl/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/sq/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/sr/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/sr@ijekavian/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/sv/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/tr/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/ug/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/uk/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/libktnef5.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/libktnef5.mo
* /usr/share/qlogging-categories5/ktnef.categories
* /usr/share/qlogging-categories5/ktnef.renamecategories
* /usr/share/qt5/mkspecs/modules/qt_KTNef.pri
{{< /files >}}