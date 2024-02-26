+++
draft = false
title = "kbookmarks 5.115.0-1"
version = "5.115.0-1"
description = "Framework that let you access and manipulate bookmarks stored using XBEL format."
date = "2024-02-19T11:00:55"
aliases = "/packages/218277"
categories = ['kf5']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "141820"
usize = "684019"
sha1sum = "06f3fb3b54e8a87ed3630036e37fa335bd237a22"
depends = "['kxmlgui>=5.115.0']"
reverse_depends = "['dolphin', 'kcharselect', 'kio', 'krdc']"
+++
Framework that let you access and manipulate bookmarks stored using XBEL format.

{{< files text="show files" >}}* /usr/include/KF5/KBookmarks/KBookmark
* /usr/include/KF5/KBookmarks/kbookmark.h
* /usr/include/KF5/KBookmarks/KBookmarkAction
* /usr/include/KF5/KBookmarks/kbookmarkaction.h
* /usr/include/KF5/KBookmarks/KBookmarkActionInterface
* /usr/include/KF5/KBookmarks/kbookmarkactioninterface.h
* /usr/include/KF5/KBookmarks/KBookmarkActionMenu
* /usr/include/KF5/KBookmarks/kbookmarkactionmenu.h
* /usr/include/KF5/KBookmarks/KBookmarkContextMenu
* /usr/include/KF5/KBookmarks/kbookmarkcontextmenu.h
* /usr/include/KF5/KBookmarks/KBookmarkDialog
* /usr/include/KF5/KBookmarks/kbookmarkdialog.h
* /usr/include/KF5/KBookmarks/KBookmarkDomBuilder
* /usr/include/KF5/KBookmarks/kbookmarkdombuilder.h
* /usr/include/KF5/KBookmarks/kbookmarkexporter.h
* /usr/include/KF5/KBookmarks/kbookmarkimporter.h
* /usr/include/KF5/KBookmarks/kbookmarkimporter_ie.h
* /usr/include/KF5/KBookmarks/kbookmarkimporter_ns.h
* /usr/include/KF5/KBookmarks/kbookmarkimporter_opera.h
* /usr/include/KF5/KBookmarks/KBookmarkManager
* /usr/include/KF5/KBookmarks/kbookmarkmanager.h
* /usr/include/KF5/KBookmarks/KBookmarkMenu
* /usr/include/KF5/KBookmarks/kbookmarkmenu.h
* /usr/include/KF5/KBookmarks/KBookmarkOwner
* /usr/include/KF5/KBookmarks/kbookmarkowner.h
* /usr/include/KF5/KBookmarks/kbookmarks_export.h
* /usr/include/KF5/KBookmarks/kbookmarks_version.h
* /usr/include/KF5/KBookmarks/KonqBookmarkMenu
* /usr/include/KF5/KBookmarks/konqbookmarkmenu.h
* /usr/lib/cmake/KF5Bookmarks/KF5BookmarksConfig.cmake
* /usr/lib/cmake/KF5Bookmarks/KF5BookmarksConfigVersion.cmake
* /usr/lib/cmake/KF5Bookmarks/KF5BookmarksTargets-release.cmake
* /usr/lib/cmake/KF5Bookmarks/KF5BookmarksTargets.cmake
* /usr/lib/libKF5Bookmarks.so
* /usr/lib/libKF5Bookmarks.so.5
* /usr/lib/libKF5Bookmarks.so.5.115.0
* /usr/share/doc/kbookmarks-5.115.0/README.md
* /usr/share/locale/af/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/ar/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/az/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/be/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/be@latin/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/bg/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/bn/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/br/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/bs/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/ca/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/ca@valencia/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/cs/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/csb/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/cy/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/da/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/de/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/el/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/en_GB/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/eo/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/es/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/et/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/eu/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/fa/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/fi/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/fr/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/fy/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/ga/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/gd/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/gl/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/gu/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/he/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/hi/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/hr/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/hsb/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/hu/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/ia/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/id/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/is/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/it/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/ja/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/ka/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/kk/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/km/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/ko/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/ku/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/lt/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/lv/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/mai/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/mk/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/ml/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/mr/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/ms/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/nb/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/nds/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/ne/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/nl/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/nn/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/oc/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/pa/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/pl/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/pt/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/pt_BR/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/ro/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/ru/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/se/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/sk/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/sl/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/sq/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/sr/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/sr@ijekavian/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/sr@latin/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/sv/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/ta/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/tg/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/th/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/tr/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/ug/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/uk/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/uz/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/uz@cyrillic/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/vi/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/wa/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/xh/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/zh_CN/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/locale/zh_TW/LC_MESSAGES/kbookmarks5_qt.qm
* /usr/share/qlogging-categories5/kbookmarks.categories
* /usr/share/qlogging-categories5/kbookmarks.renamecategories
* /usr/share/qt5/mkspecs/modules/qt_KBookmarks.pri
{{< /files >}}