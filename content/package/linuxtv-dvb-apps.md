+++
draft = false
title = "linuxtv-dvb-apps 1.1.1-2"
version = "1.1.1-2"
date = "2018-02-11T15:00:07"
categories = ['apps-extra']
upstreamurl = "http://www.linuxtv.org"
arch = "x86_64"
size = "215792"
usize = "1409580"
sha1sum = "8f2bbe398f20b530fafd85bebdac6befb7f4c62a"
depends = "['glibc']"
files = "['usr/', 'usr/bin/', 'usr/bin/atsc_epg', 'usr/bin/av7110_loadkeys', 'usr/bin/azap', 'usr/bin/czap', 'usr/bin/dib3000-watch', 'usr/bin/dst_test', 'usr/bin/dvbdate', 'usr/bin/dvbnet', 'usr/bin/dvbscan', 'usr/bin/dvbtraffic', 'usr/bin/femon', 'usr/bin/gnutv', 'usr/bin/gotox', 'usr/bin/lsdvb', 'usr/bin/scan', 'usr/bin/szap', 'usr/bin/tzap', 'usr/bin/zap', 'usr/include/', 'usr/include/libdvbapi/', 'usr/include/libdvbapi/dvbaudio.h', 'usr/include/libdvbapi/dvbca.h', 'usr/include/libdvbapi/dvbdemux.h', 'usr/include/libdvbapi/dvbfe.h', 'usr/include/libdvbapi/dvbnet.h', 'usr/include/libdvbapi/dvbvideo.h', 'usr/include/libdvbcfg/', 'usr/include/libdvbcfg/dvbcfg_scanfile.h', 'usr/include/libdvbcfg/dvbcfg_zapchannel.h', 'usr/include/libdvben50221/', 'usr/include/libdvben50221/asn_1.h', 'usr/include/libdvben50221/en50221_app_ai.h', 'usr/include/libdvben50221/en50221_app_auth.h', 'usr/include/libdvben50221/en50221_app_ca.h', 'usr/include/libdvben50221/en50221_app_datetime.h', 'usr/include/libdvben50221/en50221_app_dvb.h', 'usr/include/libdvben50221/en50221_app_epg.h', 'usr/include/libdvben50221/en50221_app_lowspeed.h', 'usr/include/libdvben50221/en50221_app_mmi.h', 'usr/include/libdvben50221/en50221_app_rm.h', 'usr/include/libdvben50221/en50221_app_smartcard.h', 'usr/include/libdvben50221/en50221_app_tags.h', 'usr/include/libdvben50221/en50221_app_teletext.h', 'usr/include/libdvben50221/en50221_app_utils.h', 'usr/include/libdvben50221/en50221_errno.h', 'usr/include/libdvben50221/en50221_session.h', 'usr/include/libdvben50221/en50221_stdcam.h', 'usr/include/libdvben50221/en50221_transport.h', 'usr/include/libdvbsec/', 'usr/include/libdvbsec/dvbsec_api.h', 'usr/include/libdvbsec/dvbsec_cfg.h', 'usr/include/libesg/', 'usr/include/libesg/bootstrap/', 'usr/include/libesg/bootstrap/access_descriptor.h', 'usr/include/libesg/bootstrap/provider_discovery_descriptor.h', 'usr/include/libesg/encapsulation/', 'usr/include/libesg/encapsulation/container.h', 'usr/include/libesg/encapsulation/data_repository.h', 'usr/include/libesg/encapsulation/fragment_management_information.h', 'usr/include/libesg/encapsulation/string_repository.h', 'usr/include/libesg/representation/', 'usr/include/libesg/representation/encapsulated_textual_esg_xml_fragment.h', 'usr/include/libesg/representation/init_message.h', 'usr/include/libesg/representation/textual_decoder_init.h', 'usr/include/libesg/transport/', 'usr/include/libesg/transport/session_partition_declaration.h', 'usr/include/libesg/types.h', 'usr/include/libucsi/', 'usr/include/libucsi/atsc/', 'usr/include/libucsi/atsc/ac3_descriptor.h', 'usr/include/libucsi/atsc/caption_service_descriptor.h', 'usr/include/libucsi/atsc/component_name_descriptor.h', 'usr/include/libucsi/atsc/content_advisory_descriptor.h', 'usr/include/libucsi/atsc/cvct_section.h', 'usr/include/libucsi/atsc/dcc_arriving_request_descriptor.h', 'usr/include/libucsi/atsc/dcc_departing_request_descriptor.h', 'usr/include/libucsi/atsc/dccsct_section.h', 'usr/include/libucsi/atsc/dcct_section.h', 'usr/include/libucsi/atsc/descriptor.h', 'usr/include/libucsi/atsc/eit_section.h', 'usr/include/libucsi/atsc/ett_section.h', 'usr/include/libucsi/atsc/extended_channel_name_descriptor.h', 'usr/include/libucsi/atsc/genre_descriptor.h', 'usr/include/libucsi/atsc/mgt_section.h', 'usr/include/libucsi/atsc/rc_descriptor.h', 'usr/include/libucsi/atsc/rrt_section.h', 'usr/include/libucsi/atsc/section.h', 'usr/include/libucsi/atsc/service_location_descriptor.h', 'usr/include/libucsi/atsc/stt_section.h', 'usr/include/libucsi/atsc/stuffing_descriptor.h', 'usr/include/libucsi/atsc/time_shifted_service_descriptor.h', 'usr/include/libucsi/atsc/tvct_section.h', 'usr/include/libucsi/atsc/types.h', 'usr/include/libucsi/crc32.h', 'usr/include/libucsi/descriptor.h', 'usr/include/libucsi/dvb/', 'usr/include/libucsi/dvb/ac3_descriptor.h', 'usr/include/libucsi/dvb/adaptation_field_data_descriptor.h', 'usr/include/libucsi/dvb/ait_application_descriptor.h', 'usr/include/libucsi/dvb/ait_application_icons_descriptor.h', 'usr/include/libucsi/dvb/ait_application_name_descriptor.h', 'usr/include/libucsi/dvb/ait_external_application_authorisation_descriptor.h', 'usr/include/libucsi/dvb/ancillary_data_descriptor.h', 'usr/include/libucsi/dvb/announcement_support_descriptor.h', 'usr/include/libucsi/dvb/application_signalling_descriptor.h', 'usr/include/libucsi/dvb/bat_section.h', 'usr/include/libucsi/dvb/bouquet_name_descriptor.h', 'usr/include/libucsi/dvb/ca_identifier_descriptor.h', 'usr/include/libucsi/dvb/cable_delivery_descriptor.h', 'usr/include/libucsi/dvb/cell_frequency_link_descriptor.h', 'usr/include/libucsi/dvb/cell_list_descriptor.h', 'usr/include/libucsi/dvb/component_descriptor.h', 'usr/include/libucsi/dvb/content_descriptor.h', 'usr/include/libucsi/dvb/content_identifier_descriptor.h', 'usr/include/libucsi/dvb/country_availability_descriptor.h', 'usr/include/libucsi/dvb/data_broadcast_descriptor.h', 'usr/include/libucsi/dvb/data_broadcast_id_descriptor.h', 'usr/include/libucsi/dvb/default_authority_descriptor.h', 'usr/include/libucsi/dvb/descriptor.h', 'usr/include/libucsi/dvb/dit_section.h', 'usr/include/libucsi/dvb/dsng_descriptor.h', 'usr/include/libucsi/dvb/eit_section.h', 'usr/include/libucsi/dvb/extended_event_descriptor.h', 'usr/include/libucsi/dvb/frequency_list_descriptor.h', 'usr/include/libucsi/dvb/int_section.h', 'usr/include/libucsi/dvb/ip_mac_platform_name_descriptor.h', 'usr/include/libucsi/dvb/ip_mac_platform_provider_name_descriptor.h', 'usr/include/libucsi/dvb/ip_mac_stream_location_descriptor.h', 'usr/include/libucsi/dvb/linkage_descriptor.h', 'usr/include/libucsi/dvb/local_time_offset_descriptor.h', 'usr/include/libucsi/dvb/mhp_data_broadcast_id_descriptor.h', 'usr/include/libucsi/dvb/mosaic_descriptor.h', 'usr/include/libucsi/dvb/mpe_fec_section.h', 'usr/include/libucsi/dvb/multilingual_bouquet_name_descriptor.h', 'usr/include/libucsi/dvb/multilingual_component_descriptor.h', 'usr/include/libucsi/dvb/multilingual_network_name_descriptor.h', 'usr/include/libucsi/dvb/multilingual_service_name_descriptor.h', 'usr/include/libucsi/dvb/network_name_descriptor.h', 'usr/include/libucsi/dvb/nit_section.h', 'usr/include/libucsi/dvb/nvod_reference_descriptor.h', 'usr/include/libucsi/dvb/parental_rating_descriptor.h', 'usr/include/libucsi/dvb/partial_transport_stream_descriptor.h', 'usr/include/libucsi/dvb/pdc_descriptor.h', 'usr/include/libucsi/dvb/private_data_specifier_descriptor.h', 'usr/include/libucsi/dvb/related_content_descriptor.h', 'usr/include/libucsi/dvb/rnt_rar_over_dvb_stream_descriptor.h', 'usr/include/libucsi/dvb/rnt_rar_over_ip_descriptor.h', 'usr/include/libucsi/dvb/rnt_rnt_scan_descriptor.h', 'usr/include/libucsi/dvb/rst_section.h', 'usr/include/libucsi/dvb/s2_satellite_delivery_descriptor.h', 'usr/include/libucsi/dvb/satellite_delivery_descriptor.h', 'usr/include/libucsi/dvb/scrambling_descriptor.h', 'usr/include/libucsi/dvb/sdt_section.h', 'usr/include/libucsi/dvb/section.h', 'usr/include/libucsi/dvb/service_availability_descriptor.h', 'usr/include/libucsi/dvb/service_descriptor.h', 'usr/include/libucsi/dvb/service_identifier_descriptor.h', 'usr/include/libucsi/dvb/service_list_descriptor.h', 'usr/include/libucsi/dvb/service_move_descriptor.h', 'usr/include/libucsi/dvb/short_event_descriptor.h', 'usr/include/libucsi/dvb/short_smoothing_buffer_descriptor.h', 'usr/include/libucsi/dvb/sit_section.h', 'usr/include/libucsi/dvb/st_section.h', 'usr/include/libucsi/dvb/stream_identifier_descriptor.h', 'usr/include/libucsi/dvb/stuffing_descriptor.h', 'usr/include/libucsi/dvb/subtitling_descriptor.h', 'usr/include/libucsi/dvb/target_ip_address_descriptor.h', 'usr/include/libucsi/dvb/target_ip_slash_descriptor.h', 'usr/include/libucsi/dvb/target_ip_source_slash_descriptor.h', 'usr/include/libucsi/dvb/target_ipv6_address_descriptor.h', 'usr/include/libucsi/dvb/target_ipv6_slash_descriptor.h', 'usr/include/libucsi/dvb/target_ipv6_source_slash_descriptor.h', 'usr/include/libucsi/dvb/tdt_section.h', 'usr/include/libucsi/dvb/telephone_descriptor.h', 'usr/include/libucsi/dvb/teletext_descriptor.h', 'usr/include/libucsi/dvb/terrestrial_delivery_descriptor.h', 'usr/include/libucsi/dvb/time_shifted_event_descriptor.h', 'usr/include/libucsi/dvb/time_shifted_service_descriptor.h', 'usr/include/libucsi/dvb/time_slice_fec_identifier_descriptor.h', 'usr/include/libucsi/dvb/tot_section.h', 'usr/include/libucsi/dvb/transport_stream_descriptor.h', 'usr/include/libucsi/dvb/tva_container_section.h', 'usr/include/libucsi/dvb/tva_id_descriptor.h', 'usr/include/libucsi/dvb/types.h', 'usr/include/libucsi/dvb/vbi_data_descriptor.h', 'usr/include/libucsi/dvb/vbi_teletext_descriptor.h', 'usr/include/libucsi/endianops.h', 'usr/include/libucsi/mpeg/', 'usr/include/libucsi/mpeg/audio_stream_descriptor.h', 'usr/include/libucsi/mpeg/ca_descriptor.h', 'usr/include/libucsi/mpeg/cat_section.h', 'usr/include/libucsi/mpeg/content_labelling_descriptor.h', 'usr/include/libucsi/mpeg/copyright_descriptor.h', 'usr/include/libucsi/mpeg/data_stream_alignment_descriptor.h', 'usr/include/libucsi/mpeg/datagram_section.h', 'usr/include/libucsi/mpeg/descriptor.h', 'usr/include/libucsi/mpeg/external_es_id_descriptor.h', 'usr/include/libucsi/mpeg/fmc_descriptor.h', 'usr/include/libucsi/mpeg/fmxbuffer_size_descriptor.h', 'usr/include/libucsi/mpeg/hierarchy_descriptor.h', 'usr/include/libucsi/mpeg/ibp_descriptor.h', 'usr/include/libucsi/mpeg/iod_descriptor.h', 'usr/include/libucsi/mpeg/iso_639_language_descriptor.h', 'usr/include/libucsi/mpeg/maximum_bitrate_descriptor.h', 'usr/include/libucsi/mpeg/metadata_descriptor.h', 'usr/include/libucsi/mpeg/metadata_pointer_descriptor.h', 'usr/include/libucsi/mpeg/metadata_section.h', 'usr/include/libucsi/mpeg/metadata_std_descriptor.h', 'usr/include/libucsi/mpeg/mpeg4_audio_descriptor.h', 'usr/include/libucsi/mpeg/mpeg4_video_descriptor.h', 'usr/include/libucsi/mpeg/multiplex_buffer_descriptor.h', 'usr/include/libucsi/mpeg/multiplex_buffer_utilization_descriptor.h', 'usr/include/libucsi/mpeg/muxcode_descriptor.h', 'usr/include/libucsi/mpeg/odsmt_section.h', 'usr/include/libucsi/mpeg/pat_section.h', 'usr/include/libucsi/mpeg/pmt_section.h', 'usr/include/libucsi/mpeg/private_data_indicator_descriptor.h', 'usr/include/libucsi/mpeg/registration_descriptor.h', 'usr/include/libucsi/mpeg/section.h', 'usr/include/libucsi/mpeg/sl_descriptor.h', 'usr/include/libucsi/mpeg/smoothing_buffer_descriptor.h', 'usr/include/libucsi/mpeg/std_descriptor.h', 'usr/include/libucsi/mpeg/system_clock_descriptor.h', 'usr/include/libucsi/mpeg/target_background_grid_descriptor.h', 'usr/include/libucsi/mpeg/tsdt_section.h', 'usr/include/libucsi/mpeg/types.h', 'usr/include/libucsi/mpeg/video_stream_descriptor.h', 'usr/include/libucsi/mpeg/video_window_descriptor.h', 'usr/include/libucsi/section.h', 'usr/include/libucsi/section_buf.h', 'usr/include/libucsi/transport_packet.h', 'usr/include/libucsi/types.h', 'usr/lib/', 'usr/lib/libdvbapi.so', 'usr/lib/libdvbcfg.so', 'usr/lib/libdvben50221.so', 'usr/lib/libdvbsec.so', 'usr/lib/libesg.so', 'usr/lib/libucsi.so', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/linuxtv-dvb-apps-1.1.1/', 'usr/share/doc/linuxtv-dvb-apps-1.1.1/COPYING', 'usr/share/doc/linuxtv-dvb-apps-1.1.1/COPYING.LGPL', 'usr/share/doc/linuxtv-dvb-apps-1.1.1/INSTALL', 'usr/share/doc/linuxtv-dvb-apps-1.1.1/README', 'usr/share/dvb/', 'usr/share/dvb/av7110_loadkeys/', 'usr/share/dvb/av7110_loadkeys/activy.rcmm', 'usr/share/dvb/av7110_loadkeys/galaxis.rcmm', 'usr/share/dvb/av7110_loadkeys/hauppauge.rc5', 'usr/share/dvb/av7110_loadkeys/hauppauge2.rc5', 'usr/share/dvb/av7110_loadkeys/hauppauge_grey.rc5', 'usr/share/dvb/av7110_loadkeys/mbo_81095-code_562.rc5', 'usr/share/dvb/av7110_loadkeys/medion_088.rc5', 'usr/share/dvb/av7110_loadkeys/medion_155.rc5', 'usr/share/dvb/av7110_loadkeys/philips.rc5', 'usr/share/dvb/av7110_loadkeys/philips1358.rc5', 'usr/share/dvb/av7110_loadkeys/technotrend.rc5']"
+++
Utilities for DVB cards