+++
draft = false
title = "qscintilla2-qt5 2.11.2-6"
version = "2.11.2-6"
description = "QScintilla2 is a port to Qt of Neil Hodgson's Scintilla C++ editor class. (Qt5)"
date = "2023-10-26T13:40:19"
aliases = "/packages/217428"
categories = ['xlib-extra']
upstreamurl = "http://www.riverbankcomputing.co.uk/"
arch = "x86_64"
size = "1137820"
usize = "6374335"
sha1sum = "bc07cd0bbe10759f2e633d20e164111a404cfdc0"
depends = "['qt5-base>=5.15.10', 'qt5-tools>=5.15.10']"
reverse_depends = "['database-browser-sqlite', 'openscad']"
license = "2"
+++
QScintilla2 is a port to Qt of Neil Hodgson's Scintilla C++ editor class. (Qt5)

{{< files text="show files" >}}* /usr/include/qt5/Qsci/qsciabstractapis.h
* /usr/include/qt5/Qsci/qsciapis.h
* /usr/include/qt5/Qsci/qscicommand.h
* /usr/include/qt5/Qsci/qscicommandset.h
* /usr/include/qt5/Qsci/qscidocument.h
* /usr/include/qt5/Qsci/qsciglobal.h
* /usr/include/qt5/Qsci/qscilexer.h
* /usr/include/qt5/Qsci/qscilexeravs.h
* /usr/include/qt5/Qsci/qscilexerbash.h
* /usr/include/qt5/Qsci/qscilexerbatch.h
* /usr/include/qt5/Qsci/qscilexercmake.h
* /usr/include/qt5/Qsci/qscilexercoffeescript.h
* /usr/include/qt5/Qsci/qscilexercpp.h
* /usr/include/qt5/Qsci/qscilexercsharp.h
* /usr/include/qt5/Qsci/qscilexercss.h
* /usr/include/qt5/Qsci/qscilexercustom.h
* /usr/include/qt5/Qsci/qscilexerd.h
* /usr/include/qt5/Qsci/qscilexerdiff.h
* /usr/include/qt5/Qsci/qscilexeredifact.h
* /usr/include/qt5/Qsci/qscilexerfortran.h
* /usr/include/qt5/Qsci/qscilexerfortran77.h
* /usr/include/qt5/Qsci/qscilexerhtml.h
* /usr/include/qt5/Qsci/qscilexeridl.h
* /usr/include/qt5/Qsci/qscilexerjava.h
* /usr/include/qt5/Qsci/qscilexerjavascript.h
* /usr/include/qt5/Qsci/qscilexerjson.h
* /usr/include/qt5/Qsci/qscilexerlua.h
* /usr/include/qt5/Qsci/qscilexermakefile.h
* /usr/include/qt5/Qsci/qscilexermarkdown.h
* /usr/include/qt5/Qsci/qscilexermatlab.h
* /usr/include/qt5/Qsci/qscilexeroctave.h
* /usr/include/qt5/Qsci/qscilexerpascal.h
* /usr/include/qt5/Qsci/qscilexerperl.h
* /usr/include/qt5/Qsci/qscilexerpo.h
* /usr/include/qt5/Qsci/qscilexerpostscript.h
* /usr/include/qt5/Qsci/qscilexerpov.h
* /usr/include/qt5/Qsci/qscilexerproperties.h
* /usr/include/qt5/Qsci/qscilexerpython.h
* /usr/include/qt5/Qsci/qscilexerruby.h
* /usr/include/qt5/Qsci/qscilexerspice.h
* /usr/include/qt5/Qsci/qscilexersql.h
* /usr/include/qt5/Qsci/qscilexertcl.h
* /usr/include/qt5/Qsci/qscilexertex.h
* /usr/include/qt5/Qsci/qscilexerverilog.h
* /usr/include/qt5/Qsci/qscilexervhdl.h
* /usr/include/qt5/Qsci/qscilexerxml.h
* /usr/include/qt5/Qsci/qscilexeryaml.h
* /usr/include/qt5/Qsci/qscimacro.h
* /usr/include/qt5/Qsci/qsciprinter.h
* /usr/include/qt5/Qsci/qsciscintilla.h
* /usr/include/qt5/Qsci/qsciscintillabase.h
* /usr/include/qt5/Qsci/qscistyle.h
* /usr/include/qt5/Qsci/qscistyledtext.h
* /usr/lib/libqscintilla2_qt5.so
* /usr/lib/libqscintilla2_qt5.so.15
* /usr/lib/libqscintilla2_qt5.so.15.0
* /usr/lib/libqscintilla2_qt5.so.15.0.0
* /usr/lib/qt5/plugins/designer/libqscintillaplugin.so
* /usr/share/doc/qscintilla2-qt5-2.11.2/ChangeLog
* /usr/share/doc/qscintilla2-qt5-2.11.2/LICENSE
* /usr/share/doc/qscintilla2-qt5-2.11.2/NEWS
* /usr/share/doc/qscintilla2-qt5-2.11.2/README
* /usr/share/qt5/mkspecs/features/qscintilla2.prf
* /usr/share/qt5/qsci/api/python/Python-2.4.api
* /usr/share/qt5/qsci/api/python/Python-2.5.api
* /usr/share/qt5/qsci/api/python/Python-2.6.api
* /usr/share/qt5/qsci/api/python/Python-2.7.api
* /usr/share/qt5/qsci/api/python/Python-3.1.api
* /usr/share/qt5/qsci/api/python/Python-3.2.api
* /usr/share/qt5/qsci/api/python/Python-3.3.api
* /usr/share/qt5/qsci/api/python/Python-3.4.api
* /usr/share/qt5/qsci/api/python/Python-3.5.api
* /usr/share/qt5/qsci/api/python/Python-3.6.api
* /usr/share/qt5/qsci/api/python/Python-3.7.api
* /usr/share/qt5/qsci/api/python/Python-3.8.api
* /usr/share/qt5/translations/qscintilla_cs.qm
* /usr/share/qt5/translations/qscintilla_de.qm
* /usr/share/qt5/translations/qscintilla_es.qm
* /usr/share/qt5/translations/qscintilla_fr.qm
* /usr/share/qt5/translations/qscintilla_pt_br.qm
{{< /files >}}