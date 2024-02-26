+++
draft = false
title = "privoxy 3.0.34-2"
version = "3.0.34-2"
description = "Privoxy is a web proxy with advanced filtering capabilities."
date = "2024-01-15T15:41:37"
aliases = "/packages/15113"
categories = ['network-extra']
upstreamurl = "http://www.privoxy.org/"
arch = "x86_64"
size = "541332"
usize = "2303968"
sha1sum = "e063293396c190ce36d2dc88204af5eb7d2632a4"
depends = "['pcre']"
+++
Privoxy is a web proxy with advanced filtering capabilities.{{< files text="show files" >}}* /etc/privoxy/config
* /etc/privoxy/default.action
* /etc/privoxy/default.filter
* /etc/privoxy/match-all.action
* /etc/privoxy/regression-tests.action
* /etc/privoxy/templates/blocked
* /etc/privoxy/templates/cgi-error-404
* /etc/privoxy/templates/cgi-error-bad-param
* /etc/privoxy/templates/cgi-error-disabled
* /etc/privoxy/templates/cgi-error-file
* /etc/privoxy/templates/cgi-error-file-read-only
* /etc/privoxy/templates/cgi-error-modified
* /etc/privoxy/templates/cgi-error-parse
* /etc/privoxy/templates/cgi-style.css
* /etc/privoxy/templates/client-tags
* /etc/privoxy/templates/connect-failed
* /etc/privoxy/templates/connection-timeout
* /etc/privoxy/templates/default
* /etc/privoxy/templates/edit-actions-add-url-form
* /etc/privoxy/templates/edit-actions-for-url
* /etc/privoxy/templates/edit-actions-for-url-filter
* /etc/privoxy/templates/edit-actions-for-url-string-action
* /etc/privoxy/templates/edit-actions-list
* /etc/privoxy/templates/edit-actions-list-button
* /etc/privoxy/templates/edit-actions-list-section
* /etc/privoxy/templates/edit-actions-list-url
* /etc/privoxy/templates/edit-actions-remove-url-form
* /etc/privoxy/templates/edit-actions-url-form
* /etc/privoxy/templates/forwarding-failed
* /etc/privoxy/templates/mod-local-help
* /etc/privoxy/templates/mod-support-and-service
* /etc/privoxy/templates/mod-title
* /etc/privoxy/templates/mod-unstable-warning
* /etc/privoxy/templates/no-server-data
* /etc/privoxy/templates/no-such-domain
* /etc/privoxy/templates/show-request
* /etc/privoxy/templates/show-status
* /etc/privoxy/templates/show-status-file
* /etc/privoxy/templates/show-url-info
* /etc/privoxy/templates/toggle
* /etc/privoxy/templates/toggle-mini
* /etc/privoxy/templates/untrusted
* /etc/privoxy/templates/url-info-osd.xml
* /etc/privoxy/templates/wpad.dat
* /etc/privoxy/trust
* /etc/privoxy/user.action
* /etc/privoxy/user.filter
* /usr/bin/privoxy
* /usr/lib/systemd/system/privoxy.service
* /usr/share/doc/privoxy-3.0.34/AUTHORS
* /usr/share/doc/privoxy-3.0.34/ChangeLog
* /usr/share/doc/privoxy-3.0.34/developer-manual/coding.html
* /usr/share/doc/privoxy-3.0.34/developer-manual/documentation.html
* /usr/share/doc/privoxy-3.0.34/developer-manual/git.html
* /usr/share/doc/privoxy-3.0.34/developer-manual/index.html
* /usr/share/doc/privoxy-3.0.34/developer-manual/introduction.html
* /usr/share/doc/privoxy-3.0.34/developer-manual/newrelease.html
* /usr/share/doc/privoxy-3.0.34/developer-manual/testing.html
* /usr/share/doc/privoxy-3.0.34/developer-manual/webserver-update.html
* /usr/share/doc/privoxy-3.0.34/faq/configuration.html
* /usr/share/doc/privoxy-3.0.34/faq/contact.html
* /usr/share/doc/privoxy-3.0.34/faq/copyright.html
* /usr/share/doc/privoxy-3.0.34/faq/general.html
* /usr/share/doc/privoxy-3.0.34/faq/index.html
* /usr/share/doc/privoxy-3.0.34/faq/installation.html
* /usr/share/doc/privoxy-3.0.34/faq/misc.html
* /usr/share/doc/privoxy-3.0.34/faq/trouble.html
* /usr/share/doc/privoxy-3.0.34/index.html
* /usr/share/doc/privoxy-3.0.34/INSTALL
* /usr/share/doc/privoxy-3.0.34/LICENSE
* /usr/share/doc/privoxy-3.0.34/LICENSE.GPLv3
* /usr/share/doc/privoxy-3.0.34/man-page/privoxy-man-page.html
* /usr/share/doc/privoxy-3.0.34/p_doc.css
* /usr/share/doc/privoxy-3.0.34/README
* /usr/share/doc/privoxy-3.0.34/TODO
* /usr/share/doc/privoxy-3.0.34/user-manual/actions-file.html
* /usr/share/doc/privoxy-3.0.34/user-manual/appendix.html
* /usr/share/doc/privoxy-3.0.34/user-manual/config.html
* /usr/share/doc/privoxy-3.0.34/user-manual/configuration.html
* /usr/share/doc/privoxy-3.0.34/user-manual/contact.html
* /usr/share/doc/privoxy-3.0.34/user-manual/copyright.html
* /usr/share/doc/privoxy-3.0.34/user-manual/files-in-use.jpg
* /usr/share/doc/privoxy-3.0.34/user-manual/filter-file.html
* /usr/share/doc/privoxy-3.0.34/user-manual/index.html
* /usr/share/doc/privoxy-3.0.34/user-manual/installation.html
* /usr/share/doc/privoxy-3.0.34/user-manual/introduction.html
* /usr/share/doc/privoxy-3.0.34/user-manual/proxy2.jpg
* /usr/share/doc/privoxy-3.0.34/user-manual/proxy_setup.jpg
* /usr/share/doc/privoxy-3.0.34/user-manual/p_doc.css
* /usr/share/doc/privoxy-3.0.34/user-manual/quickstart.html
* /usr/share/doc/privoxy-3.0.34/user-manual/seealso.html
* /usr/share/doc/privoxy-3.0.34/user-manual/startup.html
* /usr/share/doc/privoxy-3.0.34/user-manual/templates.html
* /usr/share/doc/privoxy-3.0.34/user-manual/whatsnew.html
* /usr/share/man/man1/privoxy.8.gz
* /var/log/privoxy/logfile
{{< /files >}}