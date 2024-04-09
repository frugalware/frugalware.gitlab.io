+++
draft = false
title = "polkit 121-7"
version = "121-7"
description = "Policy framework for controlling privileges for system-wide services"
date = "2024-01-30T09:04:31"
aliases = "/packages/74585"
categories = ['base']
upstreamurl = "http://www.freedesktop.org/wiki/Software/polkit"
arch = "x86_64"
size = "401540"
usize = "1954934"
sha1sum = "87f40c32e3fa80cd87667cdbc7b0c102da1948f5"
depends = "['duktape', 'expat>=2.1.0-6', 'libffi>=3.2.1-2', 'libsystemd>=242', 'pam>=1.3.0-4', 'scriptlet-core']"
reverse_depends = "['accountsservice', 'bolt', 'clightd', 'colord', 'connman', 'cups-pk-helper', 'flatpak', 'fprintd', 'gamemode', 'gconf', 'iio-sensor-proxy', 'libvirt', 'modemmanager', 'networkmanager', 'packagekit', 'pcsc-lite', 'polkit-qt5-1', 'polkit-qt6-1', 'power-profiles-daemon', 'rtkit', 'sysprof', 'udisks2', 'usbguard']"
+++
### Description: 
Policy framework for controlling privileges for system-wide services

### Files: 
* /etc/pam.d/polkit-1
* /etc/polkit-1/rules.d/50-default.rules
* /usr/bin/pk-example-frobnicate
* /usr/bin/pkaction
* /usr/bin/pkcheck
* /usr/bin/pkexec
* /usr/bin/pkttyagent
* /usr/include/polkit-1/polkit/polkit.h
* /usr/include/polkit-1/polkit/polkitactiondescription.h
* /usr/include/polkit-1/polkit/polkitauthority.h
* /usr/include/polkit-1/polkit/polkitauthorityfeatures.h
* /usr/include/polkit-1/polkit/polkitauthorizationresult.h
* /usr/include/polkit-1/polkit/polkitcheckauthorizationflags.h
* /usr/include/polkit-1/polkit/polkitdetails.h
* /usr/include/polkit-1/polkit/polkitenumtypes.h
* /usr/include/polkit-1/polkit/polkiterror.h
* /usr/include/polkit-1/polkit/polkitidentity.h
* /usr/include/polkit-1/polkit/polkitimplicitauthorization.h
* /usr/include/polkit-1/polkit/polkitpermission.h
* /usr/include/polkit-1/polkit/polkitprivate.h
* /usr/include/polkit-1/polkit/polkitsubject.h
* /usr/include/polkit-1/polkit/polkitsystembusname.h
* /usr/include/polkit-1/polkit/polkittemporaryauthorization.h
* /usr/include/polkit-1/polkit/polkittypes.h
* /usr/include/polkit-1/polkit/polkitunixgroup.h
* /usr/include/polkit-1/polkit/polkitunixnetgroup.h
* /usr/include/polkit-1/polkit/polkitunixprocess.h
* /usr/include/polkit-1/polkit/polkitunixsession.h
* /usr/include/polkit-1/polkit/polkitunixuser.h
* /usr/include/polkit-1/polkitagent/polkitagent.h
* /usr/include/polkit-1/polkitagent/polkitagentenumtypes.h
* /usr/include/polkit-1/polkitagent/polkitagentlistener.h
* /usr/include/polkit-1/polkitagent/polkitagentsession.h
* /usr/include/polkit-1/polkitagent/polkitagenttextlistener.h
* /usr/include/polkit-1/polkitagent/polkitagenttypes.h
* /usr/lib/girepository-1.0/Polkit-1.0.typelib
* /usr/lib/girepository-1.0/PolkitAgent-1.0.typelib
* /usr/lib/libpolkit-agent-1.so
* /usr/lib/libpolkit-agent-1.so.0
* /usr/lib/libpolkit-agent-1.so.0.0.0
* /usr/lib/libpolkit-gobject-1.so
* /usr/lib/libpolkit-gobject-1.so.0
* /usr/lib/libpolkit-gobject-1.so.0.0.0
* /usr/lib/pkgconfig/polkit-agent-1.pc
* /usr/lib/pkgconfig/polkit-gobject-1.pc
* /usr/lib/polkit-1/polkit-agent-helper-1
* /usr/lib/polkit-1/polkitd
* /usr/lib/systemd/system/polkit.service
* /usr/lib/sysusers.d/polkit.conf
* /usr/share/dbus-1/system-services/org.freedesktop.PolicyKit1.service
* /usr/share/dbus-1/system.d/org.freedesktop.PolicyKit1.conf
* /usr/share/doc/polkit-121/AUTHORS
* /usr/share/doc/polkit-121/COPYING
* /usr/share/doc/polkit-121/LICENSE
* /usr/share/doc/polkit-121/README.md
* /usr/share/gettext/its/polkit.its
* /usr/share/gettext/its/polkit.loc
* /usr/share/gir-1.0/Polkit-1.0.gir
* /usr/share/gir-1.0/PolkitAgent-1.0.gir
* /usr/share/gtk-doc/html/polkit-1/annotation-glossary.html
* /usr/share/gtk-doc/html/polkit-1/eggdbus-interface-org.freedesktop.PolicyKit1.AuthenticationAgent.html
* /usr/share/gtk-doc/html/polkit-1/eggdbus-interface-org.freedesktop.PolicyKit1.Authority.html
* /usr/share/gtk-doc/html/polkit-1/home.png
* /usr/share/gtk-doc/html/polkit-1/Identities.html
* /usr/share/gtk-doc/html/polkit-1/index.html
* /usr/share/gtk-doc/html/polkit-1/left-insensitive.png
* /usr/share/gtk-doc/html/polkit-1/left.png
* /usr/share/gtk-doc/html/polkit-1/license.html
* /usr/share/gtk-doc/html/polkit-1/manpages.html
* /usr/share/gtk-doc/html/polkit-1/overview.html
* /usr/share/gtk-doc/html/polkit-1/pkaction.1.html
* /usr/share/gtk-doc/html/polkit-1/pkcheck.1.html
* /usr/share/gtk-doc/html/polkit-1/pkexec.1.html
* /usr/share/gtk-doc/html/polkit-1/pkttyagent.1.html
* /usr/share/gtk-doc/html/polkit-1/polit-index.html
* /usr/share/gtk-doc/html/polkit-1/polkit-1-PolkitError.html
* /usr/share/gtk-doc/html/polkit-1/polkit-agents.html
* /usr/share/gtk-doc/html/polkit-1/polkit-apps.html
* /usr/share/gtk-doc/html/polkit-1/polkit-architecture.html
* /usr/share/gtk-doc/html/polkit-1/polkit-architecture.png
* /usr/share/gtk-doc/html/polkit-1/polkit-authentication-agent-example-wheel.html
* /usr/share/gtk-doc/html/polkit-1/polkit-authentication-agent-example-wheel.png
* /usr/share/gtk-doc/html/polkit-1/polkit-authentication-agent-example.html
* /usr/share/gtk-doc/html/polkit-1/polkit-authentication-agent-example.png
* /usr/share/gtk-doc/html/polkit-1/polkit-hierarchy.html
* /usr/share/gtk-doc/html/polkit-1/polkit-intro.html
* /usr/share/gtk-doc/html/polkit-1/polkit.8.html
* /usr/share/gtk-doc/html/polkit-1/PolkitActionDescription.html
* /usr/share/gtk-doc/html/polkit-1/PolkitAgentListener.html
* /usr/share/gtk-doc/html/polkit-1/PolkitAgentSession.html
* /usr/share/gtk-doc/html/polkit-1/PolkitAgentTextListener.html
* /usr/share/gtk-doc/html/polkit-1/PolkitAuthority.html
* /usr/share/gtk-doc/html/polkit-1/PolkitAuthorizationResult.html
* /usr/share/gtk-doc/html/polkit-1/polkitd.8.html
* /usr/share/gtk-doc/html/polkit-1/PolkitDetails.html
* /usr/share/gtk-doc/html/polkit-1/PolkitIdentity.html
* /usr/share/gtk-doc/html/polkit-1/PolkitPermission.html
* /usr/share/gtk-doc/html/polkit-1/PolkitSubject.html
* /usr/share/gtk-doc/html/polkit-1/PolkitSystemBusName.html
* /usr/share/gtk-doc/html/polkit-1/PolkitTemporaryAuthorization.html
* /usr/share/gtk-doc/html/polkit-1/PolkitUnixGroup.html
* /usr/share/gtk-doc/html/polkit-1/PolkitUnixNetgroup.html
* /usr/share/gtk-doc/html/polkit-1/PolkitUnixProcess.html
* /usr/share/gtk-doc/html/polkit-1/PolkitUnixSession.html
* /usr/share/gtk-doc/html/polkit-1/PolkitUnixUser.html
* /usr/share/gtk-doc/html/polkit-1/ref-api.html
* /usr/share/gtk-doc/html/polkit-1/ref-authentication-agent-api.html
* /usr/share/gtk-doc/html/polkit-1/ref-dbus-api.html
* /usr/share/gtk-doc/html/polkit-1/right-insensitive.png
* /usr/share/gtk-doc/html/polkit-1/right.png
* /usr/share/gtk-doc/html/polkit-1/style.css
* /usr/share/gtk-doc/html/polkit-1/subjects.html
* /usr/share/gtk-doc/html/polkit-1/up-insensitive.png
* /usr/share/gtk-doc/html/polkit-1/up.png
* /usr/share/locale/cs/LC_MESSAGES/polkit-1.mo
* /usr/share/locale/da/LC_MESSAGES/polkit-1.mo
* /usr/share/locale/de/LC_MESSAGES/polkit-1.mo
* /usr/share/locale/hr/LC_MESSAGES/polkit-1.mo
* /usr/share/locale/hu/LC_MESSAGES/polkit-1.mo
* /usr/share/locale/id/LC_MESSAGES/polkit-1.mo
* /usr/share/locale/it/LC_MESSAGES/polkit-1.mo
* /usr/share/locale/nl/LC_MESSAGES/polkit-1.mo
* /usr/share/locale/nn/LC_MESSAGES/polkit-1.mo
* /usr/share/locale/pl/LC_MESSAGES/polkit-1.mo
* /usr/share/locale/pt/LC_MESSAGES/polkit-1.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/polkit-1.mo
* /usr/share/locale/ro/LC_MESSAGES/polkit-1.mo
* /usr/share/locale/sk/LC_MESSAGES/polkit-1.mo
* /usr/share/locale/sv/LC_MESSAGES/polkit-1.mo
* /usr/share/locale/tr/LC_MESSAGES/polkit-1.mo
* /usr/share/locale/uk/LC_MESSAGES/polkit-1.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/polkit-1.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/polkit-1.mo
* /usr/share/man/man1/pkaction.1.gz
* /usr/share/man/man1/pkcheck.1.gz
* /usr/share/man/man1/pkexec.1.gz
* /usr/share/man/man1/pkttyagent.1.gz
* /usr/share/man/man8/polkit.8.gz
* /usr/share/man/man8/polkitd.8.gz
* /usr/share/polkit-1/actions/org.freedesktop.policykit.examples.pkexec.policy
* /usr/share/polkit-1/actions/org.freedesktop.policykit.policy
* /usr/share/polkit-1/policyconfig-1.dtd
