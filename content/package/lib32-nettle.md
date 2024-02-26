+++
draft = false
title = "lib32-nettle 3.9.1-1"
version = "3.9.1-1"
description = "A low-level cryptographic library ( 32bit )"
date = "2023-06-02T13:51:18"
aliases = "/packages/217894"
categories = ['lib32-extra']
upstreamurl = "http://www.lysator.liu.se/~nisse/nettle/"
arch = "x86_64"
size = "487180"
usize = "1448601"
sha1sum = "889313a02e1a4905d93865a3c790a96af288c840"
depends = "['lib32-gmp>=6.1.2-12']"
reverse_depends = "['lib32-gnutls', 'lib32-libcurl-gnutls']"
+++
A low-level cryptographic library ( 32bit )"

{{< files text="show files" >}}* /usr/i686-frugalware-linux/bin/nettle-hash
* /usr/i686-frugalware-linux/bin/nettle-lfib-stream
* /usr/i686-frugalware-linux/bin/nettle-pbkdf2
* /usr/i686-frugalware-linux/bin/pkcs1-conv
* /usr/i686-frugalware-linux/bin/sexp-conv
* /usr/i686-frugalware-linux/include/nettle/aes.h
* /usr/i686-frugalware-linux/include/nettle/arcfour.h
* /usr/i686-frugalware-linux/include/nettle/arctwo.h
* /usr/i686-frugalware-linux/include/nettle/asn1.h
* /usr/i686-frugalware-linux/include/nettle/balloon.h
* /usr/i686-frugalware-linux/include/nettle/base16.h
* /usr/i686-frugalware-linux/include/nettle/base64.h
* /usr/i686-frugalware-linux/include/nettle/bignum.h
* /usr/i686-frugalware-linux/include/nettle/blowfish.h
* /usr/i686-frugalware-linux/include/nettle/buffer.h
* /usr/i686-frugalware-linux/include/nettle/camellia.h
* /usr/i686-frugalware-linux/include/nettle/cast128.h
* /usr/i686-frugalware-linux/include/nettle/cbc.h
* /usr/i686-frugalware-linux/include/nettle/ccm.h
* /usr/i686-frugalware-linux/include/nettle/cfb.h
* /usr/i686-frugalware-linux/include/nettle/chacha-poly1305.h
* /usr/i686-frugalware-linux/include/nettle/chacha.h
* /usr/i686-frugalware-linux/include/nettle/cmac.h
* /usr/i686-frugalware-linux/include/nettle/ctr.h
* /usr/i686-frugalware-linux/include/nettle/curve25519.h
* /usr/i686-frugalware-linux/include/nettle/curve448.h
* /usr/i686-frugalware-linux/include/nettle/des.h
* /usr/i686-frugalware-linux/include/nettle/dsa-compat.h
* /usr/i686-frugalware-linux/include/nettle/dsa.h
* /usr/i686-frugalware-linux/include/nettle/eax.h
* /usr/i686-frugalware-linux/include/nettle/ecc-curve.h
* /usr/i686-frugalware-linux/include/nettle/ecc.h
* /usr/i686-frugalware-linux/include/nettle/ecdsa.h
* /usr/i686-frugalware-linux/include/nettle/eddsa.h
* /usr/i686-frugalware-linux/include/nettle/gcm.h
* /usr/i686-frugalware-linux/include/nettle/gostdsa.h
* /usr/i686-frugalware-linux/include/nettle/gosthash94.h
* /usr/i686-frugalware-linux/include/nettle/hkdf.h
* /usr/i686-frugalware-linux/include/nettle/hmac.h
* /usr/i686-frugalware-linux/include/nettle/knuth-lfib.h
* /usr/i686-frugalware-linux/include/nettle/macros.h
* /usr/i686-frugalware-linux/include/nettle/md2.h
* /usr/i686-frugalware-linux/include/nettle/md4.h
* /usr/i686-frugalware-linux/include/nettle/md5-compat.h
* /usr/i686-frugalware-linux/include/nettle/md5.h
* /usr/i686-frugalware-linux/include/nettle/memops.h
* /usr/i686-frugalware-linux/include/nettle/memxor.h
* /usr/i686-frugalware-linux/include/nettle/nettle-meta.h
* /usr/i686-frugalware-linux/include/nettle/nettle-types.h
* /usr/i686-frugalware-linux/include/nettle/nist-keywrap.h
* /usr/i686-frugalware-linux/include/nettle/ocb.h
* /usr/i686-frugalware-linux/include/nettle/pbkdf2.h
* /usr/i686-frugalware-linux/include/nettle/pgp.h
* /usr/i686-frugalware-linux/include/nettle/pkcs1.h
* /usr/i686-frugalware-linux/include/nettle/poly1305.h
* /usr/i686-frugalware-linux/include/nettle/pss-mgf1.h
* /usr/i686-frugalware-linux/include/nettle/pss.h
* /usr/i686-frugalware-linux/include/nettle/realloc.h
* /usr/i686-frugalware-linux/include/nettle/ripemd160.h
* /usr/i686-frugalware-linux/include/nettle/rsa.h
* /usr/i686-frugalware-linux/include/nettle/salsa20.h
* /usr/i686-frugalware-linux/include/nettle/serpent.h
* /usr/i686-frugalware-linux/include/nettle/sexp.h
* /usr/i686-frugalware-linux/include/nettle/sha.h
* /usr/i686-frugalware-linux/include/nettle/sha1.h
* /usr/i686-frugalware-linux/include/nettle/sha2.h
* /usr/i686-frugalware-linux/include/nettle/sha3.h
* /usr/i686-frugalware-linux/include/nettle/siv-cmac.h
* /usr/i686-frugalware-linux/include/nettle/siv-gcm.h
* /usr/i686-frugalware-linux/include/nettle/sm3.h
* /usr/i686-frugalware-linux/include/nettle/sm4.h
* /usr/i686-frugalware-linux/include/nettle/streebog.h
* /usr/i686-frugalware-linux/include/nettle/twofish.h
* /usr/i686-frugalware-linux/include/nettle/umac.h
* /usr/i686-frugalware-linux/include/nettle/version.h
* /usr/i686-frugalware-linux/include/nettle/xts.h
* /usr/i686-frugalware-linux/include/nettle/yarrow.h
* /usr/lib32/libhogweed.so
* /usr/lib32/libhogweed.so.6
* /usr/lib32/libhogweed.so.6.8
* /usr/lib32/libnettle.so
* /usr/lib32/libnettle.so.8
* /usr/lib32/libnettle.so.8.8
* /usr/lib32/pkgconfig/hogweed.pc
* /usr/lib32/pkgconfig/nettle.pc
{{< /files >}}