+++
draft = false
title = "qcoro 0.10.0-1"
version = "0.10.0-1"
description = "C++ Coroutines for Qt"
date = "2023-12-06T16:37:17"
aliases = "/packages/220955"
categories = ['xlib']
upstreamurl = "https://github.com/danvratil/qcoro"
arch = "x86_64"
size = "2416244"
usize = "4663757"
sha1sum = "ab9fbc4af5eca830a840ab3a8bb3224c27f0169a"
depends = "['qt5-declarative>=5.15.10', 'qt5-websockets>=5.15.10']"
reverse_depends = "['angelfish', 'audiotube', 'kaccounts-integration', 'kdenetwork-filesharing', 'kontrast']"
+++
C++ Coroutines for Qt

{{< files text="show files" >}}* /usr/include/qcoro5/qcoro/concepts_p.h
* /usr/include/qcoro5/qcoro/config.h
* /usr/include/qcoro5/qcoro/coroutine.h
* /usr/include/qcoro5/qcoro/impl/connect.h
* /usr/include/qcoro5/qcoro/impl/isqprivatesignal.h
* /usr/include/qcoro5/qcoro/impl/task.h
* /usr/include/qcoro5/qcoro/impl/taskawaiterbase.h
* /usr/include/qcoro5/qcoro/impl/taskfinalsuspend.h
* /usr/include/qcoro5/qcoro/impl/taskpromise.h
* /usr/include/qcoro5/qcoro/impl/taskpromisebase.h
* /usr/include/qcoro5/qcoro/impl/waitfor.h
* /usr/include/qcoro5/qcoro/macros_p.h
* /usr/include/qcoro5/QCoro/QCoro
* /usr/include/qcoro5/qcoro/qcoro.h
* /usr/include/qcoro5/QCoro/QCoroAbstractSocket
* /usr/include/qcoro5/qcoro/qcoroabstractsocket.h
* /usr/include/qcoro5/QCoro/QCoroAsyncGenerator
* /usr/include/qcoro5/qcoro/qcoroasyncgenerator.h
* /usr/include/qcoro5/QCoro/QCoroCore
* /usr/include/qcoro5/qcoro/qcorocore.h
* /usr/include/qcoro5/qcoro/qcorocore_export.h
* /usr/include/qcoro5/QCoro/QCoroDBus
* /usr/include/qcoro5/qcoro/qcorodbus.h
* /usr/include/qcoro5/QCoro/QCoroDBusPendingCall
* /usr/include/qcoro5/qcoro/qcorodbuspendingcall.h
* /usr/include/qcoro5/QCoro/QCoroDBusPendingReply
* /usr/include/qcoro5/qcoro/qcorodbuspendingreply.h
* /usr/include/qcoro5/qcoro/qcorodbus_export.h
* /usr/include/qcoro5/QCoro/QCoroFuture
* /usr/include/qcoro5/qcoro/qcorofuture.h
* /usr/include/qcoro5/QCoro/QCoroFwd
* /usr/include/qcoro5/qcoro/qcorofwd.h
* /usr/include/qcoro5/QCoro/QCoroGenerator
* /usr/include/qcoro5/qcoro/qcorogenerator.h
* /usr/include/qcoro5/QCoro/QCoroImageProvider
* /usr/include/qcoro5/qcoro/qcoroimageprovider.h
* /usr/include/qcoro5/QCoro/QCoroIODevice
* /usr/include/qcoro5/qcoro/qcoroiodevice.h
* /usr/include/qcoro5/QCoro/QCoroLocalSocket
* /usr/include/qcoro5/qcoro/qcorolocalsocket.h
* /usr/include/qcoro5/QCoro/QCoroNetwork
* /usr/include/qcoro5/qcoro/qcoronetwork.h
* /usr/include/qcoro5/QCoro/QCoroNetworkReply
* /usr/include/qcoro5/qcoro/qcoronetworkreply.h
* /usr/include/qcoro5/qcoro/qcoronetwork_export.h
* /usr/include/qcoro5/QCoro/QCoroProcess
* /usr/include/qcoro5/qcoro/qcoroprocess.h
* /usr/include/qcoro5/QCoro/QCoroQml
* /usr/include/qcoro5/qcoro/qcoroqml.h
* /usr/include/qcoro5/QCoro/QCoroQmlTask
* /usr/include/qcoro5/qcoro/qcoroqmltask.h
* /usr/include/qcoro5/qcoro/qcoroqml_export.h
* /usr/include/qcoro5/qcoro/qcoroquick_export.h
* /usr/include/qcoro5/QCoro/QCoroSignal
* /usr/include/qcoro5/qcoro/qcorosignal.h
* /usr/include/qcoro5/QCoro/QCoroTask
* /usr/include/qcoro5/qcoro/qcorotask.h
* /usr/include/qcoro5/QCoro/QCoroTcpServer
* /usr/include/qcoro5/qcoro/qcorotcpserver.h
* /usr/include/qcoro5/QCoro/QCoroTest
* /usr/include/qcoro5/qcoro/qcorotest.h
* /usr/include/qcoro5/QCoro/QCoroThread
* /usr/include/qcoro5/qcoro/qcorothread.h
* /usr/include/qcoro5/QCoro/QCoroTimer
* /usr/include/qcoro5/qcoro/qcorotimer.h
* /usr/include/qcoro5/QCoro/QCoroWebSocket
* /usr/include/qcoro5/qcoro/qcorowebsocket.h
* /usr/include/qcoro5/QCoro/QCoroWebSockets
* /usr/include/qcoro5/qcoro/qcorowebsockets.h
* /usr/include/qcoro5/QCoro/QCoroWebSocketServer
* /usr/include/qcoro5/qcoro/qcorowebsocketserver.h
* /usr/include/qcoro5/qcoro/qcorowebsockets_export.h
* /usr/include/qcoro5/QCoro/Task
* /usr/include/qcoro5/qcoro/task.h
* /usr/include/qcoro5/qcoro/waitoperationbase_p.h
* /usr/lib/cmake/QCoro5/QCoro5Config.cmake
* /usr/lib/cmake/QCoro5/QCoro5ConfigVersion.cmake
* /usr/lib/cmake/QCoro5Core/QCoro5CoreConfig.cmake
* /usr/lib/cmake/QCoro5Core/QCoro5CoreConfigVersion.cmake
* /usr/lib/cmake/QCoro5Core/QCoro5CoreTargets-release.cmake
* /usr/lib/cmake/QCoro5Core/QCoro5CoreTargets.cmake
* /usr/lib/cmake/QCoro5Coro/QCoro5CoroConfig.cmake
* /usr/lib/cmake/QCoro5Coro/QCoro5CoroConfigVersion.cmake
* /usr/lib/cmake/QCoro5Coro/QCoro5CoroTargets.cmake
* /usr/lib/cmake/QCoro5Coro/QCoroMacros.cmake
* /usr/lib/cmake/QCoro5DBus/QCoro5DBusConfig.cmake
* /usr/lib/cmake/QCoro5DBus/QCoro5DBusConfigVersion.cmake
* /usr/lib/cmake/QCoro5DBus/QCoro5DBusTargets-release.cmake
* /usr/lib/cmake/QCoro5DBus/QCoro5DBusTargets.cmake
* /usr/lib/cmake/QCoro5Network/QCoro5NetworkConfig.cmake
* /usr/lib/cmake/QCoro5Network/QCoro5NetworkConfigVersion.cmake
* /usr/lib/cmake/QCoro5Network/QCoro5NetworkTargets-release.cmake
* /usr/lib/cmake/QCoro5Network/QCoro5NetworkTargets.cmake
* /usr/lib/cmake/QCoro5Qml/QCoro5QmlConfig.cmake
* /usr/lib/cmake/QCoro5Qml/QCoro5QmlConfigVersion.cmake
* /usr/lib/cmake/QCoro5Qml/QCoro5QmlTargets-release.cmake
* /usr/lib/cmake/QCoro5Qml/QCoro5QmlTargets.cmake
* /usr/lib/cmake/QCoro5Quick/QCoro5QuickConfig.cmake
* /usr/lib/cmake/QCoro5Quick/QCoro5QuickConfigVersion.cmake
* /usr/lib/cmake/QCoro5Quick/QCoro5QuickTargets-release.cmake
* /usr/lib/cmake/QCoro5Quick/QCoro5QuickTargets.cmake
* /usr/lib/cmake/QCoro5Test/QCoro5TestConfig.cmake
* /usr/lib/cmake/QCoro5Test/QCoro5TestConfigVersion.cmake
* /usr/lib/cmake/QCoro5Test/QCoro5TestTargets.cmake
* /usr/lib/cmake/QCoro5WebSockets/QCoro5WebSocketsConfig.cmake
* /usr/lib/cmake/QCoro5WebSockets/QCoro5WebSocketsConfigVersion.cmake
* /usr/lib/cmake/QCoro5WebSockets/QCoro5WebSocketsTargets-release.cmake
* /usr/lib/cmake/QCoro5WebSockets/QCoro5WebSocketsTargets.cmake
* /usr/lib/libQCoro5Core.a
* /usr/lib/libQCoro5DBus.a
* /usr/lib/libQCoro5Network.a
* /usr/lib/libQCoro5Qml.a
* /usr/lib/libQCoro5Quick.a
* /usr/lib/libQCoro5WebSockets.a
* /usr/share/doc/qcoro-0.10.0/LICENSE
* /usr/share/doc/qcoro-0.10.0/README.md
* /usr/share/qt5/mkspecs/modules/qt_QCoroCore.pri
* /usr/share/qt5/mkspecs/modules/qt_QCoroCoro.pri
* /usr/share/qt5/mkspecs/modules/qt_QCoroDBus.pri
* /usr/share/qt5/mkspecs/modules/qt_QCoroNetwork.pri
* /usr/share/qt5/mkspecs/modules/qt_QCoroQml.pri
* /usr/share/qt5/mkspecs/modules/qt_QCoroQuick.pri
* /usr/share/qt5/mkspecs/modules/qt_QCoroTest.pri
* /usr/share/qt5/mkspecs/modules/qt_QCoroWebSockets.pri
{{< /files >}}