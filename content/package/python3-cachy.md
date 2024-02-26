+++
draft = false
title = "python3-cachy 0.3.0-1"
version = "0.3.0-1"
description = "simple yet effective caching library"
date = "2023-11-06T16:22:30"
aliases = "/packages/221155"
categories = ['devel-extra']
upstreamurl = "http://pypi.python.org/pypi/cachy"
arch = "x86_64"
size = "48436"
usize = "367222"
sha1sum = "d12f73eaa6fc993eb00b03f6d2bded0c07efac44"
depends = "['python3']"
reverse_depends = "['python3-poetry']"
+++
simple yet effective caching library{{< spoiler text="show files" >}}* /usr/lib/python3.12/site-packages/cachy-0.3.0.dist-info/LICENSE
* /usr/lib/python3.12/site-packages/cachy-0.3.0.dist-info/METADATA
* /usr/lib/python3.12/site-packages/cachy-0.3.0.dist-info/RECORD
* /usr/lib/python3.12/site-packages/cachy-0.3.0.dist-info/top_level.txt
* /usr/lib/python3.12/site-packages/cachy-0.3.0.dist-info/WHEEL
* /usr/lib/python3.12/site-packages/cachy/cache_manager.py
* /usr/lib/python3.12/site-packages/cachy/contracts/factory.py
* /usr/lib/python3.12/site-packages/cachy/contracts/repository.py
* /usr/lib/python3.12/site-packages/cachy/contracts/store.py
* /usr/lib/python3.12/site-packages/cachy/contracts/taggable_store.py
* /usr/lib/python3.12/site-packages/cachy/contracts/__init__.py
* /usr/lib/python3.12/site-packages/cachy/contracts/__pycache__/factory.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/contracts/__pycache__/factory.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/contracts/__pycache__/repository.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/contracts/__pycache__/repository.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/contracts/__pycache__/store.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/contracts/__pycache__/store.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/contracts/__pycache__/taggable_store.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/contracts/__pycache__/taggable_store.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/contracts/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/contracts/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/helpers.py
* /usr/lib/python3.12/site-packages/cachy/redis_tagged_cache.py
* /usr/lib/python3.12/site-packages/cachy/repository.py
* /usr/lib/python3.12/site-packages/cachy/serializers/json_serializer.py
* /usr/lib/python3.12/site-packages/cachy/serializers/msgpack_serializer.py
* /usr/lib/python3.12/site-packages/cachy/serializers/pickle_serializer.py
* /usr/lib/python3.12/site-packages/cachy/serializers/serializer.py
* /usr/lib/python3.12/site-packages/cachy/serializers/__init__.py
* /usr/lib/python3.12/site-packages/cachy/serializers/__pycache__/json_serializer.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/serializers/__pycache__/json_serializer.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/serializers/__pycache__/msgpack_serializer.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/serializers/__pycache__/msgpack_serializer.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/serializers/__pycache__/pickle_serializer.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/serializers/__pycache__/pickle_serializer.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/serializers/__pycache__/serializer.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/serializers/__pycache__/serializer.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/serializers/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/serializers/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/stores/dict_store.py
* /usr/lib/python3.12/site-packages/cachy/stores/file_store.py
* /usr/lib/python3.12/site-packages/cachy/stores/memcached_store.py
* /usr/lib/python3.12/site-packages/cachy/stores/null_store.py
* /usr/lib/python3.12/site-packages/cachy/stores/redis_store.py
* /usr/lib/python3.12/site-packages/cachy/stores/__init__.py
* /usr/lib/python3.12/site-packages/cachy/stores/__pycache__/dict_store.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/stores/__pycache__/dict_store.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/stores/__pycache__/file_store.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/stores/__pycache__/file_store.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/stores/__pycache__/memcached_store.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/stores/__pycache__/memcached_store.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/stores/__pycache__/null_store.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/stores/__pycache__/null_store.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/stores/__pycache__/redis_store.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/stores/__pycache__/redis_store.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/stores/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/stores/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/tagged_cache.py
* /usr/lib/python3.12/site-packages/cachy/tag_set.py
* /usr/lib/python3.12/site-packages/cachy/utils.py
* /usr/lib/python3.12/site-packages/cachy/__init__.py
* /usr/lib/python3.12/site-packages/cachy/__pycache__/cache_manager.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/__pycache__/cache_manager.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/__pycache__/helpers.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/__pycache__/helpers.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/__pycache__/redis_tagged_cache.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/__pycache__/redis_tagged_cache.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/__pycache__/repository.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/__pycache__/repository.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/__pycache__/tagged_cache.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/__pycache__/tagged_cache.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/__pycache__/tag_set.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/__pycache__/tag_set.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/__pycache__/utils.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/__pycache__/utils.cpython-312.pyc
* /usr/lib/python3.12/site-packages/cachy/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/cachy/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/tests/stores/test_dict_store.py
* /usr/lib/python3.12/site-packages/tests/stores/test_file_store.py
* /usr/lib/python3.12/site-packages/tests/stores/test_memcached_store.py
* /usr/lib/python3.12/site-packages/tests/stores/test_null_store.py
* /usr/lib/python3.12/site-packages/tests/stores/test_redis_store.py
* /usr/lib/python3.12/site-packages/tests/stores/__init__.py
* /usr/lib/python3.12/site-packages/tests/stores/__pycache__/test_dict_store.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/tests/stores/__pycache__/test_dict_store.cpython-312.pyc
* /usr/lib/python3.12/site-packages/tests/stores/__pycache__/test_file_store.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/tests/stores/__pycache__/test_file_store.cpython-312.pyc
* /usr/lib/python3.12/site-packages/tests/stores/__pycache__/test_memcached_store.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/tests/stores/__pycache__/test_memcached_store.cpython-312.pyc
* /usr/lib/python3.12/site-packages/tests/stores/__pycache__/test_null_store.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/tests/stores/__pycache__/test_null_store.cpython-312.pyc
* /usr/lib/python3.12/site-packages/tests/stores/__pycache__/test_redis_store.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/tests/stores/__pycache__/test_redis_store.cpython-312.pyc
* /usr/lib/python3.12/site-packages/tests/stores/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/tests/stores/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/tests/test_cache_manager.py
* /usr/lib/python3.12/site-packages/tests/test_repository.py
* /usr/lib/python3.12/site-packages/tests/test_tagged_cache.py
* /usr/lib/python3.12/site-packages/tests/__init__.py
* /usr/lib/python3.12/site-packages/tests/__pycache__/test_cache_manager.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/tests/__pycache__/test_cache_manager.cpython-312.pyc
* /usr/lib/python3.12/site-packages/tests/__pycache__/test_repository.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/tests/__pycache__/test_repository.cpython-312.pyc
* /usr/lib/python3.12/site-packages/tests/__pycache__/test_tagged_cache.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/tests/__pycache__/test_tagged_cache.cpython-312.pyc
* /usr/lib/python3.12/site-packages/tests/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/tests/__pycache__/__init__.cpython-312.pyc
* /usr/share/doc/python3-cachy-0.3.0/CONTRIBUTORS
* /usr/share/doc/python3-cachy-0.3.0/LICENSE
* /usr/share/doc/python3-cachy-0.3.0/README.md
* /usr/share/doc/python3-cachy-0.3.0/README.rst
{{< /spoiler >}}