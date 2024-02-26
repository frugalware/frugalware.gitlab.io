+++
draft = false
title = "lib32-nss 3.98-1"
version = "3.98-1"
description = "NSS library from mozilla.org ( 32bit )"
date = "2024-02-17T22:12:19"
aliases = "/packages/218950"
categories = ['lib32-extra']
upstreamurl = "http://www.mozilla.org/projects/security/pki/nss/"
arch = "x86_64"
size = "1861088"
usize = "6262460"
sha1sum = "fff90f8446bb29d20d2b7153f253ad7d64c58bdf"
depends = "['lib32-nspr>=4.34', 'lib32-sqlite3>=3.14.2-2', 'lib32-zlib>=1.2.12']"
reverse_depends = "['lib32-networkmanager', 'steam-native']"
+++
NSS library from mozilla.org ( 32bit )

{{< files text="show files" >}}* /usr/i686-frugalware-linux/bin/nss
* /usr/i686-frugalware-linux/bin/nss-certutil
* /usr/i686-frugalware-linux/bin/nss-cmsutil
* /usr/i686-frugalware-linux/bin/nss-config
* /usr/i686-frugalware-linux/bin/nss-crlutil
* /usr/i686-frugalware-linux/bin/nss-dbtool
* /usr/i686-frugalware-linux/bin/nss-hw-support
* /usr/i686-frugalware-linux/bin/nss-modutil
* /usr/i686-frugalware-linux/bin/nss-pk12util
* /usr/i686-frugalware-linux/bin/nss-pwdecrypt
* /usr/i686-frugalware-linux/bin/nss-shlibsign
* /usr/i686-frugalware-linux/bin/nss-signtool
* /usr/i686-frugalware-linux/bin/nss-signver
* /usr/i686-frugalware-linux/bin/nss-ssltap
* /usr/i686-frugalware-linux/bin/nss-symkeyutil
* /usr/i686-frugalware-linux/bin/nss-validation
* /usr/i686-frugalware-linux/include/nss3/base64.h
* /usr/i686-frugalware-linux/include/nss3/blapit.h
* /usr/i686-frugalware-linux/include/nss3/cert.h
* /usr/i686-frugalware-linux/include/nss3/certdb.h
* /usr/i686-frugalware-linux/include/nss3/certt.h
* /usr/i686-frugalware-linux/include/nss3/ciferfam.h
* /usr/i686-frugalware-linux/include/nss3/cmmf.h
* /usr/i686-frugalware-linux/include/nss3/cmmft.h
* /usr/i686-frugalware-linux/include/nss3/cms.h
* /usr/i686-frugalware-linux/include/nss3/cmsreclist.h
* /usr/i686-frugalware-linux/include/nss3/cmst.h
* /usr/i686-frugalware-linux/include/nss3/crmf.h
* /usr/i686-frugalware-linux/include/nss3/crmft.h
* /usr/i686-frugalware-linux/include/nss3/cryptohi.h
* /usr/i686-frugalware-linux/include/nss3/cryptoht.h
* /usr/i686-frugalware-linux/include/nss3/eccutil.h
* /usr/i686-frugalware-linux/include/nss3/ecl-exp.h
* /usr/i686-frugalware-linux/include/nss3/hasht.h
* /usr/i686-frugalware-linux/include/nss3/jar-ds.h
* /usr/i686-frugalware-linux/include/nss3/jar.h
* /usr/i686-frugalware-linux/include/nss3/jarfile.h
* /usr/i686-frugalware-linux/include/nss3/key.h
* /usr/i686-frugalware-linux/include/nss3/keyhi.h
* /usr/i686-frugalware-linux/include/nss3/keyt.h
* /usr/i686-frugalware-linux/include/nss3/keythi.h
* /usr/i686-frugalware-linux/include/nss3/kyber.h
* /usr/i686-frugalware-linux/include/nss3/lowkeyi.h
* /usr/i686-frugalware-linux/include/nss3/lowkeyti.h
* /usr/i686-frugalware-linux/include/nss3/nss.h
* /usr/i686-frugalware-linux/include/nss3/nssb64.h
* /usr/i686-frugalware-linux/include/nss3/nssb64t.h
* /usr/i686-frugalware-linux/include/nss3/nssbase.h
* /usr/i686-frugalware-linux/include/nss3/nssbaset.h
* /usr/i686-frugalware-linux/include/nss3/nssckbi.h
* /usr/i686-frugalware-linux/include/nss3/nssckepv.h
* /usr/i686-frugalware-linux/include/nss3/nssckft.h
* /usr/i686-frugalware-linux/include/nss3/nssckfw.h
* /usr/i686-frugalware-linux/include/nss3/nssckfwc.h
* /usr/i686-frugalware-linux/include/nss3/nssckfwt.h
* /usr/i686-frugalware-linux/include/nss3/nssckg.h
* /usr/i686-frugalware-linux/include/nss3/nssckmdt.h
* /usr/i686-frugalware-linux/include/nss3/nssckt.h
* /usr/i686-frugalware-linux/include/nss3/nssilckt.h
* /usr/i686-frugalware-linux/include/nss3/nssilock.h
* /usr/i686-frugalware-linux/include/nss3/nsslocks.h
* /usr/i686-frugalware-linux/include/nss3/nsslowhash.h
* /usr/i686-frugalware-linux/include/nss3/nssrwlk.h
* /usr/i686-frugalware-linux/include/nss3/nssrwlkt.h
* /usr/i686-frugalware-linux/include/nss3/nssutil.h
* /usr/i686-frugalware-linux/include/nss3/ocsp.h
* /usr/i686-frugalware-linux/include/nss3/ocspt.h
* /usr/i686-frugalware-linux/include/nss3/p12.h
* /usr/i686-frugalware-linux/include/nss3/p12plcy.h
* /usr/i686-frugalware-linux/include/nss3/p12t.h
* /usr/i686-frugalware-linux/include/nss3/pk11func.h
* /usr/i686-frugalware-linux/include/nss3/pk11hpke.h
* /usr/i686-frugalware-linux/include/nss3/pk11pqg.h
* /usr/i686-frugalware-linux/include/nss3/pk11priv.h
* /usr/i686-frugalware-linux/include/nss3/pk11pub.h
* /usr/i686-frugalware-linux/include/nss3/pk11sdr.h
* /usr/i686-frugalware-linux/include/nss3/pkcs11.h
* /usr/i686-frugalware-linux/include/nss3/pkcs11f.h
* /usr/i686-frugalware-linux/include/nss3/pkcs11n.h
* /usr/i686-frugalware-linux/include/nss3/pkcs11p.h
* /usr/i686-frugalware-linux/include/nss3/pkcs11t.h
* /usr/i686-frugalware-linux/include/nss3/pkcs11u.h
* /usr/i686-frugalware-linux/include/nss3/pkcs11uri.h
* /usr/i686-frugalware-linux/include/nss3/pkcs12.h
* /usr/i686-frugalware-linux/include/nss3/pkcs12t.h
* /usr/i686-frugalware-linux/include/nss3/pkcs1sig.h
* /usr/i686-frugalware-linux/include/nss3/pkcs7t.h
* /usr/i686-frugalware-linux/include/nss3/portreg.h
* /usr/i686-frugalware-linux/include/nss3/preenc.h
* /usr/i686-frugalware-linux/include/nss3/secasn1.h
* /usr/i686-frugalware-linux/include/nss3/secasn1t.h
* /usr/i686-frugalware-linux/include/nss3/seccomon.h
* /usr/i686-frugalware-linux/include/nss3/secder.h
* /usr/i686-frugalware-linux/include/nss3/secdert.h
* /usr/i686-frugalware-linux/include/nss3/secdig.h
* /usr/i686-frugalware-linux/include/nss3/secdigt.h
* /usr/i686-frugalware-linux/include/nss3/secerr.h
* /usr/i686-frugalware-linux/include/nss3/sechash.h
* /usr/i686-frugalware-linux/include/nss3/secitem.h
* /usr/i686-frugalware-linux/include/nss3/secmime.h
* /usr/i686-frugalware-linux/include/nss3/secmod.h
* /usr/i686-frugalware-linux/include/nss3/secmodt.h
* /usr/i686-frugalware-linux/include/nss3/secoid.h
* /usr/i686-frugalware-linux/include/nss3/secoidt.h
* /usr/i686-frugalware-linux/include/nss3/secpkcs5.h
* /usr/i686-frugalware-linux/include/nss3/secpkcs7.h
* /usr/i686-frugalware-linux/include/nss3/secport.h
* /usr/i686-frugalware-linux/include/nss3/shsign.h
* /usr/i686-frugalware-linux/include/nss3/smime.h
* /usr/i686-frugalware-linux/include/nss3/ssl.h
* /usr/i686-frugalware-linux/include/nss3/sslerr.h
* /usr/i686-frugalware-linux/include/nss3/sslexp.h
* /usr/i686-frugalware-linux/include/nss3/sslproto.h
* /usr/i686-frugalware-linux/include/nss3/sslt.h
* /usr/i686-frugalware-linux/include/nss3/utilmodt.h
* /usr/i686-frugalware-linux/include/nss3/utilpars.h
* /usr/i686-frugalware-linux/include/nss3/utilparst.h
* /usr/i686-frugalware-linux/include/nss3/utilrename.h
* /usr/lib32/libfreebl3.chk
* /usr/lib32/libfreebl3.so
* /usr/lib32/libfreeblpriv3.chk
* /usr/lib32/libfreeblpriv3.so
* /usr/lib32/libnss3.so
* /usr/lib32/libnssckbi.so
* /usr/lib32/libnsssysinit.so
* /usr/lib32/libnssutil3.so
* /usr/lib32/libsmime3.so
* /usr/lib32/libsoftokn3.chk
* /usr/lib32/libsoftokn3.so
* /usr/lib32/libssl3.so
* /usr/lib32/pkgconfig/nss.pc
{{< /files >}}