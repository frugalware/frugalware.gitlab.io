+++
draft = false
title = "frei0r-plugins 1.8.0-1"
version = "1.8.0-1"
description = "frei0r is a minimalistic plugin API for video sources and filters."
date = "2022-04-14T10:38:55"
aliases = "/packages/218264"
categories = ['xmultimedia-extra']
upstreamurl = "http://frei0r.dyne.org/"
arch = "x86_64"
size = "334964"
usize = "5759428"
sha1sum = "aad208cb92bcc3360f18be38c881c7d9b3e8eaf4"
depends = "['gavl>=1.4.0-3']"
reverse_depends = "['kamoso', 'mlt']"
+++
frei0r is a minimalistic plugin API for video sources and filters.{{< files text="show files" >}}* /usr/include/frei0r.h
* /usr/lib/frei0r-1/3dflippo.so
* /usr/lib/frei0r-1/addition.so
* /usr/lib/frei0r-1/addition_alpha.so
* /usr/lib/frei0r-1/aech0r.so
* /usr/lib/frei0r-1/alpha0ps.so
* /usr/lib/frei0r-1/alphaatop.so
* /usr/lib/frei0r-1/alphagrad.so
* /usr/lib/frei0r-1/alphain.so
* /usr/lib/frei0r-1/alphainjection.so
* /usr/lib/frei0r-1/alphaout.so
* /usr/lib/frei0r-1/alphaover.so
* /usr/lib/frei0r-1/alphaspot.so
* /usr/lib/frei0r-1/alphaxor.so
* /usr/lib/frei0r-1/B.so
* /usr/lib/frei0r-1/balanc0r.so
* /usr/lib/frei0r-1/baltan.so
* /usr/lib/frei0r-1/bgsubtract0r.so
* /usr/lib/frei0r-1/blend.so
* /usr/lib/frei0r-1/bluescreen0r.so
* /usr/lib/frei0r-1/brightness.so
* /usr/lib/frei0r-1/burn.so
* /usr/lib/frei0r-1/bw0r.so
* /usr/lib/frei0r-1/c0rners.so
* /usr/lib/frei0r-1/cartoon.so
* /usr/lib/frei0r-1/cluster.so
* /usr/lib/frei0r-1/colgate.so
* /usr/lib/frei0r-1/coloradj_RGB.so
* /usr/lib/frei0r-1/colordistance.so
* /usr/lib/frei0r-1/colorhalftone.so
* /usr/lib/frei0r-1/colorize.so
* /usr/lib/frei0r-1/colortap.so
* /usr/lib/frei0r-1/color_only.so
* /usr/lib/frei0r-1/composition.so
* /usr/lib/frei0r-1/contrast0r.so
* /usr/lib/frei0r-1/curves.so
* /usr/lib/frei0r-1/d90stairsteppingfix.so
* /usr/lib/frei0r-1/darken.so
* /usr/lib/frei0r-1/defish0r.so
* /usr/lib/frei0r-1/delay0r.so
* /usr/lib/frei0r-1/delaygrab.so
* /usr/lib/frei0r-1/difference.so
* /usr/lib/frei0r-1/distort0r.so
* /usr/lib/frei0r-1/dither.so
* /usr/lib/frei0r-1/divide.so
* /usr/lib/frei0r-1/dodge.so
* /usr/lib/frei0r-1/edgeglow.so
* /usr/lib/frei0r-1/elastic_scale.so
* /usr/lib/frei0r-1/emboss.so
* /usr/lib/frei0r-1/equaliz0r.so
* /usr/lib/frei0r-1/flippo.so
* /usr/lib/frei0r-1/G.so
* /usr/lib/frei0r-1/gamma.so
* /usr/lib/frei0r-1/glitch0r.so
* /usr/lib/frei0r-1/glow.so
* /usr/lib/frei0r-1/grain_extract.so
* /usr/lib/frei0r-1/grain_merge.so
* /usr/lib/frei0r-1/hardlight.so
* /usr/lib/frei0r-1/hqdn3d.so
* /usr/lib/frei0r-1/hue.so
* /usr/lib/frei0r-1/hueshift0r.so
* /usr/lib/frei0r-1/IIRblur.so
* /usr/lib/frei0r-1/invert0r.so
* /usr/lib/frei0r-1/ising0r.so
* /usr/lib/frei0r-1/keyspillm0pup.so
* /usr/lib/frei0r-1/lenscorrection.so
* /usr/lib/frei0r-1/letterb0xed.so
* /usr/lib/frei0r-1/levels.so
* /usr/lib/frei0r-1/lighten.so
* /usr/lib/frei0r-1/lightgraffiti.so
* /usr/lib/frei0r-1/lissajous0r.so
* /usr/lib/frei0r-1/luminance.so
* /usr/lib/frei0r-1/mask0mate.so
* /usr/lib/frei0r-1/medians.so
* /usr/lib/frei0r-1/multiply.so
* /usr/lib/frei0r-1/ndvi.so
* /usr/lib/frei0r-1/nervous.so
* /usr/lib/frei0r-1/nois0r.so
* /usr/lib/frei0r-1/normaliz0r.so
* /usr/lib/frei0r-1/nosync0r.so
* /usr/lib/frei0r-1/onecol0r.so
* /usr/lib/frei0r-1/overlay.so
* /usr/lib/frei0r-1/partik0l.so
* /usr/lib/frei0r-1/perspective.so
* /usr/lib/frei0r-1/pixeliz0r.so
* /usr/lib/frei0r-1/plasma.so
* /usr/lib/frei0r-1/posterize.so
* /usr/lib/frei0r-1/pr0be.so
* /usr/lib/frei0r-1/pr0file.so
* /usr/lib/frei0r-1/premultiply.so
* /usr/lib/frei0r-1/primaries.so
* /usr/lib/frei0r-1/R.so
* /usr/lib/frei0r-1/RGB.so
* /usr/lib/frei0r-1/rgbnoise.so
* /usr/lib/frei0r-1/rgbparade.so
* /usr/lib/frei0r-1/rgbsplit0r.so
* /usr/lib/frei0r-1/saturat0r.so
* /usr/lib/frei0r-1/saturation.so
* /usr/lib/frei0r-1/scale0tilt.so
* /usr/lib/frei0r-1/scanline0r.so
* /usr/lib/frei0r-1/screen.so
* /usr/lib/frei0r-1/select0r.so
* /usr/lib/frei0r-1/sharpness.so
* /usr/lib/frei0r-1/sigmoidaltransfer.so
* /usr/lib/frei0r-1/sobel.so
* /usr/lib/frei0r-1/softglow.so
* /usr/lib/frei0r-1/softlight.so
* /usr/lib/frei0r-1/sopsat.so
* /usr/lib/frei0r-1/spillsupress.so
* /usr/lib/frei0r-1/squareblur.so
* /usr/lib/frei0r-1/subtract.so
* /usr/lib/frei0r-1/tehRoxx0r.so
* /usr/lib/frei0r-1/test_pat_B.so
* /usr/lib/frei0r-1/test_pat_C.so
* /usr/lib/frei0r-1/test_pat_G.so
* /usr/lib/frei0r-1/test_pat_I.so
* /usr/lib/frei0r-1/test_pat_L.so
* /usr/lib/frei0r-1/test_pat_R.so
* /usr/lib/frei0r-1/threelay0r.so
* /usr/lib/frei0r-1/three_point_balance.so
* /usr/lib/frei0r-1/threshold0r.so
* /usr/lib/frei0r-1/timeout.so
* /usr/lib/frei0r-1/tint0r.so
* /usr/lib/frei0r-1/transparency.so
* /usr/lib/frei0r-1/twolay0r.so
* /usr/lib/frei0r-1/uvmap.so
* /usr/lib/frei0r-1/value.so
* /usr/lib/frei0r-1/vectorscope.so
* /usr/lib/frei0r-1/vertigo.so
* /usr/lib/frei0r-1/vignette.so
* /usr/lib/frei0r-1/xfade0r.so
* /usr/lib/pkgconfig/frei0r.pc
* /usr/share/doc/frei0r-plugins-1.8.0/COPYING.txt
* /usr/share/doc/frei0r-plugins-1.8.0/INSTALL.txt
* /usr/share/doc/frei0r-plugins-1.8.0/README.txt
{{< /files >}}