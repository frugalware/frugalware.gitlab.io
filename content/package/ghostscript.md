+++
draft = false
title = "ghostscript 10.02.1-1"
version = "10.02.1-1"
date = "2023-11-07T15:19:13"
categories = ['apps']
upstreamurl = "https://www.ghostscript.com/"
arch = "x86_64"
size = "18173800"
usize = "28435429"
sha1sum = "c6e15fb681fee0486d902214eb77a13a503212d3"
depends = "['libcups', 'lcms2', 'libpaper', 'fontconfig', 'zlib>=1.2.12', 'libpng', 'libjpeg-turbo', 'libtiff', 'ijs', 'jasper', 'openjpeg', 'libgs', 'foomatic-filters>=4.0.17-5']"
license = "GPLv2"
files = "['usr/', 'usr/bin/', 'usr/bin/dvipdf', 'usr/bin/eps2eps', 'usr/bin/gs', 'usr/bin/gsbj', 'usr/bin/gsc', 'usr/bin/gsdj', 'usr/bin/gsdj500', 'usr/bin/gslj', 'usr/bin/gslp', 'usr/bin/gsnd', 'usr/bin/lprsetup.sh', 'usr/bin/pdf2dsc', 'usr/bin/pdf2ps', 'usr/bin/pf2afm', 'usr/bin/pfbtopfa', 'usr/bin/pphs', 'usr/bin/printafm', 'usr/bin/ps2ascii', 'usr/bin/ps2epsi', 'usr/bin/ps2pdf', 'usr/bin/ps2pdf12', 'usr/bin/ps2pdf13', 'usr/bin/ps2pdf14', 'usr/bin/ps2pdfwr', 'usr/bin/ps2ps', 'usr/bin/ps2ps2', 'usr/bin/unix-lpr.sh', 'usr/include/', 'usr/include/ghostscript/', 'usr/include/ghostscript/gdevdsp.h', 'usr/include/ghostscript/gserrors.h', 'usr/include/ghostscript/iapi.h', 'usr/include/ghostscript/ierrors.h', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/ghostscript-10.02.1/', 'usr/share/doc/ghostscript-10.02.1/10.02.1/', 'usr/share/doc/ghostscript-10.02.1/10.02.1/COPYING', 'usr/share/doc/ghostscript-10.02.1/10.02.1/GS9_Color_Management.pdf', 'usr/share/doc/ghostscript-10.02.1/10.02.1/Ghostscript.pdf', 'usr/share/doc/ghostscript-10.02.1/10.02.1/News.html', 'usr/share/doc/ghostscript-10.02.1/LICENSE', 'usr/share/ghostscript/', 'usr/share/ghostscript/10.02.1/', 'usr/share/ghostscript/10.02.1/Resource/', 'usr/share/ghostscript/10.02.1/Resource/CIDFSubst/', 'usr/share/ghostscript/10.02.1/Resource/CIDFSubst/DroidSansFallback.ttf', 'usr/share/ghostscript/10.02.1/Resource/CIDFont/', 'usr/share/ghostscript/10.02.1/Resource/CIDFont/ArtifexBullet', 'usr/share/ghostscript/10.02.1/Resource/CMap/', 'usr/share/ghostscript/10.02.1/Resource/CMap/78-EUC-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/78-EUC-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/78-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/78-RKSJ-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/78-RKSJ-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/78-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/78ms-RKSJ-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/78ms-RKSJ-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/83pv-RKSJ-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/90ms-RKSJ-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/90ms-RKSJ-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/90msp-RKSJ-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/90msp-RKSJ-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/90pv-RKSJ-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/90pv-RKSJ-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/Add-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/Add-RKSJ-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/Add-RKSJ-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/Add-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-CNS1-0', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-CNS1-1', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-CNS1-2', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-CNS1-3', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-CNS1-4', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-CNS1-5', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-CNS1-6', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-CNS1-7', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-GB1-0', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-GB1-1', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-GB1-2', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-GB1-3', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-GB1-4', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-GB1-5', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-Japan1-0', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-Japan1-1', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-Japan1-2', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-Japan1-3', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-Japan1-4', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-Japan1-5', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-Japan1-6', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-Japan2-0', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-Korea1-0', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-Korea1-1', 'usr/share/ghostscript/10.02.1/Resource/CMap/Adobe-Korea1-2', 'usr/share/ghostscript/10.02.1/Resource/CMap/B5-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/B5-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/B5pc-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/B5pc-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/CNS-EUC-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/CNS-EUC-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/CNS1-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/CNS1-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/CNS2-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/CNS2-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/ETHK-B5-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/ETHK-B5-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/ETen-B5-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/ETen-B5-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/ETenms-B5-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/ETenms-B5-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/EUC-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/EUC-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/Ext-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/Ext-RKSJ-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/Ext-RKSJ-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/Ext-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/GB-EUC-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/GB-EUC-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/GB-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/GB-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/GBK-EUC-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/GBK-EUC-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/GBK2K-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/GBK2K-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/GBKp-EUC-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/GBKp-EUC-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/GBT-EUC-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/GBT-EUC-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/GBT-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/GBT-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/GBTpc-EUC-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/GBTpc-EUC-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/GBpc-EUC-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/GBpc-EUC-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/H', 'usr/share/ghostscript/10.02.1/Resource/CMap/HKdla-B5-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/HKdla-B5-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/HKdlb-B5-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/HKdlb-B5-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/HKgccs-B5-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/HKgccs-B5-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/HKm314-B5-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/HKm314-B5-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/HKm471-B5-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/HKm471-B5-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/HKscs-B5-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/HKscs-B5-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/Hankaku', 'usr/share/ghostscript/10.02.1/Resource/CMap/Hiragana', 'usr/share/ghostscript/10.02.1/Resource/CMap/Hojo-EUC-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/Hojo-EUC-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/Hojo-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/Hojo-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/Identity-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/Identity-UTF16-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/Identity-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/KSC-EUC-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/KSC-EUC-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/KSC-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/KSC-Johab-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/KSC-Johab-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/KSC-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/KSCms-UHC-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/KSCms-UHC-HW-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/KSCms-UHC-HW-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/KSCms-UHC-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/KSCpc-EUC-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/KSCpc-EUC-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/Katakana', 'usr/share/ghostscript/10.02.1/Resource/CMap/NWP-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/NWP-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/RKSJ-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/RKSJ-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/Roman', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniCNS-UCS2-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniCNS-UCS2-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniCNS-UTF16-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniCNS-UTF16-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniCNS-UTF32-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniCNS-UTF32-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniCNS-UTF8-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniCNS-UTF8-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniGB-UCS2-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniGB-UCS2-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniGB-UTF16-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniGB-UTF16-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniGB-UTF32-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniGB-UTF32-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniGB-UTF8-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniGB-UTF8-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniHojo-UCS2-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniHojo-UCS2-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniHojo-UTF16-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniHojo-UTF16-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniHojo-UTF32-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniHojo-UTF32-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniHojo-UTF8-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniHojo-UTF8-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJIS-UCS2-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJIS-UCS2-HW-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJIS-UCS2-HW-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJIS-UCS2-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJIS-UTF16-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJIS-UTF16-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJIS-UTF32-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJIS-UTF32-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJIS-UTF8-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJIS-UTF8-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJIS2004-UTF16-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJIS2004-UTF16-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJIS2004-UTF32-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJIS2004-UTF32-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJIS2004-UTF8-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJIS2004-UTF8-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJISPro-UCS2-HW-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJISPro-UCS2-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJISPro-UTF8-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJISX0213-UTF32-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJISX0213-UTF32-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJISX02132004-UTF32-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniJISX02132004-UTF32-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniKS-UCS2-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniKS-UCS2-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniKS-UTF16-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniKS-UTF16-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniKS-UTF32-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniKS-UTF32-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniKS-UTF8-H', 'usr/share/ghostscript/10.02.1/Resource/CMap/UniKS-UTF8-V', 'usr/share/ghostscript/10.02.1/Resource/CMap/V', 'usr/share/ghostscript/10.02.1/Resource/CMap/WP-Symbol', 'usr/share/ghostscript/10.02.1/Resource/ColorSpace/', 'usr/share/ghostscript/10.02.1/Resource/ColorSpace/DefaultCMYK', 'usr/share/ghostscript/10.02.1/Resource/ColorSpace/DefaultGray', 'usr/share/ghostscript/10.02.1/Resource/ColorSpace/DefaultRGB', 'usr/share/ghostscript/10.02.1/Resource/ColorSpace/TrivialCMYK', 'usr/share/ghostscript/10.02.1/Resource/ColorSpace/sGray', 'usr/share/ghostscript/10.02.1/Resource/ColorSpace/sRGB', 'usr/share/ghostscript/10.02.1/Resource/Decoding/', 'usr/share/ghostscript/10.02.1/Resource/Decoding/FCO_Dingbats', 'usr/share/ghostscript/10.02.1/Resource/Decoding/FCO_Symbol', 'usr/share/ghostscript/10.02.1/Resource/Decoding/FCO_Unicode', 'usr/share/ghostscript/10.02.1/Resource/Decoding/FCO_Wingdings', 'usr/share/ghostscript/10.02.1/Resource/Decoding/Latin1', 'usr/share/ghostscript/10.02.1/Resource/Decoding/StandardEncoding', 'usr/share/ghostscript/10.02.1/Resource/Decoding/Unicode', 'usr/share/ghostscript/10.02.1/Resource/Encoding/', 'usr/share/ghostscript/10.02.1/Resource/Encoding/CEEncoding', 'usr/share/ghostscript/10.02.1/Resource/Encoding/ExpertEncoding', 'usr/share/ghostscript/10.02.1/Resource/Encoding/ExpertSubsetEncoding', 'usr/share/ghostscript/10.02.1/Resource/Encoding/NotDefEncoding', 'usr/share/ghostscript/10.02.1/Resource/Encoding/Wingdings', 'usr/share/ghostscript/10.02.1/Resource/Font/', 'usr/share/ghostscript/10.02.1/Resource/Font/C059-BdIta', 'usr/share/ghostscript/10.02.1/Resource/Font/C059-Bold', 'usr/share/ghostscript/10.02.1/Resource/Font/C059-Italic', 'usr/share/ghostscript/10.02.1/Resource/Font/C059-Roman', 'usr/share/ghostscript/10.02.1/Resource/Font/D050000L', 'usr/share/ghostscript/10.02.1/Resource/Font/NimbusMonoPS-Bold', 'usr/share/ghostscript/10.02.1/Resource/Font/NimbusMonoPS-BoldItalic', 'usr/share/ghostscript/10.02.1/Resource/Font/NimbusMonoPS-Italic', 'usr/share/ghostscript/10.02.1/Resource/Font/NimbusMonoPS-Regular', 'usr/share/ghostscript/10.02.1/Resource/Font/NimbusRoman-Bold', 'usr/share/ghostscript/10.02.1/Resource/Font/NimbusRoman-BoldItalic', 'usr/share/ghostscript/10.02.1/Resource/Font/NimbusRoman-Italic', 'usr/share/ghostscript/10.02.1/Resource/Font/NimbusRoman-Regular', 'usr/share/ghostscript/10.02.1/Resource/Font/NimbusSans-Bold', 'usr/share/ghostscript/10.02.1/Resource/Font/NimbusSans-BoldItalic', 'usr/share/ghostscript/10.02.1/Resource/Font/NimbusSans-Italic', 'usr/share/ghostscript/10.02.1/Resource/Font/NimbusSans-Regular', 'usr/share/ghostscript/10.02.1/Resource/Font/NimbusSansNarrow-Bold', 'usr/share/ghostscript/10.02.1/Resource/Font/NimbusSansNarrow-BoldOblique', 'usr/share/ghostscript/10.02.1/Resource/Font/NimbusSansNarrow-Oblique', 'usr/share/ghostscript/10.02.1/Resource/Font/NimbusSansNarrow-Regular', 'usr/share/ghostscript/10.02.1/Resource/Font/P052-Bold', 'usr/share/ghostscript/10.02.1/Resource/Font/P052-BoldItalic', 'usr/share/ghostscript/10.02.1/Resource/Font/P052-Italic', 'usr/share/ghostscript/10.02.1/Resource/Font/P052-Roman', 'usr/share/ghostscript/10.02.1/Resource/Font/StandardSymbolsPS', 'usr/share/ghostscript/10.02.1/Resource/Font/URWBookman-Demi', 'usr/share/ghostscript/10.02.1/Resource/Font/URWBookman-DemiItalic', 'usr/share/ghostscript/10.02.1/Resource/Font/URWBookman-Light', 'usr/share/ghostscript/10.02.1/Resource/Font/URWBookman-LightItalic', 'usr/share/ghostscript/10.02.1/Resource/Font/URWGothic-Book', 'usr/share/ghostscript/10.02.1/Resource/Font/URWGothic-BookOblique', 'usr/share/ghostscript/10.02.1/Resource/Font/URWGothic-Demi', 'usr/share/ghostscript/10.02.1/Resource/Font/URWGothic-DemiOblique', 'usr/share/ghostscript/10.02.1/Resource/Font/Z003-MediumItalic', 'usr/share/ghostscript/10.02.1/Resource/IdiomSet/', 'usr/share/ghostscript/10.02.1/Resource/IdiomSet/PPI_CUtils', 'usr/share/ghostscript/10.02.1/Resource/IdiomSet/Pscript5Idiom', 'usr/share/ghostscript/10.02.1/Resource/Init/', 'usr/share/ghostscript/10.02.1/Resource/Init/FAPIcidfmap', 'usr/share/ghostscript/10.02.1/Resource/Init/FAPIconfig', 'usr/share/ghostscript/10.02.1/Resource/Init/FAPIfontmap', 'usr/share/ghostscript/10.02.1/Resource/Init/FCOfontmap-PCLPS2', 'usr/share/ghostscript/10.02.1/Resource/Init/Fontmap', 'usr/share/ghostscript/10.02.1/Resource/Init/Fontmap.GS', 'usr/share/ghostscript/10.02.1/Resource/Init/cidfmap', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_agl.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_btokn.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_cet.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_cff.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_cidcm.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_ciddc.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_cidfm.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_cidfn.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_cidtt.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_cmap.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_cspace.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_dbt_e.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_diskn.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_dps1.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_dps2.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_dscp.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_epsf.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_fapi.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_fntem.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_fonts.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_frsd.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_icc.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_il1_e.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_img.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_init.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_lev2.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_ll3.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_mex_e.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_mgl_e.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_mro_e.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_pdf_e.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_pdfwr.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_res.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_resmp.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_setpd.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_statd.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_std_e.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_sym_e.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_trap.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_ttf.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_typ32.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_typ42.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_type1.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/gs_wan_e.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/pdf_main.ps', 'usr/share/ghostscript/10.02.1/Resource/Init/xlatmap', 'usr/share/ghostscript/10.02.1/Resource/SubstCID/', 'usr/share/ghostscript/10.02.1/Resource/SubstCID/CNS1-WMode', 'usr/share/ghostscript/10.02.1/Resource/SubstCID/GB1-WMode', 'usr/share/ghostscript/10.02.1/Resource/SubstCID/Japan1-WMode', 'usr/share/ghostscript/10.02.1/Resource/SubstCID/Korea1-WMode', 'usr/share/ghostscript/10.02.1/iccprofiles/', 'usr/share/ghostscript/10.02.1/iccprofiles/a98.icc', 'usr/share/ghostscript/10.02.1/iccprofiles/default_cmyk.icc', 'usr/share/ghostscript/10.02.1/iccprofiles/default_gray.icc', 'usr/share/ghostscript/10.02.1/iccprofiles/default_rgb.icc', 'usr/share/ghostscript/10.02.1/iccprofiles/esrgb.icc', 'usr/share/ghostscript/10.02.1/iccprofiles/gray_to_k.icc', 'usr/share/ghostscript/10.02.1/iccprofiles/lab.icc', 'usr/share/ghostscript/10.02.1/iccprofiles/ps_cmyk.icc', 'usr/share/ghostscript/10.02.1/iccprofiles/ps_gray.icc', 'usr/share/ghostscript/10.02.1/iccprofiles/ps_rgb.icc', 'usr/share/ghostscript/10.02.1/iccprofiles/rommrgb.icc', 'usr/share/ghostscript/10.02.1/iccprofiles/scrgb.icc', 'usr/share/ghostscript/10.02.1/iccprofiles/sgray.icc', 'usr/share/ghostscript/10.02.1/iccprofiles/srgb.icc', 'usr/share/ghostscript/10.02.1/lib/', 'usr/share/ghostscript/10.02.1/lib/PDFA_def.ps', 'usr/share/ghostscript/10.02.1/lib/PDFX_def.ps', 'usr/share/ghostscript/10.02.1/lib/PM760p.upp', 'usr/share/ghostscript/10.02.1/lib/PM760pl.upp', 'usr/share/ghostscript/10.02.1/lib/PM820p.upp', 'usr/share/ghostscript/10.02.1/lib/PM820pl.upp', 'usr/share/ghostscript/10.02.1/lib/Stc670p.upp', 'usr/share/ghostscript/10.02.1/lib/Stc670pl.upp', 'usr/share/ghostscript/10.02.1/lib/Stc680p.upp', 'usr/share/ghostscript/10.02.1/lib/Stc680pl.upp', 'usr/share/ghostscript/10.02.1/lib/Stc740p.upp', 'usr/share/ghostscript/10.02.1/lib/Stc740pl.upp', 'usr/share/ghostscript/10.02.1/lib/Stc760p.upp', 'usr/share/ghostscript/10.02.1/lib/Stc760pl.upp', 'usr/share/ghostscript/10.02.1/lib/Stc777p.upp', 'usr/share/ghostscript/10.02.1/lib/Stc777pl.upp', 'usr/share/ghostscript/10.02.1/lib/Stp720p.upp', 'usr/share/ghostscript/10.02.1/lib/Stp720pl.upp', 'usr/share/ghostscript/10.02.1/lib/Stp870p.upp', 'usr/share/ghostscript/10.02.1/lib/Stp870pl.upp', 'usr/share/ghostscript/10.02.1/lib/acctest.ps', 'usr/share/ghostscript/10.02.1/lib/align.ps', 'usr/share/ghostscript/10.02.1/lib/bj8.rpd', 'usr/share/ghostscript/10.02.1/lib/bj8gc12f.upp', 'usr/share/ghostscript/10.02.1/lib/bj8hg12f.upp', 'usr/share/ghostscript/10.02.1/lib/bj8oh06n.upp', 'usr/share/ghostscript/10.02.1/lib/bj8pa06n.upp', 'usr/share/ghostscript/10.02.1/lib/bj8pp12f.upp', 'usr/share/ghostscript/10.02.1/lib/bj8ts06n.upp', 'usr/share/ghostscript/10.02.1/lib/bjc6000a1.upp', 'usr/share/ghostscript/10.02.1/lib/bjc6000b1.upp', 'usr/share/ghostscript/10.02.1/lib/bjc610a0.upp', 'usr/share/ghostscript/10.02.1/lib/bjc610a1.upp', 'usr/share/ghostscript/10.02.1/lib/bjc610a2.upp', 'usr/share/ghostscript/10.02.1/lib/bjc610a3.upp', 'usr/share/ghostscript/10.02.1/lib/bjc610a4.upp', 'usr/share/ghostscript/10.02.1/lib/bjc610a5.upp', 'usr/share/ghostscript/10.02.1/lib/bjc610a6.upp', 'usr/share/ghostscript/10.02.1/lib/bjc610a7.upp', 'usr/share/ghostscript/10.02.1/lib/bjc610a8.upp', 'usr/share/ghostscript/10.02.1/lib/bjc610b1.upp', 'usr/share/ghostscript/10.02.1/lib/bjc610b2.upp', 'usr/share/ghostscript/10.02.1/lib/bjc610b3.upp', 'usr/share/ghostscript/10.02.1/lib/bjc610b4.upp', 'usr/share/ghostscript/10.02.1/lib/bjc610b6.upp', 'usr/share/ghostscript/10.02.1/lib/bjc610b7.upp', 'usr/share/ghostscript/10.02.1/lib/bjc610b8.upp', 'usr/share/ghostscript/10.02.1/lib/caption.ps', 'usr/share/ghostscript/10.02.1/lib/cbjc600.ppd', 'usr/share/ghostscript/10.02.1/lib/cbjc800.ppd', 'usr/share/ghostscript/10.02.1/lib/cdj550.upp', 'usr/share/ghostscript/10.02.1/lib/cdj690.upp', 'usr/share/ghostscript/10.02.1/lib/cdj690ec.upp', 'usr/share/ghostscript/10.02.1/lib/cid2code.ps', 'usr/share/ghostscript/10.02.1/lib/dnj750c.upp', 'usr/share/ghostscript/10.02.1/lib/dnj750m.upp', 'usr/share/ghostscript/10.02.1/lib/docie.ps', 'usr/share/ghostscript/10.02.1/lib/font2pcl.ps', 'usr/share/ghostscript/10.02.1/lib/ghostpdf.ppd', 'usr/share/ghostscript/10.02.1/lib/gs_ce_e.ps', 'usr/share/ghostscript/10.02.1/lib/gs_css_e.ps', 'usr/share/ghostscript/10.02.1/lib/gs_il2_e.ps', 'usr/share/ghostscript/10.02.1/lib/gs_kanji.ps', 'usr/share/ghostscript/10.02.1/lib/gs_ksb_e.ps', 'usr/share/ghostscript/10.02.1/lib/gs_l.xbm', 'usr/share/ghostscript/10.02.1/lib/gs_l.xpm', 'usr/share/ghostscript/10.02.1/lib/gs_l_m.xbm', 'usr/share/ghostscript/10.02.1/lib/gs_lgo_e.ps', 'usr/share/ghostscript/10.02.1/lib/gs_lgx_e.ps', 'usr/share/ghostscript/10.02.1/lib/gs_m.xbm', 'usr/share/ghostscript/10.02.1/lib/gs_m.xpm', 'usr/share/ghostscript/10.02.1/lib/gs_m_m.xbm', 'usr/share/ghostscript/10.02.1/lib/gs_s.xbm', 'usr/share/ghostscript/10.02.1/lib/gs_s.xpm', 'usr/share/ghostscript/10.02.1/lib/gs_s_m.xbm', 'usr/share/ghostscript/10.02.1/lib/gs_t.xbm', 'usr/share/ghostscript/10.02.1/lib/gs_t.xpm', 'usr/share/ghostscript/10.02.1/lib/gs_t_m.xbm', 'usr/share/ghostscript/10.02.1/lib/gs_wl1_e.ps', 'usr/share/ghostscript/10.02.1/lib/gs_wl2_e.ps', 'usr/share/ghostscript/10.02.1/lib/gs_wl5_e.ps', 'usr/share/ghostscript/10.02.1/lib/gslp.ps', 'usr/share/ghostscript/10.02.1/lib/gsnup.ps', 'usr/share/ghostscript/10.02.1/lib/ht_ccsto.ps', 'usr/share/ghostscript/10.02.1/lib/image-qa.ps', 'usr/share/ghostscript/10.02.1/lib/jispaper.ps', 'usr/share/ghostscript/10.02.1/lib/landscap.ps', 'usr/share/ghostscript/10.02.1/lib/lines.ps', 'usr/share/ghostscript/10.02.1/lib/mkcidfm.ps', 'usr/share/ghostscript/10.02.1/lib/necp2x.upp', 'usr/share/ghostscript/10.02.1/lib/necp2x6.upp', 'usr/share/ghostscript/10.02.1/lib/pdf2dsc.ps', 'usr/share/ghostscript/10.02.1/lib/pdf_info.ps', 'usr/share/ghostscript/10.02.1/lib/pf2afm.ps', 'usr/share/ghostscript/10.02.1/lib/pfbtopfa.ps', 'usr/share/ghostscript/10.02.1/lib/ppath.ps', 'usr/share/ghostscript/10.02.1/lib/pphs.ps', 'usr/share/ghostscript/10.02.1/lib/prfont.ps', 'usr/share/ghostscript/10.02.1/lib/printafm.ps', 'usr/share/ghostscript/10.02.1/lib/ps2ai.ps', 'usr/share/ghostscript/10.02.1/lib/ps2epsi.ps', 'usr/share/ghostscript/10.02.1/lib/ras1.upp', 'usr/share/ghostscript/10.02.1/lib/ras24.upp', 'usr/share/ghostscript/10.02.1/lib/ras3.upp', 'usr/share/ghostscript/10.02.1/lib/ras32.upp', 'usr/share/ghostscript/10.02.1/lib/ras4.upp', 'usr/share/ghostscript/10.02.1/lib/ras8m.upp', 'usr/share/ghostscript/10.02.1/lib/rollconv.ps', 'usr/share/ghostscript/10.02.1/lib/s400a1.upp', 'usr/share/ghostscript/10.02.1/lib/s400b1.upp', 'usr/share/ghostscript/10.02.1/lib/sharp.upp', 'usr/share/ghostscript/10.02.1/lib/sipixa6.upp', 'usr/share/ghostscript/10.02.1/lib/st640ih.upp', 'usr/share/ghostscript/10.02.1/lib/st640ihg.upp', 'usr/share/ghostscript/10.02.1/lib/st640p.upp', 'usr/share/ghostscript/10.02.1/lib/st640pg.upp', 'usr/share/ghostscript/10.02.1/lib/st640pl.upp', 'usr/share/ghostscript/10.02.1/lib/st640plg.upp', 'usr/share/ghostscript/10.02.1/lib/stc.upp', 'usr/share/ghostscript/10.02.1/lib/stc1520h.upp', 'usr/share/ghostscript/10.02.1/lib/stc2.upp', 'usr/share/ghostscript/10.02.1/lib/stc200_h.upp', 'usr/share/ghostscript/10.02.1/lib/stc2_h.upp', 'usr/share/ghostscript/10.02.1/lib/stc2s_h.upp', 'usr/share/ghostscript/10.02.1/lib/stc300.upp', 'usr/share/ghostscript/10.02.1/lib/stc300bl.upp', 'usr/share/ghostscript/10.02.1/lib/stc300bm.upp', 'usr/share/ghostscript/10.02.1/lib/stc500p.upp', 'usr/share/ghostscript/10.02.1/lib/stc500ph.upp', 'usr/share/ghostscript/10.02.1/lib/stc600ih.upp', 'usr/share/ghostscript/10.02.1/lib/stc600p.upp', 'usr/share/ghostscript/10.02.1/lib/stc600pl.upp', 'usr/share/ghostscript/10.02.1/lib/stc640p.upp', 'usr/share/ghostscript/10.02.1/lib/stc740ih.upp', 'usr/share/ghostscript/10.02.1/lib/stc800ih.upp', 'usr/share/ghostscript/10.02.1/lib/stc800p.upp', 'usr/share/ghostscript/10.02.1/lib/stc800pl.upp', 'usr/share/ghostscript/10.02.1/lib/stc_h.upp', 'usr/share/ghostscript/10.02.1/lib/stc_l.upp', 'usr/share/ghostscript/10.02.1/lib/stcany.upp', 'usr/share/ghostscript/10.02.1/lib/stcany_h.upp', 'usr/share/ghostscript/10.02.1/lib/stcinfo.ps', 'usr/share/ghostscript/10.02.1/lib/stcolor.ps', 'usr/share/ghostscript/10.02.1/lib/stocht.ps', 'usr/share/ghostscript/10.02.1/lib/traceimg.ps', 'usr/share/ghostscript/10.02.1/lib/traceop.ps', 'usr/share/ghostscript/10.02.1/lib/uninfo.ps', 'usr/share/ghostscript/10.02.1/lib/viewcmyk.ps', 'usr/share/ghostscript/10.02.1/lib/viewgif.ps', 'usr/share/ghostscript/10.02.1/lib/viewjpeg.ps', 'usr/share/ghostscript/10.02.1/lib/viewmiff.ps', 'usr/share/ghostscript/10.02.1/lib/viewpbm.ps', 'usr/share/ghostscript/10.02.1/lib/viewpcx.ps', 'usr/share/ghostscript/10.02.1/lib/viewps2a.ps', 'usr/share/ghostscript/10.02.1/lib/winmaps.ps', 'usr/share/ghostscript/10.02.1/lib/zeroline.ps', 'usr/share/man/', 'usr/share/man/man1/', 'usr/share/man/man1/dvipdf.1.gz', 'usr/share/man/man1/eps2eps.1.gz', 'usr/share/man/man1/gs.1.gz', 'usr/share/man/man1/gsbj.1.gz', 'usr/share/man/man1/gsdj.1.gz', 'usr/share/man/man1/gsdj500.1.gz', 'usr/share/man/man1/gslj.1.gz', 'usr/share/man/man1/gslp.1.gz', 'usr/share/man/man1/gsnd.1.gz', 'usr/share/man/man1/pdf2dsc.1.gz', 'usr/share/man/man1/pdf2ps.1.gz', 'usr/share/man/man1/pf2afm.1.gz', 'usr/share/man/man1/pfbtopfa.1.gz', 'usr/share/man/man1/printafm.1.gz', 'usr/share/man/man1/ps2ascii.1.gz', 'usr/share/man/man1/ps2epsi.1.gz', 'usr/share/man/man1/ps2pdf.1.gz', 'usr/share/man/man1/ps2pdf12.1.gz', 'usr/share/man/man1/ps2pdf13.1.gz', 'usr/share/man/man1/ps2pdf14.1.gz', 'usr/share/man/man1/ps2pdfwr.1.gz', 'usr/share/man/man1/ps2ps.1.gz']"
+++
An interpreter for the PostScript language.