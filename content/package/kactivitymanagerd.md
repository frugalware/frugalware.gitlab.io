+++
draft = false
title = "kactivitymanagerd 5.27.10-5"
version = "5.27.10-5"
description = "System service to manage user's activities, track the usage patterns etc."
date = "2024-02-19T12:15:01"
aliases = "/packages/218271"
categories = ['plasma']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "165456"
usize = "725782"
sha1sum = "9b29a869e1bb86a7f6b8951db918514cd926438a"
depends = "['kio>=5.115.0']"
reverse_depends = "['plasma-desktop']"
+++
System service to manage user's activities, track the usage patterns etc."

{{< files text="show files" >}}* /usr/lib/kf5/kactivitymanagerd
* /usr/lib/libkactivitymanagerd_plugin.so
* /usr/lib/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_activityrunner.so
* /usr/lib/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_activitytemplates.so
* /usr/lib/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_eventspy.so
* /usr/lib/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_globalshortcuts.so
* /usr/lib/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_gtk_eventspy.so
* /usr/lib/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_runapplication.so
* /usr/lib/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_slc.so
* /usr/lib/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_sqlite.so
* /usr/lib/qt5/plugins/kactivitymanagerd/1/kactivitymanagerd_plugin_virtualdesktopswitch.so
* /usr/lib/systemd/user/plasma-kactivitymanagerd.service
* /usr/share/dbus-1/services/org.kde.ActivityManager.service
* /usr/share/doc/kactivitymanagerd-5.27.10/README.developers
* /usr/share/doc/kactivitymanagerd-5.27.10/README.md
* /usr/share/doc/kactivitymanagerd-5.27.10/TODO
* /usr/share/krunner/dbusplugins/plasma-runnners-activities.desktop
* /usr/share/kservices5/kactivitymanagerd.desktop
* /usr/share/locale/ar/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/az/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/bg/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/bs/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/ca/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/cs/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/da/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/de/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/el/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/en_GB/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/es/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/et/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/eu/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/fi/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/fr/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/ga/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/gd/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/gl/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/gu/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/he/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/hi/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/hr/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/hu/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/ia/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/id/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/is/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/it/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/ja/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/ka/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/kk/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/km/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/kn/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/ko/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/lt/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/lv/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/ml/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/mr/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/ms/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/nb/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/nds/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/nl/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/nn/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/pa/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/pl/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/pt/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/ro/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/ru/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/se/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/sk/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/sl/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/sr/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/sr@ijekavian/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/sv/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/tg/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/th/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/tr/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/ug/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/uk/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/vi/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/wa/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/kactivities5.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/kactivities5.mo
* /usr/share/qlogging-categories5/kactivitymanagerd.categories
{{< /files >}}