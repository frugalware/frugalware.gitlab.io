+++
draft = false
title = "modemmanager 1.18.12-2"
version = "1.18.12-2"
date = "2023-09-04T14:21:56"
categories = ['base']
upstreamurl = "http://www.freedesktop.org/wiki/Software/ModemManager/"
arch = "x86_64"
size = "9081949"
usize = "0"
sha1sum = ""
depends = "['ppp>=2.4.7', 'libgudev>=231-2', 'elfutils>=0.167-2', 'libsystemd>=242']"
files = "['etc/', 'etc/ModemManager/', 'etc/ModemManager/connection.d/', 'etc/ModemManager/fcc-unlock.d/', 'etc/dbus-1/', 'etc/dbus-1/system.d/', 'etc/dbus-1/system.d/org.freedesktop.ModemManager1.conf', 'lib/', 'lib/systemd/', 'lib/systemd/system/', 'lib/systemd/system/ModemManager.service', 'lib/udev/', 'lib/udev/rules.d/', 'lib/udev/rules.d/77-mm-broadmobi-port-types.rules', 'lib/udev/rules.d/77-mm-cinterion-port-types.rules', 'lib/udev/rules.d/77-mm-dell-port-types.rules', 'lib/udev/rules.d/77-mm-dlink-port-types.rules', 'lib/udev/rules.d/77-mm-ericsson-mbm.rules', 'lib/udev/rules.d/77-mm-fibocom-port-types.rules', 'lib/udev/rules.d/77-mm-foxconn-port-types.rules', 'lib/udev/rules.d/77-mm-gosuncn-port-types.rules', 'lib/udev/rules.d/77-mm-haier-port-types.rules', 'lib/udev/rules.d/77-mm-huawei-net-port-types.rules', 'lib/udev/rules.d/77-mm-linktop-port-types.rules', 'lib/udev/rules.d/77-mm-longcheer-port-types.rules', 'lib/udev/rules.d/77-mm-mtk-port-types.rules', 'lib/udev/rules.d/77-mm-nokia-port-types.rules', 'lib/udev/rules.d/77-mm-quectel-port-types.rules', 'lib/udev/rules.d/77-mm-sierra.rules', 'lib/udev/rules.d/77-mm-simtech-port-types.rules', 'lib/udev/rules.d/77-mm-telit-port-types.rules', 'lib/udev/rules.d/77-mm-tplink-port-types.rules', 'lib/udev/rules.d/77-mm-ublox-port-types.rules', 'lib/udev/rules.d/77-mm-x22x-port-types.rules', 'lib/udev/rules.d/77-mm-zte-port-types.rules', 'lib/udev/rules.d/80-mm-candidate.rules', 'usr/', 'usr/bin/', 'usr/bin/mmcli', 'usr/include/', 'usr/include/ModemManager/', 'usr/include/ModemManager/ModemManager-compat.h', 'usr/include/ModemManager/ModemManager-enums.h', 'usr/include/ModemManager/ModemManager-errors.h', 'usr/include/ModemManager/ModemManager-names.h', 'usr/include/ModemManager/ModemManager-version.h', 'usr/include/ModemManager/ModemManager.h', 'usr/include/libmm-glib/', 'usr/include/libmm-glib/libmm-glib.h', 'usr/include/libmm-glib/mm-3gpp-profile.h', 'usr/include/libmm-glib/mm-bearer-ip-config.h', 'usr/include/libmm-glib/mm-bearer-properties.h', 'usr/include/libmm-glib/mm-bearer-stats.h', 'usr/include/libmm-glib/mm-bearer.h', 'usr/include/libmm-glib/mm-call-audio-format.h', 'usr/include/libmm-glib/mm-call-properties.h', 'usr/include/libmm-glib/mm-call.h', 'usr/include/libmm-glib/mm-cdma-manual-activation-properties.h', 'usr/include/libmm-glib/mm-compat.h', 'usr/include/libmm-glib/mm-enums-types.h', 'usr/include/libmm-glib/mm-errors-types.h', 'usr/include/libmm-glib/mm-firmware-properties.h', 'usr/include/libmm-glib/mm-firmware-update-settings.h', 'usr/include/libmm-glib/mm-gdbus-bearer.h', 'usr/include/libmm-glib/mm-gdbus-call.h', 'usr/include/libmm-glib/mm-gdbus-manager.h', 'usr/include/libmm-glib/mm-gdbus-modem.h', 'usr/include/libmm-glib/mm-gdbus-sim.h', 'usr/include/libmm-glib/mm-gdbus-sms.h', 'usr/include/libmm-glib/mm-helper-types.h', 'usr/include/libmm-glib/mm-kernel-event-properties.h', 'usr/include/libmm-glib/mm-location-3gpp.h', 'usr/include/libmm-glib/mm-location-cdma-bs.h', 'usr/include/libmm-glib/mm-location-common.h', 'usr/include/libmm-glib/mm-location-gps-nmea.h', 'usr/include/libmm-glib/mm-location-gps-raw.h', 'usr/include/libmm-glib/mm-manager.h', 'usr/include/libmm-glib/mm-modem-3gpp-profile-manager.h', 'usr/include/libmm-glib/mm-modem-3gpp-ussd.h', 'usr/include/libmm-glib/mm-modem-3gpp.h', 'usr/include/libmm-glib/mm-modem-cdma.h', 'usr/include/libmm-glib/mm-modem-firmware.h', 'usr/include/libmm-glib/mm-modem-location.h', 'usr/include/libmm-glib/mm-modem-messaging.h', 'usr/include/libmm-glib/mm-modem-oma.h', 'usr/include/libmm-glib/mm-modem-signal.h', 'usr/include/libmm-glib/mm-modem-simple.h', 'usr/include/libmm-glib/mm-modem-time.h', 'usr/include/libmm-glib/mm-modem-voice.h', 'usr/include/libmm-glib/mm-modem.h', 'usr/include/libmm-glib/mm-network-timezone.h', 'usr/include/libmm-glib/mm-object.h', 'usr/include/libmm-glib/mm-pco.h', 'usr/include/libmm-glib/mm-signal.h', 'usr/include/libmm-glib/mm-sim-preferred-network.h', 'usr/include/libmm-glib/mm-sim.h', 'usr/include/libmm-glib/mm-simple-connect-properties.h', 'usr/include/libmm-glib/mm-simple-status.h', 'usr/include/libmm-glib/mm-sms-properties.h', 'usr/include/libmm-glib/mm-sms.h', 'usr/include/libmm-glib/mm-unlock-retries.h', 'usr/lib/', 'usr/lib/ModemManager/', 'usr/lib/ModemManager/connection.d/', 'usr/lib/ModemManager/fcc-unlock.d/', 'usr/lib/ModemManager/libmm-plugin-altair-lte.so', 'usr/lib/ModemManager/libmm-plugin-anydata.so', 'usr/lib/ModemManager/libmm-plugin-broadmobi.so', 'usr/lib/ModemManager/libmm-plugin-cinterion.so', 'usr/lib/ModemManager/libmm-plugin-dell.so', 'usr/lib/ModemManager/libmm-plugin-dlink.so', 'usr/lib/ModemManager/libmm-plugin-ericsson-mbm.so', 'usr/lib/ModemManager/libmm-plugin-fibocom.so', 'usr/lib/ModemManager/libmm-plugin-foxconn.so', 'usr/lib/ModemManager/libmm-plugin-generic.so', 'usr/lib/ModemManager/libmm-plugin-gosuncn.so', 'usr/lib/ModemManager/libmm-plugin-haier.so', 'usr/lib/ModemManager/libmm-plugin-huawei.so', 'usr/lib/ModemManager/libmm-plugin-iridium.so', 'usr/lib/ModemManager/libmm-plugin-linktop.so', 'usr/lib/ModemManager/libmm-plugin-longcheer.so', 'usr/lib/ModemManager/libmm-plugin-motorola.so', 'usr/lib/ModemManager/libmm-plugin-mtk.so', 'usr/lib/ModemManager/libmm-plugin-nokia-icera.so', 'usr/lib/ModemManager/libmm-plugin-nokia.so', 'usr/lib/ModemManager/libmm-plugin-novatel-lte.so', 'usr/lib/ModemManager/libmm-plugin-novatel.so', 'usr/lib/ModemManager/libmm-plugin-option-hso.so', 'usr/lib/ModemManager/libmm-plugin-option.so', 'usr/lib/ModemManager/libmm-plugin-pantech.so', 'usr/lib/ModemManager/libmm-plugin-quectel.so', 'usr/lib/ModemManager/libmm-plugin-samsung.so', 'usr/lib/ModemManager/libmm-plugin-sierra-legacy.so', 'usr/lib/ModemManager/libmm-plugin-sierra.so', 'usr/lib/ModemManager/libmm-plugin-simtech.so', 'usr/lib/ModemManager/libmm-plugin-telit.so', 'usr/lib/ModemManager/libmm-plugin-thuraya.so', 'usr/lib/ModemManager/libmm-plugin-tplink.so', 'usr/lib/ModemManager/libmm-plugin-ublox.so', 'usr/lib/ModemManager/libmm-plugin-via.so', 'usr/lib/ModemManager/libmm-plugin-wavecom.so', 'usr/lib/ModemManager/libmm-plugin-x22x.so', 'usr/lib/ModemManager/libmm-plugin-zte.so', 'usr/lib/ModemManager/libmm-shared-icera.so', 'usr/lib/ModemManager/libmm-shared-novatel.so', 'usr/lib/ModemManager/libmm-shared-option.so', 'usr/lib/ModemManager/libmm-shared-sierra.so', 'usr/lib/ModemManager/libmm-shared-telit.so', 'usr/lib/ModemManager/libmm-shared-xmm.so', 'usr/lib/libmm-glib.so', 'usr/lib/libmm-glib.so.0', 'usr/lib/libmm-glib.so.0.8.0', 'usr/lib/pkgconfig/', 'usr/lib/pkgconfig/ModemManager.pc', 'usr/lib/pkgconfig/mm-glib.pc', 'usr/sbin/', 'usr/sbin/ModemManager', 'usr/share/', 'usr/share/ModemManager/', 'usr/share/ModemManager/connection.available.d/', 'usr/share/ModemManager/connection.available.d/99-log-event', 'usr/share/ModemManager/fcc-unlock.available.d/', 'usr/share/ModemManager/fcc-unlock.available.d/03f0:4e1d', 'usr/share/ModemManager/fcc-unlock.available.d/105b', 'usr/share/ModemManager/fcc-unlock.available.d/105b:e0ab', 'usr/share/ModemManager/fcc-unlock.available.d/1199', 'usr/share/ModemManager/fcc-unlock.available.d/1199:9079', 'usr/share/ModemManager/fcc-unlock.available.d/1eac', 'usr/share/ModemManager/fcc-unlock.available.d/1eac:1001', 'usr/share/ModemManager/fcc-unlock.available.d/413c:81a3', 'usr/share/ModemManager/fcc-unlock.available.d/413c:81a8', 'usr/share/ModemManager/mm-foxconn-t77w968-carrier-mapping.conf', 'usr/share/bash-completion/', 'usr/share/bash-completion/completions/', 'usr/share/bash-completion/completions/mmcli', 'usr/share/dbus-1/', 'usr/share/dbus-1/interfaces/', 'usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Bearer.xml', 'usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Call.xml', 'usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Firmware.xml', 'usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Location.xml', 'usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Messaging.xml', 'usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Modem3gpp.ProfileManager.xml', 'usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Modem3gpp.Ussd.xml', 'usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Modem3gpp.xml', 'usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.ModemCdma.xml', 'usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Oma.xml', 'usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Signal.xml', 'usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Simple.xml', 'usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Time.xml', 'usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.Voice.xml', 'usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Modem.xml', 'usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Sim.xml', 'usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.Sms.xml', 'usr/share/dbus-1/interfaces/org.freedesktop.ModemManager1.xml', 'usr/share/dbus-1/system-services/', 'usr/share/dbus-1/system-services/org.freedesktop.ModemManager1.service', 'usr/share/doc/', 'usr/share/doc/modemmanager-1.18.12/', 'usr/share/doc/modemmanager-1.18.12/AUTHORS', 'usr/share/doc/modemmanager-1.18.12/COPYING', 'usr/share/doc/modemmanager-1.18.12/COPYING.LIB', 'usr/share/doc/modemmanager-1.18.12/ChangeLog', 'usr/share/doc/modemmanager-1.18.12/INSTALL', 'usr/share/doc/modemmanager-1.18.12/NEWS', 'usr/share/doc/modemmanager-1.18.12/README', 'usr/share/doc/modemmanager-1.18.12/TODO', 'usr/share/icons/', 'usr/share/icons/hicolor/', 'usr/share/icons/hicolor/22x22/', 'usr/share/icons/hicolor/22x22/apps/', 'usr/share/icons/hicolor/22x22/apps/ModemManager.png', 'usr/share/locale/', 'usr/share/locale/cs/', 'usr/share/locale/cs/LC_MESSAGES/', 'usr/share/locale/cs/LC_MESSAGES/ModemManager.mo', 'usr/share/locale/da/', 'usr/share/locale/da/LC_MESSAGES/', 'usr/share/locale/da/LC_MESSAGES/ModemManager.mo', 'usr/share/locale/de/', 'usr/share/locale/de/LC_MESSAGES/', 'usr/share/locale/de/LC_MESSAGES/ModemManager.mo', 'usr/share/locale/fi/', 'usr/share/locale/fi/LC_MESSAGES/', 'usr/share/locale/fi/LC_MESSAGES/ModemManager.mo', 'usr/share/locale/fr/', 'usr/share/locale/fr/LC_MESSAGES/', 'usr/share/locale/fr/LC_MESSAGES/ModemManager.mo', 'usr/share/locale/fur/', 'usr/share/locale/fur/LC_MESSAGES/', 'usr/share/locale/fur/LC_MESSAGES/ModemManager.mo', 'usr/share/locale/he/', 'usr/share/locale/he/LC_MESSAGES/', 'usr/share/locale/he/LC_MESSAGES/ModemManager.mo', 'usr/share/locale/hu/', 'usr/share/locale/hu/LC_MESSAGES/', 'usr/share/locale/hu/LC_MESSAGES/ModemManager.mo', 'usr/share/locale/id/', 'usr/share/locale/id/LC_MESSAGES/', 'usr/share/locale/id/LC_MESSAGES/ModemManager.mo', 'usr/share/locale/it/', 'usr/share/locale/it/LC_MESSAGES/', 'usr/share/locale/it/LC_MESSAGES/ModemManager.mo', 'usr/share/locale/lt/', 'usr/share/locale/lt/LC_MESSAGES/', 'usr/share/locale/lt/LC_MESSAGES/ModemManager.mo', 'usr/share/locale/pl/', 'usr/share/locale/pl/LC_MESSAGES/', 'usr/share/locale/pl/LC_MESSAGES/ModemManager.mo', 'usr/share/locale/pt_BR/', 'usr/share/locale/pt_BR/LC_MESSAGES/', 'usr/share/locale/pt_BR/LC_MESSAGES/ModemManager.mo', 'usr/share/locale/ru/', 'usr/share/locale/ru/LC_MESSAGES/', 'usr/share/locale/ru/LC_MESSAGES/ModemManager.mo', 'usr/share/locale/sk/', 'usr/share/locale/sk/LC_MESSAGES/', 'usr/share/locale/sk/LC_MESSAGES/ModemManager.mo', 'usr/share/locale/sv/', 'usr/share/locale/sv/LC_MESSAGES/', 'usr/share/locale/sv/LC_MESSAGES/ModemManager.mo', 'usr/share/locale/tr/', 'usr/share/locale/tr/LC_MESSAGES/', 'usr/share/locale/tr/LC_MESSAGES/ModemManager.mo', 'usr/share/locale/uk/', 'usr/share/locale/uk/LC_MESSAGES/', 'usr/share/locale/uk/LC_MESSAGES/ModemManager.mo', 'usr/share/locale/zh_CN/', 'usr/share/locale/zh_CN/LC_MESSAGES/', 'usr/share/locale/zh_CN/LC_MESSAGES/ModemManager.mo', 'usr/share/man/', 'usr/share/man/man1/', 'usr/share/man/man1/mmcli.1.gz', 'usr/share/man/man8/', 'usr/share/man/man8/ModemManager.8.gz']"
+++
Mobile broadband modem management service