+++
draft = false
title = "courier-authlib 0.72.4-1"
version = "0.72.4-1"
description = "The Courier authentication library & daemon"
date = "2025-04-19T19:40:19"
aliases = "/packages/2951"
categories = ['network-extra']
upstreamurl = "http://www.courier-mta.org/"
arch = "x86_64"
size = "243280"
usize = "901749"
sha1sum = "eef75e84b35e250caf4840372c2afd2660e83247"
depends = "['courier-unicode>=2.1', 'gdbm>=1.15', 'libldap>=2.5.4', 'libpq>=11.2-2', 'libtool', 'mariadb-libs>=10.3.14', 'sqlite3>=3.10.2']"
reverse_depends = "['courier-imap', 'courier-maildrop']"
+++
### Description: 
The Courier authentication library & daemon

### Files: 
* /etc/courier/authdaemonrc
* /etc/courier/authlib/userdb
* /etc/ld.so.conf.d/courier-authlib.conf
* /usr/bin/authdaemond
* /usr/bin/authenumerate
* /usr/bin/authpasswd
* /usr/bin/authtest
* /usr/bin/courierauthconfig
* /usr/bin/courierlogger
* /usr/bin/makeuserdb
* /usr/bin/pw2userdb
* /usr/bin/userdb
* /usr/bin/userdbpw
* /usr/include/courierauth.h
* /usr/include/courierauthdebug.h
* /usr/include/courierauthsasl.h
* /usr/include/courierauthsaslclient.h
* /usr/include/courierauthstaticlist.h
* /usr/lib/courier-authlib/libauthcustom.so
* /usr/lib/courier-authlib/libauthcustom.so.0
* /usr/lib/courier-authlib/libauthcustom.so.0.0.0
* /usr/lib/courier-authlib/libauthldap.so
* /usr/lib/courier-authlib/libauthldap.so.0
* /usr/lib/courier-authlib/libauthldap.so.0.0.0
* /usr/lib/courier-authlib/libauthmysql.so
* /usr/lib/courier-authlib/libauthmysql.so.0
* /usr/lib/courier-authlib/libauthmysql.so.0.0.0
* /usr/lib/courier-authlib/libauthpgsql.so
* /usr/lib/courier-authlib/libauthpgsql.so.0
* /usr/lib/courier-authlib/libauthpgsql.so.0.0.0
* /usr/lib/courier-authlib/libauthpipe.so
* /usr/lib/courier-authlib/libauthpipe.so.0
* /usr/lib/courier-authlib/libauthpipe.so.0.0.0
* /usr/lib/courier-authlib/libauthshadow.so
* /usr/lib/courier-authlib/libauthshadow.so.0
* /usr/lib/courier-authlib/libauthshadow.so.0.0.0
* /usr/lib/courier-authlib/libauthsqlite.so
* /usr/lib/courier-authlib/libauthsqlite.so.0
* /usr/lib/courier-authlib/libauthsqlite.so.0.0.0
* /usr/lib/courier-authlib/libauthuserdb.so
* /usr/lib/courier-authlib/libauthuserdb.so.0
* /usr/lib/courier-authlib/libauthuserdb.so.0.0.0
* /usr/lib/courier-authlib/libcourierauth.so
* /usr/lib/courier-authlib/libcourierauth.so.0
* /usr/lib/courier-authlib/libcourierauth.so.0.0.0
* /usr/lib/courier-authlib/libcourierauthcommon.so
* /usr/lib/courier-authlib/libcourierauthcommon.so.0
* /usr/lib/courier-authlib/libcourierauthcommon.so.0.0.0
* /usr/lib/courier-authlib/libcourierauthsasl.so
* /usr/lib/courier-authlib/libcourierauthsasl.so.0
* /usr/lib/courier-authlib/libcourierauthsasl.so.0.0.0
* /usr/lib/courier-authlib/libcourierauthsaslclient.so
* /usr/lib/courier-authlib/libcourierauthsaslclient.so.0
* /usr/lib/courier-authlib/libcourierauthsaslclient.so.0.0.0
* /usr/lib/courier/courier-authlib/authdaemond
* /usr/lib/courier/courier-authlib/authsystem.passwd
* /usr/lib/courier/courier-authlib/makedatprog
* /usr/lib/systemd/system/courier-authlib.service
* /usr/lib/tmpfiles.d/courier-authlib.conf
* /usr/share/doc/courier-authlib-0.72.4/AUTHORS
* /usr/share/doc/courier-authlib-0.72.4/ChangeLog
* /usr/share/doc/courier-authlib-0.72.4/COPYING
* /usr/share/doc/courier-authlib-0.72.4/COPYING.GPL
* /usr/share/doc/courier-authlib-0.72.4/examples/authdaemonrc.dist
* /usr/share/doc/courier-authlib-0.72.4/examples/authldaprc.dist
* /usr/share/doc/courier-authlib-0.72.4/examples/authlib/authsqliterc.dist
* /usr/share/doc/courier-authlib-0.72.4/examples/authmysqlrc.dist
* /usr/share/doc/courier-authlib-0.72.4/examples/authpgsqlrc.dist
* /usr/share/doc/courier-authlib-0.72.4/INSTALL
* /usr/share/doc/courier-authlib-0.72.4/INSTALL.html
* /usr/share/doc/courier-authlib-0.72.4/NEWS
* /usr/share/doc/courier-authlib-0.72.4/README
* /usr/share/doc/courier-authlib-0.72.4/README.authdebug.html
* /usr/share/doc/courier-authlib-0.72.4/README.authdebug.html.in
* /usr/share/doc/courier-authlib-0.72.4/README.authmysql.html
* /usr/share/doc/courier-authlib-0.72.4/README.authmysql.myownquery
* /usr/share/doc/courier-authlib-0.72.4/README.authpostgres.html
* /usr/share/doc/courier-authlib-0.72.4/README.authsqlite.html
* /usr/share/doc/courier-authlib-0.72.4/README.frugalware
* /usr/share/doc/courier-authlib-0.72.4/README.html
* /usr/share/doc/courier-authlib-0.72.4/README.ldap
* /usr/share/doc/courier-authlib-0.72.4/README_authlib.html
* /usr/share/doc/courier-authlib-0.72.4/README_authlib.html.in
* /usr/share/man/man1/authpasswd.1.gz
* /usr/share/man/man1/authtest.1.gz
* /usr/share/man/man1/courierlogger.1.gz
* /usr/share/man/man3/authlib.3.gz
* /usr/share/man/man3/auth_enumerate.3.gz
* /usr/share/man/man3/auth_generic.3.gz
* /usr/share/man/man3/auth_generic_meta.3.gz
* /usr/share/man/man3/auth_getoption.3.gz
* /usr/share/man/man3/auth_getuserinfo.3.gz
* /usr/share/man/man3/auth_getuserinfo_meta.3.gz
* /usr/share/man/man3/auth_login.3.gz
* /usr/share/man/man3/auth_login_meta.3.gz
* /usr/share/man/man3/auth_meta.3.gz
* /usr/share/man/man3/auth_mkhomedir.3.gz
* /usr/share/man/man3/auth_passwd.3.gz
* /usr/share/man/man3/auth_sasl.3.gz
* /usr/share/man/man3/auth_sasl_ex.3.gz
* /usr/share/man/man8/makeuserdb.8.gz
* /usr/share/man/man8/pw2userdb.8.gz
* /usr/share/man/man8/userdb.8.gz
* /usr/share/man/man8/userdbpw.8.gz
