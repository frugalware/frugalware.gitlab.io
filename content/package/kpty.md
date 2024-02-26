+++
draft = false
title = "kpty 5.115.0-1"
version = "5.115.0-1"
description = "Interfacing with pseudo terminal devices."
date = "2024-02-19T10:39:36"
aliases = "/packages/218346"
categories = ['kf5']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "44804"
usize = "154505"
sha1sum = "0e78942819a2fbb24957c95aa434ba574898c221"
depends = "['kcoreaddons>=5.115.0', 'ki18n>=5.115.0', 'libutempter']"
reverse_depends = "['ark', 'cantor', 'kdesu', 'kio-extras', 'konsole', 'kwrited5', 'okular']"
+++
Interfacing with pseudo terminal devices.{{< files text="show files" >}}* /usr/include/KF5/KPty/KPty
* /usr/include/KF5/KPty/kpty.h
* /usr/include/KF5/KPty/KPtyDevice
* /usr/include/KF5/KPty/kptydevice.h
* /usr/include/KF5/KPty/KPtyProcess
* /usr/include/KF5/KPty/kptyprocess.h
* /usr/include/KF5/KPty/kpty_export.h
* /usr/include/KF5/KPty/kpty_version.h
* /usr/lib/cmake/KF5Pty/KF5PtyConfig.cmake
* /usr/lib/cmake/KF5Pty/KF5PtyConfigVersion.cmake
* /usr/lib/cmake/KF5Pty/KF5PtyTargets-release.cmake
* /usr/lib/cmake/KF5Pty/KF5PtyTargets.cmake
* /usr/lib/libKF5Pty.so
* /usr/lib/libKF5Pty.so.5
* /usr/lib/libKF5Pty.so.5.115.0
* /usr/share/doc/kpty-5.115.0/README.md
* /usr/share/locale/af/LC_MESSAGES/kpty5.mo
* /usr/share/locale/ar/LC_MESSAGES/kpty5.mo
* /usr/share/locale/as/LC_MESSAGES/kpty5.mo
* /usr/share/locale/az/LC_MESSAGES/kpty5.mo
* /usr/share/locale/be/LC_MESSAGES/kpty5.mo
* /usr/share/locale/be@latin/LC_MESSAGES/kpty5.mo
* /usr/share/locale/bg/LC_MESSAGES/kpty5.mo
* /usr/share/locale/bn/LC_MESSAGES/kpty5.mo
* /usr/share/locale/bn_IN/LC_MESSAGES/kpty5.mo
* /usr/share/locale/br/LC_MESSAGES/kpty5.mo
* /usr/share/locale/bs/LC_MESSAGES/kpty5.mo
* /usr/share/locale/ca/LC_MESSAGES/kpty5.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/kpty5.mo
* /usr/share/locale/crh/LC_MESSAGES/kpty5.mo
* /usr/share/locale/cs/LC_MESSAGES/kpty5.mo
* /usr/share/locale/csb/LC_MESSAGES/kpty5.mo
* /usr/share/locale/cy/LC_MESSAGES/kpty5.mo
* /usr/share/locale/da/LC_MESSAGES/kpty5.mo
* /usr/share/locale/de/LC_MESSAGES/kpty5.mo
* /usr/share/locale/el/LC_MESSAGES/kpty5.mo
* /usr/share/locale/en_GB/LC_MESSAGES/kpty5.mo
* /usr/share/locale/eo/LC_MESSAGES/kpty5.mo
* /usr/share/locale/es/LC_MESSAGES/kpty5.mo
* /usr/share/locale/et/LC_MESSAGES/kpty5.mo
* /usr/share/locale/eu/LC_MESSAGES/kpty5.mo
* /usr/share/locale/fa/LC_MESSAGES/kpty5.mo
* /usr/share/locale/fi/LC_MESSAGES/kpty5.mo
* /usr/share/locale/fr/LC_MESSAGES/kpty5.mo
* /usr/share/locale/fy/LC_MESSAGES/kpty5.mo
* /usr/share/locale/ga/LC_MESSAGES/kpty5.mo
* /usr/share/locale/gd/LC_MESSAGES/kpty5.mo
* /usr/share/locale/gl/LC_MESSAGES/kpty5.mo
* /usr/share/locale/gu/LC_MESSAGES/kpty5.mo
* /usr/share/locale/ha/LC_MESSAGES/kpty5.mo
* /usr/share/locale/he/LC_MESSAGES/kpty5.mo
* /usr/share/locale/hi/LC_MESSAGES/kpty5.mo
* /usr/share/locale/hne/LC_MESSAGES/kpty5.mo
* /usr/share/locale/hr/LC_MESSAGES/kpty5.mo
* /usr/share/locale/hsb/LC_MESSAGES/kpty5.mo
* /usr/share/locale/hu/LC_MESSAGES/kpty5.mo
* /usr/share/locale/hy/LC_MESSAGES/kpty5.mo
* /usr/share/locale/ia/LC_MESSAGES/kpty5.mo
* /usr/share/locale/id/LC_MESSAGES/kpty5.mo
* /usr/share/locale/is/LC_MESSAGES/kpty5.mo
* /usr/share/locale/it/LC_MESSAGES/kpty5.mo
* /usr/share/locale/ja/LC_MESSAGES/kpty5.mo
* /usr/share/locale/ka/LC_MESSAGES/kpty5.mo
* /usr/share/locale/kk/LC_MESSAGES/kpty5.mo
* /usr/share/locale/km/LC_MESSAGES/kpty5.mo
* /usr/share/locale/kn/LC_MESSAGES/kpty5.mo
* /usr/share/locale/ko/LC_MESSAGES/kpty5.mo
* /usr/share/locale/ku/LC_MESSAGES/kpty5.mo
* /usr/share/locale/lb/LC_MESSAGES/kpty5.mo
* /usr/share/locale/lt/LC_MESSAGES/kpty5.mo
* /usr/share/locale/lv/LC_MESSAGES/kpty5.mo
* /usr/share/locale/mai/LC_MESSAGES/kpty5.mo
* /usr/share/locale/mk/LC_MESSAGES/kpty5.mo
* /usr/share/locale/ml/LC_MESSAGES/kpty5.mo
* /usr/share/locale/mr/LC_MESSAGES/kpty5.mo
* /usr/share/locale/ms/LC_MESSAGES/kpty5.mo
* /usr/share/locale/nb/LC_MESSAGES/kpty5.mo
* /usr/share/locale/nds/LC_MESSAGES/kpty5.mo
* /usr/share/locale/ne/LC_MESSAGES/kpty5.mo
* /usr/share/locale/nl/LC_MESSAGES/kpty5.mo
* /usr/share/locale/nn/LC_MESSAGES/kpty5.mo
* /usr/share/locale/oc/LC_MESSAGES/kpty5.mo
* /usr/share/locale/or/LC_MESSAGES/kpty5.mo
* /usr/share/locale/pa/LC_MESSAGES/kpty5.mo
* /usr/share/locale/pl/LC_MESSAGES/kpty5.mo
* /usr/share/locale/ps/LC_MESSAGES/kpty5.mo
* /usr/share/locale/pt/LC_MESSAGES/kpty5.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/kpty5.mo
* /usr/share/locale/ro/LC_MESSAGES/kpty5.mo
* /usr/share/locale/ru/LC_MESSAGES/kpty5.mo
* /usr/share/locale/se/LC_MESSAGES/kpty5.mo
* /usr/share/locale/si/LC_MESSAGES/kpty5.mo
* /usr/share/locale/sk/LC_MESSAGES/kpty5.mo
* /usr/share/locale/sl/LC_MESSAGES/kpty5.mo
* /usr/share/locale/sq/LC_MESSAGES/kpty5.mo
* /usr/share/locale/sr/LC_MESSAGES/kpty5.mo
* /usr/share/locale/sr@ijekavian/LC_MESSAGES/kpty5.mo
* /usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kpty5.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/kpty5.mo
* /usr/share/locale/sv/LC_MESSAGES/kpty5.mo
* /usr/share/locale/ta/LC_MESSAGES/kpty5.mo
* /usr/share/locale/te/LC_MESSAGES/kpty5.mo
* /usr/share/locale/tg/LC_MESSAGES/kpty5.mo
* /usr/share/locale/th/LC_MESSAGES/kpty5.mo
* /usr/share/locale/tr/LC_MESSAGES/kpty5.mo
* /usr/share/locale/tt/LC_MESSAGES/kpty5.mo
* /usr/share/locale/ug/LC_MESSAGES/kpty5.mo
* /usr/share/locale/uk/LC_MESSAGES/kpty5.mo
* /usr/share/locale/uz/LC_MESSAGES/kpty5.mo
* /usr/share/locale/uz@cyrillic/LC_MESSAGES/kpty5.mo
* /usr/share/locale/vi/LC_MESSAGES/kpty5.mo
* /usr/share/locale/wa/LC_MESSAGES/kpty5.mo
* /usr/share/locale/xh/LC_MESSAGES/kpty5.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/kpty5.mo
* /usr/share/locale/zh_HK/LC_MESSAGES/kpty5.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/kpty5.mo
* /usr/share/qlogging-categories5/kpty.categories
* /usr/share/qt5/mkspecs/modules/qt_KPty.pri
{{< /files >}}