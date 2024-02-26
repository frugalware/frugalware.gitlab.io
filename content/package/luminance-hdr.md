+++
draft = false
title = "luminance-hdr 2.6.1.1-13"
version = "2.6.1.1-13"
description = "An open source graphical user interface application that aims to provide a workflow for HDR imaging"
date = "2023-11-07T11:24:25"
aliases = "/packages/118995"
categories = ['xapps-extra']
upstreamurl = "https://sourceforge.net/projects/qtpfsgui"
arch = "x86_64"
size = "4922400"
usize = "10895960"
sha1sum = "e9efe8d352dbde7df48e799ee1ea62bdb4413879"
depends = "['eigen', 'exiv2>=0.28.1', 'fftw', 'gsl>=2.7.1', 'lcms2>=2.8-2', 'libboost>=1.82.0', 'libgomp>=6.2.1-5', 'libraw>=0.21.1', 'openexr>=3.2.0', 'qt5-svg>=5.15.10', 'qt5-webengine']"
+++
An open source graphical user interface application that aims to provide a workflow for HDR imaging{{< files text="show files" >}}* /usr/bin/luminance-hdr
* /usr/bin/luminance-hdr-cli
* /usr/share/appdata/net.sourceforge.qtpfsgui.LuminanceHDR.appdata.xml
* /usr/share/applications/net.sourceforge.qtpfsgui.LuminanceHDR.desktop
* /usr/share/doc/luminance-hdr-2.6.1.1/AUTHORS
* /usr/share/doc/luminance-hdr-2.6.1.1/BUGS
* /usr/share/doc/luminance-hdr-2.6.1.1/Changelog
* /usr/share/doc/luminance-hdr-2.6.1.1/INSTALL.md
* /usr/share/doc/luminance-hdr-2.6.1.1/LICENSE
* /usr/share/doc/luminance-hdr-2.6.1.1/README.i18n
* /usr/share/doc/luminance-hdr-2.6.1.1/README.md
* /usr/share/doc/luminance-hdr-2.6.1.1/TODO
* /usr/share/icons/hicolor/48x48/apps/luminance-hdr.png
* /usr/share/luminance-hdr/doc/AUTHORS
* /usr/share/luminance-hdr/doc/Changelog
* /usr/share/luminance-hdr/doc/LICENSE
* /usr/share/luminance-hdr/doc/README.md
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_c_b2.csv
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_c_b3.csv
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_c_b4.csv
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_c_b5.csv
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_default_templ/hdrhtml_image_templ.html
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_default_templ/hdrhtml_page_templ.html
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_hdrlabs_templ/hdrhtml_assets/hdr_viewer.css
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_hdrlabs_templ/hdrhtml_assets/hdr_viewer.js
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_hdrlabs_templ/hdrhtml_assets/information-red.png
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_hdrlabs_templ/hdrhtml_assets/information.png
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_hdrlabs_templ/hdrhtml_assets/loading-spinner.gif
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_hdrlabs_templ/hdrhtml_assets/mootools-1.2.4.js
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_hdrlabs_templ/hdrhtml_assets/mouse2touch.js
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_hdrlabs_templ/hdrhtml_assets/slider-black.png
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_hdrlabs_templ/hdrhtml_assets/slider-red.png
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_hdrlabs_templ/hdrhtml_assets/slider-white.png
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_hdrlabs_templ/hdrhtml_image_templ.html
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_hdrlabs_templ/hdrhtml_image_templ_slider-above.html
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_hdrlabs_templ/hdrhtml_page_templ.html
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_hdrlabs_templ/hdrhtml_page_templ_short.html
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_t_b2.csv
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_t_b3.csv
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_t_b4.csv
* /usr/share/luminance-hdr/hdrhtml/hdrhtml_t_b5.csv
* /usr/share/luminance-hdr/help/en/additional.html
* /usr/share/luminance-hdr/help/en/basics.html
* /usr/share/luminance-hdr/help/en/color_management.html
* /usr/share/luminance-hdr/help/en/contributing.html
* /usr/share/luminance-hdr/help/en/contributing_donating.html
* /usr/share/luminance-hdr/help/en/contributing_programming.html
* /usr/share/luminance-hdr/help/en/contributing_testing.html
* /usr/share/luminance-hdr/help/en/contributing_translating.html
* /usr/share/luminance-hdr/help/en/copying_exif.html
* /usr/share/luminance-hdr/help/en/creating_hdr.html
* /usr/share/luminance-hdr/help/en/creating_hdr_batch.html
* /usr/share/luminance-hdr/help/en/creating_hdr_cli.html
* /usr/share/luminance-hdr/help/en/creating_hdr_interactive.html
* /usr/share/luminance-hdr/help/en/dcraw.html
* /usr/share/luminance-hdr/help/en/editing_hdr.html
* /usr/share/luminance-hdr/help/en/editing_tools.html
* /usr/share/luminance-hdr/help/en/external.png
* /usr/share/luminance-hdr/help/en/faq.html
* /usr/share/luminance-hdr/help/en/features.html
* /usr/share/luminance-hdr/help/en/hints.html
* /usr/share/luminance-hdr/help/en/images/batch-hdr.png
* /usr/share/luminance-hdr/help/en/images/batch-tmo.png
* /usr/share/luminance-hdr/help/en/images/color_management.png
* /usr/share/luminance-hdr/help/en/images/copy-exif.png
* /usr/share/luminance-hdr/help/en/images/cropping_frame.png
* /usr/share/luminance-hdr/help/en/images/editingtools-1.png
* /usr/share/luminance-hdr/help/en/images/editingtools-2.png
* /usr/share/luminance-hdr/help/en/images/editingtools-3.png
* /usr/share/luminance-hdr/help/en/images/editingtools-4.png
* /usr/share/luminance-hdr/help/en/images/editingtools-5.png
* /usr/share/luminance-hdr/help/en/images/editingtools-6.png
* /usr/share/luminance-hdr/help/en/images/edit_menu.png
* /usr/share/luminance-hdr/help/en/images/hdrwizard.png
* /usr/share/luminance-hdr/help/en/images/mainwin.png
* /usr/share/luminance-hdr/help/en/images/not-translated-menu-item.png
* /usr/share/luminance-hdr/help/en/images/preferences-menu.png
* /usr/share/luminance-hdr/help/en/images/preferences.png
* /usr/share/luminance-hdr/help/en/images/prefs-cms.png
* /usr/share/luminance-hdr/help/en/images/prefs-ext.png
* /usr/share/luminance-hdr/help/en/images/prefs-fast-export.png
* /usr/share/luminance-hdr/help/en/images/prefs-hdr.png
* /usr/share/luminance-hdr/help/en/images/prefs-raw-color.png
* /usr/share/luminance-hdr/help/en/images/prefs-raw-corrections.png
* /usr/share/luminance-hdr/help/en/images/prefs-raw-general.png
* /usr/share/luminance-hdr/help/en/images/prefs-raw.png
* /usr/share/luminance-hdr/help/en/images/prefs-tm.png
* /usr/share/luminance-hdr/help/en/images/prefs-ui.png
* /usr/share/luminance-hdr/help/en/images/projectiveTransformationDialog.png
* /usr/share/luminance-hdr/help/en/images/resize.png
* /usr/share/luminance-hdr/help/en/images/tonemappingpanel.png
* /usr/share/luminance-hdr/help/en/images/translated-menu-item.png
* /usr/share/luminance-hdr/help/en/index.html
* /usr/share/luminance-hdr/help/en/manual.html
* /usr/share/luminance-hdr/help/en/menu.xml
* /usr/share/luminance-hdr/help/en/news.html
* /usr/share/luminance-hdr/help/en/prefs.html
* /usr/share/luminance-hdr/help/en/prefs_cms.html
* /usr/share/luminance-hdr/help/en/prefs_fast_export.html
* /usr/share/luminance-hdr/help/en/prefs_hdr.html
* /usr/share/luminance-hdr/help/en/prefs_rawconversion.html
* /usr/share/luminance-hdr/help/en/prefs_tonemapping.html
* /usr/share/luminance-hdr/help/en/prefs_tools.html
* /usr/share/luminance-hdr/help/en/prefs_ui.html
* /usr/share/luminance-hdr/help/en/projective_transformation.html
* /usr/share/luminance-hdr/help/en/README
* /usr/share/luminance-hdr/help/en/style.css
* /usr/share/luminance-hdr/help/en/tmap_ref.html
* /usr/share/luminance-hdr/help/en/tmap_ref_ashikhmin.html
* /usr/share/luminance-hdr/help/en/tmap_ref_drago.html
* /usr/share/luminance-hdr/help/en/tmap_ref_durand.html
* /usr/share/luminance-hdr/help/en/tmap_ref_fattal.html
* /usr/share/luminance-hdr/help/en/tmap_ref_ferradans.html
* /usr/share/luminance-hdr/help/en/tmap_ref_mai.html
* /usr/share/luminance-hdr/help/en/tmap_ref_mantiuk06.html
* /usr/share/luminance-hdr/help/en/tmap_ref_mantiuk08.html
* /usr/share/luminance-hdr/help/en/tmap_ref_pattanaik.html
* /usr/share/luminance-hdr/help/en/tmap_ref_reinhard02.html
* /usr/share/luminance-hdr/help/en/tmap_ref_reinhard05.html
* /usr/share/luminance-hdr/help/en/tonemapping.html
* /usr/share/luminance-hdr/help/en/tonemapping_batch.html
* /usr/share/luminance-hdr/help/en/tonemapping_cli.html
* /usr/share/luminance-hdr/help/en/tonemapping_interactive.html
* /usr/share/luminance-hdr/help/en/workflow.html
* /usr/share/luminance-hdr/i18n/lang_cs.qm
* /usr/share/luminance-hdr/i18n/lang_da.qm
* /usr/share/luminance-hdr/i18n/lang_de.qm
* /usr/share/luminance-hdr/i18n/lang_es.qm
* /usr/share/luminance-hdr/i18n/lang_fi.qm
* /usr/share/luminance-hdr/i18n/lang_fr.qm
* /usr/share/luminance-hdr/i18n/lang_hu.qm
* /usr/share/luminance-hdr/i18n/lang_id.qm
* /usr/share/luminance-hdr/i18n/lang_it.qm
* /usr/share/luminance-hdr/i18n/lang_nl.qm
* /usr/share/luminance-hdr/i18n/lang_pl.qm
* /usr/share/luminance-hdr/i18n/lang_pt_BR.qm
* /usr/share/luminance-hdr/i18n/lang_ro.qm
* /usr/share/luminance-hdr/i18n/lang_ru.qm
* /usr/share/luminance-hdr/i18n/lang_tr.qm
* /usr/share/luminance-hdr/i18n/lang_zh.qm
{{< /files >}}