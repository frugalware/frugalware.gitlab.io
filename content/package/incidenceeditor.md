+++
draft = false
title = "incidenceeditor 23.08.5-1"
version = "23.08.5-1"
description = "This lib provides incidence editor"
date = "2024-02-20T09:47:58"
aliases = "/packages/218490"
categories = ['kde5']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "525940"
usize = "2772794"
sha1sum = "16d56fe6f60cd4d2ca96ea2565014209d835b497"
depends = "['akonadi>=23.08.5', 'eventviews>=23.08.5', 'ki18n>=5.115.0']"
reverse_depends = "['kdepim-addons', 'korganizer']"
+++
This lib provides incidence editor{{< files text="show files" >}}* /usr/include/KPim5/IncidenceEditor/IncidenceEditor/EditorItemManager
* /usr/include/KPim5/IncidenceEditor/incidenceeditor/editoritemmanager.h
* /usr/include/KPim5/IncidenceEditor/incidenceeditor/globalsettings_incidenceeditor.h
* /usr/include/KPim5/IncidenceEditor/IncidenceEditor/GroupwareUiDelegate
* /usr/include/KPim5/IncidenceEditor/incidenceeditor/groupwareuidelegate.h
* /usr/include/KPim5/IncidenceEditor/IncidenceEditor/IncidenceDefaults
* /usr/include/KPim5/IncidenceEditor/incidenceeditor/incidencedefaults.h
* /usr/include/KPim5/IncidenceEditor/IncidenceEditor/IncidenceDialog
* /usr/include/KPim5/IncidenceEditor/incidenceeditor/incidencedialog.h
* /usr/include/KPim5/IncidenceEditor/IncidenceEditor/IncidenceDialogFactory
* /usr/include/KPim5/IncidenceEditor/incidenceeditor/incidencedialogfactory.h
* /usr/include/KPim5/IncidenceEditor/IncidenceEditor/IncidenceEditor-Ng
* /usr/include/KPim5/IncidenceEditor/incidenceeditor/incidenceeditor-ng.h
* /usr/include/KPim5/IncidenceEditor/IncidenceEditor/IncidenceEditorSettings
* /usr/include/KPim5/IncidenceEditor/incidenceeditor/incidenceeditorsettings.h
* /usr/include/KPim5/IncidenceEditor/incidenceeditor/incidenceeditor_export.h
* /usr/include/KPim5/IncidenceEditor/IncidenceEditor/IndividualMailComponentFactory
* /usr/include/KPim5/IncidenceEditor/incidenceeditor/individualmailcomponentfactory.h
* /usr/include/KPim5/IncidenceEditor/incidenceeditor_version.h
* /usr/lib/cmake/KPim5IncidenceEditor/KPim5IncidenceEditorConfig.cmake
* /usr/lib/cmake/KPim5IncidenceEditor/KPim5IncidenceEditorConfigVersion.cmake
* /usr/lib/cmake/KPim5IncidenceEditor/KPim5IncidenceEditorTargets-release.cmake
* /usr/lib/cmake/KPim5IncidenceEditor/KPim5IncidenceEditorTargets.cmake
* /usr/lib/libKPim5IncidenceEditor.so
* /usr/lib/libKPim5IncidenceEditor.so.5
* /usr/lib/libKPim5IncidenceEditor.so.5.24.5
* /usr/share/locale/ar/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/bg/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/bs/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/ca/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/cs/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/da/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/de/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/el/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/en_GB/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/eo/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/es/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/et/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/eu/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/fi/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/fr/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/ga/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/gl/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/hu/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/ia/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/it/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/ja/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/ka/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/kk/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/ko/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/lt/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/mai/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/mr/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/nb/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/nds/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/nl/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/pa/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/pl/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/pt/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/ro/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/ru/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/sk/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/sl/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/sv/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/ta/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/tr/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/ug/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/uk/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/libincidenceeditors.mo
* /usr/share/qlogging-categories5/incidenceeditor.categories
* /usr/share/qlogging-categories5/incidenceeditor.renamecategories
* /usr/share/qt5/mkspecs/modules/qt_IncidenceEditor.pri
{{< /files >}}