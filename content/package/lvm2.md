+++
draft = false
title = "lvm2 2.03.23-2"
version = "2.03.23-2"
description = "Logical Volume Manager 2 utilities"
date = "2024-01-02T14:48:45"
aliases = "/packages/3220"
categories = ['base']
upstreamurl = "http://sources.redhat.com/lvm2/"
arch = "x86_64"
size = "1411556"
usize = "4053810"
sha1sum = "fb8927fd67c63cc911d60d337874e539864a2975"
depends = "['libaio', 'libblkid>=2.31.1-3', 'libsystemd', 'libudev>=242', 'lvm2-libs', 'ncurses>=6.1', 'readline>=8.0', 'systemd-systemctl', 'thin-provisioning-tools>=1.0.2']"
reverse_depends = "['docker', 'dracut', 'kernel-initrd', 'kernel-lts-initrd', 'libvirt', 'multipath-tools', 'parted', 'udisks2', 'virtualbox']"
+++
### Description: 
Logical Volume Manager 2 utilities

### Files: 
* /etc/dracut.conf.d/11-lvm2.conf
* /etc/lvm/cache/.cache
* /etc/lvm/lvm.conf
* /etc/lvm/lvmlocal.conf
* /etc/lvm/profile/cache-mq.profile
* /etc/lvm/profile/cache-smq.profile
* /etc/lvm/profile/command_profile_template.profile
* /etc/lvm/profile/lvmdbusd.profile
* /etc/lvm/profile/metadata_profile_template.profile
* /etc/lvm/profile/thin-generic.profile
* /etc/lvm/profile/thin-performance.profile
* /etc/lvm/profile/vdo-small.profile
* /usr/bin/blkdeactivate
* /usr/bin/dmeventd
* /usr/bin/dmfilemapd
* /usr/bin/dmsetup
* /usr/bin/dmstats
* /usr/bin/fsadm
* /usr/bin/lvchange
* /usr/bin/lvconvert
* /usr/bin/lvcreate
* /usr/bin/lvdisplay
* /usr/bin/lvextend
* /usr/bin/lvm
* /usr/bin/lvmconfig
* /usr/bin/lvmdevices
* /usr/bin/lvmdiskscan
* /usr/bin/lvmdump
* /usr/bin/lvmpolld
* /usr/bin/lvmsadc
* /usr/bin/lvmsar
* /usr/bin/lvm_import_vdo
* /usr/bin/lvreduce
* /usr/bin/lvremove
* /usr/bin/lvrename
* /usr/bin/lvresize
* /usr/bin/lvs
* /usr/bin/lvscan
* /usr/bin/pvchange
* /usr/bin/pvck
* /usr/bin/pvcreate
* /usr/bin/pvdisplay
* /usr/bin/pvmove
* /usr/bin/pvremove
* /usr/bin/pvresize
* /usr/bin/pvs
* /usr/bin/pvscan
* /usr/bin/vgcfgbackup
* /usr/bin/vgcfgrestore
* /usr/bin/vgchange
* /usr/bin/vgck
* /usr/bin/vgconvert
* /usr/bin/vgcreate
* /usr/bin/vgdisplay
* /usr/bin/vgexport
* /usr/bin/vgextend
* /usr/bin/vgimport
* /usr/bin/vgimportclone
* /usr/bin/vgimportdevices
* /usr/bin/vgmerge
* /usr/bin/vgmknodes
* /usr/bin/vgreduce
* /usr/bin/vgremove
* /usr/bin/vgrename
* /usr/bin/vgs
* /usr/bin/vgscan
* /usr/bin/vgsplit
* /usr/lib/device-mapper/libdevmapper-event-lvm2vdo.so
* /usr/lib/libdevmapper-event-lvm2vdo.so
* /usr/lib/lvresize_fs_helper
* /usr/lib/systemd/system/blk-availability.service
* /usr/lib/systemd/system/dm-event.service
* /usr/lib/systemd/system/dm-event.socket
* /usr/lib/systemd/system/lvm2-lvmpolld.service
* /usr/lib/systemd/system/lvm2-lvmpolld.socket
* /usr/lib/systemd/system/lvm2-monitor.service
* /usr/lib/tmpfiles.d/lvm2.conf
* /usr/lib/udev/rules.d/10-dm.rules
* /usr/lib/udev/rules.d/11-dm-lvm.rules
* /usr/lib/udev/rules.d/13-dm-disk.rules
* /usr/lib/udev/rules.d/69-dm-lvm.rules
* /usr/lib/udev/rules.d/95-dm-notify.rules
* /usr/share/doc/lvm2-2.03.23/COPYING
* /usr/share/doc/lvm2-2.03.23/COPYING.BSD
* /usr/share/doc/lvm2-2.03.23/COPYING.LIB
* /usr/share/doc/lvm2-2.03.23/INSTALL
* /usr/share/doc/lvm2-2.03.23/README
* /usr/share/doc/lvm2-2.03.23/README.Frugalware
* /usr/share/doc/lvm2-2.03.23/VERSION
* /usr/share/man/man5/lvm.conf.5.gz
* /usr/share/man/man7/lvmautoactivation.7.gz
* /usr/share/man/man7/lvmcache.7.gz
* /usr/share/man/man7/lvmraid.7.gz
* /usr/share/man/man7/lvmreport.7.gz
* /usr/share/man/man7/lvmsystemid.7.gz
* /usr/share/man/man7/lvmthin.7.gz
* /usr/share/man/man7/lvmvdo.7.gz
* /usr/share/man/man8/blkdeactivate.8.gz
* /usr/share/man/man8/dmeventd.8.gz
* /usr/share/man/man8/dmfilemapd.8.gz
* /usr/share/man/man8/dmsetup.8.gz
* /usr/share/man/man8/dmstats.8.gz
* /usr/share/man/man8/fsadm.8.gz
* /usr/share/man/man8/lvchange.8.gz
* /usr/share/man/man8/lvconvert.8.gz
* /usr/share/man/man8/lvcreate.8.gz
* /usr/share/man/man8/lvdisplay.8.gz
* /usr/share/man/man8/lvextend.8.gz
* /usr/share/man/man8/lvm-config.8.gz
* /usr/share/man/man8/lvm-dumpconfig.8.gz
* /usr/share/man/man8/lvm-fullreport.8.gz
* /usr/share/man/man8/lvm-lvpoll.8.gz
* /usr/share/man/man8/lvm.8.gz
* /usr/share/man/man8/lvmconfig.8.gz
* /usr/share/man/man8/lvmdevices.8.gz
* /usr/share/man/man8/lvmdiskscan.8.gz
* /usr/share/man/man8/lvmdump.8.gz
* /usr/share/man/man8/lvmpolld.8.gz
* /usr/share/man/man8/lvmsadc.8.gz
* /usr/share/man/man8/lvmsar.8.gz
* /usr/share/man/man8/lvm_import_vdo.8.gz
* /usr/share/man/man8/lvreduce.8.gz
* /usr/share/man/man8/lvremove.8.gz
* /usr/share/man/man8/lvrename.8.gz
* /usr/share/man/man8/lvresize.8.gz
* /usr/share/man/man8/lvs.8.gz
* /usr/share/man/man8/lvscan.8.gz
* /usr/share/man/man8/pvchange.8.gz
* /usr/share/man/man8/pvck.8.gz
* /usr/share/man/man8/pvcreate.8.gz
* /usr/share/man/man8/pvdisplay.8.gz
* /usr/share/man/man8/pvmove.8.gz
* /usr/share/man/man8/pvremove.8.gz
* /usr/share/man/man8/pvresize.8.gz
* /usr/share/man/man8/pvs.8.gz
* /usr/share/man/man8/pvscan.8.gz
* /usr/share/man/man8/vgcfgbackup.8.gz
* /usr/share/man/man8/vgcfgrestore.8.gz
* /usr/share/man/man8/vgchange.8.gz
* /usr/share/man/man8/vgck.8.gz
* /usr/share/man/man8/vgconvert.8.gz
* /usr/share/man/man8/vgcreate.8.gz
* /usr/share/man/man8/vgdisplay.8.gz
* /usr/share/man/man8/vgexport.8.gz
* /usr/share/man/man8/vgextend.8.gz
* /usr/share/man/man8/vgimport.8.gz
* /usr/share/man/man8/vgimportclone.8.gz
* /usr/share/man/man8/vgimportdevices.8.gz
* /usr/share/man/man8/vgmerge.8.gz
* /usr/share/man/man8/vgmknodes.8.gz
* /usr/share/man/man8/vgreduce.8.gz
* /usr/share/man/man8/vgremove.8.gz
* /usr/share/man/man8/vgrename.8.gz
* /usr/share/man/man8/vgs.8.gz
* /usr/share/man/man8/vgscan.8.gz
* /usr/share/man/man8/vgsplit.8.gz
