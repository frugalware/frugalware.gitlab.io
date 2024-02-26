+++
draft = false
title = "mbedtls 2.28.4-2"
version = "2.28.4-2"
description = "Portable cryptographic and SSL/TLS library, aka polarssl"
date = "2023-09-05T11:21:45"
aliases = "/packages/218827"
categories = ['lib']
upstreamurl = "https://tls.mbed.org"
arch = "x86_64"
size = "761500"
usize = "4500544"
sha1sum = "9c0d34ba150ed6b312ea2be5dc2a9543a37229c4"
depends = "['glibc>=2.34']"
reverse_depends = "['bctoolbox', 'julia', 'librist', 'neko', 'obs-studio', 'openrgb']"
+++
Portable cryptographic and SSL/TLS library, aka polarssl"

{{< files text="show files" >}}* /usr/bin/mbedtls_benchmark
* /usr/bin/mbedtls_cert_app
* /usr/bin/mbedtls_cert_req
* /usr/bin/mbedtls_cert_write
* /usr/bin/mbedtls_crl_app
* /usr/bin/mbedtls_crypto_examples
* /usr/bin/mbedtls_crypt_and_hash
* /usr/bin/mbedtls_dh_client
* /usr/bin/mbedtls_dh_genprime
* /usr/bin/mbedtls_dh_server
* /usr/bin/mbedtls_dlopen
* /usr/bin/mbedtls_dlopen_demo.sh
* /usr/bin/mbedtls_dtls_client
* /usr/bin/mbedtls_dtls_server
* /usr/bin/mbedtls_ecdh_curve25519
* /usr/bin/mbedtls_ecdsa
* /usr/bin/mbedtls_fuzz_client
* /usr/bin/mbedtls_fuzz_dtlsclient
* /usr/bin/mbedtls_fuzz_dtlsserver
* /usr/bin/mbedtls_fuzz_privkey
* /usr/bin/mbedtls_fuzz_pubkey
* /usr/bin/mbedtls_fuzz_server
* /usr/bin/mbedtls_fuzz_x509crl
* /usr/bin/mbedtls_fuzz_x509crt
* /usr/bin/mbedtls_fuzz_x509csr
* /usr/bin/mbedtls_generate_cpp_dummy_build.sh
* /usr/bin/mbedtls_generic_sum
* /usr/bin/mbedtls_gen_entropy
* /usr/bin/mbedtls_gen_key
* /usr/bin/mbedtls_gen_random_ctr_drbg
* /usr/bin/mbedtls_gen_random_havege
* /usr/bin/mbedtls_hello
* /usr/bin/mbedtls_key_app
* /usr/bin/mbedtls_key_app_writer
* /usr/bin/mbedtls_key_ladder_demo
* /usr/bin/mbedtls_key_ladder_demo.sh
* /usr/bin/mbedtls_load_roots
* /usr/bin/mbedtls_mini_client
* /usr/bin/mbedtls_mpi_demo
* /usr/bin/mbedtls_pem2der
* /usr/bin/mbedtls_pk_decrypt
* /usr/bin/mbedtls_pk_encrypt
* /usr/bin/mbedtls_pk_sign
* /usr/bin/mbedtls_pk_verify
* /usr/bin/mbedtls_psa_constant_names
* /usr/bin/mbedtls_query_compile_time_config
* /usr/bin/mbedtls_req_app
* /usr/bin/mbedtls_rsa_decrypt
* /usr/bin/mbedtls_rsa_encrypt
* /usr/bin/mbedtls_rsa_genkey
* /usr/bin/mbedtls_rsa_sign
* /usr/bin/mbedtls_rsa_sign_pss
* /usr/bin/mbedtls_rsa_verify
* /usr/bin/mbedtls_rsa_verify_pss
* /usr/bin/mbedtls_selftest
* /usr/bin/mbedtls_ssl_client1
* /usr/bin/mbedtls_ssl_client2
* /usr/bin/mbedtls_ssl_context_info
* /usr/bin/mbedtls_ssl_fork_server
* /usr/bin/mbedtls_ssl_mail_client
* /usr/bin/mbedtls_ssl_server
* /usr/bin/mbedtls_ssl_server2
* /usr/bin/mbedtls_strerror
* /usr/bin/mbedtls_udp_proxy
* /usr/bin/mbedtls_udp_proxy_wrapper.sh
* /usr/bin/mbedtls_zeroize
* /usr/include/mbedtls/aes.h
* /usr/include/mbedtls/aesni.h
* /usr/include/mbedtls/arc4.h
* /usr/include/mbedtls/aria.h
* /usr/include/mbedtls/asn1.h
* /usr/include/mbedtls/asn1write.h
* /usr/include/mbedtls/base64.h
* /usr/include/mbedtls/bignum.h
* /usr/include/mbedtls/blowfish.h
* /usr/include/mbedtls/bn_mul.h
* /usr/include/mbedtls/camellia.h
* /usr/include/mbedtls/ccm.h
* /usr/include/mbedtls/certs.h
* /usr/include/mbedtls/chacha20.h
* /usr/include/mbedtls/chachapoly.h
* /usr/include/mbedtls/check_config.h
* /usr/include/mbedtls/cipher.h
* /usr/include/mbedtls/cipher_internal.h
* /usr/include/mbedtls/cmac.h
* /usr/include/mbedtls/compat-1.3.h
* /usr/include/mbedtls/config.h
* /usr/include/mbedtls/config_psa.h
* /usr/include/mbedtls/constant_time.h
* /usr/include/mbedtls/ctr_drbg.h
* /usr/include/mbedtls/debug.h
* /usr/include/mbedtls/des.h
* /usr/include/mbedtls/dhm.h
* /usr/include/mbedtls/ecdh.h
* /usr/include/mbedtls/ecdsa.h
* /usr/include/mbedtls/ecjpake.h
* /usr/include/mbedtls/ecp.h
* /usr/include/mbedtls/ecp_internal.h
* /usr/include/mbedtls/entropy.h
* /usr/include/mbedtls/entropy_poll.h
* /usr/include/mbedtls/error.h
* /usr/include/mbedtls/gcm.h
* /usr/include/mbedtls/havege.h
* /usr/include/mbedtls/hkdf.h
* /usr/include/mbedtls/hmac_drbg.h
* /usr/include/mbedtls/md.h
* /usr/include/mbedtls/md2.h
* /usr/include/mbedtls/md4.h
* /usr/include/mbedtls/md5.h
* /usr/include/mbedtls/md_internal.h
* /usr/include/mbedtls/memory_buffer_alloc.h
* /usr/include/mbedtls/net.h
* /usr/include/mbedtls/net_sockets.h
* /usr/include/mbedtls/nist_kw.h
* /usr/include/mbedtls/oid.h
* /usr/include/mbedtls/padlock.h
* /usr/include/mbedtls/pem.h
* /usr/include/mbedtls/pk.h
* /usr/include/mbedtls/pkcs11.h
* /usr/include/mbedtls/pkcs12.h
* /usr/include/mbedtls/pkcs5.h
* /usr/include/mbedtls/pk_internal.h
* /usr/include/mbedtls/platform.h
* /usr/include/mbedtls/platform_time.h
* /usr/include/mbedtls/platform_util.h
* /usr/include/mbedtls/poly1305.h
* /usr/include/mbedtls/psa_util.h
* /usr/include/mbedtls/ripemd160.h
* /usr/include/mbedtls/rsa.h
* /usr/include/mbedtls/rsa_internal.h
* /usr/include/mbedtls/sha1.h
* /usr/include/mbedtls/sha256.h
* /usr/include/mbedtls/sha512.h
* /usr/include/mbedtls/ssl.h
* /usr/include/mbedtls/ssl_cache.h
* /usr/include/mbedtls/ssl_ciphersuites.h
* /usr/include/mbedtls/ssl_cookie.h
* /usr/include/mbedtls/ssl_internal.h
* /usr/include/mbedtls/ssl_ticket.h
* /usr/include/mbedtls/threading.h
* /usr/include/mbedtls/timing.h
* /usr/include/mbedtls/version.h
* /usr/include/mbedtls/x509.h
* /usr/include/mbedtls/x509_crl.h
* /usr/include/mbedtls/x509_crt.h
* /usr/include/mbedtls/x509_csr.h
* /usr/include/mbedtls/xtea.h
* /usr/include/psa/crypto.h
* /usr/include/psa/crypto_builtin_composites.h
* /usr/include/psa/crypto_builtin_primitives.h
* /usr/include/psa/crypto_compat.h
* /usr/include/psa/crypto_config.h
* /usr/include/psa/crypto_driver_common.h
* /usr/include/psa/crypto_driver_contexts_composites.h
* /usr/include/psa/crypto_driver_contexts_primitives.h
* /usr/include/psa/crypto_extra.h
* /usr/include/psa/crypto_platform.h
* /usr/include/psa/crypto_se_driver.h
* /usr/include/psa/crypto_sizes.h
* /usr/include/psa/crypto_struct.h
* /usr/include/psa/crypto_types.h
* /usr/include/psa/crypto_values.h
* /usr/lib/libmbedcrypto.so
* /usr/lib/libmbedcrypto.so.7
* /usr/lib/libmbedtls.so
* /usr/lib/libmbedtls.so.14
* /usr/lib/libmbedx509.so
* /usr/lib/libmbedx509.so.1
* /usr/share/doc/mbedtls-2.28.4/BUGS.md
* /usr/share/doc/mbedtls-2.28.4/ChangeLog
* /usr/share/doc/mbedtls-2.28.4/LICENSE
* /usr/share/doc/mbedtls-2.28.4/README.md
{{< /files >}}