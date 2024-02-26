+++
draft = false
title = "varnish 7.4.2-1"
version = "7.4.2-1"
description = "Varnish is an high-performance HTTP accelerator."
date = "2024-01-16T10:05:05"
aliases = "/packages/15053"
categories = ['network-extra']
upstreamurl = "http://varnish-cache.org/"
arch = "x86_64"
size = "1086324"
usize = "3589582"
sha1sum = "45bda2cef9b05654940bf1058e1e2917412e2d0b"
depends = "['pcre']"
+++
### Description: 
Varnish is an high-performance HTTP accelerator.

### Files: 
* /etc/varnish.conf
* /usr/bin/varnishadm
* /usr/bin/varnishd
* /usr/bin/varnishhist
* /usr/bin/varnishlog
* /usr/bin/varnishncsa
* /usr/bin/varnishstat
* /usr/bin/varnishstat_help_gen
* /usr/bin/varnishtest
* /usr/bin/varnishtop
* /usr/include/varnish/cache/cache.h
* /usr/include/varnish/cache/cache_backend.h
* /usr/include/varnish/cache/cache_director.h
* /usr/include/varnish/cache/cache_filter.h
* /usr/include/varnish/cache/cache_varnishd.h
* /usr/include/varnish/common/common_param.h
* /usr/include/varnish/miniobj.h
* /usr/include/varnish/tbl/acct_fields_bereq.h
* /usr/include/varnish/tbl/acct_fields_req.h
* /usr/include/varnish/tbl/backend_poll.h
* /usr/include/varnish/tbl/ban_arg_oper.h
* /usr/include/varnish/tbl/ban_oper.h
* /usr/include/varnish/tbl/ban_vars.h
* /usr/include/varnish/tbl/bereq_flags.h
* /usr/include/varnish/tbl/beresp_flags.h
* /usr/include/varnish/tbl/boc_state.h
* /usr/include/varnish/tbl/body_status.h
* /usr/include/varnish/tbl/cli_cmds.h
* /usr/include/varnish/tbl/debug_bits.h
* /usr/include/varnish/tbl/experimental_bits.h
* /usr/include/varnish/tbl/feature_bits.h
* /usr/include/varnish/tbl/h2_error.h
* /usr/include/varnish/tbl/h2_frames.h
* /usr/include/varnish/tbl/h2_settings.h
* /usr/include/varnish/tbl/h2_stream.h
* /usr/include/varnish/tbl/htc.h
* /usr/include/varnish/tbl/http_headers.h
* /usr/include/varnish/tbl/http_response.h
* /usr/include/varnish/tbl/locks.h
* /usr/include/varnish/tbl/obj_attr.h
* /usr/include/varnish/tbl/oc_exp_flags.h
* /usr/include/varnish/tbl/oc_flags.h
* /usr/include/varnish/tbl/params.h
* /usr/include/varnish/tbl/req_bereq_flags.h
* /usr/include/varnish/tbl/req_flags.h
* /usr/include/varnish/tbl/sess_attr.h
* /usr/include/varnish/tbl/sess_close.h
* /usr/include/varnish/tbl/symbol_kind.h
* /usr/include/varnish/tbl/vcc_feature_bits.h
* /usr/include/varnish/tbl/vcl_context.h
* /usr/include/varnish/tbl/vcl_returns.h
* /usr/include/varnish/tbl/vcl_states.h
* /usr/include/varnish/tbl/vhd_fsm.h
* /usr/include/varnish/tbl/vhd_fsm_funcs.h
* /usr/include/varnish/tbl/vhd_return.h
* /usr/include/varnish/tbl/vhp_huffman.h
* /usr/include/varnish/tbl/vhp_static.h
* /usr/include/varnish/tbl/vrt_stv_var.h
* /usr/include/varnish/tbl/vsc_levels.h
* /usr/include/varnish/tbl/vsig_list.h
* /usr/include/varnish/tbl/vsl_tags.h
* /usr/include/varnish/tbl/vsl_tags_http.h
* /usr/include/varnish/tbl/waiters.h
* /usr/include/varnish/vapi/vapi_options.h
* /usr/include/varnish/vapi/voptget.h
* /usr/include/varnish/vapi/vsc.h
* /usr/include/varnish/vapi/vsig.h
* /usr/include/varnish/vapi/vsl.h
* /usr/include/varnish/vapi/vsl_int.h
* /usr/include/varnish/vapi/vsm.h
* /usr/include/varnish/vas.h
* /usr/include/varnish/vav.h
* /usr/include/varnish/vbh.h
* /usr/include/varnish/vbm.h
* /usr/include/varnish/vcl.h
* /usr/include/varnish/vcli.h
* /usr/include/varnish/vcs.h
* /usr/include/varnish/vdef.h
* /usr/include/varnish/vmod_abi.h
* /usr/include/varnish/vnum.h
* /usr/include/varnish/vqueue.h
* /usr/include/varnish/vre.h
* /usr/include/varnish/vre_pcre2.h
* /usr/include/varnish/vrnd.h
* /usr/include/varnish/vrt.h
* /usr/include/varnish/vrt_obj.h
* /usr/include/varnish/vsa.h
* /usr/include/varnish/vsb.h
* /usr/include/varnish/vsha256.h
* /usr/include/varnish/vtcp.h
* /usr/include/varnish/vte.h
* /usr/include/varnish/vtim.h
* /usr/include/varnish/vtree.h
* /usr/include/varnish/vut.h
* /usr/include/varnish/vut_options.h
* /usr/include/varnish/waiter/waiter.h
* /usr/lib/libvarnishapi.so
* /usr/lib/libvarnishapi.so.3
* /usr/lib/libvarnishapi.so.3.1.0
* /usr/lib/pkgconfig/varnishapi.pc
* /usr/lib/systemd/system/varnish.service
* /usr/lib/varnish/vmods/libvmod_blob.so
* /usr/lib/varnish/vmods/libvmod_cookie.so
* /usr/lib/varnish/vmods/libvmod_debug.so
* /usr/lib/varnish/vmods/libvmod_directors.so
* /usr/lib/varnish/vmods/libvmod_h2.so
* /usr/lib/varnish/vmods/libvmod_proxy.so
* /usr/lib/varnish/vmods/libvmod_purge.so
* /usr/lib/varnish/vmods/libvmod_std.so
* /usr/lib/varnish/vmods/libvmod_unix.so
* /usr/lib/varnish/vmods/libvmod_vtc.so
* /usr/share/aclocal/varnish-legacy.m4
* /usr/share/aclocal/varnish.m4
* /usr/share/doc/varnish-7.4.2/builtin.vcl
* /usr/share/doc/varnish-7.4.2/ChangeLog
* /usr/share/doc/varnish-7.4.2/example.vcl
* /usr/share/doc/varnish-7.4.2/INSTALL
* /usr/share/doc/varnish-7.4.2/LICENSE
* /usr/share/doc/varnish-7.4.2/README.Packaging
* /usr/share/doc/varnish-7.4.2/README.rst
* /usr/share/man/man1/varnishadm.1.gz
* /usr/share/man/man1/varnishd.1.gz
* /usr/share/man/man1/varnishhist.1.gz
* /usr/share/man/man1/varnishlog.1.gz
* /usr/share/man/man1/varnishncsa.1.gz
* /usr/share/man/man1/varnishstat.1.gz
* /usr/share/man/man1/varnishtest.1.gz
* /usr/share/man/man1/varnishtop.1.gz
* /usr/share/man/man3/vmod_blob.3.gz
* /usr/share/man/man3/vmod_cookie.3.gz
* /usr/share/man/man3/vmod_directors.3.gz
* /usr/share/man/man3/vmod_h2.3.gz
* /usr/share/man/man3/vmod_proxy.3.gz
* /usr/share/man/man3/vmod_purge.3.gz
* /usr/share/man/man3/vmod_std.3.gz
* /usr/share/man/man3/vmod_unix.3.gz
* /usr/share/man/man3/vmod_vtc.3.gz
* /usr/share/man/man7/varnish-cli.7.gz
* /usr/share/man/man7/varnish-counters.7.gz
* /usr/share/man/man7/vcl-backend.7.gz
* /usr/share/man/man7/vcl-probe.7.gz
* /usr/share/man/man7/vcl-step.7.gz
* /usr/share/man/man7/vcl-var.7.gz
* /usr/share/man/man7/vcl.7.gz
* /usr/share/man/man7/vsl-query.7.gz
* /usr/share/man/man7/vsl.7.gz
* /usr/share/man/man7/vtc.7.gz
* /usr/share/varnish/vcc/vmod_blob.vcc
* /usr/share/varnish/vcc/vmod_cookie.vcc
* /usr/share/varnish/vcc/vmod_directors.vcc
* /usr/share/varnish/vcc/vmod_h2.vcc
* /usr/share/varnish/vcc/vmod_proxy.vcc
* /usr/share/varnish/vcc/vmod_purge.vcc
* /usr/share/varnish/vcc/vmod_std.vcc
* /usr/share/varnish/vcc/vmod_unix.vcc
* /usr/share/varnish/vcc/vmod_vtc.vcc
* /usr/share/varnish/vcl/devicedetect.vcl
* /usr/share/varnish/vmodtool.py
* /usr/share/varnish/vsctool.py
