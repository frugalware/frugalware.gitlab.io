+++
draft = false
title = "saturn 0.5.0-1"
version = "0.5.0-1"
description = "Lock-free data structures for multicore OCaml"
date = "2024-10-21T14:34:00"
aliases = "/packages/221060"
categories = ['devel-extra']
upstreamurl = "https://github.com/ocaml-multicore/saturn"
arch = "x86_64"
size = "554344"
usize = "1094151"
sha1sum = "b4ec2933eb93a26049ea5d0dd4f2e95279566182"
depends = "['backoff', 'multicore-magic', 'ocaml-domain-shims']"
reverse_depends = "['domainslib']"
+++
### Description: 
Lock-free data structures for multicore OCaml

### Files: 
* /usr/lib/ocaml/saturn/dune-package
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
* /usr/lib/ocaml/saturn_lockfree/dune-package
* /usr/lib/ocaml/saturn_lockfree/META
* /usr/lib/ocaml/saturn_lockfree/michael_scott_queue.ml
* /usr/lib/ocaml/saturn_lockfree/michael_scott_queue.mli
* /usr/lib/ocaml/saturn_lockfree/michael_scott_queue_intf.ml
* /usr/lib/ocaml/saturn_lockfree/michael_scott_queue_unsafe.ml
* /usr/lib/ocaml/saturn_lockfree/michael_scott_queue_unsafe.mli
* /usr/lib/ocaml/saturn_lockfree/michael_scott_queue_unsafe_node.ml
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
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Michael_scott_queue.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Michael_scott_queue.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Michael_scott_queue.cmti
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Michael_scott_queue.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Michael_scott_queue_intf.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Michael_scott_queue_intf.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Michael_scott_queue_intf.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Michael_scott_queue_unsafe.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Michael_scott_queue_unsafe.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Michael_scott_queue_unsafe.cmti
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Michael_scott_queue_unsafe.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Michael_scott_queue_unsafe_node.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Michael_scott_queue_unsafe_node.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Michael_scott_queue_unsafe_node.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Mpmc_relaxed_queue.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Mpmc_relaxed_queue.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Mpmc_relaxed_queue.cmti
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Mpmc_relaxed_queue.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Mpsc_queue.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Mpsc_queue.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Mpsc_queue.cmti
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Mpsc_queue.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Size.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Size.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Size.cmti
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Size.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Skiplist.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Skiplist.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Skiplist.cmti
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Skiplist.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Spsc_queue.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Spsc_queue.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Spsc_queue.cmti
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Spsc_queue.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Spsc_queue_intf.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Spsc_queue_intf.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Spsc_queue_intf.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Spsc_queue_unsafe.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Spsc_queue_unsafe.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Spsc_queue_unsafe.cmti
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Spsc_queue_unsafe.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Treiber_stack.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Treiber_stack.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Treiber_stack.cmti
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Treiber_stack.cmx
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Ws_deque.cmi
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Ws_deque.cmt
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Ws_deque.cmti
* /usr/lib/ocaml/saturn_lockfree/saturn_lockfree__Ws_deque.cmx
* /usr/lib/ocaml/saturn_lockfree/size.ml
* /usr/lib/ocaml/saturn_lockfree/size.mli
* /usr/lib/ocaml/saturn_lockfree/skiplist.ml
* /usr/lib/ocaml/saturn_lockfree/skiplist.mli
* /usr/lib/ocaml/saturn_lockfree/spsc_queue.ml
* /usr/lib/ocaml/saturn_lockfree/spsc_queue.mli
* /usr/lib/ocaml/saturn_lockfree/spsc_queue_intf.ml
* /usr/lib/ocaml/saturn_lockfree/spsc_queue_unsafe.ml
* /usr/lib/ocaml/saturn_lockfree/spsc_queue_unsafe.mli
* /usr/lib/ocaml/saturn_lockfree/treiber_stack.ml
* /usr/lib/ocaml/saturn_lockfree/treiber_stack.mli
* /usr/lib/ocaml/saturn_lockfree/ws_deque.ml
* /usr/lib/ocaml/saturn_lockfree/ws_deque.mli
* /usr/lib/ocaml/saturn_lockfree/__private__/linked_set/.public_cmi/linked_set.cmi
* /usr/lib/ocaml/saturn_lockfree/__private__/linked_set/.public_cmi/linked_set.cmt
* /usr/lib/ocaml/saturn_lockfree/__private__/linked_set/linked_set.a
* /usr/lib/ocaml/saturn_lockfree/__private__/linked_set/linked_set.cma
* /usr/lib/ocaml/saturn_lockfree/__private__/linked_set/linked_set.cmx
* /usr/lib/ocaml/saturn_lockfree/__private__/linked_set/linked_set.cmxa
* /usr/lib/ocaml/saturn_lockfree/__private__/linked_set/linked_set.cmxs
* /usr/lib/ocaml/saturn_lockfree/__private__/linked_set/linked_set.ml
* /usr/share/doc/saturn-0.5.0/README.md
* /usr/share/doc/saturn-0.5.0/saturn/CHANGES.md
* /usr/share/doc/saturn-0.5.0/saturn/LICENSE.md
* /usr/share/doc/saturn-0.5.0/saturn/README.md
* /usr/share/doc/saturn-0.5.0/saturn_lockfree/CHANGES.md
* /usr/share/doc/saturn-0.5.0/saturn_lockfree/LICENSE.md
* /usr/share/doc/saturn-0.5.0/saturn_lockfree/README.md
