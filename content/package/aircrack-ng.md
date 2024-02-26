+++
draft = false
title = "aircrack-ng 1.7-4"
version = "1.7-4"
description = "WLAN tools for breaking 802.11 WEP/WPA keys"
date = "2024-01-10T09:26:52"
aliases = "/packages/10380"
categories = ['network-extra']
upstreamurl = "http://www.aircrack-ng.org/"
arch = "x86_64"
size = "408968"
usize = "1487086"
sha1sum = "df0a080f7a7fcc05df45f77c25b8deb5ac7715d4"
depends = "['ethtool', 'iw', 'libnl', 'openssl>=3.1.0', 'sqlite3']"
+++
WLAN tools for breaking 802.11 WEP/WPA keys"

{{< files text="show files" >}}* /usr/bin/airbase-ng
* /usr/bin/aircrack-ng
* /usr/bin/airdecap-ng
* /usr/bin/airdecloak-ng
* /usr/bin/aireplay-ng
* /usr/bin/airmon-ng
* /usr/bin/airodump-ng
* /usr/bin/airodump-ng-oui-update
* /usr/bin/airolib-ng
* /usr/bin/airserv-ng
* /usr/bin/airtun-ng
* /usr/bin/airventriloquist-ng
* /usr/bin/buddy-ng
* /usr/bin/ivstools
* /usr/bin/kstats
* /usr/bin/makeivs-ng
* /usr/bin/packetforge-ng
* /usr/bin/wpaclean
* /usr/include/aircrack-ng/adt/avl_tree.h
* /usr/include/aircrack-ng/adt/circular_buffer.h
* /usr/include/aircrack-ng/adt/circular_queue.h
* /usr/include/aircrack-ng/aircrack-ng.h
* /usr/include/aircrack-ng/ce-wep/uniqueiv.h
* /usr/include/aircrack-ng/ce-wpa/aligned.h
* /usr/include/aircrack-ng/ce-wpa/arch.h
* /usr/include/aircrack-ng/ce-wpa/crypto_engine.h
* /usr/include/aircrack-ng/ce-wpa/jcommon.h
* /usr/include/aircrack-ng/ce-wpa/johnswap.h
* /usr/include/aircrack-ng/ce-wpa/memory.h
* /usr/include/aircrack-ng/ce-wpa/misc.h
* /usr/include/aircrack-ng/ce-wpa/pseudo_intrinsics.h
* /usr/include/aircrack-ng/ce-wpa/simd-intrinsics-load-flags.h
* /usr/include/aircrack-ng/ce-wpa/simd-intrinsics.h
* /usr/include/aircrack-ng/ce-wpa/wpapsk.h
* /usr/include/aircrack-ng/compat.h
* /usr/include/aircrack-ng/cowpatty/cowpatty.h
* /usr/include/aircrack-ng/cpu/cpuset.h
* /usr/include/aircrack-ng/cpu/simd_cpuid.h
* /usr/include/aircrack-ng/cpu/trampoline.h
* /usr/include/aircrack-ng/crypto/crctable.h
* /usr/include/aircrack-ng/crypto/crypto.h
* /usr/include/aircrack-ng/crypto/gcrypt-openssl-wrapper.h
* /usr/include/aircrack-ng/crypto/sha1-git.h
* /usr/include/aircrack-ng/crypto/sha1-sse2.h
* /usr/include/aircrack-ng/defs.h
* /usr/include/aircrack-ng/osdep/byteorder.h
* /usr/include/aircrack-ng/osdep/channel.h
* /usr/include/aircrack-ng/osdep/common.h
* /usr/include/aircrack-ng/osdep/network.h
* /usr/include/aircrack-ng/osdep/osdep.h
* /usr/include/aircrack-ng/osdep/packed.h
* /usr/include/aircrack-ng/ptw/aircrack-ptw-lib.h
* /usr/include/aircrack-ng/support/common.h
* /usr/include/aircrack-ng/support/communications.h
* /usr/include/aircrack-ng/support/crypto_engine_loader.h
* /usr/include/aircrack-ng/support/fragments.h
* /usr/include/aircrack-ng/support/mcs_index_rates.h
* /usr/include/aircrack-ng/support/pcap_local.h
* /usr/include/aircrack-ng/support/station.h
* /usr/include/aircrack-ng/third-party/eapol.h
* /usr/include/aircrack-ng/third-party/ethernet.h
* /usr/include/aircrack-ng/third-party/hashcat.h
* /usr/include/aircrack-ng/third-party/ieee80211.h
* /usr/include/aircrack-ng/third-party/if_arp.h
* /usr/include/aircrack-ng/third-party/if_llc.h
* /usr/include/aircrack-ng/tui/console.h
* /usr/include/aircrack-ng/utf8/verifyssid.h
* /usr/include/aircrack-ng/version.h
* /usr/lib/libaircrack-ce-wpa-1.7.0.so
* /usr/lib/libaircrack-ce-wpa-x86-avx-1.7.0.so
* /usr/lib/libaircrack-ce-wpa-x86-avx.so
* /usr/lib/libaircrack-ce-wpa-x86-avx2-1.7.0.so
* /usr/lib/libaircrack-ce-wpa-x86-avx2.so
* /usr/lib/libaircrack-ce-wpa-x86-sse2-1.7.0.so
* /usr/lib/libaircrack-ce-wpa-x86-sse2.so
* /usr/lib/libaircrack-ce-wpa.so
* /usr/lib/libaircrack-osdep-1.7.0.so
* /usr/lib/libaircrack-osdep.so
* /usr/share/doc/aircrack-ng-1.7/AUTHORS
* /usr/share/doc/aircrack-ng-1.7/ChangeLog
* /usr/share/doc/aircrack-ng-1.7/INSTALLING
* /usr/share/doc/aircrack-ng-1.7/LICENSE
* /usr/share/doc/aircrack-ng-1.7/README
* /usr/share/doc/aircrack-ng-1.7/README.md
* /usr/share/man/man1/aircrack-ng.1.gz
* /usr/share/man/man1/airdecap-ng.1.gz
* /usr/share/man/man1/airdecloak-ng.1.gz
* /usr/share/man/man1/airolib-ng.1.gz
* /usr/share/man/man1/buddy-ng.1.gz
* /usr/share/man/man1/ivstools.1.gz
* /usr/share/man/man1/kstats.1.gz
* /usr/share/man/man1/makeivs-ng.1.gz
* /usr/share/man/man1/packetforge-ng.1.gz
* /usr/share/man/man8/airmon-ng.8.gz
* /usr/share/man/man8/airodump-ng-oui-update.8.gz
{{< /files >}}