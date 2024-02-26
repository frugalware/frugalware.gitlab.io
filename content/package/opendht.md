+++
draft = false
title = "opendht 3.1.7-1"
version = "3.1.7-1"
description = "A C++11 implementation of the Kademlia DHT (Distributed Hash Table)"
date = "2024-01-09T12:32:45"
aliases = "/packages/219645"
categories = ['network-extra']
upstreamurl = "https://github.com/savoirfairelinux/opendht"
arch = "x86_64"
size = "1117640"
usize = "3993753"
sha1sum = "196b8130d57e40b1cff58a5e03609db9aeb25541"
depends = "['argon2', 'asio', 'fmtlib>=10.0.0', 'gnutls', 'jsoncpp>=1.9.5', 'nettle>=3.6', 'readline>=8.0', 'restinio']"
+++
A C++11 implementation of the Kademlia DHT (Distributed Hash Table)"

{{< files text="show files" >}}* /etc/dhtcluster.conf
* /etc/dhtnode.conf
* /usr/bin/dhtchat
* /usr/bin/dhtcluster
* /usr/bin/dhtnode
* /usr/bin/dhtscanner
* /usr/include/opendht.h
* /usr/include/opendht/callbacks.h
* /usr/include/opendht/crypto.h
* /usr/include/opendht/crypto/secure_vector.h
* /usr/include/opendht/def.h
* /usr/include/opendht/default_types.h
* /usr/include/opendht/dht.h
* /usr/include/opendht/dhtrunner.h
* /usr/include/opendht/dht_interface.h
* /usr/include/opendht/dht_proxy_client.h
* /usr/include/opendht/dht_proxy_server.h
* /usr/include/opendht/http.h
* /usr/include/opendht/indexation/pht.h
* /usr/include/opendht/infohash.h
* /usr/include/opendht/log.h
* /usr/include/opendht/logger.h
* /usr/include/opendht/network_engine.h
* /usr/include/opendht/network_utils.h
* /usr/include/opendht/node.h
* /usr/include/opendht/node_cache.h
* /usr/include/opendht/node_export.h
* /usr/include/opendht/peer_discovery.h
* /usr/include/opendht/proxy.h
* /usr/include/opendht/rate_limiter.h
* /usr/include/opendht/rng.h
* /usr/include/opendht/routing_table.h
* /usr/include/opendht/scheduler.h
* /usr/include/opendht/securedht.h
* /usr/include/opendht/sockaddr.h
* /usr/include/opendht/thread_pool.h
* /usr/include/opendht/utils.h
* /usr/include/opendht/value.h
* /usr/lib/cmake/opendht/opendhtConfig-none.cmake
* /usr/lib/cmake/opendht/opendhtConfig.cmake
* /usr/lib/cmake/opendht/opendhtConfigVersion.cmake
* /usr/lib/libopendht.so
* /usr/lib/libopendht.so.3
* /usr/lib/libopendht.so.3.1.7
* /usr/lib/pkgconfig/opendht.pc
* /usr/lib/python3.12/site-packages/opendht-3.1.7-py3.12.egg-info/dependency_links.txt
* /usr/lib/python3.12/site-packages/opendht-3.1.7-py3.12.egg-info/PKG-INFO
* /usr/lib/python3.12/site-packages/opendht-3.1.7-py3.12.egg-info/SOURCES.txt
* /usr/lib/python3.12/site-packages/opendht-3.1.7-py3.12.egg-info/top_level.txt
* /usr/lib/python3.12/site-packages/opendht.cpython-312-x86_64-linux-gnu.so
* /usr/lib/systemd/system/dhtcluster.service
* /usr/lib/systemd/system/dhtnode.service
* /usr/share/doc/opendht-3.1.7/COPYING
* /usr/share/doc/opendht-3.1.7/README.md
* /usr/share/man/man1/dhtnode.1.gz
{{< /files >}}