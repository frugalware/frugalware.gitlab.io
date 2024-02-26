+++
draft = false
title = "ufw 0.36.2-1"
version = "0.36.2-1"
description = "Uncomplicated Firewall is program for managing a netfilter firewall"
date = "2024-01-14T15:14:03"
aliases = "/packages/60653"
categories = ['network-extra']
upstreamurl = "https://launchpad.net/ufw"
arch = "x86_64"
size = "221348"
usize = "1019561"
sha1sum = "e62f33d0f457745a39a52d06874967f30e2add06"
depends = "['iptables>=1.8.2-3', 'python3', 'sed>=4.2.1']"
+++
Uncomplicated Firewall is program for managing a netfilter firewall"

{{< files text="show files" >}}* /etc/default/ufw
* /etc/ufw/after.init
* /etc/ufw/after.rules
* /etc/ufw/after6.rules
* /etc/ufw/applications.d/ufw-bittorent
* /etc/ufw/applications.d/ufw-chat
* /etc/ufw/applications.d/ufw-directoryserver
* /etc/ufw/applications.d/ufw-dnsserver
* /etc/ufw/applications.d/ufw-fileserver
* /etc/ufw/applications.d/ufw-loginserver
* /etc/ufw/applications.d/ufw-mailserver
* /etc/ufw/applications.d/ufw-printserver
* /etc/ufw/applications.d/ufw-proxyserver
* /etc/ufw/applications.d/ufw-webserver
* /etc/ufw/before.init
* /etc/ufw/before.rules
* /etc/ufw/before6.rules
* /etc/ufw/sysctl.conf
* /etc/ufw/ufw.conf
* /etc/ufw/user.rules
* /etc/ufw/user6.rules
* /usr/bin/ufw
* /usr/lib/python3.12/site-packages/ufw-0.36.2-py3.12.egg-info/dependency_links.txt
* /usr/lib/python3.12/site-packages/ufw-0.36.2-py3.12.egg-info/PKG-INFO
* /usr/lib/python3.12/site-packages/ufw-0.36.2-py3.12.egg-info/SOURCES.txt
* /usr/lib/python3.12/site-packages/ufw-0.36.2-py3.12.egg-info/top_level.txt
* /usr/lib/python3.12/site-packages/ufw/applications.py
* /usr/lib/python3.12/site-packages/ufw/backend.py
* /usr/lib/python3.12/site-packages/ufw/backend_iptables.py
* /usr/lib/python3.12/site-packages/ufw/common.py
* /usr/lib/python3.12/site-packages/ufw/frontend.py
* /usr/lib/python3.12/site-packages/ufw/parser.py
* /usr/lib/python3.12/site-packages/ufw/util.py
* /usr/lib/python3.12/site-packages/ufw/__init__.py
* /usr/lib/python3.12/site-packages/ufw/__pycache__/applications.cpython-312.pyc
* /usr/lib/python3.12/site-packages/ufw/__pycache__/backend.cpython-312.pyc
* /usr/lib/python3.12/site-packages/ufw/__pycache__/backend_iptables.cpython-312.pyc
* /usr/lib/python3.12/site-packages/ufw/__pycache__/common.cpython-312.pyc
* /usr/lib/python3.12/site-packages/ufw/__pycache__/frontend.cpython-312.pyc
* /usr/lib/python3.12/site-packages/ufw/__pycache__/parser.cpython-312.pyc
* /usr/lib/python3.12/site-packages/ufw/__pycache__/util.cpython-312.pyc
* /usr/lib/python3.12/site-packages/ufw/__pycache__/__init__.cpython-312.pyc
* /usr/lib/systemd/system/ufw.service
* /usr/lib/ufw/ufw-init
* /usr/lib/ufw/ufw-init-functions
* /usr/share/doc/ufw-0.36.2/AUTHORS
* /usr/share/doc/ufw-0.36.2/ChangeLog
* /usr/share/doc/ufw-0.36.2/COPYING
* /usr/share/doc/ufw-0.36.2/README
* /usr/share/doc/ufw-0.36.2/README.design
* /usr/share/doc/ufw-0.36.2/README.translations
* /usr/share/doc/ufw-0.36.2/TODO
* /usr/share/man/man8/ufw-framework.8.gz
* /usr/share/man/man8/ufw.8.gz
* /usr/share/ufw/iptables/after.rules
* /usr/share/ufw/iptables/after6.rules
* /usr/share/ufw/iptables/before.rules
* /usr/share/ufw/iptables/before6.rules
* /usr/share/ufw/iptables/user.rules
* /usr/share/ufw/iptables/user6.rules
* /usr/share/ufw/messages/ar.mo
* /usr/share/ufw/messages/ast.mo
* /usr/share/ufw/messages/bg.mo
* /usr/share/ufw/messages/bs.mo
* /usr/share/ufw/messages/ca.mo
* /usr/share/ufw/messages/ce.mo
* /usr/share/ufw/messages/cs.mo
* /usr/share/ufw/messages/da.mo
* /usr/share/ufw/messages/de.mo
* /usr/share/ufw/messages/el.mo
* /usr/share/ufw/messages/en_AU.mo
* /usr/share/ufw/messages/en_GB.mo
* /usr/share/ufw/messages/es.mo
* /usr/share/ufw/messages/et.mo
* /usr/share/ufw/messages/fi.mo
* /usr/share/ufw/messages/fr.mo
* /usr/share/ufw/messages/he.mo
* /usr/share/ufw/messages/hu.mo
* /usr/share/ufw/messages/id.mo
* /usr/share/ufw/messages/it.mo
* /usr/share/ufw/messages/ja.mo
* /usr/share/ufw/messages/ko.mo
* /usr/share/ufw/messages/lv.mo
* /usr/share/ufw/messages/nb.mo
* /usr/share/ufw/messages/nl.mo
* /usr/share/ufw/messages/pl.mo
* /usr/share/ufw/messages/pt.mo
* /usr/share/ufw/messages/pt_BR.mo
* /usr/share/ufw/messages/ro.mo
* /usr/share/ufw/messages/ru.mo
* /usr/share/ufw/messages/se.mo
* /usr/share/ufw/messages/sk.mo
* /usr/share/ufw/messages/sl.mo
* /usr/share/ufw/messages/sr.mo
* /usr/share/ufw/messages/sv.mo
* /usr/share/ufw/messages/tl.mo
* /usr/share/ufw/messages/tr.mo
* /usr/share/ufw/messages/uk.mo
* /usr/share/ufw/messages/ur.mo
* /usr/share/ufw/messages/zh_CN.mo
* /usr/share/ufw/messages/zh_TW.mo
{{< /files >}}