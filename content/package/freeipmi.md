+++
draft = false
title = "freeipmi 1.6.10-1"
version = "1.6.10-1"
date = "2023-01-09T13:52:52"
categories = ['apps-extra']
upstreamurl = "https://www.gnu.org/software/freeipmi/"
arch = "x86_64"
size = "2113068"
usize = "12916420"
sha1sum = "1cf63f1efd16907395b555220462d6394a49a8b0"
depends = "['glibc', 'libgcrypt', 'libgpg-error']"
files = "['etc/', 'etc/freeipmi/', 'etc/freeipmi/freeipmi.conf', 'etc/freeipmi/freeipmi_interpret_sel.conf', 'etc/freeipmi/freeipmi_interpret_sensor.conf', 'etc/freeipmi/ipmidetect.conf', 'etc/freeipmi/ipmidetectd.conf', 'etc/freeipmi/ipmiseld.conf', 'etc/freeipmi/libipmiconsole.conf', 'etc/init.d/', 'etc/init.d/bmc-watchdog', 'etc/init.d/ipmidetectd', 'etc/init.d/ipmiseld', 'etc/sysconfig/', 'etc/sysconfig/bmc-watchdog', 'usr/', 'usr/include/', 'usr/include/freeipmi/', 'usr/include/freeipmi/api/', 'usr/include/freeipmi/api/ipmi-api.h', 'usr/include/freeipmi/api/ipmi-chassis-cmds-api.h', 'usr/include/freeipmi/api/ipmi-dcmi-cmds-api.h', 'usr/include/freeipmi/api/ipmi-device-global-cmds-api.h', 'usr/include/freeipmi/api/ipmi-event-cmds-api.h', 'usr/include/freeipmi/api/ipmi-firmware-firewall-command-discovery-cmds-api.h', 'usr/include/freeipmi/api/ipmi-fru-inventory-device-cmds-api.h', 'usr/include/freeipmi/api/ipmi-lan-cmds-api.h', 'usr/include/freeipmi/api/ipmi-messaging-support-cmds-api.h', 'usr/include/freeipmi/api/ipmi-oem-intel-node-manager-cmds-api.h', 'usr/include/freeipmi/api/ipmi-pef-and-alerting-cmds-api.h', 'usr/include/freeipmi/api/ipmi-rmcpplus-support-and-payload-cmds-api.h', 'usr/include/freeipmi/api/ipmi-sdr-repository-cmds-api.h', 'usr/include/freeipmi/api/ipmi-sel-cmds-api.h', 'usr/include/freeipmi/api/ipmi-sensor-cmds-api.h', 'usr/include/freeipmi/api/ipmi-serial-modem-cmds-api.h', 'usr/include/freeipmi/api/ipmi-sol-cmds-api.h', 'usr/include/freeipmi/cmds/', 'usr/include/freeipmi/cmds/ipmi-bmc-watchdog-timer-cmds.h', 'usr/include/freeipmi/cmds/ipmi-chassis-cmds.h', 'usr/include/freeipmi/cmds/ipmi-dcmi-cmds.h', 'usr/include/freeipmi/cmds/ipmi-dcmi-oem-cmds.h', 'usr/include/freeipmi/cmds/ipmi-device-global-cmds.h', 'usr/include/freeipmi/cmds/ipmi-event-cmds.h', 'usr/include/freeipmi/cmds/ipmi-firmware-firewall-command-discovery-cmds.h', 'usr/include/freeipmi/cmds/ipmi-fru-inventory-device-cmds.h', 'usr/include/freeipmi/cmds/ipmi-lan-cmds.h', 'usr/include/freeipmi/cmds/ipmi-messaging-support-cmds.h', 'usr/include/freeipmi/cmds/ipmi-oem-intel-node-manager-cmds.h', 'usr/include/freeipmi/cmds/ipmi-pef-and-alerting-cmds.h', 'usr/include/freeipmi/cmds/ipmi-rmcpplus-support-and-payload-cmds.h', 'usr/include/freeipmi/cmds/ipmi-sdr-repository-cmds.h', 'usr/include/freeipmi/cmds/ipmi-sel-cmds.h', 'usr/include/freeipmi/cmds/ipmi-sensor-cmds.h', 'usr/include/freeipmi/cmds/ipmi-serial-modem-cmds.h', 'usr/include/freeipmi/cmds/ipmi-sol-cmds.h', 'usr/include/freeipmi/cmds/rmcp-cmds.h', 'usr/include/freeipmi/debug/', 'usr/include/freeipmi/debug/ipmi-debug.h', 'usr/include/freeipmi/driver/', 'usr/include/freeipmi/driver/ipmi-inteldcmi-driver.h', 'usr/include/freeipmi/driver/ipmi-kcs-driver.h', 'usr/include/freeipmi/driver/ipmi-openipmi-driver.h', 'usr/include/freeipmi/driver/ipmi-ssif-driver.h', 'usr/include/freeipmi/driver/ipmi-sunbmc-driver.h', 'usr/include/freeipmi/fiid/', 'usr/include/freeipmi/fiid/fiid.h', 'usr/include/freeipmi/freeipmi.h', 'usr/include/freeipmi/fru/', 'usr/include/freeipmi/fru/ipmi-fru.h', 'usr/include/freeipmi/interface/', 'usr/include/freeipmi/interface/ipmi-interface.h', 'usr/include/freeipmi/interface/ipmi-ipmb-interface.h', 'usr/include/freeipmi/interface/ipmi-kcs-interface.h', 'usr/include/freeipmi/interface/ipmi-lan-interface.h', 'usr/include/freeipmi/interface/ipmi-rmcpplus-interface.h', 'usr/include/freeipmi/interface/rmcp-interface.h', 'usr/include/freeipmi/interpret/', 'usr/include/freeipmi/interpret/ipmi-interpret.h', 'usr/include/freeipmi/locate/', 'usr/include/freeipmi/locate/ipmi-locate.h', 'usr/include/freeipmi/payload/', 'usr/include/freeipmi/payload/ipmi-sol-payload.h', 'usr/include/freeipmi/record-format/', 'usr/include/freeipmi/record-format/ipmi-cipher-suite-record-format.h', 'usr/include/freeipmi/record-format/ipmi-fru-dimmspd-record-format.h', 'usr/include/freeipmi/record-format/ipmi-fru-information-record-format.h', 'usr/include/freeipmi/record-format/ipmi-fru-oem-record-format.h', 'usr/include/freeipmi/record-format/ipmi-platform-event-trap-record-format.h', 'usr/include/freeipmi/record-format/ipmi-sdr-oem-record-format.h', 'usr/include/freeipmi/record-format/ipmi-sdr-record-format.h', 'usr/include/freeipmi/record-format/ipmi-sel-oem-record-format.h', 'usr/include/freeipmi/record-format/ipmi-sel-record-format.h', 'usr/include/freeipmi/record-format/oem/', 'usr/include/freeipmi/record-format/oem/ipmi-fru-wistron-oem-record-format.h', 'usr/include/freeipmi/record-format/oem/ipmi-sdr-oem-intel-node-manager-record-format.h', 'usr/include/freeipmi/record-format/oem/ipmi-sdr-oem-intel-record-format.h', 'usr/include/freeipmi/record-format/oem/ipmi-sel-oem-intel-record-format.h', 'usr/include/freeipmi/record-format/oem/ipmi-sel-oem-linux-kernel-record-format.h', 'usr/include/freeipmi/sdr/', 'usr/include/freeipmi/sdr/ipmi-sdr-oem.h', 'usr/include/freeipmi/sdr/ipmi-sdr.h', 'usr/include/freeipmi/sdr/oem/', 'usr/include/freeipmi/sdr/oem/ipmi-sdr-oem-intel-node-manager.h', 'usr/include/freeipmi/sel/', 'usr/include/freeipmi/sel/ipmi-sel.h', 'usr/include/freeipmi/sensor-read/', 'usr/include/freeipmi/sensor-read/ipmi-sensor-read.h', 'usr/include/freeipmi/spec/', 'usr/include/freeipmi/spec/ipmi-authentication-type-spec.h', 'usr/include/freeipmi/spec/ipmi-channel-spec.h', 'usr/include/freeipmi/spec/ipmi-cmd-dcmi-spec.h', 'usr/include/freeipmi/spec/ipmi-cmd-spec.h', 'usr/include/freeipmi/spec/ipmi-comp-code-dcmi-spec.h', 'usr/include/freeipmi/spec/ipmi-comp-code-oem-spec.h', 'usr/include/freeipmi/spec/ipmi-comp-code-spec.h', 'usr/include/freeipmi/spec/ipmi-device-types-oem-spec.h', 'usr/include/freeipmi/spec/ipmi-device-types-spec.h', 'usr/include/freeipmi/spec/ipmi-entity-ids-spec.h', 'usr/include/freeipmi/spec/ipmi-event-reading-type-code-oem-spec.h', 'usr/include/freeipmi/spec/ipmi-event-reading-type-code-spec.h', 'usr/include/freeipmi/spec/ipmi-fru-chassis-types-spec.h', 'usr/include/freeipmi/spec/ipmi-fru-language-codes-spec.h', 'usr/include/freeipmi/spec/ipmi-iana-enterprise-numbers-spec.h', 'usr/include/freeipmi/spec/ipmi-ipmb-lun-spec.h', 'usr/include/freeipmi/spec/ipmi-jedec-manufacturer-identification-code-spec.h', 'usr/include/freeipmi/spec/ipmi-lan-configuration-parameters-oem-spec.h', 'usr/include/freeipmi/spec/ipmi-lan-configuration-parameters-spec.h', 'usr/include/freeipmi/spec/ipmi-netfn-oem-spec.h', 'usr/include/freeipmi/spec/ipmi-netfn-spec.h', 'usr/include/freeipmi/spec/ipmi-oem-spec.h', 'usr/include/freeipmi/spec/ipmi-pef-configuration-parameters-oem-spec.h', 'usr/include/freeipmi/spec/ipmi-pef-configuration-parameters-spec.h', 'usr/include/freeipmi/spec/ipmi-privilege-level-spec.h', 'usr/include/freeipmi/spec/ipmi-product-id-spec.h', 'usr/include/freeipmi/spec/ipmi-rmcpplus-status-spec.h', 'usr/include/freeipmi/spec/ipmi-sensor-and-event-code-tables-oem-spec.h', 'usr/include/freeipmi/spec/ipmi-sensor-and-event-code-tables-spec.h', 'usr/include/freeipmi/spec/ipmi-sensor-numbers-oem-spec.h', 'usr/include/freeipmi/spec/ipmi-sensor-types-oem-spec.h', 'usr/include/freeipmi/spec/ipmi-sensor-types-spec.h', 'usr/include/freeipmi/spec/ipmi-sensor-units-spec.h', 'usr/include/freeipmi/spec/ipmi-serial-modem-configuration-parameters-oem-spec.h', 'usr/include/freeipmi/spec/ipmi-serial-modem-configuration-parameters-spec.h', 'usr/include/freeipmi/spec/ipmi-slave-address-oem-spec.h', 'usr/include/freeipmi/spec/ipmi-slave-address-spec.h', 'usr/include/freeipmi/spec/ipmi-sol-configuration-parameters-oem-spec.h', 'usr/include/freeipmi/spec/ipmi-sol-configuration-parameters-spec.h', 'usr/include/freeipmi/spec/ipmi-system-boot-option-parameters-oem-spec.h', 'usr/include/freeipmi/spec/ipmi-system-boot-option-parameters-spec.h', 'usr/include/freeipmi/spec/ipmi-system-info-parameters-oem-spec.h', 'usr/include/freeipmi/spec/ipmi-system-info-parameters-spec.h', 'usr/include/freeipmi/spec/ipmi-system-software-id-spec.h', 'usr/include/freeipmi/spec/ipmi-timestamp-spec.h', 'usr/include/freeipmi/spec/oem/', 'usr/include/freeipmi/spec/oem/ipmi-cmd-oem-dell-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-cmd-oem-fujitsu-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-cmd-oem-gigabyte-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-cmd-oem-ibm-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-cmd-oem-intel-node-manager-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-cmd-oem-intel-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-cmd-oem-inventec-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-cmd-oem-quanta-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-cmd-oem-sun-microsystems-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-cmd-oem-supermicro-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-cmd-oem-wistron-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-comp-code-oem-dell-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-comp-code-oem-fujitsu-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-comp-code-oem-intel-node-manager-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-comp-code-oem-intel-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-comp-code-oem-wistron-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-event-reading-type-code-oem-dell-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-event-reading-type-code-oem-hp-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-event-reading-type-code-oem-intel-node-manager-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-event-reading-type-code-oem-intel-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-event-reading-type-code-oem-inventec-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-event-reading-type-code-oem-supermicro-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-lan-configuration-parameters-oem-inventec-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-lan-configuration-parameters-oem-wistron-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-netfn-oem-dell-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-netfn-oem-fujitsu-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-netfn-oem-ibm-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-netfn-oem-intel-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-netfn-oem-inventec-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-netfn-oem-quanta-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-netfn-oem-supermicro-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-netfn-oem-wistron-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-oem-dell-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-oem-fujitsu-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-oem-gigabyte-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-oem-ibm-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-oem-intel-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-oem-inventec-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-oem-quanta-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-oem-sun-microsystems-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-oem-supermicro-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-oem-wistron-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-dell-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-fujitsu-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-gigabyte-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-hp-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-intel-node-manager-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-intel-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-inventec-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-quanta-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-supermicro-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-wistron-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-numbers-oem-dell-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-numbers-oem-intel-node-manager-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-numbers-oem-intel-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-numbers-oem-inventec-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-numbers-oem-quanta-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-numbers-oem-wistron-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-types-oem-dell-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-types-oem-fujitsu-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-types-oem-hp-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-types-oem-intel-node-manager-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-types-oem-intel-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-types-oem-inventec-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-types-oem-supermicro-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sensor-types-oem-wistron-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-slave-address-oem-intel-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-slave-address-oem-inventec-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-slave-address-oem-linux-kernel-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-slave-address-oem-quanta-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-slave-address-oem-wistron-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sol-configuration-parameters-oem-inventec-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-sol-configuration-parameters-oem-wistron-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-system-info-parameters-oem-dell-spec.h', 'usr/include/freeipmi/spec/oem/ipmi-system-info-parameters-oem-wistron-spec.h', 'usr/include/freeipmi/templates/', 'usr/include/freeipmi/templates/ipmi-bmc-watchdog-timer-cmds-templates.h', 'usr/include/freeipmi/templates/ipmi-chassis-cmds-templates.h', 'usr/include/freeipmi/templates/ipmi-cipher-suite-record-format-templates.h', 'usr/include/freeipmi/templates/ipmi-dcmi-cmds-templates.h', 'usr/include/freeipmi/templates/ipmi-device-global-cmds-templates.h', 'usr/include/freeipmi/templates/ipmi-event-cmds-templates.h', 'usr/include/freeipmi/templates/ipmi-firmware-firewall-command-discovery-cmds-templates.h', 'usr/include/freeipmi/templates/ipmi-fru-dimmspd-record-format-templates.h', 'usr/include/freeipmi/templates/ipmi-fru-information-record-format-templates.h', 'usr/include/freeipmi/templates/ipmi-fru-inventory-device-cmds-templates.h', 'usr/include/freeipmi/templates/ipmi-ipmb-interface-templates.h', 'usr/include/freeipmi/templates/ipmi-kcs-interface-templates.h', 'usr/include/freeipmi/templates/ipmi-lan-cmds-templates.h', 'usr/include/freeipmi/templates/ipmi-lan-interface-templates.h', 'usr/include/freeipmi/templates/ipmi-messaging-support-cmds-templates.h', 'usr/include/freeipmi/templates/ipmi-oem-intel-node-manager-cmds-templates.h', 'usr/include/freeipmi/templates/ipmi-pef-and-alerting-cmds-templates.h', 'usr/include/freeipmi/templates/ipmi-rmcpplus-interface-templates.h', 'usr/include/freeipmi/templates/ipmi-rmcpplus-support-and-payload-cmds-templates.h', 'usr/include/freeipmi/templates/ipmi-sdr-record-format-templates.h', 'usr/include/freeipmi/templates/ipmi-sdr-repository-cmds-templates.h', 'usr/include/freeipmi/templates/ipmi-sel-cmds-templates.h', 'usr/include/freeipmi/templates/ipmi-sel-record-format-templates.h', 'usr/include/freeipmi/templates/ipmi-sensor-cmds-templates.h', 'usr/include/freeipmi/templates/ipmi-serial-modem-cmds-templates.h', 'usr/include/freeipmi/templates/ipmi-sol-cmds-templates.h', 'usr/include/freeipmi/templates/ipmi-sol-payload-templates.h', 'usr/include/freeipmi/templates/oem/', 'usr/include/freeipmi/templates/oem/ipmi-sdr-oem-intel-node-manager-record-format-templates.h', 'usr/include/freeipmi/templates/rmcp-cmds-templates.h', 'usr/include/freeipmi/templates/rmcp-interface-templates.h', 'usr/include/freeipmi/util/', 'usr/include/freeipmi/util/ipmi-channel-util.h', 'usr/include/freeipmi/util/ipmi-cipher-suite-util.h', 'usr/include/freeipmi/util/ipmi-dcmi-util.h', 'usr/include/freeipmi/util/ipmi-device-types-util.h', 'usr/include/freeipmi/util/ipmi-entity-ids-util.h', 'usr/include/freeipmi/util/ipmi-error-dcmi-util.h', 'usr/include/freeipmi/util/ipmi-error-util.h', 'usr/include/freeipmi/util/ipmi-iana-enterprise-numbers-util.h', 'usr/include/freeipmi/util/ipmi-ipmb-util.h', 'usr/include/freeipmi/util/ipmi-jedec-manufacturer-identification-code-util.h', 'usr/include/freeipmi/util/ipmi-lan-util.h', 'usr/include/freeipmi/util/ipmi-outofband-util.h', 'usr/include/freeipmi/util/ipmi-rmcpplus-util.h', 'usr/include/freeipmi/util/ipmi-sensor-and-event-code-tables-util.h', 'usr/include/freeipmi/util/ipmi-sensor-util.h', 'usr/include/freeipmi/util/ipmi-timestamp-util.h', 'usr/include/freeipmi/util/ipmi-util.h', 'usr/include/freeipmi/util/rmcp-util.h', 'usr/include/ipmi_monitoring.h', 'usr/include/ipmi_monitoring_bitmasks.h', 'usr/include/ipmi_monitoring_offsets.h', 'usr/include/ipmiconsole.h', 'usr/include/ipmidetect.h', 'usr/lib/', 'usr/lib/libfreeipmi.so', 'usr/lib/libfreeipmi.so.17', 'usr/lib/libfreeipmi.so.17.2.9', 'usr/lib/libipmiconsole.so', 'usr/lib/libipmiconsole.so.2', 'usr/lib/libipmiconsole.so.2.3.6', 'usr/lib/libipmidetect.so', 'usr/lib/libipmidetect.so.0', 'usr/lib/libipmidetect.so.0.0.1', 'usr/lib/libipmimonitoring.so', 'usr/lib/libipmimonitoring.so.6', 'usr/lib/libipmimonitoring.so.6.0.8', 'usr/lib/pkgconfig/', 'usr/lib/pkgconfig/libfreeipmi.pc', 'usr/lib/pkgconfig/libipmiconsole.pc', 'usr/lib/pkgconfig/libipmidetect.pc', 'usr/lib/pkgconfig/libipmimonitoring.pc', 'usr/sbin/', 'usr/sbin/bmc-config', 'usr/sbin/bmc-device', 'usr/sbin/bmc-info', 'usr/sbin/bmc-watchdog', 'usr/sbin/ipmi-chassis', 'usr/sbin/ipmi-chassis-config', 'usr/sbin/ipmi-config', 'usr/sbin/ipmi-console', 'usr/sbin/ipmi-dcmi', 'usr/sbin/ipmi-detect', 'usr/sbin/ipmi-fru', 'usr/sbin/ipmi-locate', 'usr/sbin/ipmi-oem', 'usr/sbin/ipmi-pef-config', 'usr/sbin/ipmi-pet', 'usr/sbin/ipmi-ping', 'usr/sbin/ipmi-power', 'usr/sbin/ipmi-raw', 'usr/sbin/ipmi-sel', 'usr/sbin/ipmi-sensors', 'usr/sbin/ipmi-sensors-config', 'usr/sbin/ipmiconsole', 'usr/sbin/ipmidetect', 'usr/sbin/ipmidetectd', 'usr/sbin/ipmimonitoring', 'usr/sbin/ipmiping', 'usr/sbin/ipmipower', 'usr/sbin/ipmiseld', 'usr/sbin/pef-config', 'usr/sbin/rmcp-ping', 'usr/sbin/rmcpping', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/freeipmi-1.6.10/', 'usr/share/doc/freeipmi-1.6.10/AUTHORS', 'usr/share/doc/freeipmi-1.6.10/COPYING', 'usr/share/doc/freeipmi-1.6.10/COPYING.ZRESEARCH', 'usr/share/doc/freeipmi-1.6.10/COPYING.bmc-watchdog', 'usr/share/doc/freeipmi-1.6.10/COPYING.ipmi-dcmi', 'usr/share/doc/freeipmi-1.6.10/COPYING.ipmi-fru', 'usr/share/doc/freeipmi-1.6.10/COPYING.ipmiconsole', 'usr/share/doc/freeipmi-1.6.10/COPYING.ipmidetect', 'usr/share/doc/freeipmi-1.6.10/COPYING.ipmimonitoring', 'usr/share/doc/freeipmi-1.6.10/COPYING.ipmiping', 'usr/share/doc/freeipmi-1.6.10/COPYING.ipmipower', 'usr/share/doc/freeipmi-1.6.10/COPYING.ipmiseld', 'usr/share/doc/freeipmi-1.6.10/COPYING.pstdout', 'usr/share/doc/freeipmi-1.6.10/COPYING.sunbmc', 'usr/share/doc/freeipmi-1.6.10/ChangeLog', 'usr/share/doc/freeipmi-1.6.10/ChangeLog.0', 'usr/share/doc/freeipmi-1.6.10/DISCLAIMER.bmc-watchdog', 'usr/share/doc/freeipmi-1.6.10/DISCLAIMER.bmc-watchdog.UC', 'usr/share/doc/freeipmi-1.6.10/DISCLAIMER.ipmi-dcmi', 'usr/share/doc/freeipmi-1.6.10/DISCLAIMER.ipmi-fru', 'usr/share/doc/freeipmi-1.6.10/DISCLAIMER.ipmi-fru.UC', 'usr/share/doc/freeipmi-1.6.10/DISCLAIMER.ipmiconsole', 'usr/share/doc/freeipmi-1.6.10/DISCLAIMER.ipmiconsole.UC', 'usr/share/doc/freeipmi-1.6.10/DISCLAIMER.ipmidetect', 'usr/share/doc/freeipmi-1.6.10/DISCLAIMER.ipmidetect.UC', 'usr/share/doc/freeipmi-1.6.10/DISCLAIMER.ipmimonitoring', 'usr/share/doc/freeipmi-1.6.10/DISCLAIMER.ipmimonitoring.UC', 'usr/share/doc/freeipmi-1.6.10/DISCLAIMER.ipmiping', 'usr/share/doc/freeipmi-1.6.10/DISCLAIMER.ipmiping.UC', 'usr/share/doc/freeipmi-1.6.10/DISCLAIMER.ipmipower', 'usr/share/doc/freeipmi-1.6.10/DISCLAIMER.ipmipower.UC', 'usr/share/doc/freeipmi-1.6.10/DISCLAIMER.ipmiseld', 'usr/share/doc/freeipmi-1.6.10/DISCLAIMER.pstdout', 'usr/share/doc/freeipmi-1.6.10/DISCLAIMER.pstdout.UC', 'usr/share/doc/freeipmi-1.6.10/INSTALL', 'usr/share/doc/freeipmi-1.6.10/NEWS', 'usr/share/doc/freeipmi-1.6.10/README', 'usr/share/doc/freeipmi-1.6.10/README.argp', 'usr/share/doc/freeipmi-1.6.10/README.build', 'usr/share/doc/freeipmi-1.6.10/README.openipmi', 'usr/share/doc/freeipmi-1.6.10/TODO', 'usr/share/doc/freeipmi-1.6.10/contrib/', 'usr/share/doc/freeipmi-1.6.10/contrib/ganglia/', 'usr/share/doc/freeipmi-1.6.10/contrib/ganglia/README', 'usr/share/doc/freeipmi-1.6.10/contrib/ganglia/ganglia_ipmi_sensors.pl', 'usr/share/doc/freeipmi-1.6.10/contrib/libipmimonitoring/', 'usr/share/doc/freeipmi-1.6.10/contrib/libipmimonitoring/ipmimonitoring-sel.c', 'usr/share/doc/freeipmi-1.6.10/contrib/libipmimonitoring/ipmimonitoring-sensors.c', 'usr/share/doc/freeipmi-1.6.10/contrib/nagios/', 'usr/share/doc/freeipmi-1.6.10/contrib/nagios/README', 'usr/share/doc/freeipmi-1.6.10/contrib/nagios/nagios_ipmi_sensors.pl', 'usr/share/doc/freeipmi-1.6.10/contrib/pet/', 'usr/share/doc/freeipmi-1.6.10/contrib/pet/README', 'usr/share/doc/freeipmi-1.6.10/contrib/pet/check_rmcpping', 'usr/share/doc/freeipmi-1.6.10/contrib/pet/ipminodes.cfg', 'usr/share/doc/freeipmi-1.6.10/contrib/pet/petalert.pl', 'usr/share/doc/freeipmi-1.6.10/freeipmi-bugs-issues-and-workarounds.txt', 'usr/share/doc/freeipmi-1.6.10/freeipmi-coding.txt', 'usr/share/doc/freeipmi-1.6.10/freeipmi-design.txt', 'usr/share/doc/freeipmi-1.6.10/freeipmi-hostrange.txt', 'usr/share/doc/freeipmi-1.6.10/freeipmi-libraries.txt', 'usr/share/doc/freeipmi-1.6.10/freeipmi-oem-documentation-requirements.txt', 'usr/share/doc/freeipmi-1.6.10/freeipmi-testing.txt', 'usr/share/info/', 'usr/share/info/freeipmi-faq.info.gz', 'usr/share/man/', 'usr/share/man/man3/', 'usr/share/man/man3/libfreeipmi.3.gz', 'usr/share/man/man3/libipmiconsole.3.gz', 'usr/share/man/man3/libipmidetect.3.gz', 'usr/share/man/man3/libipmimonitoring.3.gz', 'usr/share/man/man5/', 'usr/share/man/man5/bmc-config.conf.5.gz', 'usr/share/man/man5/freeipmi.conf.5.gz', 'usr/share/man/man5/freeipmi_interpret_sel.conf.5.gz', 'usr/share/man/man5/freeipmi_interpret_sensor.conf.5.gz', 'usr/share/man/man5/ipmi-config.conf.5.gz', 'usr/share/man/man5/ipmi_monitoring_sensors.conf.5.gz', 'usr/share/man/man5/ipmiconsole.conf.5.gz', 'usr/share/man/man5/ipmidetect.conf.5.gz', 'usr/share/man/man5/ipmidetectd.conf.5.gz', 'usr/share/man/man5/ipmimonitoring.conf.5.gz', 'usr/share/man/man5/ipmimonitoring_sensors.conf.5.gz', 'usr/share/man/man5/ipmipower.conf.5.gz', 'usr/share/man/man5/ipmiseld.conf.5.gz', 'usr/share/man/man5/libipmiconsole.conf.5.gz', 'usr/share/man/man5/libipmimonitoring.conf.5.gz', 'usr/share/man/man7/', 'usr/share/man/man7/freeipmi.7.gz', 'usr/share/man/man8/', 'usr/share/man/man8/bmc-config.8.gz', 'usr/share/man/man8/bmc-device.8.gz', 'usr/share/man/man8/bmc-info.8.gz', 'usr/share/man/man8/bmc-watchdog.8.gz', 'usr/share/man/man8/ipmi-chassis-config.8.gz', 'usr/share/man/man8/ipmi-chassis.8.gz', 'usr/share/man/man8/ipmi-config.8.gz', 'usr/share/man/man8/ipmi-console.8.gz', 'usr/share/man/man8/ipmi-dcmi.8.gz', 'usr/share/man/man8/ipmi-detect.8.gz', 'usr/share/man/man8/ipmi-fru.8.gz', 'usr/share/man/man8/ipmi-locate.8.gz', 'usr/share/man/man8/ipmi-oem.8.gz', 'usr/share/man/man8/ipmi-pef-config.8.gz', 'usr/share/man/man8/ipmi-pet.8.gz', 'usr/share/man/man8/ipmi-ping.8.gz', 'usr/share/man/man8/ipmi-power.8.gz', 'usr/share/man/man8/ipmi-raw.8.gz', 'usr/share/man/man8/ipmi-sel.8.gz', 'usr/share/man/man8/ipmi-sensors-config.8.gz', 'usr/share/man/man8/ipmi-sensors.8.gz', 'usr/share/man/man8/ipmiconsole.8.gz', 'usr/share/man/man8/ipmidetect.8.gz', 'usr/share/man/man8/ipmidetectd.8.gz', 'usr/share/man/man8/ipmimonitoring.8.gz', 'usr/share/man/man8/ipmiping.8.gz', 'usr/share/man/man8/ipmipower.8.gz', 'usr/share/man/man8/ipmiseld.8.gz', 'usr/share/man/man8/pef-config.8.gz', 'usr/share/man/man8/rmcp-ping.8.gz', 'usr/share/man/man8/rmcpping.8.gz', 'var/', 'var/cache/', 'var/cache/ipmimonitoringsdrcache/', 'var/cache/ipmiseld/', 'var/lib/', 'var/lib/freeipmi/', 'var/lib/freeipmi/ipckey']"
+++
GNU Intelligent Platform Management Interface implementation.