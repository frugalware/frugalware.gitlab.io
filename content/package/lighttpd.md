+++
draft = false
title = "lighttpd 1.4.73-2"
version = "1.4.73-2"
description = "A webserver designed and optimized for high performance environments."
date = "2024-02-01T14:49:25"
aliases = "/packages/9439"
categories = ['network-extra']
upstreamurl = "http://www.lighttpd.net/"
arch = "x86_64"
size = "426256"
usize = "1412534"
sha1sum = "7323d10e65f9c09a2e7893d7be856aac639666a6"
depends = "['bzip2', 'geoip', 'libldap>=2.5.4', 'lua>=5.4', 'mariadb-libs>=10.3.14', 'openssl>=3.1.0', 'pam', 'pcre>=8.30', 'xfsprogs-attr']"
license = "BSD"
+++
A webserver designed and optimized for high performance environments.

{{< files text="show files" >}}* /etc/lighttpd/conf.d/access_log.conf
* /etc/lighttpd/conf.d/auth.conf
* /etc/lighttpd/conf.d/cgi.conf
* /etc/lighttpd/conf.d/debug.conf
* /etc/lighttpd/conf.d/deflate.conf
* /etc/lighttpd/conf.d/dirlisting.conf
* /etc/lighttpd/conf.d/evhost.conf
* /etc/lighttpd/conf.d/expire.conf
* /etc/lighttpd/conf.d/fastcgi.conf
* /etc/lighttpd/conf.d/magnet.conf
* /etc/lighttpd/conf.d/mime.conf
* /etc/lighttpd/conf.d/mod.template
* /etc/lighttpd/conf.d/proxy.conf
* /etc/lighttpd/conf.d/rrdtool.conf
* /etc/lighttpd/conf.d/scgi.conf
* /etc/lighttpd/conf.d/simple_vhost.conf
* /etc/lighttpd/conf.d/ssi.conf
* /etc/lighttpd/conf.d/status.conf
* /etc/lighttpd/conf.d/userdir.conf
* /etc/lighttpd/conf.d/webdav.conf
* /etc/lighttpd/lighttpd.conf
* /etc/lighttpd/modules.conf
* /etc/lighttpd/vhosts.d/vhosts.template
* /usr/bin/lighttpd
* /usr/bin/lighttpd-angel
* /usr/lib/mod_accesslog.so
* /usr/lib/mod_ajp13.so
* /usr/lib/mod_auth.so
* /usr/lib/mod_authn_file.so
* /usr/lib/mod_authn_ldap.so
* /usr/lib/mod_authn_pam.so
* /usr/lib/mod_cgi.so
* /usr/lib/mod_deflate.so
* /usr/lib/mod_dirlisting.so
* /usr/lib/mod_extforward.so
* /usr/lib/mod_h2.so
* /usr/lib/mod_magnet.so
* /usr/lib/mod_openssl.so
* /usr/lib/mod_proxy.so
* /usr/lib/mod_rrdtool.so
* /usr/lib/mod_sockproxy.so
* /usr/lib/mod_ssi.so
* /usr/lib/mod_status.so
* /usr/lib/mod_userdir.so
* /usr/lib/mod_vhostdb.so
* /usr/lib/mod_vhostdb_ldap.so
* /usr/lib/mod_vhostdb_mysql.so
* /usr/lib/mod_webdav.so
* /usr/lib/mod_wstunnel.so
* /usr/lib/systemd/system/lighttpd.service
* /usr/share/doc/lighttpd-1.4.73/AUTHORS
* /usr/share/doc/lighttpd-1.4.73/COPYING
* /usr/share/doc/lighttpd-1.4.73/INSTALL
* /usr/share/doc/lighttpd-1.4.73/NEWS
* /usr/share/doc/lighttpd-1.4.73/README
* /usr/share/doc/lighttpd-1.4.73/README.FreeBSD
* /usr/share/man/man8/lighttpd-angel.8.gz
* /usr/share/man/man8/lighttpd.8.gz
* /var/www/htdocs/frugalware.png
* /var/www/htdocs/index.html
{{< /files >}}