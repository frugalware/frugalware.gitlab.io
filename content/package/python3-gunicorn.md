+++
draft = false
title = "python3-gunicorn 21.2.0-1"
version = "21.2.0-1"
description = "WSGI HTTP Server for UNIX"
date = "2023-12-04T14:41:45"
aliases = "/packages/219797"
categories = ['devel-extra']
upstreamurl = "http://gunicorn.org/"
arch = "x86_64"
size = "157408"
usize = "630278"
sha1sum = "aeaccab70d5fa0366346b281321c3f0b41df8023"
depends = "['python3>=3.10', 'python3-eventlet', 'python3-gevent']"
+++
WSGI HTTP Server for UNIX

{{< files text="show files" >}}* /usr/bin/gunicorn
* /usr/lib/python3.12/site-packages/gunicorn-21.2.0-py3.12.egg-info/dependency_links.txt
* /usr/lib/python3.12/site-packages/gunicorn-21.2.0-py3.12.egg-info/entry_points.txt
* /usr/lib/python3.12/site-packages/gunicorn-21.2.0-py3.12.egg-info/not-zip-safe
* /usr/lib/python3.12/site-packages/gunicorn-21.2.0-py3.12.egg-info/PKG-INFO
* /usr/lib/python3.12/site-packages/gunicorn-21.2.0-py3.12.egg-info/requires.txt
* /usr/lib/python3.12/site-packages/gunicorn-21.2.0-py3.12.egg-info/SOURCES.txt
* /usr/lib/python3.12/site-packages/gunicorn-21.2.0-py3.12.egg-info/top_level.txt
* /usr/lib/python3.12/site-packages/gunicorn/app/base.py
* /usr/lib/python3.12/site-packages/gunicorn/app/pasterapp.py
* /usr/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py
* /usr/lib/python3.12/site-packages/gunicorn/app/__init__.py
* /usr/lib/python3.12/site-packages/gunicorn/app/__pycache__/base.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/app/__pycache__/pasterapp.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/app/__pycache__/wsgiapp.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/app/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/arbiter.py
* /usr/lib/python3.12/site-packages/gunicorn/config.py
* /usr/lib/python3.12/site-packages/gunicorn/debug.py
* /usr/lib/python3.12/site-packages/gunicorn/errors.py
* /usr/lib/python3.12/site-packages/gunicorn/glogging.py
* /usr/lib/python3.12/site-packages/gunicorn/http/body.py
* /usr/lib/python3.12/site-packages/gunicorn/http/errors.py
* /usr/lib/python3.12/site-packages/gunicorn/http/message.py
* /usr/lib/python3.12/site-packages/gunicorn/http/parser.py
* /usr/lib/python3.12/site-packages/gunicorn/http/unreader.py
* /usr/lib/python3.12/site-packages/gunicorn/http/wsgi.py
* /usr/lib/python3.12/site-packages/gunicorn/http/__init__.py
* /usr/lib/python3.12/site-packages/gunicorn/http/__pycache__/body.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/http/__pycache__/errors.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/http/__pycache__/message.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/http/__pycache__/parser.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/http/__pycache__/unreader.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/http/__pycache__/wsgi.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/http/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/instrument/statsd.py
* /usr/lib/python3.12/site-packages/gunicorn/instrument/__init__.py
* /usr/lib/python3.12/site-packages/gunicorn/instrument/__pycache__/statsd.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/instrument/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/pidfile.py
* /usr/lib/python3.12/site-packages/gunicorn/reloader.py
* /usr/lib/python3.12/site-packages/gunicorn/sock.py
* /usr/lib/python3.12/site-packages/gunicorn/systemd.py
* /usr/lib/python3.12/site-packages/gunicorn/util.py
* /usr/lib/python3.12/site-packages/gunicorn/workers/base.py
* /usr/lib/python3.12/site-packages/gunicorn/workers/base_async.py
* /usr/lib/python3.12/site-packages/gunicorn/workers/geventlet.py
* /usr/lib/python3.12/site-packages/gunicorn/workers/ggevent.py
* /usr/lib/python3.12/site-packages/gunicorn/workers/gthread.py
* /usr/lib/python3.12/site-packages/gunicorn/workers/gtornado.py
* /usr/lib/python3.12/site-packages/gunicorn/workers/sync.py
* /usr/lib/python3.12/site-packages/gunicorn/workers/workertmp.py
* /usr/lib/python3.12/site-packages/gunicorn/workers/__init__.py
* /usr/lib/python3.12/site-packages/gunicorn/workers/__pycache__/base.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/workers/__pycache__/base_async.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/workers/__pycache__/geventlet.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/workers/__pycache__/ggevent.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/workers/__pycache__/gthread.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/workers/__pycache__/gtornado.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/workers/__pycache__/sync.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/workers/__pycache__/workertmp.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/workers/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/__init__.py
* /usr/lib/python3.12/site-packages/gunicorn/__main__.py
* /usr/lib/python3.12/site-packages/gunicorn/__pycache__/arbiter.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/__pycache__/config.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/__pycache__/debug.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/__pycache__/errors.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/__pycache__/glogging.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/__pycache__/pidfile.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/__pycache__/reloader.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/__pycache__/sock.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/__pycache__/systemd.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/__pycache__/util.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gunicorn/__pycache__/__main__.cpython-312.pyc
* /usr/share/doc/python3-gunicorn-21.2.0/LICENSE
* /usr/share/doc/python3-gunicorn-21.2.0/README.rst
* /usr/share/doc/python3-gunicorn-21.2.0/THANKS
{{< /files >}}