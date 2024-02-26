+++
draft = false
title = "khtml 5.115.0-1"
version = "5.115.0-1"
description = "HTML rendering engine."
date = "2024-02-19T11:20:36"
aliases = "/packages/218314"
categories = ['kf5']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "2303888"
usize = "10602552"
sha1sum = "79c568cdf45c0315324a0c1e16c45be5d01c73d8"
depends = "['kjs>=5.115.0', 'kparts>=5.115.0', 'libgif>=5.1.4-2']"
reverse_depends = "['kalzium', 'khelpcenter5', 'kile', 'kimagemapeditor', 'kio-extras', 'kiten', 'konqueror', 'kopete', 'okular', 'step', 'systemsettings5']"
+++
HTML rendering engine.

{{< files text="show files" >}}* /etc/xdg/khtmlrc
* /usr/include/KF5/KHtml/dom/css_rule.h
* /usr/include/KF5/KHtml/dom/css_stylesheet.h
* /usr/include/KF5/KHtml/dom/css_value.h
* /usr/include/KF5/KHtml/dom/dom2_events.h
* /usr/include/KF5/KHtml/dom/dom2_range.h
* /usr/include/KF5/KHtml/dom/dom2_traversal.h
* /usr/include/KF5/KHtml/dom/dom2_views.h
* /usr/include/KF5/KHtml/dom/dom_core.h
* /usr/include/KF5/KHtml/dom/dom_doc.h
* /usr/include/KF5/KHtml/dom/dom_element.h
* /usr/include/KF5/KHtml/dom/dom_exception.h
* /usr/include/KF5/KHtml/dom/dom_html.h
* /usr/include/KF5/KHtml/dom/dom_misc.h
* /usr/include/KF5/KHtml/dom/dom_node.h
* /usr/include/KF5/KHtml/dom/dom_string.h
* /usr/include/KF5/KHtml/dom/dom_text.h
* /usr/include/KF5/KHtml/dom/dom_xml.h
* /usr/include/KF5/KHtml/dom/html_base.h
* /usr/include/KF5/KHtml/dom/html_block.h
* /usr/include/KF5/KHtml/dom/html_document.h
* /usr/include/KF5/KHtml/dom/html_element.h
* /usr/include/KF5/KHtml/dom/html_form.h
* /usr/include/KF5/KHtml/dom/html_head.h
* /usr/include/KF5/KHtml/dom/html_image.h
* /usr/include/KF5/KHtml/dom/html_inline.h
* /usr/include/KF5/KHtml/dom/html_list.h
* /usr/include/KF5/KHtml/dom/html_misc.h
* /usr/include/KF5/KHtml/dom/html_object.h
* /usr/include/KF5/KHtml/dom/html_table.h
* /usr/include/KF5/KHtml/kencodingdetector.h
* /usr/include/KF5/KHtml/khtmldefaults.h
* /usr/include/KF5/KHtml/KHTMLPart
* /usr/include/KF5/KHtml/khtmlpart.h
* /usr/include/KF5/KHtml/KHTMLSettings
* /usr/include/KF5/KHtml/khtmlsettings.h
* /usr/include/KF5/KHtml/KHTMLView
* /usr/include/KF5/KHtml/khtmlview.h
* /usr/include/KF5/KHtml/khtml_debug.h
* /usr/include/KF5/KHtml/khtml_events.h
* /usr/include/KF5/KHtml/khtml_export.h
* /usr/include/KF5/KHtml/khtml_part.h
* /usr/include/KF5/KHtml/khtml_settings.h
* /usr/include/KF5/KHtml/khtml_version.h
* /usr/lib/cmake/KF5KHtml/KF5KHtmlConfig.cmake
* /usr/lib/cmake/KF5KHtml/KF5KHtmlConfigVersion.cmake
* /usr/lib/cmake/KF5KHtml/KF5KHtmlTargets-release.cmake
* /usr/lib/cmake/KF5KHtml/KF5KHtmlTargets.cmake
* /usr/lib/libKF5KHtml.so
* /usr/lib/libKF5KHtml.so.5
* /usr/lib/libKF5KHtml.so.5.115.0
* /usr/lib/qt5/plugins/kf5/parts/khtmladaptorpart.so
* /usr/lib/qt5/plugins/kf5/parts/khtmlimagepart.so
* /usr/lib/qt5/plugins/kf5/parts/khtmlpart.so
* /usr/lib/qt5/plugins/kf5/parts/kmultipart.so
* /usr/share/doc/khtml-5.115.0/COPYING.GPL3
* /usr/share/doc/khtml-5.115.0/COPYING.LGPL-2
* /usr/share/doc/khtml-5.115.0/COPYING.LIB
* /usr/share/doc/khtml-5.115.0/README.md
* /usr/share/kf5/khtml/css/html4.css
* /usr/share/kf5/khtml/css/presentational.css
* /usr/share/kf5/khtml/css/quirks.css
* /usr/share/kf5/khtml/error.html
* /usr/share/kservices5/khtml.desktop
* /usr/share/kservices5/khtmladaptorpart.desktop
* /usr/share/kservices5/khtmlimage.desktop
* /usr/share/kservices5/kmultipart.desktop
* /usr/share/locale/af/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ar/LC_MESSAGES/khtml5.mo
* /usr/share/locale/as/LC_MESSAGES/khtml5.mo
* /usr/share/locale/az/LC_MESSAGES/khtml5.mo
* /usr/share/locale/be/LC_MESSAGES/khtml5.mo
* /usr/share/locale/be@latin/LC_MESSAGES/khtml5.mo
* /usr/share/locale/bg/LC_MESSAGES/khtml5.mo
* /usr/share/locale/bn/LC_MESSAGES/khtml5.mo
* /usr/share/locale/bn_IN/LC_MESSAGES/khtml5.mo
* /usr/share/locale/br/LC_MESSAGES/khtml5.mo
* /usr/share/locale/bs/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ca/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/khtml5.mo
* /usr/share/locale/crh/LC_MESSAGES/khtml5.mo
* /usr/share/locale/cs/LC_MESSAGES/khtml5.mo
* /usr/share/locale/csb/LC_MESSAGES/khtml5.mo
* /usr/share/locale/cy/LC_MESSAGES/khtml5.mo
* /usr/share/locale/da/LC_MESSAGES/khtml5.mo
* /usr/share/locale/de/LC_MESSAGES/khtml5.mo
* /usr/share/locale/el/LC_MESSAGES/khtml5.mo
* /usr/share/locale/en_GB/LC_MESSAGES/khtml5.mo
* /usr/share/locale/eo/LC_MESSAGES/khtml5.mo
* /usr/share/locale/es/LC_MESSAGES/khtml5.mo
* /usr/share/locale/et/LC_MESSAGES/khtml5.mo
* /usr/share/locale/eu/LC_MESSAGES/khtml5.mo
* /usr/share/locale/fa/LC_MESSAGES/khtml5.mo
* /usr/share/locale/fi/LC_MESSAGES/khtml5.mo
* /usr/share/locale/fr/LC_MESSAGES/khtml5.mo
* /usr/share/locale/fy/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ga/LC_MESSAGES/khtml5.mo
* /usr/share/locale/gd/LC_MESSAGES/khtml5.mo
* /usr/share/locale/gl/LC_MESSAGES/khtml5.mo
* /usr/share/locale/gu/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ha/LC_MESSAGES/khtml5.mo
* /usr/share/locale/he/LC_MESSAGES/khtml5.mo
* /usr/share/locale/hi/LC_MESSAGES/khtml5.mo
* /usr/share/locale/hne/LC_MESSAGES/khtml5.mo
* /usr/share/locale/hr/LC_MESSAGES/khtml5.mo
* /usr/share/locale/hsb/LC_MESSAGES/khtml5.mo
* /usr/share/locale/hu/LC_MESSAGES/khtml5.mo
* /usr/share/locale/hy/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ia/LC_MESSAGES/khtml5.mo
* /usr/share/locale/id/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ie/LC_MESSAGES/khtml5.mo
* /usr/share/locale/is/LC_MESSAGES/khtml5.mo
* /usr/share/locale/it/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ja/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ka/LC_MESSAGES/khtml5.mo
* /usr/share/locale/kk/LC_MESSAGES/khtml5.mo
* /usr/share/locale/km/LC_MESSAGES/khtml5.mo
* /usr/share/locale/kn/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ko/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ku/LC_MESSAGES/khtml5.mo
* /usr/share/locale/lb/LC_MESSAGES/khtml5.mo
* /usr/share/locale/lt/LC_MESSAGES/khtml5.mo
* /usr/share/locale/lv/LC_MESSAGES/khtml5.mo
* /usr/share/locale/mai/LC_MESSAGES/khtml5.mo
* /usr/share/locale/mk/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ml/LC_MESSAGES/khtml5.mo
* /usr/share/locale/mr/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ms/LC_MESSAGES/khtml5.mo
* /usr/share/locale/nb/LC_MESSAGES/khtml5.mo
* /usr/share/locale/nds/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ne/LC_MESSAGES/khtml5.mo
* /usr/share/locale/nl/LC_MESSAGES/khtml5.mo
* /usr/share/locale/nn/LC_MESSAGES/khtml5.mo
* /usr/share/locale/oc/LC_MESSAGES/khtml5.mo
* /usr/share/locale/or/LC_MESSAGES/khtml5.mo
* /usr/share/locale/pa/LC_MESSAGES/khtml5.mo
* /usr/share/locale/pl/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ps/LC_MESSAGES/khtml5.mo
* /usr/share/locale/pt/LC_MESSAGES/khtml5.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ro/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ru/LC_MESSAGES/khtml5.mo
* /usr/share/locale/se/LC_MESSAGES/khtml5.mo
* /usr/share/locale/si/LC_MESSAGES/khtml5.mo
* /usr/share/locale/sk/LC_MESSAGES/khtml5.mo
* /usr/share/locale/sl/LC_MESSAGES/khtml5.mo
* /usr/share/locale/sq/LC_MESSAGES/khtml5.mo
* /usr/share/locale/sr/LC_MESSAGES/khtml5.mo
* /usr/share/locale/sr@ijekavian/LC_MESSAGES/khtml5.mo
* /usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/khtml5.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/khtml5.mo
* /usr/share/locale/sv/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ta/LC_MESSAGES/khtml5.mo
* /usr/share/locale/te/LC_MESSAGES/khtml5.mo
* /usr/share/locale/tg/LC_MESSAGES/khtml5.mo
* /usr/share/locale/th/LC_MESSAGES/khtml5.mo
* /usr/share/locale/tr/LC_MESSAGES/khtml5.mo
* /usr/share/locale/tt/LC_MESSAGES/khtml5.mo
* /usr/share/locale/ug/LC_MESSAGES/khtml5.mo
* /usr/share/locale/uk/LC_MESSAGES/khtml5.mo
* /usr/share/locale/uz/LC_MESSAGES/khtml5.mo
* /usr/share/locale/uz@cyrillic/LC_MESSAGES/khtml5.mo
* /usr/share/locale/vi/LC_MESSAGES/khtml5.mo
* /usr/share/locale/wa/LC_MESSAGES/khtml5.mo
* /usr/share/locale/xh/LC_MESSAGES/khtml5.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/khtml5.mo
* /usr/share/locale/zh_HK/LC_MESSAGES/khtml5.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/khtml5.mo
* /usr/share/qlogging-categories5/khtml.categories
* /usr/share/qlogging-categories5/khtml.renamecategories
* /usr/share/qt5/mkspecs/modules/qt_KHtml.pri
{{< /files >}}