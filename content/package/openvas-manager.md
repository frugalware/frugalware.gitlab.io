+++
draft = false
title = "openvas-manager 23.1.0-1"
version = "23.1.0-1"
description = "OpenVAS manager."
date = "2024-01-09T18:25:56"
aliases = "/packages/217468"
categories = ['network-extra']
upstreamurl = "http://www.openvas.org"
arch = "x86_64"
size = "753012"
usize = "4946424"
sha1sum = "846d2f53315375eaba6b625a3ee853983610db16"
depends = "['gpgme', 'libbsd', 'libical', 'libpq', 'openvas-libraries>=22.7.3', 'postgresql']"
reverse_depends = "['openvas-cli']"
+++
OpenVAS manager.

{{< files text="show files" >}}* /etc/gvm/gvmd_log.conf
* /etc/gvm/pwpolicy.conf
* /etc/logrotate.d/gvmd
* /usr/bin/gvm-manage-certs
* /usr/bin/gvmd
* /usr/lib/libgvm-pg-server.so
* /usr/lib/libgvm-pg-server.so.23
* /usr/lib/libgvm-pg-server.so.23.1.0
* /usr/lib/systemd/system/gvmd.service
* /usr/share/doc/gvm/example-gvm-manage-certs.conf
* /usr/share/doc/gvm/html/gmp.html
* /usr/share/doc/openvas-manager-23.1.0/COPYING
* /usr/share/doc/openvas-manager-23.1.0/INSTALL.md
* /usr/share/doc/openvas-manager-23.1.0/README.md
* /usr/share/gvm/cert/cert_bund_getbyname.xsl
* /usr/share/gvm/cert/dfn_cert_getbyname.xsl
* /usr/share/gvm/gvm-lsc-deb-creator
* /usr/share/gvm/gvm-lsc-exe-creator
* /usr/share/gvm/gvm-lsc-rpm-creator
* /usr/share/gvm/gvmd/global_alert_methods/159f79a5-fce8-4ec5-aa49-7d17a77739a3/alert
* /usr/share/gvm/gvmd/global_alert_methods/2db07698-ec49-11e5-bcff-28d24461215b/alert
* /usr/share/gvm/gvmd/global_alert_methods/4a398d42-87c0-11e5-a1c0-28d24461215b/alert
* /usr/share/gvm/gvmd/global_alert_methods/5b39c481-9137-4876-b734-263849dd96ce/alert
* /usr/share/gvm/gvmd/global_alert_methods/5b39c481-9137-4876-b734-263849dd96ce/report-convert.py
* /usr/share/gvm/gvmd/global_alert_methods/9d435134-15d3-11e6-bf5c-28d24461215b/alert
* /usr/share/gvm/gvmd/global_alert_methods/c427a688-b653-40ab-a9d0-d6ba842a9d63/alert
* /usr/share/gvm/gvmd/global_alert_methods/cd1f5a34-6bdc-11e0-9827-002264764cea/alert
* /usr/share/gvm/gvmd/global_alert_methods/f9d97653-f89b-41af-9ba1-0f6ee00e9c1a/alert
* /usr/share/gvm/gvmd/global_schema_formats/02052818-dab6-11df-9be4-002264764cea/generate
* /usr/share/gvm/gvmd/global_schema_formats/02052818-dab6-11df-9be4-002264764cea/HTML.xsl
* /usr/share/gvm/gvmd/global_schema_formats/02052818-dab6-11df-9be4-002264764cea/rnc.xsl
* /usr/share/gvm/gvmd/global_schema_formats/18e826fc-dab6-11df-b913-002264764cea/generate
* /usr/share/gvm/gvmd/global_schema_formats/18e826fc-dab6-11df-b913-002264764cea/GMP.xml
* /usr/share/gvm/gvmd/global_schema_formats/787a4a18-dabc-11df-9486-002264764cea/generate
* /usr/share/gvm/gvmd/global_schema_formats/787a4a18-dabc-11df-9486-002264764cea/rnc.xsl
* /usr/share/gvm/gvmd/global_schema_formats/787a4a18-dabc-11df-9486-002264764cea/RNC.xsl
* /usr/share/gvm/gvmd/global_schema_formats/d6cf255e-947c-11e1-829a-406186ea4fc5/generate
* /usr/share/gvm/gvmd/global_schema_formats/d6cf255e-947c-11e1-829a-406186ea4fc5/GMP.xsl
* /usr/share/gvm/gvmd/global_schema_formats/rnc.xsl
* /usr/share/gvm/gvmd/template.nsis
* /usr/share/gvm/gvmd/wizards/delete_task_deep.xml
* /usr/share/gvm/gvmd/wizards/get_tasks_deep.xml
* /usr/share/gvm/gvmd/wizards/modify_task.xml
* /usr/share/gvm/gvmd/wizards/quick_auth_scan.xml
* /usr/share/gvm/gvmd/wizards/quick_first_scan.xml
* /usr/share/gvm/gvmd/wizards/quick_task.xml
* /usr/share/gvm/gvmd/wizards/reset_task.xml
* /usr/share/gvm/scap/cpe_getbyname.xsl
* /usr/share/gvm/scap/cve_getbyname.xsl
* /usr/share/man/man1/gvm-manage-certs.1.gz
* /usr/share/man/man8/gvmd.8.gz
{{< /files >}}