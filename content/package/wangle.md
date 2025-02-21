+++
draft = false
title = "wangle 2025.02.17.00-1"
version = "2025.02.17.00-1"
description = "C++ networking library providing client/server abstractions for building services"
date = "2025-02-21T07:59:51"
aliases = "/packages/222640"
categories = ['lib-extra']
upstreamurl = "https://github.com/facebook/wangle"
arch = "x86_64"
size = "333600"
usize = "1289389"
sha1sum = "9307ed552e6d32e03de3985952359d8fd1dc55ed"
depends = "['fizz']"
+++
### Description: 
C++ networking library providing client/server abstractions for building services

### Files: 
* /usr/include/wangle/acceptor/AcceptObserver.h
* /usr/include/wangle/acceptor/Acceptor.h
* /usr/include/wangle/acceptor/AcceptorHandshakeManager.h
* /usr/include/wangle/acceptor/ConnectionCounter.h
* /usr/include/wangle/acceptor/ConnectionManager.h
* /usr/include/wangle/acceptor/EvbHandshakeHelper.h
* /usr/include/wangle/acceptor/FizzAcceptorHandshakeHelper.h
* /usr/include/wangle/acceptor/FizzConfig.h
* /usr/include/wangle/acceptor/FizzConfigUtil.h
* /usr/include/wangle/acceptor/LoadShedConfiguration.h
* /usr/include/wangle/acceptor/ManagedConnection.h
* /usr/include/wangle/acceptor/NetworkAddress.h
* /usr/include/wangle/acceptor/PeekingAcceptorHandshakeHelper.h
* /usr/include/wangle/acceptor/SecureTransportType.h
* /usr/include/wangle/acceptor/SecurityProtocolContextManager.h
* /usr/include/wangle/acceptor/ServerSocketConfig.h
* /usr/include/wangle/acceptor/SharedSSLContextManager.h
* /usr/include/wangle/acceptor/SocketOptions.h
* /usr/include/wangle/acceptor/SocketPeeker.h
* /usr/include/wangle/acceptor/SSLAcceptorHandshakeHelper.h
* /usr/include/wangle/acceptor/SSLContextSelectionMisc.h
* /usr/include/wangle/acceptor/test/AcceptorHelperMocks.h
* /usr/include/wangle/acceptor/TLSPlaintextPeekingCallback.h
* /usr/include/wangle/acceptor/TransportInfo.h
* /usr/include/wangle/acceptor/UnencryptedAcceptorHandshakeHelper.h
* /usr/include/wangle/bootstrap/AcceptRoutingHandler-inl.h
* /usr/include/wangle/bootstrap/AcceptRoutingHandler.h
* /usr/include/wangle/bootstrap/BaseClientBootstrap.h
* /usr/include/wangle/bootstrap/ClientBootstrap.h
* /usr/include/wangle/bootstrap/RoutingDataHandler-inl.h
* /usr/include/wangle/bootstrap/RoutingDataHandler.h
* /usr/include/wangle/bootstrap/ServerBootstrap-inl.h
* /usr/include/wangle/bootstrap/ServerBootstrap.h
* /usr/include/wangle/bootstrap/ServerSocketFactory.h
* /usr/include/wangle/bootstrap/test/Mocks.h
* /usr/include/wangle/channel/AsyncSocketHandler.h
* /usr/include/wangle/channel/broadcast/BroadcastHandler-inl.h
* /usr/include/wangle/channel/broadcast/BroadcastHandler.h
* /usr/include/wangle/channel/broadcast/BroadcastPool-inl.h
* /usr/include/wangle/channel/broadcast/BroadcastPool.h
* /usr/include/wangle/channel/broadcast/ObservingHandler-inl.h
* /usr/include/wangle/channel/broadcast/ObservingHandler.h
* /usr/include/wangle/channel/broadcast/Subscriber.h
* /usr/include/wangle/channel/broadcast/test/Mocks.h
* /usr/include/wangle/channel/EventBaseHandler.h
* /usr/include/wangle/channel/FileRegion.h
* /usr/include/wangle/channel/Handler.h
* /usr/include/wangle/channel/HandlerContext-inl.h
* /usr/include/wangle/channel/HandlerContext.h
* /usr/include/wangle/channel/OutputBufferingHandler.h
* /usr/include/wangle/channel/Pipeline-inl.h
* /usr/include/wangle/channel/Pipeline.h
* /usr/include/wangle/channel/StaticPipeline.h
* /usr/include/wangle/channel/test/MockHandler.h
* /usr/include/wangle/channel/test/MockPipeline.h
* /usr/include/wangle/client/persistence/FilePersistenceLayer.h
* /usr/include/wangle/client/persistence/FilePersistentCache.h
* /usr/include/wangle/client/persistence/LRUInMemoryCache-inl.h
* /usr/include/wangle/client/persistence/LRUInMemoryCache.h
* /usr/include/wangle/client/persistence/LRUPersistentCache-inl.h
* /usr/include/wangle/client/persistence/LRUPersistentCache.h
* /usr/include/wangle/client/persistence/PersistentCache.h
* /usr/include/wangle/client/persistence/PersistentCacheCommon.h
* /usr/include/wangle/client/persistence/test/Mocks.h
* /usr/include/wangle/client/persistence/test/TestUtil.h
* /usr/include/wangle/client/ssl/SSLSessionCacheData.h
* /usr/include/wangle/client/ssl/SSLSessionCacheUtils.h
* /usr/include/wangle/client/ssl/SSLSessionCallbacks.h
* /usr/include/wangle/client/ssl/SSLSessionPersistentCache-inl.h
* /usr/include/wangle/client/ssl/SSLSessionPersistentCache.h
* /usr/include/wangle/client/ssl/test/Mocks.h
* /usr/include/wangle/client/ssl/test/TestUtil.h
* /usr/include/wangle/client/ssl/ThreadSafeSSLSessionCache.h
* /usr/include/wangle/codec/ByteToMessageDecoder.h
* /usr/include/wangle/codec/FixedLengthFrameDecoder.h
* /usr/include/wangle/codec/LengthFieldBasedFrameDecoder.h
* /usr/include/wangle/codec/LengthFieldPrepender.h
* /usr/include/wangle/codec/LineBasedFrameDecoder.h
* /usr/include/wangle/codec/MessageToByteEncoder.h
* /usr/include/wangle/codec/StringCodec.h
* /usr/include/wangle/codec/test/CodecTestUtils.h
* /usr/include/wangle/service/ClientDispatcher.h
* /usr/include/wangle/service/CloseOnReleaseFilter.h
* /usr/include/wangle/service/ExecutorFilter.h
* /usr/include/wangle/service/ExpiringFilter.h
* /usr/include/wangle/service/ServerDispatcher.h
* /usr/include/wangle/service/Service.h
* /usr/include/wangle/ssl/ClientHelloExtStats.h
* /usr/include/wangle/ssl/PasswordInFileFactory.h
* /usr/include/wangle/ssl/ServerSSLContext.h
* /usr/include/wangle/ssl/SNIConfig.h
* /usr/include/wangle/ssl/SSLCacheOptions.h
* /usr/include/wangle/ssl/SSLCacheProvider.h
* /usr/include/wangle/ssl/SSLContextConfig.h
* /usr/include/wangle/ssl/SSLContextManager.h
* /usr/include/wangle/ssl/SSLSessionCacheManager.h
* /usr/include/wangle/ssl/SSLStats.h
* /usr/include/wangle/ssl/SSLUtil.h
* /usr/include/wangle/ssl/test/MockSSLStats.h
* /usr/include/wangle/ssl/test/TicketUtil.h
* /usr/include/wangle/ssl/TLSCredProcessor.h
* /usr/include/wangle/ssl/TLSInMemoryTicketProcessor.h
* /usr/include/wangle/ssl/TLSTicketKeyManager.h
* /usr/include/wangle/ssl/TLSTicketKeySeeds.h
* /usr/include/wangle/util/FilePoller.h
* /usr/include/wangle/util/MultiFilePoller.h
* /usr/lib/cmake/wangle/wangle-config.cmake
* /usr/lib/cmake/wangle/wangle-targets-release.cmake
* /usr/lib/cmake/wangle/wangle-targets.cmake
* /usr/lib/libwangle.so
* /usr/lib/libwangle.so.2025.02.17.00
* /usr/share/doc/wangle-2025.02.17.00/LICENSE
* /usr/share/doc/wangle-2025.02.17.00/README.md
