+++
draft = false
title = "kosmindoormap 23.08.5-1"
version = "23.08.5-1"
description = "OSM multi-floor indoor map renderer"
date = "2024-02-20T14:24:09"
aliases = "/packages/220317"
categories = ['kde5-extra']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "409604"
usize = "1735550"
sha1sum = "fb673552bf4502748d2685197f5ac06fcebf2e29"
depends = "['ki18n>=5.115.0', 'kpublictransport=>23.08.5']"
reverse_depends = "['itinerary']"
+++
OSM multi-floor indoor map renderer{{< files text="show files" >}}* /usr/include/KOSM/Datatypes
* /usr/include/kosm/datatypes.h
* /usr/include/KOSM/Element
* /usr/include/kosm/element.h
* /usr/include/kosm/internal.h
* /usr/include/kosm/kosm_export.h
* /usr/include/kosm/stringpool.h
* /usr/include/KOSMIndoorMap/EquipmentModel
* /usr/include/kosmindoormap/equipmentmodel.h
* /usr/include/KOSMIndoorMap/FloorLevelModel
* /usr/include/kosmindoormap/floorlevelmodel.h
* /usr/include/KOSMIndoorMap/GateModel
* /usr/include/kosmindoormap/gatemodel.h
* /usr/include/KOSMIndoorMap/HitDetector
* /usr/include/kosmindoormap/hitdetector.h
* /usr/include/kosmindoormap/kosmindoormap_export.h
* /usr/include/KOSMIndoorMap/MapCSSParser
* /usr/include/kosmindoormap/mapcssparser.h
* /usr/include/KOSMIndoorMap/MapCSSStyle
* /usr/include/kosmindoormap/mapcssstyle.h
* /usr/include/KOSMIndoorMap/MapData
* /usr/include/kosmindoormap/mapdata.h
* /usr/include/KOSMIndoorMap/MapLoader
* /usr/include/kosmindoormap/maploader.h
* /usr/include/KOSMIndoorMap/OverlaySource
* /usr/include/kosmindoormap/overlaysource.h
* /usr/include/KOSMIndoorMap/PainterRenderer
* /usr/include/kosmindoormap/painterrenderer.h
* /usr/include/KOSMIndoorMap/Platform
* /usr/include/kosmindoormap/platform.h
* /usr/include/KOSMIndoorMap/PlatformModel
* /usr/include/kosmindoormap/platformmodel.h
* /usr/include/KOSMIndoorMap/SceneController
* /usr/include/kosmindoormap/scenecontroller.h
* /usr/include/KOSMIndoorMap/SceneGraph
* /usr/include/kosmindoormap/scenegraph.h
* /usr/include/KOSMIndoorMap/SceneGraphItem
* /usr/include/kosmindoormap/scenegraphitem.h
* /usr/include/KOSMIndoorMap/View
* /usr/include/kosmindoormap/view.h
* /usr/include/kosmindoormap_version.h
* /usr/lib/cmake/KOSMIndoorMap/KOSMIndoorMapConfig.cmake
* /usr/lib/cmake/KOSMIndoorMap/KOSMIndoorMapConfigVersion.cmake
* /usr/lib/cmake/KOSMIndoorMap/KOSMIndoorMapTargets-release.cmake
* /usr/lib/cmake/KOSMIndoorMap/KOSMIndoorMapTargets.cmake
* /usr/lib/libKOSM.so
* /usr/lib/libKOSM.so.1
* /usr/lib/libKOSM.so.23.08.5
* /usr/lib/libKOSMIndoorMap.so
* /usr/lib/libKOSMIndoorMap.so.1
* /usr/lib/libKOSMIndoorMap.so.23.08.5
* /usr/share/doc/kosmindoormap-23.08.5/README.md
* /usr/share/doc/kosmindoormap-23.08.5/README.md.license
* /usr/share/locale/ca/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/cs/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/de/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/en_GB/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/es/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/eu/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/fi/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/fr/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/it/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/ja/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/ka/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/ko/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/lt/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/nl/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/pl/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/pt/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/ru/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/sk/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/sl/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/sv/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/tr/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/uk/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/kosmindoormap.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/kosmindoormap.mo
* /usr/share/qlogging-categories5/org_kde_kosmindoormap.categories
* /usr/share/qt5/qml/org/kde/kosmindoormap/IndoorMap.qml
* /usr/share/qt5/qml/org/kde/kosmindoormap/IndoorMapAttributionLabel.qml
* /usr/share/qt5/qml/org/kde/kosmindoormap/IndoorMapScale.qml
* /usr/share/qt5/qml/org/kde/kosmindoormap/kpublictransport/libkosmindoormap_kpublictransport_integration_plugin.so
* /usr/share/qt5/qml/org/kde/kosmindoormap/kpublictransport/qmldir
* /usr/share/qt5/qml/org/kde/kosmindoormap/libkosmindoormapquickplugin.so
* /usr/share/qt5/qml/org/kde/kosmindoormap/qmldir
{{< /files >}}