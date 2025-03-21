+++
draft = false
title = "squid 6.12-1"
version = "6.12-1"
description = "Squid Web Proxy Cache"
date = "2024-12-23T21:33:32"
aliases = "/packages/4064"
categories = ['network-extra']
upstreamurl = "http://www.squid-cache.org/"
arch = "x86_64"
size = "2597148"
usize = "8292061"
sha1sum = "33989c46d45653a701d3e22674eb2c0d565a7786"
depends = "['dcron', 'gnutls', 'libtool', 'libxcrypt', 'nettle>=3.6']"
+++
### Description: 
Squid Web Proxy Cache

### Files: 
* /etc/cron.weekly/squid
* /etc/squid/cachemgr.conf
* /etc/squid/cachemgr.conf.default
* /etc/squid/errorpage.css
* /etc/squid/errorpage.css.default
* /etc/squid/mime.conf
* /etc/squid/mime.conf.default
* /etc/squid/squid.conf
* /etc/squid/squid.conf.default
* /etc/squid/squid.conf.documented
* /etc/sysconfig/squid
* /usr/bin/purge
* /usr/bin/squid
* /usr/bin/squidclient
* /usr/lib/basic_db_auth
* /usr/lib/basic_fake_auth
* /usr/lib/basic_getpwnam_auth
* /usr/lib/basic_ncsa_auth
* /usr/lib/basic_pam_auth
* /usr/lib/basic_pop3_auth
* /usr/lib/basic_radius_auth
* /usr/lib/basic_smb_auth
* /usr/lib/basic_smb_auth.sh
* /usr/lib/cachemgr.cgi
* /usr/lib/digest_file_auth
* /usr/lib/diskd
* /usr/lib/ext_delayer_acl
* /usr/lib/ext_file_userip_acl
* /usr/lib/ext_kerberos_sid_group_acl
* /usr/lib/ext_sql_session_acl
* /usr/lib/ext_unix_group_acl
* /usr/lib/ext_wbinfo_group_acl
* /usr/lib/helper-mux
* /usr/lib/log_db_daemon
* /usr/lib/log_file_daemon
* /usr/lib/negotiate_wrapper_auth
* /usr/lib/ntlm_fake_auth
* /usr/lib/security_fake_certverify
* /usr/lib/squid/cache_swap.sh
* /usr/lib/storeid_file_rewrite
* /usr/lib/systemd/system/squid.service
* /usr/lib/sysusers.d/squid.conf
* /usr/lib/unlinkd
* /usr/lib/url_fake_rewrite
* /usr/lib/url_fake_rewrite.sh
* /usr/lib/url_lfs_rewrite
* /usr/share/doc/squid-6.12/ChangeLog
* /usr/share/doc/squid-6.12/CONTRIBUTORS
* /usr/share/doc/squid-6.12/COPYING
* /usr/share/doc/squid-6.12/CREDITS
* /usr/share/doc/squid-6.12/INSTALL
* /usr/share/doc/squid-6.12/README
* /usr/share/doc/squid-6.12/RELEASENOTES.html
* /usr/share/man/man1/purge.1.gz
* /usr/share/man/man1/squidclient.1.gz
* /usr/share/man/man8/basic_db_auth.8.gz
* /usr/share/man/man8/basic_getpwnam_auth.8.gz
* /usr/share/man/man8/basic_ncsa_auth.8.gz
* /usr/share/man/man8/basic_pam_auth.8.gz
* /usr/share/man/man8/basic_pop3_auth.8.gz
* /usr/share/man/man8/basic_radius_auth.8.gz
* /usr/share/man/man8/cachemgr.cgi.8.gz
* /usr/share/man/man8/digest_file_auth.8.gz
* /usr/share/man/man8/ext_delayer_acl.8.gz
* /usr/share/man/man8/ext_file_userip_acl.8.gz
* /usr/share/man/man8/ext_kerberos_sid_group_acl.8.gz
* /usr/share/man/man8/ext_sql_session_acl.8.gz
* /usr/share/man/man8/ext_unix_group_acl.8.gz
* /usr/share/man/man8/ext_wbinfo_group_acl.8.gz
* /usr/share/man/man8/helper-mux.8.gz
* /usr/share/man/man8/log_db_daemon.8.gz
* /usr/share/man/man8/security_fake_certverify.8.gz
* /usr/share/man/man8/squid.8.gz
* /usr/share/man/man8/storeid_file_rewrite.8.gz
* /usr/share/man/man8/url_lfs_rewrite.8.gz
* /usr/share/squid/errors/COPYRIGHT
* /usr/share/squid/errors/templates/error-details.txt
* /usr/share/squid/errors/templates/ERR_ACCESS_DENIED
* /usr/share/squid/errors/templates/ERR_ACL_TIME_QUOTA_EXCEEDED
* /usr/share/squid/errors/templates/ERR_AGENT_CONFIGURE
* /usr/share/squid/errors/templates/ERR_AGENT_WPAD
* /usr/share/squid/errors/templates/ERR_CACHE_ACCESS_DENIED
* /usr/share/squid/errors/templates/ERR_CACHE_MGR_ACCESS_DENIED
* /usr/share/squid/errors/templates/ERR_CANNOT_FORWARD
* /usr/share/squid/errors/templates/ERR_CONFLICT_HOST
* /usr/share/squid/errors/templates/ERR_CONNECT_FAIL
* /usr/share/squid/errors/templates/ERR_DIR_LISTING
* /usr/share/squid/errors/templates/ERR_DNS_FAIL
* /usr/share/squid/errors/templates/ERR_ESI
* /usr/share/squid/errors/templates/ERR_FORWARDING_DENIED
* /usr/share/squid/errors/templates/ERR_FTP_DISABLED
* /usr/share/squid/errors/templates/ERR_FTP_FAILURE
* /usr/share/squid/errors/templates/ERR_FTP_FORBIDDEN
* /usr/share/squid/errors/templates/ERR_FTP_NOT_FOUND
* /usr/share/squid/errors/templates/ERR_FTP_PUT_CREATED
* /usr/share/squid/errors/templates/ERR_FTP_PUT_ERROR
* /usr/share/squid/errors/templates/ERR_FTP_PUT_MODIFIED
* /usr/share/squid/errors/templates/ERR_FTP_UNAVAILABLE
* /usr/share/squid/errors/templates/ERR_GATEWAY_FAILURE
* /usr/share/squid/errors/templates/ERR_ICAP_FAILURE
* /usr/share/squid/errors/templates/ERR_INVALID_REQ
* /usr/share/squid/errors/templates/ERR_INVALID_RESP
* /usr/share/squid/errors/templates/ERR_INVALID_URL
* /usr/share/squid/errors/templates/ERR_LIFETIME_EXP
* /usr/share/squid/errors/templates/ERR_NO_RELAY
* /usr/share/squid/errors/templates/ERR_ONLY_IF_CACHED_MISS
* /usr/share/squid/errors/templates/ERR_PRECONDITION_FAILED
* /usr/share/squid/errors/templates/ERR_PROTOCOL_UNKNOWN
* /usr/share/squid/errors/templates/ERR_READ_ERROR
* /usr/share/squid/errors/templates/ERR_READ_TIMEOUT
* /usr/share/squid/errors/templates/ERR_SECURE_CONNECT_FAIL
* /usr/share/squid/errors/templates/ERR_SHUTTING_DOWN
* /usr/share/squid/errors/templates/ERR_SOCKET_FAILURE
* /usr/share/squid/errors/templates/ERR_TOO_BIG
* /usr/share/squid/errors/templates/ERR_UNSUP_HTTPVERSION
* /usr/share/squid/errors/templates/ERR_UNSUP_REQ
* /usr/share/squid/errors/templates/ERR_URN_RESOLVE
* /usr/share/squid/errors/templates/ERR_WRITE_ERROR
* /usr/share/squid/errors/templates/ERR_ZERO_SIZE_OBJECT
* /usr/share/squid/errors/TRANSLATORS
* /usr/share/squid/icons/silk/application.png
* /usr/share/squid/icons/silk/arrow_up.png
* /usr/share/squid/icons/silk/bomb.png
* /usr/share/squid/icons/silk/box.png
* /usr/share/squid/icons/silk/bricks.png
* /usr/share/squid/icons/silk/bullet_red.png
* /usr/share/squid/icons/silk/cd.png
* /usr/share/squid/icons/silk/chart_line.png
* /usr/share/squid/icons/silk/compress.png
* /usr/share/squid/icons/silk/computer_link.png
* /usr/share/squid/icons/silk/css.png
* /usr/share/squid/icons/silk/cup.png
* /usr/share/squid/icons/silk/database.png
* /usr/share/squid/icons/silk/database_table.png
* /usr/share/squid/icons/silk/drive_disk.png
* /usr/share/squid/icons/silk/film.png
* /usr/share/squid/icons/silk/film_key.png
* /usr/share/squid/icons/silk/folder.png
* /usr/share/squid/icons/silk/folder_table.png
* /usr/share/squid/icons/silk/image.png
* /usr/share/squid/icons/silk/information.png
* /usr/share/squid/icons/silk/layers.png
* /usr/share/squid/icons/silk/layout.png
* /usr/share/squid/icons/silk/link.png
* /usr/share/squid/icons/silk/music.png
* /usr/share/squid/icons/silk/package.png
* /usr/share/squid/icons/silk/package_go.png
* /usr/share/squid/icons/silk/page_code.png
* /usr/share/squid/icons/silk/page_excel.png
* /usr/share/squid/icons/silk/page_green.png
* /usr/share/squid/icons/silk/page_white.png
* /usr/share/squid/icons/silk/page_white_acrobat.png
* /usr/share/squid/icons/silk/page_white_c.png
* /usr/share/squid/icons/silk/page_white_cplusplus.png
* /usr/share/squid/icons/silk/page_white_flash.png
* /usr/share/squid/icons/silk/page_white_magnify.png
* /usr/share/squid/icons/silk/page_white_picture.png
* /usr/share/squid/icons/silk/page_white_powerpoint.png
* /usr/share/squid/icons/silk/page_white_stack.png
* /usr/share/squid/icons/silk/page_white_text.png
* /usr/share/squid/icons/silk/page_white_word.png
* /usr/share/squid/icons/silk/page_white_zip.png
* /usr/share/squid/icons/silk/page_world.png
* /usr/share/squid/icons/silk/photo.png
* /usr/share/squid/icons/silk/picture.png
* /usr/share/squid/icons/silk/plugin.png
* /usr/share/squid/icons/silk/plugin_add.png
* /usr/share/squid/icons/silk/script.png
* /usr/share/squid/icons/silk/script_gear.png
* /usr/share/squid/icons/silk/script_palette.png
* /usr/share/squid/icons/SN.png
* /usr/share/squid/mib.txt
