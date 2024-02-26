+++
draft = false
title = "pycurl 7.45.3-1"
version = "7.45.3-1"
description = "Python module interface to the cURL library"
date = "2024-02-19T09:08:44"
aliases = "/packages/73256"
categories = ['devel']
upstreamurl = "http://pycurl.io/"
arch = "x86_64"
size = "117304"
usize = "564104"
sha1sum = "7292516981382059891bba7462b2bea6c1cf44f1"
depends = "['curl>=7.50.3-2', 'openssl>=3.1.0', 'python3', 'zlib>=1.2.12']"
reverse_depends = "['system-config-printer']"
+++
Python module interface to the cURL library{{< spoiler text="show files" >}}* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/curl/__init__.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/curl/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/EGG-INFO/dependency_links.txt
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/EGG-INFO/native_libs.txt
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/EGG-INFO/not-zip-safe
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/EGG-INFO/PKG-INFO
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/EGG-INFO/SOURCES.txt
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/EGG-INFO/top_level.txt
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/pycurl.cpython-312-x86_64-linux-gnu.so
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/pycurl.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/AUTHORS
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/ChangeLog
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/COPYING-LGPL
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/COPYING-MIT
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/basicfirst.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/file_upload.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/linksys.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/multi-socket_action-select.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/opensocketexception.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/file_upload_buffer.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/file_upload_real.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/file_upload_real_fancy.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/follow_redirect.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/form_post.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/get.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/get_python2.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/get_python2_https.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/get_python3.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/get_python3_https.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/put_buffer.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/put_file.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/response_headers.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/response_info.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/write_file.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/__pycache__/file_upload_buffer.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/__pycache__/file_upload_real.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/__pycache__/file_upload_real_fancy.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/__pycache__/follow_redirect.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/__pycache__/form_post.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/__pycache__/get.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/__pycache__/get_python2.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/__pycache__/get_python2_https.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/__pycache__/get_python3.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/__pycache__/get_python3_https.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/__pycache__/put_buffer.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/__pycache__/put_file.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/__pycache__/response_headers.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/__pycache__/response_info.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/quickstart/__pycache__/write_file.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/retriever-multi.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/retriever.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/sfquery.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/smtp.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/ssh_keyfunction.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/xmlrpc_curl.py
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/__pycache__/basicfirst.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/__pycache__/file_upload.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/__pycache__/linksys.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/__pycache__/multi-socket_action-select.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/__pycache__/opensocketexception.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/__pycache__/retriever-multi.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/__pycache__/retriever.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/__pycache__/sfquery.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/__pycache__/smtp.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/__pycache__/ssh_keyfunction.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/examples/__pycache__/xmlrpc_curl.cpython-312.pyc
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/INSTALL.rst
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/README.rst
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/share/doc/pycurl/RELEASE-NOTES.rst
* /usr/lib/python3.12/site-packages/pycurl-7.45.3-py3.12-linux-x86_64.egg/__pycache__/pycurl.cpython-312.pyc
* /usr/share/doc/pycurl-7.45.3/AUTHORS
* /usr/share/doc/pycurl-7.45.3/ChangeLog
* /usr/share/doc/pycurl-7.45.3/COPYING-LGPL
* /usr/share/doc/pycurl-7.45.3/COPYING-MIT
* /usr/share/doc/pycurl-7.45.3/INSTALL.rst
* /usr/share/doc/pycurl-7.45.3/README.rst
* /usr/share/doc/pycurl-7.45.3/RELEASE-NOTES.rst
{{< /spoiler >}}