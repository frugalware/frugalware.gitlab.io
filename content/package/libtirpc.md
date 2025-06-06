+++
draft = false
title = "libtirpc 1.3.6-1"
version = "1.3.6-1"
description = "A port of Suns Transport-Independent RPC library to Linux."
date = "2024-10-18T15:07:05"
aliases = "/packages/103874"
categories = ['lib']
upstreamurl = "https://sourceforge.net/projects/libtirpc"
arch = "x86_64"
size = "171716"
usize = "447719"
sha1sum = "1d3f94d8501d493c1e389d84600474446697e804"
depends = "['libgssglue>=0.4-3', 'libkrb5>=1.16']"
reverse_depends = "['kio-extras', 'kio5-extras', 'libnsl', 'libvirt', 'lsof', 'quota-tools', 'rpcbind', 'xorg-server-xwayland', 'zfs']"
+++
### Description: 
A port of Suns Transport-Independent RPC library to Linux.

### Files: 
* /etc/bindresvport.blacklist
* /etc/netconfig
* /usr/include/tirpc/netconfig.h
* /usr/include/tirpc/rpc/auth.h
* /usr/include/tirpc/rpc/auth_des.h
* /usr/include/tirpc/rpc/auth_gss.h
* /usr/include/tirpc/rpc/auth_unix.h
* /usr/include/tirpc/rpc/clnt.h
* /usr/include/tirpc/rpc/clnt_soc.h
* /usr/include/tirpc/rpc/clnt_stat.h
* /usr/include/tirpc/rpc/des.h
* /usr/include/tirpc/rpc/des_crypt.h
* /usr/include/tirpc/rpc/key_prot.h
* /usr/include/tirpc/rpc/nettype.h
* /usr/include/tirpc/rpc/pmap_clnt.h
* /usr/include/tirpc/rpc/pmap_prot.h
* /usr/include/tirpc/rpc/pmap_rmt.h
* /usr/include/tirpc/rpc/raw.h
* /usr/include/tirpc/rpc/rpc.h
* /usr/include/tirpc/rpc/rpcb_clnt.h
* /usr/include/tirpc/rpc/rpcb_prot.h
* /usr/include/tirpc/rpc/rpcb_prot.x
* /usr/include/tirpc/rpc/rpcent.h
* /usr/include/tirpc/rpc/rpcsec_gss.h
* /usr/include/tirpc/rpc/rpc_com.h
* /usr/include/tirpc/rpc/rpc_msg.h
* /usr/include/tirpc/rpc/svc.h
* /usr/include/tirpc/rpc/svc_auth.h
* /usr/include/tirpc/rpc/svc_auth_gss.h
* /usr/include/tirpc/rpc/svc_dg.h
* /usr/include/tirpc/rpc/svc_mt.h
* /usr/include/tirpc/rpc/svc_soc.h
* /usr/include/tirpc/rpc/types.h
* /usr/include/tirpc/rpc/xdr.h
* /usr/include/tirpc/rpcsvc/crypt.h
* /usr/include/tirpc/rpcsvc/crypt.x
* /usr/lib/libtirpc.so
* /usr/lib/libtirpc.so.3
* /usr/lib/libtirpc.so.3.0.0
* /usr/lib/pkgconfig/libtirpc.pc
* /usr/share/doc/libtirpc-1.3.6/AUTHORS
* /usr/share/doc/libtirpc-1.3.6/ChangeLog
* /usr/share/doc/libtirpc-1.3.6/COPYING
* /usr/share/doc/libtirpc-1.3.6/HACKING
* /usr/share/doc/libtirpc-1.3.6/NEWS
* /usr/share/doc/libtirpc-1.3.6/README
* /usr/share/doc/libtirpc-1.3.6/THANKS
* /usr/share/doc/libtirpc-1.3.6/TODO
* /usr/share/doc/libtirpc-1.3.6/VERSION
* /usr/share/man/man3/bindresvport.3t.gz
* /usr/share/man/man3/des_crypt.3t.gz
* /usr/share/man/man3/getnetconfig.3t.gz
* /usr/share/man/man3/getnetpath.3t.gz
* /usr/share/man/man3/getrpcent.3t.gz
* /usr/share/man/man3/getrpcport.3t.gz
* /usr/share/man/man3/rpc.3t.gz
* /usr/share/man/man3/rpcbind.3t.gz
* /usr/share/man/man3/rpcsec_gss.3t.gz
* /usr/share/man/man3/rpc_clnt_auth.3t.gz
* /usr/share/man/man3/rpc_clnt_calls.3t.gz
* /usr/share/man/man3/rpc_clnt_create.3t.gz
* /usr/share/man/man3/rpc_gss_getcred.3t.gz
* /usr/share/man/man3/rpc_gss_get_error.3t.gz
* /usr/share/man/man3/rpc_gss_get_mechanisms.3t.gz
* /usr/share/man/man3/rpc_gss_get_mech_info.3t.gz
* /usr/share/man/man3/rpc_gss_get_principal_name.3t.gz
* /usr/share/man/man3/rpc_gss_get_versions.3t.gz
* /usr/share/man/man3/rpc_gss_is_installed.3t.gz
* /usr/share/man/man3/rpc_gss_max_data_length.3t.gz
* /usr/share/man/man3/rpc_gss_mech_to_oid.3t.gz
* /usr/share/man/man3/rpc_gss_qop_to_num.3t.gz
* /usr/share/man/man3/rpc_gss_seccreate.3t.gz
* /usr/share/man/man3/rpc_gss_set_callback.3t.gz
* /usr/share/man/man3/rpc_gss_set_defaults.3t.gz
* /usr/share/man/man3/rpc_gss_set_svc_name.3t.gz
* /usr/share/man/man3/rpc_gss_svc_max_data_length.3t.gz
* /usr/share/man/man3/rpc_secure.3t.gz
* /usr/share/man/man3/rpc_soc.3t.gz
* /usr/share/man/man3/rpc_svc_calls.3t.gz
* /usr/share/man/man3/rpc_svc_create.3t.gz
* /usr/share/man/man3/rpc_svc_err.3t.gz
* /usr/share/man/man3/rpc_svc_reg.3t.gz
* /usr/share/man/man3/rpc_xdr.3t.gz
* /usr/share/man/man3/rtime.3t.gz
* /usr/share/man/man5/netconfig.5.gz
