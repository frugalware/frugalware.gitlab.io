+++
draft = false
title = "saturn 1.0.0-1"
version = "1.0.0-1"
description = "Lock-free data structures for multicore OCaml"
date = "2025-01-18T14:21:39"
aliases = "/packages/221060"
categories = ['devel-extra']
upstreamurl = "https://github.com/ocaml-multicore/saturn"
arch = "x86_64"
size = "1163544"
usize = "2124696"
sha1sum = "f191290eff8112cfc219de197f33fec61a3eb90a"
depends = "['backoff', 'multicore-magic', 'ocaml-domain-shims']"
reverse_depends = "['domainslib']"
+++
### Description: 
Lock-free data structures for multicore OCaml

### Files: 
* /usr/lib/ocaml/saturn/ArrayExtra.ml
* /usr/lib/ocaml/saturn/bag.ml
* /usr/lib/ocaml/saturn/bag.mli
* /usr/lib/ocaml/saturn/bounded_queue/bounded_queue.ml
* /usr/lib/ocaml/saturn/bounded_queue/bounded_queue.mli
* /usr/lib/ocaml/saturn/bounded_queue/bounded_queue_intf.mli
* /usr/lib/ocaml/saturn/bounded_queue/bounded_queue_unsafe.ml
* /usr/lib/ocaml/saturn/bounded_queue/bounded_queue_unsafe.mli
* /usr/lib/ocaml/saturn/bounded_stack.ml
* /usr/lib/ocaml/saturn/bounded_stack.mli
* /usr/lib/ocaml/saturn/dune-package
* /usr/lib/ocaml/saturn/htbl/htbl.ml
* /usr/lib/ocaml/saturn/htbl/htbl.mli
* /usr/lib/ocaml/saturn/htbl/htbl_intf.mli
* /usr/lib/ocaml/saturn/htbl/htbl_unsafe.ml
* /usr/lib/ocaml/saturn/htbl/htbl_unsafe.mli
* /usr/lib/ocaml/saturn/htbl/htbl_utils.ml
* /usr/lib/ocaml/saturn/META
* /usr/lib/ocaml/saturn/michael_scott_queue/michael_scott_queue.ml
* /usr/lib/ocaml/saturn/michael_scott_queue/michael_scott_queue.mli
* /usr/lib/ocaml/saturn/michael_scott_queue/michael_scott_queue_intf.mli
* /usr/lib/ocaml/saturn/michael_scott_queue/michael_scott_queue_unsafe.ml
* /usr/lib/ocaml/saturn/michael_scott_queue/michael_scott_queue_unsafe.mli
* /usr/lib/ocaml/saturn/michael_scott_queue/michael_scott_queue_unsafe_node.ml
* /usr/lib/ocaml/saturn/mpsc_queue.ml
* /usr/lib/ocaml/saturn/mpsc_queue.mli
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
* /usr/lib/ocaml/saturn/saturn__ArrayExtra.cmi
* /usr/lib/ocaml/saturn/saturn__ArrayExtra.cmt
* /usr/lib/ocaml/saturn/saturn__ArrayExtra.cmx
* /usr/lib/ocaml/saturn/saturn__Bag.cmi
* /usr/lib/ocaml/saturn/saturn__Bag.cmt
* /usr/lib/ocaml/saturn/saturn__Bag.cmti
* /usr/lib/ocaml/saturn/saturn__Bag.cmx
* /usr/lib/ocaml/saturn/saturn__Bounded_queue.cmi
* /usr/lib/ocaml/saturn/saturn__Bounded_queue.cmt
* /usr/lib/ocaml/saturn/saturn__Bounded_queue.cmti
* /usr/lib/ocaml/saturn/saturn__Bounded_queue.cmx
* /usr/lib/ocaml/saturn/saturn__Bounded_queue_intf.cmi
* /usr/lib/ocaml/saturn/saturn__Bounded_queue_intf.cmti
* /usr/lib/ocaml/saturn/saturn__Bounded_queue_unsafe.cmi
* /usr/lib/ocaml/saturn/saturn__Bounded_queue_unsafe.cmt
* /usr/lib/ocaml/saturn/saturn__Bounded_queue_unsafe.cmti
* /usr/lib/ocaml/saturn/saturn__Bounded_queue_unsafe.cmx
* /usr/lib/ocaml/saturn/saturn__Bounded_stack.cmi
* /usr/lib/ocaml/saturn/saturn__Bounded_stack.cmt
* /usr/lib/ocaml/saturn/saturn__Bounded_stack.cmti
* /usr/lib/ocaml/saturn/saturn__Bounded_stack.cmx
* /usr/lib/ocaml/saturn/saturn__Htbl.cmi
* /usr/lib/ocaml/saturn/saturn__Htbl.cmt
* /usr/lib/ocaml/saturn/saturn__Htbl.cmti
* /usr/lib/ocaml/saturn/saturn__Htbl.cmx
* /usr/lib/ocaml/saturn/saturn__Htbl_intf.cmi
* /usr/lib/ocaml/saturn/saturn__Htbl_intf.cmti
* /usr/lib/ocaml/saturn/saturn__Htbl_unsafe.cmi
* /usr/lib/ocaml/saturn/saturn__Htbl_unsafe.cmt
* /usr/lib/ocaml/saturn/saturn__Htbl_unsafe.cmti
* /usr/lib/ocaml/saturn/saturn__Htbl_unsafe.cmx
* /usr/lib/ocaml/saturn/saturn__Htbl_utils.cmi
* /usr/lib/ocaml/saturn/saturn__Htbl_utils.cmt
* /usr/lib/ocaml/saturn/saturn__Htbl_utils.cmx
* /usr/lib/ocaml/saturn/saturn__Michael_scott_queue.cmi
* /usr/lib/ocaml/saturn/saturn__Michael_scott_queue.cmt
* /usr/lib/ocaml/saturn/saturn__Michael_scott_queue.cmti
* /usr/lib/ocaml/saturn/saturn__Michael_scott_queue.cmx
* /usr/lib/ocaml/saturn/saturn__Michael_scott_queue_intf.cmi
* /usr/lib/ocaml/saturn/saturn__Michael_scott_queue_intf.cmti
* /usr/lib/ocaml/saturn/saturn__Michael_scott_queue_unsafe.cmi
* /usr/lib/ocaml/saturn/saturn__Michael_scott_queue_unsafe.cmt
* /usr/lib/ocaml/saturn/saturn__Michael_scott_queue_unsafe.cmti
* /usr/lib/ocaml/saturn/saturn__Michael_scott_queue_unsafe.cmx
* /usr/lib/ocaml/saturn/saturn__Michael_scott_queue_unsafe_node.cmi
* /usr/lib/ocaml/saturn/saturn__Michael_scott_queue_unsafe_node.cmt
* /usr/lib/ocaml/saturn/saturn__Michael_scott_queue_unsafe_node.cmx
* /usr/lib/ocaml/saturn/saturn__Mpsc_queue.cmi
* /usr/lib/ocaml/saturn/saturn__Mpsc_queue.cmt
* /usr/lib/ocaml/saturn/saturn__Mpsc_queue.cmti
* /usr/lib/ocaml/saturn/saturn__Mpsc_queue.cmx
* /usr/lib/ocaml/saturn/saturn__Size.cmi
* /usr/lib/ocaml/saturn/saturn__Size.cmt
* /usr/lib/ocaml/saturn/saturn__Size.cmti
* /usr/lib/ocaml/saturn/saturn__Size.cmx
* /usr/lib/ocaml/saturn/saturn__Skiplist.cmi
* /usr/lib/ocaml/saturn/saturn__Skiplist.cmt
* /usr/lib/ocaml/saturn/saturn__Skiplist.cmti
* /usr/lib/ocaml/saturn/saturn__Skiplist.cmx
* /usr/lib/ocaml/saturn/saturn__Spsc_queue.cmi
* /usr/lib/ocaml/saturn/saturn__Spsc_queue.cmt
* /usr/lib/ocaml/saturn/saturn__Spsc_queue.cmti
* /usr/lib/ocaml/saturn/saturn__Spsc_queue.cmx
* /usr/lib/ocaml/saturn/saturn__Spsc_queue_intf.cmi
* /usr/lib/ocaml/saturn/saturn__Spsc_queue_intf.cmti
* /usr/lib/ocaml/saturn/saturn__Spsc_queue_unsafe.cmi
* /usr/lib/ocaml/saturn/saturn__Spsc_queue_unsafe.cmt
* /usr/lib/ocaml/saturn/saturn__Spsc_queue_unsafe.cmti
* /usr/lib/ocaml/saturn/saturn__Spsc_queue_unsafe.cmx
* /usr/lib/ocaml/saturn/saturn__Treiber_stack.cmi
* /usr/lib/ocaml/saturn/saturn__Treiber_stack.cmt
* /usr/lib/ocaml/saturn/saturn__Treiber_stack.cmti
* /usr/lib/ocaml/saturn/saturn__Treiber_stack.cmx
* /usr/lib/ocaml/saturn/saturn__Ws_deque.cmi
* /usr/lib/ocaml/saturn/saturn__Ws_deque.cmt
* /usr/lib/ocaml/saturn/saturn__Ws_deque.cmti
* /usr/lib/ocaml/saturn/saturn__Ws_deque.cmx
* /usr/lib/ocaml/saturn/size.ml
* /usr/lib/ocaml/saturn/size.mli
* /usr/lib/ocaml/saturn/skiplist.ml
* /usr/lib/ocaml/saturn/skiplist.mli
* /usr/lib/ocaml/saturn/spsc_queue/spsc_queue.ml
* /usr/lib/ocaml/saturn/spsc_queue/spsc_queue.mli
* /usr/lib/ocaml/saturn/spsc_queue/spsc_queue_intf.mli
* /usr/lib/ocaml/saturn/spsc_queue/spsc_queue_unsafe.ml
* /usr/lib/ocaml/saturn/spsc_queue/spsc_queue_unsafe.mli
* /usr/lib/ocaml/saturn/treiber_stack.ml
* /usr/lib/ocaml/saturn/treiber_stack.mli
* /usr/lib/ocaml/saturn/ws_deque.ml
* /usr/lib/ocaml/saturn/ws_deque.mli
* /usr/lib/ocaml/saturn/__private__/linked_set/.public_cmi/linked_set.cmi
* /usr/lib/ocaml/saturn/__private__/linked_set/.public_cmi/linked_set.cmt
* /usr/lib/ocaml/saturn/__private__/linked_set/linked_set.a
* /usr/lib/ocaml/saturn/__private__/linked_set/linked_set.cma
* /usr/lib/ocaml/saturn/__private__/linked_set/linked_set.cmx
* /usr/lib/ocaml/saturn/__private__/linked_set/linked_set.cmxa
* /usr/lib/ocaml/saturn/__private__/linked_set/linked_set.cmxs
* /usr/lib/ocaml/saturn/__private__/linked_set/linked_set.ml
* /usr/share/doc/saturn-1.0.0/README.md
* /usr/share/doc/saturn-1.0.0/saturn/CHANGES.md
* /usr/share/doc/saturn-1.0.0/saturn/LICENSE.md
* /usr/share/doc/saturn-1.0.0/saturn/README.md
