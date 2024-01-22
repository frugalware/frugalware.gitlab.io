+++
draft = false
title = "acpi_call 1.1.0-614"
version = "1.1.0-614"
date = "2024-01-22T14:40:29"
categories = ['apps-extra']
upstreamurl = "https://github.com/mkottman/acpi_call"
arch = "x86_64"
size = "27848"
usize = "7867"
sha1sum = "84ec690f7ed3cd532babefd5ce27add3eae90c99"
depends = "['kernel=6.7.1-1']"
license = "GPL"
files = "['usr/', 'usr/lib/', 'usr/lib/modules/', 'usr/lib/modules/6.7.1-fw1/', 'usr/lib/modules/6.7.1-fw1/kernel/', 'usr/lib/modules/6.7.1-fw1/kernel/drivers/', 'usr/lib/modules/6.7.1-fw1/kernel/drivers/acpi/', 'usr/lib/modules/6.7.1-fw1/kernel/drivers/acpi/acpi_call.ko.zst', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/acpi_call-1.1.0/', 'usr/share/doc/acpi_call-1.1.0/README.md']"
+++
kernel module that enables calls to ACPI methods through /proc/acpi/call