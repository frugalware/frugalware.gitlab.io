+++
draft = false
title = "acpi_call 1.1.0-616"
version = "1.1.0-616"
date = "2024-02-02T15:07:43"
categories = ['apps-extra']
upstreamurl = "https://github.com/mkottman/acpi_call"
arch = "x86_64"
size = "27916"
usize = "7870"
sha1sum = "c336a07114c6a62a6ebbece6925b9b8d20407bfe"
depends = "['kernel=6.7.3-1']"
license = "GPL"
files = "['usr/', 'usr/lib/', 'usr/lib/modules/', 'usr/lib/modules/6.7.3-fw1/', 'usr/lib/modules/6.7.3-fw1/kernel/', 'usr/lib/modules/6.7.3-fw1/kernel/drivers/', 'usr/lib/modules/6.7.3-fw1/kernel/drivers/acpi/', 'usr/lib/modules/6.7.3-fw1/kernel/drivers/acpi/acpi_call.ko.zst', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/acpi_call-1.1.0/', 'usr/share/doc/acpi_call-1.1.0/README.md']"
+++
kernel module that enables calls to ACPI methods through /proc/acpi/call