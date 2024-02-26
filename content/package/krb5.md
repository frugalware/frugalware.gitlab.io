+++
draft = false
title = "krb5 1.21.2-2"
version = "1.21.2-2"
description = "Kerberos: The Network Authentication Protocol"
date = "2024-01-14T14:03:57"
aliases = "/packages/74088"
categories = ['lib-extra']
upstreamurl = "http://web.mit.edu/kerberos/"
arch = "x86_64"
size = "516588"
usize = "1892090"
sha1sum = "3fd0426dec6843c13d6b9a5474af23ce24c17a5a"
depends = "['e2fsprogs>=1.43.3-2', 'libkrb5>=1.21.2', 'openssl>=3.1.0']"
reverse_depends = "['openconnect']"
license = "licence"
+++
Kerberos: The Network Authentication Protocol

{{< files text="show files" >}}* /usr/bin/gss-client
* /usr/bin/gss-server
* /usr/bin/k5srvutil
* /usr/bin/kadmin
* /usr/bin/kadmin.local
* /usr/bin/kadmind
* /usr/bin/kdb5_util
* /usr/bin/kdestroy
* /usr/bin/kinit
* /usr/bin/klist
* /usr/bin/kpasswd
* /usr/bin/kprop
* /usr/bin/kpropd
* /usr/bin/kproplog
* /usr/bin/krb5-config
* /usr/bin/krb5-send-pr
* /usr/bin/krb5kdc
* /usr/bin/ksu
* /usr/bin/kswitch
* /usr/bin/ktutil
* /usr/bin/kvno
* /usr/bin/sclient
* /usr/bin/sim_client
* /usr/bin/sim_server
* /usr/bin/sserver
* /usr/bin/uuclient
* /usr/bin/uuserver
* /usr/lib/krb5/plugins/kdb/db2.so
* /usr/lib/krb5/plugins/preauth/otp.so
* /usr/lib/krb5/plugins/preauth/pkinit.so
* /usr/lib/krb5/plugins/preauth/spake.so
* /usr/lib/krb5/plugins/preauth/test.so
* /usr/lib/krb5/plugins/tls/k5tls.so
* /usr/share/doc/krb5-1.21.2/README
* /usr/share/examples/krb5/kdc.conf
* /usr/share/examples/krb5/krb5.conf
* /usr/share/examples/krb5/services.append
* /usr/share/locale/de/LC_MESSAGES/mit-krb5.mo
* /usr/share/locale/en_US/LC_MESSAGES/mit-krb5.mo
* /usr/share/locale/ka/LC_MESSAGES/mit-krb5.mo
* /usr/share/man/man1/k5srvutil.1.gz
* /usr/share/man/man1/kadmin.1.gz
* /usr/share/man/man1/kdestroy.1.gz
* /usr/share/man/man1/kinit.1.gz
* /usr/share/man/man1/klist.1.gz
* /usr/share/man/man1/kpasswd.1.gz
* /usr/share/man/man1/krb5-config.1.gz
* /usr/share/man/man1/ksu.1.gz
* /usr/share/man/man1/kswitch.1.gz
* /usr/share/man/man1/ktutil.1.gz
* /usr/share/man/man1/kvno.1.gz
* /usr/share/man/man1/sclient.1.gz
* /usr/share/man/man5/.k5identity.5.gz
* /usr/share/man/man5/.k5login.5.gz
* /usr/share/man/man5/k5identity.5.gz
* /usr/share/man/man5/k5login.5.gz
* /usr/share/man/man5/kadm5.acl.5.gz
* /usr/share/man/man5/kdc.conf.5.gz
* /usr/share/man/man5/krb5.conf.5.gz
* /usr/share/man/man7/kerberos.7.gz
* /usr/share/man/man8/kadmin.local.8.gz
* /usr/share/man/man8/kadmind.8.gz
* /usr/share/man/man8/kdb5_ldap_util.8.gz
* /usr/share/man/man8/kdb5_util.8.gz
* /usr/share/man/man8/kprop.8.gz
* /usr/share/man/man8/kpropd.8.gz
* /usr/share/man/man8/kproplog.8.gz
* /usr/share/man/man8/krb5kdc.8.gz
* /usr/share/man/man8/sserver.8.gz
{{< /files >}}