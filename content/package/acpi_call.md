+++
draft = false
title = "acpi_call 1.1.0-619"
version = "1.1.0-619"
date = "2024-02-23T18:59:02"
categories = ['apps-extra']
upstreamurl = "https://github.com/mkottman/acpi_call"
arch = "x86_64"
size = "28052"
usize = "7911"
sha1sum = "da1377d1f59234ae6abcf7042f9e840b4b35e357"
depends = "['kernel=6.7.6-1']"
license = "GPL"
files = "['usr/', 'usr/lib/', 'usr/lib/modules/', 'usr/lib/modules/6.7.6-fw1/', 'usr/lib/modules/6.7.6-fw1/kernel/', 'usr/lib/modules/6.7.6-fw1/kernel/drivers/', 'usr/lib/modules/6.7.6-fw1/kernel/drivers/acpi/', 'usr/lib/modules/6.7.6-fw1/kernel/drivers/acpi/acpi_call.ko.zst', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/acpi_call-1.1.0/', 'usr/share/doc/acpi_call-1.1.0/README.md']"
+++
kernel module that enables calls to ACPI methods through /proc/acpi/call