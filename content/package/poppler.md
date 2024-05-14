+++
draft = false
title = "poppler 24.05.0-1"
version = "24.05.0-1"
description = "A PDF rendering library"
date = "2024-05-02T09:13:39"
aliases = "/packages/3295"
categories = ['xlib']
upstreamurl = "https://poppler.freedesktop.org/"
arch = "x86_64"
size = "1968864"
usize = "9977305"
sha1sum = "50cbebc1370ae33ee674bc056f5472a8cca86b4e"
depends = "['cairo>=1.14.6-4', 'curl', 'fontconfig>=2.12-2', 'libgpgmepp', 'libjpeg-turbo', 'libpng>=1.6.25', 'libstdc++>=9.1.0-3', 'nss', 'openjpeg>=2.2.0', 'poppler-data', 'poppler-data']"
reverse_depends = "['efl', 'kitinerary', 'libcupsfilters', 'poppler-glib', 'poppler-pdftools', 'poppler-qt5', 'poppler-qt6', 'scribus', 'texlive']"
+++
### Description: 
A PDF rendering library

### Files: 
* /etc/fonts/conf.avail/01-poppler.conf
* /etc/fonts/conf.d/01-poppler.conf
* /usr/include/poppler/Annot.h
* /usr/include/poppler/AnnotStampImageHelper.h
* /usr/include/poppler/Array.h
* /usr/include/poppler/BBoxOutputDev.h
* /usr/include/poppler/CachedFile.h
* /usr/include/poppler/CairoFontEngine.h
* /usr/include/poppler/CairoOutputDev.h
* /usr/include/poppler/CairoRescaleBox.h
* /usr/include/poppler/Catalog.h
* /usr/include/poppler/CertificateInfo.h
* /usr/include/poppler/CharCodeToUnicode.h
* /usr/include/poppler/CharTypes.h
* /usr/include/poppler/CMap.h
* /usr/include/poppler/cpp/poppler-destination.h
* /usr/include/poppler/cpp/poppler-document.h
* /usr/include/poppler/cpp/poppler-embedded-file.h
* /usr/include/poppler/cpp/poppler-font-private.h
* /usr/include/poppler/cpp/poppler-font.h
* /usr/include/poppler/cpp/poppler-global.h
* /usr/include/poppler/cpp/poppler-image.h
* /usr/include/poppler/cpp/poppler-page-renderer.h
* /usr/include/poppler/cpp/poppler-page-transition.h
* /usr/include/poppler/cpp/poppler-page.h
* /usr/include/poppler/cpp/poppler-rectangle.h
* /usr/include/poppler/cpp/poppler-toc.h
* /usr/include/poppler/cpp/poppler-version.h
* /usr/include/poppler/cpp/poppler_cpp_export.h
* /usr/include/poppler/CurlCachedFile.h
* /usr/include/poppler/CurlPDFDocBuilder.h
* /usr/include/poppler/DateInfo.h
* /usr/include/poppler/Decrypt.h
* /usr/include/poppler/Dict.h
* /usr/include/poppler/Error.h
* /usr/include/poppler/ErrorCodes.h
* /usr/include/poppler/FDPDFDocBuilder.h
* /usr/include/poppler/FILECacheLoader.h
* /usr/include/poppler/FileSpec.h
* /usr/include/poppler/fofi/FoFiBase.h
* /usr/include/poppler/fofi/FoFiEncodings.h
* /usr/include/poppler/fofi/FoFiIdentifier.h
* /usr/include/poppler/fofi/FoFiTrueType.h
* /usr/include/poppler/fofi/FoFiType1.h
* /usr/include/poppler/fofi/FoFiType1C.h
* /usr/include/poppler/FontEncodingTables.h
* /usr/include/poppler/FontInfo.h
* /usr/include/poppler/Form.h
* /usr/include/poppler/Function.h
* /usr/include/poppler/Gfx.h
* /usr/include/poppler/GfxFont.h
* /usr/include/poppler/GfxState.h
* /usr/include/poppler/GfxState_helpers.h
* /usr/include/poppler/GlobalParams.h
* /usr/include/poppler/goo/gdir.h
* /usr/include/poppler/goo/gfile.h
* /usr/include/poppler/goo/gmem.h
* /usr/include/poppler/goo/GooCheckedOps.h
* /usr/include/poppler/goo/GooLikely.h
* /usr/include/poppler/goo/GooString.h
* /usr/include/poppler/goo/GooTimer.h
* /usr/include/poppler/goo/grandom.h
* /usr/include/poppler/goo/gstrtod.h
* /usr/include/poppler/goo/ImgWriter.h
* /usr/include/poppler/goo/JpegWriter.h
* /usr/include/poppler/goo/PNGWriter.h
* /usr/include/poppler/goo/TiffWriter.h
* /usr/include/poppler/HashAlgorithm.h
* /usr/include/poppler/Hints.h
* /usr/include/poppler/JArithmeticDecoder.h
* /usr/include/poppler/JBIG2Stream.h
* /usr/include/poppler/JPEG2000Stream.h
* /usr/include/poppler/JSInfo.h
* /usr/include/poppler/Lexer.h
* /usr/include/poppler/Linearization.h
* /usr/include/poppler/Link.h
* /usr/include/poppler/LocalPDFDocBuilder.h
* /usr/include/poppler/MarkedContentOutputDev.h
* /usr/include/poppler/Movie.h
* /usr/include/poppler/NameToCharCode.h
* /usr/include/poppler/NameToUnicodeTable.h
* /usr/include/poppler/Object.h
* /usr/include/poppler/OptionalContent.h
* /usr/include/poppler/Outline.h
* /usr/include/poppler/OutputDev.h
* /usr/include/poppler/Page.h
* /usr/include/poppler/PageTransition.h
* /usr/include/poppler/Parser.h
* /usr/include/poppler/PDFDoc.h
* /usr/include/poppler/PDFDocBuilder.h
* /usr/include/poppler/PDFDocEncoding.h
* /usr/include/poppler/PDFDocFactory.h
* /usr/include/poppler/poppler-config.h
* /usr/include/poppler/PopplerCache.h
* /usr/include/poppler/poppler_private_export.h
* /usr/include/poppler/PreScanOutputDev.h
* /usr/include/poppler/ProfileData.h
* /usr/include/poppler/PSOutputDev.h
* /usr/include/poppler/PSTokenizer.h
* /usr/include/poppler/Rendition.h
* /usr/include/poppler/SecurityHandler.h
* /usr/include/poppler/SignatureInfo.h
* /usr/include/poppler/Sound.h
* /usr/include/poppler/splash/Splash.h
* /usr/include/poppler/splash/SplashBitmap.h
* /usr/include/poppler/splash/SplashClip.h
* /usr/include/poppler/splash/SplashErrorCodes.h
* /usr/include/poppler/splash/SplashFont.h
* /usr/include/poppler/splash/SplashFontEngine.h
* /usr/include/poppler/splash/SplashFontFile.h
* /usr/include/poppler/splash/SplashFontFileID.h
* /usr/include/poppler/splash/SplashFTFont.h
* /usr/include/poppler/splash/SplashFTFontEngine.h
* /usr/include/poppler/splash/SplashFTFontFile.h
* /usr/include/poppler/splash/SplashGlyphBitmap.h
* /usr/include/poppler/splash/SplashMath.h
* /usr/include/poppler/splash/SplashPath.h
* /usr/include/poppler/splash/SplashPattern.h
* /usr/include/poppler/splash/SplashScreen.h
* /usr/include/poppler/splash/SplashState.h
* /usr/include/poppler/splash/SplashTypes.h
* /usr/include/poppler/splash/SplashXPath.h
* /usr/include/poppler/splash/SplashXPathScanner.h
* /usr/include/poppler/SplashOutputDev.h
* /usr/include/poppler/Stream-CCITT.h
* /usr/include/poppler/Stream.h
* /usr/include/poppler/StructElement.h
* /usr/include/poppler/StructTreeRoot.h
* /usr/include/poppler/TextOutputDev.h
* /usr/include/poppler/UnicodeCClassTables.h
* /usr/include/poppler/UnicodeCompTables.h
* /usr/include/poppler/UnicodeDecompTables.h
* /usr/include/poppler/UnicodeMap.h
* /usr/include/poppler/UnicodeMapFuncs.h
* /usr/include/poppler/UnicodeMapTables.h
* /usr/include/poppler/UnicodeTypeTable.h
* /usr/include/poppler/UTF.h
* /usr/include/poppler/ViewerPreferences.h
* /usr/include/poppler/XRef.h
* /usr/lib/girepository-1.0/Poppler-0.18.typelib
* /usr/lib/libpoppler-cpp.so
* /usr/lib/libpoppler-cpp.so.1
* /usr/lib/libpoppler-cpp.so.1.0.0
* /usr/lib/libpoppler.so
* /usr/lib/libpoppler.so.137
* /usr/lib/libpoppler.so.137.0.0
* /usr/lib/pkgconfig/poppler-cpp.pc
* /usr/lib/pkgconfig/poppler.pc
* /usr/share/doc/poppler-24.05.0/AUTHORS
* /usr/share/doc/poppler-24.05.0/ChangeLog
* /usr/share/doc/poppler-24.05.0/COPYING
* /usr/share/doc/poppler-24.05.0/COPYING3
* /usr/share/doc/poppler-24.05.0/INSTALL
* /usr/share/doc/poppler-24.05.0/NEWS
* /usr/share/doc/poppler-24.05.0/README-XPDF
* /usr/share/doc/poppler-24.05.0/README.contributors
* /usr/share/doc/poppler-24.05.0/README.md
* /usr/share/gir-1.0/Poppler-0.18.gir
* /usr/share/locale/ca/LC_MESSAGES/pdfsig.mo
