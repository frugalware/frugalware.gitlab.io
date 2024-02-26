+++
draft = false
title = "nfs-utils 2.6.4-2"
version = "2.6.4-2"
description = "Support programs for Network File Systems"
date = "2024-01-07T16:53:44"
aliases = "/packages/3261"
categories = ['network']
upstreamurl = "https://sourceforge.net/projects/nfs-utils"
arch = "x86_64"
size = "339532"
usize = "1210088"
sha1sum = "624705853bde977b05a75cb84e7fff0627592bbf"
depends = "['keyutils', 'libevent>=2.1.11', 'lvm2-libs>=2.02.141', 'rpcbind', 'sqlite3>=3.10.2']"
reverse_depends = "['dracut-network']"
+++
Support programs for Network File Systems"

{{< files text="show files" >}}* /etc/exports
* /etc/request-key.d/id_resolver.conf
* /etc/sysconfig/nfs
* /usr/bin/blkmapd
* /usr/bin/exportfs
* /usr/bin/fsidd
* /usr/bin/mount.nfs
* /usr/bin/mount.nfs4
* /usr/bin/mountstats
* /usr/bin/nfsconf
* /usr/bin/nfsdcld
* /usr/bin/nfsdclddb
* /usr/bin/nfsdclnts
* /usr/bin/nfsdcltrack
* /usr/bin/nfsidmap
* /usr/bin/nfsiostat
* /usr/bin/nfsstat
* /usr/bin/rpc.idmapd
* /usr/bin/rpc.mountd
* /usr/bin/rpc.nfsd
* /usr/bin/rpc.statd
* /usr/bin/rpcctl
* /usr/bin/rpcdebug
* /usr/bin/showmount
* /usr/bin/sm-notify
* /usr/bin/start-statd
* /usr/bin/umount.nfs
* /usr/bin/umount.nfs4
* /usr/include/nfsidmap.h
* /usr/include/nfsidmap_plugin.h
* /usr/lib/libnfsidmap.so
* /usr/lib/libnfsidmap.so.1
* /usr/lib/libnfsidmap.so.1.0.0
* /usr/lib/libnfsidmap/nsswitch.so
* /usr/lib/libnfsidmap/regex.so
* /usr/lib/libnfsidmap/static.so
* /usr/lib/nfs-utils/nfsrahead
* /usr/lib/nfs/nfs-lock.preconfig
* /usr/lib/nfs/nfs-server.postconfig
* /usr/lib/nfs/nfs-server.preconfig
* /usr/lib/pkgconfig/libnfsidmap.pc
* /usr/lib/systemd/system-generators/nfs-server-generator
* /usr/lib/systemd/system-generators/rpc-pipefs-generator
* /usr/lib/systemd/system/fsidd.service
* /usr/lib/systemd/system/nfs-blkmap.service
* /usr/lib/systemd/system/nfs-client.target
* /usr/lib/systemd/system/nfs-idmap.service
* /usr/lib/systemd/system/nfs-idmapd.service
* /usr/lib/systemd/system/nfs-lock.service
* /usr/lib/systemd/system/nfs-mountd.service
* /usr/lib/systemd/system/nfs-rquotad.service
* /usr/lib/systemd/system/nfs-server.service
* /usr/lib/systemd/system/nfs-utils.service
* /usr/lib/systemd/system/nfs.target
* /usr/lib/systemd/system/nfsdcld.service
* /usr/lib/systemd/system/proc-fs-nfsd.mount
* /usr/lib/systemd/system/rpc-statd-notify.service
* /usr/lib/systemd/system/rpc-statd.service
* /usr/lib/systemd/system/rpc_pipefs.target
* /usr/lib/systemd/system/var-lib-nfs-rpc_pipefs.mount
* /usr/lib/udev/rules.d/60-nfs.rules
* /usr/lib/udev/rules.d/99-nfs.rules
* /usr/share/doc/nfs-utils-2.6.4/COPYING
* /usr/share/doc/nfs-utils-2.6.4/INSTALL
* /usr/share/doc/nfs-utils-2.6.4/NEWS
* /usr/share/doc/nfs-utils-2.6.4/README
* /usr/share/man/man3/nfs4_uid_to_name.3.gz
* /usr/share/man/man5/exports.5.gz
* /usr/share/man/man5/nfs.5.gz
* /usr/share/man/man5/nfs.conf.5.gz
* /usr/share/man/man5/nfsmount.conf.5.gz
* /usr/share/man/man5/nfsrahead.5.gz
* /usr/share/man/man7/nfs.systemd.7.gz
* /usr/share/man/man7/nfsd.7.gz
* /usr/share/man/man8/blkmapd.8.gz
* /usr/share/man/man8/exportfs.8.gz
* /usr/share/man/man8/idmapd.8.gz
* /usr/share/man/man8/mount.nfs.8.gz
* /usr/share/man/man8/mountd.8.gz
* /usr/share/man/man8/mountstats.8.gz
* /usr/share/man/man8/nfsconf.8.gz
* /usr/share/man/man8/nfsd.8.gz
* /usr/share/man/man8/nfsdcld.8.gz
* /usr/share/man/man8/nfsdclddb.8.gz
* /usr/share/man/man8/nfsdclnts.8.gz
* /usr/share/man/man8/nfsdcltrack.8.gz
* /usr/share/man/man8/nfsidmap.8.gz
* /usr/share/man/man8/nfsiostat.8.gz
* /usr/share/man/man8/nfsstat.8.gz
* /usr/share/man/man8/rpc.idmapd.8.gz
* /usr/share/man/man8/rpc.mountd.8.gz
* /usr/share/man/man8/rpc.nfsd.8.gz
* /usr/share/man/man8/rpc.sm-notify.8.gz
* /usr/share/man/man8/rpc.statd.8.gz
* /usr/share/man/man8/rpcctl.8.gz
* /usr/share/man/man8/rpcdebug.8.gz
* /usr/share/man/man8/showmount.8.gz
* /usr/share/man/man8/sm-notify.8.gz
* /usr/share/man/man8/statd.8.gz
* /usr/share/man/man8/umount.nfs.8.gz
* /var/lib/nfs/etab
* /var/lib/nfs/rmtab
* /var/lib/nfs/statd/state
{{< /files >}}