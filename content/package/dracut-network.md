+++
draft = false
title = "dracut-network 059-4"
version = "059-4"
description = "Dracut modules to build a dracut initramfs with network support"
date = "2023-12-29T18:14:13"
aliases = "/packages/103624"
categories = ['base-extra']
upstreamurl = "https://github.com/dracutdevs/dracut"
arch = "x86_64"
size = "30516"
usize = "117599"
sha1sum = "ba32dfdf9b81a51c174041f1ebe8f24c6bbecf38"
depends = "['bridge-utils', 'dhclient', 'dracut=059', 'iproute2', 'iputils', 'iscsi', 'nfs-utils']"
+++
Dracut modules to build a dracut initramfs with network support{{< spoiler text="show files" >}}* /usr/lib/dracut/modules.d/40network/dhcp-root.sh
* /usr/lib/dracut/modules.d/40network/ifname-genrules.sh
* /usr/lib/dracut/modules.d/40network/module-setup.sh
* /usr/lib/dracut/modules.d/40network/net-lib.sh
* /usr/lib/dracut/modules.d/40network/netroot.sh
* /usr/lib/dracut/modules.d/45ifcfg/module-setup.sh
* /usr/lib/dracut/modules.d/45ifcfg/write-ifcfg.sh
* /usr/lib/dracut/modules.d/45url-lib/module-setup.sh
* /usr/lib/dracut/modules.d/45url-lib/url-lib.sh
* /usr/lib/dracut/modules.d/90dmsquash-live-ntfs/module-setup.sh
* /usr/lib/dracut/modules.d/90dmsquash-live-ntfs/mount-ntfs-3g.sh
* /usr/lib/dracut/modules.d/90kernel-network-modules/module-setup.sh
* /usr/lib/dracut/modules.d/90livenet/fetch-liveupdate.sh
* /usr/lib/dracut/modules.d/90livenet/livenet-generator.sh
* /usr/lib/dracut/modules.d/90livenet/livenetroot.sh
* /usr/lib/dracut/modules.d/90livenet/module-setup.sh
* /usr/lib/dracut/modules.d/90livenet/parse-livenet.sh
* /usr/lib/dracut/modules.d/90qemu-net/module-setup.sh
* /usr/lib/dracut/modules.d/95cifs/cifs-lib.sh
* /usr/lib/dracut/modules.d/95cifs/cifsroot.sh
* /usr/lib/dracut/modules.d/95cifs/module-setup.sh
* /usr/lib/dracut/modules.d/95cifs/parse-cifsroot.sh
* /usr/lib/dracut/modules.d/95iscsi/cleanup-iscsi.sh
* /usr/lib/dracut/modules.d/95iscsi/iscsiroot.sh
* /usr/lib/dracut/modules.d/95iscsi/module-setup.sh
* /usr/lib/dracut/modules.d/95iscsi/mount-lun.sh
* /usr/lib/dracut/modules.d/95iscsi/parse-iscsiroot.sh
* /usr/lib/dracut/modules.d/95nbd/module-setup.sh
* /usr/lib/dracut/modules.d/95nbd/nbd-generator.sh
* /usr/lib/dracut/modules.d/95nbd/nbdroot.sh
* /usr/lib/dracut/modules.d/95nbd/parse-nbdroot.sh
* /usr/lib/dracut/modules.d/95nfs/module-setup.sh
* /usr/lib/dracut/modules.d/95nfs/nfs-lib.sh
* /usr/lib/dracut/modules.d/95nfs/nfs-start-rpc.sh
* /usr/lib/dracut/modules.d/95nfs/nfsroot-cleanup.sh
* /usr/lib/dracut/modules.d/95nfs/nfsroot.sh
* /usr/lib/dracut/modules.d/95nfs/parse-nfsroot.sh
* /usr/lib/dracut/modules.d/95ssh-client/module-setup.sh
{{< /spoiler >}}