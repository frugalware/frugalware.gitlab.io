+++
draft = false
title = "libwebsockets 4.3.5-1"
version = "4.3.5-1"
description = "C library for websocket clients and servers"
date = "2025-02-28T14:34:25"
aliases = "/packages/220925"
categories = ['lib-extra']
upstreamurl = "https://github.com/warmcat/libwebsockets"
arch = "x86_64"
size = "387976"
usize = "1388923"
sha1sum = "c6e93197b5af37bb5a60b9a33ee637eb10def5b7"
depends = "['glibc', 'libev', 'libuv', 'openssl>=3.1.0']"
reverse_depends = "['seafile']"
+++
### Description: 
C library for websocket clients and servers

### Files: 
* /usr/include/libwebsockets.h
* /usr/include/libwebsockets/abstract/abstract.h
* /usr/include/libwebsockets/abstract/protocols.h
* /usr/include/libwebsockets/abstract/protocols/smtp.h
* /usr/include/libwebsockets/abstract/transports.h
* /usr/include/libwebsockets/abstract/transports/raw-skt.h
* /usr/include/libwebsockets/abstract/transports/unit-test.h
* /usr/include/libwebsockets/lws-adopt.h
* /usr/include/libwebsockets/lws-async-dns.h
* /usr/include/libwebsockets/lws-bb-i2c.h
* /usr/include/libwebsockets/lws-bb-spi.h
* /usr/include/libwebsockets/lws-button.h
* /usr/include/libwebsockets/lws-cache-ttl.h
* /usr/include/libwebsockets/lws-callbacks.h
* /usr/include/libwebsockets/lws-cgi.h
* /usr/include/libwebsockets/lws-client.h
* /usr/include/libwebsockets/lws-conmon.h
* /usr/include/libwebsockets/lws-context-vhost.h
* /usr/include/libwebsockets/lws-cose.h
* /usr/include/libwebsockets/lws-dbus.h
* /usr/include/libwebsockets/lws-diskcache.h
* /usr/include/libwebsockets/lws-display.h
* /usr/include/libwebsockets/lws-dll2.h
* /usr/include/libwebsockets/lws-dsh.h
* /usr/include/libwebsockets/lws-eventlib-exports.h
* /usr/include/libwebsockets/lws-fault-injection.h
* /usr/include/libwebsockets/lws-freertos.h
* /usr/include/libwebsockets/lws-fts.h
* /usr/include/libwebsockets/lws-genaes.h
* /usr/include/libwebsockets/lws-gencrypto.h
* /usr/include/libwebsockets/lws-genec.h
* /usr/include/libwebsockets/lws-genhash.h
* /usr/include/libwebsockets/lws-genrsa.h
* /usr/include/libwebsockets/lws-gpio.h
* /usr/include/libwebsockets/lws-http.h
* /usr/include/libwebsockets/lws-i2c.h
* /usr/include/libwebsockets/lws-ili9341-spi.h
* /usr/include/libwebsockets/lws-jose.h
* /usr/include/libwebsockets/lws-jwe.h
* /usr/include/libwebsockets/lws-jwk.h
* /usr/include/libwebsockets/lws-jws.h
* /usr/include/libwebsockets/lws-lecp.h
* /usr/include/libwebsockets/lws-led.h
* /usr/include/libwebsockets/lws-lejp.h
* /usr/include/libwebsockets/lws-logs.h
* /usr/include/libwebsockets/lws-lwsac.h
* /usr/include/libwebsockets/lws-map.h
* /usr/include/libwebsockets/lws-metrics.h
* /usr/include/libwebsockets/lws-misc.h
* /usr/include/libwebsockets/lws-mqtt.h
* /usr/include/libwebsockets/lws-netdev.h
* /usr/include/libwebsockets/lws-network-helper.h
* /usr/include/libwebsockets/lws-optee.h
* /usr/include/libwebsockets/lws-protocols-plugins.h
* /usr/include/libwebsockets/lws-purify.h
* /usr/include/libwebsockets/lws-pwm.h
* /usr/include/libwebsockets/lws-retry.h
* /usr/include/libwebsockets/lws-ring.h
* /usr/include/libwebsockets/lws-secure-streams-client.h
* /usr/include/libwebsockets/lws-secure-streams-policy.h
* /usr/include/libwebsockets/lws-secure-streams.h
* /usr/include/libwebsockets/lws-sequencer.h
* /usr/include/libwebsockets/lws-service.h
* /usr/include/libwebsockets/lws-settings.h
* /usr/include/libwebsockets/lws-sha1-base64.h
* /usr/include/libwebsockets/lws-smd.h
* /usr/include/libwebsockets/lws-spa.h
* /usr/include/libwebsockets/lws-spi.h
* /usr/include/libwebsockets/lws-ssd1306-i2c.h
* /usr/include/libwebsockets/lws-state.h
* /usr/include/libwebsockets/lws-struct.h
* /usr/include/libwebsockets/lws-system.h
* /usr/include/libwebsockets/lws-test-sequencer.h
* /usr/include/libwebsockets/lws-threadpool.h
* /usr/include/libwebsockets/lws-timeout-timer.h
* /usr/include/libwebsockets/lws-tls-sessions.h
* /usr/include/libwebsockets/lws-tokenize.h
* /usr/include/libwebsockets/lws-vfs.h
* /usr/include/libwebsockets/lws-write.h
* /usr/include/libwebsockets/lws-writeable.h
* /usr/include/libwebsockets/lws-ws-close.h
* /usr/include/libwebsockets/lws-ws-ext.h
* /usr/include/libwebsockets/lws-ws-state.h
* /usr/include/libwebsockets/lws-x509.h
* /usr/include/lws_config.h
* /usr/lib/cmake/libwebsockets/libwebsockets-config-version.cmake
* /usr/lib/cmake/libwebsockets/libwebsockets-config.cmake
* /usr/lib/cmake/libwebsockets/LibwebsocketsTargets-release.cmake
* /usr/lib/cmake/libwebsockets/LibwebsocketsTargets.cmake
* /usr/lib/cmake/libwebsockets/LwsCheckRequirements.cmake
* /usr/lib/libwebsockets-evlib_ev.so
* /usr/lib/libwebsockets-evlib_glib.so
* /usr/lib/libwebsockets-evlib_uv.so
* /usr/lib/libwebsockets.so
* /usr/lib/libwebsockets.so.19
* /usr/lib/pkgconfig/libwebsockets.pc
* /usr/lib/pkgconfig/libwebsockets_static.pc
* /usr/share/doc/libwebsockets-4.3.5/LICENSE
* /usr/share/doc/libwebsockets-4.3.5/README.md
