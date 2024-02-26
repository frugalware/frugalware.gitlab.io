+++
draft = false
title = "ndctl 78-2"
version = "78-2"
description = "Utility for managing the libnvdimm sub-system in the Linux kernel"
date = "2024-01-05T15:14:04"
aliases = "/packages/219663"
categories = ['apps']
upstreamurl = "https://github.com/pmem/ndctl"
arch = "x86_64"
size = "292316"
usize = "740634"
sha1sum = "d2256ec4356ee04a9b959d9eb1cb6e5659fa9a74"
depends = "['json-c>=0.14', 'keyutils', 'kmod', 'libdaxctl>=78', 'libndctl>=78', 'libtracefs', 'libudev>=242', 'libuuid']"
+++
### Description: 
Utility for managing the libnvdimm sub-system in the Linux kernel

### Files: 
* /etc/daxctl.conf.d/daxctl.example.conf
* /etc/modprobe.d/nvdimm-security.conf
* /etc/ndctl.conf.d/monitor.conf
* /etc/ndctl.conf.d/ndctl.conf
* /etc/ndctl/keys/keys.readme
* /usr/bin/cxl
* /usr/bin/daxctl
* /usr/bin/ndctl
* /usr/include/cxl/libcxl.h
* /usr/lib/libcxl.so
* /usr/lib/libcxl.so.1
* /usr/lib/libcxl.so.1.0.5
* /usr/lib/pkgconfig/libcxl.pc
* /usr/lib/systemd/system/cxl-monitor.service
* /usr/lib/systemd/system/daxdev-reconfigure@.service
* /usr/lib/systemd/system/ndctl-monitor.service
* /usr/lib/udev/rules.d/90-daxctl-device.rules
* /usr/share/bash-completion/completions/cxl
* /usr/share/bash-completion/completions/daxctl
* /usr/share/bash-completion/completions/ndctl
* /usr/share/daxctl/daxctl.conf
* /usr/share/doc/ndctl-78/COPYING
* /usr/share/doc/ndctl-78/README.md
* /usr/share/man/man1/cxl-create-region.1.gz
* /usr/share/man/man1/cxl-destroy-region.1.gz
* /usr/share/man/man1/cxl-disable-bus.1.gz
* /usr/share/man/man1/cxl-disable-memdev.1.gz
* /usr/share/man/man1/cxl-disable-port.1.gz
* /usr/share/man/man1/cxl-disable-region.1.gz
* /usr/share/man/man1/cxl-enable-memdev.1.gz
* /usr/share/man/man1/cxl-enable-port.1.gz
* /usr/share/man/man1/cxl-enable-region.1.gz
* /usr/share/man/man1/cxl-free-dpa.1.gz
* /usr/share/man/man1/cxl-list.1.gz
* /usr/share/man/man1/cxl-monitor.1.gz
* /usr/share/man/man1/cxl-read-labels.1.gz
* /usr/share/man/man1/cxl-reserve-dpa.1.gz
* /usr/share/man/man1/cxl-set-partition.1.gz
* /usr/share/man/man1/cxl-update-firmware.1.gz
* /usr/share/man/man1/cxl-write-labels.1.gz
* /usr/share/man/man1/cxl-zero-labels.1.gz
* /usr/share/man/man1/cxl.1.gz
* /usr/share/man/man1/daxctl-create-device.1.gz
* /usr/share/man/man1/daxctl-destroy-device.1.gz
* /usr/share/man/man1/daxctl-disable-device.1.gz
* /usr/share/man/man1/daxctl-enable-device.1.gz
* /usr/share/man/man1/daxctl-list.1.gz
* /usr/share/man/man1/daxctl-migrate-device-model.1.gz
* /usr/share/man/man1/daxctl-offline-memory.1.gz
* /usr/share/man/man1/daxctl-online-memory.1.gz
* /usr/share/man/man1/daxctl-reconfigure-device.1.gz
* /usr/share/man/man1/daxctl.1.gz
* /usr/share/man/man1/ndctl-activate-firmware.1.gz
* /usr/share/man/man1/ndctl-check-labels.1.gz
* /usr/share/man/man1/ndctl-check-namespace.1.gz
* /usr/share/man/man1/ndctl-clear-errors.1.gz
* /usr/share/man/man1/ndctl-create-namespace.1.gz
* /usr/share/man/man1/ndctl-destroy-namespace.1.gz
* /usr/share/man/man1/ndctl-disable-dimm.1.gz
* /usr/share/man/man1/ndctl-disable-namespace.1.gz
* /usr/share/man/man1/ndctl-disable-region.1.gz
* /usr/share/man/man1/ndctl-enable-dimm.1.gz
* /usr/share/man/man1/ndctl-enable-namespace.1.gz
* /usr/share/man/man1/ndctl-enable-region.1.gz
* /usr/share/man/man1/ndctl-freeze-security.1.gz
* /usr/share/man/man1/ndctl-init-labels.1.gz
* /usr/share/man/man1/ndctl-inject-error.1.gz
* /usr/share/man/man1/ndctl-inject-smart.1.gz
* /usr/share/man/man1/ndctl-list.1.gz
* /usr/share/man/man1/ndctl-load-keys.1.gz
* /usr/share/man/man1/ndctl-monitor.1.gz
* /usr/share/man/man1/ndctl-read-infoblock.1.gz
* /usr/share/man/man1/ndctl-read-labels.1.gz
* /usr/share/man/man1/ndctl-remove-passphrase.1.gz
* /usr/share/man/man1/ndctl-sanitize-dimm.1.gz
* /usr/share/man/man1/ndctl-setup-passphrase.1.gz
* /usr/share/man/man1/ndctl-start-scrub.1.gz
* /usr/share/man/man1/ndctl-update-firmware.1.gz
* /usr/share/man/man1/ndctl-update-passphrase.1.gz
* /usr/share/man/man1/ndctl-wait-overwrite.1.gz
* /usr/share/man/man1/ndctl-wait-scrub.1.gz
* /usr/share/man/man1/ndctl-write-infoblock.1.gz
* /usr/share/man/man1/ndctl-write-labels.1.gz
* /usr/share/man/man1/ndctl-zero-labels.1.gz
* /usr/share/man/man1/ndctl.1.gz
* /usr/share/man/man3/cxl_new.3.gz
* /usr/share/man/man3/libcxl.3.gz
