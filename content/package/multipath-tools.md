+++
draft = false
title = "multipath-tools 0.11.1-1"
version = "0.11.1-1"
description = "Device mapper target autoconfig"
date = "2025-02-11T09:10:24"
aliases = "/packages/218697"
categories = ['base']
upstreamurl = "http://christophe.varoqui.free.fr"
arch = "x86_64"
size = "359540"
usize = "1065099"
sha1sum = "1340340a0c3b6846cf9c21f124e6d011f72921da"
depends = "['json-c>=0.14', 'libaio>=0.3.110-5', 'libsystemd>=242', 'libudev>=242', 'liburcu>=0.13', 'lvm2>=2.03', 'readline>=8.0']"
reverse_depends = "['dracut']"
+++
### Description: 
Device mapper target autoconfig

### Files: 
* /usr/bin/kpartx
* /usr/bin/mpathpersist
* /usr/bin/multipath
* /usr/bin/multipathc
* /usr/bin/multipathd
* /usr/include/libdmmp/libdmmp.h
* /usr/include/mpath_cmd.h
* /usr/include/mpath_persist.h
* /usr/include/mpath_valid.h
* /usr/lib/libdmmp.so
* /usr/lib/libdmmp.so.0.2.0
* /usr/lib/libmpathcmd.so
* /usr/lib/libmpathcmd.so.0
* /usr/lib/libmpathpersist.so
* /usr/lib/libmpathpersist.so.0
* /usr/lib/libmpathutil.so
* /usr/lib/libmpathutil.so.0
* /usr/lib/libmpathvalid.so
* /usr/lib/libmpathvalid.so.0
* /usr/lib/libmultipath.so
* /usr/lib/libmultipath.so.0
* /usr/lib/multipath/libcheckcciss_tur.so
* /usr/lib/multipath/libcheckdirectio.so
* /usr/lib/multipath/libcheckemc_clariion.so
* /usr/lib/multipath/libcheckhp_sw.so
* /usr/lib/multipath/libcheckrdac.so
* /usr/lib/multipath/libcheckreadsector0.so
* /usr/lib/multipath/libchecktur.so
* /usr/lib/multipath/libforeign-nvme.so
* /usr/lib/multipath/libprioalua.so
* /usr/lib/multipath/libprioana.so
* /usr/lib/multipath/libprioconst.so
* /usr/lib/multipath/libpriodatacore.so
* /usr/lib/multipath/libprioemc.so
* /usr/lib/multipath/libpriohds.so
* /usr/lib/multipath/libpriohp_sw.so
* /usr/lib/multipath/libprioiet.so
* /usr/lib/multipath/libprioontap.so
* /usr/lib/multipath/libpriopath_latency.so
* /usr/lib/multipath/libpriorandom.so
* /usr/lib/multipath/libpriordac.so
* /usr/lib/multipath/libpriosysfs.so
* /usr/lib/multipath/libprioweightedpath.so
* /usr/lib/pkgconfig/libdmmp.pc
* /usr/lib/systemd/system/multipathd.service
* /usr/lib/systemd/system/multipathd.socket
* /usr/lib/tmpfiles.d/multipath.conf
* /usr/lib/udev/kpartx_id
* /usr/lib/udev/rules.d/11-dm-mpath.rules
* /usr/lib/udev/rules.d/11-dm-parts.rules
* /usr/lib/udev/rules.d/56-multipath.rules
* /usr/lib/udev/rules.d/66-kpartx.rules
* /usr/lib/udev/rules.d/68-del-part-nodes.rules
* /usr/lib/udev/rules.d/99-z-dm-mpath-late.rules
* /usr/share/doc/multipath-tools-0.11.1/COPYING
* /usr/share/doc/multipath-tools-0.11.1/README.md
* /usr/share/man/man3/dmmp_context_free.3.gz
* /usr/share/man/man3/dmmp_context_log_func_set.3.gz
* /usr/share/man/man3/dmmp_context_log_priority_get.3.gz
* /usr/share/man/man3/dmmp_context_log_priority_set.3.gz
* /usr/share/man/man3/dmmp_context_new.3.gz
* /usr/share/man/man3/dmmp_context_timeout_get.3.gz
* /usr/share/man/man3/dmmp_context_timeout_set.3.gz
* /usr/share/man/man3/dmmp_context_userdata_get.3.gz
* /usr/share/man/man3/dmmp_context_userdata_set.3.gz
* /usr/share/man/man3/dmmp_flush_mpath.3.gz
* /usr/share/man/man3/dmmp_last_error_msg.3.gz
* /usr/share/man/man3/dmmp_log_priority_str.3.gz
* /usr/share/man/man3/dmmp_mpath_array_free.3.gz
* /usr/share/man/man3/dmmp_mpath_array_get.3.gz
* /usr/share/man/man3/dmmp_mpath_kdev_name_get.3.gz
* /usr/share/man/man3/dmmp_mpath_name_get.3.gz
* /usr/share/man/man3/dmmp_mpath_wwid_get.3.gz
* /usr/share/man/man3/dmmp_path_array_get.3.gz
* /usr/share/man/man3/dmmp_path_blk_name_get.3.gz
* /usr/share/man/man3/dmmp_path_group_array_get.3.gz
* /usr/share/man/man3/dmmp_path_group_id_get.3.gz
* /usr/share/man/man3/dmmp_path_group_priority_get.3.gz
* /usr/share/man/man3/dmmp_path_group_selector_get.3.gz
* /usr/share/man/man3/dmmp_path_group_status_get.3.gz
* /usr/share/man/man3/dmmp_path_group_status_str.3.gz
* /usr/share/man/man3/dmmp_path_status_get.3.gz
* /usr/share/man/man3/dmmp_path_status_str.3.gz
* /usr/share/man/man3/dmmp_reconfig.3.gz
* /usr/share/man/man3/dmmp_strerror.3.gz
* /usr/share/man/man3/libdmmp.h.3.gz
* /usr/share/man/man3/mpath_persistent_reserve_in.3.gz
* /usr/share/man/man3/mpath_persistent_reserve_out.3.gz
* /usr/share/man/man5/multipath.conf.5.gz
* /usr/share/man/man8/kpartx.8.gz
* /usr/share/man/man8/mpathpersist.8.gz
* /usr/share/man/man8/multipath.8.gz
* /usr/share/man/man8/multipathc.8.gz
* /usr/share/man/man8/multipathd.8.gz
