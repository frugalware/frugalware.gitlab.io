+++
draft = false
title = "gimp-print 4.2.7-1"
version = "4.2.7-1"
description = "IJS printer driver for Ghostscript and CUPS"
date = "2006-02-15T05:00:46"
aliases = "/packages/3030"
categories = ['apps']
upstreamurl = ""
arch = "x86_64"
size = "3950215"
usize = "0"
sha1sum = "d12736f870d2bf651cd898c1d2374bcf6cce47eb"
depends = "['cups', 'readline']"
+++
IJS printer driver for Ghostscript and CUPS{{< spoiler text="show files" >}}* etc/cups/command.types
* usr/bin/cups-calibrate
* usr/bin/escputil
* usr/bin/gimpprint-config
* usr/include/gimp-print/gimp-print.h
* usr/info/gimpprint.info
* usr/info/gimpprint.info-1
* usr/info/gimpprint.info-2
* usr/info/gimpprint.info-3
* usr/info/gimpprint.info-4
* usr/info/gimpprint.info-5
* usr/lib/cups/backend/canon
* usr/lib/cups/backend/epson
* usr/lib/cups/filter/commandtocanon
* usr/lib/cups/filter/commandtoepson
* usr/lib/cups/filter/rastertoprinter
* usr/lib/libgimpprint.la
* usr/lib/libgimpprint.so
* usr/lib/libgimpprint.so.1
* usr/lib/libgimpprint.so.1.1.3
* usr/man/man1/escputil.1.gz
* usr/man/man1/gimpprint-config.1.gz
* usr/man/man1/ijsgimpprint.1.gz
* usr/man/man3/gimpprint.3.gz
* usr/man/man7/gimpprint-color.7.gz
* usr/man/man7/gimpprint-dithers.7.gz
* usr/man/man7/gimpprint-imagetypes.7.gz
* usr/man/man7/gimpprint-inktypes.7.gz
* usr/man/man7/gimpprint-mediasizes.7.gz
* usr/man/man7/gimpprint-mediasources.7.gz
* usr/man/man7/gimpprint-mediatypes.7.gz
* usr/man/man7/gimpprint-models.7.gz
* usr/man/man7/gimpprint-resolutions.7.gz
* usr/man/man8/cups-calibrate.8.gz
* usr/share/aclocal/gimpprint.m4
* usr/share/cups/calibrate.ppm
* usr/share/cups/model/C/bjc-1000.ppd.gz
* usr/share/cups/model/C/bjc-2000.ppd.gz
* usr/share/cups/model/C/bjc-210.ppd.gz
* usr/share/cups/model/C/bjc-240.ppd.gz
* usr/share/cups/model/C/bjc-250.ppd.gz
* usr/share/cups/model/C/bjc-30.ppd.gz
* usr/share/cups/model/C/bjc-3000.ppd.gz
* usr/share/cups/model/C/bjc-4300.ppd.gz
* usr/share/cups/model/C/bjc-4400.ppd.gz
* usr/share/cups/model/C/bjc-50.ppd.gz
* usr/share/cups/model/C/bjc-55.ppd.gz
* usr/share/cups/model/C/bjc-6000.ppd.gz
* usr/share/cups/model/C/bjc-6100.ppd.gz
* usr/share/cups/model/C/bjc-6200.ppd.gz
* usr/share/cups/model/C/bjc-6500.ppd.gz
* usr/share/cups/model/C/bjc-7000.ppd.gz
* usr/share/cups/model/C/bjc-7100.ppd.gz
* usr/share/cups/model/C/bjc-80.ppd.gz
* usr/share/cups/model/C/bjc-8200.ppd.gz
* usr/share/cups/model/C/bjc-85.ppd.gz
* usr/share/cups/model/C/bjc-s200.ppd.gz
* usr/share/cups/model/C/bjc-s400.ppd.gz
* usr/share/cups/model/C/bjc-s450.ppd.gz
* usr/share/cups/model/C/bjc-s4500.ppd.gz
* usr/share/cups/model/C/bjc-s800.ppd.gz
* usr/share/cups/model/C/escp2-10000.ppd.gz
* usr/share/cups/model/C/escp2-1160.ppd.gz
* usr/share/cups/model/C/escp2-1200.ppd.gz
* usr/share/cups/model/C/escp2-1270.ppd.gz
* usr/share/cups/model/C/escp2-1280.ppd.gz
* usr/share/cups/model/C/escp2-1290.ppd.gz
* usr/share/cups/model/C/escp2-1500.ppd.gz
* usr/share/cups/model/C/escp2-1520.ppd.gz
* usr/share/cups/model/C/escp2-2000.ppd.gz
* usr/share/cups/model/C/escp2-2100.ppd.gz
* usr/share/cups/model/C/escp2-2200.ppd.gz
* usr/share/cups/model/C/escp2-3000.ppd.gz
* usr/share/cups/model/C/escp2-400.ppd.gz
* usr/share/cups/model/C/escp2-440.ppd.gz
* usr/share/cups/model/C/escp2-460.ppd.gz
* usr/share/cups/model/C/escp2-480.ppd.gz
* usr/share/cups/model/C/escp2-500.ppd.gz
* usr/share/cups/model/C/escp2-5000.ppd.gz
* usr/share/cups/model/C/escp2-5500.ppd.gz
* usr/share/cups/model/C/escp2-580.ppd.gz
* usr/share/cups/model/C/escp2-600.ppd.gz
* usr/share/cups/model/C/escp2-640.ppd.gz
* usr/share/cups/model/C/escp2-660.ppd.gz
* usr/share/cups/model/C/escp2-670.ppd.gz
* usr/share/cups/model/C/escp2-680.ppd.gz
* usr/share/cups/model/C/escp2-700.ppd.gz
* usr/share/cups/model/C/escp2-7000.ppd.gz
* usr/share/cups/model/C/escp2-720.ppd.gz
* usr/share/cups/model/C/escp2-740.ppd.gz
* usr/share/cups/model/C/escp2-750.ppd.gz
* usr/share/cups/model/C/escp2-7500.ppd.gz
* usr/share/cups/model/C/escp2-760.ppd.gz
* usr/share/cups/model/C/escp2-7600.ppd.gz
* usr/share/cups/model/C/escp2-777.ppd.gz
* usr/share/cups/model/C/escp2-780.ppd.gz
* usr/share/cups/model/C/escp2-785.ppd.gz
* usr/share/cups/model/C/escp2-790.ppd.gz
* usr/share/cups/model/C/escp2-800.ppd.gz
* usr/share/cups/model/C/escp2-810.ppd.gz
* usr/share/cups/model/C/escp2-820.ppd.gz
* usr/share/cups/model/C/escp2-825.ppd.gz
* usr/share/cups/model/C/escp2-83.ppd.gz
* usr/share/cups/model/C/escp2-830.ppd.gz
* usr/share/cups/model/C/escp2-850.ppd.gz
* usr/share/cups/model/C/escp2-860.ppd.gz
* usr/share/cups/model/C/escp2-870.ppd.gz
* usr/share/cups/model/C/escp2-875.ppd.gz
* usr/share/cups/model/C/escp2-880.ppd.gz
* usr/share/cups/model/C/escp2-890.ppd.gz
* usr/share/cups/model/C/escp2-895.ppd.gz
* usr/share/cups/model/C/escp2-900.ppd.gz
* usr/share/cups/model/C/escp2-9000.ppd.gz
* usr/share/cups/model/C/escp2-915.ppd.gz
* usr/share/cups/model/C/escp2-925.ppd.gz
* usr/share/cups/model/C/escp2-950.ppd.gz
* usr/share/cups/model/C/escp2-9500.ppd.gz
* usr/share/cups/model/C/escp2-960.ppd.gz
* usr/share/cups/model/C/escp2-9600.ppd.gz
* usr/share/cups/model/C/escp2-980.ppd.gz
* usr/share/cups/model/C/escp2-c20sx.ppd.gz
* usr/share/cups/model/C/escp2-c20ux.ppd.gz
* usr/share/cups/model/C/escp2-c40sx.ppd.gz
* usr/share/cups/model/C/escp2-c40ux.ppd.gz
* usr/share/cups/model/C/escp2-c41sx.ppd.gz
* usr/share/cups/model/C/escp2-c41ux.ppd.gz
* usr/share/cups/model/C/escp2-c42sx.ppd.gz
* usr/share/cups/model/C/escp2-c42ux.ppd.gz
* usr/share/cups/model/C/escp2-c43sx.ppd.gz
* usr/share/cups/model/C/escp2-c43ux.ppd.gz
* usr/share/cups/model/C/escp2-c44sx.ppd.gz
* usr/share/cups/model/C/escp2-c44ux.ppd.gz
* usr/share/cups/model/C/escp2-c50.ppd.gz
* usr/share/cups/model/C/escp2-c60.ppd.gz
* usr/share/cups/model/C/escp2-c61.ppd.gz
* usr/share/cups/model/C/escp2-c62.ppd.gz
* usr/share/cups/model/C/escp2-c63.ppd.gz
* usr/share/cups/model/C/escp2-c64.ppd.gz
* usr/share/cups/model/C/escp2-c70.ppd.gz
* usr/share/cups/model/C/escp2-c80.ppd.gz
* usr/share/cups/model/C/escp2-c82.ppd.gz
* usr/share/cups/model/C/escp2-c83.ppd.gz
* usr/share/cups/model/C/escp2-c84.ppd.gz
* usr/share/cups/model/C/escp2-cl700.ppd.gz
* usr/share/cups/model/C/escp2-cl750.ppd.gz
* usr/share/cups/model/C/escp2-cl760.ppd.gz
* usr/share/cups/model/C/escp2-cx3100.ppd.gz
* usr/share/cups/model/C/escp2-cx3200.ppd.gz
* usr/share/cups/model/C/escp2-cx5100.ppd.gz
* usr/share/cups/model/C/escp2-cx5200.ppd.gz
* usr/share/cups/model/C/escp2-cx6300.ppd.gz
* usr/share/cups/model/C/escp2-cx6400.ppd.gz
* usr/share/cups/model/C/escp2-cx8300.ppd.gz
* usr/share/cups/model/C/escp2-cx8400.ppd.gz
* usr/share/cups/model/C/escp2-em900c.ppd.gz
* usr/share/cups/model/C/escp2-em930c.ppd.gz
* usr/share/cups/model/C/escp2-ex.ppd.gz
* usr/share/cups/model/C/escp2-ex3.ppd.gz
* usr/share/cups/model/C/escp2-mc10000.ppd.gz
* usr/share/cups/model/C/escp2-mc2000.ppd.gz
* usr/share/cups/model/C/escp2-mc5000.ppd.gz
* usr/share/cups/model/C/escp2-mc7000.ppd.gz
* usr/share/cups/model/C/escp2-mc9000.ppd.gz
* usr/share/cups/model/C/escp2-mj5100c.ppd.gz
* usr/share/cups/model/C/escp2-mj6000c.ppd.gz
* usr/share/cups/model/C/escp2-mj8000c.ppd.gz
* usr/share/cups/model/C/escp2-mj930c.ppd.gz
* usr/share/cups/model/C/escp2-ph900.ppd.gz
* usr/share/cups/model/C/escp2-photo.ppd.gz
* usr/share/cups/model/C/escp2-pm10000.ppd.gz
* usr/share/cups/model/C/escp2-pm2000c.ppd.gz
* usr/share/cups/model/C/escp2-pm2200c.ppd.gz
* usr/share/cups/model/C/escp2-pm3000c.ppd.gz
* usr/share/cups/model/C/escp2-pm3300c.ppd.gz
* usr/share/cups/model/C/escp2-pm3500c.ppd.gz
* usr/share/cups/model/C/escp2-pm3700c.ppd.gz
* usr/share/cups/model/C/escp2-pm4000px.ppd.gz
* usr/share/cups/model/C/escp2-pm5000c.ppd.gz
* usr/share/cups/model/C/escp2-pm7000c.ppd.gz
* usr/share/cups/model/C/escp2-pm700c.ppd.gz
* usr/share/cups/model/C/escp2-pm730c.ppd.gz
* usr/share/cups/model/C/escp2-pm740c.ppd.gz
* usr/share/cups/model/C/escp2-pm750c.ppd.gz
* usr/share/cups/model/C/escp2-pm760c.ppd.gz
* usr/share/cups/model/C/escp2-pm770c.ppd.gz
* usr/share/cups/model/C/escp2-pm780c.ppd.gz
* usr/share/cups/model/C/escp2-pm790pt.ppd.gz
* usr/share/cups/model/C/escp2-pm800c.ppd.gz
* usr/share/cups/model/C/escp2-pm850pt.ppd.gz
* usr/share/cups/model/C/escp2-pm870c.ppd.gz
* usr/share/cups/model/C/escp2-pm880c.ppd.gz
* usr/share/cups/model/C/escp2-pm9000c.ppd.gz
* usr/share/cups/model/C/escp2-pm930c.ppd.gz
* usr/share/cups/model/C/escp2-pm950c.ppd.gz
* usr/share/cups/model/C/escp2-pm970c.ppd.gz
* usr/share/cups/model/C/escp2-pro-xl.ppd.gz
* usr/share/cups/model/C/escp2-pro.ppd.gz
* usr/share/cups/model/C/escp2-px7000.ppd.gz
* usr/share/cups/model/C/escp2-px9000.ppd.gz
* usr/share/cups/model/C/escp2-pxv500.ppd.gz
* usr/share/cups/model/C/escp2-scan2000.ppd.gz
* usr/share/cups/model/C/escp2-scan2500.ppd.gz
* usr/share/cups/model/C/escp2.ppd.gz
* usr/share/cups/model/C/lexmark-4076.ppd.gz
* usr/share/cups/model/C/lexmark-z42.ppd.gz
* usr/share/cups/model/C/lexmark-z43.ppd.gz
* usr/share/cups/model/C/lexmark-z52.ppd.gz
* usr/share/cups/model/C/lexmark-z53.ppd.gz
* usr/share/cups/model/C/pcl-1100.ppd.gz
* usr/share/cups/model/C/pcl-1120.ppd.gz
* usr/share/cups/model/C/pcl-1200.ppd.gz
* usr/share/cups/model/C/pcl-1220.ppd.gz
* usr/share/cups/model/C/pcl-1600.ppd.gz
* usr/share/cups/model/C/pcl-2.ppd.gz
* usr/share/cups/model/C/pcl-2000.ppd.gz
* usr/share/cups/model/C/pcl-2500.ppd.gz
* usr/share/cups/model/C/pcl-2p.ppd.gz
* usr/share/cups/model/C/pcl-3.ppd.gz
* usr/share/cups/model/C/pcl-340.ppd.gz
* usr/share/cups/model/C/pcl-4.ppd.gz
* usr/share/cups/model/C/pcl-400.ppd.gz
* usr/share/cups/model/C/pcl-4l.ppd.gz
* usr/share/cups/model/C/pcl-4v.ppd.gz
* usr/share/cups/model/C/pcl-5.ppd.gz
* usr/share/cups/model/C/pcl-500.ppd.gz
* usr/share/cups/model/C/pcl-501.ppd.gz
* usr/share/cups/model/C/pcl-520.ppd.gz
* usr/share/cups/model/C/pcl-540.ppd.gz
* usr/share/cups/model/C/pcl-550.ppd.gz
* usr/share/cups/model/C/pcl-560.ppd.gz
* usr/share/cups/model/C/pcl-5si.ppd.gz
* usr/share/cups/model/C/pcl-6.ppd.gz
* usr/share/cups/model/C/pcl-600.ppd.gz
* usr/share/cups/model/C/pcl-601.ppd.gz
* usr/share/cups/model/C/pcl-690.ppd.gz
* usr/share/cups/model/C/pcl-750.ppd.gz
* usr/share/cups/model/C/pcl-810.ppd.gz
* usr/share/cups/model/C/pcl-812.ppd.gz
* usr/share/cups/model/C/pcl-840.ppd.gz
* usr/share/cups/model/C/pcl-842.ppd.gz
* usr/share/cups/model/C/pcl-845.ppd.gz
* usr/share/cups/model/C/pcl-850.ppd.gz
* usr/share/cups/model/C/pcl-855.ppd.gz
* usr/share/cups/model/C/pcl-870.ppd.gz
* usr/share/cups/model/C/pcl-890.ppd.gz
* usr/share/cups/model/C/pcl-895.ppd.gz
* usr/share/cups/model/C/pcl-900.ppd.gz
* usr/share/cups/model/C/pcl-apple-4100.ppd.gz
* usr/share/cups/model/C/pcl-apple-4500.ppd.gz
* usr/share/cups/model/C/pcl-apple-6500.ppd.gz
* usr/share/cups/model/C/pcl-desnj-230.ppd.gz
* usr/share/cups/model/C/pcl-desnj-250.ppd.gz
* usr/share/cups/model/C/pcl-desnj-2500.ppd.gz
* usr/share/cups/model/C/pcl-desnj-3500.ppd.gz
* usr/share/cups/model/C/pcl-desnj-430.ppd.gz
* usr/share/cups/model/C/pcl-desnj-450.ppd.gz
* usr/share/cups/model/C/pcl-desnj-455.ppd.gz
* usr/share/cups/model/C/pcl-desnj-488.ppd.gz
* usr/share/cups/model/C/pcl-desnj-700.ppd.gz
* usr/share/cups/model/C/pcl-P1000.ppd.gz
* usr/share/cups/model/C/pcl-P1100.ppd.gz
* usr/share/doc/gimp-print-4.2.7/AUTHORS
* usr/share/doc/gimp-print-4.2.7/ChangeLog
* usr/share/doc/gimp-print-4.2.7/COPYING
* usr/share/doc/gimp-print-4.2.7/INSTALL
* usr/share/doc/gimp-print-4.2.7/NEWS
* usr/share/doc/gimp-print-4.2.7/README
* usr/share/gimp-print/doc/gimpprint.ps
* usr/share/gimp-print/doc/html/book1.html
* usr/share/gimp-print/doc/html/c29.html
* usr/share/gimp-print/doc/html/c447.html
* usr/share/gimp-print/doc/html/c570.html
* usr/share/gimp-print/doc/html/ch-gimp-and-gimp-print.html
* usr/share/gimp-print/doc/html/docbook.css
* usr/share/gimp-print/doc/html/figures/cups_admin.png
* usr/share/gimp-print/doc/html/figures/cups_admin_device.png
* usr/share/gimp-print/doc/html/figures/cups_admin_make.png
* usr/share/gimp-print/doc/html/figures/cups_admin_model.png
* usr/share/gimp-print/doc/html/figures/cups_admin_success.png
* usr/share/gimp-print/doc/html/figures/cups_config_printer.png
* usr/share/gimp-print/doc/html/figures/cups_my_printer.png
* usr/share/gimp-print/doc/html/figures/cups_printers.png
* usr/share/gimp-print/doc/html/figures/cups_startup.png
* usr/share/gimp-print/doc/html/figures/gimp-print-gui-1.png
* usr/share/gimp-print/doc/html/figures/gimp-print-gui.png
* usr/share/gimp-print/doc/html/figures/gimp-print-new-printer.png
* usr/share/gimp-print/doc/html/figures/gimp-print-print-color-adjust.png
* usr/share/gimp-print/doc/html/figures/gimp-print-setup.png
* usr/share/gimp-print/doc/html/figures/gimp_image.png
* usr/share/gimp-print/doc/html/figures/gimp_startup.png
* usr/share/gimp-print/doc/html/gfdl.html
* usr/share/gimp-print/doc/html/ln12.html
* usr/share/gimp-print/doc/html/stylesheet-images/caution.gif
* usr/share/gimp-print/doc/html/stylesheet-images/home.gif
* usr/share/gimp-print/doc/html/stylesheet-images/important.gif
* usr/share/gimp-print/doc/html/stylesheet-images/next.gif
* usr/share/gimp-print/doc/html/stylesheet-images/note.gif
* usr/share/gimp-print/doc/html/stylesheet-images/prev.gif
* usr/share/gimp-print/doc/html/stylesheet-images/tip.gif
* usr/share/gimp-print/doc/html/stylesheet-images/toc-blank.gif
* usr/share/gimp-print/doc/html/stylesheet-images/toc-minus.gif
* usr/share/gimp-print/doc/html/stylesheet-images/toc-plus.gif
* usr/share/gimp-print/doc/html/stylesheet-images/up.gif
* usr/share/gimp-print/doc/html/stylesheet-images/warning.gif
* usr/share/gimp-print/doc/html/x456.html
* usr/share/gimp-print/doc/html/x548.html
* usr/share/gimp-print/doc/html/x562.html
* usr/share/gimp-print/doc/html/x642.html
* usr/share/gimp-print/doc/html/x652.html
* usr/share/gimp-print/doc/html/x656.html
* usr/share/gimp-print/doc/html/x662.html
* usr/share/gimp-print/doc/html/x698.html
* usr/share/gimp-print/doc/html/x703.html
* usr/share/gimp-print/doc/html/x707.html
* usr/share/gimp-print/doc/html/x711.html
* usr/share/gimp-print/doc/html/x714.html
* usr/share/gimp-print/doc/html/x717.html
* usr/share/gimp-print/doc/html/x722.html
* usr/share/gimp-print/doc/html/x85.html
* usr/share/gimp-print/doc/manual-html/gimpprint_1.html
* usr/share/gimp-print/doc/manual-html/gimpprint_10.html
* usr/share/gimp-print/doc/manual-html/gimpprint_11.html
* usr/share/gimp-print/doc/manual-html/gimpprint_12.html
* usr/share/gimp-print/doc/manual-html/gimpprint_13.html
* usr/share/gimp-print/doc/manual-html/gimpprint_14.html
* usr/share/gimp-print/doc/manual-html/gimpprint_15.html
* usr/share/gimp-print/doc/manual-html/gimpprint_16.html
* usr/share/gimp-print/doc/manual-html/gimpprint_17.html
* usr/share/gimp-print/doc/manual-html/gimpprint_18.html
* usr/share/gimp-print/doc/manual-html/gimpprint_19.html
* usr/share/gimp-print/doc/manual-html/gimpprint_2.html
* usr/share/gimp-print/doc/manual-html/gimpprint_20.html
* usr/share/gimp-print/doc/manual-html/gimpprint_21.html
* usr/share/gimp-print/doc/manual-html/gimpprint_22.html
* usr/share/gimp-print/doc/manual-html/gimpprint_23.html
* usr/share/gimp-print/doc/manual-html/gimpprint_24.html
* usr/share/gimp-print/doc/manual-html/gimpprint_25.html
* usr/share/gimp-print/doc/manual-html/gimpprint_26.html
* usr/share/gimp-print/doc/manual-html/gimpprint_27.html
* usr/share/gimp-print/doc/manual-html/gimpprint_28.html
* usr/share/gimp-print/doc/manual-html/gimpprint_29.html
* usr/share/gimp-print/doc/manual-html/gimpprint_3.html
* usr/share/gimp-print/doc/manual-html/gimpprint_30.html
* usr/share/gimp-print/doc/manual-html/gimpprint_31.html
* usr/share/gimp-print/doc/manual-html/gimpprint_32.html
* usr/share/gimp-print/doc/manual-html/gimpprint_33.html
* usr/share/gimp-print/doc/manual-html/gimpprint_34.html
* usr/share/gimp-print/doc/manual-html/gimpprint_35.html
* usr/share/gimp-print/doc/manual-html/gimpprint_36.html
* usr/share/gimp-print/doc/manual-html/gimpprint_37.html
* usr/share/gimp-print/doc/manual-html/gimpprint_38.html
* usr/share/gimp-print/doc/manual-html/gimpprint_39.html
* usr/share/gimp-print/doc/manual-html/gimpprint_4.html
* usr/share/gimp-print/doc/manual-html/gimpprint_40.html
* usr/share/gimp-print/doc/manual-html/gimpprint_41.html
* usr/share/gimp-print/doc/manual-html/gimpprint_42.html
* usr/share/gimp-print/doc/manual-html/gimpprint_43.html
* usr/share/gimp-print/doc/manual-html/gimpprint_44.html
* usr/share/gimp-print/doc/manual-html/gimpprint_45.html
* usr/share/gimp-print/doc/manual-html/gimpprint_46.html
* usr/share/gimp-print/doc/manual-html/gimpprint_47.html
* usr/share/gimp-print/doc/manual-html/gimpprint_5.html
* usr/share/gimp-print/doc/manual-html/gimpprint_6.html
* usr/share/gimp-print/doc/manual-html/gimpprint_7.html
* usr/share/gimp-print/doc/manual-html/gimpprint_8.html
* usr/share/gimp-print/doc/manual-html/gimpprint_9.html
* usr/share/gimp-print/doc/manual-html/gimpprint_foot.html
* usr/share/gimp-print/doc/manual-html/gimpprint_toc.html
* usr/share/gimp-print/doc/manual-html/print-color.png
* usr/share/gimp-print/doc/manual-html/print-main.png
* usr/share/gimp-print/doc/manual-html/print-setup.png
* usr/share/gimp-print/doc/users-guide.pdf
* usr/share/gimp-print/samples/colorbars4.png
* usr/share/gimp-print/samples/colorsweep.png
* usr/share/gimp-print/samples/profile.jpg
* usr/share/gimp-print/samples/testpattern.sample
* usr/share/locale/cs/LC_MESSAGES/gimp-print.mo
* usr/share/locale/da/LC_MESSAGES/gimp-print.mo
* usr/share/locale/de/LC_MESSAGES/gimp-print.mo
* usr/share/locale/el/LC_MESSAGES/gimp-print.mo
* usr/share/locale/en_GB/LC_MESSAGES/gimp-print.mo
* usr/share/locale/es/LC_MESSAGES/gimp-print.mo
* usr/share/locale/fr/LC_MESSAGES/gimp-print.mo
* usr/share/locale/hu/LC_MESSAGES/gimp-print.mo
* usr/share/locale/ja/LC_MESSAGES/gimp-print.mo
* usr/share/locale/nb/LC_MESSAGES/gimp-print.mo
* usr/share/locale/nl/LC_MESSAGES/gimp-print.mo
* usr/share/locale/no/LC_MESSAGES/gimp-print.mo
* usr/share/locale/pl/LC_MESSAGES/gimp-print.mo
* usr/share/locale/pt/LC_MESSAGES/gimp-print.mo
* usr/share/locale/sk/LC_MESSAGES/gimp-print.mo
* usr/share/locale/sv/LC_MESSAGES/gimp-print.mo
* usr/share/locale/uk/LC_MESSAGES/gimp-print.mo
{{< /spoiler >}}