+++
draft = false
title = "speech_tools 2.5.0-1"
version = "2.5.0-1"
description = "Speech tools for Festival Text to Speech engine"
date = "2020-02-13T18:45:31"
aliases = "/packages/220038"
categories = ['apps-extra']
upstreamurl = "http://festvox.org/festival/"
arch = "x86_64"
size = "15619100"
usize = "27128706"
sha1sum = "d791daa1474bda733da0dd342d5075822c2d9faf"
depends = "['libstdc++', 'ncurses']"
+++
Speech tools for Festival Text to Speech engine{{< spoiler text="show files" >}}* /usr/bin/align
* /usr/bin/bcat
* /usr/bin/build_docbook_index
* /usr/bin/ch_lab
* /usr/bin/ch_track
* /usr/bin/ch_utt
* /usr/bin/ch_wave
* /usr/bin/cxx_to_docbook
* /usr/bin/design_filter
* /usr/bin/dp
* /usr/bin/est_examples
* /usr/bin/est_gdb
* /usr/bin/est_program
* /usr/bin/example_to_doc++
* /usr/bin/make_wagon_desc
* /usr/bin/na_play
* /usr/bin/na_record
* /usr/bin/ngram_build
* /usr/bin/ngram_test
* /usr/bin/ols
* /usr/bin/ols_test
* /usr/bin/pda
* /usr/bin/pitchmark
* /usr/bin/pm
* /usr/bin/raw_to_xgraph
* /usr/bin/resynth
* /usr/bin/scfg_make
* /usr/bin/scfg_parse
* /usr/bin/scfg_test
* /usr/bin/scfg_train
* /usr/bin/sig2fv
* /usr/bin/sigfilter
* /usr/bin/siod
* /usr/bin/spectgen
* /usr/bin/tex_to_images
* /usr/bin/tilt_analysis
* /usr/bin/tilt_synthesis
* /usr/bin/viterbi
* /usr/bin/wagon
* /usr/bin/wagon_test
* /usr/bin/wfst_build
* /usr/bin/wfst_run
* /usr/bin/wfst_train
* /usr/bin/xml_parser
* /usr/include/speech-tools/EST.h
* /usr/include/speech-tools/EST_audio.h
* /usr/include/speech-tools/EST_bool.h
* /usr/include/speech-tools/EST_ChannelType.h
* /usr/include/speech-tools/EST_Chunk.h
* /usr/include/speech-tools/EST_cluster.h
* /usr/include/speech-tools/EST_cmd_line.h
* /usr/include/speech-tools/EST_cmd_line_options.h
* /usr/include/speech-tools/EST_common.h
* /usr/include/speech-tools/EST_Complex.h
* /usr/include/speech-tools/EST_Contents.h
* /usr/include/speech-tools/EST_cutils.h
* /usr/include/speech-tools/EST_DMatrix.h
* /usr/include/speech-tools/EST_dynamic_model.h
* /usr/include/speech-tools/EST_error.h
* /usr/include/speech-tools/EST_Event.h
* /usr/include/speech-tools/EST_Featured.h
* /usr/include/speech-tools/EST_FeatureData.h
* /usr/include/speech-tools/EST_Features.h
* /usr/include/speech-tools/EST_features_aux.h
* /usr/include/speech-tools/EST_FileType.h
* /usr/include/speech-tools/EST_FMatrix.h
* /usr/include/speech-tools/EST_FringeServer.h
* /usr/include/speech-tools/EST_grammar.h
* /usr/include/speech-tools/EST_Handleable.h
* /usr/include/speech-tools/EST_HMM.h
* /usr/include/speech-tools/EST_IMatrix.h
* /usr/include/speech-tools/EST_inline_utils.h
* /usr/include/speech-tools/EST_iostream.h
* /usr/include/speech-tools/EST_io_aux.h
* /usr/include/speech-tools/EST_kalman.h
* /usr/include/speech-tools/EST_lattice.h
* /usr/include/speech-tools/EST_lattice_io.h
* /usr/include/speech-tools/EST_ling_class.h
* /usr/include/speech-tools/EST_math.h
* /usr/include/speech-tools/EST_model_types.h
* /usr/include/speech-tools/EST_multistats.h
* /usr/include/speech-tools/EST_Ngrammar.h
* /usr/include/speech-tools/EST_Option.h
* /usr/include/speech-tools/EST_Pathname.h
* /usr/include/speech-tools/EST_PST.h
* /usr/include/speech-tools/EST_Regex.h
* /usr/include/speech-tools/EST_rw_status.h
* /usr/include/speech-tools/EST_SCFG.h
* /usr/include/speech-tools/EST_SCFG_Chart.h
* /usr/include/speech-tools/EST_Server.h
* /usr/include/speech-tools/EST_ServiceTable.h
* /usr/include/speech-tools/EST_sigpr.h
* /usr/include/speech-tools/EST_simplestats.h
* /usr/include/speech-tools/EST_SingleChannelWave.h
* /usr/include/speech-tools/EST_SMatrix.h
* /usr/include/speech-tools/EST_socket.h
* /usr/include/speech-tools/EST_sort.h
* /usr/include/speech-tools/EST_speech_class.h
* /usr/include/speech-tools/EST_stats.h
* /usr/include/speech-tools/EST_strcasecmp.h
* /usr/include/speech-tools/EST_String.h
* /usr/include/speech-tools/EST_StringTrie.h
* /usr/include/speech-tools/EST_string_aux.h
* /usr/include/speech-tools/EST_system.h
* /usr/include/speech-tools/EST_TBox.h
* /usr/include/speech-tools/EST_TBuffer.h
* /usr/include/speech-tools/EST_TDeque.h
* /usr/include/speech-tools/EST_THandle.h
* /usr/include/speech-tools/EST_THash.h
* /usr/include/speech-tools/EST_tilt.h
* /usr/include/speech-tools/EST_TIterator.h
* /usr/include/speech-tools/EST_TKVL.h
* /usr/include/speech-tools/EST_TList.h
* /usr/include/speech-tools/EST_TMatrix.h
* /usr/include/speech-tools/EST_TNamedEnum.h
* /usr/include/speech-tools/EST_Token.h
* /usr/include/speech-tools/EST_Track.h
* /usr/include/speech-tools/EST_TrackMap.h
* /usr/include/speech-tools/EST_track_aux.h
* /usr/include/speech-tools/EST_TSimpleMatrix.h
* /usr/include/speech-tools/EST_TSimpleVector.h
* /usr/include/speech-tools/EST_TSortable.h
* /usr/include/speech-tools/EST_TTimeIndex.h
* /usr/include/speech-tools/EST_TVector.h
* /usr/include/speech-tools/EST_types.h
* /usr/include/speech-tools/EST_UList.h
* /usr/include/speech-tools/EST_unix.h
* /usr/include/speech-tools/EST_util_class.h
* /usr/include/speech-tools/EST_Val.h
* /usr/include/speech-tools/EST_Val_defs.h
* /usr/include/speech-tools/EST_viterbi.h
* /usr/include/speech-tools/EST_Wagon.h
* /usr/include/speech-tools/EST_walloc.h
* /usr/include/speech-tools/EST_Wave.h
* /usr/include/speech-tools/EST_wave_aux.h
* /usr/include/speech-tools/EST_WFST.h
* /usr/include/speech-tools/instantiate/EST_TDequeI.h
* /usr/include/speech-tools/instantiate/EST_THashI.h
* /usr/include/speech-tools/instantiate/EST_TIteratorI.h
* /usr/include/speech-tools/instantiate/EST_TKVLI.h
* /usr/include/speech-tools/instantiate/EST_TListI.h
* /usr/include/speech-tools/instantiate/EST_TMatrixI.h
* /usr/include/speech-tools/instantiate/EST_TNamedEnumI.h
* /usr/include/speech-tools/instantiate/EST_TSimpleMatrixI.h
* /usr/include/speech-tools/instantiate/EST_TSimpleVectorI.h
* /usr/include/speech-tools/instantiate/EST_TSortableI.h
* /usr/include/speech-tools/instantiate/EST_TStringHashI.h
* /usr/include/speech-tools/instantiate/EST_TVectorI.h
* /usr/include/speech-tools/instantiate/Makefile
* /usr/include/speech-tools/ling_class/EST_FeatureFunctionPackage.h
* /usr/include/speech-tools/ling_class/EST_Item.h
* /usr/include/speech-tools/ling_class/EST_item_aux.h
* /usr/include/speech-tools/ling_class/EST_Item_Content.h
* /usr/include/speech-tools/ling_class/EST_item_content_aux.h
* /usr/include/speech-tools/ling_class/EST_Relation.h
* /usr/include/speech-tools/ling_class/EST_relation_aux.h
* /usr/include/speech-tools/ling_class/EST_relation_compare.h
* /usr/include/speech-tools/ling_class/EST_Relation_list.h
* /usr/include/speech-tools/ling_class/EST_Relation_mls.h
* /usr/include/speech-tools/ling_class/EST_Relation_tree.h
* /usr/include/speech-tools/ling_class/EST_Utterance.h
* /usr/include/speech-tools/ling_class/EST_utterance_aux.h
* /usr/include/speech-tools/ling_class/EST_utterance_xml.h
* /usr/include/speech-tools/ling_class/Makefile
* /usr/include/speech-tools/Makefile
* /usr/include/speech-tools/rxp/charset.h
* /usr/include/speech-tools/rxp/ctype16.h
* /usr/include/speech-tools/rxp/dtd.h
* /usr/include/speech-tools/rxp/input.h
* /usr/include/speech-tools/rxp/Makefile
* /usr/include/speech-tools/rxp/rxp.h
* /usr/include/speech-tools/rxp/stdio16.h
* /usr/include/speech-tools/rxp/string16.h
* /usr/include/speech-tools/rxp/system.h
* /usr/include/speech-tools/rxp/url.h
* /usr/include/speech-tools/rxp/xmlparser.h
* /usr/include/speech-tools/rxp/XML_Parser.h
* /usr/include/speech-tools/sigpr/EST_fft.h
* /usr/include/speech-tools/sigpr/EST_filter.h
* /usr/include/speech-tools/sigpr/EST_filter_design.h
* /usr/include/speech-tools/sigpr/EST_misc_sigpr.h
* /usr/include/speech-tools/sigpr/EST_pitchmark.h
* /usr/include/speech-tools/sigpr/EST_sigpr_frame.h
* /usr/include/speech-tools/sigpr/EST_sigpr_utt.h
* /usr/include/speech-tools/sigpr/EST_spectrogram.h
* /usr/include/speech-tools/sigpr/EST_Window.h
* /usr/include/speech-tools/sigpr/Makefile
* /usr/include/speech-tools/siod.h
* /usr/include/speech-tools/siod_defs.h
* /usr/include/speech-tools/siod_est.h
* /usr/include/speech-tools/unix/EST_defines_unix.h
* /usr/include/speech-tools/unix/EST_socket_unix.h
* /usr/include/speech-tools/unix/Makefile
* /usr/include/speech-tools/win32/EST_defines_win32.h
* /usr/include/speech-tools/win32/EST_iostream_win32.h
* /usr/include/speech-tools/win32/EST_socket_win32.h
* /usr/include/speech-tools/win32/EST_unix_win32.h
* /usr/include/speech-tools/win32/Makefile
* /usr/lib/libestbase.a
* /usr/lib/libestbase.so
* /usr/lib/libestbase.so.2.5.0.1
* /usr/lib/libestools.a
* /usr/lib/libeststring.a
* /usr/lib/libeststring.so
* /usr/lib/libeststring.so.1.2
* /usr/share/doc/speech_tools-2.5.0/alice
* /usr/share/doc/speech_tools-2.5.0/channel_names.map
* /usr/share/doc/speech_tools-2.5.0/ch_track.htk
* /usr/share/doc/speech_tools-2.5.0/ch_wave.wav
* /usr/share/doc/speech_tools-2.5.0/colours.map
* /usr/share/doc/speech_tools-2.5.0/colours_translation.map
* /usr/share/doc/speech_tools-2.5.0/cstrutt.dtd
* /usr/share/doc/speech_tools-2.5.0/eg.dtd
* /usr/share/doc/speech_tools-2.5.0/eg.xml
* /usr/share/doc/speech_tools-2.5.0/INSTALL
* /usr/share/doc/speech_tools-2.5.0/kdt_001.il
* /usr/share/doc/speech_tools-2.5.0/kdt_001.pm
* /usr/share/doc/speech_tools-2.5.0/kdt_001.tilt
* /usr/share/doc/speech_tools-2.5.0/kdt_001.wav
* /usr/share/doc/speech_tools-2.5.0/ked_wr1_012.utt
* /usr/share/doc/speech_tools-2.5.0/key.lab
* /usr/share/doc/speech_tools-2.5.0/Makefile
* /usr/share/doc/speech_tools-2.5.0/options.file
* /usr/share/doc/speech_tools-2.5.0/README.md
* /usr/share/doc/speech_tools-2.5.0/vit.B.ngram
* /usr/share/doc/speech_tools-2.5.0/vit.observes
* /usr/share/doc/speech_tools-2.5.0/vit.vocab
* /usr/share/doc/speech_tools-2.5.0/wagon.data
* /usr/share/doc/speech_tools-2.5.0/wagon.desc
* /usr/share/doc/speech_tools-2.5.0/wagon.tree
* /usr/share/speech-tools/config/common_make_rules
* /usr/share/speech-tools/config/compilers/egcs.mak
* /usr/share/speech-tools/config/compilers/gcc.mak
* /usr/share/speech-tools/config/compilers/gcc27.mak
* /usr/share/speech-tools/config/compilers/gcc27emx.mak
* /usr/share/speech-tools/config/compilers/gcc28.mak
* /usr/share/speech-tools/config/compilers/gcc295.mak
* /usr/share/speech-tools/config/compilers/gcc296.mak
* /usr/share/speech-tools/config/compilers/gcc30.mak
* /usr/share/speech-tools/config/compilers/gcc31.mak
* /usr/share/speech-tools/config/compilers/gcc32.mak
* /usr/share/speech-tools/config/compilers/gcc_defaults.mak
* /usr/share/speech-tools/config/compilers/intel80.mak
* /usr/share/speech-tools/config/compilers/jdk.mak
* /usr/share/speech-tools/config/compilers/jdk12.mak
* /usr/share/speech-tools/config/compilers/jdk_defaults.mak
* /usr/share/speech-tools/config/compilers/jikes.mak
* /usr/share/speech-tools/config/compilers/jikes_defaults.mak
* /usr/share/speech-tools/config/compilers/jolt.mak
* /usr/share/speech-tools/config/compilers/Makefile
* /usr/share/speech-tools/config/compilers/none.mak
* /usr/share/speech-tools/config/compilers/suncc.mak
* /usr/share/speech-tools/config/compilers/suncc40.mak
* /usr/share/speech-tools/config/compilers/suncc_defaults.mak
* /usr/share/speech-tools/config/config
* /usr/share/speech-tools/config/config.in
* /usr/share/speech-tools/config/configs/cstr.mak
* /usr/share/speech-tools/config/configs/cstr_jdk1.2.mak
* /usr/share/speech-tools/config/configs/egcs_as_gcc.mak
* /usr/share/speech-tools/config/configs/ellipsis.mak
* /usr/share/speech-tools/config/configs/kellogg.mak
* /usr/share/speech-tools/config/configs/Makefile
* /usr/share/speech-tools/config/configs/rjc.mak
* /usr/share/speech-tools/config/configs/v_java.mak
* /usr/share/speech-tools/config/example.Makefile
* /usr/share/speech-tools/config/example.module.mak
* /usr/share/speech-tools/config/Makefile
* /usr/share/speech-tools/config/make_system.mak
* /usr/share/speech-tools/config/modincludes.inc
* /usr/share/speech-tools/config/modules/debugging.mak
* /usr/share/speech-tools/config/modules/descriptions
* /usr/share/speech-tools/config/modules/dmalloc.mak
* /usr/share/speech-tools/config/modules/editline.mak
* /usr/share/speech-tools/config/modules/efence.mak
* /usr/share/speech-tools/config/modules/esd_audio.mak
* /usr/share/speech-tools/config/modules/freebsd16_audio.mak
* /usr/share/speech-tools/config/modules/irix_audio.mak
* /usr/share/speech-tools/config/modules/linux16_audio.mak
* /usr/share/speech-tools/config/modules/macosx_audio.mak
* /usr/share/speech-tools/config/modules/Makefile
* /usr/share/speech-tools/config/modules/mplayer_audio.mak
* /usr/share/speech-tools/config/modules/nas_audio.mak
* /usr/share/speech-tools/config/modules/psola_tm.mak
* /usr/share/speech-tools/config/modules/siod_python.mak
* /usr/share/speech-tools/config/modules/sun16_audio.mak
* /usr/share/speech-tools/config/modules/tcl.mak
* /usr/share/speech-tools/config/modules/win32_audio.mak
* /usr/share/speech-tools/config/project.mak
* /usr/share/speech-tools/config/ReadMe
* /usr/share/speech-tools/config/rules/bin_process.mak
* /usr/share/speech-tools/config/rules/build_dir.mak
* /usr/share/speech-tools/config/rules/build_tree.sh
* /usr/share/speech-tools/config/rules/c.mak
* /usr/share/speech-tools/config/rules/common_make_rules.mak
* /usr/share/speech-tools/config/rules/compile_options.mak
* /usr/share/speech-tools/config/rules/config_errors.mak
* /usr/share/speech-tools/config/rules/cvs.mak
* /usr/share/speech-tools/config/rules/defaults.mak
* /usr/share/speech-tools/config/rules/doc.mak
* /usr/share/speech-tools/config/rules/install.mak
* /usr/share/speech-tools/config/rules/java.mak
* /usr/share/speech-tools/config/rules/library.mak
* /usr/share/speech-tools/config/rules/Makefile
* /usr/share/speech-tools/config/rules/make_depend.awk
* /usr/share/speech-tools/config/rules/make_depend.mak
* /usr/share/speech-tools/config/rules/modules.mak
* /usr/share/speech-tools/config/rules/modules.sh
* /usr/share/speech-tools/config/rules/rcs.mak
* /usr/share/speech-tools/config/rules/rules.mak
* /usr/share/speech-tools/config/rules/script_process.awk
* /usr/share/speech-tools/config/rules/targets.mak
* /usr/share/speech-tools/config/rules/test_make_rules.mak
* /usr/share/speech-tools/config/rules/top_level.mak
* /usr/share/speech-tools/config/rules/visual_c.mak
* /usr/share/speech-tools/config/system.mak
* /usr/share/speech-tools/config/system.sh
* /usr/share/speech-tools/config/systems/alpha_Linux.mak
* /usr/share/speech-tools/config/systems/alpha_OSF1V4.0.mak
* /usr/share/speech-tools/config/systems/alpha_RedHatLinux.mak
* /usr/share/speech-tools/config/systems/DebianGNULinux.mak
* /usr/share/speech-tools/config/systems/default.mak
* /usr/share/speech-tools/config/systems/hp9000_HP-UX.mak
* /usr/share/speech-tools/config/systems/hp9000_HP-UXB.10.mak
* /usr/share/speech-tools/config/systems/ip_IRIX.mak
* /usr/share/speech-tools/config/systems/ip_IRIX5.3.mak
* /usr/share/speech-tools/config/systems/ip_IRIX6.3.mak
* /usr/share/speech-tools/config/systems/ip_IRIX6.4.mak
* /usr/share/speech-tools/config/systems/ip_IRIX646.4.mak
* /usr/share/speech-tools/config/systems/ix86_CYGWIN1.0.mak
* /usr/share/speech-tools/config/systems/ix86_CYGWIN1.1.mak
* /usr/share/speech-tools/config/systems/ix86_CYGWIN1.3.mak
* /usr/share/speech-tools/config/systems/ix86_CYGWIN1.4.mak
* /usr/share/speech-tools/config/systems/ix86_CYGWIN1.5.mak
* /usr/share/speech-tools/config/systems/ix86_CYGWIN1.7.mak
* /usr/share/speech-tools/config/systems/ix86_CYGWIN20.1.mak
* /usr/share/speech-tools/config/systems/ix86_CYGWIN32.mak
* /usr/share/speech-tools/config/systems/ix86_CYGWIN324.0.mak
* /usr/share/speech-tools/config/systems/ix86_Darwin.mak
* /usr/share/speech-tools/config/systems/ix86_FreeBSD.mak
* /usr/share/speech-tools/config/systems/ix86_FreeBSD2.1.mak
* /usr/share/speech-tools/config/systems/ix86_FreeBSD2.2.mak
* /usr/share/speech-tools/config/systems/ix86_FreeBSD3.0.mak
* /usr/share/speech-tools/config/systems/ix86_FreeBSD3.1.mak
* /usr/share/speech-tools/config/systems/ix86_FreeBSD3.2.mak
* /usr/share/speech-tools/config/systems/ix86_FreeBSD3.3.mak
* /usr/share/speech-tools/config/systems/ix86_FreeBSD4.0.mak
* /usr/share/speech-tools/config/systems/ix86_OS22.mak
* /usr/share/speech-tools/config/systems/ix86_RedHatLinux4.0.mak
* /usr/share/speech-tools/config/systems/ix86_RedHatLinux4.1.mak
* /usr/share/speech-tools/config/systems/ix86_RedHatLinux4.2.mak
* /usr/share/speech-tools/config/systems/ix86_RedHatLinux5.0.mak
* /usr/share/speech-tools/config/systems/ix86_RedHatLinux5.1.mak
* /usr/share/speech-tools/config/systems/ix86_RedHatLinux5.2.mak
* /usr/share/speech-tools/config/systems/ix86_RedHatLinux6.0.mak
* /usr/share/speech-tools/config/systems/ix86_RedHatLinux6.1.mak
* /usr/share/speech-tools/config/systems/ix86_RedHatLinux6.2.mak
* /usr/share/speech-tools/config/systems/ix86_RedHatLinux7.0.mak
* /usr/share/speech-tools/config/systems/ix86_SunOS5.5.mak
* /usr/share/speech-tools/config/systems/ix86_SunOS5.6.mak
* /usr/share/speech-tools/config/systems/ix86_SunOS5.7.mak
* /usr/share/speech-tools/config/systems/ix86_SunOS5.8.mak
* /usr/share/speech-tools/config/systems/ix86_SunOS5.mak
* /usr/share/speech-tools/config/systems/Linux.mak
* /usr/share/speech-tools/config/systems/Makefile
* /usr/share/speech-tools/config/systems/power_macintosh_Darwin.mak
* /usr/share/speech-tools/config/systems/RedHatLinux.mak
* /usr/share/speech-tools/config/systems/rs6000_AIX4.1.mak
* /usr/share/speech-tools/config/systems/sparc_SunOS4.1.mak
* /usr/share/speech-tools/config/systems/sparc_SunOS4.mak
* /usr/share/speech-tools/config/systems/sparc_SunOS5.5.mak
* /usr/share/speech-tools/config/systems/sparc_SunOS5.6.mak
* /usr/share/speech-tools/config/systems/sparc_SunOS5.7.mak
* /usr/share/speech-tools/config/systems/sparc_SunOS5.8.mak
* /usr/share/speech-tools/config/systems/sparc_SunOS5.9.mak
* /usr/share/speech-tools/config/systems/sparc_SunOS5.mak
* /usr/share/speech-tools/config/systems/sparc_unknown.mak
* /usr/share/speech-tools/config/systems/unknown_DebianGNULinux.mak
* /usr/share/speech-tools/config/systems/unknown_Linux.mak
* /usr/share/speech-tools/config/systems/unknown_RedHatLinux.mak
* /usr/share/speech-tools/config/systems/unknown_unknown.mak
* /usr/share/speech-tools/config/systems/x86_64_Darwin.mak
* /usr/share/speech-tools/config/test_make_rules
* /usr/share/speech-tools/config/vc_common_make_rules
* /usr/share/speech-tools/config/vc_config_make_rules-dist
* /usr/share/speech-tools/include
* /usr/share/speech-tools/lib/siod/cstr.scm
* /usr/share/speech-tools/lib/siod/fringe.scm
* /usr/share/speech-tools/lib/siod/init.scm
* /usr/share/speech-tools/lib/siod/Makefile
* /usr/share/speech-tools/lib/siod/siod.scm
* /usr/share/speech-tools/lib/siod/siod_client.scm
* /usr/share/speech-tools/lib/siod/siod_server.scm
* /usr/share/speech-tools/lib/siod/web.scm
{{< /spoiler >}}