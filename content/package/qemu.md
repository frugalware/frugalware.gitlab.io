+++
draft = false
title = "qemu 10.0.2-2"
version = "10.0.2-2"
description = "QEMU is a FAST! processor emulator"
date = "2025-06-23T14:36:04"
aliases = "/packages/3815"
categories = ['xapps-extra']
upstreamurl = "http://www.nongnu.org/qemu/"
arch = "x86_64"
size = "119853340"
usize = "540401294"
sha1sum = "cf4056b93433cfd85be9adf223b41785d9d19cc3"
depends = "['alsa-lib', 'bluez', 'curl', 'cyrus-sasl', 'dtc', 'edk2', 'fuse3', 'gperftools', 'libaio', 'libbpf', 'libcbor', 'libepoxy', 'libgbm', 'libglu', 'libjpeg-turbo', 'libpng>=1.6.20', 'libseccomp', 'libslirp', 'libssh2', 'libsysprof-capture', 'liburing', 'libx11', 'lzo', 'ncurses>=6.0-3', 'nettle>=3.6', 'nss', 'numactl', 'pipewire', 'pixman', 'pulseaudio', 'rutabaga-ffi', 'snappy', 'spice-protocol', 'usbredir>=0.8.0', 'vte3', 'xkeyboard-config']"
reverse_depends = "['libguestfs']"
+++
### Description: 
QEMU is a FAST! processor emulator

### Files: 
* /usr/bin/elf2dmp
* /usr/bin/qemu
* /usr/bin/qemu-edid
* /usr/bin/qemu-img
* /usr/bin/qemu-io
* /usr/bin/qemu-keymap
* /usr/bin/qemu-nbd
* /usr/bin/qemu-pr-helper
* /usr/bin/qemu-storage-daemon
* /usr/bin/qemu-system-aarch64
* /usr/bin/qemu-system-alpha
* /usr/bin/qemu-system-arm
* /usr/bin/qemu-system-avr
* /usr/bin/qemu-system-hppa
* /usr/bin/qemu-system-i386
* /usr/bin/qemu-system-loongarch64
* /usr/bin/qemu-system-m68k
* /usr/bin/qemu-system-microblaze
* /usr/bin/qemu-system-microblazeel
* /usr/bin/qemu-system-mips
* /usr/bin/qemu-system-mips64
* /usr/bin/qemu-system-mips64el
* /usr/bin/qemu-system-mipsel
* /usr/bin/qemu-system-or1k
* /usr/bin/qemu-system-ppc
* /usr/bin/qemu-system-ppc64
* /usr/bin/qemu-system-riscv32
* /usr/bin/qemu-system-riscv64
* /usr/bin/qemu-system-rx
* /usr/bin/qemu-system-s390x
* /usr/bin/qemu-system-sh4
* /usr/bin/qemu-system-sh4eb
* /usr/bin/qemu-system-sparc
* /usr/bin/qemu-system-sparc64
* /usr/bin/qemu-system-tricore
* /usr/bin/qemu-system-x86_64
* /usr/bin/qemu-system-xtensa
* /usr/bin/qemu-system-xtensaeb
* /usr/bin/qemu-vmsr-helper
* /usr/include/qemu-plugin.h
* /usr/lib/qemu/accel-qtest-aarch64.so
* /usr/lib/qemu/accel-qtest-alpha.so
* /usr/lib/qemu/accel-qtest-arm.so
* /usr/lib/qemu/accel-qtest-avr.so
* /usr/lib/qemu/accel-qtest-hppa.so
* /usr/lib/qemu/accel-qtest-i386.so
* /usr/lib/qemu/accel-qtest-loongarch64.so
* /usr/lib/qemu/accel-qtest-m68k.so
* /usr/lib/qemu/accel-qtest-microblaze.so
* /usr/lib/qemu/accel-qtest-microblazeel.so
* /usr/lib/qemu/accel-qtest-mips.so
* /usr/lib/qemu/accel-qtest-mips64.so
* /usr/lib/qemu/accel-qtest-mips64el.so
* /usr/lib/qemu/accel-qtest-mipsel.so
* /usr/lib/qemu/accel-qtest-or1k.so
* /usr/lib/qemu/accel-qtest-ppc.so
* /usr/lib/qemu/accel-qtest-ppc64.so
* /usr/lib/qemu/accel-qtest-riscv32.so
* /usr/lib/qemu/accel-qtest-riscv64.so
* /usr/lib/qemu/accel-qtest-rx.so
* /usr/lib/qemu/accel-qtest-s390x.so
* /usr/lib/qemu/accel-qtest-sh4.so
* /usr/lib/qemu/accel-qtest-sh4eb.so
* /usr/lib/qemu/accel-qtest-sparc.so
* /usr/lib/qemu/accel-qtest-sparc64.so
* /usr/lib/qemu/accel-qtest-tricore.so
* /usr/lib/qemu/accel-qtest-x86_64.so
* /usr/lib/qemu/accel-qtest-xtensa.so
* /usr/lib/qemu/accel-qtest-xtensaeb.so
* /usr/lib/qemu/audio-alsa.so
* /usr/lib/qemu/audio-dbus.so
* /usr/lib/qemu/audio-oss.so
* /usr/lib/qemu/audio-pa.so
* /usr/lib/qemu/audio-pipewire.so
* /usr/lib/qemu/audio-sdl.so
* /usr/lib/qemu/audio-spice.so
* /usr/lib/qemu/block-curl.so
* /usr/lib/qemu/block-dmg-bz2.so
* /usr/lib/qemu/block-ssh.so
* /usr/lib/qemu/chardev-spice.so
* /usr/lib/qemu/hw-display-qxl.so
* /usr/lib/qemu/hw-display-virtio-gpu-gl.so
* /usr/lib/qemu/hw-display-virtio-gpu-pci-gl.so
* /usr/lib/qemu/hw-display-virtio-gpu-pci-rutabaga.so
* /usr/lib/qemu/hw-display-virtio-gpu-pci.so
* /usr/lib/qemu/hw-display-virtio-gpu-rutabaga.so
* /usr/lib/qemu/hw-display-virtio-gpu.so
* /usr/lib/qemu/hw-display-virtio-vga-gl.so
* /usr/lib/qemu/hw-display-virtio-vga-rutabaga.so
* /usr/lib/qemu/hw-display-virtio-vga.so
* /usr/lib/qemu/hw-s390x-virtio-gpu-ccw.so
* /usr/lib/qemu/hw-uefi-vars.so
* /usr/lib/qemu/hw-usb-host.so
* /usr/lib/qemu/hw-usb-redirect.so
* /usr/lib/qemu/qemu-bridge-helper
* /usr/lib/qemu/ui-curses.so
* /usr/lib/qemu/ui-dbus.so
* /usr/lib/qemu/ui-egl-headless.so
* /usr/lib/qemu/ui-gtk.so
* /usr/lib/qemu/ui-opengl.so
* /usr/lib/qemu/ui-sdl.so
* /usr/lib/qemu/ui-spice-app.so
* /usr/lib/qemu/ui-spice-core.so
* /usr/lib/qemu/vhost-user-gpu
* /usr/share/applications/qemu.desktop
* /usr/share/doc/qemu-10.0.2/COPYING
* /usr/share/doc/qemu-10.0.2/COPYING.LIB
* /usr/share/doc/qemu-10.0.2/LICENSE
* /usr/share/doc/qemu-10.0.2/README.Frugalware
* /usr/share/doc/qemu-10.0.2/README.rst
* /usr/share/doc/qemu-10.0.2/VERSION
* /usr/share/doc/qemu/.buildinfo
* /usr/share/doc/qemu/about/build-platforms.html
* /usr/share/doc/qemu/about/deprecated.html
* /usr/share/doc/qemu/about/emulation.html
* /usr/share/doc/qemu/about/index.html
* /usr/share/doc/qemu/about/license.html
* /usr/share/doc/qemu/about/removed-features.html
* /usr/share/doc/qemu/dbus-dbusindex.html
* /usr/share/doc/qemu/devel/atomics.html
* /usr/share/doc/qemu/devel/bitops.html
* /usr/share/doc/qemu/devel/block-coroutine-wrapper.html
* /usr/share/doc/qemu/devel/build-environment.html
* /usr/share/doc/qemu/devel/build-system.html
* /usr/share/doc/qemu/devel/clocks.html
* /usr/share/doc/qemu/devel/code-of-conduct.html
* /usr/share/doc/qemu/devel/codebase.html
* /usr/share/doc/qemu/devel/conflict-resolution.html
* /usr/share/doc/qemu/devel/control-flow-integrity.html
* /usr/share/doc/qemu/devel/crypto.html
* /usr/share/doc/qemu/devel/decodetree.html
* /usr/share/doc/qemu/devel/docs.html
* /usr/share/doc/qemu/devel/ebpf_rss.html
* /usr/share/doc/qemu/devel/index-api.html
* /usr/share/doc/qemu/devel/index-build.html
* /usr/share/doc/qemu/devel/index-internals.html
* /usr/share/doc/qemu/devel/index-process.html
* /usr/share/doc/qemu/devel/index-tcg.html
* /usr/share/doc/qemu/devel/index.html
* /usr/share/doc/qemu/devel/kconfig.html
* /usr/share/doc/qemu/devel/loads-stores.html
* /usr/share/doc/qemu/devel/lockcnt.html
* /usr/share/doc/qemu/devel/luks-detached-header.html
* /usr/share/doc/qemu/devel/maintainers.html
* /usr/share/doc/qemu/devel/memory.html
* /usr/share/doc/qemu/devel/migration/best-practices.html
* /usr/share/doc/qemu/devel/migration/compatibility.html
* /usr/share/doc/qemu/devel/migration/CPR.html
* /usr/share/doc/qemu/devel/migration/dirty-limit.html
* /usr/share/doc/qemu/devel/migration/features.html
* /usr/share/doc/qemu/devel/migration/index.html
* /usr/share/doc/qemu/devel/migration/main.html
* /usr/share/doc/qemu/devel/migration/mapped-ram.html
* /usr/share/doc/qemu/devel/migration/postcopy.html
* /usr/share/doc/qemu/devel/migration/qatzip-compression.html
* /usr/share/doc/qemu/devel/migration/qpl-compression.html
* /usr/share/doc/qemu/devel/migration/uadk-compression.html
* /usr/share/doc/qemu/devel/migration/vfio.html
* /usr/share/doc/qemu/devel/migration/virtio.html
* /usr/share/doc/qemu/devel/modules.html
* /usr/share/doc/qemu/devel/multi-process.html
* /usr/share/doc/qemu/devel/multi-thread-tcg.html
* /usr/share/doc/qemu/devel/multiple-iothreads.html
* /usr/share/doc/qemu/devel/pci.html
* /usr/share/doc/qemu/devel/qapi-code-gen.html
* /usr/share/doc/qemu/devel/qapi-domain.html
* /usr/share/doc/qemu/devel/qdev-api.html
* /usr/share/doc/qemu/devel/qom-api.html
* /usr/share/doc/qemu/devel/qom.html
* /usr/share/doc/qemu/devel/rcu.html
* /usr/share/doc/qemu/devel/replay.html
* /usr/share/doc/qemu/devel/reset.html
* /usr/share/doc/qemu/devel/rust.html
* /usr/share/doc/qemu/devel/s390-cpu-topology.html
* /usr/share/doc/qemu/devel/s390-dasd-ipl.html
* /usr/share/doc/qemu/devel/secure-coding-practices.html
* /usr/share/doc/qemu/devel/stable-process.html
* /usr/share/doc/qemu/devel/style.html
* /usr/share/doc/qemu/devel/submitting-a-patch.html
* /usr/share/doc/qemu/devel/submitting-a-pull-request.html
* /usr/share/doc/qemu/devel/tcg-icount.html
* /usr/share/doc/qemu/devel/tcg-ops.html
* /usr/share/doc/qemu/devel/tcg-plugins.html
* /usr/share/doc/qemu/devel/tcg.html
* /usr/share/doc/qemu/devel/testing/acpi-bits.html
* /usr/share/doc/qemu/devel/testing/avocado.html
* /usr/share/doc/qemu/devel/testing/blkdebug.html
* /usr/share/doc/qemu/devel/testing/blkverify.html
* /usr/share/doc/qemu/devel/testing/ci.html
* /usr/share/doc/qemu/devel/testing/functional.html
* /usr/share/doc/qemu/devel/testing/fuzzing.html
* /usr/share/doc/qemu/devel/testing/index.html
* /usr/share/doc/qemu/devel/testing/main.html
* /usr/share/doc/qemu/devel/testing/qgraph.html
* /usr/share/doc/qemu/devel/testing/qtest.html
* /usr/share/doc/qemu/devel/tracing.html
* /usr/share/doc/qemu/devel/trivial-patches.html
* /usr/share/doc/qemu/devel/uefi-vars.html
* /usr/share/doc/qemu/devel/ui.html
* /usr/share/doc/qemu/devel/vfio-iommufd.html
* /usr/share/doc/qemu/devel/virtio-backends.html
* /usr/share/doc/qemu/devel/writing-monitor-commands.html
* /usr/share/doc/qemu/devel/zoned-storage.html
* /usr/share/doc/qemu/genindex.html
* /usr/share/doc/qemu/glossary.html
* /usr/share/doc/qemu/index.html
* /usr/share/doc/qemu/interop/barrier.html
* /usr/share/doc/qemu/interop/bitmaps.html
* /usr/share/doc/qemu/interop/dbus-display.html
* /usr/share/doc/qemu/interop/dbus-vmstate.html
* /usr/share/doc/qemu/interop/dbus.html
* /usr/share/doc/qemu/interop/index.html
* /usr/share/doc/qemu/interop/live-block-operations.html
* /usr/share/doc/qemu/interop/nbd.html
* /usr/share/doc/qemu/interop/parallels.html
* /usr/share/doc/qemu/interop/pr-helper.html
* /usr/share/doc/qemu/interop/prl-xml.html
* /usr/share/doc/qemu/interop/qemu-ga-ref.html
* /usr/share/doc/qemu/interop/qemu-ga.html
* /usr/share/doc/qemu/interop/qemu-qmp-ref.html
* /usr/share/doc/qemu/interop/qemu-storage-daemon-qmp-ref.html
* /usr/share/doc/qemu/interop/qmp-spec.html
* /usr/share/doc/qemu/interop/vhost-user-gpu.html
* /usr/share/doc/qemu/interop/vhost-user.html
* /usr/share/doc/qemu/interop/vhost-vdpa.html
* /usr/share/doc/qemu/interop/virtio-balloon-stats.html
* /usr/share/doc/qemu/interop/vnc-ledstate-pseudo-encoding.html
* /usr/share/doc/qemu/objects.inv
* /usr/share/doc/qemu/qapi-qga-index.html
* /usr/share/doc/qemu/qapi-qmp-index.html
* /usr/share/doc/qemu/qapi-qsd-index.html
* /usr/share/doc/qemu/search.html
* /usr/share/doc/qemu/searchindex.js
* /usr/share/doc/qemu/specs/acpi_cpu_hotplug.html
* /usr/share/doc/qemu/specs/acpi_erst.html
* /usr/share/doc/qemu/specs/acpi_hest_ghes.html
* /usr/share/doc/qemu/specs/acpi_hw_reduced_hotplug.html
* /usr/share/doc/qemu/specs/acpi_mem_hotplug.html
* /usr/share/doc/qemu/specs/acpi_nvdimm.html
* /usr/share/doc/qemu/specs/acpi_pci_hotplug.html
* /usr/share/doc/qemu/specs/aspeed-intc.html
* /usr/share/doc/qemu/specs/edu.html
* /usr/share/doc/qemu/specs/fsi.html
* /usr/share/doc/qemu/specs/fw_cfg.html
* /usr/share/doc/qemu/specs/index.html
* /usr/share/doc/qemu/specs/ivshmem-spec.html
* /usr/share/doc/qemu/specs/pci-ids.html
* /usr/share/doc/qemu/specs/pci-serial.html
* /usr/share/doc/qemu/specs/pci-testdev.html
* /usr/share/doc/qemu/specs/ppc-spapr-hcalls.html
* /usr/share/doc/qemu/specs/ppc-spapr-hotplug.html
* /usr/share/doc/qemu/specs/ppc-spapr-numa.html
* /usr/share/doc/qemu/specs/ppc-spapr-uv-hcalls.html
* /usr/share/doc/qemu/specs/ppc-spapr-xive.html
* /usr/share/doc/qemu/specs/ppc-xive.html
* /usr/share/doc/qemu/specs/pvpanic.html
* /usr/share/doc/qemu/specs/rapl-msr.html
* /usr/share/doc/qemu/specs/riscv-aia.html
* /usr/share/doc/qemu/specs/riscv-iommu.html
* /usr/share/doc/qemu/specs/rocker.html
* /usr/share/doc/qemu/specs/sev-guest-firmware.html
* /usr/share/doc/qemu/specs/spdm.html
* /usr/share/doc/qemu/specs/standard-vga.html
* /usr/share/doc/qemu/specs/tpm.html
* /usr/share/doc/qemu/specs/virt-ctlr.html
* /usr/share/doc/qemu/specs/vmcoreinfo.html
* /usr/share/doc/qemu/specs/vmgenid.html
* /usr/share/doc/qemu/specs/vmw_pvscsi-spec.html
* /usr/share/doc/qemu/system/arm/aspeed.html
* /usr/share/doc/qemu/system/arm/b-l475e-iot01a.html
* /usr/share/doc/qemu/system/arm/bananapi_m2u.html
* /usr/share/doc/qemu/system/arm/collie.html
* /usr/share/doc/qemu/system/arm/cpu-features.html
* /usr/share/doc/qemu/system/arm/cubieboard.html
* /usr/share/doc/qemu/system/arm/digic.html
* /usr/share/doc/qemu/system/arm/emcraft-sf2.html
* /usr/share/doc/qemu/system/arm/emulation.html
* /usr/share/doc/qemu/system/arm/exynos.html
* /usr/share/doc/qemu/system/arm/fby35.html
* /usr/share/doc/qemu/system/arm/highbank.html
* /usr/share/doc/qemu/system/arm/imx25-pdk.html
* /usr/share/doc/qemu/system/arm/imx8mp-evk.html
* /usr/share/doc/qemu/system/arm/integratorcp.html
* /usr/share/doc/qemu/system/arm/kzm.html
* /usr/share/doc/qemu/system/arm/mcimx6ul-evk.html
* /usr/share/doc/qemu/system/arm/mcimx7d-sabre.html
* /usr/share/doc/qemu/system/arm/mps2.html
* /usr/share/doc/qemu/system/arm/musca.html
* /usr/share/doc/qemu/system/arm/musicpal.html
* /usr/share/doc/qemu/system/arm/nrf.html
* /usr/share/doc/qemu/system/arm/nuvoton.html
* /usr/share/doc/qemu/system/arm/orangepi.html
* /usr/share/doc/qemu/system/arm/raspi.html
* /usr/share/doc/qemu/system/arm/realview.html
* /usr/share/doc/qemu/system/arm/sabrelite.html
* /usr/share/doc/qemu/system/arm/sbsa.html
* /usr/share/doc/qemu/system/arm/stellaris.html
* /usr/share/doc/qemu/system/arm/stm32.html
* /usr/share/doc/qemu/system/arm/sx1.html
* /usr/share/doc/qemu/system/arm/versatile.html
* /usr/share/doc/qemu/system/arm/vexpress.html
* /usr/share/doc/qemu/system/arm/virt.html
* /usr/share/doc/qemu/system/arm/vmapple.html
* /usr/share/doc/qemu/system/arm/xenpvh.html
* /usr/share/doc/qemu/system/arm/xlnx-versal-virt.html
* /usr/share/doc/qemu/system/arm/xlnx-zcu102.html
* /usr/share/doc/qemu/system/arm/xlnx-zynq.html
* /usr/share/doc/qemu/system/authz.html
* /usr/share/doc/qemu/system/barrier.html
* /usr/share/doc/qemu/system/bootindex.html
* /usr/share/doc/qemu/system/confidential-guest-support.html
* /usr/share/doc/qemu/system/cpu-hotplug.html
* /usr/share/doc/qemu/system/device-emulation.html
* /usr/share/doc/qemu/system/devices/can.html
* /usr/share/doc/qemu/system/devices/canokey.html
* /usr/share/doc/qemu/system/devices/ccid.html
* /usr/share/doc/qemu/system/devices/cxl.html
* /usr/share/doc/qemu/system/devices/igb.html
* /usr/share/doc/qemu/system/devices/ivshmem-flat.html
* /usr/share/doc/qemu/system/devices/ivshmem.html
* /usr/share/doc/qemu/system/devices/keyboard.html
* /usr/share/doc/qemu/system/devices/net.html
* /usr/share/doc/qemu/system/devices/nvme.html
* /usr/share/doc/qemu/system/devices/usb-u2f.html
* /usr/share/doc/qemu/system/devices/usb.html
* /usr/share/doc/qemu/system/devices/vhost-user-input.html
* /usr/share/doc/qemu/system/devices/vhost-user-rng.html
* /usr/share/doc/qemu/system/devices/vhost-user.html
* /usr/share/doc/qemu/system/devices/virtio-gpu.html
* /usr/share/doc/qemu/system/devices/virtio-pmem.html
* /usr/share/doc/qemu/system/devices/virtio-snd.html
* /usr/share/doc/qemu/system/gdb.html
* /usr/share/doc/qemu/system/generic-loader.html
* /usr/share/doc/qemu/system/guest-loader.html
* /usr/share/doc/qemu/system/i386/amd-memory-encryption.html
* /usr/share/doc/qemu/system/i386/cpu.html
* /usr/share/doc/qemu/system/i386/hyperv.html
* /usr/share/doc/qemu/system/i386/kvm-pv.html
* /usr/share/doc/qemu/system/i386/microvm.html
* /usr/share/doc/qemu/system/i386/nitro-enclave.html
* /usr/share/doc/qemu/system/i386/pc.html
* /usr/share/doc/qemu/system/i386/sgx.html
* /usr/share/doc/qemu/system/i386/xen.html
* /usr/share/doc/qemu/system/i386/xenpvh.html
* /usr/share/doc/qemu/system/images.html
* /usr/share/doc/qemu/system/index.html
* /usr/share/doc/qemu/system/introduction.html
* /usr/share/doc/qemu/system/invocation.html
* /usr/share/doc/qemu/system/keys.html
* /usr/share/doc/qemu/system/linuxboot.html
* /usr/share/doc/qemu/system/loongarch/virt.html
* /usr/share/doc/qemu/system/managed-startup.html
* /usr/share/doc/qemu/system/monitor.html
* /usr/share/doc/qemu/system/multi-process.html
* /usr/share/doc/qemu/system/mux-chardev.html
* /usr/share/doc/qemu/system/openrisc/cpu-features.html
* /usr/share/doc/qemu/system/openrisc/emulation.html
* /usr/share/doc/qemu/system/openrisc/or1k-sim.html
* /usr/share/doc/qemu/system/openrisc/virt.html
* /usr/share/doc/qemu/system/ppc/amigang.html
* /usr/share/doc/qemu/system/ppc/embedded.html
* /usr/share/doc/qemu/system/ppc/powermac.html
* /usr/share/doc/qemu/system/ppc/powernv.html
* /usr/share/doc/qemu/system/ppc/ppce500.html
* /usr/share/doc/qemu/system/ppc/prep.html
* /usr/share/doc/qemu/system/ppc/pseries.html
* /usr/share/doc/qemu/system/pr-manager.html
* /usr/share/doc/qemu/system/qemu-block-drivers.html
* /usr/share/doc/qemu/system/qemu-cpu-models.html
* /usr/share/doc/qemu/system/qemu-manpage.html
* /usr/share/doc/qemu/system/replay.html
* /usr/share/doc/qemu/system/riscv/microblaze-v-generic.html
* /usr/share/doc/qemu/system/riscv/microchip-icicle-kit.html
* /usr/share/doc/qemu/system/riscv/shakti-c.html
* /usr/share/doc/qemu/system/riscv/sifive_u.html
* /usr/share/doc/qemu/system/riscv/virt.html
* /usr/share/doc/qemu/system/s390x/3270.html
* /usr/share/doc/qemu/system/s390x/bootdevices.html
* /usr/share/doc/qemu/system/s390x/cpu-topology.html
* /usr/share/doc/qemu/system/s390x/css.html
* /usr/share/doc/qemu/system/s390x/pcidevices.html
* /usr/share/doc/qemu/system/s390x/protvirt.html
* /usr/share/doc/qemu/system/s390x/vfio-ap.html
* /usr/share/doc/qemu/system/s390x/vfio-ccw.html
* /usr/share/doc/qemu/system/secrets.html
* /usr/share/doc/qemu/system/security.html
* /usr/share/doc/qemu/system/target-arm.html
* /usr/share/doc/qemu/system/target-avr.html
* /usr/share/doc/qemu/system/target-i386.html
* /usr/share/doc/qemu/system/target-loongarch.html
* /usr/share/doc/qemu/system/target-m68k.html
* /usr/share/doc/qemu/system/target-mips.html
* /usr/share/doc/qemu/system/target-openrisc.html
* /usr/share/doc/qemu/system/target-ppc.html
* /usr/share/doc/qemu/system/target-riscv.html
* /usr/share/doc/qemu/system/target-rx.html
* /usr/share/doc/qemu/system/target-s390x.html
* /usr/share/doc/qemu/system/target-sparc.html
* /usr/share/doc/qemu/system/target-sparc64.html
* /usr/share/doc/qemu/system/target-xtensa.html
* /usr/share/doc/qemu/system/targets.html
* /usr/share/doc/qemu/system/tls.html
* /usr/share/doc/qemu/system/virtio-net-failover.html
* /usr/share/doc/qemu/system/vm-templating.html
* /usr/share/doc/qemu/system/vnc-security.html
* /usr/share/doc/qemu/tools/index.html
* /usr/share/doc/qemu/tools/qemu-img.html
* /usr/share/doc/qemu/tools/qemu-nbd.html
* /usr/share/doc/qemu/tools/qemu-pr-helper.html
* /usr/share/doc/qemu/tools/qemu-storage-daemon.html
* /usr/share/doc/qemu/tools/qemu-trace-stap.html
* /usr/share/doc/qemu/tools/qemu-vmsr-helper.html
* /usr/share/doc/qemu/user/index.html
* /usr/share/doc/qemu/user/main.html
* /usr/share/doc/qemu/_static/basic.css
* /usr/share/doc/qemu/_static/css/badge_only.css
* /usr/share/doc/qemu/_static/css/fonts/fontawesome-webfont.eot
* /usr/share/doc/qemu/_static/css/fonts/fontawesome-webfont.svg
* /usr/share/doc/qemu/_static/css/fonts/fontawesome-webfont.ttf
* /usr/share/doc/qemu/_static/css/fonts/fontawesome-webfont.woff
* /usr/share/doc/qemu/_static/css/fonts/fontawesome-webfont.woff2
* /usr/share/doc/qemu/_static/css/fonts/lato-bold-italic.woff
* /usr/share/doc/qemu/_static/css/fonts/lato-bold-italic.woff2
* /usr/share/doc/qemu/_static/css/fonts/lato-bold.woff
* /usr/share/doc/qemu/_static/css/fonts/lato-bold.woff2
* /usr/share/doc/qemu/_static/css/fonts/lato-normal-italic.woff
* /usr/share/doc/qemu/_static/css/fonts/lato-normal-italic.woff2
* /usr/share/doc/qemu/_static/css/fonts/lato-normal.woff
* /usr/share/doc/qemu/_static/css/fonts/lato-normal.woff2
* /usr/share/doc/qemu/_static/css/fonts/Roboto-Slab-Bold.woff
* /usr/share/doc/qemu/_static/css/fonts/Roboto-Slab-Bold.woff2
* /usr/share/doc/qemu/_static/css/fonts/Roboto-Slab-Regular.woff
* /usr/share/doc/qemu/_static/css/fonts/Roboto-Slab-Regular.woff2
* /usr/share/doc/qemu/_static/css/theme.css
* /usr/share/doc/qemu/_static/custom.js
* /usr/share/doc/qemu/_static/doctools.js
* /usr/share/doc/qemu/_static/documentation_options.js
* /usr/share/doc/qemu/_static/file.png
* /usr/share/doc/qemu/_static/fonts/Lato/lato-bold.eot
* /usr/share/doc/qemu/_static/fonts/Lato/lato-bold.ttf
* /usr/share/doc/qemu/_static/fonts/Lato/lato-bold.woff
* /usr/share/doc/qemu/_static/fonts/Lato/lato-bold.woff2
* /usr/share/doc/qemu/_static/fonts/Lato/lato-bolditalic.eot
* /usr/share/doc/qemu/_static/fonts/Lato/lato-bolditalic.ttf
* /usr/share/doc/qemu/_static/fonts/Lato/lato-bolditalic.woff
* /usr/share/doc/qemu/_static/fonts/Lato/lato-bolditalic.woff2
* /usr/share/doc/qemu/_static/fonts/Lato/lato-italic.eot
* /usr/share/doc/qemu/_static/fonts/Lato/lato-italic.ttf
* /usr/share/doc/qemu/_static/fonts/Lato/lato-italic.woff
* /usr/share/doc/qemu/_static/fonts/Lato/lato-italic.woff2
* /usr/share/doc/qemu/_static/fonts/Lato/lato-regular.eot
* /usr/share/doc/qemu/_static/fonts/Lato/lato-regular.ttf
* /usr/share/doc/qemu/_static/fonts/Lato/lato-regular.woff
* /usr/share/doc/qemu/_static/fonts/Lato/lato-regular.woff2
* /usr/share/doc/qemu/_static/fonts/RobotoSlab/roboto-slab-v7-bold.eot
* /usr/share/doc/qemu/_static/fonts/RobotoSlab/roboto-slab-v7-bold.ttf
* /usr/share/doc/qemu/_static/fonts/RobotoSlab/roboto-slab-v7-bold.woff
* /usr/share/doc/qemu/_static/fonts/RobotoSlab/roboto-slab-v7-bold.woff2
* /usr/share/doc/qemu/_static/fonts/RobotoSlab/roboto-slab-v7-regular.eot
* /usr/share/doc/qemu/_static/fonts/RobotoSlab/roboto-slab-v7-regular.ttf
* /usr/share/doc/qemu/_static/fonts/RobotoSlab/roboto-slab-v7-regular.woff
* /usr/share/doc/qemu/_static/fonts/RobotoSlab/roboto-slab-v7-regular.woff2
* /usr/share/doc/qemu/_static/jquery.js
* /usr/share/doc/qemu/_static/js/badge_only.js
* /usr/share/doc/qemu/_static/js/theme.js
* /usr/share/doc/qemu/_static/js/versions.js
* /usr/share/doc/qemu/_static/language_data.js
* /usr/share/doc/qemu/_static/minus.png
* /usr/share/doc/qemu/_static/plus.png
* /usr/share/doc/qemu/_static/pygments.css
* /usr/share/doc/qemu/_static/qemu_128x128.png
* /usr/share/doc/qemu/_static/qemu_32x32.png
* /usr/share/doc/qemu/_static/searchtools.js
* /usr/share/doc/qemu/_static/sphinx_highlight.js
* /usr/share/doc/qemu/_static/theme_overrides.css
* /usr/share/doc/qemu/_static/_sphinx_javascript_frameworks_compat.js
* /usr/share/icons/hicolor/128x128/apps/qemu.png
* /usr/share/icons/hicolor/16x16/apps/qemu.png
* /usr/share/icons/hicolor/24x24/apps/qemu.png
* /usr/share/icons/hicolor/256x256/apps/qemu.png
* /usr/share/icons/hicolor/32x32/apps/qemu.bmp
* /usr/share/icons/hicolor/32x32/apps/qemu.png
* /usr/share/icons/hicolor/48x48/apps/qemu.png
* /usr/share/icons/hicolor/512x512/apps/qemu.png
* /usr/share/icons/hicolor/64x64/apps/qemu.png
* /usr/share/icons/hicolor/scalable/apps/qemu.svg
* /usr/share/locale/bg/LC_MESSAGES/qemu.mo
* /usr/share/locale/de_DE/LC_MESSAGES/qemu.mo
* /usr/share/locale/fr_FR/LC_MESSAGES/qemu.mo
* /usr/share/locale/hu/LC_MESSAGES/qemu.mo
* /usr/share/locale/it/LC_MESSAGES/qemu.mo
* /usr/share/locale/sv/LC_MESSAGES/qemu.mo
* /usr/share/locale/tr/LC_MESSAGES/qemu.mo
* /usr/share/locale/uk/LC_MESSAGES/qemu.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/qemu.mo
* /usr/share/man/man1/qemu-img.1.gz
* /usr/share/man/man1/qemu-storage-daemon.1.gz
* /usr/share/man/man1/qemu.1.gz
* /usr/share/man/man7/qemu-block-drivers.7.gz
* /usr/share/man/man7/qemu-cpu-models.7.gz
* /usr/share/man/man7/qemu-ga-ref.7.gz
* /usr/share/man/man7/qemu-qmp-ref.7.gz
* /usr/share/man/man7/qemu-storage-daemon-qmp-ref.7.gz
* /usr/share/man/man8/qemu-ga.8.gz
* /usr/share/man/man8/qemu-nbd.8.gz
* /usr/share/man/man8/qemu-pr-helper.8.gz
* /usr/share/qemu/bamboo.dtb
* /usr/share/qemu/bios-256k.bin
* /usr/share/qemu/bios-microvm.bin
* /usr/share/qemu/bios.bin
* /usr/share/qemu/canyonlands.dtb
* /usr/share/qemu/efi-e1000.rom
* /usr/share/qemu/efi-e1000e.rom
* /usr/share/qemu/efi-eepro100.rom
* /usr/share/qemu/efi-ne2k_pci.rom
* /usr/share/qemu/efi-pcnet.rom
* /usr/share/qemu/efi-rtl8139.rom
* /usr/share/qemu/efi-virtio.rom
* /usr/share/qemu/efi-vmxnet3.rom
* /usr/share/qemu/hppa-firmware.img
* /usr/share/qemu/hppa-firmware64.img
* /usr/share/qemu/keymaps/ar
* /usr/share/qemu/keymaps/bepo
* /usr/share/qemu/keymaps/cz
* /usr/share/qemu/keymaps/da
* /usr/share/qemu/keymaps/de
* /usr/share/qemu/keymaps/de-ch
* /usr/share/qemu/keymaps/en-gb
* /usr/share/qemu/keymaps/en-us
* /usr/share/qemu/keymaps/es
* /usr/share/qemu/keymaps/et
* /usr/share/qemu/keymaps/fi
* /usr/share/qemu/keymaps/fo
* /usr/share/qemu/keymaps/fr
* /usr/share/qemu/keymaps/fr-be
* /usr/share/qemu/keymaps/fr-ca
* /usr/share/qemu/keymaps/fr-ch
* /usr/share/qemu/keymaps/hr
* /usr/share/qemu/keymaps/hu
* /usr/share/qemu/keymaps/is
* /usr/share/qemu/keymaps/it
* /usr/share/qemu/keymaps/ja
* /usr/share/qemu/keymaps/lt
* /usr/share/qemu/keymaps/lv
* /usr/share/qemu/keymaps/mk
* /usr/share/qemu/keymaps/nl
* /usr/share/qemu/keymaps/no
* /usr/share/qemu/keymaps/pl
* /usr/share/qemu/keymaps/pt
* /usr/share/qemu/keymaps/pt-br
* /usr/share/qemu/keymaps/ru
* /usr/share/qemu/keymaps/sl
* /usr/share/qemu/keymaps/sv
* /usr/share/qemu/keymaps/th
* /usr/share/qemu/keymaps/tr
* /usr/share/qemu/kvmvapic.bin
* /usr/share/qemu/linuxboot.bin
* /usr/share/qemu/linuxboot_dma.bin
* /usr/share/qemu/multiboot.bin
* /usr/share/qemu/multiboot_dma.bin
* /usr/share/qemu/npcm7xx_bootrom.bin
* /usr/share/qemu/npcm8xx_bootrom.bin
* /usr/share/qemu/openbios-ppc
* /usr/share/qemu/openbios-sparc32
* /usr/share/qemu/openbios-sparc64
* /usr/share/qemu/opensbi-riscv32-generic-fw_dynamic.bin
* /usr/share/qemu/opensbi-riscv64-generic-fw_dynamic.bin
* /usr/share/qemu/palcode-clipper
* /usr/share/qemu/petalogix-ml605.dtb
* /usr/share/qemu/petalogix-s3adsp1800.dtb
* /usr/share/qemu/pnv-pnor.bin
* /usr/share/qemu/pvh.bin
* /usr/share/qemu/pxe-e1000.rom
* /usr/share/qemu/pxe-eepro100.rom
* /usr/share/qemu/pxe-ne2k_pci.rom
* /usr/share/qemu/pxe-pcnet.rom
* /usr/share/qemu/pxe-rtl8139.rom
* /usr/share/qemu/pxe-virtio.rom
* /usr/share/qemu/qboot.rom
* /usr/share/qemu/QEMU,cgthree.bin
* /usr/share/qemu/QEMU,tcx.bin
* /usr/share/qemu/qemu-nsis.bmp
* /usr/share/qemu/qemu_vga.ndrv
* /usr/share/qemu/s390-ccw.img
* /usr/share/qemu/skiboot.lid
* /usr/share/qemu/slof.bin
* /usr/share/qemu/trace-events-all
* /usr/share/qemu/u-boot-sam460-20100605.bin
* /usr/share/qemu/u-boot.e500
* /usr/share/qemu/vgabios-ati.bin
* /usr/share/qemu/vgabios-bochs-display.bin
* /usr/share/qemu/vgabios-cirrus.bin
* /usr/share/qemu/vgabios-qxl.bin
* /usr/share/qemu/vgabios-ramfb.bin
* /usr/share/qemu/vgabios-stdvga.bin
* /usr/share/qemu/vgabios-virtio.bin
* /usr/share/qemu/vgabios-vmware.bin
* /usr/share/qemu/vgabios.bin
* /usr/share/qemu/vhost-user/50-qemu-gpu.json
* /usr/share/qemu/vof-nvram.bin
* /usr/share/qemu/vof.bin
