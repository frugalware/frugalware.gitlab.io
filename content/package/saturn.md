+++
draft = false
title = "saturn 0.4.1-2"
version = "0.4.1-2"
description = "Lock-free data structures for multicore OCaml"
date = "2023-12-19T13:20:54"
aliases = "/packages/221060"
categories = ['devel-extra']
upstreamurl = "https://github.com/ocaml-multicore/saturn"
arch = "x86_64"
size = "291220"
usize = "631471"
sha1sum = "f1f85319eb24f39952a73ed9e4f79d77bdfde06d"
depends = "['ocaml-domain-shims']"
reverse_depends = "['domainslib']"
+++
Lock-free data structures for multicore OCaml{{< spoiler text="show files" >}}* /usr/lib/ocaml/saturn/dune-package
* /usr/lib/ocaml/saturn/META
* /usr/lib/ocaml/saturn/mpmc_relaxed_queue.ml
* /usr/lib/ocaml/saturn/mpmc_relaxed_queue.mli
* /usr/lib/ocaml/saturn/opam
* /usr/lib/ocaml/saturn/saturn.a
* /usr/lib/ocaml/saturn/saturn.cma
* /usr/lib/ocaml/saturn/saturn.cmi
* /usr/lib/ocaml/saturn/saturn.cmt
* /usr/lib/ocaml/saturn/saturn.cmti
* /usr/lib/ocaml/saturn/saturn.cmx
* /usr/lib/ocaml/saturn/saturn.cmxa
* /usr/lib/ocaml/saturn/saturn.cmxs
* /usr/lib/ocaml/saturn/saturn.ml
* /usr/lib/ocaml/saturn/saturn.mli
* /usr/lib/ocaml/saturn/saturn__.cmi
* /usr/lib/ocaml/saturn/saturn__.cmt
* /usr/lib/ocaml/saturn/saturn__.cmx
* /usr/lib/ocaml/saturn/saturn__.ml
* /usr/lib/ocaml/saturn/saturn__Mpmc_relaxed_queue.cmi
* /usr/lib/ocaml/saturn/saturn__Mpmc_relaxed_queue.cmt
* /usr/lib/ocaml/saturn/saturn__Mpmc_relaxed_queue.cmti
* /usr/lib/ocaml/saturn/saturn__Mpmc_relaxed_queue.cmx
* /usr/lib/ocaml/saturn_lockfree/ArrayExtra.ml
* /usr/lib/ocaml/saturn_lockfree/backoff.ml
* /usr/lib/ocaml/saturn_lockfree/backoff.mli
* /usr/lib/ocaml/saturn_lockfree/dune-package
* /usr/lib/ocaml/saturn_lockfree/META
* /usr/lib/ocaml/saturn_lockfree/michael_scott_queue.ml
* /usr/lib/ocaml/saturn_lockfree/michael_scott_queue.mli
* /usr/lib/ocaml/saturn_lockfree/mpmc_relaxed_queue.ml
* /usr/lib/ocaml/saturn_lockfree/mpmc_relaxed_queue.mli
* /usr/lib/ocaml/saturn_lockfree/mpsc_queue.ml
* /usr/lib/ocaml/saturn_lockfree/mpsc_queue.mli
* /usr/lib/ocaml/saturn_lockfree/opam
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree.a
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree.cma
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree.cmti
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree.cmxa
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree.cmxs
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree.ml
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree.mli
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__.ml
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__ArrayExtra.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__ArrayExtra.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__ArrayExtra.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Backoff.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Backoff.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Backoff.cmti
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Backoff.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Michael_scott_queue.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Michael_scott_queue.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Michael_scott_queue.cmti
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Michael_scott_queue.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Mpmc_relaxed_queue.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Mpmc_relaxed_queue.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Mpmc_relaxed_queue.cmti
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Mpmc_relaxed_queue.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Mpsc_queue.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Mpsc_queue.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Mpsc_queue.cmti
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Mpsc_queue.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Spsc_queue.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Spsc_queue.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Spsc_queue.cmti
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Spsc_queue.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Treiber_stack.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Treiber_stack.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Treiber_stack.cmti
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Treiber_stack.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Ws_deque.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Ws_deque.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Ws_deque.cmti
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Ws_deque.cmx
* /usr/lib/ocaml/saturn_lockfree/spsc_queue.ml
* /usr/lib/ocaml/saturn_lockfree/spsc_queue.mli
* /usr/lib/ocaml/saturn_lockfree/treiber_stack.ml
* /usr/lib/ocaml/saturn_lockfree/treiber_stack.mli
* /usr/lib/ocaml/saturn_lockfree/ws_deque.ml
* /usr/lib/ocaml/saturn_lockfree/ws_deque.mli
* /usr/share/doc/saturn-0.4.1/README.md
* /usr/share/doc/saturn-0.4.1/saturn/CHANGES.md
* /usr/share/doc/saturn-0.4.1/saturn/LICENSE.md
* /usr/share/doc/saturn-0.4.1/saturn/README.md
* /usr/share/doc/saturn-0.4.1/saturn_lockfree/CHANGES.md
* /usr/share/doc/saturn-0.4.1/saturn_lockfree/LICENSE.md
* /usr/share/doc/saturn-0.4.1/saturn_lockfree/README.md
{{< /spoiler >}}