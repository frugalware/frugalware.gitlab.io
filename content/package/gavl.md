+++
draft = false
title = "gavl 1.4.0-7"
version = "1.4.0-7"
description = "A library which provides basic support for uncompressed Audio, Video and Image data."
date = "2022-02-08T15:03:22"
aliases = "/packages/218265"
categories = ['lib-extra']
upstreamurl = "http://gmerlin.sourceforge.net/"
arch = "x86_64"
size = "2992832"
usize = "7658695"
sha1sum = "609965e9bcfcc7a38379391508bd22f0df1e0b5e"
depends = "['glibc>=2.29-6']"
reverse_depends = "['frei0r-plugins']"
+++
A library which provides basic support for uncompressed Audio, Video and Image data.

{{< files text="show files" >}}* /usr/include/gavl/compression.h
* /usr/include/gavl/gavl.h
* /usr/include/gavl/gavldefs.h
* /usr/include/gavl/gavldsp.h
* /usr/include/gavl/gavltime.h
* /usr/include/gavl/gavl_version.h
* /usr/include/gavl/metadata.h
* /usr/include/gavl/metatags.h
* /usr/include/gavl/timecode.h
* /usr/lib/libgavl.so
* /usr/lib/libgavl.so.1
* /usr/lib/libgavl.so.1.0.0
* /usr/lib/pkgconfig/gavl.pc
* /usr/share/doc/gavl-1.4.0/apiref/annotated.html
* /usr/share/doc/gavl-1.4.0/apiref/bc_s.png
* /usr/share/doc/gavl-1.4.0/apiref/bdwn.png
* /usr/share/doc/gavl-1.4.0/apiref/classes.html
* /usr/share/doc/gavl-1.4.0/apiref/closed.png
* /usr/share/doc/gavl-1.4.0/apiref/compression_8h_source.html
* /usr/share/doc/gavl-1.4.0/apiref/dir_8d9966fd6a811526508c2e8ea93de85b.html
* /usr/share/doc/gavl-1.4.0/apiref/dir_d44c64559bbebec7f509842c48db8b23.html
* /usr/share/doc/gavl-1.4.0/apiref/doc.png
* /usr/share/doc/gavl-1.4.0/apiref/doxygen.css
* /usr/share/doc/gavl-1.4.0/apiref/doxygen.svg
* /usr/share/doc/gavl-1.4.0/apiref/dynsections.js
* /usr/share/doc/gavl-1.4.0/apiref/files.html
* /usr/share/doc/gavl-1.4.0/apiref/folderclosed.png
* /usr/share/doc/gavl-1.4.0/apiref/folderopen.png
* /usr/share/doc/gavl-1.4.0/apiref/functions.html
* /usr/share/doc/gavl-1.4.0/apiref/functions_vars.html
* /usr/share/doc/gavl-1.4.0/apiref/gavldsp_8h_source.html
* /usr/share/doc/gavl-1.4.0/apiref/gavltime_8h_source.html
* /usr/share/doc/gavl-1.4.0/apiref/gavl_8h.html
* /usr/share/doc/gavl-1.4.0/apiref/gavl_8h_source.html
* /usr/share/doc/gavl-1.4.0/apiref/globals.html
* /usr/share/doc/gavl-1.4.0/apiref/globals_defs.html
* /usr/share/doc/gavl-1.4.0/apiref/globals_enum.html
* /usr/share/doc/gavl-1.4.0/apiref/globals_eval.html
* /usr/share/doc/gavl-1.4.0/apiref/globals_func.html
* /usr/share/doc/gavl-1.4.0/apiref/globals_type.html
* /usr/share/doc/gavl-1.4.0/apiref/group__accel__flags.html
* /usr/share/doc/gavl-1.4.0/apiref/group__audio.html
* /usr/share/doc/gavl-1.4.0/apiref/group__audio__conversion__flags.html
* /usr/share/doc/gavl-1.4.0/apiref/group__audio__converter.html
* /usr/share/doc/gavl-1.4.0/apiref/group__audio__format.html
* /usr/share/doc/gavl-1.4.0/apiref/group__audio__frame.html
* /usr/share/doc/gavl-1.4.0/apiref/group__audio__options.html
* /usr/share/doc/gavl-1.4.0/apiref/group__compression.html
* /usr/share/doc/gavl-1.4.0/apiref/group__dsp.html
* /usr/share/doc/gavl-1.4.0/apiref/group__dsputils.html
* /usr/share/doc/gavl-1.4.0/apiref/group__frame__table.html
* /usr/share/doc/gavl-1.4.0/apiref/group__metadata.html
* /usr/share/doc/gavl-1.4.0/apiref/group__metatags.html
* /usr/share/doc/gavl-1.4.0/apiref/group__mt.html
* /usr/share/doc/gavl-1.4.0/apiref/group__peak__detection.html
* /usr/share/doc/gavl-1.4.0/apiref/group__quality.html
* /usr/share/doc/gavl-1.4.0/apiref/group__rectangle.html
* /usr/share/doc/gavl-1.4.0/apiref/group__time.html
* /usr/share/doc/gavl-1.4.0/apiref/group__timecode.html
* /usr/share/doc/gavl-1.4.0/apiref/group__timer.html
* /usr/share/doc/gavl-1.4.0/apiref/group__video.html
* /usr/share/doc/gavl-1.4.0/apiref/group__video__blend.html
* /usr/share/doc/gavl-1.4.0/apiref/group__video__conversion__flags.html
* /usr/share/doc/gavl-1.4.0/apiref/group__video__converter.html
* /usr/share/doc/gavl-1.4.0/apiref/group__video__deinterlacer.html
* /usr/share/doc/gavl-1.4.0/apiref/group__video__format.html
* /usr/share/doc/gavl-1.4.0/apiref/group__video__frame.html
* /usr/share/doc/gavl-1.4.0/apiref/group__video__options.html
* /usr/share/doc/gavl-1.4.0/apiref/group__video__scaler.html
* /usr/share/doc/gavl-1.4.0/apiref/group__video__transform.html
* /usr/share/doc/gavl-1.4.0/apiref/group__volume__control.html
* /usr/share/doc/gavl-1.4.0/apiref/index.html
* /usr/share/doc/gavl-1.4.0/apiref/jquery.js
* /usr/share/doc/gavl-1.4.0/apiref/menu.js
* /usr/share/doc/gavl-1.4.0/apiref/menudata.js
* /usr/share/doc/gavl-1.4.0/apiref/metadata_8h_source.html
* /usr/share/doc/gavl-1.4.0/apiref/metatags_8h_source.html
* /usr/share/doc/gavl-1.4.0/apiref/modules.html
* /usr/share/doc/gavl-1.4.0/apiref/nav_f.png
* /usr/share/doc/gavl-1.4.0/apiref/nav_g.png
* /usr/share/doc/gavl-1.4.0/apiref/nav_h.png
* /usr/share/doc/gavl-1.4.0/apiref/open.png
* /usr/share/doc/gavl-1.4.0/apiref/splitbar.png
* /usr/share/doc/gavl-1.4.0/apiref/structgavl__audio__format__t.html
* /usr/share/doc/gavl-1.4.0/apiref/structgavl__audio__frame__t.html
* /usr/share/doc/gavl-1.4.0/apiref/structgavl__compression__info__t.html
* /usr/share/doc/gavl-1.4.0/apiref/structgavl__dsp__funcs__t.html
* /usr/share/doc/gavl-1.4.0/apiref/structgavl__frame__table__t.html
* /usr/share/doc/gavl-1.4.0/apiref/structgavl__metadata__t.html
* /usr/share/doc/gavl-1.4.0/apiref/structgavl__metadata__tag__t.html
* /usr/share/doc/gavl-1.4.0/apiref/structgavl__overlay__t.html
* /usr/share/doc/gavl-1.4.0/apiref/structgavl__packet__t.html
* /usr/share/doc/gavl-1.4.0/apiref/structgavl__rectangle__f__t.html
* /usr/share/doc/gavl-1.4.0/apiref/structgavl__rectangle__i__t.html
* /usr/share/doc/gavl-1.4.0/apiref/structgavl__timecode__format__t.html
* /usr/share/doc/gavl-1.4.0/apiref/structgavl__video__format__s.html
* /usr/share/doc/gavl-1.4.0/apiref/structgavl__video__frame__t.html
* /usr/share/doc/gavl-1.4.0/apiref/sync_off.png
* /usr/share/doc/gavl-1.4.0/apiref/sync_on.png
* /usr/share/doc/gavl-1.4.0/apiref/tabs.css
* /usr/share/doc/gavl-1.4.0/apiref/tab_a.png
* /usr/share/doc/gavl-1.4.0/apiref/tab_b.png
* /usr/share/doc/gavl-1.4.0/apiref/tab_h.png
* /usr/share/doc/gavl-1.4.0/apiref/tab_s.png
* /usr/share/doc/gavl-1.4.0/apiref/timecode_8h_source.html
* /usr/share/doc/gavl-1.4.0/apiref/uniongavl__audio__channels__t.html
* /usr/share/doc/gavl-1.4.0/apiref/uniongavl__audio__samples__t.html
* /usr/share/doc/gavl-1.4.0/AUTHORS
* /usr/share/doc/gavl-1.4.0/COPYING
* /usr/share/doc/gavl-1.4.0/INSTALL
* /usr/share/doc/gavl-1.4.0/README
* /usr/share/doc/gavl-1.4.0/TODO
{{< /files >}}