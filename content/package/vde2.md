+++
draft = false
title = "vde2 2.3.2-9"
version = "2.3.2-9"
description = "Emulates ethernet switches over existing connections."
date = "2024-01-10T20:45:20"
aliases = "/packages/23321"
categories = ['network-extra']
upstreamurl = "http://vde.sourceforge.net/"
arch = "x86_64"
size = "230940"
usize = "891770"
sha1sum = "b0ac910476c6402c50c937ccbbefbe47971c7662"
depends = "['glibc', 'libpcap', 'openssl>=3.1.0', 'python3']"
+++
Emulates ethernet switches over existing connections."

{{< files text="show files" >}}* /etc/vde2/libvdemgmt/asyncrecv.rc
* /etc/vde2/libvdemgmt/closemachine.rc
* /etc/vde2/libvdemgmt/openmachine.rc
* /etc/vde2/libvdemgmt/sendcmd.rc
* /etc/vde2/vdecmd
* /usr/bin/dpipe
* /usr/bin/slirpvde
* /usr/bin/unixcmd
* /usr/bin/unixterm
* /usr/bin/vdecmd
* /usr/bin/vdekvm
* /usr/bin/vdeq
* /usr/bin/vdeqemu
* /usr/bin/vdeterm
* /usr/bin/vde_autolink
* /usr/bin/vde_cryptcab
* /usr/bin/vde_l3
* /usr/bin/vde_over_ns
* /usr/bin/vde_pcapplug
* /usr/bin/vde_plug
* /usr/bin/vde_plug2tap
* /usr/bin/vde_router
* /usr/bin/vde_switch
* /usr/bin/vde_tunctl
* /usr/bin/vde_vxlan
* /usr/bin/wirefilter
* /usr/include/libvdehist.h
* /usr/include/libvdemgmt.h
* /usr/include/libvdeplug.h
* /usr/include/libvdeplug_dyn.h
* /usr/include/libvdesnmp.h
* /usr/lib/libvdehist.so
* /usr/lib/libvdehist.so.0
* /usr/lib/libvdehist.so.0.0.1
* /usr/lib/libvdemgmt.so
* /usr/lib/libvdemgmt.so.0
* /usr/lib/libvdemgmt.so.0.0.1
* /usr/lib/libvdeplug.so
* /usr/lib/libvdeplug.so.3
* /usr/lib/libvdeplug.so.3.0.1
* /usr/lib/libvdesnmp.so
* /usr/lib/libvdesnmp.so.0
* /usr/lib/libvdesnmp.so.0.0.1
* /usr/lib/pkgconfig/vdehist.pc
* /usr/lib/pkgconfig/vdemgmt.pc
* /usr/lib/pkgconfig/vdeplug.pc
* /usr/lib/pkgconfig/vdesnmp.pc
* /usr/lib/python3.12/site-packages/VdePlug.py
* /usr/lib/python3.12/site-packages/vdeplug_python.so
* /usr/lib/vde2/libvdetap.so
* /usr/lib/vde2/vdetap
* /usr/lib/vde2/vde_l3/bfifo.so
* /usr/lib/vde2/vde_l3/pfifo.so
* /usr/lib/vde2/vde_l3/tbf.so
* /usr/share/doc/vde2-2.3.2/Changelog
* /usr/share/doc/vde2-2.3.2/COPYING
* /usr/share/doc/vde2-2.3.2/COPYING.libvdeplug
* /usr/share/doc/vde2-2.3.2/COPYING.slirpvde
* /usr/share/doc/vde2-2.3.2/INSTALL
* /usr/share/doc/vde2-2.3.2/README
* /usr/share/man/man1/dpipe.1.gz
* /usr/share/man/man1/slirpvde.1.gz
* /usr/share/man/man1/unixcmd.1.gz
* /usr/share/man/man1/unixterm.1.gz
* /usr/share/man/man1/vdecmd.1.gz
* /usr/share/man/man1/vdekvm.1.gz
* /usr/share/man/man1/vdeq.1.gz
* /usr/share/man/man1/vdeqemu.1.gz
* /usr/share/man/man1/vdetaplib.1.gz
* /usr/share/man/man1/vdeterm.1.gz
* /usr/share/man/man1/vde_autolink.1.gz
* /usr/share/man/man1/vde_cryptcab.1.gz
* /usr/share/man/man1/vde_l3.1.gz
* /usr/share/man/man1/vde_over_ns.1.gz
* /usr/share/man/man1/vde_pcapplug.1.gz
* /usr/share/man/man1/vde_plug.1.gz
* /usr/share/man/man1/vde_plug2tap.1.gz
* /usr/share/man/man1/vde_router.1.gz
* /usr/share/man/man1/vde_switch.1.gz
* /usr/share/man/man1/vde_vxlan.1.gz
* /usr/share/man/man1/wirefilter.1.gz
* /usr/share/man/man8/vde_tunctl.8.gz
{{< /files >}}