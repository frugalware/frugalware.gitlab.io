+++
draft = false
title = "libgphoto2 2.5.31-2"
version = "2.5.31-2"
description = "A portable library to gives access to many digital cameras"
date = "2024-01-06T13:47:33"
aliases = "/packages/3177"
categories = ['lib']
upstreamurl = "http://www.gphoto.org"
arch = "x86_64"
size = "1251704"
usize = "6909057"
sha1sum = "d33e3dd69471511e252d874d81479eae887153c0"
depends = "['gd>=2.1.1-3', 'libexif>=0.6.21-3', 'libffi>=3.2.1-2', 'libjpeg-turbo', 'libtool', 'libudev>=242', 'libusb1>=1.0.20-5']"
reverse_depends = "['darktable', 'gphoto2', 'opencv', 'sane-backends', 'wine', 'wine-devel', 'xsane']"
+++
A portable library to gives access to many digital cameras{{< files text="show files" >}}* /usr/bin/gphoto2-config
* /usr/bin/gphoto2-port-config
* /usr/include/gphoto2/gphoto2-abilities-list.h
* /usr/include/gphoto2/gphoto2-camera.h
* /usr/include/gphoto2/gphoto2-context.h
* /usr/include/gphoto2/gphoto2-file.h
* /usr/include/gphoto2/gphoto2-filesys.h
* /usr/include/gphoto2/gphoto2-library.h
* /usr/include/gphoto2/gphoto2-list.h
* /usr/include/gphoto2/gphoto2-port-info-list.h
* /usr/include/gphoto2/gphoto2-port-log.h
* /usr/include/gphoto2/gphoto2-port-portability.h
* /usr/include/gphoto2/gphoto2-port-result.h
* /usr/include/gphoto2/gphoto2-port-version.h
* /usr/include/gphoto2/gphoto2-port.h
* /usr/include/gphoto2/gphoto2-result.h
* /usr/include/gphoto2/gphoto2-setting.h
* /usr/include/gphoto2/gphoto2-version.h
* /usr/include/gphoto2/gphoto2-widget.h
* /usr/include/gphoto2/gphoto2.h
* /usr/lib/libgphoto2.so
* /usr/lib/libgphoto2.so.6
* /usr/lib/libgphoto2.so.6.3.0
* /usr/lib/libgphoto2/2.5.31/ax203.so
* /usr/lib/libgphoto2/2.5.31/canon.so
* /usr/lib/libgphoto2/2.5.31/digigr8.so
* /usr/lib/libgphoto2/2.5.31/dimagev.so
* /usr/lib/libgphoto2/2.5.31/directory.so
* /usr/lib/libgphoto2/2.5.31/docupen.so
* /usr/lib/libgphoto2/2.5.31/jl2005a.so
* /usr/lib/libgphoto2/2.5.31/jl2005c.so
* /usr/lib/libgphoto2/2.5.31/kodak_dc240.so
* /usr/lib/libgphoto2/2.5.31/mars.so
* /usr/lib/libgphoto2/2.5.31/pentax.so
* /usr/lib/libgphoto2/2.5.31/ptp2.so
* /usr/lib/libgphoto2/2.5.31/ricoh_g3.so
* /usr/lib/libgphoto2/2.5.31/sierra.so
* /usr/lib/libgphoto2/2.5.31/sonix.so
* /usr/lib/libgphoto2/2.5.31/sq905.so
* /usr/lib/libgphoto2/2.5.31/st2205.so
* /usr/lib/libgphoto2/2.5.31/topfield.so
* /usr/lib/libgphoto2/2.5.31/tp6801.so
* /usr/lib/libgphoto2/print-camera-list
* /usr/lib/libgphoto2_port.so
* /usr/lib/libgphoto2_port.so.12
* /usr/lib/libgphoto2_port.so.12.2.0
* /usr/lib/libgphoto2_port/0.12.2/disk.so
* /usr/lib/libgphoto2_port/0.12.2/ptpip.so
* /usr/lib/libgphoto2_port/0.12.2/serial.so
* /usr/lib/libgphoto2_port/0.12.2/usb1.so
* /usr/lib/libgphoto2_port/0.12.2/usbdiskdirect.so
* /usr/lib/libgphoto2_port/0.12.2/usbscsi.so
* /usr/lib/pkgconfig/libgphoto2.pc
* /usr/lib/pkgconfig/libgphoto2_port.pc
* /usr/lib/udev/check-ptp-camera
* /usr/lib/udev/rules.d/40-libgphoto2.rules
* /usr/share/doc/libgphoto2-2.5.31/ABOUT-NLS
* /usr/share/doc/libgphoto2-2.5.31/AUTHORS
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.9050
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.9051
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.9052
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.905C
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.913C
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.913D
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.adc65
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.agfa-cl20
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.aox
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.ax203
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.ax203-compression
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.canon
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.clicksmart310
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.enigma13
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.gsmart300
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.iclick
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.jamcam
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.jl2005a
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.jl2005bcd-compression
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.jl2005c
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.konica
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.largan-lmini
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.lg_gsm
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.mars
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.minolta-dimagev
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.mustek
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.panasonic
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.panasonic-coolshot
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.panasonic-l859
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.pccam300
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.pccam600
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.pentax
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.ptp2
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.smal
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.sonix
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.sonydscf1
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.soundvision
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.spca50x
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.sq905
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.st2205
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.st2205-compression
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.toshiba-pdrm11
* /usr/share/doc/libgphoto2-2.5.31/camlibs/README.tp6801
* /usr/share/doc/libgphoto2-2.5.31/ChangeLog
* /usr/share/doc/libgphoto2-2.5.31/COPYING
* /usr/share/doc/libgphoto2-2.5.31/INSTALL
* /usr/share/doc/libgphoto2-2.5.31/NEWS
* /usr/share/doc/libgphoto2-2.5.31/README
* /usr/share/doc/libgphoto2-2.5.31/README.md
* /usr/share/doc/libgphoto2-2.5.31/README.packaging
* /usr/share/doc/libgphoto2-2.5.31/RELEASE-HOWTO.md
* /usr/share/libgphoto2/2.5.31/konica/english
* /usr/share/libgphoto2/2.5.31/konica/french
* /usr/share/libgphoto2/2.5.31/konica/german
* /usr/share/libgphoto2/2.5.31/konica/japanese
* /usr/share/libgphoto2/2.5.31/konica/korean
* /usr/share/libgphoto2/2.5.31/konica/spanish
* /usr/share/libgphoto2_port/0.12.2/vcamera/README.txt
* /usr/share/locale/cs/LC_MESSAGES/libgphoto2-6.mo
* /usr/share/locale/cs/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/da/LC_MESSAGES/libgphoto2-6.mo
* /usr/share/locale/da/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/de/LC_MESSAGES/libgphoto2-6.mo
* /usr/share/locale/de/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/es/LC_MESSAGES/libgphoto2-6.mo
* /usr/share/locale/es/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/eu/LC_MESSAGES/libgphoto2-6.mo
* /usr/share/locale/eu/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/fi/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/fr/LC_MESSAGES/libgphoto2-6.mo
* /usr/share/locale/fr/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/hu/LC_MESSAGES/libgphoto2-6.mo
* /usr/share/locale/it/LC_MESSAGES/libgphoto2-6.mo
* /usr/share/locale/it/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/ja/LC_MESSAGES/libgphoto2-6.mo
* /usr/share/locale/ja/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/nl/LC_MESSAGES/libgphoto2-6.mo
* /usr/share/locale/nl/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/pl/LC_MESSAGES/libgphoto2-6.mo
* /usr/share/locale/pl/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/ro/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/ru/LC_MESSAGES/libgphoto2-6.mo
* /usr/share/locale/ru/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/sk/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/sr/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/sv/LC_MESSAGES/libgphoto2-6.mo
* /usr/share/locale/sv/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/uk/LC_MESSAGES/libgphoto2-6.mo
* /usr/share/locale/uk/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/vi/LC_MESSAGES/libgphoto2-6.mo
* /usr/share/locale/vi/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/libgphoto2-6.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/libgphoto2_port-12.mo
* /usr/share/man/man3/libgphoto2.3.gz
* /usr/share/man/man3/libgphoto2_port.3.gz
{{< /files >}}