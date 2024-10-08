+++
draft = false
title = "cyrus-sasl 2.1.28-7"
version = "2.1.28-7"
description = "SASL Authentication mechanism"
date = "2024-02-02T16:49:57"
aliases = "/packages/2957"
categories = ['network']
upstreamurl = "https://cyrusimap.org/"
arch = "x86_64"
size = "234296"
usize = "804877"
sha1sum = "e4ae7c3ff25e3ae03e7d1cc78ea49144f56892a1"
depends = "['e2fsprogs>=1.42.13-4', 'gdbm>=1.15', 'libkrb5>=1.17-2', 'openssl>=3.1.0']"
reverse_depends = "['apr-util', 'cyrus-sasl-gssapiv2', 'cyrus-sasl-sql', 'gtk-vnc', 'kimap', 'ksmtp', 'kvm', 'libetpan', 'libkgapi', 'libldap', 'libpurple', 'libvirt', 'mutt-devel', 'postfix', 'qca', 'qca-cyrus-sasl', 'qca-qt5', 'qemu', 'saslauthd', 'spice', 'telepathy-salut', 'znc']"
+++
### Description: 
SASL Authentication mechanism

### Files: 
* /usr/bin/pluginviewer
* /usr/bin/sasldblistusers2
* /usr/bin/saslpasswd2
* /usr/include/sasl/hmac-md5.h
* /usr/include/sasl/md5.h
* /usr/include/sasl/md5global.h
* /usr/include/sasl/prop.h
* /usr/include/sasl/sasl.h
* /usr/include/sasl/saslplug.h
* /usr/include/sasl/saslutil.h
* /usr/lib/libsasl2.so
* /usr/lib/libsasl2.so.3
* /usr/lib/libsasl2.so.3.0.0
* /usr/lib/pkgconfig/libsasl2.pc
* /usr/lib/sasl2/libcrammd5.so
* /usr/lib/sasl2/libcrammd5.so.3
* /usr/lib/sasl2/libcrammd5.so.3.0.0
* /usr/lib/sasl2/libdigestmd5.so
* /usr/lib/sasl2/libdigestmd5.so.3
* /usr/lib/sasl2/libdigestmd5.so.3.0.0
* /usr/lib/sasl2/libgs2.so
* /usr/lib/sasl2/libgs2.so.3
* /usr/lib/sasl2/libgs2.so.3.0.0
* /usr/lib/sasl2/liblogin.so
* /usr/lib/sasl2/liblogin.so.3
* /usr/lib/sasl2/liblogin.so.3.0.0
* /usr/lib/sasl2/libotp.so
* /usr/lib/sasl2/libotp.so.3
* /usr/lib/sasl2/libotp.so.3.0.0
* /usr/lib/sasl2/libplain.so
* /usr/lib/sasl2/libplain.so.3
* /usr/lib/sasl2/libplain.so.3.0.0
* /usr/lib/sasl2/libsasldb.so
* /usr/lib/sasl2/libsasldb.so.3
* /usr/lib/sasl2/libsasldb.so.3.0.0
* /usr/lib/sasl2/libscram.so
* /usr/lib/sasl2/libscram.so.3
* /usr/lib/sasl2/libscram.so.3.0.0
* /usr/share/doc/cyrus-sasl-2.1.28/AUTHORS
* /usr/share/doc/cyrus-sasl-2.1.28/ChangeLog
* /usr/share/doc/cyrus-sasl-2.1.28/COPYING
* /usr/share/doc/cyrus-sasl-2.1.28/INSTALL.TXT
* /usr/share/doc/cyrus-sasl-2.1.28/README
* /usr/share/doc/cyrus-sasl-2.1.28/README.Frugalware
* /usr/share/man/man3/sasl.3.gz
* /usr/share/man/man3/sasl_authorize_t.3.gz
* /usr/share/man/man3/sasl_auxprop.3.gz
* /usr/share/man/man3/sasl_auxprop_getctx.3.gz
* /usr/share/man/man3/sasl_auxprop_request.3.gz
* /usr/share/man/man3/sasl_callbacks.3.gz
* /usr/share/man/man3/sasl_canon_user_t.3.gz
* /usr/share/man/man3/sasl_chalprompt_t.3.gz
* /usr/share/man/man3/sasl_checkapop.3.gz
* /usr/share/man/man3/sasl_checkpass.3.gz
* /usr/share/man/man3/sasl_client_init.3.gz
* /usr/share/man/man3/sasl_client_new.3.gz
* /usr/share/man/man3/sasl_client_start.3.gz
* /usr/share/man/man3/sasl_client_step.3.gz
* /usr/share/man/man3/sasl_decode.3.gz
* /usr/share/man/man3/sasl_dispose.3.gz
* /usr/share/man/man3/sasl_done.3.gz
* /usr/share/man/man3/sasl_encode.3.gz
* /usr/share/man/man3/sasl_encodev.3.gz
* /usr/share/man/man3/sasl_errdetail.3.gz
* /usr/share/man/man3/sasl_errors.3.gz
* /usr/share/man/man3/sasl_errstring.3.gz
* /usr/share/man/man3/sasl_getconfpath_t.3.gz
* /usr/share/man/man3/sasl_getopt_t.3.gz
* /usr/share/man/man3/sasl_getpath_t.3.gz
* /usr/share/man/man3/sasl_getprop.3.gz
* /usr/share/man/man3/sasl_getrealm_t.3.gz
* /usr/share/man/man3/sasl_getsecret_t.3.gz
* /usr/share/man/man3/sasl_getsimple_t.3.gz
* /usr/share/man/man3/sasl_global_listmech.3.gz
* /usr/share/man/man3/sasl_idle.3.gz
* /usr/share/man/man3/sasl_listmech.3.gz
* /usr/share/man/man3/sasl_log_t.3.gz
* /usr/share/man/man3/sasl_server_init.3.gz
* /usr/share/man/man3/sasl_server_new.3.gz
* /usr/share/man/man3/sasl_server_start.3.gz
* /usr/share/man/man3/sasl_server_step.3.gz
* /usr/share/man/man3/sasl_server_userdb_checkpass_t.3.gz
* /usr/share/man/man3/sasl_server_userdb_setpass_t.3.gz
* /usr/share/man/man3/sasl_setpass.3.gz
* /usr/share/man/man3/sasl_setprop.3.gz
* /usr/share/man/man3/sasl_user_exists.3.gz
* /usr/share/man/man3/sasl_verifyfile_t.3.gz
* /usr/share/man/man8/pluginviewer.8.gz
* /usr/share/man/man8/sasldblistusers2.8.gz
* /usr/share/man/man8/saslpasswd2.8.gz
* /usr/share/man/man8/testsaslauthd.8.gz
