+++
draft = false
title = "gtk-doc 1.32-4"
version = "1.32-4"
date = "2022-12-12T08:41:31"
categories = ['devel-extra']
upstreamurl = "http://www.gnome.org/"
arch = "x86_64"
size = "340976"
usize = "2768873"
sha1sum = "06b15da3d57c5635ebb8b8e28bd331298b44a512"
depends = "['openjade', 'docbook-xsl', 'source-highlight', 'perl>=5.28.2', 'python3-six']"
files = "['usr/', 'usr/bin/', 'usr/bin/gtkdoc-check', 'usr/bin/gtkdoc-depscan', 'usr/bin/gtkdoc-fixxref', 'usr/bin/gtkdoc-mkdb', 'usr/bin/gtkdoc-mkhtml', 'usr/bin/gtkdoc-mkhtml2', 'usr/bin/gtkdoc-mkman', 'usr/bin/gtkdoc-mkpdf', 'usr/bin/gtkdoc-rebase', 'usr/bin/gtkdoc-scan', 'usr/bin/gtkdoc-scangobj', 'usr/bin/gtkdocize', 'usr/lib/', 'usr/lib/pkgconfig/', 'usr/lib/pkgconfig/gtk-doc.pc', 'usr/share/', 'usr/share/aclocal/', 'usr/share/aclocal/gtk-doc.m4', 'usr/share/cmake/', 'usr/share/cmake/GtkDoc/', 'usr/share/cmake/GtkDoc/GtkDocConfig.cmake', 'usr/share/cmake/GtkDoc/GtkDocConfigVersion.cmake', 'usr/share/cmake/GtkDoc/GtkDocScanGObjWrapper.cmake', 'usr/share/doc/', 'usr/share/doc/gtk-doc-1.32/', 'usr/share/doc/gtk-doc-1.32/AUTHORS', 'usr/share/doc/gtk-doc-1.32/COPYING', 'usr/share/doc/gtk-doc-1.32/COPYING-DOCS', 'usr/share/doc/gtk-doc-1.32/ChangeLog', 'usr/share/doc/gtk-doc-1.32/INSTALL', 'usr/share/doc/gtk-doc-1.32/NEWS', 'usr/share/doc/gtk-doc-1.32/README', 'usr/share/doc/gtk-doc-1.32/TODO', 'usr/share/gtk-doc/', 'usr/share/gtk-doc/data/', 'usr/share/gtk-doc/data/devhelp2.xsd', 'usr/share/gtk-doc/data/devhelp2.xsl', 'usr/share/gtk-doc/data/gtk-doc.flat.make', 'usr/share/gtk-doc/data/gtk-doc.make', 'usr/share/gtk-doc/data/gtk-doc.no-xslt-flat.make', 'usr/share/gtk-doc/data/gtk-doc.no-xslt.make', 'usr/share/gtk-doc/data/gtk-doc.xsl', 'usr/share/gtk-doc/data/home.png', 'usr/share/gtk-doc/data/left-insensitive.png', 'usr/share/gtk-doc/data/left.png', 'usr/share/gtk-doc/data/right-insensitive.png', 'usr/share/gtk-doc/data/right.png', 'usr/share/gtk-doc/data/style.css', 'usr/share/gtk-doc/data/up-insensitive.png', 'usr/share/gtk-doc/data/up.png', 'usr/share/gtk-doc/data/version-greater-or-equal.xsl', 'usr/share/gtk-doc/python/', 'usr/share/gtk-doc/python/gtkdoc/', 'usr/share/gtk-doc/python/gtkdoc/__init__.py', 'usr/share/gtk-doc/python/gtkdoc/check.py', 'usr/share/gtk-doc/python/gtkdoc/common.py', 'usr/share/gtk-doc/python/gtkdoc/config.py', 'usr/share/gtk-doc/python/gtkdoc/fixxref.py', 'usr/share/gtk-doc/python/gtkdoc/highlight.py', 'usr/share/gtk-doc/python/gtkdoc/md_to_db.py', 'usr/share/gtk-doc/python/gtkdoc/mkdb.py', 'usr/share/gtk-doc/python/gtkdoc/mkhtml.py', 'usr/share/gtk-doc/python/gtkdoc/mkhtml2.py', 'usr/share/gtk-doc/python/gtkdoc/mkman.py', 'usr/share/gtk-doc/python/gtkdoc/mkpdf.py', 'usr/share/gtk-doc/python/gtkdoc/rebase.py', 'usr/share/gtk-doc/python/gtkdoc/scan.py', 'usr/share/gtk-doc/python/gtkdoc/scangobj.py', 'usr/share/help/', 'usr/share/help/C/', 'usr/share/help/C/gtk-doc-manual/', 'usr/share/help/C/gtk-doc-manual/fdl-appendix.xml', 'usr/share/help/C/gtk-doc-manual/index.docbook', 'usr/share/help/bn_IN/', 'usr/share/help/bn_IN/gtk-doc-manual/', 'usr/share/help/bn_IN/gtk-doc-manual/fdl-appendix.xml', 'usr/share/help/bn_IN/gtk-doc-manual/index.docbook', 'usr/share/help/cs/', 'usr/share/help/cs/gtk-doc-manual/', 'usr/share/help/cs/gtk-doc-manual/fdl-appendix.xml', 'usr/share/help/cs/gtk-doc-manual/index.docbook', 'usr/share/help/de/', 'usr/share/help/de/gtk-doc-manual/', 'usr/share/help/de/gtk-doc-manual/fdl-appendix.xml', 'usr/share/help/de/gtk-doc-manual/index.docbook', 'usr/share/help/el/', 'usr/share/help/el/gtk-doc-manual/', 'usr/share/help/el/gtk-doc-manual/fdl-appendix.xml', 'usr/share/help/el/gtk-doc-manual/index.docbook', 'usr/share/help/en_GB/', 'usr/share/help/en_GB/gtk-doc-manual/', 'usr/share/help/en_GB/gtk-doc-manual/fdl-appendix.xml', 'usr/share/help/en_GB/gtk-doc-manual/index.docbook', 'usr/share/help/es/', 'usr/share/help/es/gtk-doc-manual/', 'usr/share/help/es/gtk-doc-manual/fdl-appendix.xml', 'usr/share/help/es/gtk-doc-manual/index.docbook', 'usr/share/help/fr/', 'usr/share/help/fr/gtk-doc-manual/', 'usr/share/help/fr/gtk-doc-manual/fdl-appendix.xml', 'usr/share/help/fr/gtk-doc-manual/index.docbook', 'usr/share/help/gl/', 'usr/share/help/gl/gtk-doc-manual/', 'usr/share/help/gl/gtk-doc-manual/fdl-appendix.xml', 'usr/share/help/gl/gtk-doc-manual/index.docbook', 'usr/share/help/gu/', 'usr/share/help/gu/gtk-doc-manual/', 'usr/share/help/gu/gtk-doc-manual/fdl-appendix.xml', 'usr/share/help/gu/gtk-doc-manual/index.docbook', 'usr/share/help/pt_BR/', 'usr/share/help/pt_BR/gtk-doc-manual/', 'usr/share/help/pt_BR/gtk-doc-manual/fdl-appendix.xml', 'usr/share/help/pt_BR/gtk-doc-manual/index.docbook', 'usr/share/help/sl/', 'usr/share/help/sl/gtk-doc-manual/', 'usr/share/help/sl/gtk-doc-manual/fdl-appendix.xml', 'usr/share/help/sl/gtk-doc-manual/index.docbook', 'usr/share/help/sv/', 'usr/share/help/sv/gtk-doc-manual/', 'usr/share/help/sv/gtk-doc-manual/fdl-appendix.xml', 'usr/share/help/sv/gtk-doc-manual/index.docbook', 'usr/share/help/ta/', 'usr/share/help/ta/gtk-doc-manual/', 'usr/share/help/ta/gtk-doc-manual/fdl-appendix.xml', 'usr/share/help/ta/gtk-doc-manual/index.docbook', 'usr/share/help/te/', 'usr/share/help/te/gtk-doc-manual/', 'usr/share/help/te/gtk-doc-manual/fdl-appendix.xml', 'usr/share/help/te/gtk-doc-manual/index.docbook', 'usr/share/help/zh_CN/', 'usr/share/help/zh_CN/gtk-doc-manual/', 'usr/share/help/zh_CN/gtk-doc-manual/fdl-appendix.xml', 'usr/share/help/zh_CN/gtk-doc-manual/index.docbook']"
+++
Used to document the public API of libraries