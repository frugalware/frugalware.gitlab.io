+++
draft = false
title = "nfs-utils 2.6.3-1"
version = "2.6.3-1"
date = "2023-04-25T07:33:51"
categories = ['network']
upstreamurl = "https://sourceforge.net/projects/nfs"
arch = "x86_64"
size = "333032"
usize = "1158085"
sha1sum = "77a2a794072abf1c6d3f7764e381c3a7245da712"
depends = "['rpcbind', 'sqlite3>=3.10.2', 'lvm2-libs>=2.02.141', 'libevent>=2.1.11', 'keyutils']"
files = "['etc/', 'etc/exports', 'etc/exports.d/', 'etc/request-key.d/', 'etc/request-key.d/id_resolver.conf', 'etc/sysconfig/', 'etc/sysconfig/nfs', 'lib/', 'lib/systemd/', 'lib/systemd/system/', 'lib/systemd/system/nfs-blkmap.service', 'lib/systemd/system/nfs-idmap.service', 'lib/systemd/system/nfs-lock.service', 'lib/systemd/system/nfs-mountd.service', 'lib/systemd/system/nfs-rquotad.service', 'lib/systemd/system/nfs-server.service', 'lib/systemd/system/nfs.target', 'lib/systemd/system/proc-fs-nfsd.mount', 'lib/systemd/system/var-lib-nfs-rpc_pipefs.mount', 'sbin/', 'sbin/mount.nfs', 'sbin/mount.nfs4', 'sbin/nfsdcltrack', 'sbin/umount.nfs', 'sbin/umount.nfs4', 'usr/', 'usr/include/', 'usr/include/nfsidmap.h', 'usr/include/nfsidmap_plugin.h', 'usr/lib/', 'usr/lib/libnfsidmap.so', 'usr/lib/libnfsidmap.so.1', 'usr/lib/libnfsidmap.so.1.0.0', 'usr/lib/libnfsidmap/', 'usr/lib/libnfsidmap/nsswitch.so', 'usr/lib/libnfsidmap/regex.so', 'usr/lib/libnfsidmap/static.so', 'usr/lib/nfs-utils/', 'usr/lib/nfs-utils/nfsrahead', 'usr/lib/nfs/', 'usr/lib/nfs/nfs-lock.preconfig', 'usr/lib/nfs/nfs-server.postconfig', 'usr/lib/nfs/nfs-server.preconfig', 'usr/lib/pkgconfig/', 'usr/lib/pkgconfig/libnfsidmap.pc', 'usr/lib/udev/', 'usr/lib/udev/rules.d/', 'usr/lib/udev/rules.d/99-nfs.rules', 'usr/sbin/', 'usr/sbin/blkmapd', 'usr/sbin/exportfs', 'usr/sbin/fsidd', 'usr/sbin/mountstats', 'usr/sbin/nfsconf', 'usr/sbin/nfsdcld', 'usr/sbin/nfsdclddb', 'usr/sbin/nfsdclnts', 'usr/sbin/nfsidmap', 'usr/sbin/nfsiostat', 'usr/sbin/nfsstat', 'usr/sbin/rpc.idmapd', 'usr/sbin/rpc.mountd', 'usr/sbin/rpc.nfsd', 'usr/sbin/rpc.statd', 'usr/sbin/rpcctl', 'usr/sbin/rpcdebug', 'usr/sbin/showmount', 'usr/sbin/sm-notify', 'usr/sbin/start-statd', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/nfs-utils-2.6.3/', 'usr/share/doc/nfs-utils-2.6.3/COPYING', 'usr/share/doc/nfs-utils-2.6.3/INSTALL', 'usr/share/doc/nfs-utils-2.6.3/NEWS', 'usr/share/doc/nfs-utils-2.6.3/README', 'usr/share/man/', 'usr/share/man/man3/', 'usr/share/man/man3/nfs4_uid_to_name.3.gz', 'usr/share/man/man5/', 'usr/share/man/man5/exports.5.gz', 'usr/share/man/man5/nfs.5.gz', 'usr/share/man/man5/nfs.conf.5.gz', 'usr/share/man/man5/nfsmount.conf.5.gz', 'usr/share/man/man5/nfsrahead.5.gz', 'usr/share/man/man7/', 'usr/share/man/man7/nfs.systemd.7.gz', 'usr/share/man/man7/nfsd.7.gz', 'usr/share/man/man8/', 'usr/share/man/man8/blkmapd.8.gz', 'usr/share/man/man8/exportfs.8.gz', 'usr/share/man/man8/idmapd.8.gz', 'usr/share/man/man8/mount.nfs.8.gz', 'usr/share/man/man8/mountd.8.gz', 'usr/share/man/man8/mountstats.8.gz', 'usr/share/man/man8/nfsconf.8.gz', 'usr/share/man/man8/nfsd.8.gz', 'usr/share/man/man8/nfsdcld.8.gz', 'usr/share/man/man8/nfsdclddb.8.gz', 'usr/share/man/man8/nfsdclnts.8.gz', 'usr/share/man/man8/nfsdcltrack.8.gz', 'usr/share/man/man8/nfsidmap.8.gz', 'usr/share/man/man8/nfsiostat.8.gz', 'usr/share/man/man8/nfsstat.8.gz', 'usr/share/man/man8/rpc.idmapd.8.gz', 'usr/share/man/man8/rpc.mountd.8.gz', 'usr/share/man/man8/rpc.nfsd.8.gz', 'usr/share/man/man8/rpc.sm-notify.8.gz', 'usr/share/man/man8/rpc.statd.8.gz', 'usr/share/man/man8/rpcctl.8.gz', 'usr/share/man/man8/rpcdebug.8.gz', 'usr/share/man/man8/showmount.8.gz', 'usr/share/man/man8/sm-notify.8.gz', 'usr/share/man/man8/statd.8.gz', 'usr/share/man/man8/umount.nfs.8.gz', 'var/', 'var/lib/', 'var/lib/nfs/', 'var/lib/nfs/etab', 'var/lib/nfs/rmtab', 'var/lib/nfs/sm.bak/', 'var/lib/nfs/sm/', 'var/lib/nfs/state']"
+++
Support programs for Network File Systems