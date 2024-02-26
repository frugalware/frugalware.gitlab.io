+++
draft = false
title = "libxi 1.8.1-2"
version = "1.8.1-2"
description = "X inputextension library"
date = "2023-09-05T11:04:25"
aliases = "/packages/4796"
categories = ['x11']
upstreamurl = "http://xorg.freedesktop.org"
arch = "x86_64"
size = "197024"
usize = "697353"
sha1sum = "7cbd17e711ad7aa3efb42aaecb5d457b7f8470f9"
depends = "['libx11>=1.6.8', 'libxext>=1.3.3-3', 'libxfixes>=5.0.3']"
reverse_depends = "['blender', 'box2d', 'efl', 'enlightenment', 'flightgear', 'fox', 'freeglut', 'geogram', 'gtk+2-libs', 'gtk+3', 'gtk+4', 'guarddog', 'kasablanca', 'kat', 'kitty', 'klamav', 'knetstats', 'knoda', 'ksniffer', 'ksubeditor', 'ksubtile', 'kzenexplorer', 'libxtst', 'maxemumtvguide', 'mlt-qt', 'mupdf', 'opendiablo2', 'qscintilla2', 'qt5-base', 'qt6-base', 'terminology', 'whalebird', 'wine', 'wine-devel', 'xeyes', 'xf86-input-synaptics', 'xf86-input-wacom', 'xinput', 'xsetmode', 'xsetpointer']"
license = "GPL2"
+++
X inputextension library{{< files text="show files" >}}* /usr/include/X11/extensions/XInput.h
* /usr/include/X11/extensions/XInput2.h
* /usr/lib/libXi.so
* /usr/lib/libXi.so.6
* /usr/lib/libXi.so.6.1.0
* /usr/lib/pkgconfig/xi.pc
* /usr/share/doc/libxi-1.8.1/ChangeLog
* /usr/share/doc/libxi-1.8.1/COPYING
* /usr/share/doc/libxi-1.8.1/encoding.xml
* /usr/share/doc/libxi-1.8.1/inputlib.xml
* /usr/share/doc/libxi-1.8.1/INSTALL
* /usr/share/doc/libxi-1.8.1/library.xml
* /usr/share/doc/libxi-1.8.1/README.md
* /usr/share/man/man3/XAllowDeviceEvents.3.gz
* /usr/share/man/man3/XChangeDeviceControl.3.gz
* /usr/share/man/man3/XChangeDeviceDontPropagateList.3.gz
* /usr/share/man/man3/XChangeDeviceKeyMapping.3.gz
* /usr/share/man/man3/XChangeDeviceProperty.3.gz
* /usr/share/man/man3/XChangeFeedbackControl.3.gz
* /usr/share/man/man3/XChangeKeyboardDevice.3.gz
* /usr/share/man/man3/XChangePointerDevice.3.gz
* /usr/share/man/man3/XCloseDevice.3.gz
* /usr/share/man/man3/XDeleteDeviceProperty.3.gz
* /usr/share/man/man3/XDeviceBell.3.gz
* /usr/share/man/man3/XDeviceTimeCoord.3.gz
* /usr/share/man/man3/XFreeDeviceList.3.gz
* /usr/share/man/man3/XGetDeviceButtonMapping.3.gz
* /usr/share/man/man3/XGetDeviceControl.3.gz
* /usr/share/man/man3/XGetDeviceDontPropagateList.3.gz
* /usr/share/man/man3/XGetDeviceFocus.3.gz
* /usr/share/man/man3/XGetDeviceKeyMapping.3.gz
* /usr/share/man/man3/XGetDeviceModifierMapping.3.gz
* /usr/share/man/man3/XGetDeviceMotionEvents.3.gz
* /usr/share/man/man3/XGetDeviceProperty.3.gz
* /usr/share/man/man3/XGetExtensionVersion.3.gz
* /usr/share/man/man3/XGetFeedbackControl.3.gz
* /usr/share/man/man3/XGetSelectedExtensionEvents.3.gz
* /usr/share/man/man3/XGrabDevice.3.gz
* /usr/share/man/man3/XGrabDeviceButton.3.gz
* /usr/share/man/man3/XGrabDeviceKey.3.gz
* /usr/share/man/man3/XIAllowEvents.3.gz
* /usr/share/man/man3/XIBarrierReleasePointer.3.gz
* /usr/share/man/man3/XIBarrierReleasePointers.3.gz
* /usr/share/man/man3/XIChangeHierarchy.3.gz
* /usr/share/man/man3/XIChangeProperty.3.gz
* /usr/share/man/man3/XIDefineCursor.3.gz
* /usr/share/man/man3/XIDeleteProperty.3.gz
* /usr/share/man/man3/XIFreeDeviceInfo.3.gz
* /usr/share/man/man3/XIGetClientPointer.3.gz
* /usr/share/man/man3/XIGetFocus.3.gz
* /usr/share/man/man3/XIGetProperty.3.gz
* /usr/share/man/man3/XIGetSelectedEvents.3.gz
* /usr/share/man/man3/XIGrabButton.3.gz
* /usr/share/man/man3/XIGrabDevice.3.gz
* /usr/share/man/man3/XIGrabEnter.3.gz
* /usr/share/man/man3/XIGrabFocusIn.3.gz
* /usr/share/man/man3/XIGrabKeycode.3.gz
* /usr/share/man/man3/XIGrabTouchBegin.3.gz
* /usr/share/man/man3/XIListProperties.3.gz
* /usr/share/man/man3/XIQueryDevice.3.gz
* /usr/share/man/man3/XIQueryPointer.3.gz
* /usr/share/man/man3/XIQueryVersion.3.gz
* /usr/share/man/man3/XISelectEvents.3.gz
* /usr/share/man/man3/XISetClientPointer.3.gz
* /usr/share/man/man3/XISetFocus.3.gz
* /usr/share/man/man3/XIUndefineCursor.3.gz
* /usr/share/man/man3/XIUngrabButton.3.gz
* /usr/share/man/man3/XIUngrabDevice.3.gz
* /usr/share/man/man3/XIUngrabEnter.3.gz
* /usr/share/man/man3/XIUngrabFocusIn.3.gz
* /usr/share/man/man3/XIUngrabKeycode.3.gz
* /usr/share/man/man3/XIUngrabTouchBegin.3.gz
* /usr/share/man/man3/XIWarpPointer.3.gz
* /usr/share/man/man3/XListDeviceProperties.3.gz
* /usr/share/man/man3/XListInputDevices.3.gz
* /usr/share/man/man3/XOpenDevice.3.gz
* /usr/share/man/man3/XQueryDeviceState.3.gz
* /usr/share/man/man3/XSelectExtensionEvent.3.gz
* /usr/share/man/man3/XSendExtensionEvent.3.gz
* /usr/share/man/man3/XSetDeviceButtonMapping.3.gz
* /usr/share/man/man3/XSetDeviceFocus.3.gz
* /usr/share/man/man3/XSetDeviceMode.3.gz
* /usr/share/man/man3/XSetDeviceModifierMapping.3.gz
* /usr/share/man/man3/XSetDeviceValuators.3.gz
* /usr/share/man/man3/XUngrabDevice.3.gz
* /usr/share/man/man3/XUngrabDeviceButton.3.gz
* /usr/share/man/man3/XUngrabDeviceKey.3.gz
{{< /files >}}