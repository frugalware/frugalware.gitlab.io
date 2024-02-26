+++
draft = false
title = "haskell-warp 3.3.31-1"
version = "3.3.31-1"
description = "A fast, light-weight web server for WAI applications"
date = "2023-12-13T10:59:16"
aliases = "/packages/220717"
categories = ['devel-extra']
upstreamurl = "http://hackage.haskell.org/cgi-bin/hackage-scripts/package/warp"
arch = "x86_64"
size = "441192"
usize = "4412853"
sha1sum = "4892b4a94eea65f1a18e16215b0660fc89e7184d"
depends = "['haskell-bsb-http-chunked', 'haskell-http-date', 'haskell-http2', 'haskell-iproute', 'haskell-recv', 'haskell-simple-sendfile', 'haskell-streaming-commons', 'haskell-unix-compat', 'haskell-unliftio', 'haskell-wai', 'haskell-word8']"
reverse_depends = "['haskell-wai-extra']"
+++
A fast, light-weight web server for WAI applications{{< files text="show files" >}}* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/libHSwarp-3.3.31-D722qC70NKg6WEjEWreknu.a
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Buffer.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Buffer.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Conduit.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Conduit.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Counter.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Counter.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Date.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Date.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/FdCache.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/FdCache.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/File.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/File.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/FileInfoCache.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/FileInfoCache.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/HashMap.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/HashMap.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Header.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Header.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/HTTP1.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/HTTP1.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/HTTP2.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/HTTP2.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/HTTP2/File.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/HTTP2/File.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/HTTP2/PushPromise.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/HTTP2/PushPromise.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/HTTP2/Request.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/HTTP2/Request.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/HTTP2/Response.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/HTTP2/Response.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/HTTP2/Types.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/HTTP2/Types.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Imports.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Imports.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Internal.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Internal.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/IO.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/IO.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/MultiMap.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/MultiMap.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/PackInt.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/PackInt.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/ReadInt.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/ReadInt.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Request.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Request.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/RequestHeader.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/RequestHeader.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Response.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Response.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/ResponseHeader.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/ResponseHeader.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Run.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Run.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/SendFile.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/SendFile.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Settings.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Settings.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Types.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Types.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Windows.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/Windows.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/WithApplication.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Network/Wai/Handler/Warp/WithApplication.hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Paths_warp.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/warp-3.3.31/Paths_warp.hi
* /usr/lib/x86_64-linux-ghc-9.8.1/libHSwarp-3.3.31-D722qC70NKg6WEjEWreknu-ghc9.8.1.so
* /usr/share/doc/haskell-warp-3.3.31/LICENSE
* /usr/share/doc/haskell-warp-3.3.31/README.md
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-A.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-All.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-B.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-C.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-D.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-E.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-F.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-G.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-H.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-I.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-K.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-M.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-N.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-O.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-P.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-Q.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-R.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-S.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-T.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index-W.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/doc-index.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/haddock-bundle.min.js
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/index.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/linuwial.css
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/meta.json
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/Network-Wai-Handler-Warp-Internal.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/Network-Wai-Handler-Warp.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/quick-jump.css
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/synopsis.png
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/html/warp.haddock
* /usr/share/doc/x86_64-linux-ghc-9.8.1/warp-3.3.31/LICENSE
* /usr/share/haskell/haskell-warp/register.sh
* /usr/share/haskell/haskell-warp/unregister.sh
{{< /files >}}