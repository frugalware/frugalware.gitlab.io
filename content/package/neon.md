+++
draft = false
title = "neon 0.32.5-2"
version = "0.32.5-2"
date = "2023-03-15T22:15:12"
categories = ['network']
upstreamurl = "https://notroj.github.io/neon/"
arch = "x86_64"
size = "216524"
usize = "784236"
sha1sum = "8de48db73df873aca8f135397fd808d2eb04f090"
depends = "['libkrb5>=1.17-2', 'expat>=2.1.0-5', 'zlib>=1.2.12', 'openssl>=3.1.0']"
files = "['usr/', 'usr/bin/', 'usr/bin/neon-config', 'usr/include/', 'usr/include/neon/', 'usr/include/neon/ne_207.h', 'usr/include/neon/ne_acl.h', 'usr/include/neon/ne_acl3744.h', 'usr/include/neon/ne_alloc.h', 'usr/include/neon/ne_auth.h', 'usr/include/neon/ne_basic.h', 'usr/include/neon/ne_compress.h', 'usr/include/neon/ne_dates.h', 'usr/include/neon/ne_defs.h', 'usr/include/neon/ne_i18n.h', 'usr/include/neon/ne_locks.h', 'usr/include/neon/ne_md5.h', 'usr/include/neon/ne_pkcs11.h', 'usr/include/neon/ne_props.h', 'usr/include/neon/ne_redirect.h', 'usr/include/neon/ne_request.h', 'usr/include/neon/ne_session.h', 'usr/include/neon/ne_socket.h', 'usr/include/neon/ne_ssl.h', 'usr/include/neon/ne_string.h', 'usr/include/neon/ne_uri.h', 'usr/include/neon/ne_utils.h', 'usr/include/neon/ne_xml.h', 'usr/include/neon/ne_xmlreq.h', 'usr/lib/', 'usr/lib/libneon.so', 'usr/lib/libneon.so.27', 'usr/lib/libneon.so.27.5.5', 'usr/lib/pkgconfig/', 'usr/lib/pkgconfig/neon.pc', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/neon-0.32.5/', 'usr/share/doc/neon-0.32.5/AUTHORS', 'usr/share/doc/neon-0.32.5/BUGS', 'usr/share/doc/neon-0.32.5/ChangeLog', 'usr/share/doc/neon-0.32.5/INSTALL.win32', 'usr/share/doc/neon-0.32.5/NEWS', 'usr/share/doc/neon-0.32.5/README.md', 'usr/share/doc/neon-0.32.5/THANKS', 'usr/share/doc/neon-0.32.5/TODO', 'usr/share/doc/neon-0.32.5/html/', 'usr/share/doc/neon-0.32.5/html/api.html', 'usr/share/doc/neon-0.32.5/html/biblio.html', 'usr/share/doc/neon-0.32.5/html/compliance.html', 'usr/share/doc/neon-0.32.5/html/features.html', 'usr/share/doc/neon-0.32.5/html/index.html', 'usr/share/doc/neon-0.32.5/html/intro.html', 'usr/share/doc/neon-0.32.5/html/ref.html', 'usr/share/doc/neon-0.32.5/html/refalloc.html', 'usr/share/doc/neon-0.32.5/html/refauth.html', 'usr/share/doc/neon-0.32.5/html/refbuf.html', 'usr/share/doc/neon-0.32.5/html/refbufapp.html', 'usr/share/doc/neon-0.32.5/html/refbufcr.html', 'usr/share/doc/neon-0.32.5/html/refbufdest.html', 'usr/share/doc/neon-0.32.5/html/refbufutil.html', 'usr/share/doc/neon-0.32.5/html/refcert.html', 'usr/share/doc/neon-0.32.5/html/refclicert.html', 'usr/share/doc/neon-0.32.5/html/refconfig.html', 'usr/share/doc/neon-0.32.5/html/referr.html', 'usr/share/doc/neon-0.32.5/html/reffeat.html', 'usr/share/doc/neon-0.32.5/html/refgetst.html', 'usr/share/doc/neon-0.32.5/html/refhash.html', 'usr/share/doc/neon-0.32.5/html/refi18n.html', 'usr/share/doc/neon-0.32.5/html/refiaddr.html', 'usr/share/doc/neon-0.32.5/html/refneon.html', 'usr/share/doc/neon-0.32.5/html/refopts.html', 'usr/share/doc/neon-0.32.5/html/refparam.html', 'usr/share/doc/neon-0.32.5/html/refproxy.html', 'usr/share/doc/neon-0.32.5/html/refreq.html', 'usr/share/doc/neon-0.32.5/html/refreqbody.html', 'usr/share/doc/neon-0.32.5/html/refreqflags.html', 'usr/share/doc/neon-0.32.5/html/refreqhdr.html', 'usr/share/doc/neon-0.32.5/html/refresolve.html', 'usr/share/doc/neon-0.32.5/html/refresphdr.html', 'usr/share/doc/neon-0.32.5/html/refsess.html', 'usr/share/doc/neon-0.32.5/html/refsessflags.html', 'usr/share/doc/neon-0.32.5/html/refshave.html', 'usr/share/doc/neon-0.32.5/html/refsockinit.html', 'usr/share/doc/neon-0.32.5/html/refsslca.html', 'usr/share/doc/neon-0.32.5/html/refsslcert2.html', 'usr/share/doc/neon-0.32.5/html/refsslcertio.html', 'usr/share/doc/neon-0.32.5/html/refssldname.html', 'usr/share/doc/neon-0.32.5/html/refsslvfy.html', 'usr/share/doc/neon-0.32.5/html/refstatus.html', 'usr/share/doc/neon-0.32.5/html/reftok.html', 'usr/share/doc/neon-0.32.5/html/refvers.html', 'usr/share/doc/neon-0.32.5/html/refxml.html', 'usr/share/doc/neon-0.32.5/html/security.html', 'usr/share/doc/neon-0.32.5/html/using.html', 'usr/share/doc/neon-0.32.5/html/xml.html', 'usr/share/locale/', 'usr/share/locale/cs/', 'usr/share/locale/cs/LC_MESSAGES/', 'usr/share/locale/cs/LC_MESSAGES/neon.mo', 'usr/share/locale/de/', 'usr/share/locale/de/LC_MESSAGES/', 'usr/share/locale/de/LC_MESSAGES/neon.mo', 'usr/share/locale/fr/', 'usr/share/locale/fr/LC_MESSAGES/', 'usr/share/locale/fr/LC_MESSAGES/neon.mo', 'usr/share/locale/ja/', 'usr/share/locale/ja/LC_MESSAGES/', 'usr/share/locale/ja/LC_MESSAGES/neon.mo', 'usr/share/locale/ka/', 'usr/share/locale/ka/LC_MESSAGES/', 'usr/share/locale/ka/LC_MESSAGES/neon.mo', 'usr/share/locale/nn/', 'usr/share/locale/nn/LC_MESSAGES/', 'usr/share/locale/nn/LC_MESSAGES/neon.mo', 'usr/share/locale/pl/', 'usr/share/locale/pl/LC_MESSAGES/', 'usr/share/locale/pl/LC_MESSAGES/neon.mo', 'usr/share/locale/ru/', 'usr/share/locale/ru/LC_MESSAGES/', 'usr/share/locale/ru/LC_MESSAGES/neon.mo', 'usr/share/locale/tr/', 'usr/share/locale/tr/LC_MESSAGES/', 'usr/share/locale/tr/LC_MESSAGES/neon.mo', 'usr/share/locale/zh_CN/', 'usr/share/locale/zh_CN/LC_MESSAGES/', 'usr/share/locale/zh_CN/LC_MESSAGES/neon.mo', 'usr/share/man/', 'usr/share/man/man1/', 'usr/share/man/man1/neon-config.1.gz', 'usr/share/man/man3/', 'usr/share/man/man3/ne_add_request_header.3.gz', 'usr/share/man/man3/ne_addr_destroy.3.gz', 'usr/share/man/man3/ne_addr_error.3.gz', 'usr/share/man/man3/ne_addr_first.3.gz', 'usr/share/man/man3/ne_addr_next.3.gz', 'usr/share/man/man3/ne_addr_resolve.3.gz', 'usr/share/man/man3/ne_addr_result.3.gz', 'usr/share/man/man3/ne_buffer.3.gz', 'usr/share/man/man3/ne_buffer_altered.3.gz', 'usr/share/man/man3/ne_buffer_append.3.gz', 'usr/share/man/man3/ne_buffer_clear.3.gz', 'usr/share/man/man3/ne_buffer_concat.3.gz', 'usr/share/man/man3/ne_buffer_create.3.gz', 'usr/share/man/man3/ne_buffer_destroy.3.gz', 'usr/share/man/man3/ne_buffer_finish.3.gz', 'usr/share/man/man3/ne_buffer_grow.3.gz', 'usr/share/man/man3/ne_buffer_ncreate.3.gz', 'usr/share/man/man3/ne_buffer_zappend.3.gz', 'usr/share/man/man3/ne_calloc.3.gz', 'usr/share/man/man3/ne_close_connection.3.gz', 'usr/share/man/man3/ne_forget_auth.3.gz', 'usr/share/man/man3/ne_get_error.3.gz', 'usr/share/man/man3/ne_get_request_flag.3.gz', 'usr/share/man/man3/ne_get_response_header.3.gz', 'usr/share/man/man3/ne_get_scheme.3.gz', 'usr/share/man/man3/ne_get_server_hostport.3.gz', 'usr/share/man/man3/ne_get_session_flag.3.gz', 'usr/share/man/man3/ne_get_status.3.gz', 'usr/share/man/man3/ne_has_support.3.gz', 'usr/share/man/man3/ne_i18n_init.3.gz', 'usr/share/man/man3/ne_iaddr_cmp.3.gz', 'usr/share/man/man3/ne_iaddr_free.3.gz', 'usr/share/man/man3/ne_iaddr_make.3.gz', 'usr/share/man/man3/ne_iaddr_parse.3.gz', 'usr/share/man/man3/ne_iaddr_print.3.gz', 'usr/share/man/man3/ne_iaddr_raw.3.gz', 'usr/share/man/man3/ne_iaddr_reverse.3.gz', 'usr/share/man/man3/ne_iaddr_typeof.3.gz', 'usr/share/man/man3/ne_malloc.3.gz', 'usr/share/man/man3/ne_oom_callback.3.gz', 'usr/share/man/man3/ne_print_request_header.3.gz', 'usr/share/man/man3/ne_qtoken.3.gz', 'usr/share/man/man3/ne_realloc.3.gz', 'usr/share/man/man3/ne_request_create.3.gz', 'usr/share/man/man3/ne_request_destroy.3.gz', 'usr/share/man/man3/ne_request_dispatch.3.gz', 'usr/share/man/man3/ne_response_header_iterate.3.gz', 'usr/share/man/man3/ne_session_create.3.gz', 'usr/share/man/man3/ne_session_destroy.3.gz', 'usr/share/man/man3/ne_session_proxy.3.gz', 'usr/share/man/man3/ne_session_socks_proxy.3.gz', 'usr/share/man/man3/ne_session_system_proxy.3.gz', 'usr/share/man/man3/ne_set_addrlist.3.gz', 'usr/share/man/man3/ne_set_connect_timeout.3.gz', 'usr/share/man/man3/ne_set_error.3.gz', 'usr/share/man/man3/ne_set_proxy_auth.3.gz', 'usr/share/man/man3/ne_set_read_timeout.3.gz', 'usr/share/man/man3/ne_set_request_body_buffer.3.gz', 'usr/share/man/man3/ne_set_request_body_fd.3.gz', 'usr/share/man/man3/ne_set_request_flag.3.gz', 'usr/share/man/man3/ne_set_server_auth.3.gz', 'usr/share/man/man3/ne_set_session_flag.3.gz', 'usr/share/man/man3/ne_set_useragent.3.gz', 'usr/share/man/man3/ne_shave.3.gz', 'usr/share/man/man3/ne_sock_exit.3.gz', 'usr/share/man/man3/ne_sock_init.3.gz', 'usr/share/man/man3/ne_ssl_cert_cmp.3.gz', 'usr/share/man/man3/ne_ssl_cert_export.3.gz', 'usr/share/man/man3/ne_ssl_cert_free.3.gz', 'usr/share/man/man3/ne_ssl_cert_identity.3.gz', 'usr/share/man/man3/ne_ssl_cert_import.3.gz', 'usr/share/man/man3/ne_ssl_cert_issuer.3.gz', 'usr/share/man/man3/ne_ssl_cert_read.3.gz', 'usr/share/man/man3/ne_ssl_cert_signedby.3.gz', 'usr/share/man/man3/ne_ssl_cert_subject.3.gz', 'usr/share/man/man3/ne_ssl_cert_write.3.gz', 'usr/share/man/man3/ne_ssl_clicert_decrypt.3.gz', 'usr/share/man/man3/ne_ssl_clicert_encrypted.3.gz', 'usr/share/man/man3/ne_ssl_clicert_free.3.gz', 'usr/share/man/man3/ne_ssl_clicert_name.3.gz', 'usr/share/man/man3/ne_ssl_clicert_owner.3.gz', 'usr/share/man/man3/ne_ssl_clicert_read.3.gz', 'usr/share/man/man3/ne_ssl_dname_cmp.3.gz', 'usr/share/man/man3/ne_ssl_readable_dname.3.gz', 'usr/share/man/man3/ne_ssl_set_verify.3.gz', 'usr/share/man/man3/ne_ssl_trust_cert.3.gz', 'usr/share/man/man3/ne_ssl_trust_default_ca.3.gz', 'usr/share/man/man3/ne_status.3.gz', 'usr/share/man/man3/ne_strdup.3.gz', 'usr/share/man/man3/ne_strhash.3.gz', 'usr/share/man/man3/ne_strndup.3.gz', 'usr/share/man/man3/ne_strparam.3.gz', 'usr/share/man/man3/ne_token.3.gz', 'usr/share/man/man3/ne_version_match.3.gz', 'usr/share/man/man3/ne_version_string.3.gz', 'usr/share/man/man3/ne_vstrhash.3.gz', 'usr/share/man/man3/ne_xml_create.3.gz', 'usr/share/man/man3/ne_xml_destroy.3.gz', 'usr/share/man/man3/neon.3.gz']"
+++
An HTTP and WebDAV client library, with a C interface.