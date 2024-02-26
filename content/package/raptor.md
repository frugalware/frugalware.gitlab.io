+++
draft = false
title = "raptor 2.0.16-3"
version = "2.0.16-3"
description = "Library providing a set of parsers that generate Resource Description Framework (RDF)."
date = "2023-11-10T12:36:56"
aliases = "/packages/73108"
categories = ['lib']
upstreamurl = "http://librdf.org/raptor/"
arch = "x86_64"
size = "350124"
usize = "2388302"
sha1sum = "f16693eaf440d34fb806a99bb68788379e01ead1"
depends = "['curl>=7.50.3-2', 'libxml2>=2.9.4-3', 'libxslt>=1.1.28-3', 'openssl>=1.0.2-20']"
reverse_depends = "['flickcurl', 'rasqal']"
+++
Library providing a set of parsers that generate Resource Description Framework (RDF).

{{< files text="show files" >}}* /usr/bin/rapper
* /usr/include/raptor2/raptor.h
* /usr/include/raptor2/raptor2.h
* /usr/lib/libraptor2.so
* /usr/lib/libraptor2.so.0
* /usr/lib/libraptor2.so.0.0.0
* /usr/lib/pkgconfig/raptor2.pc
* /usr/share/doc/raptor-2.0.16/AUTHORS
* /usr/share/doc/raptor-2.0.16/ChangeLog
* /usr/share/doc/raptor-2.0.16/COPYING
* /usr/share/doc/raptor-2.0.16/COPYING.LIB
* /usr/share/doc/raptor-2.0.16/INSTALL
* /usr/share/doc/raptor-2.0.16/INSTALL.html
* /usr/share/doc/raptor-2.0.16/NEWS
* /usr/share/doc/raptor-2.0.16/README
* /usr/share/doc/raptor-2.0.16/README-cmake.md
* /usr/share/doc/raptor-2.0.16/README.html
* /usr/share/doc/raptor-2.0.16/RELEASE.html
* /usr/share/gtk-doc/html/raptor2/home.png
* /usr/share/gtk-doc/html/raptor2/index.html
* /usr/share/gtk-doc/html/raptor2/introduction.html
* /usr/share/gtk-doc/html/raptor2/ix01.html
* /usr/share/gtk-doc/html/raptor2/left-insensitive.png
* /usr/share/gtk-doc/html/raptor2/left.png
* /usr/share/gtk-doc/html/raptor2/parser-grddl.html
* /usr/share/gtk-doc/html/raptor2/parser-guess.html
* /usr/share/gtk-doc/html/raptor2/parser-json.html
* /usr/share/gtk-doc/html/raptor2/parser-ntriples.html
* /usr/share/gtk-doc/html/raptor2/parser-rdfa.html
* /usr/share/gtk-doc/html/raptor2/parser-rdfxml.html
* /usr/share/gtk-doc/html/raptor2/parser-rss-tag-soup.html
* /usr/share/gtk-doc/html/raptor2/parser-trig.html
* /usr/share/gtk-doc/html/raptor2/parser-turtle.html
* /usr/share/gtk-doc/html/raptor2/raptor-formats-types-by-parser.html
* /usr/share/gtk-doc/html/raptor2/raptor-formats-types-by-serializer.html
* /usr/share/gtk-doc/html/raptor2/raptor-formats-types-index.html
* /usr/share/gtk-doc/html/raptor2/raptor-formats.html
* /usr/share/gtk-doc/html/raptor2/raptor-parsers.html
* /usr/share/gtk-doc/html/raptor2/raptor-serializers.html
* /usr/share/gtk-doc/html/raptor2/raptor2-changes-1-4-21-to-2-0-0.html
* /usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-10-to-2-0-11.html
* /usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-11-to-2-0-12.html
* /usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-13-to-2-0-14.html
* /usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-14-to-2-0-15.html
* /usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-15-to-2-0-16.html
* /usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-3-to-2-0-4.html
* /usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-4-to-2-0-5.html
* /usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-5-to-2-0-6.html
* /usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-6-to-2-0-7.html
* /usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-7-to-2-0-8.html
* /usr/share/gtk-doc/html/raptor2/raptor2-changes-2-0-9-to-2-0-10.html
* /usr/share/gtk-doc/html/raptor2/raptor2-changes.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-avltree.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-constants.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-general.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-iostream.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-locator.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-memory.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-option.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-parser.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-sax2.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-sequence.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-serializer.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-stringbuffer.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-triples.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-unicode.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-uri.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-world.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-www.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-xml-namespace.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-xml-qname.html
* /usr/share/gtk-doc/html/raptor2/raptor2-section-xml.html
* /usr/share/gtk-doc/html/raptor2/raptor2.devhelp2
* /usr/share/gtk-doc/html/raptor2/reference-manual.html
* /usr/share/gtk-doc/html/raptor2/restrict-parser-network-access.html
* /usr/share/gtk-doc/html/raptor2/right-insensitive.png
* /usr/share/gtk-doc/html/raptor2/right.png
* /usr/share/gtk-doc/html/raptor2/serializer-atom.html
* /usr/share/gtk-doc/html/raptor2/serializer-dot.html
* /usr/share/gtk-doc/html/raptor2/serializer-json.html
* /usr/share/gtk-doc/html/raptor2/serializer-mkr.html
* /usr/share/gtk-doc/html/raptor2/serializer-nquads.html
* /usr/share/gtk-doc/html/raptor2/serializer-ntriples.html
* /usr/share/gtk-doc/html/raptor2/serializer-rdfxml-abbrev.html
* /usr/share/gtk-doc/html/raptor2/serializer-rdfxml-xmp.html
* /usr/share/gtk-doc/html/raptor2/serializer-rdfxml.html
* /usr/share/gtk-doc/html/raptor2/serializer-rss-1-0.html
* /usr/share/gtk-doc/html/raptor2/serializer-turtle.html
* /usr/share/gtk-doc/html/raptor2/style.css
* /usr/share/gtk-doc/html/raptor2/tutorial-initialising-finishing.html
* /usr/share/gtk-doc/html/raptor2/tutorial-parse-strictness.html
* /usr/share/gtk-doc/html/raptor2/tutorial-parser-abort.html
* /usr/share/gtk-doc/html/raptor2/tutorial-parser-content.html
* /usr/share/gtk-doc/html/raptor2/tutorial-parser-create.html
* /usr/share/gtk-doc/html/raptor2/tutorial-parser-destroy.html
* /usr/share/gtk-doc/html/raptor2/tutorial-parser-example.html
* /usr/share/gtk-doc/html/raptor2/tutorial-parser-features.html
* /usr/share/gtk-doc/html/raptor2/tutorial-parser-runtime-info.html
* /usr/share/gtk-doc/html/raptor2/tutorial-parser-set-error-warning-handlers.html
* /usr/share/gtk-doc/html/raptor2/tutorial-parser-set-id-handler.html
* /usr/share/gtk-doc/html/raptor2/tutorial-parser-set-namespace-handler.html
* /usr/share/gtk-doc/html/raptor2/tutorial-parser-set-triple-handler.html
* /usr/share/gtk-doc/html/raptor2/tutorial-parser-static-info.html
* /usr/share/gtk-doc/html/raptor2/tutorial-parsing.html
* /usr/share/gtk-doc/html/raptor2/tutorial-querying-functionality.html
* /usr/share/gtk-doc/html/raptor2/tutorial-serializer-create.html
* /usr/share/gtk-doc/html/raptor2/tutorial-serializer-declare-namespace.html
* /usr/share/gtk-doc/html/raptor2/tutorial-serializer-destroy.html
* /usr/share/gtk-doc/html/raptor2/tutorial-serializer-example.html
* /usr/share/gtk-doc/html/raptor2/tutorial-serializer-features.html
* /usr/share/gtk-doc/html/raptor2/tutorial-serializer-get-triples.html
* /usr/share/gtk-doc/html/raptor2/tutorial-serializer-runtime-info.html
* /usr/share/gtk-doc/html/raptor2/tutorial-serializer-send-triples.html
* /usr/share/gtk-doc/html/raptor2/tutorial-serializer-set-error-warning-handlers.html
* /usr/share/gtk-doc/html/raptor2/tutorial-serializer-to-destination.html
* /usr/share/gtk-doc/html/raptor2/tutorial-serializing.html
* /usr/share/gtk-doc/html/raptor2/tutorial.html
* /usr/share/gtk-doc/html/raptor2/up-insensitive.png
* /usr/share/gtk-doc/html/raptor2/up.png
* /usr/share/man/man1/rapper.1.gz
* /usr/share/man/man3/libraptor2.3.gz
{{< /files >}}