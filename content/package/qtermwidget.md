+++
draft = false
title = "qtermwidget 1.3.0-2"
version = "1.3.0-2"
description = "A terminal emulator widget for Qt5"
date = "2023-10-20T15:03:58"
aliases = "/packages/217828"
categories = ['xapps-extra']
upstreamurl = "https://www.lxde.org"
arch = "x86_64"
size = "185916"
usize = "698879"
sha1sum = "7c7f8373bcea92a9a413bcba5b10062a4a0948e1"
depends = "['qt5-base>=5.15.10', 'utf8proc>=2.2.0']"
reverse_depends = "['qt-virt-manager', 'qterminal']"
+++
A terminal emulator widget for Qt5{{< files text="show files" >}}* /usr/include/qtermwidget5/Emulation.h
* /usr/include/qtermwidget5/Filter.h
* /usr/include/qtermwidget5/KeyboardTranslator.h
* /usr/include/qtermwidget5/qtermwidget.h
* /usr/include/qtermwidget5/qtermwidget_export.h
* /usr/include/qtermwidget5/qtermwidget_interface.h
* /usr/include/qtermwidget5/qtermwidget_version.h
* /usr/lib/cmake/qtermwidget5/qtermwidget5-config-version.cmake
* /usr/lib/cmake/qtermwidget5/qtermwidget5-config.cmake
* /usr/lib/cmake/qtermwidget5/qtermwidget5-targets-release.cmake
* /usr/lib/cmake/qtermwidget5/qtermwidget5-targets.cmake
* /usr/lib/libqtermwidget5.so
* /usr/lib/libqtermwidget5.so.1
* /usr/lib/libqtermwidget5.so.1.3.0
* /usr/lib/pkgconfig/qtermwidget5.pc
* /usr/share/doc/qtermwidget-1.3.0/AUTHORS
* /usr/share/doc/qtermwidget-1.3.0/CHANGELOG
* /usr/share/doc/qtermwidget-1.3.0/COPYING-CMAKE-SCRIPTS
* /usr/share/doc/qtermwidget-1.3.0/LICENSE
* /usr/share/doc/qtermwidget-1.3.0/README.md
* /usr/share/qtermwidget5/color-schemes/BlackOnLightYellow.colorscheme
* /usr/share/qtermwidget5/color-schemes/BlackOnRandomLight.colorscheme
* /usr/share/qtermwidget5/color-schemes/BlackOnWhite.colorscheme
* /usr/share/qtermwidget5/color-schemes/BreezeModified.colorscheme
* /usr/share/qtermwidget5/color-schemes/DarkPastels.colorscheme
* /usr/share/qtermwidget5/color-schemes/GreenOnBlack.colorscheme
* /usr/share/qtermwidget5/color-schemes/historic/BlackOnLightColor.schema
* /usr/share/qtermwidget5/color-schemes/historic/DarkPicture.schema
* /usr/share/qtermwidget5/color-schemes/historic/GreenOnBlack.schema
* /usr/share/qtermwidget5/color-schemes/historic/GreenTint.schema
* /usr/share/qtermwidget5/color-schemes/historic/GreenTint_MC.schema
* /usr/share/qtermwidget5/color-schemes/historic/LightPicture.schema
* /usr/share/qtermwidget5/color-schemes/historic/Linux.schema
* /usr/share/qtermwidget5/color-schemes/historic/syscolor.schema
* /usr/share/qtermwidget5/color-schemes/historic/Transparent.schema
* /usr/share/qtermwidget5/color-schemes/historic/Transparent_darkbg.schema
* /usr/share/qtermwidget5/color-schemes/historic/Transparent_lightbg.schema
* /usr/share/qtermwidget5/color-schemes/historic/Transparent_MC.schema
* /usr/share/qtermwidget5/color-schemes/historic/vim.schema
* /usr/share/qtermwidget5/color-schemes/historic/XTerm.schema
* /usr/share/qtermwidget5/color-schemes/Linux.colorscheme
* /usr/share/qtermwidget5/color-schemes/Solarized.colorscheme
* /usr/share/qtermwidget5/color-schemes/SolarizedLight.colorscheme
* /usr/share/qtermwidget5/color-schemes/Tango.colorscheme
* /usr/share/qtermwidget5/color-schemes/Ubuntu.colorscheme
* /usr/share/qtermwidget5/color-schemes/WhiteOnBlack.colorscheme
* /usr/share/qtermwidget5/kb-layouts/default.keytab
* /usr/share/qtermwidget5/kb-layouts/historic/vt100.keytab
* /usr/share/qtermwidget5/kb-layouts/historic/x11r5.keytab
* /usr/share/qtermwidget5/kb-layouts/linux.keytab
* /usr/share/qtermwidget5/kb-layouts/macbook.keytab
* /usr/share/qtermwidget5/kb-layouts/solaris.keytab
* /usr/share/qtermwidget5/kb-layouts/vt420pc.keytab
* /usr/share/qtermwidget5/translations/qtermwidget_ar.qm
* /usr/share/qtermwidget5/translations/qtermwidget_arn.qm
* /usr/share/qtermwidget5/translations/qtermwidget_ast.qm
* /usr/share/qtermwidget5/translations/qtermwidget_bg.qm
* /usr/share/qtermwidget5/translations/qtermwidget_ca.qm
* /usr/share/qtermwidget5/translations/qtermwidget_cs.qm
* /usr/share/qtermwidget5/translations/qtermwidget_cy.qm
* /usr/share/qtermwidget5/translations/qtermwidget_da.qm
* /usr/share/qtermwidget5/translations/qtermwidget_de.qm
* /usr/share/qtermwidget5/translations/qtermwidget_de_CH.qm
* /usr/share/qtermwidget5/translations/qtermwidget_el.qm
* /usr/share/qtermwidget5/translations/qtermwidget_es.qm
* /usr/share/qtermwidget5/translations/qtermwidget_et.qm
* /usr/share/qtermwidget5/translations/qtermwidget_fr.qm
* /usr/share/qtermwidget5/translations/qtermwidget_gl.qm
* /usr/share/qtermwidget5/translations/qtermwidget_he.qm
* /usr/share/qtermwidget5/translations/qtermwidget_hr.qm
* /usr/share/qtermwidget5/translations/qtermwidget_hu.qm
* /usr/share/qtermwidget5/translations/qtermwidget_it.qm
* /usr/share/qtermwidget5/translations/qtermwidget_ja.qm
* /usr/share/qtermwidget5/translations/qtermwidget_ko.qm
* /usr/share/qtermwidget5/translations/qtermwidget_lt.qm
* /usr/share/qtermwidget5/translations/qtermwidget_nb_NO.qm
* /usr/share/qtermwidget5/translations/qtermwidget_nl.qm
* /usr/share/qtermwidget5/translations/qtermwidget_oc.qm
* /usr/share/qtermwidget5/translations/qtermwidget_pl.qm
* /usr/share/qtermwidget5/translations/qtermwidget_pt.qm
* /usr/share/qtermwidget5/translations/qtermwidget_pt_BR.qm
* /usr/share/qtermwidget5/translations/qtermwidget_ru.qm
* /usr/share/qtermwidget5/translations/qtermwidget_si.qm
* /usr/share/qtermwidget5/translations/qtermwidget_sk.qm
* /usr/share/qtermwidget5/translations/qtermwidget_tr.qm
* /usr/share/qtermwidget5/translations/qtermwidget_uk.qm
* /usr/share/qtermwidget5/translations/qtermwidget_zh_CN.qm
* /usr/share/qtermwidget5/translations/qtermwidget_zh_TW.qm
{{< /files >}}