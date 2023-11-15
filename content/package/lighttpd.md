+++
draft = false
title = "lighttpd 1.4.71-1"
version = "1.4.71-1"
date = "2023-06-18T18:44:17"
categories = ['network-extra']
upstreamurl = "http://www.lighttpd.net/"
arch = "x86_64"
size = "425132"
usize = "1405661"
sha1sum = "01ac07a6d399564af0672925697596baecaf49c4"
depends = "['mariadb-libs>=10.3.14', 'geoip', 'lua>=5.4', 'pam', 'bzip2', 'pcre>=8.30', 'xfsprogs-attr', 'libldap>=2.5.4', 'openssl>=3.1.0']"
license = "BSD"
files = "['etc/', 'etc/lighttpd/', 'etc/lighttpd/conf.d/', 'etc/lighttpd/conf.d/access_log.conf', 'etc/lighttpd/conf.d/auth.conf', 'etc/lighttpd/conf.d/cgi.conf', 'etc/lighttpd/conf.d/debug.conf', 'etc/lighttpd/conf.d/deflate.conf', 'etc/lighttpd/conf.d/dirlisting.conf', 'etc/lighttpd/conf.d/evhost.conf', 'etc/lighttpd/conf.d/expire.conf', 'etc/lighttpd/conf.d/fastcgi.conf', 'etc/lighttpd/conf.d/magnet.conf', 'etc/lighttpd/conf.d/mime.conf', 'etc/lighttpd/conf.d/mod.template', 'etc/lighttpd/conf.d/proxy.conf', 'etc/lighttpd/conf.d/rrdtool.conf', 'etc/lighttpd/conf.d/scgi.conf', 'etc/lighttpd/conf.d/simple_vhost.conf', 'etc/lighttpd/conf.d/ssi.conf', 'etc/lighttpd/conf.d/status.conf', 'etc/lighttpd/conf.d/userdir.conf', 'etc/lighttpd/conf.d/webdav.conf', 'etc/lighttpd/lighttpd.conf', 'etc/lighttpd/modules.conf', 'etc/lighttpd/vhosts.d/', 'etc/lighttpd/vhosts.d/vhosts.template', 'lib/', 'lib/systemd/', 'lib/systemd/system/', 'lib/systemd/system/lighttpd.service', 'usr/', 'usr/lib/', 'usr/lib/mod_accesslog.so', 'usr/lib/mod_ajp13.so', 'usr/lib/mod_auth.so', 'usr/lib/mod_authn_file.so', 'usr/lib/mod_authn_ldap.so', 'usr/lib/mod_authn_pam.so', 'usr/lib/mod_cgi.so', 'usr/lib/mod_deflate.so', 'usr/lib/mod_dirlisting.so', 'usr/lib/mod_extforward.so', 'usr/lib/mod_h2.so', 'usr/lib/mod_magnet.so', 'usr/lib/mod_openssl.so', 'usr/lib/mod_proxy.so', 'usr/lib/mod_rrdtool.so', 'usr/lib/mod_sockproxy.so', 'usr/lib/mod_ssi.so', 'usr/lib/mod_status.so', 'usr/lib/mod_userdir.so', 'usr/lib/mod_vhostdb.so', 'usr/lib/mod_vhostdb_ldap.so', 'usr/lib/mod_vhostdb_mysql.so', 'usr/lib/mod_webdav.so', 'usr/lib/mod_wstunnel.so', 'usr/sbin/', 'usr/sbin/lighttpd', 'usr/sbin/lighttpd-angel', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/lighttpd-1.4.71/', 'usr/share/doc/lighttpd-1.4.71/AUTHORS', 'usr/share/doc/lighttpd-1.4.71/COPYING', 'usr/share/doc/lighttpd-1.4.71/INSTALL', 'usr/share/doc/lighttpd-1.4.71/NEWS', 'usr/share/doc/lighttpd-1.4.71/README', 'usr/share/doc/lighttpd-1.4.71/README.FreeBSD', 'usr/share/man/', 'usr/share/man/man8/', 'usr/share/man/man8/lighttpd-angel.8.gz', 'usr/share/man/man8/lighttpd.8.gz', 'var/', 'var/cache/', 'var/cache/lighttpd/', 'var/lib/', 'var/lib/lighttpd/', 'var/log/', 'var/log/lighttpd/', 'var/www/', 'var/www/htdocs/', 'var/www/htdocs/frugalware.png', 'var/www/htdocs/index.html']"
+++
A webserver designed and optimized for high performance environments.