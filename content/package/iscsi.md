+++
draft = false
title = "iscsi 2.1.9-1"
version = "2.1.9-1"
description = "Open-iSCSI project is a high performance, transport independent"
date = "2024-01-14T13:51:35"
aliases = "/packages/74664"
categories = ['network-extra']
upstreamurl = "https://github.com/open-iscsi/open-iscsi"
arch = "x86_64"
size = "419072"
usize = "1507536"
sha1sum = "8605ad407e3488cc2d974b8709cf21de52f0d5a6"
depends = "['kmod', 'libsystemd', 'open-isns>=0.102']"
reverse_depends = "['dracut-network', 'libvirt']"
+++
### Description: 
Open-iSCSI project is a high performance, transport independent

### Files: 
* /etc/iscsi/initiatorname.iscsi
* /etc/iscsi/iscsid.conf
* /etc/logrotate.d/iscsiuiolog
* /etc/sysconfig/iscsid
* /etc/udev/rules.d/50-iscsi-firmware-login.rules
* /usr/bin/brcm_iscsiuio
* /usr/bin/iscsi-gen-initiatorname
* /usr/bin/iscsi-iname
* /usr/bin/iscsiadm
* /usr/bin/iscsid
* /usr/bin/iscsistart
* /usr/bin/iscsiuio
* /usr/bin/iscsi_discovery
* /usr/bin/iscsi_fw_login
* /usr/bin/iscsi_offload
* /usr/include/libopeniscsiusr.h
* /usr/include/libopeniscsiusr_common.h
* /usr/include/libopeniscsiusr_iface.h
* /usr/include/libopeniscsiusr_node.h
* /usr/include/libopeniscsiusr_session.h
* /usr/lib/libopeniscsiusr.so
* /usr/lib/libopeniscsiusr.so.0
* /usr/lib/libopeniscsiusr.so.0.2.0
* /usr/lib/pkgconfig/libopeniscsiusr.pc
* /usr/lib/systemd/system-generators/ibft-rule-generator
* /usr/lib/systemd/system/iscsi-init.service
* /usr/lib/systemd/system/iscsi.service
* /usr/lib/systemd/system/iscsid.service
* /usr/lib/systemd/system/iscsid.socket
* /usr/lib/systemd/system/iscsiuio.service
* /usr/lib/systemd/system/iscsiuio.socket
* /usr/share/doc/iscsi-2.1.9/Changelog
* /usr/share/doc/iscsi-2.1.9/COPYING
* /usr/share/doc/iscsi-2.1.9/README
* /usr/share/doc/iscsi-2.1.9/THANKS
* /usr/share/doc/iscsi-2.1.9/TODO
* /usr/share/man/man3/iscsi_context_free.3.gz
* /usr/share/man/man3/iscsi_context_log_func_set.3.gz
* /usr/share/man/man3/iscsi_context_log_priority_get.3.gz
* /usr/share/man/man3/iscsi_context_log_priority_set.3.gz
* /usr/share/man/man3/iscsi_context_new.3.gz
* /usr/share/man/man3/iscsi_context_userdata_get.3.gz
* /usr/share/man/man3/iscsi_context_userdata_set.3.gz
* /usr/share/man/man3/iscsi_default_iface_setup.3.gz
* /usr/share/man/man3/iscsi_ifaces_free.3.gz
* /usr/share/man/man3/iscsi_ifaces_get.3.gz
* /usr/share/man/man3/iscsi_iface_dump_config.3.gz
* /usr/share/man/man3/iscsi_iface_free.3.gz
* /usr/share/man/man3/iscsi_iface_get.3.gz
* /usr/share/man/man3/iscsi_iface_hwaddress_get.3.gz
* /usr/share/man/man3/iscsi_iface_iname_get.3.gz
* /usr/share/man/man3/iscsi_iface_ipaddress_get.3.gz
* /usr/share/man/man3/iscsi_iface_name_get.3.gz
* /usr/share/man/man3/iscsi_iface_netdev_get.3.gz
* /usr/share/man/man3/iscsi_iface_port_speed_get.3.gz
* /usr/share/man/man3/iscsi_iface_port_state_get.3.gz
* /usr/share/man/man3/iscsi_iface_print_config.3.gz
* /usr/share/man/man3/iscsi_iface_transport_name_get.3.gz
* /usr/share/man/man3/iscsi_is_default_iface.3.gz
* /usr/share/man/man3/iscsi_log_priority_str.3.gz
* /usr/share/man/man3/iscsi_nodes_free.3.gz
* /usr/share/man/man3/iscsi_nodes_get.3.gz
* /usr/share/man/man3/iscsi_node_conn_address_get.3.gz
* /usr/share/man/man3/iscsi_node_conn_is_ipv6.3.gz
* /usr/share/man/man3/iscsi_node_conn_port_get.3.gz
* /usr/share/man/man3/iscsi_node_dump_config.3.gz
* /usr/share/man/man3/iscsi_node_iface_name_get.3.gz
* /usr/share/man/man3/iscsi_node_portal_get.3.gz
* /usr/share/man/man3/iscsi_node_print_config.3.gz
* /usr/share/man/man3/iscsi_node_target_name_get.3.gz
* /usr/share/man/man3/iscsi_node_tpgt_get.3.gz
* /usr/share/man/man3/iscsi_sessions_free.3.gz
* /usr/share/man/man3/iscsi_sessions_get.3.gz
* /usr/share/man/man3/iscsi_session_abort_tmo_get.3.gz
* /usr/share/man/man3/iscsi_session_address_get.3.gz
* /usr/share/man/man3/iscsi_session_free.3.gz
* /usr/share/man/man3/iscsi_session_get.3.gz
* /usr/share/man/man3/iscsi_session_iface_get.3.gz
* /usr/share/man/man3/iscsi_session_lu_reset_tmo_get.3.gz
* /usr/share/man/man3/iscsi_session_password_get.3.gz
* /usr/share/man/man3/iscsi_session_password_in_get.3.gz
* /usr/share/man/man3/iscsi_session_persistent_address_get.3.gz
* /usr/share/man/man3/iscsi_session_persistent_port_get.3.gz
* /usr/share/man/man3/iscsi_session_port_get.3.gz
* /usr/share/man/man3/iscsi_session_recovery_tmo_get.3.gz
* /usr/share/man/man3/iscsi_session_sid_get.3.gz
* /usr/share/man/man3/iscsi_session_target_name_get.3.gz
* /usr/share/man/man3/iscsi_session_tgt_reset_tmo_get.3.gz
* /usr/share/man/man3/iscsi_session_tpgt_get.3.gz
* /usr/share/man/man3/iscsi_session_username_get.3.gz
* /usr/share/man/man3/iscsi_session_username_in_get.3.gz
* /usr/share/man/man3/iscsi_strerror.3.gz
* /usr/share/man/man3/libopeniscsiusr.h.3.gz
* /usr/share/man/man8/iscsi-gen-initiatorname.8.gz
* /usr/share/man/man8/iscsi-iname.8.gz
* /usr/share/man/man8/iscsiadm.8.gz
* /usr/share/man/man8/iscsid.8.gz
* /usr/share/man/man8/iscsistart.8.gz
* /usr/share/man/man8/iscsiuio.8.gz
* /usr/share/man/man8/iscsi_discovery.8.gz
* /usr/share/man/man8/iscsi_fw_login.8.gz
* /var/lib/iscsi/ifaces/iface.example
