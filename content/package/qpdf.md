+++
draft = false
title = "qpdf 11.6.1-1"
version = "11.6.1-1"
date = "2023-09-13T19:35:27"
categories = ['apps']
upstreamurl = "https://sourceforge.net/projects/qpdf"
arch = "x86_64"
size = "939268"
usize = "3474353"
sha1sum = "b2b3c2d3a706aeb5989fe10308ef4795c8ef0a8e"
depends = "['pcre>=8.37-4', 'libstdc++>=11.2', 'libjpeg-turbo', 'openssl>=3.1.0']"
files = "['usr/', 'usr/bin/', 'usr/bin/fix-qdf', 'usr/bin/qpdf', 'usr/bin/zlib-flate', 'usr/include/', 'usr/include/qpdf/', 'usr/include/qpdf/Buffer.hh', 'usr/include/qpdf/BufferInputSource.hh', 'usr/include/qpdf/ClosedFileInputSource.hh', 'usr/include/qpdf/Constants.h', 'usr/include/qpdf/DLL.h', 'usr/include/qpdf/FileInputSource.hh', 'usr/include/qpdf/InputSource.hh', 'usr/include/qpdf/JSON.hh', 'usr/include/qpdf/PDFVersion.hh', 'usr/include/qpdf/Pipeline.hh', 'usr/include/qpdf/Pl_Buffer.hh', 'usr/include/qpdf/Pl_Concatenate.hh', 'usr/include/qpdf/Pl_Count.hh', 'usr/include/qpdf/Pl_DCT.hh', 'usr/include/qpdf/Pl_Discard.hh', 'usr/include/qpdf/Pl_Flate.hh', 'usr/include/qpdf/Pl_Function.hh', 'usr/include/qpdf/Pl_OStream.hh', 'usr/include/qpdf/Pl_QPDFTokenizer.hh', 'usr/include/qpdf/Pl_RunLength.hh', 'usr/include/qpdf/Pl_StdioFile.hh', 'usr/include/qpdf/Pl_String.hh', 'usr/include/qpdf/PointerHolder.hh', 'usr/include/qpdf/QIntC.hh', 'usr/include/qpdf/QPDF.hh', 'usr/include/qpdf/QPDFAcroFormDocumentHelper.hh', 'usr/include/qpdf/QPDFAnnotationObjectHelper.hh', 'usr/include/qpdf/QPDFCryptoImpl.hh', 'usr/include/qpdf/QPDFCryptoProvider.hh', 'usr/include/qpdf/QPDFDocumentHelper.hh', 'usr/include/qpdf/QPDFEFStreamObjectHelper.hh', 'usr/include/qpdf/QPDFEmbeddedFileDocumentHelper.hh', 'usr/include/qpdf/QPDFExc.hh', 'usr/include/qpdf/QPDFFileSpecObjectHelper.hh', 'usr/include/qpdf/QPDFFormFieldObjectHelper.hh', 'usr/include/qpdf/QPDFJob.hh', 'usr/include/qpdf/QPDFLogger.hh', 'usr/include/qpdf/QPDFMatrix.hh', 'usr/include/qpdf/QPDFNameTreeObjectHelper.hh', 'usr/include/qpdf/QPDFNumberTreeObjectHelper.hh', 'usr/include/qpdf/QPDFObjGen.hh', 'usr/include/qpdf/QPDFObject.hh', 'usr/include/qpdf/QPDFObjectHandle.hh', 'usr/include/qpdf/QPDFObjectHelper.hh', 'usr/include/qpdf/QPDFOutlineDocumentHelper.hh', 'usr/include/qpdf/QPDFOutlineObjectHelper.hh', 'usr/include/qpdf/QPDFPageDocumentHelper.hh', 'usr/include/qpdf/QPDFPageLabelDocumentHelper.hh', 'usr/include/qpdf/QPDFPageObjectHelper.hh', 'usr/include/qpdf/QPDFStreamFilter.hh', 'usr/include/qpdf/QPDFSystemError.hh', 'usr/include/qpdf/QPDFTokenizer.hh', 'usr/include/qpdf/QPDFUsage.hh', 'usr/include/qpdf/QPDFWriter.hh', 'usr/include/qpdf/QPDFXRefEntry.hh', 'usr/include/qpdf/QTC.hh', 'usr/include/qpdf/QUtil.hh', 'usr/include/qpdf/RandomDataProvider.hh', 'usr/include/qpdf/Types.h', 'usr/include/qpdf/auto_job_c_att.hh', 'usr/include/qpdf/auto_job_c_copy_att.hh', 'usr/include/qpdf/auto_job_c_enc.hh', 'usr/include/qpdf/auto_job_c_main.hh', 'usr/include/qpdf/auto_job_c_pages.hh', 'usr/include/qpdf/auto_job_c_uo.hh', 'usr/include/qpdf/qpdf-c.h', 'usr/include/qpdf/qpdfjob-c.h', 'usr/include/qpdf/qpdflogger-c.h', 'usr/lib/', 'usr/lib/cmake/', 'usr/lib/cmake/qpdf/', 'usr/lib/cmake/qpdf/libqpdfTargets-release.cmake', 'usr/lib/cmake/qpdf/libqpdfTargets.cmake', 'usr/lib/cmake/qpdf/qpdfConfig.cmake', 'usr/lib/cmake/qpdf/qpdfConfigVersion.cmake', 'usr/lib/libqpdf.so', 'usr/lib/libqpdf.so.29', 'usr/lib/libqpdf.so.29.6.1', 'usr/lib/pkgconfig/', 'usr/lib/pkgconfig/libqpdf.pc', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/qpdf-11.6.1/', 'usr/share/doc/qpdf-11.6.1/ChangeLog', 'usr/share/doc/qpdf-11.6.1/README-appimage.md', 'usr/share/doc/qpdf-11.6.1/README-doc.txt', 'usr/share/doc/qpdf-11.6.1/README-hardening.md', 'usr/share/doc/qpdf-11.6.1/README-maintainer.md', 'usr/share/doc/qpdf-11.6.1/README-what-to-download.md', 'usr/share/doc/qpdf-11.6.1/README-windows.md', 'usr/share/doc/qpdf-11.6.1/README.md', 'usr/share/doc/qpdf/', 'usr/share/doc/qpdf/README-doc.txt', 'usr/share/doc/qpdf/examples/', 'usr/share/doc/qpdf/examples/pdf-attach-file.cc', 'usr/share/doc/qpdf/examples/pdf-bookmarks.cc', 'usr/share/doc/qpdf/examples/pdf-c-objects.c', 'usr/share/doc/qpdf/examples/pdf-count-strings.cc', 'usr/share/doc/qpdf/examples/pdf-create.cc', 'usr/share/doc/qpdf/examples/pdf-custom-filter.cc', 'usr/share/doc/qpdf/examples/pdf-double-page-size.cc', 'usr/share/doc/qpdf/examples/pdf-filter-tokens.cc', 'usr/share/doc/qpdf/examples/pdf-invert-images.cc', 'usr/share/doc/qpdf/examples/pdf-linearize.c', 'usr/share/doc/qpdf/examples/pdf-mod-info.cc', 'usr/share/doc/qpdf/examples/pdf-name-number-tree.cc', 'usr/share/doc/qpdf/examples/pdf-npages.cc', 'usr/share/doc/qpdf/examples/pdf-overlay-page.cc', 'usr/share/doc/qpdf/examples/pdf-parse-content.cc', 'usr/share/doc/qpdf/examples/pdf-set-form-values.cc', 'usr/share/doc/qpdf/examples/pdf-split-pages.cc', 'usr/share/doc/qpdf/examples/qpdf-job.cc', 'usr/share/doc/qpdf/examples/qpdfjob-c-save-attachment.c', 'usr/share/doc/qpdf/examples/qpdfjob-c.c', 'usr/share/doc/qpdf/examples/qpdfjob-remove-annotations.cc', 'usr/share/doc/qpdf/examples/qpdfjob-save-attachment.cc', 'usr/share/man/', 'usr/share/man/man1/', 'usr/share/man/man1/fix-qdf.1.gz', 'usr/share/man/man1/qpdf.1.gz', 'usr/share/man/man1/zlib-flate.1.gz']"
+++
QPDF do structural, content-preserving transformations on PDF files.