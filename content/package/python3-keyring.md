+++
draft = false
title = "python3-keyring 24.3.0-1"
version = "24.3.0-1"
description = "Store and access your passwords safely"
date = "2023-12-04T14:47:06"
aliases = "/packages/221166"
categories = ['devel-extra']
upstreamurl = "http://pypi.python.org/pypi/keyring"
arch = "x86_64"
size = "62700"
usize = "352998"
sha1sum = "a1c6cd158c6fb3a321b6a87d1cff75b45bcb4c6f"
depends = "['python3-importlib-metadata', 'python3-jaraco.classes', 'python3-secretstorage']"
reverse_depends = "['python3-poetry']"
+++
Store and access your passwords safely{{< spoiler text="show files" >}}* /usr/bin/keyring
* /usr/lib/python3.12/site-packages/keyring-24.3.0.dist-info/entry_points.txt
* /usr/lib/python3.12/site-packages/keyring-24.3.0.dist-info/LICENSE
* /usr/lib/python3.12/site-packages/keyring-24.3.0.dist-info/METADATA
* /usr/lib/python3.12/site-packages/keyring-24.3.0.dist-info/RECORD
* /usr/lib/python3.12/site-packages/keyring-24.3.0.dist-info/top_level.txt
* /usr/lib/python3.12/site-packages/keyring-24.3.0.dist-info/WHEEL
* /usr/lib/python3.12/site-packages/keyring/backend.py
* /usr/lib/python3.12/site-packages/keyring/backends/chainer.py
* /usr/lib/python3.12/site-packages/keyring/backends/fail.py
* /usr/lib/python3.12/site-packages/keyring/backends/kwallet.py
* /usr/lib/python3.12/site-packages/keyring/backends/libsecret.py
* /usr/lib/python3.12/site-packages/keyring/backends/macOS/api.py
* /usr/lib/python3.12/site-packages/keyring/backends/macOS/__init__.py
* /usr/lib/python3.12/site-packages/keyring/backends/macOS/__pycache__/api.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/macOS/__pycache__/api.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/macOS/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/macOS/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/null.py
* /usr/lib/python3.12/site-packages/keyring/backends/SecretService.py
* /usr/lib/python3.12/site-packages/keyring/backends/Windows.py
* /usr/lib/python3.12/site-packages/keyring/backends/__init__.py
* /usr/lib/python3.12/site-packages/keyring/backends/__pycache__/chainer.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/__pycache__/chainer.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/__pycache__/fail.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/__pycache__/fail.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/__pycache__/kwallet.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/__pycache__/kwallet.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/__pycache__/libsecret.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/__pycache__/libsecret.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/__pycache__/null.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/__pycache__/null.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/__pycache__/SecretService.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/__pycache__/SecretService.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/__pycache__/Windows.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/__pycache__/Windows.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/backends/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/backend_complete.bash
* /usr/lib/python3.12/site-packages/keyring/backend_complete.zsh
* /usr/lib/python3.12/site-packages/keyring/cli.py
* /usr/lib/python3.12/site-packages/keyring/completion.py
* /usr/lib/python3.12/site-packages/keyring/core.py
* /usr/lib/python3.12/site-packages/keyring/credentials.py
* /usr/lib/python3.12/site-packages/keyring/devpi_client.py
* /usr/lib/python3.12/site-packages/keyring/errors.py
* /usr/lib/python3.12/site-packages/keyring/http.py
* /usr/lib/python3.12/site-packages/keyring/py.typed
* /usr/lib/python3.12/site-packages/keyring/py312compat.py
* /usr/lib/python3.12/site-packages/keyring/testing/backend.py
* /usr/lib/python3.12/site-packages/keyring/testing/util.py
* /usr/lib/python3.12/site-packages/keyring/testing/__init__.py
* /usr/lib/python3.12/site-packages/keyring/testing/__pycache__/backend.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/testing/__pycache__/backend.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/testing/__pycache__/util.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/testing/__pycache__/util.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/testing/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/testing/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/util/platform_.py
* /usr/lib/python3.12/site-packages/keyring/util/__init__.py
* /usr/lib/python3.12/site-packages/keyring/util/__pycache__/platform_.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/util/__pycache__/platform_.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/util/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/util/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/_compat.py
* /usr/lib/python3.12/site-packages/keyring/_properties_compat.py
* /usr/lib/python3.12/site-packages/keyring/__init__.py
* /usr/lib/python3.12/site-packages/keyring/__main__.py
* /usr/lib/python3.12/site-packages/keyring/__pycache__/backend.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/backend.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/cli.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/cli.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/completion.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/completion.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/core.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/core.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/credentials.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/credentials.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/devpi_client.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/devpi_client.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/errors.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/errors.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/http.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/http.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/py312compat.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/py312compat.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/_compat.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/_compat.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/_properties_compat.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/_properties_compat.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/__main__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/keyring/__pycache__/__main__.cpython-312.pyc
* /usr/share/doc/python3-keyring-24.3.0/LICENSE
* /usr/share/doc/python3-keyring-24.3.0/README.rst
{{< /spoiler >}}