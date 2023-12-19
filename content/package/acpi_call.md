+++
draft = false
title = "acpi_call 1.1.0-608"
version = "1.1.0-608"
date = "2023-12-13T20:36:34"
categories = ['apps-extra']
upstreamurl = "https://github.com/mkottman/acpi_call"
arch = "x86_64"
size = "27680"
usize = "7858"
sha1sum = "d887963138eda76395a3fcd83d79a63464dd5c62"
depends = "['kernel=6.6.7-1']"
license = "GPL"
files = "['lib/', 'lib/modules/', 'lib/modules/6.6.7-fw1/', 'lib/modules/6.6.7-fw1/kernel/', 'lib/modules/6.6.7-fw1/kernel/drivers/', 'lib/modules/6.6.7-fw1/kernel/drivers/acpi/', 'lib/modules/6.6.7-fw1/kernel/drivers/acpi/acpi_call.ko.zst', 'usr/', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/acpi_call-1.1.0/', 'usr/share/doc/acpi_call-1.1.0/README.md']"
+++
kernel module that enables calls to ACPI methods through /proc/acpi/call