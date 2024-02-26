+++
draft = false
title = "lib32-v4l-utils 1.26.1-3"
version = "1.26.1-3"
description = "v4l-utils (32-bit)"
date = "2024-01-05T11:23:17"
aliases = "/packages/219239"
categories = ['lib32-extra']
upstreamurl = "http://linuxtv.org"
arch = "x86_64"
size = "1054736"
usize = "4143094"
sha1sum = "1bb2c51e0804f688d5f1df7b401e76a5b57369d3"
depends = "['lib32-elfutils', 'lib32-json-c', 'lib32-libglu', 'lib32-libjpeg-turbo', 'lib32-libsystemd', 'lib32-libudev', 'lib32-libx11', 'lib32-sdl2', 'lib32-sdl2_image', 'v4l-utils>=1.26.1']"
reverse_depends = "['lib32-ffmpeg']"
+++
v4l-utils (32-bit)"

{{< files text="show files" >}}* /usr/i686-frugalware-linux/bin/cec-compliance
* /usr/i686-frugalware-linux/bin/cec-ctl
* /usr/i686-frugalware-linux/bin/cec-follower
* /usr/i686-frugalware-linux/bin/cx18-ctl
* /usr/i686-frugalware-linux/bin/decode_tm6000
* /usr/i686-frugalware-linux/bin/dvb-fe-tool
* /usr/i686-frugalware-linux/bin/dvb-format-convert
* /usr/i686-frugalware-linux/bin/dvbv5-daemon
* /usr/i686-frugalware-linux/bin/dvbv5-scan
* /usr/i686-frugalware-linux/bin/dvbv5-zap
* /usr/i686-frugalware-linux/bin/ir-ctl
* /usr/i686-frugalware-linux/bin/ir-keytable
* /usr/i686-frugalware-linux/bin/ivtv-ctl
* /usr/i686-frugalware-linux/bin/media-ctl
* /usr/i686-frugalware-linux/bin/rds-ctl
* /usr/i686-frugalware-linux/bin/v4l2-compliance
* /usr/i686-frugalware-linux/bin/v4l2-ctl
* /usr/i686-frugalware-linux/bin/v4l2-sysfs-path
* /usr/i686-frugalware-linux/bin/v4l2-tracer
* /usr/i686-frugalware-linux/include/libdvbv5/atsc_eit.h
* /usr/i686-frugalware-linux/include/libdvbv5/atsc_header.h
* /usr/i686-frugalware-linux/include/libdvbv5/cat.h
* /usr/i686-frugalware-linux/include/libdvbv5/countries.h
* /usr/i686-frugalware-linux/include/libdvbv5/crc32.h
* /usr/i686-frugalware-linux/include/libdvbv5/descriptors.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_atsc_service_location.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_ca.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_cable_delivery.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_ca_identifier.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_event_extended.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_event_short.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_extension.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_frequency_list.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_hierarchy.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_isdbt_delivery.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_language.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_logical_channel.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_network_name.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_partial_reception.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_registration_id.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_sat.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_service.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_t2_delivery.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_terrestrial_delivery.h
* /usr/i686-frugalware-linux/include/libdvbv5/desc_ts_info.h
* /usr/i686-frugalware-linux/include/libdvbv5/dvb-demux.h
* /usr/i686-frugalware-linux/include/libdvbv5/dvb-dev.h
* /usr/i686-frugalware-linux/include/libdvbv5/dvb-fe.h
* /usr/i686-frugalware-linux/include/libdvbv5/dvb-file.h
* /usr/i686-frugalware-linux/include/libdvbv5/dvb-frontend.h
* /usr/i686-frugalware-linux/include/libdvbv5/dvb-log.h
* /usr/i686-frugalware-linux/include/libdvbv5/dvb-sat.h
* /usr/i686-frugalware-linux/include/libdvbv5/dvb-scan.h
* /usr/i686-frugalware-linux/include/libdvbv5/dvb-v5-std.h
* /usr/i686-frugalware-linux/include/libdvbv5/eit.h
* /usr/i686-frugalware-linux/include/libdvbv5/header.h
* /usr/i686-frugalware-linux/include/libdvbv5/mgt.h
* /usr/i686-frugalware-linux/include/libdvbv5/mpeg_es.h
* /usr/i686-frugalware-linux/include/libdvbv5/mpeg_pes.h
* /usr/i686-frugalware-linux/include/libdvbv5/mpeg_ts.h
* /usr/i686-frugalware-linux/include/libdvbv5/nit.h
* /usr/i686-frugalware-linux/include/libdvbv5/pat.h
* /usr/i686-frugalware-linux/include/libdvbv5/pmt.h
* /usr/i686-frugalware-linux/include/libdvbv5/sdt.h
* /usr/i686-frugalware-linux/include/libdvbv5/vct.h
* /usr/i686-frugalware-linux/include/libv4l-plugin.h
* /usr/i686-frugalware-linux/include/libv4l1-videodev.h
* /usr/i686-frugalware-linux/include/libv4l1.h
* /usr/i686-frugalware-linux/include/libv4l2.h
* /usr/i686-frugalware-linux/include/libv4l2rds.h
* /usr/i686-frugalware-linux/include/libv4lconvert.h
* /usr/lib32/libdvbv5.so
* /usr/lib32/libdvbv5.so.0
* /usr/lib32/libdvbv5.so.0.0.0
* /usr/lib32/libv4l/ov511-decomp
* /usr/lib32/libv4l/ov518-decomp
* /usr/lib32/libv4l/plugins/libv4l-mplane.so
* /usr/lib32/libv4l/v4l1compat.so
* /usr/lib32/libv4l/v4l2convert.so
* /usr/lib32/libv4l1.so
* /usr/lib32/libv4l1.so.0
* /usr/lib32/libv4l1.so.0.0.0
* /usr/lib32/libv4l2.so
* /usr/lib32/libv4l2.so.0
* /usr/lib32/libv4l2.so.0.0.0
* /usr/lib32/libv4l2rds.so
* /usr/lib32/libv4l2rds.so.0
* /usr/lib32/libv4l2rds.so.0.0.0
* /usr/lib32/libv4l2tracer.so
* /usr/lib32/libv4lconvert.so
* /usr/lib32/libv4lconvert.so.0
* /usr/lib32/libv4lconvert.so.0.0.0
* /usr/lib32/pkgconfig/libdvbv5.pc
* /usr/lib32/pkgconfig/libv4l1.pc
* /usr/lib32/pkgconfig/libv4l2.pc
* /usr/lib32/pkgconfig/libv4l2rds.pc
* /usr/lib32/pkgconfig/libv4lconvert.pc
{{< /files >}}