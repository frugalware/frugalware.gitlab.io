+++
draft = false
title = "xsane 0.999-5"
version = "0.999-5"
description = "XSane is a graphical scanning frontend for SANE (Scanner Access Now Easy)."
date = "2024-01-09T15:38:26"
aliases = "/packages/218755"
categories = ['xapps-extra']
upstreamurl = "https://gitlab.com/sane-project/frontend/xsane"
arch = "x86_64"
size = "1593124"
usize = "5026259"
sha1sum = "b5cc62dd1323c5ac6d97ead505798b14e1da9a75"
depends = "['gtk+2', 'lcms', 'libgphoto2>=2.5.0', 'libjpeg', 'sane-backends>=1.0.21', 'zlib>=1.2.12']"
reverse_depends = "['xsane-gimp']"
license = "2"
+++
XSane is a graphical scanning frontend for SANE (Scanner Access Now Easy)."

{{< files text="show files" >}}* /usr/bin/xsane
* /usr/share/applications/xsane.desktop
* /usr/share/doc/xsane-0.999/xsane-WIN32-README.txt
* /usr/share/doc/xsane-0.999/xsane.BUGS
* /usr/share/doc/xsane-0.999/xsane.COPYING
* /usr/share/doc/xsane-0.999/xsane.FAQ
* /usr/share/locale/ca/LC_MESSAGES/xsane.mo
* /usr/share/locale/cs/LC_MESSAGES/xsane.mo
* /usr/share/locale/da/LC_MESSAGES/xsane.mo
* /usr/share/locale/de/LC_MESSAGES/xsane.mo
* /usr/share/locale/es/LC_MESSAGES/xsane.mo
* /usr/share/locale/fi/LC_MESSAGES/xsane.mo
* /usr/share/locale/fr/LC_MESSAGES/xsane.mo
* /usr/share/locale/hu/LC_MESSAGES/xsane.mo
* /usr/share/locale/it/LC_MESSAGES/xsane.mo
* /usr/share/locale/ja/LC_MESSAGES/xsane.mo
* /usr/share/locale/nl/LC_MESSAGES/xsane.mo
* /usr/share/locale/pa/LC_MESSAGES/xsane.mo
* /usr/share/locale/pl/LC_MESSAGES/xsane.mo
* /usr/share/locale/pt/LC_MESSAGES/xsane.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/xsane.mo
* /usr/share/locale/ro/LC_MESSAGES/xsane.mo
* /usr/share/locale/ru/LC_MESSAGES/xsane.mo
* /usr/share/locale/sk/LC_MESSAGES/xsane.mo
* /usr/share/locale/sl/LC_MESSAGES/xsane.mo
* /usr/share/locale/sr/LC_MESSAGES/xsane.mo
* /usr/share/locale/sv/LC_MESSAGES/xsane.mo
* /usr/share/locale/tr/LC_MESSAGES/xsane.mo
* /usr/share/locale/vi/LC_MESSAGES/xsane.mo
* /usr/share/locale/zh/LC_MESSAGES/xsane.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/xsane.mo
* /usr/share/man/man1/xsane.1.gz
* /usr/share/pixmaps/xsane.xpm
* /usr/share/sane/xsane/doc/sane-backends-doc.html
* /usr/share/sane/xsane/doc/sane-pnm-doc.html
* /usr/share/sane/xsane/doc/sane-problems-doc.html
* /usr/share/sane/xsane/doc/sane-scantips-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-advanced-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-batch-scan-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-color-correction-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-color-management-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-copy-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-email-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-empty-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-fax-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-gimp-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-guide-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-histogram-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-medium-definition-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-multipage-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-preview-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-save-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-scan-options-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-setup-color-management-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-setup-copy-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-setup-display-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-setup-email-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-setup-enhancement-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-setup-fax-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-setup-filetype-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-setup-save-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-standard-doc.html
* /usr/share/sane/xsane/doc/sane-xsane-viewer-doc.html
* /usr/share/sane/xsane/doc/xsane-adf-pages.jpg
* /usr/share/sane/xsane/doc/xsane-advanced.jpg
* /usr/share/sane/xsane/doc/xsane-aspect-ratio.jpg
* /usr/share/sane/xsane/doc/xsane-autoenhance.jpg
* /usr/share/sane/xsane/doc/xsane-autoraise_scanarea.jpg
* /usr/share/sane/xsane/doc/xsane-autoselect.jpg
* /usr/share/sane/xsane/doc/xsane-batch-scan-add.jpg
* /usr/share/sane/xsane/doc/xsane-batch-scan-delete.jpg
* /usr/share/sane/xsane/doc/xsane-batch-scan.jpg
* /usr/share/sane/xsane/doc/xsane-blur.jpg
* /usr/share/sane/xsane/doc/xsane-brightness.jpg
* /usr/share/sane/xsane/doc/xsane-clone.jpg
* /usr/share/sane/xsane/doc/xsane-cms-function.jpg
* /usr/share/sane/xsane/doc/xsane-color-correction-rgb-default.jpg
* /usr/share/sane/xsane/doc/xsane-color-correction.jpg
* /usr/share/sane/xsane/doc/xsane-color-management-main-window.jpg
* /usr/share/sane/xsane/doc/xsane-colormode.jpg
* /usr/share/sane/xsane/doc/xsane-contrast.jpg
* /usr/share/sane/xsane/doc/xsane-copy-number.jpg
* /usr/share/sane/xsane/doc/xsane-copy.jpg
* /usr/share/sane/xsane/doc/xsane-default.jpg
* /usr/share/sane/xsane/doc/xsane-delete-preview-cache.jpg
* /usr/share/sane/xsane/doc/xsane-despeckle.jpg
* /usr/share/sane/xsane/doc/xsane-disk.jpg
* /usr/share/sane/xsane/doc/xsane-edit-medium.jpg
* /usr/share/sane/xsane/doc/xsane-email-project.jpg
* /usr/share/sane/xsane/doc/xsane-email.jpg
* /usr/share/sane/xsane/doc/xsane-enable-color-management.jpg
* /usr/share/sane/xsane/doc/xsane-fax-project.jpg
* /usr/share/sane/xsane/doc/xsane-fax.jpg
* /usr/share/sane/xsane/doc/xsane-gamma.jpg
* /usr/share/sane/xsane/doc/xsane-gimp.jpg
* /usr/share/sane/xsane/doc/xsane-guide-1-decoration.jpg
* /usr/share/sane/xsane/doc/xsane-guide-10-scan.jpg
* /usr/share/sane/xsane/doc/xsane-guide-2-menu.jpg
* /usr/share/sane/xsane/doc/xsane-guide-3-options.jpg
* /usr/share/sane/xsane/doc/xsane-guide-4.jpg
* /usr/share/sane/xsane/doc/xsane-guide-4a-adf-pages.jpg
* /usr/share/sane/xsane/doc/xsane-guide-4b-xsane-mode.jpg
* /usr/share/sane/xsane/doc/xsane-guide-5-saving-options.jpg
* /usr/share/sane/xsane/doc/xsane-guide-6-scan-options.jpg
* /usr/share/sane/xsane/doc/xsane-guide-7-medium-selection.jpg
* /usr/share/sane/xsane/doc/xsane-guide-8-resolution.jpg
* /usr/share/sane/xsane/doc/xsane-guide-9-color-correction.jpg
* /usr/share/sane/xsane/doc/xsane-histogram.jpg
* /usr/share/sane/xsane/doc/xsane-logo.jpg
* /usr/share/sane/xsane/doc/xsane-medium-add.jpg
* /usr/share/sane/xsane/doc/xsane-medium.jpg
* /usr/share/sane/xsane/doc/xsane-mirror-x.jpg
* /usr/share/sane/xsane/doc/xsane-mirror-y.jpg
* /usr/share/sane/xsane/doc/xsane-multipage-project.jpg
* /usr/share/sane/xsane/doc/xsane-multipage.jpg
* /usr/share/sane/xsane/doc/xsane-negative.jpg
* /usr/share/sane/xsane/doc/xsane-new.jpg
* /usr/share/sane/xsane/doc/xsane-ocr.jpg
* /usr/share/sane/xsane/doc/xsane-open.jpg
* /usr/share/sane/xsane/doc/xsane-paper-landscape-bottom-left.jpg
* /usr/share/sane/xsane/doc/xsane-paper-landscape-bottom-right.jpg
* /usr/share/sane/xsane/doc/xsane-paper-landscape-center.jpg
* /usr/share/sane/xsane/doc/xsane-paper-landscape-top-left.jpg
* /usr/share/sane/xsane/doc/xsane-paper-landscape-top-right.jpg
* /usr/share/sane/xsane/doc/xsane-paper-portrait-bottom-left.jpg
* /usr/share/sane/xsane/doc/xsane-paper-portrait-bottom-right.jpg
* /usr/share/sane/xsane/doc/xsane-paper-portrait-center.jpg
* /usr/share/sane/xsane/doc/xsane-paper-portrait-top-left.jpg
* /usr/share/sane/xsane/doc/xsane-paper-portrait-top-right.jpg
* /usr/share/sane/xsane/doc/xsane-pipette-black.jpg
* /usr/share/sane/xsane/doc/xsane-pipette-gray.jpg
* /usr/share/sane/xsane/doc/xsane-pipette-white.jpg
* /usr/share/sane/xsane/doc/xsane-preferences.jpg
* /usr/share/sane/xsane/doc/xsane-preset-area-context-menu.jpg
* /usr/share/sane/xsane/doc/xsane-preset-area.jpg
* /usr/share/sane/xsane/doc/xsane-preview.jpg
* /usr/share/sane/xsane/doc/xsane-printer.jpg
* /usr/share/sane/xsane/doc/xsane-rename.jpg
* /usr/share/sane/xsane/doc/xsane-resolution.jpg
* /usr/share/sane/xsane/doc/xsane-restore.jpg
* /usr/share/sane/xsane/doc/xsane-rgb-default.jpg
* /usr/share/sane/xsane/doc/xsane-rgb-values.jpg
* /usr/share/sane/xsane/doc/xsane-rotate-180.jpg
* /usr/share/sane/xsane/doc/xsane-rotate-270.jpg
* /usr/share/sane/xsane/doc/xsane-rotate-90.jpg
* /usr/share/sane/xsane/doc/xsane-rotation.jpg
* /usr/share/sane/xsane/doc/xsane-save.jpg
* /usr/share/sane/xsane/doc/xsane-save2.jpg
* /usr/share/sane/xsane/doc/xsane-scale.jpg
* /usr/share/sane/xsane/doc/xsane-scansource.jpg
* /usr/share/sane/xsane/doc/xsane-setup-color-management.jpg
* /usr/share/sane/xsane/doc/xsane-setup-copy.jpg
* /usr/share/sane/xsane/doc/xsane-setup-display.jpg
* /usr/share/sane/xsane/doc/xsane-setup-email.jpg
* /usr/share/sane/xsane/doc/xsane-setup-enhancement.jpg
* /usr/share/sane/xsane/doc/xsane-setup-fax.jpg
* /usr/share/sane/xsane/doc/xsane-setup-filetype.jpg
* /usr/share/sane/xsane/doc/xsane-setup-ocr.jpg
* /usr/share/sane/xsane/doc/xsane-setup-save.jpg
* /usr/share/sane/xsane/doc/xsane-standard.jpg
* /usr/share/sane/xsane/doc/xsane-step.jpg
* /usr/share/sane/xsane/doc/xsane-store.jpg
* /usr/share/sane/xsane/doc/xsane-target.jpg
* /usr/share/sane/xsane/doc/xsane-threshold.jpg
* /usr/share/sane/xsane/doc/xsane-viewer-window.jpg
* /usr/share/sane/xsane/doc/xsane-viewer.jpg
* /usr/share/sane/xsane/doc/xsane-visible-area.jpg
* /usr/share/sane/xsane/doc/xsane-zoom-in.jpg
* /usr/share/sane/xsane/doc/xsane-zoom-not.jpg
* /usr/share/sane/xsane/doc/xsane-zoom-out.jpg
* /usr/share/sane/xsane/doc/xsane-zoom-undo.jpg
* /usr/share/sane/xsane/doc/xsane-zoom.jpg
* /usr/share/sane/xsane/Mustek-logo.xpm
* /usr/share/sane/xsane/Plustek-logo.xpm
* /usr/share/sane/xsane/sane-epson-logo.xpm
* /usr/share/sane/xsane/sane-hp-logo.xpm
* /usr/share/sane/xsane/sane-umax-logo.xpm
* /usr/share/sane/xsane/sane-xsane-logo.xpm
* /usr/share/sane/xsane/UMAX-logo.xpm
* /usr/share/sane/xsane/xsane-calibration.pnm
* /usr/share/sane/xsane/xsane-eula.txt
* /usr/share/sane/xsane/xsane-gpl.txt
* /usr/share/sane/xsane/xsane-logo.xpm
* /usr/share/sane/xsane/xsane-startimage.pnm
* /usr/share/sane/xsane/xsane-style.rc
{{< /files >}}