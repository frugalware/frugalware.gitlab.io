+++
draft = false
title = "nss 3.100-1"
version = "3.100-1"
description = "NSS library from mozilla.org"
date = "2024-05-23T07:46:38"
aliases = "/packages/3265"
categories = ['base']
upstreamurl = "http://www.mozilla.org/projects/security/pki/nss/"
arch = "x86_64"
size = "1886784"
usize = "6336149"
sha1sum = "60e2b2482854ddf2e0aaded3aa3e6d8564721375"
depends = "['glibc>=2.35', 'libstdc++>=11.3', 'nspr>=4.34', 'sqlite3>=3.14.2-2', 'zlib>=1.2.12']"
reverse_depends = "['apr-util', 'cef', 'chromium-browser', 'discord', 'firefox', 'libblockdev', 'libfprint', 'liboauth', 'libpurple', 'libreswan', 'networkmanager', 'nvu', 'openjre', 'pesign', 'poppler', 'qca', 'qca-nss', 'qca-qt5', 'qemu', 'qt5-webengine', 'qt6-webengine', 'r2modman', 'slack-desktop', 'teams', 'thunderbird', 'volume_key', 'whalebird', 'xmlsec1']"
license = "GPL"
+++
### Description: 
NSS library from mozilla.org

### Files: 
* /usr/bin/nss-certutil
* /usr/bin/nss-cmsutil
* /usr/bin/nss-config
* /usr/bin/nss-crlutil
* /usr/bin/nss-dbtool
* /usr/bin/nss-hw-support
* /usr/bin/nss-modutil
* /usr/bin/nss-nss
* /usr/bin/nss-pk12util
* /usr/bin/nss-pwdecrypt
* /usr/bin/nss-shlibsign
* /usr/bin/nss-signtool
* /usr/bin/nss-signver
* /usr/bin/nss-ssltap
* /usr/bin/nss-symkeyutil
* /usr/bin/nss-validation
* /usr/include/nss
* /usr/include/nss3/base64.h
* /usr/include/nss3/blapit.h
* /usr/include/nss3/cert.h
* /usr/include/nss3/certdb.h
* /usr/include/nss3/certt.h
* /usr/include/nss3/ciferfam.h
* /usr/include/nss3/cmmf.h
* /usr/include/nss3/cmmft.h
* /usr/include/nss3/cms.h
* /usr/include/nss3/cmsreclist.h
* /usr/include/nss3/cmst.h
* /usr/include/nss3/crmf.h
* /usr/include/nss3/crmft.h
* /usr/include/nss3/cryptohi.h
* /usr/include/nss3/cryptoht.h
* /usr/include/nss3/eccutil.h
* /usr/include/nss3/ecl-exp.h
* /usr/include/nss3/hasht.h
* /usr/include/nss3/jar-ds.h
* /usr/include/nss3/jar.h
* /usr/include/nss3/jarfile.h
* /usr/include/nss3/key.h
* /usr/include/nss3/keyhi.h
* /usr/include/nss3/keyt.h
* /usr/include/nss3/keythi.h
* /usr/include/nss3/kyber.h
* /usr/include/nss3/lowkeyi.h
* /usr/include/nss3/lowkeyti.h
* /usr/include/nss3/nss.h
* /usr/include/nss3/nssb64.h
* /usr/include/nss3/nssb64t.h
* /usr/include/nss3/nssbase.h
* /usr/include/nss3/nssbaset.h
* /usr/include/nss3/nssckbi.h
* /usr/include/nss3/nssckepv.h
* /usr/include/nss3/nssckft.h
* /usr/include/nss3/nssckfw.h
* /usr/include/nss3/nssckfwc.h
* /usr/include/nss3/nssckfwt.h
* /usr/include/nss3/nssckg.h
* /usr/include/nss3/nssckmdt.h
* /usr/include/nss3/nssckt.h
* /usr/include/nss3/nssilckt.h
* /usr/include/nss3/nssilock.h
* /usr/include/nss3/nsslocks.h
* /usr/include/nss3/nsslowhash.h
* /usr/include/nss3/nssrwlk.h
* /usr/include/nss3/nssrwlkt.h
* /usr/include/nss3/nssutil.h
* /usr/include/nss3/ocsp.h
* /usr/include/nss3/ocspt.h
* /usr/include/nss3/p12.h
* /usr/include/nss3/p12plcy.h
* /usr/include/nss3/p12t.h
* /usr/include/nss3/pk11func.h
* /usr/include/nss3/pk11hpke.h
* /usr/include/nss3/pk11pqg.h
* /usr/include/nss3/pk11priv.h
* /usr/include/nss3/pk11pub.h
* /usr/include/nss3/pk11sdr.h
* /usr/include/nss3/pkcs11.h
* /usr/include/nss3/pkcs11f.h
* /usr/include/nss3/pkcs11n.h
* /usr/include/nss3/pkcs11p.h
* /usr/include/nss3/pkcs11t.h
* /usr/include/nss3/pkcs11u.h
* /usr/include/nss3/pkcs11uri.h
* /usr/include/nss3/pkcs12.h
* /usr/include/nss3/pkcs12t.h
* /usr/include/nss3/pkcs1sig.h
* /usr/include/nss3/pkcs7t.h
* /usr/include/nss3/portreg.h
* /usr/include/nss3/preenc.h
* /usr/include/nss3/secasn1.h
* /usr/include/nss3/secasn1t.h
* /usr/include/nss3/seccomon.h
* /usr/include/nss3/secder.h
* /usr/include/nss3/secdert.h
* /usr/include/nss3/secdig.h
* /usr/include/nss3/secdigt.h
* /usr/include/nss3/secerr.h
* /usr/include/nss3/sechash.h
* /usr/include/nss3/secitem.h
* /usr/include/nss3/secmime.h
* /usr/include/nss3/secmod.h
* /usr/include/nss3/secmodt.h
* /usr/include/nss3/secoid.h
* /usr/include/nss3/secoidt.h
* /usr/include/nss3/secpkcs5.h
* /usr/include/nss3/secpkcs7.h
* /usr/include/nss3/secport.h
* /usr/include/nss3/shsign.h
* /usr/include/nss3/smime.h
* /usr/include/nss3/ssl.h
* /usr/include/nss3/sslerr.h
* /usr/include/nss3/sslexp.h
* /usr/include/nss3/sslproto.h
* /usr/include/nss3/sslt.h
* /usr/include/nss3/utilmodt.h
* /usr/include/nss3/utilpars.h
* /usr/include/nss3/utilparst.h
* /usr/include/nss3/utilrename.h
* /usr/lib/libfreebl3.chk
* /usr/lib/libfreebl3.so
* /usr/lib/libfreeblpriv3.chk
* /usr/lib/libfreeblpriv3.so
* /usr/lib/libnss3.so
* /usr/lib/libnssckbi.so
* /usr/lib/libnsssysinit.so
* /usr/lib/libnssutil3.so
* /usr/lib/libsmime3.so
* /usr/lib/libsoftokn3.chk
* /usr/lib/libsoftokn3.so
* /usr/lib/libssl3.so
* /usr/lib/pkgconfig/nss-softokn.pc
* /usr/lib/pkgconfig/nss.pc
* /usr/share/man/man1/certutil.1.gz
* /usr/share/man/man1/cmsutil.1.gz
* /usr/share/man/man1/crlutil.1.gz
* /usr/share/man/man1/derdump.1.gz
* /usr/share/man/man1/modutil.1.gz
* /usr/share/man/man1/pk12util.1.gz
* /usr/share/man/man1/pp.1.gz
* /usr/share/man/man1/signtool.1.gz
* /usr/share/man/man1/signver.1.gz
* /usr/share/man/man1/ssltap.1.gz
* /usr/share/man/man1/vfychain.1.gz
* /usr/share/man/man1/vfyserv.1.gz
