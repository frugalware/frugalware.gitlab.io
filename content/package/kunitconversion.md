+++
draft = false
title = "kunitconversion 5.115.0-1"
version = "5.115.0-1"
description = "Converting physical units."
date = "2024-02-19T10:40:38"
aliases = "/packages/218358"
categories = ['kf5']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "826716"
usize = "11109758"
sha1sum = "5a718c7a6bb067b4272f204229bae088c3a8d50b"
depends = "['ki18n>=5.115.0', 'qt5-base>=5.15.12']"
reverse_depends = "['kalk', 'kalzium', 'kdelibs4support', 'kdeplasma-addons5']"
+++
Converting physical units."

{{< files text="show files" >}}* /usr/include/KF5/KUnitConversion/KUnitConversion/Converter
* /usr/include/KF5/KUnitConversion/kunitconversion/converter.h
* /usr/include/KF5/KUnitConversion/kunitconversion/kunitconversion_export.h
* /usr/include/KF5/KUnitConversion/KUnitConversion/Unit
* /usr/include/KF5/KUnitConversion/kunitconversion/unit.h
* /usr/include/KF5/KUnitConversion/KUnitConversion/UnitCategory
* /usr/include/KF5/KUnitConversion/kunitconversion/unitcategory.h
* /usr/include/KF5/KUnitConversion/KUnitConversion/Value
* /usr/include/KF5/KUnitConversion/kunitconversion/value.h
* /usr/include/KF5/KUnitConversion/kunitconversion_version.h
* /usr/lib/cmake/KF5UnitConversion/KF5UnitConversionConfig.cmake
* /usr/lib/cmake/KF5UnitConversion/KF5UnitConversionConfigVersion.cmake
* /usr/lib/cmake/KF5UnitConversion/KF5UnitConversionTargets-release.cmake
* /usr/lib/cmake/KF5UnitConversion/KF5UnitConversionTargets.cmake
* /usr/lib/libKF5UnitConversion.so
* /usr/lib/libKF5UnitConversion.so.5
* /usr/lib/libKF5UnitConversion.so.5.115.0
* /usr/share/doc/kunitconversion-5.115.0/README.md
* /usr/share/locale/ar/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/az/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/bg/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/bs/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/ca/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/cs/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/da/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/de/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/el/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/en_GB/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/eo/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/es/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/et/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/eu/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/fi/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/fr/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/ga/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/gd/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/gl/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/hr/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/hu/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/ia/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/id/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/is/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/it/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/ja/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/ka/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/kk/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/ko/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/lt/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/lv/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/ml/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/mr/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/ms/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/nb/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/nds/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/nl/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/nn/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/pa/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/pl/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/pt/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/ro/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/ru/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/se/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/sk/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/sl/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/sr/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/sr@ijekavian/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/sv/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/ta/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/tg/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/th/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/tr/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/ug/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/uk/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/kunitconversion5.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/kunitconversion5.mo
* /usr/share/qlogging-categories5/kunitconversion.categories
* /usr/share/qt5/mkspecs/modules/qt_KUnitConversion.pri
{{< /files >}}