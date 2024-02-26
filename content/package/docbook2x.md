+++
draft = false
title = "docbook2x 0.8.8-5"
version = "0.8.8-5"
description = "Converts DocBook documents to man and Texinfo format."
date = "2021-10-18T09:05:52"
aliases = "/packages/30926"
categories = ['apps-extra']
upstreamurl = "https://sourceforge.net/projects/docbook2x"
arch = "x86_64"
size = "279964"
usize = "1366607"
sha1sum = "833661bbd9b5013b3baaddf4bce627d1561a8c58"
depends = "['libxslt', 'perl-sgmlspm', 'perl-xml-sax>=0.99-5', 'perl-xml-writer>=0.625-5', 'perl-xml-xslt>=0.48-4']"
+++
Converts DocBook documents to man and Texinfo format."

{{< files text="show files" >}}* /usr/bin/db2x_manxml
* /usr/bin/db2x_texixml
* /usr/bin/db2x_xsltproc
* /usr/bin/docbook-to-man
* /usr/bin/docbook2man
* /usr/bin/docbook2texi
* /usr/bin/sgml2xml-isoent
* /usr/bin/utf8trans
* /usr/share/doc/docbook2x-0.8.8/AUTHORS
* /usr/share/doc/docbook2x-0.8.8/ChangeLog
* /usr/share/doc/docbook2x-0.8.8/COPYING
* /usr/share/doc/docbook2x-0.8.8/INSTALL
* /usr/share/doc/docbook2x-0.8.8/NEWS
* /usr/share/doc/docbook2x-0.8.8/README
* /usr/share/doc/docbook2x-0.8.8/THANKS
* /usr/share/doc/docbook2x-0.8.8/TODO
* /usr/share/doc/docbook2x-0.8.8/VERSION
* /usr/share/doc/docbook2X/changes.html
* /usr/share/doc/docbook2X/charsets.html
* /usr/share/doc/docbook2X/cindex.html
* /usr/share/doc/docbook2X/db2x_manxml.html
* /usr/share/doc/docbook2X/db2x_texixml.html
* /usr/share/doc/docbook2X/db2x_xsltproc.html
* /usr/share/doc/docbook2X/dependencies.html
* /usr/share/doc/docbook2X/design-notes.html
* /usr/share/doc/docbook2X/docbook2man.html
* /usr/share/doc/docbook2X/docbook2texi.html
* /usr/share/doc/docbook2X/docbook2X.html
* /usr/share/doc/docbook2X/faq.html
* /usr/share/doc/docbook2X/install.html
* /usr/share/doc/docbook2X/manpages.html
* /usr/share/doc/docbook2X/performance.html
* /usr/share/doc/docbook2X/sgml2xml-isoent.html
* /usr/share/doc/docbook2X/testing.html
* /usr/share/doc/docbook2X/texinfo.html
* /usr/share/doc/docbook2X/todo.html
* /usr/share/doc/docbook2X/utf8trans.html
* /usr/share/doc/docbook2X/xsltproc.html
* /usr/share/docbook2X/charmaps/roff-small.charmap.xml
* /usr/share/docbook2X/charmaps/roff.charmap
* /usr/share/docbook2X/charmaps/roff.charmap.xml
* /usr/share/docbook2X/charmaps/texi-small.charmap.xml
* /usr/share/docbook2X/charmaps/texi.charmap
* /usr/share/docbook2X/charmaps/texi.charmap.xml
* /usr/share/docbook2X/dtd/catalog.xml
* /usr/share/docbook2X/dtd/Man-XML
* /usr/share/docbook2X/dtd/Texi-XML
* /usr/share/docbook2X/VERSION
* /usr/share/docbook2X/xslt/backend/charmap.xsl
* /usr/share/docbook2X/xslt/backend/db2x_manxml.xsl
* /usr/share/docbook2X/xslt/backend/db2x_texixml.xsl
* /usr/share/docbook2X/xslt/backend/man-html-table.xsl
* /usr/share/docbook2X/xslt/backend/man-table.xsl
* /usr/share/docbook2X/xslt/backend/string.xsl
* /usr/share/docbook2X/xslt/catalog.xml
* /usr/share/docbook2X/xslt/common/check-idref.xsl
* /usr/share/docbook2X/xslt/common/cmdsynopsis.xsl
* /usr/share/docbook2X/xslt/common/gentext.xsl
* /usr/share/docbook2X/xslt/common/l10n.xsl
* /usr/share/docbook2X/xslt/common/labels.xsl
* /usr/share/docbook2X/xslt/common/lists.xsl
* /usr/share/docbook2X/xslt/common/messages.xsl
* /usr/share/docbook2X/xslt/common/person.xsl
* /usr/share/docbook2X/xslt/common/string.xsl
* /usr/share/docbook2X/xslt/common/text/af.xml
* /usr/share/docbook2X/xslt/common/text/bg.xml
* /usr/share/docbook2X/xslt/common/text/ca.xml
* /usr/share/docbook2X/xslt/common/text/cs.xml
* /usr/share/docbook2X/xslt/common/text/da.xml
* /usr/share/docbook2X/xslt/common/text/de.xml
* /usr/share/docbook2X/xslt/common/text/el.xml
* /usr/share/docbook2X/xslt/common/text/en.xml
* /usr/share/docbook2X/xslt/common/text/es.xml
* /usr/share/docbook2X/xslt/common/text/et.xml
* /usr/share/docbook2X/xslt/common/text/eu.xml
* /usr/share/docbook2X/xslt/common/text/fi.xml
* /usr/share/docbook2X/xslt/common/text/fr.xml
* /usr/share/docbook2X/xslt/common/text/he.xml
* /usr/share/docbook2X/xslt/common/text/hu.xml
* /usr/share/docbook2X/xslt/common/text/id.xml
* /usr/share/docbook2X/xslt/common/text/it.xml
* /usr/share/docbook2X/xslt/common/text/ja.xml
* /usr/share/docbook2X/xslt/common/text/ko.xml
* /usr/share/docbook2X/xslt/common/text/l10n-set.xml
* /usr/share/docbook2X/xslt/common/text/lt.xml
* /usr/share/docbook2X/xslt/common/text/nl.xml
* /usr/share/docbook2X/xslt/common/text/nn.xml
* /usr/share/docbook2X/xslt/common/text/no.xml
* /usr/share/docbook2X/xslt/common/text/pl.xml
* /usr/share/docbook2X/xslt/common/text/pt-br.xml
* /usr/share/docbook2X/xslt/common/text/pt.xml
* /usr/share/docbook2X/xslt/common/text/ro.xml
* /usr/share/docbook2X/xslt/common/text/ru.xml
* /usr/share/docbook2X/xslt/common/text/sk.xml
* /usr/share/docbook2X/xslt/common/text/sl.xml
* /usr/share/docbook2X/xslt/common/text/sr.xml
* /usr/share/docbook2X/xslt/common/text/sv.xml
* /usr/share/docbook2X/xslt/common/text/th.xml
* /usr/share/docbook2X/xslt/common/text/tr.xml
* /usr/share/docbook2X/xslt/common/text/uk.xml
* /usr/share/docbook2X/xslt/common/text/vi.xml
* /usr/share/docbook2X/xslt/common/text/xh.xml
* /usr/share/docbook2X/xslt/common/text/zh-cn.xml
* /usr/share/docbook2X/xslt/common/text/zh-tw.xml
* /usr/share/docbook2X/xslt/common/titles.xsl
* /usr/share/docbook2X/xslt/common/ucase.xsl
* /usr/share/docbook2X/xslt/common/version.xsl
* /usr/share/docbook2X/xslt/common/whitespace.xsl
* /usr/share/docbook2X/xslt/man/admon.xsl
* /usr/share/docbook2X/xslt/man/beginpage.xsl
* /usr/share/docbook2X/xslt/man/block.xsl
* /usr/share/docbook2X/xslt/man/caption.xsl
* /usr/share/docbook2X/xslt/man/docbook.xsl
* /usr/share/docbook2X/xslt/man/formal.xsl
* /usr/share/docbook2X/xslt/man/glossary.xsl
* /usr/share/docbook2X/xslt/man/index.xsl
* /usr/share/docbook2X/xslt/man/info.xsl
* /usr/share/docbook2X/xslt/man/inline.xsl
* /usr/share/docbook2X/xslt/man/keywords.xsl
* /usr/share/docbook2X/xslt/man/lists.xsl
* /usr/share/docbook2X/xslt/man/manpage.xsl
* /usr/share/docbook2X/xslt/man/param.xsl
* /usr/share/docbook2X/xslt/man/pi.xsl
* /usr/share/docbook2X/xslt/man/refentry.xsl
* /usr/share/docbook2X/xslt/man/sectioning.xsl
* /usr/share/docbook2X/xslt/man/sections.xsl
* /usr/share/docbook2X/xslt/man/synop.xsl
* /usr/share/docbook2X/xslt/man/table.xsl
* /usr/share/docbook2X/xslt/man/toc.xsl
* /usr/share/docbook2X/xslt/man/verbatim.xsl
* /usr/share/docbook2X/xslt/man/xref.xsl
* /usr/share/docbook2X/xslt/texi/admon.xsl
* /usr/share/docbook2X/xslt/texi/autotoc.xsl
* /usr/share/docbook2X/xslt/texi/beginpage.xsl
* /usr/share/docbook2X/xslt/texi/biblio.xsl
* /usr/share/docbook2X/xslt/texi/block.xsl
* /usr/share/docbook2X/xslt/texi/callout.xsl
* /usr/share/docbook2X/xslt/texi/caption.xsl
* /usr/share/docbook2X/xslt/texi/chunk.xsl
* /usr/share/docbook2X/xslt/texi/component.xsl
* /usr/share/docbook2X/xslt/texi/division.xsl
* /usr/share/docbook2X/xslt/texi/docbook.xsl
* /usr/share/docbook2X/xslt/texi/footnote.xsl
* /usr/share/docbook2X/xslt/texi/force-inline.xsl
* /usr/share/docbook2X/xslt/texi/formal.xsl
* /usr/share/docbook2X/xslt/texi/glossary.xsl
* /usr/share/docbook2X/xslt/texi/graphics.xsl
* /usr/share/docbook2X/xslt/texi/index.xsl
* /usr/share/docbook2X/xslt/texi/info.xsl
* /usr/share/docbook2X/xslt/texi/inline.xsl
* /usr/share/docbook2X/xslt/texi/jrefentry.xsl
* /usr/share/docbook2X/xslt/texi/keywords.xsl
* /usr/share/docbook2X/xslt/texi/lists.xsl
* /usr/share/docbook2X/xslt/texi/math.xsl
* /usr/share/docbook2X/xslt/texi/menudescrip.xsl
* /usr/share/docbook2X/xslt/texi/param.xsl
* /usr/share/docbook2X/xslt/texi/pi.xsl
* /usr/share/docbook2X/xslt/texi/qandaset.xsl
* /usr/share/docbook2X/xslt/texi/refentry.xsl
* /usr/share/docbook2X/xslt/texi/sectioning.xsl
* /usr/share/docbook2X/xslt/texi/sections.xsl
* /usr/share/docbook2X/xslt/texi/synop.xsl
* /usr/share/docbook2X/xslt/texi/table.xsl
* /usr/share/docbook2X/xslt/texi/texifile.xsl
* /usr/share/docbook2X/xslt/texi/texinode-base.xsl
* /usr/share/docbook2X/xslt/texi/texinode.xsl
* /usr/share/docbook2X/xslt/texi/toc.xsl
* /usr/share/docbook2X/xslt/texi/verbatim.xsl
* /usr/share/docbook2X/xslt/texi/xref.xsl
* /usr/share/info/docbook2man-xslt.info.gz
* /usr/share/info/docbook2texi-xslt.info.gz
* /usr/share/info/docbook2X.info.gz
* /usr/share/man/man1/db2x_manxml.1.gz
* /usr/share/man/man1/db2x_texixml.1.gz
* /usr/share/man/man1/db2x_xsltproc.1.gz
* /usr/share/man/man1/docbook2man.1.gz
* /usr/share/man/man1/docbook2texi.1.gz
* /usr/share/man/man1/sgml2xml-isoent.1.gz
* /usr/share/man/man1/utf8trans.1.gz
{{< /files >}}