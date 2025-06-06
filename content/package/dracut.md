+++
draft = false
title = "dracut 107-1"
version = "107-1"
description = "Generic initramfs generationtool"
date = "2025-05-05T09:26:26"
aliases = "/packages/103623"
categories = ['base']
upstreamurl = "https://github.com/dracut-ng/dracut-ng"
arch = "x86_64"
size = "464832"
usize = "1662740"
sha1sum = "1e25c3a865dd1425400d4f7e99b4e079566fe5da"
depends = "['bash>=4.4', 'binutils', 'cpio>=2.12-3', 'dash>=0.5.8', 'dmraid', 'elfutils', 'file', 'grep', 'kbd>=2.0.3-3', 'keyutils>=1.5.9-5', 'kmod', 'lvm2>=2.03.01-3', 'multipath-tools', 'popt>=1.16-5', 'systemd>=227-15', 'util-linux>=2.27.1-4']"
reverse_depends = "['dracut-network', 'kernel-initrd', 'kernel-lts-initrd']"
+++
### Description: 
Generic initramfs generationtool

### Files: 
* /etc/dracut.conf
* /etc/dracut.conf.d/00-frugalware.conf
* /etc/dracut.conf.d/10-frugalware-omitted-modules.conf
* /usr/bin/dracut
* /usr/bin/dracut-catimages
* /usr/bin/lsinitrd
* /usr/lib/dracut/dracut-cpio
* /usr/lib/dracut/dracut-functions
* /usr/lib/dracut/dracut-functions.sh
* /usr/lib/dracut/dracut-init.sh
* /usr/lib/dracut/dracut-initramfs-restore
* /usr/lib/dracut/dracut-install
* /usr/lib/dracut/dracut-logger.sh
* /usr/lib/dracut/dracut-util
* /usr/lib/dracut/dracut-version.sh
* /usr/lib/dracut/dracut.conf.d/fedora.conf.example
* /usr/lib/dracut/dracut.conf.d/fips/50-fips.conf
* /usr/lib/dracut/dracut.conf.d/generic/50-generic.conf
* /usr/lib/dracut/dracut.conf.d/hostonly/50-hostonly.conf
* /usr/lib/dracut/dracut.conf.d/ima/50-ima.conf
* /usr/lib/dracut/dracut.conf.d/no-network/50-no-network.conf
* /usr/lib/dracut/dracut.conf.d/no-xattr/50-no-xattr.conf
* /usr/lib/dracut/dracut.conf.d/rescue/50-rescue.conf
* /usr/lib/dracut/dracut.conf.d/suse.conf.example
* /usr/lib/dracut/dracut.conf.d/test
* /usr/lib/dracut/dracut.conf.d/test-makeroot
* /usr/lib/dracut/dracut.conf.d/test-root
* /usr/lib/dracut/dracut.conf.d/uki-virt/50-uki-virt.conf
* /usr/lib/dracut/modules.d/00bash/module-setup.sh
* /usr/lib/dracut/modules.d/00dash/module-setup.sh
* /usr/lib/dracut/modules.d/00systemd-network-management/module-setup.sh
* /usr/lib/dracut/modules.d/00systemd/module-setup.sh
* /usr/lib/dracut/modules.d/00warpclock/module-setup.sh
* /usr/lib/dracut/modules.d/00warpclock/warpclock.sh
* /usr/lib/dracut/modules.d/01fips-crypto-policies/fips-crypto-policies.sh
* /usr/lib/dracut/modules.d/01fips-crypto-policies/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-ac-power/99-initrd-power-targets.rules
* /usr/lib/dracut/modules.d/01systemd-ac-power/initrd-on-ac-power.target
* /usr/lib/dracut/modules.d/01systemd-ac-power/initrd-on-battery-power.target
* /usr/lib/dracut/modules.d/01systemd-ac-power/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-ask-password/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-battery-check/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-bsod/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-coredump/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-creds/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-cryptsetup/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-hostnamed/99-systemd-networkd-dracut.conf
* /usr/lib/dracut/modules.d/01systemd-hostnamed/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-hostnamed/org.freedesktop.hostname1_dracut.conf
* /usr/lib/dracut/modules.d/01systemd-hostnamed/systemd-hostname-dracut.conf
* /usr/lib/dracut/modules.d/01systemd-initrd/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-integritysetup/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-journald/initrd.conf
* /usr/lib/dracut/modules.d/01systemd-journald/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-ldconfig/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-modules-load/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-networkd/99-default.network
* /usr/lib/dracut/modules.d/01systemd-networkd/99-wait-online-dracut.conf
* /usr/lib/dracut/modules.d/01systemd-networkd/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-networkd/networkd-config.sh
* /usr/lib/dracut/modules.d/01systemd-networkd/networkd-run.sh
* /usr/lib/dracut/modules.d/01systemd-pcrphase/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-portabled/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-pstore/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-repart/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-resolved/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-resolved/resolved-tmpfile-dracut.conf
* /usr/lib/dracut/modules.d/01systemd-sysctl/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-sysext/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-timedated/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-timesyncd/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-timesyncd/timesyncd-tmpfile-dracut.conf
* /usr/lib/dracut/modules.d/01systemd-tmpfiles/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-udevd/module-setup.sh
* /usr/lib/dracut/modules.d/01systemd-veritysetup/module-setup.sh
* /usr/lib/dracut/modules.d/02caps/caps.sh
* /usr/lib/dracut/modules.d/02caps/module-setup.sh
* /usr/lib/dracut/modules.d/02caps/README
* /usr/lib/dracut/modules.d/03modsign/load-modsign-keys.sh
* /usr/lib/dracut/modules.d/03modsign/module-setup.sh
* /usr/lib/dracut/modules.d/03rescue/module-setup.sh
* /usr/lib/dracut/modules.d/04watchdog-modules/module-setup.sh
* /usr/lib/dracut/modules.d/04watchdog/module-setup.sh
* /usr/lib/dracut/modules.d/04watchdog/watchdog-stop.sh
* /usr/lib/dracut/modules.d/04watchdog/watchdog.sh
* /usr/lib/dracut/modules.d/06dbus-broker/module-setup.sh
* /usr/lib/dracut/modules.d/06dbus-daemon/module-setup.sh
* /usr/lib/dracut/modules.d/06rngd/module-setup.sh
* /usr/lib/dracut/modules.d/06rngd/sysconfig
* /usr/lib/dracut/modules.d/09dbus/module-setup.sh
* /usr/lib/dracut/modules.d/10i18n/10-console.rules
* /usr/lib/dracut/modules.d/10i18n/console_init.sh
* /usr/lib/dracut/modules.d/10i18n/module-setup.sh
* /usr/lib/dracut/modules.d/10i18n/parse-i18n.sh
* /usr/lib/dracut/modules.d/10i18n/README
* /usr/lib/dracut/modules.d/30convertfs/convertfs.sh
* /usr/lib/dracut/modules.d/30convertfs/do-convertfs.sh
* /usr/lib/dracut/modules.d/30convertfs/module-setup.sh
* /usr/lib/dracut/modules.d/35connman/cm-config.sh
* /usr/lib/dracut/modules.d/35connman/cm-initrd.service
* /usr/lib/dracut/modules.d/35connman/cm-lib.sh
* /usr/lib/dracut/modules.d/35connman/cm-run.sh
* /usr/lib/dracut/modules.d/35connman/cm-wait-online-initrd.service
* /usr/lib/dracut/modules.d/35connman/module-setup.sh
* /usr/lib/dracut/modules.d/35network-legacy/dhclient-script.sh
* /usr/lib/dracut/modules.d/35network-legacy/dhclient.conf
* /usr/lib/dracut/modules.d/35network-legacy/dhcp-multi.sh
* /usr/lib/dracut/modules.d/35network-legacy/ifup.sh
* /usr/lib/dracut/modules.d/35network-legacy/kill-dhclient.sh
* /usr/lib/dracut/modules.d/35network-legacy/module-setup.sh
* /usr/lib/dracut/modules.d/35network-legacy/net-genrules.sh
* /usr/lib/dracut/modules.d/35network-legacy/parse-bond.sh
* /usr/lib/dracut/modules.d/35network-legacy/parse-bridge.sh
* /usr/lib/dracut/modules.d/35network-legacy/parse-ibft.sh
* /usr/lib/dracut/modules.d/35network-legacy/parse-ifname.sh
* /usr/lib/dracut/modules.d/35network-legacy/parse-ip-opts.sh
* /usr/lib/dracut/modules.d/35network-legacy/parse-team.sh
* /usr/lib/dracut/modules.d/35network-legacy/parse-vlan.sh
* /usr/lib/dracut/modules.d/35network-manager/initrd-no-auto-default.conf
* /usr/lib/dracut/modules.d/35network-manager/module-setup.sh
* /usr/lib/dracut/modules.d/35network-manager/nm-config.sh
* /usr/lib/dracut/modules.d/35network-manager/nm-initrd.service
* /usr/lib/dracut/modules.d/35network-manager/nm-lib.sh
* /usr/lib/dracut/modules.d/35network-manager/nm-run.sh
* /usr/lib/dracut/modules.d/35network-manager/nm-wait-online-initrd.service
* /usr/lib/dracut/modules.d/45drm/module-setup.sh
* /usr/lib/dracut/modules.d/45net-lib/dhcp-root.sh
* /usr/lib/dracut/modules.d/45net-lib/ifname-genrules.sh
* /usr/lib/dracut/modules.d/45net-lib/module-setup.sh
* /usr/lib/dracut/modules.d/45net-lib/net-lib.sh
* /usr/lib/dracut/modules.d/45net-lib/netroot.sh
* /usr/lib/dracut/modules.d/45plymouth/module-setup.sh
* /usr/lib/dracut/modules.d/45plymouth/plymouth-emergency.sh
* /usr/lib/dracut/modules.d/45plymouth/plymouth-newroot.sh
* /usr/lib/dracut/modules.d/45plymouth/plymouth-populate-initrd.sh
* /usr/lib/dracut/modules.d/45plymouth/plymouth-pretrigger.sh
* /usr/lib/dracut/modules.d/45simpledrm/module-setup.sh
* /usr/lib/dracut/modules.d/62bluetooth/module-setup.sh
* /usr/lib/dracut/modules.d/80cms/cms-write-ifcfg.sh
* /usr/lib/dracut/modules.d/80cms/cmsifup.sh
* /usr/lib/dracut/modules.d/80cms/cmssetup.sh
* /usr/lib/dracut/modules.d/80cms/module-setup.sh
* /usr/lib/dracut/modules.d/80lvmmerge/lvmmerge.sh
* /usr/lib/dracut/modules.d/80lvmmerge/module-setup.sh
* /usr/lib/dracut/modules.d/80lvmmerge/README.md
* /usr/lib/dracut/modules.d/80lvmthinpool-monitor/module-setup.sh
* /usr/lib/dracut/modules.d/80lvmthinpool-monitor/start-thinpool-monitor.service
* /usr/lib/dracut/modules.d/80lvmthinpool-monitor/start-thinpool-monitor.sh
* /usr/lib/dracut/modules.d/80test
* /usr/lib/dracut/modules.d/80test-makeroot
* /usr/lib/dracut/modules.d/80test-root
* /usr/lib/dracut/modules.d/81cio_ignore/module-setup.sh
* /usr/lib/dracut/modules.d/81cio_ignore/parse-cio_accept.sh
* /usr/lib/dracut/modules.d/90btrfs/80-btrfs.rules
* /usr/lib/dracut/modules.d/90btrfs/btrfs_device_ready.sh
* /usr/lib/dracut/modules.d/90btrfs/btrfs_finished.sh
* /usr/lib/dracut/modules.d/90btrfs/btrfs_timeout.sh
* /usr/lib/dracut/modules.d/90btrfs/module-setup.sh
* /usr/lib/dracut/modules.d/90crypt/crypt-cleanup.sh
* /usr/lib/dracut/modules.d/90crypt/crypt-lib.sh
* /usr/lib/dracut/modules.d/90crypt/crypt-run-generator.sh
* /usr/lib/dracut/modules.d/90crypt/cryptroot-ask.sh
* /usr/lib/dracut/modules.d/90crypt/module-setup.sh
* /usr/lib/dracut/modules.d/90crypt/parse-crypt.sh
* /usr/lib/dracut/modules.d/90crypt/parse-keydev.sh
* /usr/lib/dracut/modules.d/90crypt/probe-keydev.sh
* /usr/lib/dracut/modules.d/90dm/11-dm.rules
* /usr/lib/dracut/modules.d/90dm/dm-pre-udev.sh
* /usr/lib/dracut/modules.d/90dm/dm-shutdown.sh
* /usr/lib/dracut/modules.d/90dm/module-setup.sh
* /usr/lib/dracut/modules.d/90dmraid/61-dmraid-imsm.rules
* /usr/lib/dracut/modules.d/90dmraid/dmraid.sh
* /usr/lib/dracut/modules.d/90dmraid/module-setup.sh
* /usr/lib/dracut/modules.d/90dmraid/parse-dm.sh
* /usr/lib/dracut/modules.d/90dmsquash-live-autooverlay/create-overlay-genrules.sh
* /usr/lib/dracut/modules.d/90dmsquash-live-autooverlay/create-overlay.sh
* /usr/lib/dracut/modules.d/90dmsquash-live-autooverlay/module-setup.sh
* /usr/lib/dracut/modules.d/90dmsquash-live/apply-live-updates.sh
* /usr/lib/dracut/modules.d/90dmsquash-live/checkisomd5@.service
* /usr/lib/dracut/modules.d/90dmsquash-live/dmsquash-generator.sh
* /usr/lib/dracut/modules.d/90dmsquash-live/dmsquash-live-genrules.sh
* /usr/lib/dracut/modules.d/90dmsquash-live/dmsquash-live-root.sh
* /usr/lib/dracut/modules.d/90dmsquash-live/dmsquash-liveiso-genrules.sh
* /usr/lib/dracut/modules.d/90dmsquash-live/iso-scan.sh
* /usr/lib/dracut/modules.d/90dmsquash-live/module-setup.sh
* /usr/lib/dracut/modules.d/90dmsquash-live/parse-dmsquash-live.sh
* /usr/lib/dracut/modules.d/90dmsquash-live/parse-iso-scan.sh
* /usr/lib/dracut/modules.d/90kernel-modules-extra/module-setup.sh
* /usr/lib/dracut/modules.d/90kernel-modules/insmodpost.sh
* /usr/lib/dracut/modules.d/90kernel-modules/module-setup.sh
* /usr/lib/dracut/modules.d/90kernel-modules/parse-kernel.sh
* /usr/lib/dracut/modules.d/90lvm/64-lvm.rules
* /usr/lib/dracut/modules.d/90lvm/lvm_scan.sh
* /usr/lib/dracut/modules.d/90lvm/module-setup.sh
* /usr/lib/dracut/modules.d/90lvm/parse-lvm.sh
* /usr/lib/dracut/modules.d/90mdraid/59-persistent-storage-md.rules
* /usr/lib/dracut/modules.d/90mdraid/65-md-incremental-imsm.rules
* /usr/lib/dracut/modules.d/90mdraid/md-shutdown.sh
* /usr/lib/dracut/modules.d/90mdraid/mdmon-pre-shutdown.sh
* /usr/lib/dracut/modules.d/90mdraid/mdmon-pre-udev.sh
* /usr/lib/dracut/modules.d/90mdraid/mdraid-cleanup.sh
* /usr/lib/dracut/modules.d/90mdraid/mdraid-needshutdown.sh
* /usr/lib/dracut/modules.d/90mdraid/mdraid-waitclean.sh
* /usr/lib/dracut/modules.d/90mdraid/mdraid_start.sh
* /usr/lib/dracut/modules.d/90mdraid/module-setup.sh
* /usr/lib/dracut/modules.d/90mdraid/parse-md.sh
* /usr/lib/dracut/modules.d/90multipath/module-setup.sh
* /usr/lib/dracut/modules.d/90multipath/multipath-shutdown.sh
* /usr/lib/dracut/modules.d/90multipath/multipathd-configure.service
* /usr/lib/dracut/modules.d/90multipath/multipathd-dracut.conf
* /usr/lib/dracut/modules.d/90multipath/multipathd-needshutdown.sh
* /usr/lib/dracut/modules.d/90multipath/multipathd-stop.sh
* /usr/lib/dracut/modules.d/90multipath/multipathd.sh
* /usr/lib/dracut/modules.d/90numlock/module-setup.sh
* /usr/lib/dracut/modules.d/90numlock/numlock.sh
* /usr/lib/dracut/modules.d/90nvdimm/module-setup.sh
* /usr/lib/dracut/modules.d/90overlayfs/module-setup.sh
* /usr/lib/dracut/modules.d/90overlayfs/mount-overlayfs.sh
* /usr/lib/dracut/modules.d/90overlayfs/prepare-overlayfs.sh
* /usr/lib/dracut/modules.d/90pcmcia/module-setup.sh
* /usr/lib/dracut/modules.d/90ppcmac/load-thermal.sh
* /usr/lib/dracut/modules.d/90ppcmac/module-setup.sh
* /usr/lib/dracut/modules.d/90qemu/module-setup.sh
* /usr/lib/dracut/modules.d/91crypt-gpg/crypt-gpg-lib.sh
* /usr/lib/dracut/modules.d/91crypt-gpg/module-setup.sh
* /usr/lib/dracut/modules.d/91crypt-gpg/README
* /usr/lib/dracut/modules.d/91crypt-loop/crypt-loop-lib.sh
* /usr/lib/dracut/modules.d/91crypt-loop/module-setup.sh
* /usr/lib/dracut/modules.d/91fido2/module-setup.sh
* /usr/lib/dracut/modules.d/91pcsc/module-setup.sh
* /usr/lib/dracut/modules.d/91pcsc/pcscd.service
* /usr/lib/dracut/modules.d/91pcsc/pcscd.socket
* /usr/lib/dracut/modules.d/91pkcs11/module-setup.sh
* /usr/lib/dracut/modules.d/91tpm2-tss/module-setup.sh
* /usr/lib/dracut/modules.d/91zipl/install_zipl_cmdline.sh
* /usr/lib/dracut/modules.d/91zipl/module-setup.sh
* /usr/lib/dracut/modules.d/91zipl/parse-zipl.sh
* /usr/lib/dracut/modules.d/95dcssblk/module-setup.sh
* /usr/lib/dracut/modules.d/95dcssblk/parse-dcssblk.sh
* /usr/lib/dracut/modules.d/95debug/module-setup.sh
* /usr/lib/dracut/modules.d/95fstab-sys/module-setup.sh
* /usr/lib/dracut/modules.d/95fstab-sys/mount-sys.sh
* /usr/lib/dracut/modules.d/95hwdb/module-setup.sh
* /usr/lib/dracut/modules.d/95lunmask/fc_transport_scan_lun.sh
* /usr/lib/dracut/modules.d/95lunmask/module-setup.sh
* /usr/lib/dracut/modules.d/95lunmask/parse-lunmask.sh
* /usr/lib/dracut/modules.d/95lunmask/sas_transport_scan_lun.sh
* /usr/lib/dracut/modules.d/95nvmf/95-nvmf-initqueue.rules
* /usr/lib/dracut/modules.d/95nvmf/module-setup.sh
* /usr/lib/dracut/modules.d/95nvmf/nbftroot.sh
* /usr/lib/dracut/modules.d/95nvmf/nvmf-autoconnect.sh
* /usr/lib/dracut/modules.d/95nvmf/parse-nvmf-boot-connections.sh
* /usr/lib/dracut/modules.d/95resume/module-setup.sh
* /usr/lib/dracut/modules.d/95resume/parse-resume.sh
* /usr/lib/dracut/modules.d/95resume/resume.sh
* /usr/lib/dracut/modules.d/95rootfs-block/59-persistent-storage.rules
* /usr/lib/dracut/modules.d/95rootfs-block/61-persistent-storage.rules
* /usr/lib/dracut/modules.d/95rootfs-block/block-genrules.sh
* /usr/lib/dracut/modules.d/95rootfs-block/module-setup.sh
* /usr/lib/dracut/modules.d/95rootfs-block/mount-root.sh
* /usr/lib/dracut/modules.d/95rootfs-block/parse-block.sh
* /usr/lib/dracut/modules.d/95rootfs-block/rootfallback.sh
* /usr/lib/dracut/modules.d/95squash-erofs/module-setup.sh
* /usr/lib/dracut/modules.d/95squash-squashfs/module-setup.sh
* /usr/lib/dracut/modules.d/95terminfo/module-setup.sh
* /usr/lib/dracut/modules.d/95udev-rules/module-setup.sh
* /usr/lib/dracut/modules.d/95virtfs/module-setup.sh
* /usr/lib/dracut/modules.d/95virtfs/mount-virtfs.sh
* /usr/lib/dracut/modules.d/95virtfs/parse-virtfs.sh
* /usr/lib/dracut/modules.d/95virtiofs/module-setup.sh
* /usr/lib/dracut/modules.d/95virtiofs/mount-virtiofs.sh
* /usr/lib/dracut/modules.d/95virtiofs/parse-virtiofs.sh
* /usr/lib/dracut/modules.d/96securityfs/module-setup.sh
* /usr/lib/dracut/modules.d/96securityfs/securityfs.sh
* /usr/lib/dracut/modules.d/97biosdevname/module-setup.sh
* /usr/lib/dracut/modules.d/97biosdevname/parse-biosdevname.sh
* /usr/lib/dracut/modules.d/97masterkey/masterkey.sh
* /usr/lib/dracut/modules.d/97masterkey/module-setup.sh
* /usr/lib/dracut/modules.d/97masterkey/README
* /usr/lib/dracut/modules.d/97systemd-emergency/module-setup.sh
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-cmdline-ask.service
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-cmdline-ask.sh
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-cmdline.service
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-cmdline.service.8
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-cmdline.service.8.adoc
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-cmdline.sh
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-emergency.service
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-emergency.sh
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-initqueue.service
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-initqueue.service.8
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-initqueue.service.8.adoc
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-initqueue.sh
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-mount.service
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-mount.service.8
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-mount.service.8.adoc
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-mount.sh
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-mount.service
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-mount.service.8
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-mount.service.8.adoc
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-mount.sh
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-pivot.service
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-pivot.service.8
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-pivot.service.8.adoc
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-pivot.sh
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-trigger.service
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-trigger.service.8
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-trigger.service.8.adoc
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-trigger.sh
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-udev.service
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-udev.service.8
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-udev.service.8.adoc
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-pre-udev.sh
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-shutdown-onfailure.service
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-shutdown.service
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-shutdown.service.8
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-shutdown.service.8.adoc
* /usr/lib/dracut/modules.d/98dracut-systemd/dracut-tmpfiles.conf
* /usr/lib/dracut/modules.d/98dracut-systemd/emergency.service
* /usr/lib/dracut/modules.d/98dracut-systemd/module-setup.sh
* /usr/lib/dracut/modules.d/98dracut-systemd/parse-root.sh
* /usr/lib/dracut/modules.d/98dracut-systemd/rootfs-generator.sh
* /usr/lib/dracut/modules.d/98ecryptfs/ecryptfs-mount.sh
* /usr/lib/dracut/modules.d/98ecryptfs/module-setup.sh
* /usr/lib/dracut/modules.d/98ecryptfs/README
* /usr/lib/dracut/modules.d/98integrity/evm-enable.sh
* /usr/lib/dracut/modules.d/98integrity/ima-keys-load.sh
* /usr/lib/dracut/modules.d/98integrity/ima-policy-load.sh
* /usr/lib/dracut/modules.d/98integrity/module-setup.sh
* /usr/lib/dracut/modules.d/98integrity/README
* /usr/lib/dracut/modules.d/98pollcdrom/module-setup.sh
* /usr/lib/dracut/modules.d/98pollcdrom/pollcdrom.sh
* /usr/lib/dracut/modules.d/98syslog/module-setup.sh
* /usr/lib/dracut/modules.d/98syslog/parse-syslog-opts.sh
* /usr/lib/dracut/modules.d/98syslog/README
* /usr/lib/dracut/modules.d/98syslog/rsyslog.conf
* /usr/lib/dracut/modules.d/98syslog/rsyslogd-start.sh
* /usr/lib/dracut/modules.d/98syslog/rsyslogd-stop.sh
* /usr/lib/dracut/modules.d/98syslog/syslog-cleanup.sh
* /usr/lib/dracut/modules.d/98usrmount/module-setup.sh
* /usr/lib/dracut/modules.d/98usrmount/mount-usr.sh
* /usr/lib/dracut/modules.d/99base/dracut-dev-lib.sh
* /usr/lib/dracut/modules.d/99base/dracut-lib.sh
* /usr/lib/dracut/modules.d/99base/init.sh
* /usr/lib/dracut/modules.d/99base/initqueue.sh
* /usr/lib/dracut/modules.d/99base/loginit.sh
* /usr/lib/dracut/modules.d/99base/module-setup.sh
* /usr/lib/dracut/modules.d/99base/parse-root-opts.sh
* /usr/lib/dracut/modules.d/99base/rdsosreport.sh
* /usr/lib/dracut/modules.d/99busybox/module-setup.sh
* /usr/lib/dracut/modules.d/99fs-lib/fs-lib.sh
* /usr/lib/dracut/modules.d/99fs-lib/module-setup.sh
* /usr/lib/dracut/modules.d/99img-lib/img-lib.sh
* /usr/lib/dracut/modules.d/99img-lib/module-setup.sh
* /usr/lib/dracut/modules.d/99memstrack/memstrack-report.sh
* /usr/lib/dracut/modules.d/99memstrack/memstrack-start.sh
* /usr/lib/dracut/modules.d/99memstrack/memstrack.service
* /usr/lib/dracut/modules.d/99memstrack/module-setup.sh
* /usr/lib/dracut/modules.d/99shell-interpreter/module-setup.sh
* /usr/lib/dracut/modules.d/99shutdown/module-setup.sh
* /usr/lib/dracut/modules.d/99shutdown/shutdown.sh
* /usr/lib/dracut/modules.d/99squash-lib/init-squash.sh
* /usr/lib/dracut/modules.d/99squash-lib/module-setup.sh
* /usr/lib/dracut/modules.d/99squash/module-setup.sh
* /usr/lib/dracut/modules.d/99systemd-sysusers/module-setup.sh
* /usr/lib/dracut/modules.d/99uefi-lib/module-setup.sh
* /usr/lib/dracut/modules.d/99uefi-lib/uefi-lib.sh
* /usr/lib/dracut/skipcpio
* /usr/lib/dracut/test/container/Dockerfile-alpine
* /usr/lib/dracut/test/container/Dockerfile-arch
* /usr/lib/dracut/test/container/Dockerfile-azurelinux
* /usr/lib/dracut/test/container/Dockerfile-debian
* /usr/lib/dracut/test/container/Dockerfile-fedora
* /usr/lib/dracut/test/container/Dockerfile-gentoo
* /usr/lib/dracut/test/container/Dockerfile-opensuse
* /usr/lib/dracut/test/container/Dockerfile-void
* /usr/lib/dracut/test/dracut.conf.d/test-makeroot/test-makeroot.conf
* /usr/lib/dracut/test/dracut.conf.d/test-root/test-root.conf
* /usr/lib/dracut/test/dracut.conf.d/test/test.conf
* /usr/lib/dracut/test/Makefile
* /usr/lib/dracut/test/Makefile.testdir
* /usr/lib/dracut/test/modules.d/80test-makeroot/finished-false.sh
* /usr/lib/dracut/test/modules.d/80test-makeroot/module-setup.sh
* /usr/lib/dracut/test/modules.d/80test-root/module-setup.sh
* /usr/lib/dracut/test/modules.d/80test-root/test-init.sh
* /usr/lib/dracut/test/modules.d/80test-root/testsuite.service
* /usr/lib/dracut/test/modules.d/80test-root/testsuite.target
* /usr/lib/dracut/test/modules.d/80test/hard-off.sh
* /usr/lib/dracut/test/modules.d/80test/module-setup.sh
* /usr/lib/dracut/test/run-qemu
* /usr/lib/dracut/test/TEST-10-BASIC/Makefile
* /usr/lib/dracut/test/TEST-10-BASIC/test.sh
* /usr/lib/dracut/test/TEST-11-USR-MOUNT/create-root.sh
* /usr/lib/dracut/test/TEST-11-USR-MOUNT/fstab
* /usr/lib/dracut/test/TEST-11-USR-MOUNT/Makefile
* /usr/lib/dracut/test/TEST-11-USR-MOUNT/test.sh
* /usr/lib/dracut/test/TEST-12-UEFI/Makefile
* /usr/lib/dracut/test/TEST-12-UEFI/test.sh
* /usr/lib/dracut/test/TEST-20-STORAGE/create-root.sh
* /usr/lib/dracut/test/TEST-20-STORAGE/Makefile
* /usr/lib/dracut/test/TEST-20-STORAGE/test.sh
* /usr/lib/dracut/test/TEST-23-IMSM/create-root.sh
* /usr/lib/dracut/test/TEST-23-IMSM/Makefile
* /usr/lib/dracut/test/TEST-23-IMSM/test.sh
* /usr/lib/dracut/test/TEST-26-ENC-RAID-LVM/create-root.sh
* /usr/lib/dracut/test/TEST-26-ENC-RAID-LVM/Makefile
* /usr/lib/dracut/test/TEST-26-ENC-RAID-LVM/test.sh
* /usr/lib/dracut/test/TEST-30-DMSQUASH/Makefile
* /usr/lib/dracut/test/TEST-30-DMSQUASH/test-init.sh
* /usr/lib/dracut/test/TEST-30-DMSQUASH/test.sh
* /usr/lib/dracut/test/TEST-40-SYSTEMD/create-root.sh
* /usr/lib/dracut/test/TEST-40-SYSTEMD/Makefile
* /usr/lib/dracut/test/TEST-40-SYSTEMD/systemd-analyze.sh
* /usr/lib/dracut/test/TEST-40-SYSTEMD/test.sh
* /usr/lib/dracut/test/TEST-41-FULL-SYSTEMD/create-root.sh
* /usr/lib/dracut/test/TEST-41-FULL-SYSTEMD/Makefile
* /usr/lib/dracut/test/TEST-41-FULL-SYSTEMD/test.sh
* /usr/lib/dracut/test/TEST-42-SYSTEMD-INITRD/create-root.sh
* /usr/lib/dracut/test/TEST-42-SYSTEMD-INITRD/Makefile
* /usr/lib/dracut/test/TEST-42-SYSTEMD-INITRD/test.sh
* /usr/lib/dracut/test/TEST-43-KERNEL-INSTALL/Makefile
* /usr/lib/dracut/test/TEST-43-KERNEL-INSTALL/test.sh
* /usr/lib/dracut/test/TEST-60-NFS/client-init.sh
* /usr/lib/dracut/test/TEST-60-NFS/client.link
* /usr/lib/dracut/test/TEST-60-NFS/create-root.sh
* /usr/lib/dracut/test/TEST-60-NFS/dhcpd.conf
* /usr/lib/dracut/test/TEST-60-NFS/exports
* /usr/lib/dracut/test/TEST-60-NFS/finished-false.sh
* /usr/lib/dracut/test/TEST-60-NFS/hard-off.sh
* /usr/lib/dracut/test/TEST-60-NFS/Makefile
* /usr/lib/dracut/test/TEST-60-NFS/server-init.sh
* /usr/lib/dracut/test/TEST-60-NFS/server.link
* /usr/lib/dracut/test/TEST-60-NFS/test.sh
* /usr/lib/dracut/test/TEST-60-NFS/wait-if-server.sh
* /usr/lib/dracut/test/TEST-61-MULTINIC/client-init.sh
* /usr/lib/dracut/test/TEST-61-MULTINIC/client-persistent-lan0.link
* /usr/lib/dracut/test/TEST-61-MULTINIC/client-persistent-lan1.link
* /usr/lib/dracut/test/TEST-61-MULTINIC/client-persistent-lan2.link
* /usr/lib/dracut/test/TEST-61-MULTINIC/client-persistent-lan254.link
* /usr/lib/dracut/test/TEST-61-MULTINIC/client-persistent-lan255.link
* /usr/lib/dracut/test/TEST-61-MULTINIC/client-persistent-lan98.link
* /usr/lib/dracut/test/TEST-61-MULTINIC/client-persistent-lan99.link
* /usr/lib/dracut/test/TEST-61-MULTINIC/create-root.sh
* /usr/lib/dracut/test/TEST-61-MULTINIC/dhcpd.conf
* /usr/lib/dracut/test/TEST-61-MULTINIC/exports
* /usr/lib/dracut/test/TEST-61-MULTINIC/finished-false.sh
* /usr/lib/dracut/test/TEST-61-MULTINIC/hard-off.sh
* /usr/lib/dracut/test/TEST-61-MULTINIC/Makefile
* /usr/lib/dracut/test/TEST-61-MULTINIC/server-init.sh
* /usr/lib/dracut/test/TEST-61-MULTINIC/server.link
* /usr/lib/dracut/test/TEST-61-MULTINIC/test.sh
* /usr/lib/dracut/test/TEST-61-MULTINIC/wait-if-server.sh
* /usr/lib/dracut/test/TEST-62-BONDBRIDGEVLAN/client-init.sh
* /usr/lib/dracut/test/TEST-62-BONDBRIDGEVLAN/client.link
* /usr/lib/dracut/test/TEST-62-BONDBRIDGEVLAN/create-root.sh
* /usr/lib/dracut/test/TEST-62-BONDBRIDGEVLAN/dhcpd.conf
* /usr/lib/dracut/test/TEST-62-BONDBRIDGEVLAN/exports
* /usr/lib/dracut/test/TEST-62-BONDBRIDGEVLAN/finished-false.sh
* /usr/lib/dracut/test/TEST-62-BONDBRIDGEVLAN/hard-off.sh
* /usr/lib/dracut/test/TEST-62-BONDBRIDGEVLAN/Makefile
* /usr/lib/dracut/test/TEST-62-BONDBRIDGEVLAN/server-init.sh
* /usr/lib/dracut/test/TEST-62-BONDBRIDGEVLAN/server.link
* /usr/lib/dracut/test/TEST-62-BONDBRIDGEVLAN/test.sh
* /usr/lib/dracut/test/TEST-62-BONDBRIDGEVLAN/wait-if-server.sh
* /usr/lib/dracut/test/TEST-70-ISCSI/client-init.sh
* /usr/lib/dracut/test/TEST-70-ISCSI/client-persistent-lan0.link
* /usr/lib/dracut/test/TEST-70-ISCSI/client-persistent-lan1.link
* /usr/lib/dracut/test/TEST-70-ISCSI/create-client-root.sh
* /usr/lib/dracut/test/TEST-70-ISCSI/create-server-root.sh
* /usr/lib/dracut/test/TEST-70-ISCSI/dhcpd.conf
* /usr/lib/dracut/test/TEST-70-ISCSI/ibft.pl
* /usr/lib/dracut/test/TEST-70-ISCSI/ibft.table
* /usr/lib/dracut/test/TEST-70-ISCSI/Makefile
* /usr/lib/dracut/test/TEST-70-ISCSI/server-init.sh
* /usr/lib/dracut/test/TEST-70-ISCSI/server.link
* /usr/lib/dracut/test/TEST-70-ISCSI/test.sh
* /usr/lib/dracut/test/TEST-70-ISCSI/wait-if-server.sh
* /usr/lib/dracut/test/TEST-71-ISCSI-MULTI/client-init.sh
* /usr/lib/dracut/test/TEST-71-ISCSI-MULTI/client-persistent-lan0.link
* /usr/lib/dracut/test/TEST-71-ISCSI-MULTI/client-persistent-lan1.link
* /usr/lib/dracut/test/TEST-71-ISCSI-MULTI/create-client-root.sh
* /usr/lib/dracut/test/TEST-71-ISCSI-MULTI/create-server-root.sh
* /usr/lib/dracut/test/TEST-71-ISCSI-MULTI/dhcpd.conf
* /usr/lib/dracut/test/TEST-71-ISCSI-MULTI/Makefile
* /usr/lib/dracut/test/TEST-71-ISCSI-MULTI/server-init.sh
* /usr/lib/dracut/test/TEST-71-ISCSI-MULTI/server.link
* /usr/lib/dracut/test/TEST-71-ISCSI-MULTI/test.sh
* /usr/lib/dracut/test/TEST-71-ISCSI-MULTI/wait-if-server.sh
* /usr/lib/dracut/test/TEST-72-NBD/client-init.sh
* /usr/lib/dracut/test/TEST-72-NBD/client.link
* /usr/lib/dracut/test/TEST-72-NBD/create-client-root.sh
* /usr/lib/dracut/test/TEST-72-NBD/create-encrypted-root.sh
* /usr/lib/dracut/test/TEST-72-NBD/create-server-root.sh
* /usr/lib/dracut/test/TEST-72-NBD/dhcpd.conf
* /usr/lib/dracut/test/TEST-72-NBD/Makefile
* /usr/lib/dracut/test/TEST-72-NBD/server-init.sh
* /usr/lib/dracut/test/TEST-72-NBD/server.link
* /usr/lib/dracut/test/TEST-72-NBD/test.sh
* /usr/lib/dracut/test/TEST-72-NBD/wait-if-server.sh
* /usr/lib/dracut/test/TEST-80-GETARG/Makefile
* /usr/lib/dracut/test/TEST-80-GETARG/test.sh
* /usr/lib/dracut/test/TEST-81-SKIPCPIO/Makefile
* /usr/lib/dracut/test/TEST-81-SKIPCPIO/test.sh
* /usr/lib/dracut/test/TEST-82-DRACUT-CPIO/Makefile
* /usr/lib/dracut/test/TEST-82-DRACUT-CPIO/test.sh
* /usr/lib/dracut/test/test-container.sh
* /usr/lib/dracut/test/test-functions
* /usr/lib/dracut/test/test.sh
* /usr/lib/kernel/install.d/50-dracut.install
* /usr/lib/kernel/install.d/51-dracut-rescue.install
* /usr/lib/systemd/system/dracut-cmdline.service
* /usr/lib/systemd/system/dracut-initqueue.service
* /usr/lib/systemd/system/dracut-mount.service
* /usr/lib/systemd/system/dracut-pre-mount.service
* /usr/lib/systemd/system/dracut-pre-pivot.service
* /usr/lib/systemd/system/dracut-pre-trigger.service
* /usr/lib/systemd/system/dracut-pre-udev.service
* /usr/lib/systemd/system/dracut-shutdown-onfailure.service
* /usr/lib/systemd/system/dracut-shutdown.service
* /usr/lib/systemd/system/initrd.target.wants/dracut-cmdline.service
* /usr/lib/systemd/system/initrd.target.wants/dracut-initqueue.service
* /usr/lib/systemd/system/initrd.target.wants/dracut-mount.service
* /usr/lib/systemd/system/initrd.target.wants/dracut-pre-mount.service
* /usr/lib/systemd/system/initrd.target.wants/dracut-pre-pivot.service
* /usr/lib/systemd/system/initrd.target.wants/dracut-pre-trigger.service
* /usr/lib/systemd/system/initrd.target.wants/dracut-pre-udev.service
* /usr/lib/systemd/system/sysinit.target.wants/dracut-shutdown.service
* /usr/share/bash-completion/completions/dracut
* /usr/share/bash-completion/completions/lsinitrd
* /usr/share/doc/dracut-107/AUTHORS
* /usr/share/doc/dracut-107/COPYING
* /usr/share/doc/dracut-107/README.md
* /usr/share/man/man1/lsinitrd.1.gz
* /usr/share/man/man5/dracut.conf.5.gz
* /usr/share/man/man7/dracut.bootup.7.gz
* /usr/share/man/man7/dracut.cmdline.7.gz
* /usr/share/man/man7/dracut.kernel.7.gz
* /usr/share/man/man7/dracut.modules.7.gz
* /usr/share/man/man8/dracut-catimages.8.gz
* /usr/share/man/man8/dracut-cmdline.service.8.gz
* /usr/share/man/man8/dracut-initqueue.service.8.gz
* /usr/share/man/man8/dracut-mount.service.8.gz
* /usr/share/man/man8/dracut-pre-mount.service.8.gz
* /usr/share/man/man8/dracut-pre-pivot.service.8.gz
* /usr/share/man/man8/dracut-pre-trigger.service.8.gz
* /usr/share/man/man8/dracut-pre-udev.service.8.gz
* /usr/share/man/man8/dracut-shutdown.service.8.gz
* /usr/share/man/man8/dracut.8.gz
* /usr/share/pkgconfig/dracut.pc
