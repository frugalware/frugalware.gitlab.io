+++
draft = false
title = "xmlrpc-c 1.54.06-2"
version = "1.54.06-2"
description = "This library provides a modular implementation of XML-RPC for C and C++."
date = "2023-03-16T04:13:04"
aliases = "/packages/15116"
categories = ['network-extra']
upstreamurl = "http://xmlrpc-c.sourceforge.net/"
arch = "x86_64"
size = "335296"
usize = "1466989"
sha1sum = "b27792363f476c19a97f02cb4770f1377f3354f3"
depends = "['curl>=7.19.0', 'libstdc++', 'libxml2>=2.7.8', 'openssl>=3.1.0', 'readline>=8.0']"
reverse_depends = "['rtorrent']"
+++
This library provides a modular implementation of XML-RPC for C and C++.{{< files text="show files" >}}* /usr/bin/xml-rpc-api2cpp
* /usr/bin/xml-rpc-api2txt
* /usr/bin/xmlrpc
* /usr/bin/xmlrpc-c-config
* /usr/bin/xmlrpc_cpp_proxy
* /usr/bin/xmlrpc_dumpserver
* /usr/bin/xmlrpc_parsecall
* /usr/bin/xmlrpc_pstream
* /usr/bin/xmlrpc_transport
* /usr/include/xmlrpc-c/abyss.h
* /usr/include/xmlrpc-c/AbyssChanSwitch.hpp
* /usr/include/xmlrpc-c/AbyssChanSwitchUnix.hpp
* /usr/include/xmlrpc-c/AbyssEnvironment.hpp
* /usr/include/xmlrpc-c/AbyssServer.hpp
* /usr/include/xmlrpc-c/abyss_reqhandler_xmlrpc.hpp
* /usr/include/xmlrpc-c/abyss_unixsock.h
* /usr/include/xmlrpc-c/abyss_winsock.h
* /usr/include/xmlrpc-c/base.h
* /usr/include/xmlrpc-c/base.hpp
* /usr/include/xmlrpc-c/base64.hpp
* /usr/include/xmlrpc-c/client.h
* /usr/include/xmlrpc-c/client.hpp
* /usr/include/xmlrpc-c/client_global.h
* /usr/include/xmlrpc-c/client_simple.hpp
* /usr/include/xmlrpc-c/client_transport.hpp
* /usr/include/xmlrpc-c/config.h
* /usr/include/xmlrpc-c/c_util.h
* /usr/include/xmlrpc-c/girerr.hpp
* /usr/include/xmlrpc-c/girmem.hpp
* /usr/include/xmlrpc-c/inttypes.h
* /usr/include/xmlrpc-c/json.h
* /usr/include/xmlrpc-c/oldcppwrapper.hpp
* /usr/include/xmlrpc-c/oldxmlrpc.h
* /usr/include/xmlrpc-c/packetsocket.hpp
* /usr/include/xmlrpc-c/registry.hpp
* /usr/include/xmlrpc-c/server.h
* /usr/include/xmlrpc-c/server_abyss.h
* /usr/include/xmlrpc-c/server_abyss.hpp
* /usr/include/xmlrpc-c/server_cgi.h
* /usr/include/xmlrpc-c/server_pstream.hpp
* /usr/include/xmlrpc-c/server_w32httpsys.h
* /usr/include/xmlrpc-c/timeout.hpp
* /usr/include/xmlrpc-c/transport.h
* /usr/include/xmlrpc-c/util.h
* /usr/include/xmlrpc-c/xml.hpp
* /usr/include/xmlrpc.h
* /usr/include/XmlRpcCpp.h
* /usr/include/xmlrpc_abyss.h
* /usr/include/xmlrpc_cgi.h
* /usr/include/xmlrpc_client.h
* /usr/include/xmlrpc_server.h
* /usr/include/xmlrpc_server_w32httpsys.h
* /usr/lib/libxmlrpc++.so
* /usr/lib/libxmlrpc++.so.8
* /usr/lib/libxmlrpc++.so.8.54
* /usr/lib/libxmlrpc.so
* /usr/lib/libxmlrpc.so.3
* /usr/lib/libxmlrpc.so.3.54
* /usr/lib/libxmlrpc_abyss++.so
* /usr/lib/libxmlrpc_abyss++.so.8
* /usr/lib/libxmlrpc_abyss++.so.8.54
* /usr/lib/libxmlrpc_abyss.so
* /usr/lib/libxmlrpc_abyss.so.3
* /usr/lib/libxmlrpc_abyss.so.3.54
* /usr/lib/libxmlrpc_client++.so
* /usr/lib/libxmlrpc_client++.so.8
* /usr/lib/libxmlrpc_client++.so.8.54
* /usr/lib/libxmlrpc_client.so
* /usr/lib/libxmlrpc_client.so.3
* /usr/lib/libxmlrpc_client.so.3.54
* /usr/lib/libxmlrpc_cpp.so
* /usr/lib/libxmlrpc_cpp.so.8
* /usr/lib/libxmlrpc_cpp.so.8.54
* /usr/lib/libxmlrpc_packetsocket.so
* /usr/lib/libxmlrpc_packetsocket.so.8
* /usr/lib/libxmlrpc_packetsocket.so.8.54
* /usr/lib/libxmlrpc_server++.so
* /usr/lib/libxmlrpc_server++.so.8
* /usr/lib/libxmlrpc_server++.so.8.54
* /usr/lib/libxmlrpc_server.so
* /usr/lib/libxmlrpc_server.so.3
* /usr/lib/libxmlrpc_server.so.3.54
* /usr/lib/libxmlrpc_server_abyss++.so
* /usr/lib/libxmlrpc_server_abyss++.so.8
* /usr/lib/libxmlrpc_server_abyss++.so.8.54
* /usr/lib/libxmlrpc_server_abyss.so
* /usr/lib/libxmlrpc_server_abyss.so.3
* /usr/lib/libxmlrpc_server_abyss.so.3.54
* /usr/lib/libxmlrpc_server_cgi++.so
* /usr/lib/libxmlrpc_server_cgi++.so.8
* /usr/lib/libxmlrpc_server_cgi++.so.8.54
* /usr/lib/libxmlrpc_server_cgi.so
* /usr/lib/libxmlrpc_server_cgi.so.3
* /usr/lib/libxmlrpc_server_cgi.so.3.54
* /usr/lib/libxmlrpc_server_pstream++.so
* /usr/lib/libxmlrpc_server_pstream++.so.8
* /usr/lib/libxmlrpc_server_pstream++.so.8.54
* /usr/lib/libxmlrpc_util++.so
* /usr/lib/libxmlrpc_util++.so.8
* /usr/lib/libxmlrpc_util++.so.8.54
* /usr/lib/libxmlrpc_util.so
* /usr/lib/libxmlrpc_util.so.4
* /usr/lib/libxmlrpc_util.so.4.54
* /usr/lib/libxmlrpc_xmlparse.so
* /usr/lib/libxmlrpc_xmlparse.so.3
* /usr/lib/libxmlrpc_xmlparse.so.3.54
* /usr/lib/libxmlrpc_xmltok.so
* /usr/lib/libxmlrpc_xmltok.so.3
* /usr/lib/libxmlrpc_xmltok.so.3.54
* /usr/lib/pkgconfig/xmlrpc++.pc
* /usr/lib/pkgconfig/xmlrpc.pc
* /usr/lib/pkgconfig/xmlrpc_abyss++.pc
* /usr/lib/pkgconfig/xmlrpc_abyss.pc
* /usr/lib/pkgconfig/xmlrpc_client++.pc
* /usr/lib/pkgconfig/xmlrpc_client.pc
* /usr/lib/pkgconfig/xmlrpc_expat.pc
* /usr/lib/pkgconfig/xmlrpc_server++.pc
* /usr/lib/pkgconfig/xmlrpc_server.pc
* /usr/lib/pkgconfig/xmlrpc_server_abyss.pc
* /usr/lib/pkgconfig/xmlrpc_server_cgi.pc
* /usr/lib/pkgconfig/xmlrpc_server_pstream++.pc
* /usr/lib/pkgconfig/xmlrpc_util++.pc
* /usr/lib/pkgconfig/xmlrpc_util.pc
* /usr/share/doc/xmlrpc-c-1.54.06/README
* /usr/share/man/man1/xml-rpc-api2cpp.1.gz
* /usr/share/man/man1/xml-rpc-api2txt.1.gz
{{< /files >}}