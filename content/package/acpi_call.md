+++
draft = false
title = "acpi_call 1.1.0-617"
version = "1.1.0-617"
date = "2024-02-06T10:31:04"
categories = ['apps-extra']
upstreamurl = "https://github.com/mkottman/acpi_call"
arch = "x86_64"
size = "27948"
usize = "7872"
sha1sum = "1b3caf1955023ebd9f02a88c67961da95587134d"
depends = "['kernel=6.7.4-1']"
license = "GPL"
files = "['usr/', 'usr/lib/', 'usr/lib/modules/', 'usr/lib/modules/6.7.4-fw1/', 'usr/lib/modules/6.7.4-fw1/kernel/', 'usr/lib/modules/6.7.4-fw1/kernel/drivers/', 'usr/lib/modules/6.7.4-fw1/kernel/drivers/acpi/', 'usr/lib/modules/6.7.4-fw1/kernel/drivers/acpi/acpi_call.ko.zst', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/acpi_call-1.1.0/', 'usr/share/doc/acpi_call-1.1.0/README.md']"
+++
kernel module that enables calls to ACPI methods through /proc/acpi/call