+++
draft = false
title = "haskell-vector 0.13.1.0-1"
version = "0.13.1.0-1"
description = "Efficient Arrays"
date = "2023-12-11T14:15:42"
aliases = "/packages/219757"
categories = ['devel-extra']
upstreamurl = "http://hackage.haskell.org/cgi-bin/hackage-scripts/package/vector"
arch = "x86_64"
size = "2218756"
usize = "33799817"
sha1sum = "f3ba3ac1b37794f05ad55e1d86e84d94f610976d"
depends = "['haskell-primitive>=0.3.7.0-2', 'haskell-vector-stream']"
reverse_depends = "['haskell-bitvec', 'haskell-cassava', 'haskell-indexed-traversable-instances', 'haskell-juicypixels', 'haskell-th-lift-instances']"
+++
Efficient Arrays{{< spoiler text="show files" >}}* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Fusion/Bundle.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Fusion/Bundle.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Fusion/Bundle/Monadic.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Fusion/Bundle/Monadic.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Fusion/Bundle/Size.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Fusion/Bundle/Size.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Fusion/Stream/Monadic.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Fusion/Stream/Monadic.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Fusion/Util.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Fusion/Util.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Generic.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Generic.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Generic/Base.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Generic/Base.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Generic/Mutable.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Generic/Mutable.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Generic/Mutable/Base.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Generic/Mutable/Base.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Generic/New.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Generic/New.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Internal/Check.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Internal/Check.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Mutable.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Mutable.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Primitive.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Primitive.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Primitive/Mutable.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Primitive/Mutable.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Storable.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Storable.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Storable/Internal.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Storable/Internal.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Storable/Mutable.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Storable/Mutable.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Unboxed.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Unboxed.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Unboxed/Base.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Unboxed/Base.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Unboxed/Mutable.dyn_hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/Data/Vector/Unboxed/Mutable.hi
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/include/vector.h
* /usr/lib/ghc-9.8.1/site-local/vector-0.13.1.0/libHSvector-0.13.1.0-7ginsveWhitTP1jS2d5Q5.a
* /usr/lib/x86_64-linux-ghc-9.8.1/libHSvector-0.13.1.0-7ginsveWhitTP1jS2d5Q5-ghc9.8.1.so
* /usr/share/doc/haskell-vector-0.13.1.0/LICENSE
* /usr/share/doc/haskell-vector-0.13.1.0/README.md
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/Data-Vector-Fusion-Bundle-Monadic.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/Data-Vector-Fusion-Bundle-Size.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/Data-Vector-Fusion-Bundle.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/Data-Vector-Fusion-Stream-Monadic.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/Data-Vector-Fusion-Util.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/Data-Vector-Generic-Mutable-Base.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/Data-Vector-Generic-Mutable.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/Data-Vector-Generic-New.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/Data-Vector-Generic.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/Data-Vector-Mutable.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/Data-Vector-Primitive-Mutable.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/Data-Vector-Primitive.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/Data-Vector-Storable-Mutable.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/Data-Vector-Storable.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/Data-Vector-Unboxed-Mutable.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/Data-Vector-Unboxed.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/Data-Vector.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-33.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-43.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-47.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-A.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-All.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-B.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-C.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-D.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-E.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-F.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-G.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-H.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-I.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-L.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-M.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-N.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-O.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-P.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-R.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-S.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-T.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-U.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-V.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-W.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-Y.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index-Z.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/doc-index.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/haddock-bundle.min.js
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/index.html
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/linuwial.css
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/meta.json
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/quick-jump.css
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/synopsis.png
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/html/vector.haddock
* /usr/share/doc/x86_64-linux-ghc-9.8.1/vector-0.13.1.0/LICENSE
* /usr/share/haskell/haskell-vector/register.sh
* /usr/share/haskell/haskell-vector/unregister.sh
{{< /spoiler >}}