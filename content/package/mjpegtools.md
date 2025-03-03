+++
draft = false
title = "mjpegtools 2.2.1-6"
version = "2.2.1-6"
description = "The mjpeg programs are a set of tools that can do recording of videos and playback under Linux."
date = "2024-11-14T15:18:02"
aliases = "/packages/3228"
categories = ['xapps']
upstreamurl = "http://mjpeg.sourceforge.net/"
arch = "x86_64"
size = "719936"
usize = "2054196"
sha1sum = "c7093c50a9b071749c265ffe2d837aa312f36e06"
depends = "['libdv>=1.0.0-5', 'libjpeg-turbo', 'libpng>=1.6.25', 'libxxf86dga>=1.0.2-3']"
reverse_depends = "['gst1-plugins-bad', 'gst1-plugins-bad-mpeg2enc']"
+++
### Description: 
The mjpeg programs are a set of tools that can do recording of videos and playback under Linux.

### Files: 
* /usr/bin/anytovcd.sh
* /usr/bin/jpeg2yuv
* /usr/bin/lav2avi.sh
* /usr/bin/lav2mpeg
* /usr/bin/lav2wav
* /usr/bin/lav2yuv
* /usr/bin/lavaddwav
* /usr/bin/lavinfo
* /usr/bin/lavpipe
* /usr/bin/lavtc.sh
* /usr/bin/lavtrans
* /usr/bin/matteblend.flt
* /usr/bin/mjpeg_simd_helper
* /usr/bin/mp2enc
* /usr/bin/mpeg2enc
* /usr/bin/mpegtranscode
* /usr/bin/mplex
* /usr/bin/multiblend.flt
* /usr/bin/pgmtoy4m
* /usr/bin/png2yuv
* /usr/bin/pnmtoy4m
* /usr/bin/ppmtoy4m
* /usr/bin/transist.flt
* /usr/bin/y4mblack
* /usr/bin/y4mcolorbars
* /usr/bin/y4mdenoise
* /usr/bin/y4mhist
* /usr/bin/y4minterlace
* /usr/bin/y4mivtc
* /usr/bin/y4mscaler
* /usr/bin/y4mshift
* /usr/bin/y4mspatialfilter
* /usr/bin/y4mstabilizer
* /usr/bin/y4mtopnm
* /usr/bin/y4mtoppm
* /usr/bin/y4mtoyuv
* /usr/bin/y4munsharp
* /usr/bin/ypipe
* /usr/bin/yuv2lav
* /usr/bin/yuv4mpeg
* /usr/bin/yuvcorrect
* /usr/bin/yuvcorrect_tune
* /usr/bin/yuvdeinterlace
* /usr/bin/yuvdenoise
* /usr/bin/yuvfps
* /usr/bin/yuvinactive
* /usr/bin/yuvkineco
* /usr/bin/yuvmedianfilter
* /usr/bin/yuvscaler
* /usr/bin/yuvycsnoise
* /usr/bin/yuyvtoy4m
* /usr/include/mjpegtools/audiolib.h
* /usr/include/mjpegtools/avilib.h
* /usr/include/mjpegtools/editlist.h
* /usr/include/mjpegtools/format_codes.h
* /usr/include/mjpegtools/frequencies.h
* /usr/include/mjpegtools/jpegutils.h
* /usr/include/mjpegtools/lav_io.h
* /usr/include/mjpegtools/liblavplay.h
* /usr/include/mjpegtools/liblavrec.h
* /usr/include/mjpegtools/mjpeg_logging.h
* /usr/include/mjpegtools/mjpeg_types.h
* /usr/include/mjpegtools/motionsearch.h
* /usr/include/mjpegtools/mpeg2enc/elemstrmwriter.hh
* /usr/include/mjpegtools/mpeg2enc/encoderparams.hh
* /usr/include/mjpegtools/mpeg2enc/encodertypes.h
* /usr/include/mjpegtools/mpeg2enc/imageplanes.hh
* /usr/include/mjpegtools/mpeg2enc/macroblock.hh
* /usr/include/mjpegtools/mpeg2enc/mpeg2coder.hh
* /usr/include/mjpegtools/mpeg2enc/mpeg2encoder.hh
* /usr/include/mjpegtools/mpeg2enc/mpeg2encoptions.hh
* /usr/include/mjpegtools/mpeg2enc/mpeg2encparams.h
* /usr/include/mjpegtools/mpeg2enc/mpeg2syntaxcodes.h
* /usr/include/mjpegtools/mpeg2enc/ontheflyratectlpass1.hh
* /usr/include/mjpegtools/mpeg2enc/ontheflyratectlpass2.hh
* /usr/include/mjpegtools/mpeg2enc/picture.hh
* /usr/include/mjpegtools/mpeg2enc/picturereader.hh
* /usr/include/mjpegtools/mpeg2enc/predict_ref.h
* /usr/include/mjpegtools/mpeg2enc/quantize.hh
* /usr/include/mjpegtools/mpeg2enc/quantize_ref.h
* /usr/include/mjpegtools/mpeg2enc/ratectl.hh
* /usr/include/mjpegtools/mpeg2enc/seqencoder.hh
* /usr/include/mjpegtools/mpeg2enc/streamstate.h
* /usr/include/mjpegtools/mpeg2enc/syntaxconsts.h
* /usr/include/mjpegtools/mpegconsts.h
* /usr/include/mjpegtools/mpegtimecode.h
* /usr/include/mjpegtools/mplex/audiostrm.hpp
* /usr/include/mjpegtools/mplex/aunit.hpp
* /usr/include/mjpegtools/mplex/aunitbuffer.hpp
* /usr/include/mjpegtools/mplex/bits.hpp
* /usr/include/mjpegtools/mplex/decodebufmodel.hpp
* /usr/include/mjpegtools/mplex/inputstrm.hpp
* /usr/include/mjpegtools/mplex/interact.hpp
* /usr/include/mjpegtools/mplex/mplexconsts.hpp
* /usr/include/mjpegtools/mplex/multiplexor.hpp
* /usr/include/mjpegtools/mplex/outputstrm.hpp
* /usr/include/mjpegtools/mplex/padstrm.hpp
* /usr/include/mjpegtools/mplex/stillsstream.hpp
* /usr/include/mjpegtools/mplex/stream_params.hpp
* /usr/include/mjpegtools/mplex/systems.hpp
* /usr/include/mjpegtools/mplex/videostrm.hpp
* /usr/include/mjpegtools/yuv4mpeg.h
* /usr/lib/liblavfile-2.2.so.0
* /usr/lib/liblavfile-2.2.so.0.0.0
* /usr/lib/liblavfile.so
* /usr/lib/liblavjpeg-2.2.so.0
* /usr/lib/liblavjpeg-2.2.so.0.0.0
* /usr/lib/liblavjpeg.so
* /usr/lib/libmjpegutils-2.2.so.0
* /usr/lib/libmjpegutils-2.2.so.0.0.0
* /usr/lib/libmjpegutils.so
* /usr/lib/libmpeg2encpp-2.2.so.0
* /usr/lib/libmpeg2encpp-2.2.so.0.0.0
* /usr/lib/libmpeg2encpp.so
* /usr/lib/libmplex2-2.2.so.0
* /usr/lib/libmplex2-2.2.so.0.0.0
* /usr/lib/libmplex2.so
* /usr/lib/pkgconfig/mjpegtools.pc
* /usr/share/doc/mjpegtools-2.2.1/AUTHORS
* /usr/share/doc/mjpegtools-2.2.1/BUGS
* /usr/share/doc/mjpegtools-2.2.1/ChangeLog
* /usr/share/doc/mjpegtools-2.2.1/CHANGES
* /usr/share/doc/mjpegtools-2.2.1/COPYING
* /usr/share/doc/mjpegtools-2.2.1/INSTALL
* /usr/share/doc/mjpegtools-2.2.1/INSTALL.real
* /usr/share/doc/mjpegtools-2.2.1/NEWS
* /usr/share/doc/mjpegtools-2.2.1/README
* /usr/share/doc/mjpegtools-2.2.1/README.AltiVec
* /usr/share/doc/mjpegtools-2.2.1/README.avilib
* /usr/share/doc/mjpegtools-2.2.1/README.DV
* /usr/share/doc/mjpegtools-2.2.1/README.lavpipe
* /usr/share/doc/mjpegtools-2.2.1/README.transist
* /usr/share/doc/mjpegtools-2.2.1/TODO
* /usr/share/info/mjpeg-howto.info.gz
* /usr/share/man/man1/jpeg2yuv.1.gz
* /usr/share/man/man1/lav2mpeg.1.gz
* /usr/share/man/man1/lav2wav.1.gz
* /usr/share/man/man1/lav2yuv.1.gz
* /usr/share/man/man1/lavpipe.1.gz
* /usr/share/man/man1/lavplay.1.gz
* /usr/share/man/man1/lavrec.1.gz
* /usr/share/man/man1/lavtrans.1.gz
* /usr/share/man/man1/mjpegtools.1.gz
* /usr/share/man/man1/mp2enc.1.gz
* /usr/share/man/man1/mpeg2enc.1.gz
* /usr/share/man/man1/mplex.1.gz
* /usr/share/man/man1/pgmtoy4m.1.gz
* /usr/share/man/man1/png2yuv.1.gz
* /usr/share/man/man1/pnmtoy4m.1.gz
* /usr/share/man/man1/ppmtoy4m.1.gz
* /usr/share/man/man1/y4mcolorbars.1.gz
* /usr/share/man/man1/y4mdenoise.1.gz
* /usr/share/man/man1/y4mscaler.1.gz
* /usr/share/man/man1/y4mtopnm.1.gz
* /usr/share/man/man1/y4mtoppm.1.gz
* /usr/share/man/man1/y4munsharp.1.gz
* /usr/share/man/man1/yuv2lav.1.gz
* /usr/share/man/man1/yuvdenoise.1.gz
* /usr/share/man/man1/yuvfps.1.gz
* /usr/share/man/man1/yuvinactive.1.gz
* /usr/share/man/man1/yuvkineco.1.gz
* /usr/share/man/man1/yuvmedianfilter.1.gz
* /usr/share/man/man1/yuvplay.1.gz
* /usr/share/man/man1/yuvscaler.1.gz
* /usr/share/man/man1/yuvycsnoise.1.gz
* /usr/share/man/man5/yuv4mpeg.5.gz
