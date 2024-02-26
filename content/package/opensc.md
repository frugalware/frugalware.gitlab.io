+++
draft = false
title = "opensc 0.24.0-1"
version = "0.24.0-1"
description = "Tools and libraries for smart cards"
date = "2023-12-13T21:00:57"
aliases = "/packages/219996"
categories = ['base']
upstreamurl = "https://github.com/OpenSC/OpenSC/wiki"
arch = "x86_64"
size = "1201796"
usize = "3837990"
sha1sum = "54d87dc822359150ca2159a48bf29535dd67f633"
depends = "['openssl>=3.1.0', 'pcsc-lite']"
reverse_depends = "['rng-tools']"
+++
Tools and libraries for smart cards"

{{< files text="show files" >}}* /etc/bash_completion.d/cardos-tool
* /etc/bash_completion.d/cryptoflex-tool
* /etc/bash_completion.d/dnie-tool
* /etc/bash_completion.d/egk-tool
* /etc/bash_completion.d/eidenv
* /etc/bash_completion.d/gids-tool
* /etc/bash_completion.d/goid-tool
* /etc/bash_completion.d/iasecc-tool
* /etc/bash_completion.d/netkey-tool
* /etc/bash_completion.d/npa-tool
* /etc/bash_completion.d/openpgp-tool
* /etc/bash_completion.d/opensc-asn1
* /etc/bash_completion.d/opensc-explorer
* /etc/bash_completion.d/opensc-notify
* /etc/bash_completion.d/opensc-tool
* /etc/bash_completion.d/piv-tool
* /etc/bash_completion.d/pkcs11-register
* /etc/bash_completion.d/pkcs11-tool
* /etc/bash_completion.d/pkcs15-crypt
* /etc/bash_completion.d/pkcs15-init
* /etc/bash_completion.d/pkcs15-tool
* /etc/bash_completion.d/sc-hsm-tool
* /etc/bash_completion.d/westcos-tool
* /etc/opensc.conf
* /usr/bin/cardos-tool
* /usr/bin/cryptoflex-tool
* /usr/bin/dnie-tool
* /usr/bin/egk-tool
* /usr/bin/eidenv
* /usr/bin/gids-tool
* /usr/bin/goid-tool
* /usr/bin/iasecc-tool
* /usr/bin/netkey-tool
* /usr/bin/openpgp-tool
* /usr/bin/opensc-asn1
* /usr/bin/opensc-explorer
* /usr/bin/opensc-notify
* /usr/bin/opensc-tool
* /usr/bin/piv-tool
* /usr/bin/pkcs11-register
* /usr/bin/pkcs11-tool
* /usr/bin/pkcs15-crypt
* /usr/bin/pkcs15-init
* /usr/bin/pkcs15-tool
* /usr/bin/sc-hsm-tool
* /usr/bin/westcos-tool
* /usr/lib/libopensc.so
* /usr/lib/libopensc.so.8
* /usr/lib/libopensc.so.8.2.1
* /usr/lib/libsmm-local.so
* /usr/lib/libsmm-local.so.8
* /usr/lib/libsmm-local.so.8.2.1
* /usr/lib/onepin-opensc-pkcs11.so
* /usr/lib/opensc-pkcs11.so
* /usr/lib/pkcs11-spy.so
* /usr/lib/pkcs11/onepin-opensc-pkcs11.so
* /usr/lib/pkcs11/opensc-pkcs11.so
* /usr/lib/pkcs11/pkcs11-spy.so
* /usr/lib/pkgconfig/opensc-pkcs11.pc
* /usr/share/applications/org.opensc.notify.desktop
* /usr/share/doc/opensc-0.24.0/COPYING
* /usr/share/doc/opensc-0.24.0/NEWS
* /usr/share/doc/opensc-0.24.0/opensc.conf
* /usr/share/doc/opensc-0.24.0/README
* /usr/share/man/man1/cardos-tool.1.gz
* /usr/share/man/man1/cryptoflex-tool.1.gz
* /usr/share/man/man1/dnie-tool.1.gz
* /usr/share/man/man1/egk-tool.1.gz
* /usr/share/man/man1/eidenv.1.gz
* /usr/share/man/man1/gids-tool.1.gz
* /usr/share/man/man1/goid-tool.1.gz
* /usr/share/man/man1/iasecc-tool.1.gz
* /usr/share/man/man1/netkey-tool.1.gz
* /usr/share/man/man1/npa-tool.1.gz
* /usr/share/man/man1/openpgp-tool.1.gz
* /usr/share/man/man1/opensc-asn1.1.gz
* /usr/share/man/man1/opensc-explorer.1.gz
* /usr/share/man/man1/opensc-notify.1.gz
* /usr/share/man/man1/opensc-tool.1.gz
* /usr/share/man/man1/piv-tool.1.gz
* /usr/share/man/man1/pkcs11-register.1.gz
* /usr/share/man/man1/pkcs11-tool.1.gz
* /usr/share/man/man1/pkcs15-crypt.1.gz
* /usr/share/man/man1/pkcs15-init.1.gz
* /usr/share/man/man1/pkcs15-tool.1.gz
* /usr/share/man/man1/sc-hsm-tool.1.gz
* /usr/share/man/man1/westcos-tool.1.gz
* /usr/share/man/man5/opensc.conf.5.gz
* /usr/share/man/man5/pkcs15-profile.5.gz
* /usr/share/opensc/asepcos.profile
* /usr/share/opensc/authentic.profile
* /usr/share/opensc/cardos.profile
* /usr/share/opensc/cyberflex.profile
* /usr/share/opensc/entersafe.profile
* /usr/share/opensc/epass2003.profile
* /usr/share/opensc/flex.profile
* /usr/share/opensc/gids.profile
* /usr/share/opensc/gpk.profile
* /usr/share/opensc/iasecc.profile
* /usr/share/opensc/iasecc_admin_eid.profile
* /usr/share/opensc/iasecc_generic_oberthur.profile
* /usr/share/opensc/iasecc_generic_pki.profile
* /usr/share/opensc/ias_adele_admin1.profile
* /usr/share/opensc/ias_adele_admin2.profile
* /usr/share/opensc/ias_adele_common.profile
* /usr/share/opensc/incrypto34.profile
* /usr/share/opensc/isoApplet.profile
* /usr/share/opensc/muscle.profile
* /usr/share/opensc/myeid.profile
* /usr/share/opensc/oberthur.profile
* /usr/share/opensc/openpgp.profile
* /usr/share/opensc/pkcs15.profile
* /usr/share/opensc/rutoken.profile
* /usr/share/opensc/rutoken_ecp.profile
* /usr/share/opensc/rutoken_lite.profile
* /usr/share/opensc/sc-hsm.profile
* /usr/share/opensc/setcos.profile
* /usr/share/opensc/starcos.profile
* /usr/share/opensc/westcos.profile
{{< /files >}}