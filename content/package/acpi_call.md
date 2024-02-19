+++
draft = false
title = "acpi_call 1.1.0-618"
version = "1.1.0-618"
date = "2024-02-17T19:06:06"
categories = ['apps-extra']
upstreamurl = "https://github.com/mkottman/acpi_call"
arch = "x86_64"
size = "28024"
usize = "7912"
sha1sum = "c4fb01639a78b0509515be99cc733850663d700a"
depends = "['kernel=6.7.5-1']"
license = "GPL"
files = "['usr/', 'usr/lib/', 'usr/lib/modules/', 'usr/lib/modules/6.7.5-fw1/', 'usr/lib/modules/6.7.5-fw1/kernel/', 'usr/lib/modules/6.7.5-fw1/kernel/drivers/', 'usr/lib/modules/6.7.5-fw1/kernel/drivers/acpi/', 'usr/lib/modules/6.7.5-fw1/kernel/drivers/acpi/acpi_call.ko.zst', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/acpi_call-1.1.0/', 'usr/share/doc/acpi_call-1.1.0/README.md']"
+++
kernel module that enables calls to ACPI methods through /proc/acpi/call