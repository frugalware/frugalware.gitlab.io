+++
draft = false
title = "kauth 6.10.0-1"
version = "6.10.0-1"
description = "Framework which lets applications perform actions as a privileged user."
date = "2025-01-10T13:35:34"
aliases = "/packages/218275"
categories = ['kf6']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "106260"
usize = "421931"
sha1sum = "f6e0002d121df742e98c7a467d503a8558bb608c"
depends = "['kcoreaddons>=6.10.0', 'kwindowsystem>=6.10.0', 'polkit-qt6-1>=0.112.0-11']"
reverse_depends = "['kde-inotify-survey', 'kio', 'kpmcore', 'kwin', 'plasma-desktop']"
+++
### Description: 
Framework which lets applications perform actions as a privileged user.

### Files: 
* /usr/include/KF6/KAuth/kauth_version.h
* /usr/include/KF6/KAuthCore/KAuth/Action
* /usr/include/KF6/KAuthCore/kauth/action.h
* /usr/include/KF6/KAuthCore/KAuth/ActionReply
* /usr/include/KF6/KAuthCore/kauth/actionreply.h
* /usr/include/KF6/KAuthCore/KAuth/ExecuteJob
* /usr/include/KF6/KAuthCore/kauth/executejob.h
* /usr/include/KF6/KAuthCore/KAuth/HelperSupport
* /usr/include/KF6/KAuthCore/kauth/helpersupport.h
* /usr/include/KF6/KAuthCore/kauth/kauthcore_export.h
* /usr/lib/cmake/KF6Auth/KF6AuthConfig.cmake
* /usr/lib/cmake/KF6Auth/KF6AuthConfigVersion.cmake
* /usr/lib/cmake/KF6Auth/KF6AuthMacros.cmake
* /usr/lib/cmake/KF6Auth/KF6AuthTargets-release.cmake
* /usr/lib/cmake/KF6Auth/KF6AuthTargets.cmake
* /usr/lib/cmake/KF6Auth/KF6AuthToolsTargets-release.cmake
* /usr/lib/cmake/KF6Auth/KF6AuthToolsTargets.cmake
* /usr/lib/kauth/kf6/kauth/kauth-policy-gen
* /usr/lib/libKF6AuthCore.so
* /usr/lib/libKF6AuthCore.so.6
* /usr/lib/libKF6AuthCore.so.6.10.0
* /usr/lib/qt6/plugins/kf6/kauth/backend/kauth_backend_plugin.so
* /usr/lib/qt6/plugins/kf6/kauth/helper/kauth_helper_plugin.so
* /usr/share/dbus-1/system.d/org.kde.kf6auth.conf
* /usr/share/doc/kauth-6.10.0/README.md
* /usr/share/kf6/kauth/dbus_policy.stub
* /usr/share/kf6/kauth/dbus_service.stub
* /usr/share/locale/af/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ar/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/as/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ast/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/az/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/be/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/be@latin/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/bg/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/bn/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/bn_IN/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/br/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/bs/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ca/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ca@valencia/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/crh/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/cs/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/csb/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/cy/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/da/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/de/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/el/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/en_GB/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/eo/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/es/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/et/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/eu/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/fa/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/fi/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/fr/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/fy/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ga/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/gd/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/gl/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/gu/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ha/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/he/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/hi/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/hne/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/hr/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/hsb/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/hu/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/hy/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ia/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/id/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/is/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/it/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ja/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ka/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/kk/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/km/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/kn/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ko/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ku/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/lb/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/lt/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/lv/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/mai/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/mk/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ml/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/mr/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ms/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/nb/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/nds/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ne/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/nl/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/nn/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/oc/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/or/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/pa/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/pl/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ps/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/pt/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/pt_BR/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ro/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ru/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/sa/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/se/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/si/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/sk/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/sl/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/sq/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/sr/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/sr@ijekavian/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/sr@latin/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/sv/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ta/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/te/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/tg/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/th/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/tr/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/tt/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/ug/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/uk/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/uz/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/uz@cyrillic/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/vi/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/wa/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/xh/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/zh_CN/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/zh_HK/LC_MESSAGES/kauth6_qt.qm
* /usr/share/locale/zh_TW/LC_MESSAGES/kauth6_qt.qm
* /usr/share/qlogging-categories6/kauth.categories
* /usr/share/qlogging-categories6/kauth.renamecategories
