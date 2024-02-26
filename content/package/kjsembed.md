+++
draft = false
title = "kjsembed 5.115.0-1"
version = "5.115.0-1"
description = "Binding Javascript object to QObjects."
date = "2024-02-19T10:46:37"
aliases = "/packages/218329"
categories = ['kf5']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "382528"
usize = "1704159"
sha1sum = "f4e4a56bc37024564b8ade270d5453e7dd1f02bd"
depends = "['ki18n>=5.115.0', 'kjs>=5.115.0', 'qt5-svg>=5.15.12']"
reverse_depends = "['plasma-workspace']"
+++
Binding Javascript object to QObjects.{{< files text="show files" >}}* /usr/bin/kjscmd5
* /usr/bin/kjsconsole
* /usr/include/KF5/KJsEmbed/kjsembed/binding_support.h
* /usr/include/KF5/KJsEmbed/kjsembed/kjseglobal.h
* /usr/include/KF5/KJsEmbed/KJsEmbed/KJsEmbed
* /usr/include/KF5/KJsEmbed/kjsembed/kjsembed.h
* /usr/include/KF5/KJsEmbed/kjsembed/kjsembed_export.h
* /usr/include/KF5/KJsEmbed/kjsembed/pointer.h
* /usr/include/KF5/KJsEmbed/kjsembed/static_binding.h
* /usr/include/KF5/KJsEmbed/kjsembed/variant_binding.h
* /usr/lib/cmake/KF5JsEmbed/KF5JsEmbedConfig.cmake
* /usr/lib/cmake/KF5JsEmbed/KF5JsEmbedConfigVersion.cmake
* /usr/lib/cmake/KF5JsEmbed/KF5JsEmbedTargets-release.cmake
* /usr/lib/cmake/KF5JsEmbed/KF5JsEmbedTargets.cmake
* /usr/lib/libKF5JsEmbed.so
* /usr/lib/libKF5JsEmbed.so.5
* /usr/lib/libKF5JsEmbed.so.5.115.0
* /usr/share/doc/kjsembed-5.115.0/AUTHORS
* /usr/share/doc/kjsembed-5.115.0/COPYING.LIB
* /usr/share/doc/kjsembed-5.115.0/README.md
* /usr/share/locale/af/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/ar/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/as/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/az/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/be/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/be@latin/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/bg/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/bn/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/bn_IN/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/br/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/bs/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/ca/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/crh/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/cs/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/csb/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/cy/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/da/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/de/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/el/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/en_GB/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/eo/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/es/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/et/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/eu/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/fa/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/fi/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/fr/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/fy/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/ga/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/gd/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/gl/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/gu/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/ha/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/he/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/hi/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/hne/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/hr/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/hsb/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/hu/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/hy/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/ia/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/id/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/is/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/it/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/ja/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/ka/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/kk/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/km/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/kn/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/ko/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/ku/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/lb/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/lt/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/lv/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/mai/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/mk/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/ml/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/mr/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/ms/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/nb/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/nds/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/ne/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/nl/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/nn/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/oc/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/or/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/pa/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/pl/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/ps/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/pt/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/ro/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/ru/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/se/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/si/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/sk/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/sl/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/sq/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/sr/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/sr@ijekavian/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/sv/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/ta/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/te/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/tg/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/th/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/tr/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/tt/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/ug/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/uk/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/uz/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/uz@cyrillic/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/vi/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/wa/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/xh/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/zh_HK/LC_MESSAGES/kjsembed5.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/kjsembed5.mo
* /usr/share/man/ca/man1/kjscmd5.1.gz
* /usr/share/man/ca@valencia/man1/kjscmd5.1.gz
* /usr/share/man/de/man1/kjscmd5.1.gz
* /usr/share/man/es/man1/kjscmd5.1.gz
* /usr/share/man/fr/man1/kjscmd5.1.gz
* /usr/share/man/it/man1/kjscmd5.1.gz
* /usr/share/man/man1/kjscmd5.1.gz
* /usr/share/man/nl/man1/kjscmd5.1.gz
* /usr/share/man/pt/man1/kjscmd5.1.gz
* /usr/share/man/pt_BR/man1/kjscmd5.1.gz
* /usr/share/man/ru/man1/kjscmd5.1.gz
* /usr/share/man/sv/man1/kjscmd5.1.gz
* /usr/share/man/tr/man1/kjscmd5.1.gz
* /usr/share/man/uk/man1/kjscmd5.1.gz
* /usr/share/qt5/mkspecs/modules/qt_KJsEmbed.pri
{{< /files >}}