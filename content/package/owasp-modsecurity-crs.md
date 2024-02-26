+++
draft = false
title = "owasp-modsecurity-crs 3.2.0-1"
version = "3.2.0-1"
description = "ModSecurity Core Rule Set (CRS)"
date = "2022-05-20T07:51:53"
aliases = "/packages/219000"
categories = ['network-extra']
upstreamurl = "https://github.com/SpiderLabs/owasp-modsecurity-crs"
arch = "x86_64"
size = "124048"
usize = "705626"
sha1sum = "cb50ebd482c1c49fe1b8008ccfc419bb1fe1e4db"
depends = "[]"
reverse_depends = "['mod_security']"
+++
ModSecurity Core Rule Set (CRS)

{{< files text="show files" >}}* /etc/modsecurity/crs/CHANGES
* /etc/modsecurity/crs/CONTRIBUTING.md
* /etc/modsecurity/crs/CONTRIBUTORS.md
* /etc/modsecurity/crs/crs-setup.conf
* /etc/modsecurity/crs/documentation/README
* /etc/modsecurity/crs/INSTALL
* /etc/modsecurity/crs/KNOWN_BUGS
* /etc/modsecurity/crs/LICENSE
* /etc/modsecurity/crs/README.md
* /etc/modsecurity/crs/rules/crawlers-user-agents.data
* /etc/modsecurity/crs/rules/iis-errors.data
* /etc/modsecurity/crs/rules/java-classes.data
* /etc/modsecurity/crs/rules/java-code-leakages.data
* /etc/modsecurity/crs/rules/java-errors.data
* /etc/modsecurity/crs/rules/lfi-os-files.data
* /etc/modsecurity/crs/rules/php-config-directives.data
* /etc/modsecurity/crs/rules/php-errors.data
* /etc/modsecurity/crs/rules/php-function-names-933150.data
* /etc/modsecurity/crs/rules/php-function-names-933151.data
* /etc/modsecurity/crs/rules/php-variables.data
* /etc/modsecurity/crs/rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf
* /etc/modsecurity/crs/rules/REQUEST-901-INITIALIZATION.conf
* /etc/modsecurity/crs/rules/REQUEST-903.9001-DRUPAL-EXCLUSION-RULES.conf
* /etc/modsecurity/crs/rules/REQUEST-903.9002-WORDPRESS-EXCLUSION-RULES.conf
* /etc/modsecurity/crs/rules/REQUEST-903.9003-NEXTCLOUD-EXCLUSION-RULES.conf
* /etc/modsecurity/crs/rules/REQUEST-903.9004-DOKUWIKI-EXCLUSION-RULES.conf
* /etc/modsecurity/crs/rules/REQUEST-903.9005-CPANEL-EXCLUSION-RULES.conf
* /etc/modsecurity/crs/rules/REQUEST-903.9006-XENFORO-EXCLUSION-RULES.conf
* /etc/modsecurity/crs/rules/REQUEST-905-COMMON-EXCEPTIONS.conf
* /etc/modsecurity/crs/rules/REQUEST-910-IP-REPUTATION.conf
* /etc/modsecurity/crs/rules/REQUEST-911-METHOD-ENFORCEMENT.conf
* /etc/modsecurity/crs/rules/REQUEST-912-DOS-PROTECTION.conf
* /etc/modsecurity/crs/rules/REQUEST-913-SCANNER-DETECTION.conf
* /etc/modsecurity/crs/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf
* /etc/modsecurity/crs/rules/REQUEST-921-PROTOCOL-ATTACK.conf
* /etc/modsecurity/crs/rules/REQUEST-930-APPLICATION-ATTACK-LFI.conf
* /etc/modsecurity/crs/rules/REQUEST-931-APPLICATION-ATTACK-RFI.conf
* /etc/modsecurity/crs/rules/REQUEST-932-APPLICATION-ATTACK-RCE.conf
* /etc/modsecurity/crs/rules/REQUEST-933-APPLICATION-ATTACK-PHP.conf
* /etc/modsecurity/crs/rules/REQUEST-934-APPLICATION-ATTACK-NODEJS.conf
* /etc/modsecurity/crs/rules/REQUEST-941-APPLICATION-ATTACK-XSS.conf
* /etc/modsecurity/crs/rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf
* /etc/modsecurity/crs/rules/REQUEST-943-APPLICATION-ATTACK-SESSION-FIXATION.conf
* /etc/modsecurity/crs/rules/REQUEST-944-APPLICATION-ATTACK-JAVA.conf
* /etc/modsecurity/crs/rules/REQUEST-949-BLOCKING-EVALUATION.conf
* /etc/modsecurity/crs/rules/RESPONSE-950-DATA-LEAKAGES.conf
* /etc/modsecurity/crs/rules/RESPONSE-951-DATA-LEAKAGES-SQL.conf
* /etc/modsecurity/crs/rules/RESPONSE-952-DATA-LEAKAGES-JAVA.conf
* /etc/modsecurity/crs/rules/RESPONSE-953-DATA-LEAKAGES-PHP.conf
* /etc/modsecurity/crs/rules/RESPONSE-954-DATA-LEAKAGES-IIS.conf
* /etc/modsecurity/crs/rules/RESPONSE-959-BLOCKING-EVALUATION.conf
* /etc/modsecurity/crs/rules/RESPONSE-980-CORRELATION.conf
* /etc/modsecurity/crs/rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf
* /etc/modsecurity/crs/rules/restricted-files.data
* /etc/modsecurity/crs/rules/restricted-upload.data
* /etc/modsecurity/crs/rules/scanners-headers.data
* /etc/modsecurity/crs/rules/scanners-urls.data
* /etc/modsecurity/crs/rules/scanners-user-agents.data
* /etc/modsecurity/crs/rules/scripting-user-agents.data
* /etc/modsecurity/crs/rules/sql-errors.data
* /etc/modsecurity/crs/rules/unix-shell.data
* /etc/modsecurity/crs/rules/windows-powershell-commands.data
{{< /files >}}