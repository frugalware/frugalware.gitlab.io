+++
draft = false
title = "haskell-http2 5.0.0-1"
version = "5.0.0-1"
description = "HTTP/2 library"
date = "2023-12-13T10:53:25"
aliases = "/packages/220712"
categories = ['devel-extra']
upstreamurl = "http://hackage.haskell.org/cgi-bin/hackage-scripts/package/http2"
arch = "x86_64"
size = "1021020"
usize = "11864100"
sha1sum = "09b1cccae72809fd2d8838235f147f9e674b67a9"
depends = "['haskell-http-types', 'haskell-network', 'haskell-network-byte-order', 'haskell-network-control', 'haskell-time-manager']"
reverse_depends = "['haskell-warp']"
+++
HTTP/2 library{{< spoiler text="show files" >}}* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Imports.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Imports.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/libHShttp2-5.0.0-CU2TdgpCBx9FFSLcCkWWs0.a
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Builder.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Builder.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/HeaderBlock.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/HeaderBlock.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/HeaderBlock/Decode.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/HeaderBlock/Decode.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/HeaderBlock/Encode.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/HeaderBlock/Encode.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/HeaderBlock/Integer.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/HeaderBlock/Integer.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Huffman.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Huffman.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Huffman/Bit.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Huffman/Bit.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Huffman/ByteString.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Huffman/ByteString.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Huffman/Decode.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Huffman/Decode.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Huffman/Encode.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Huffman/Encode.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Huffman/Params.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Huffman/Params.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Huffman/Table.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Huffman/Table.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Huffman/Tree.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Huffman/Tree.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Internal.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Internal.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Table.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Table.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Table/Dynamic.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Table/Dynamic.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Table/Entry.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Table/Entry.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Table/RevIndex.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Table/RevIndex.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Table/Static.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Table/Static.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Token.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Token.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Types.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HPACK/Types.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Client.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Client.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Client/Internal.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Client/Internal.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Client/Run.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Client/Run.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Client/Types.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Client/Types.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Frame.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Frame.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Frame/Decode.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Frame/Decode.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Frame/Encode.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Frame/Encode.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Frame/Types.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Frame/Types.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Config.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Config.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Context.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Context.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/EncodeFrame.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/EncodeFrame.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/File.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/File.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/HPACK.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/HPACK.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Manager.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Manager.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Queue.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Queue.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/ReadN.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/ReadN.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Receiver.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Receiver.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Sender.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Sender.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Settings.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Settings.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Status.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Status.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Stream.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Stream.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/StreamTable.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/StreamTable.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Types.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Types.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Window.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/H2/Window.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Internal.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Internal.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Server.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Server.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Server/Internal.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Server/Internal.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Server/Run.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Server/Run.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Server/Types.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Server/Types.hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Server/Worker.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/http2-5.0.0/Network/HTTP2/Server/Worker.hi
* /usr/lib/x86_64-linux-ghc-9.8.1/libHShttp2-5.0.0-CU2TdgpCBx9FFSLcCkWWs0-ghc9.8.1.so
* /usr/share/doc/haskell-http2-5.0.0/LICENSE
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-A.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-All.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-B.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-C.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-D.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-E.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-F.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-G.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-H.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-I.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-K.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-L.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-M.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-N.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-O.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-P.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-R.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-S.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-T.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-U.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-V.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index-W.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/doc-index.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/haddock-bundle.min.js
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/http2.haddock
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/index.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/linuwial.css
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/meta.json
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/Network-HPACK-Internal.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/Network-HPACK-Token.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/Network-HPACK.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/Network-HTTP2-Client-Internal.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/Network-HTTP2-Client.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/Network-HTTP2-Frame.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/Network-HTTP2-Internal.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/Network-HTTP2-Server-Internal.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/Network-HTTP2-Server.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/quick-jump.css
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/html/synopsis.png
* /usr/share/doc/x86_64-linux-ghc-9.8.1/http2-5.0.0/LICENSE
* /usr/share/haskell/haskell-http2/register.sh
* /usr/share/haskell/haskell-http2/unregister.sh
{{< /spoiler >}}