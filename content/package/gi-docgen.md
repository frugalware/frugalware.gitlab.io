+++
draft = false
title = "gi-docgen 2023.3-1"
version = "2023.3-1"
description = "Documentation generator for GObject-based libraries"
date = "2024-02-23T13:03:38"
aliases = "/packages/220816"
categories = ['devel-extra']
upstreamurl = "https://gnome.pages.gitlab.gnome.org/gi-docgen/"
arch = "x86_64"
size = "1221084"
usize = "2211989"
sha1sum = "55f3989a0e5ec12661375a5b98229c3e6d108854"
depends = "['python3-jinja', 'python3-markdown', 'python3-markupsafe', 'python3-pygments', 'python3-toml', 'python3-typogrify']"
+++
Documentation generator for GObject-based libraries

{{< files text="show files" >}}* /usr/bin/gi-docgen
* /usr/lib/pkgconfig/gi-docgen.pc
* /usr/lib/python3.12/site-packages/gidocgen/config.py
* /usr/lib/python3.12/site-packages/gidocgen/core.py
* /usr/lib/python3.12/site-packages/gidocgen/gdcheck.py
* /usr/lib/python3.12/site-packages/gidocgen/gdgendeps.py
* /usr/lib/python3.12/site-packages/gidocgen/gdgenerate.py
* /usr/lib/python3.12/site-packages/gidocgen/gdgenindices.py
* /usr/lib/python3.12/site-packages/gidocgen/gdindex.py
* /usr/lib/python3.12/site-packages/gidocgen/gdsearch.py
* /usr/lib/python3.12/site-packages/gidocgen/gdserver.py
* /usr/lib/python3.12/site-packages/gidocgen/gidocmain.py
* /usr/lib/python3.12/site-packages/gidocgen/gir/ast.py
* /usr/lib/python3.12/site-packages/gidocgen/gir/parser.py
* /usr/lib/python3.12/site-packages/gidocgen/gir/__init__.py
* /usr/lib/python3.12/site-packages/gidocgen/gir/__pycache__/ast.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gidocgen/gir/__pycache__/parser.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gidocgen/gir/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gidocgen/log.py
* /usr/lib/python3.12/site-packages/gidocgen/mdext.py
* /usr/lib/python3.12/site-packages/gidocgen/py.typed
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/base.html
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/basic.toml
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/class.html
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/class_method.html
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/constant.html
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/content.html
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/ctor.html
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/enum.html
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/fonts.css
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/function.html
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/fzy.js
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/go-up-symbolic.png
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/interface.html
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/main.js
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/method.html
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/namespace.html
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/property.html
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatDisplay-Black.woff
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatDisplay-Black.woff2
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatDisplay-BlackItalic.woff
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatDisplay-BlackItalic.woff2
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatDisplay-Bold.woff
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatDisplay-Bold.woff2
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatDisplay-BoldItalic.woff
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatDisplay-BoldItalic.woff2
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatDisplay-Italic.woff
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatDisplay-Italic.woff2
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatDisplay-Medium.woff
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatDisplay-Medium.woff2
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatDisplay-MediumItalic.woff
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatDisplay-MediumItalic.woff2
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatDisplay-Regular.woff
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatDisplay-Regular.woff2
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatText-Bold.woff
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatText-Bold.woff2
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatText-BoldItalic.woff
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatText-BoldItalic.woff2
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatText-Italic.woff
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatText-Italic.woff2
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatText-Medium.woff
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatText-Medium.woff2
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatText-MediumItalic.woff
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatText-MediumItalic.woff2
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatText-Regular.woff
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/RedHatText-Regular.woff2
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/search.js
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/signal.html
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/solarized-dark.css
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/solarized-light.css
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/SourceCodePro-It.ttf.woff
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/SourceCodePro-Regular.ttf.woff
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/SourceCodePro-Semibold.ttf.woff
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/struct.html
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/style.css
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/type_func.html
* /usr/lib/python3.12/site-packages/gidocgen/templates/basic/vfunc.html
* /usr/lib/python3.12/site-packages/gidocgen/utils.py
* /usr/lib/python3.12/site-packages/gidocgen/__init__.py
* /usr/lib/python3.12/site-packages/gidocgen/__pycache__/config.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gidocgen/__pycache__/core.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gidocgen/__pycache__/gdcheck.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gidocgen/__pycache__/gdgendeps.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gidocgen/__pycache__/gdgenerate.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gidocgen/__pycache__/gdgenindices.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gidocgen/__pycache__/gdindex.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gidocgen/__pycache__/gdsearch.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gidocgen/__pycache__/gdserver.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gidocgen/__pycache__/gidocmain.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gidocgen/__pycache__/log.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gidocgen/__pycache__/mdext.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gidocgen/__pycache__/utils.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gidocgen/__pycache__/__init__.cpython-312.pyc
* /usr/share/doc/gi-docgen-2023.3/README.md
{{< /files >}}