+++
draft = false
title = "ruby-rdiscount 2.2.7.3-1"
version = "2.2.7.3-1"
description = "Fast Implementation of Gruber's Markdown in C"
date = "2024-01-20T22:23:57"
aliases = "/packages/219489"
categories = ['devel-extra']
upstreamurl = "http://dafoster.net/projects/rdiscount/"
arch = "x86_64"
size = "181500"
usize = "547385"
sha1sum = "adcfab4b7177cfb14b31c29bc3211e37c0f2b794"
depends = "['ruby>=3.2.0', 'ruby>=3.3.0']"
reverse_depends = "['ruby-ronn']"
+++
Fast Implementation of Gruber's Markdown in C

{{< files text="show files" >}}* /usr/bin/rdiscount
* /usr/lib/ruby/gems/3.3.0/cache/rdiscount-2.2.7.3.gem
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/cache.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/ext/page-blocktags.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/ext/page-Makefile.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/ext/page-VERSION.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/Object/cdesc-Object.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/Object/sized_int-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/page-COPYING.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/autolink-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/cdesc-RDiscount.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/explicitlist-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/filter_html-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/filter_styles-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/fold_lines-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/footnotes-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/generate_toc-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/latex-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/md1compat-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/new-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/no_image-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/no_links-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/no_pseudo_protocols-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/no_strikethrough-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/no_superscript-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/no_tables-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/safelink-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/smart-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/strict-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/text-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/toc_content-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/rdiscount-2.2.7.3/ri/RDiscount/to_html-i.ri
* /usr/lib/ruby/gems/3.3.0/extensions/x86_64-linux/3.3.0/rdiscount-2.2.7.3/gem.build_complete
* /usr/lib/ruby/gems/3.3.0/extensions/x86_64-linux/3.3.0/rdiscount-2.2.7.3/gem_make.out
* /usr/lib/ruby/gems/3.3.0/extensions/x86_64-linux/3.3.0/rdiscount-2.2.7.3/mkmf.log
* /usr/lib/ruby/gems/3.3.0/extensions/x86_64-linux/3.3.0/rdiscount-2.2.7.3/rdiscount.so
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/bin/rdiscount
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/BUILDING
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/CHANGELOG.md
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/COPYING
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/amalloc.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/amalloc.h
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/basename.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/blocktags
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/config.h
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/Csio.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/css.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/cstring.h
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/docheader.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/dumptree.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/emmatch.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/extconf.rb
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/flags.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/generate.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/gethopt.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/gethopt.h
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/github_flavoured.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/h1title.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/html5.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/Makefile
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/markdown.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/markdown.h
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/mkdio.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/mkdio.h
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/mktags.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/notspecial.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/pgm_options.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/pgm_options.h
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/rdiscount.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/resource.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/ruby-config.h
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/setup.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/tags.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/tags.h
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/toc.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/VERSION
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/version.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/xml.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/ext/xmlpage.c
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/lib/markdown.rb
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/lib/rdiscount.rb
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/lib/rdiscount.so
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/man/markdown.7
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/man/rdiscount.1
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/man/rdiscount.1.ronn
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/Rakefile
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/rdiscount.gemspec
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/README.markdown
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/test/benchmark.rb
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/test/benchmark.txt
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/test/markdown_test.rb
* /usr/lib/ruby/gems/3.3.0/gems/rdiscount-2.2.7.3/test/rdiscount_test.rb
* /usr/lib/ruby/gems/3.3.0/specifications/rdiscount-2.2.7.3.gemspec
{{< /files >}}