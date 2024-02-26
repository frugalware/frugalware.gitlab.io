+++
draft = false
title = "usbguard 1.1.2-9"
version = "1.1.2-9"
description = "USBGuard is a software framework for implementing USB device authorization policies"
date = "2024-02-23T16:01:22"
aliases = "/packages/219227"
categories = ['apps-extra']
upstreamurl = "https://github.com/dkopecek/usbguard"
arch = "x86_64"
size = "460144"
usize = "1691007"
sha1sum = "e28dfbb516b6cf67b26f62d09344b95b3a070a62"
depends = "['audit', 'dbus-glib', 'libaudit', 'libcap-ng', 'libqb>=2.0.0', 'libseccomp', 'libsodium>=1.0.19', 'polkit', 'protobuf>=25.3']"
reverse_depends = "['usbguard-applet-qt', 'usbguard-notifier']"
+++
USBGuard is a software framework for implementing USB device authorization policies

## Files: 
* /etc/usbguard/rules.conf
* /etc/usbguard/usbguard-daemon.conf
* /usr/bin/usbguard
* /usr/bin/usbguard-daemon
* /usr/bin/usbguard-dbus
* /usr/bin/usbguard-rule-parser
* /usr/include/usbguard/Audit.hpp
* /usr/include/usbguard/ConfigFile.hpp
* /usr/include/usbguard/Device.hpp
* /usr/include/usbguard/DeviceManager.hpp
* /usr/include/usbguard/DeviceManagerHooks.hpp
* /usr/include/usbguard/Exception.hpp
* /usr/include/usbguard/Interface.hpp
* /usr/include/usbguard/IPCClient.hpp
* /usr/include/usbguard/IPCServer.hpp
* /usr/include/usbguard/KeyValueParser.hpp
* /usr/include/usbguard/Logger.hpp
* /usr/include/usbguard/MemoryRuleSet.hpp
* /usr/include/usbguard/Policy.hpp
* /usr/include/usbguard/Predicates.hpp
* /usr/include/usbguard/Rule.hpp
* /usr/include/usbguard/RuleCondition.hpp
* /usr/include/usbguard/RuleSet.hpp
* /usr/include/usbguard/Typedefs.hpp
* /usr/include/usbguard/USB.hpp
* /usr/include/usbguard/USBGuard.hpp
* /usr/lib/libusbguard.so
* /usr/lib/libusbguard.so.1
* /usr/lib/libusbguard.so.1.0.1
* /usr/lib/pkgconfig/libusbguard.pc
* /usr/lib/systemd/system/usbguard-dbus.service
* /usr/lib/systemd/system/usbguard.service
* /usr/share/bash-completion/completions/usbguard
* /usr/share/dbus-1/system-services/org.usbguard1.service
* /usr/share/dbus-1/system.d/org.usbguard1.conf
* /usr/share/doc/usbguard-1.1.2/LICENSE
* /usr/share/doc/usbguard-1.1.2/README.adoc
* /usr/share/doc/usbguard-1.1.2/VERSION
* /usr/share/man/man1/usbguard.1.gz
* /usr/share/man/man5/usbguard-daemon.conf.5.gz
* /usr/share/man/man5/usbguard-rules.conf.5.gz
* /usr/share/man/man8/usbguard-daemon.8.gz
* /usr/share/man/man8/usbguard-dbus.8.gz
* /usr/share/polkit-1/actions/org.usbguard1.policy
