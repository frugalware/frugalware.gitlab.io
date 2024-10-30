+++
draft = false
title = "xfsprogs 6.11.0-2"
version = "6.11.0-2"
description = "XFS filesystem-specific static libraries and headers."
date = "2024-10-28T12:31:11"
aliases = "/packages/2462"
categories = ['apps']
upstreamurl = "http://xfs.org"
arch = "x86_64"
size = "1106148"
usize = "4167806"
sha1sum = "3a918729b80b6bdaa30dfa44ef39bea92b973437"
depends = "['glibc>=2.35', 'icu4c>=76.1', 'inih', 'liburcu', 'libuuid>=2.40.2', 'readline>=8.0']"
reverse_depends = "['kernel-initrd', 'kernel-lts-initrd', 'partitionmanager', 'qtparted']"
+++
### Description: 
XFS filesystem-specific static libraries and headers.

### Files: 
* /usr/bin/fsck.xfs
* /usr/bin/mkfs.xfs
* /usr/bin/xfs_admin
* /usr/bin/xfs_bmap
* /usr/bin/xfs_copy
* /usr/bin/xfs_db
* /usr/bin/xfs_estimate
* /usr/bin/xfs_freeze
* /usr/bin/xfs_fsr
* /usr/bin/xfs_growfs
* /usr/bin/xfs_info
* /usr/bin/xfs_io
* /usr/bin/xfs_logprint
* /usr/bin/xfs_mdrestore
* /usr/bin/xfs_metadump
* /usr/bin/xfs_mkfile
* /usr/bin/xfs_ncheck
* /usr/bin/xfs_property
* /usr/bin/xfs_quota
* /usr/bin/xfs_repair
* /usr/bin/xfs_rtcp
* /usr/bin/xfs_scrub
* /usr/bin/xfs_scrub_all
* /usr/bin/xfs_spaceman
* /usr/include/xfs/handle.h
* /usr/include/xfs/jdm.h
* /usr/include/xfs/linux.h
* /usr/include/xfs/xfs.h
* /usr/include/xfs/xfs_arch.h
* /usr/include/xfs/xfs_da_format.h
* /usr/include/xfs/xfs_format.h
* /usr/include/xfs/xfs_fs.h
* /usr/include/xfs/xfs_fs_compat.h
* /usr/include/xfs/xfs_log_format.h
* /usr/include/xfs/xfs_types.h
* /usr/include/xfs/xqm.h
* /usr/lib/libhandle.la
* /usr/lib/libhandle.so
* /usr/lib/libhandle.so.1
* /usr/lib/libhandle.so.1.0.3
* /usr/lib/systemd/system/system-xfs_scrub.slice
* /usr/lib/systemd/system/xfs_scrub@.service
* /usr/lib/systemd/system/xfs_scrub_all.service
* /usr/lib/systemd/system/xfs_scrub_all.timer
* /usr/lib/systemd/system/xfs_scrub_all_fail.service
* /usr/lib/systemd/system/xfs_scrub_fail@.service
* /usr/lib/systemd/system/xfs_scrub_media@.service
* /usr/lib/systemd/system/xfs_scrub_media_fail@.service
* /usr/lib/udev/rules.d/64-xfs.rules
* /usr/lib/xfsprogs/xfsprogs/xfs_scrub_fail
* /usr/share/doc/xfsprogs-6.11.0/README
* /usr/share/doc/xfsprogs-6.11.0/VERSION
* /usr/share/doc/xfsprogs/CHANGES.gz
* /usr/share/doc/xfsprogs/CREDITS
* /usr/share/doc/xfsprogs/README
* /usr/share/locale/de/LC_MESSAGES/xfsprogs.mo
* /usr/share/locale/pl/LC_MESSAGES/xfsprogs.mo
* /usr/share/man/man2/ioctl_xfs_ag_geometry.2.gz
* /usr/share/man/man2/ioctl_xfs_bulkstat.2.gz
* /usr/share/man/man2/ioctl_xfs_exchange_range.2.gz
* /usr/share/man/man2/ioctl_xfs_fsbulkstat.2.gz
* /usr/share/man/man2/ioctl_xfs_fscounts.2.gz
* /usr/share/man/man2/ioctl_xfs_fsgeometry.2.gz
* /usr/share/man/man2/ioctl_xfs_fsgetxattr.2.gz
* /usr/share/man/man2/ioctl_xfs_fsgetxattra.2.gz
* /usr/share/man/man2/ioctl_xfs_fsinumbers.2.gz
* /usr/share/man/man2/ioctl_xfs_fssetxattr.2.gz
* /usr/share/man/man2/ioctl_xfs_getbmap.2.gz
* /usr/share/man/man2/ioctl_xfs_getbmapa.2.gz
* /usr/share/man/man2/ioctl_xfs_getbmapx.2.gz
* /usr/share/man/man2/ioctl_xfs_getparents.2.gz
* /usr/share/man/man2/ioctl_xfs_getresblks.2.gz
* /usr/share/man/man2/ioctl_xfs_goingdown.2.gz
* /usr/share/man/man2/ioctl_xfs_inumbers.2.gz
* /usr/share/man/man2/ioctl_xfs_scrubv_metadata.2.gz
* /usr/share/man/man2/ioctl_xfs_scrub_metadata.2.gz
* /usr/share/man/man2/ioctl_xfs_setresblks.2.gz
* /usr/share/man/man3/attr_list_by_handle.3.gz
* /usr/share/man/man3/attr_multi_by_handle.3.gz
* /usr/share/man/man3/fd_to_handle.3.gz
* /usr/share/man/man3/free_handle.3.gz
* /usr/share/man/man3/fssetdm_by_handle.3.gz
* /usr/share/man/man3/getparentpaths_by_handle.3.gz
* /usr/share/man/man3/getparents_by_handle.3.gz
* /usr/share/man/man3/handle_to_fshandle.3.gz
* /usr/share/man/man3/open_by_handle.3.gz
* /usr/share/man/man3/path_to_fshandle.3.gz
* /usr/share/man/man3/path_to_handle.3.gz
* /usr/share/man/man3/readlink_by_handle.3.gz
* /usr/share/man/man3/xfsctl.3.gz
* /usr/share/man/man5/projects.5.gz
* /usr/share/man/man5/projid.5.gz
* /usr/share/man/man5/xfs.5.gz
* /usr/share/man/man8/fsck.xfs.8.gz
* /usr/share/man/man8/mkfs.xfs.8.gz
* /usr/share/man/man8/xfs_admin.8.gz
* /usr/share/man/man8/xfs_bmap.8.gz
* /usr/share/man/man8/xfs_copy.8.gz
* /usr/share/man/man8/xfs_db.8.gz
* /usr/share/man/man8/xfs_estimate.8.gz
* /usr/share/man/man8/xfs_freeze.8.gz
* /usr/share/man/man8/xfs_fsr.8.gz
* /usr/share/man/man8/xfs_growfs.8.gz
* /usr/share/man/man8/xfs_info.8.gz
* /usr/share/man/man8/xfs_io.8.gz
* /usr/share/man/man8/xfs_logprint.8.gz
* /usr/share/man/man8/xfs_mdrestore.8.gz
* /usr/share/man/man8/xfs_metadump.8.gz
* /usr/share/man/man8/xfs_mkfile.8.gz
* /usr/share/man/man8/xfs_ncheck.8.gz
* /usr/share/man/man8/xfs_property.8.gz
* /usr/share/man/man8/xfs_quota.8.gz
* /usr/share/man/man8/xfs_repair.8.gz
* /usr/share/man/man8/xfs_rtcp.8.gz
* /usr/share/man/man8/xfs_scrub.8.gz
* /usr/share/man/man8/xfs_scrub_all.8.gz
* /usr/share/man/man8/xfs_spaceman.8.gz
* /usr/share/xfsprogs/mkfs/dax_x86_64.conf
* /usr/share/xfsprogs/mkfs/lts_4.19.conf
* /usr/share/xfsprogs/mkfs/lts_5.10.conf
* /usr/share/xfsprogs/mkfs/lts_5.15.conf
* /usr/share/xfsprogs/mkfs/lts_5.4.conf
* /usr/share/xfsprogs/mkfs/lts_6.1.conf
* /usr/share/xfsprogs/mkfs/lts_6.6.conf
* /usr/share/xfsprogs/xfs_scrub_all.cron
