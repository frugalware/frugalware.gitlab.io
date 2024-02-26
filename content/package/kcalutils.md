+++
draft = false
title = "kcalutils 23.08.5-1"
version = "23.08.5-1"
description = "The KDE calendar utility library"
date = "2024-02-19T22:07:58"
aliases = "/packages/218279"
categories = ['kde5']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "269700"
usize = "1863396"
sha1sum = "e4b12340d5eb45ee977e8c6a07a87b5c1323ec8f"
depends = "['kcalendarcore>=5.115.0', 'kidentitymanagement>=23.08.5']"
reverse_depends = "['akonadi-calendar', 'kalarm', 'kmail', 'knotes', 'ktnef']"
+++
The KDE calendar utility library{{< files text="show files" >}}* /usr/include/KPim5/KCalUtils/KCalUtils/DndFactory
* /usr/include/KPim5/KCalUtils/kcalutils/dndfactory.h
* /usr/include/KPim5/KCalUtils/KCalUtils/ICalDrag
* /usr/include/KPim5/KCalUtils/kcalutils/icaldrag.h
* /usr/include/KPim5/KCalUtils/KCalUtils/IncidenceFormatter
* /usr/include/KPim5/KCalUtils/kcalutils/incidenceformatter.h
* /usr/include/KPim5/KCalUtils/kcalutils/kcalutils_export.h
* /usr/include/KPim5/KCalUtils/KCalUtils/RecurrenceActions
* /usr/include/KPim5/KCalUtils/kcalutils/recurrenceactions.h
* /usr/include/KPim5/KCalUtils/KCalUtils/Stringify
* /usr/include/KPim5/KCalUtils/kcalutils/stringify.h
* /usr/include/KPim5/KCalUtils/KCalUtils/VCalDrag
* /usr/include/KPim5/KCalUtils/kcalutils/vcaldrag.h
* /usr/include/KPim5/KCalUtils/kcalutils_version.h
* /usr/lib/cmake/KPim5CalendarUtils/KPim5CalendarUtilsConfig.cmake
* /usr/lib/cmake/KPim5CalendarUtils/KPim5CalendarUtilsConfigVersion.cmake
* /usr/lib/cmake/KPim5CalendarUtils/KPim5CalendarUtilsTargets-release.cmake
* /usr/lib/cmake/KPim5CalendarUtils/KPim5CalendarUtilsTargets.cmake
* /usr/lib/grantlee/5.3/kcalendar_grantlee_plugin.so
* /usr/lib/libKPim5CalendarUtils.so
* /usr/lib/libKPim5CalendarUtils.so.5
* /usr/lib/libKPim5CalendarUtils.so.5.24.5
* /usr/share/doc/kcalutils-23.08.5/README.md
* /usr/share/doc/kcalutils-23.08.5/README.md.license
* /usr/share/locale/ar/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/az/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/bg/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/bs/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/ca/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/cs/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/da/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/de/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/el/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/en_GB/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/es/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/et/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/eu/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/fi/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/fr/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/ga/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/gl/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/hr/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/hu/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/ia/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/it/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/ja/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/ka/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/kk/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/km/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/ko/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/lt/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/mai/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/mr/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/nb/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/nds/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/nl/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/nn/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/pa/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/pl/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/pt/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/ro/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/ru/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/se/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/sk/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/sl/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/sr/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/sr@ijekavian/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/sv/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/ta/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/tr/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/ug/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/uk/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/libkcalutils5.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/libkcalutils5.mo
* /usr/share/qlogging-categories5/kcalutils.categories
* /usr/share/qlogging-categories5/kcalutils.renamecategories
* /usr/share/qt5/mkspecs/modules/qt_KCalUtils.pri
{{< /files >}}