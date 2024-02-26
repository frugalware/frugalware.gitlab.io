+++
draft = false
title = "tiled 1.10.2-2"
version = "1.10.2-2"
description = "Tiled is a general purpose tile map editor."
date = "2023-10-18T17:41:50"
aliases = "/packages/217393"
categories = ['xapps-extra']
upstreamurl = "https://github.com/bjorn/tiled"
arch = "x86_64"
size = "3443532"
usize = "17132822"
sha1sum = "7228509cb2ce731e280f2f292709647cb65f164b"
depends = "['python3>=3.12', 'qt5-declarative>=5.15.10', 'qt5-quickcontrols2>=5.15.10', 'qt5-svg>=5.15.10', 'zlib>=1.2.12']"
+++
Tiled is a general purpose tile map editor."

{{< files text="show files" >}}* /usr/bin/terraingenerator
* /usr/bin/tiled
* /usr/bin/tmxrasterizer
* /usr/bin/tmxviewer
* /usr/include/tiled/compression.h
* /usr/include/tiled/containerhelpers.h
* /usr/include/tiled/fileformat.h
* /usr/include/tiled/filesystemwatcher.h
* /usr/include/tiled/gidmapper.h
* /usr/include/tiled/grid.h
* /usr/include/tiled/grouplayer.h
* /usr/include/tiled/hex.h
* /usr/include/tiled/hexagonalrenderer.h
* /usr/include/tiled/imagecache.h
* /usr/include/tiled/imagelayer.h
* /usr/include/tiled/imagereference.h
* /usr/include/tiled/isometricrenderer.h
* /usr/include/tiled/layer.h
* /usr/include/tiled/logginginterface.h
* /usr/include/tiled/map.h
* /usr/include/tiled/mapformat.h
* /usr/include/tiled/mapobject.h
* /usr/include/tiled/mapreader.h
* /usr/include/tiled/maprenderer.h
* /usr/include/tiled/maptovariantconverter.h
* /usr/include/tiled/mapwriter.h
* /usr/include/tiled/minimaprenderer.h
* /usr/include/tiled/moc_fileformat.cpp
* /usr/include/tiled/moc_filesystemwatcher.cpp
* /usr/include/tiled/moc_logginginterface.cpp
* /usr/include/tiled/moc_mapformat.cpp
* /usr/include/tiled/moc_objecttemplateformat.cpp
* /usr/include/tiled/moc_plugin.cpp
* /usr/include/tiled/moc_pluginmanager.cpp
* /usr/include/tiled/moc_properties.cpp
* /usr/include/tiled/moc_templatemanager.cpp
* /usr/include/tiled/moc_tileanimationdriver.cpp
* /usr/include/tiled/moc_tilelayer.cpp
* /usr/include/tiled/moc_tilesetformat.cpp
* /usr/include/tiled/moc_tilesetmanager.cpp
* /usr/include/tiled/moc_worldmanager.cpp
* /usr/include/tiled/object.h
* /usr/include/tiled/objectgroup.h
* /usr/include/tiled/objecttemplate.h
* /usr/include/tiled/objecttemplateformat.h
* /usr/include/tiled/objecttypes.h
* /usr/include/tiled/orthogonalrenderer.h
* /usr/include/tiled/plugin.h
* /usr/include/tiled/pluginmanager.h
* /usr/include/tiled/properties.h
* /usr/include/tiled/propertytype.h
* /usr/include/tiled/savefile.h
* /usr/include/tiled/staggeredrenderer.h
* /usr/include/tiled/templatemanager.h
* /usr/include/tiled/tile.h
* /usr/include/tiled/tileanimationdriver.h
* /usr/include/tiled/tiled.h
* /usr/include/tiled/tiled_global.h
* /usr/include/tiled/tilelayer.h
* /usr/include/tiled/tileset.h
* /usr/include/tiled/tilesetformat.h
* /usr/include/tiled/tilesetmanager.h
* /usr/include/tiled/varianttomapconverter.h
* /usr/include/tiled/wangset.h
* /usr/include/tiled/worldmanager.h
* /usr/lib/libtiled.so
* /usr/lib/libtilededitor.so
* /usr/lib/tiled/plugins/libcsv.so
* /usr/lib/tiled/plugins/libdefold.so
* /usr/lib/tiled/plugins/libdefoldcollection.so
* /usr/lib/tiled/plugins/libdroidcraft.so
* /usr/lib/tiled/plugins/libflare.so
* /usr/lib/tiled/plugins/libgmx.so
* /usr/lib/tiled/plugins/libjson.so
* /usr/lib/tiled/plugins/libjson1.so
* /usr/lib/tiled/plugins/liblua.so
* /usr/lib/tiled/plugins/libpython.so
* /usr/lib/tiled/plugins/libreplicaisland.so
* /usr/lib/tiled/plugins/librpmap.so
* /usr/lib/tiled/plugins/libtbin.so
* /usr/lib/tiled/plugins/libtengine.so
* /usr/lib/tiled/plugins/libtscn.so
* /usr/lib/tiled/plugins/libyy.so
* /usr/share/applications/org.mapeditor.Tiled.desktop
* /usr/share/doc/tiled-1.10.2/AUTHORS
* /usr/share/doc/tiled-1.10.2/COPYING
* /usr/share/doc/tiled-1.10.2/README.md
* /usr/share/icons/hicolor/16x16/apps/tiled.png
* /usr/share/icons/hicolor/16x16/mimetypes/application-x-tiled.png
* /usr/share/icons/hicolor/32x32/apps/tiled.png
* /usr/share/icons/hicolor/32x32/mimetypes/application-x-tiled.png
* /usr/share/icons/hicolor/scalable/apps/tiled.svg
* /usr/share/icons/hicolor/scalable/mimetypes/application-x-tiled.svg
* /usr/share/man/man1/tiled.1.gz
* /usr/share/man/man1/tmxrasterizer.1.gz
* /usr/share/man/man1/tmxviewer.1.gz
* /usr/share/metainfo/org.mapeditor.Tiled.appdata.xml
* /usr/share/mime/packages/org.mapeditor.Tiled.xml
* /usr/share/thumbnailers/tiled.thumbnailer
* /usr/share/tiled/translations/tiled_ar_DZ.qm
* /usr/share/tiled/translations/tiled_bg.qm
* /usr/share/tiled/translations/tiled_cs.qm
* /usr/share/tiled/translations/tiled_de.qm
* /usr/share/tiled/translations/tiled_en.qm
* /usr/share/tiled/translations/tiled_es.qm
* /usr/share/tiled/translations/tiled_fi.qm
* /usr/share/tiled/translations/tiled_fr.qm
* /usr/share/tiled/translations/tiled_he.qm
* /usr/share/tiled/translations/tiled_hu.qm
* /usr/share/tiled/translations/tiled_it.qm
* /usr/share/tiled/translations/tiled_ja.qm
* /usr/share/tiled/translations/tiled_ko.qm
* /usr/share/tiled/translations/tiled_nb.qm
* /usr/share/tiled/translations/tiled_nl.qm
* /usr/share/tiled/translations/tiled_pl.qm
* /usr/share/tiled/translations/tiled_pt.qm
* /usr/share/tiled/translations/tiled_pt_PT.qm
* /usr/share/tiled/translations/tiled_ru.qm
* /usr/share/tiled/translations/tiled_sv.qm
* /usr/share/tiled/translations/tiled_th.qm
* /usr/share/tiled/translations/tiled_tr.qm
* /usr/share/tiled/translations/tiled_uk.qm
* /usr/share/tiled/translations/tiled_zh_CN.qm
* /usr/share/tiled/translations/tiled_zh_TW.qm
{{< /files >}}