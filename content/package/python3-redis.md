+++
draft = false
title = "python3-redis 5.0.1-1"
version = "5.0.1-1"
date = "2023-12-04T15:20:47"
categories = ['devel-extra']
upstreamurl = "http://pypi.python.org/pypi/redis"
arch = "x86_64"
size = "436100"
usize = "3514613"
sha1sum = "bbb97fc73f6e8d18abd0aa714c52c0f1e053a5e9"
depends = "['python3-async-timeout']"
files = "['usr/', 'usr/lib/', 'usr/lib/python3.12/', 'usr/lib/python3.12/site-packages/', 'usr/lib/python3.12/site-packages/redis-5.0.1.dist-info/', 'usr/lib/python3.12/site-packages/redis-5.0.1.dist-info/LICENSE', 'usr/lib/python3.12/site-packages/redis-5.0.1.dist-info/METADATA', 'usr/lib/python3.12/site-packages/redis-5.0.1.dist-info/RECORD', 'usr/lib/python3.12/site-packages/redis-5.0.1.dist-info/WHEEL', 'usr/lib/python3.12/site-packages/redis-5.0.1.dist-info/top_level.txt', 'usr/lib/python3.12/site-packages/redis/', 'usr/lib/python3.12/site-packages/redis/__init__.py', 'usr/lib/python3.12/site-packages/redis/__pycache__/', 'usr/lib/python3.12/site-packages/redis/__pycache__/__init__.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/__init__.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/backoff.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/backoff.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/client.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/client.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/cluster.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/cluster.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/compat.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/compat.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/connection.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/connection.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/crc.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/crc.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/credentials.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/credentials.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/exceptions.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/exceptions.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/lock.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/lock.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/ocsp.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/ocsp.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/retry.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/retry.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/sentinel.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/sentinel.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/typing.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/typing.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/utils.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/__pycache__/utils.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/', 'usr/lib/python3.12/site-packages/redis/_parsers/__init__.py', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/__init__.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/__init__.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/base.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/base.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/commands.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/commands.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/encoders.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/encoders.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/helpers.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/helpers.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/hiredis.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/hiredis.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/resp2.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/resp2.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/resp3.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/resp3.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/socket.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/__pycache__/socket.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/_parsers/base.py', 'usr/lib/python3.12/site-packages/redis/_parsers/commands.py', 'usr/lib/python3.12/site-packages/redis/_parsers/encoders.py', 'usr/lib/python3.12/site-packages/redis/_parsers/helpers.py', 'usr/lib/python3.12/site-packages/redis/_parsers/hiredis.py', 'usr/lib/python3.12/site-packages/redis/_parsers/resp2.py', 'usr/lib/python3.12/site-packages/redis/_parsers/resp3.py', 'usr/lib/python3.12/site-packages/redis/_parsers/socket.py', 'usr/lib/python3.12/site-packages/redis/asyncio/', 'usr/lib/python3.12/site-packages/redis/asyncio/__init__.py', 'usr/lib/python3.12/site-packages/redis/asyncio/__pycache__/', 'usr/lib/python3.12/site-packages/redis/asyncio/__pycache__/__init__.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/asyncio/__pycache__/__init__.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/asyncio/__pycache__/client.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/asyncio/__pycache__/client.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/asyncio/__pycache__/cluster.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/asyncio/__pycache__/cluster.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/asyncio/__pycache__/connection.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/asyncio/__pycache__/connection.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/asyncio/__pycache__/lock.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/asyncio/__pycache__/lock.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/asyncio/__pycache__/retry.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/asyncio/__pycache__/retry.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/asyncio/__pycache__/sentinel.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/asyncio/__pycache__/sentinel.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/asyncio/__pycache__/utils.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/asyncio/__pycache__/utils.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/asyncio/client.py', 'usr/lib/python3.12/site-packages/redis/asyncio/cluster.py', 'usr/lib/python3.12/site-packages/redis/asyncio/connection.py', 'usr/lib/python3.12/site-packages/redis/asyncio/lock.py', 'usr/lib/python3.12/site-packages/redis/asyncio/retry.py', 'usr/lib/python3.12/site-packages/redis/asyncio/sentinel.py', 'usr/lib/python3.12/site-packages/redis/asyncio/utils.py', 'usr/lib/python3.12/site-packages/redis/backoff.py', 'usr/lib/python3.12/site-packages/redis/client.py', 'usr/lib/python3.12/site-packages/redis/cluster.py', 'usr/lib/python3.12/site-packages/redis/commands/', 'usr/lib/python3.12/site-packages/redis/commands/__init__.py', 'usr/lib/python3.12/site-packages/redis/commands/__pycache__/', 'usr/lib/python3.12/site-packages/redis/commands/__pycache__/__init__.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/__pycache__/__init__.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/__pycache__/cluster.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/__pycache__/cluster.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/__pycache__/core.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/__pycache__/core.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/__pycache__/helpers.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/__pycache__/helpers.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/__pycache__/redismodules.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/__pycache__/redismodules.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/__pycache__/sentinel.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/__pycache__/sentinel.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/bf/', 'usr/lib/python3.12/site-packages/redis/commands/bf/__init__.py', 'usr/lib/python3.12/site-packages/redis/commands/bf/__pycache__/', 'usr/lib/python3.12/site-packages/redis/commands/bf/__pycache__/__init__.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/bf/__pycache__/__init__.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/bf/__pycache__/commands.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/bf/__pycache__/commands.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/bf/__pycache__/info.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/bf/__pycache__/info.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/bf/commands.py', 'usr/lib/python3.12/site-packages/redis/commands/bf/info.py', 'usr/lib/python3.12/site-packages/redis/commands/cluster.py', 'usr/lib/python3.12/site-packages/redis/commands/core.py', 'usr/lib/python3.12/site-packages/redis/commands/graph/', 'usr/lib/python3.12/site-packages/redis/commands/graph/__init__.py', 'usr/lib/python3.12/site-packages/redis/commands/graph/__pycache__/', 'usr/lib/python3.12/site-packages/redis/commands/graph/__pycache__/__init__.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/graph/__pycache__/__init__.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/graph/__pycache__/commands.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/graph/__pycache__/commands.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/graph/__pycache__/edge.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/graph/__pycache__/edge.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/graph/__pycache__/exceptions.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/graph/__pycache__/exceptions.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/graph/__pycache__/execution_plan.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/graph/__pycache__/execution_plan.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/graph/__pycache__/node.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/graph/__pycache__/node.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/graph/__pycache__/path.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/graph/__pycache__/path.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/graph/__pycache__/query_result.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/graph/__pycache__/query_result.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/graph/commands.py', 'usr/lib/python3.12/site-packages/redis/commands/graph/edge.py', 'usr/lib/python3.12/site-packages/redis/commands/graph/exceptions.py', 'usr/lib/python3.12/site-packages/redis/commands/graph/execution_plan.py', 'usr/lib/python3.12/site-packages/redis/commands/graph/node.py', 'usr/lib/python3.12/site-packages/redis/commands/graph/path.py', 'usr/lib/python3.12/site-packages/redis/commands/graph/query_result.py', 'usr/lib/python3.12/site-packages/redis/commands/helpers.py', 'usr/lib/python3.12/site-packages/redis/commands/json/', 'usr/lib/python3.12/site-packages/redis/commands/json/__init__.py', 'usr/lib/python3.12/site-packages/redis/commands/json/__pycache__/', 'usr/lib/python3.12/site-packages/redis/commands/json/__pycache__/__init__.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/json/__pycache__/__init__.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/json/__pycache__/_util.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/json/__pycache__/_util.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/json/__pycache__/commands.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/json/__pycache__/commands.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/json/__pycache__/decoders.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/json/__pycache__/decoders.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/json/__pycache__/path.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/json/__pycache__/path.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/json/_util.py', 'usr/lib/python3.12/site-packages/redis/commands/json/commands.py', 'usr/lib/python3.12/site-packages/redis/commands/json/decoders.py', 'usr/lib/python3.12/site-packages/redis/commands/json/path.py', 'usr/lib/python3.12/site-packages/redis/commands/redismodules.py', 'usr/lib/python3.12/site-packages/redis/commands/search/', 'usr/lib/python3.12/site-packages/redis/commands/search/__init__.py', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/__init__.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/__init__.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/_util.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/_util.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/aggregation.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/aggregation.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/commands.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/commands.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/document.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/document.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/field.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/field.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/indexDefinition.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/indexDefinition.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/query.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/query.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/querystring.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/querystring.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/reducers.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/reducers.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/result.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/result.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/suggestion.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/__pycache__/suggestion.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/search/_util.py', 'usr/lib/python3.12/site-packages/redis/commands/search/aggregation.py', 'usr/lib/python3.12/site-packages/redis/commands/search/commands.py', 'usr/lib/python3.12/site-packages/redis/commands/search/document.py', 'usr/lib/python3.12/site-packages/redis/commands/search/field.py', 'usr/lib/python3.12/site-packages/redis/commands/search/indexDefinition.py', 'usr/lib/python3.12/site-packages/redis/commands/search/query.py', 'usr/lib/python3.12/site-packages/redis/commands/search/querystring.py', 'usr/lib/python3.12/site-packages/redis/commands/search/reducers.py', 'usr/lib/python3.12/site-packages/redis/commands/search/result.py', 'usr/lib/python3.12/site-packages/redis/commands/search/suggestion.py', 'usr/lib/python3.12/site-packages/redis/commands/sentinel.py', 'usr/lib/python3.12/site-packages/redis/commands/timeseries/', 'usr/lib/python3.12/site-packages/redis/commands/timeseries/__init__.py', 'usr/lib/python3.12/site-packages/redis/commands/timeseries/__pycache__/', 'usr/lib/python3.12/site-packages/redis/commands/timeseries/__pycache__/__init__.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/timeseries/__pycache__/__init__.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/timeseries/__pycache__/commands.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/timeseries/__pycache__/commands.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/timeseries/__pycache__/info.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/timeseries/__pycache__/info.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/timeseries/__pycache__/utils.cpython-312.opt-1.pyc', 'usr/lib/python3.12/site-packages/redis/commands/timeseries/__pycache__/utils.cpython-312.pyc', 'usr/lib/python3.12/site-packages/redis/commands/timeseries/commands.py', 'usr/lib/python3.12/site-packages/redis/commands/timeseries/info.py', 'usr/lib/python3.12/site-packages/redis/commands/timeseries/utils.py', 'usr/lib/python3.12/site-packages/redis/compat.py', 'usr/lib/python3.12/site-packages/redis/connection.py', 'usr/lib/python3.12/site-packages/redis/crc.py', 'usr/lib/python3.12/site-packages/redis/credentials.py', 'usr/lib/python3.12/site-packages/redis/exceptions.py', 'usr/lib/python3.12/site-packages/redis/lock.py', 'usr/lib/python3.12/site-packages/redis/ocsp.py', 'usr/lib/python3.12/site-packages/redis/retry.py', 'usr/lib/python3.12/site-packages/redis/sentinel.py', 'usr/lib/python3.12/site-packages/redis/typing.py', 'usr/lib/python3.12/site-packages/redis/utils.py', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/python3-redis-5.0.1/', 'usr/share/doc/python3-redis-5.0.1/INSTALL', 'usr/share/doc/python3-redis-5.0.1/LICENSE', 'usr/share/doc/python3-redis-5.0.1/README.md']"
+++
The Python interface to the Redis key-value store