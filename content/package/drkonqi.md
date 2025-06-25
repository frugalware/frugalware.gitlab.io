+++
draft = false
title = "drkonqi 6.4.1-1"
version = "6.4.1-1"
description = "The KDE Crash Handler."
date = "2025-06-25T08:04:10"
aliases = "/packages/219483"
categories = ['plasma']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "638040"
usize = "3324479"
sha1sum = "2dfa0eb1608e2f2d15ace52c96356ee8a9a7be53"
depends = "['kcmutils>=6.15.0', 'kidletime>=6.15.0', 'kio>=6.15.0', 'kirigami>=6.15.0', 'kitemmodels>=6.15.0', 'kstatusnotifieritem>=6.15.0', 'python3-psutil', 'python3-pygdbmi', 'python3-sentry-sdk', 'syntax-highlighting>=6.15.0']"
+++
### Description: 
The KDE Crash Handler.

### Files: 
* /usr/bin/drkonqi-coredump-gui
* /usr/bin/drkonqi-sentry-data
* /usr/lib/drkonqi/drkonqi
* /usr/lib/drkonqi/drkonqi-coredump-cleanup
* /usr/lib/drkonqi/drkonqi-coredump-launcher
* /usr/lib/drkonqi/drkonqi-coredump-processor
* /usr/lib/drkonqi/drkonqi-sentry-postman
* /usr/lib/drkonqi/kf6/drkonqi-polkit-helper
* /usr/lib/qt6/plugins/drkonqi/KDECoredumpNotifierTruck.so
* /usr/lib/systemd/system/drkonqi-coredump-processor@.service
* /usr/lib/systemd/system/systemd-coredump@.service.wants/drkonqi-coredump-processor@.service
* /usr/lib/systemd/user/default.target.wants/drkonqi-coredump-cleanup.service
* /usr/lib/systemd/user/default.target.wants/drkonqi-sentry-postman.path
* /usr/lib/systemd/user/drkonqi-coredump-cleanup.service
* /usr/lib/systemd/user/drkonqi-coredump-cleanup.timer
* /usr/lib/systemd/user/drkonqi-coredump-launcher.socket
* /usr/lib/systemd/user/drkonqi-coredump-launcher@.service
* /usr/lib/systemd/user/drkonqi-coredump-pickup.service
* /usr/lib/systemd/user/drkonqi-sentry-postman.path
* /usr/lib/systemd/user/drkonqi-sentry-postman.service
* /usr/lib/systemd/user/drkonqi-sentry-postman.timer
* /usr/lib/systemd/user/plasma-core.target.wants/drkonqi-coredump-pickup.service
* /usr/lib/systemd/user/plasma-core.target.wants/drkonqi-sentry-postman.path
* /usr/lib/systemd/user/plasma-core.target.wants/drkonqi-sentry-postman.timer
* /usr/lib/systemd/user/sockets.target.wants/drkonqi-coredump-launcher.socket
* /usr/lib/systemd/user/timers.target.wants/drkonqi-coredump-cleanup.timer
* /usr/lib/systemd/user/timers.target.wants/drkonqi-sentry-postman.timer
* /usr/share/applications/org.kde.drkonqi.coredump.gui.desktop
* /usr/share/applications/org.kde.drkonqi.desktop
* /usr/share/dbus-1/system-services/org.kde.drkonqi.service
* /usr/share/dbus-1/system.d/org.kde.drkonqi.conf
* /usr/share/doc/drkonqi-6.4.1/README.md
* /usr/share/drkonqi/gdb/python/gdb_preamble/preamble.py
* /usr/share/drkonqi/gdb/python/gdb_preamble/__init__.py
* /usr/share/drkonqi/mappings
* /usr/share/locale/af/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/ar/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/ast/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/az/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/be/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/bg/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/bn/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/bn_IN/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/br/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/bs/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/ca/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/cs/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/csb/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/cy/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/da/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/de/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/el/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/en_GB/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/eo/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/es/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/et/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/eu/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/fa/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/fi/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/fr/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/fy/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/ga/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/gl/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/gu/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/he/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/hi/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/hne/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/hr/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/hsb/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/hu/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/ia/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/id/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/is/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/it/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/ja/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/ka/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/kk/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/km/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/kn/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/ko/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/ku/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/lt/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/lv/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/mai/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/mk/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/ml/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/mr/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/ms/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/nb/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/nds/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/ne/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/nl/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/nn/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/oc/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/or/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/pa/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/pl/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/pt/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/ro/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/ru/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/sa/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/se/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/si/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/sk/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/sl/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/sq/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/sr/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/sr@ijekavian/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/sv/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/ta/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/te/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/tg/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/th/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/tr/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/ug/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/uk/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/uz/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/uz@cyrillic/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/vi/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/wa/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/xh/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/drkonqi.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/drkonqi.mo
* /usr/share/polkit-1/actions/org.kde.drkonqi.policy
* /usr/share/qlogging-categories6/drkonqi.categories
