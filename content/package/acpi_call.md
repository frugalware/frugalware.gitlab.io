+++
draft = false
title = "acpi_call 1.1.0-605"
version = "1.1.0-605"
date = "2023-12-03T13:14:17"
categories = ['apps-extra']
upstreamurl = "https://github.com/mkottman/acpi_call"
arch = "x86_64"
size = "27608"
usize = "7855"
sha1sum = "8076eb482a370c79ed3e90171243fb61c7e567eb"
depends = "['kernel=6.6.4-1']"
license = "GPL"
files = "['lib/', 'lib/modules/', 'lib/modules/6.6.4-fw1/', 'lib/modules/6.6.4-fw1/kernel/', 'lib/modules/6.6.4-fw1/kernel/drivers/', 'lib/modules/6.6.4-fw1/kernel/drivers/acpi/', 'lib/modules/6.6.4-fw1/kernel/drivers/acpi/acpi_call.ko.zst', 'usr/', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/acpi_call-1.1.0/', 'usr/share/doc/acpi_call-1.1.0/README.md']"
+++
kernel module that enables calls to ACPI methods through /proc/acpi/call