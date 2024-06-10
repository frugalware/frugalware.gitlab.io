+++
draft = false
title = "weston 13.0.3-1"
version = "13.0.3-1"
description = "Wayland Default Display Compositor"
date = "2024-06-10T20:32:24"
aliases = "/packages/168990"
categories = ['x11-extra']
upstreamurl = "http://wayland.freedesktop.org/"
arch = "x86_64"
size = "1200388"
usize = "4612843"
sha1sum = "5dac6135ae8abe7abc5ec6d7df3c80a6b8d9ff0e"
depends = "['gst1-plugins-base', 'lcms2', 'libdisplay-info', 'libgbm', 'libglvnd', 'libinput', 'libva', 'libwebp', 'libxcursor', 'libxkbcommon', 'pango', 'pipewire', 'seatd', 'wayland']"
+++
### Description: 
Wayland Default Display Compositor

### Files: 
* /usr/bin/wcap-decode
* /usr/bin/weston
* /usr/bin/weston-calibrator
* /usr/bin/weston-clickdot
* /usr/bin/weston-cliptest
* /usr/bin/weston-constraints
* /usr/bin/weston-content_protection
* /usr/bin/weston-debug
* /usr/bin/weston-dnd
* /usr/bin/weston-editor
* /usr/bin/weston-eventdemo
* /usr/bin/weston-flower
* /usr/bin/weston-fullscreen
* /usr/bin/weston-image
* /usr/bin/weston-multi-resource
* /usr/bin/weston-presentation-shm
* /usr/bin/weston-resizor
* /usr/bin/weston-scaler
* /usr/bin/weston-screenshooter
* /usr/bin/weston-simple-damage
* /usr/bin/weston-simple-dmabuf-egl
* /usr/bin/weston-simple-dmabuf-feedback
* /usr/bin/weston-simple-dmabuf-v4l
* /usr/bin/weston-simple-egl
* /usr/bin/weston-simple-shm
* /usr/bin/weston-simple-touch
* /usr/bin/weston-smoke
* /usr/bin/weston-stacking
* /usr/bin/weston-subsurfaces
* /usr/bin/weston-tablet
* /usr/bin/weston-terminal
* /usr/bin/weston-touch-calibrator
* /usr/bin/weston-transformed
* /usr/include/libweston-13/libweston/backend-drm.h
* /usr/include/libweston-13/libweston/backend-headless.h
* /usr/include/libweston-13/libweston/backend-pipewire.h
* /usr/include/libweston-13/libweston/backend-wayland.h
* /usr/include/libweston-13/libweston/backend-x11.h
* /usr/include/libweston-13/libweston/config-parser.h
* /usr/include/libweston-13/libweston/desktop.h
* /usr/include/libweston-13/libweston/libweston.h
* /usr/include/libweston-13/libweston/matrix.h
* /usr/include/libweston-13/libweston/pipewire-plugin.h
* /usr/include/libweston-13/libweston/plugin-registry.h
* /usr/include/libweston-13/libweston/remoting-plugin.h
* /usr/include/libweston-13/libweston/shell-utils.h
* /usr/include/libweston-13/libweston/version.h
* /usr/include/libweston-13/libweston/weston-log.h
* /usr/include/libweston-13/libweston/windowed-output-api.h
* /usr/include/libweston-13/libweston/xwayland-api.h
* /usr/include/libweston-13/libweston/zalloc.h
* /usr/include/weston/ivi-layout-export.h
* /usr/include/weston/weston.h
* /usr/lib/libweston-13.so
* /usr/lib/libweston-13.so.0
* /usr/lib/libweston-13.so.0.0.3
* /usr/lib/libweston-13/color-lcms.so
* /usr/lib/libweston-13/drm-backend.so
* /usr/lib/libweston-13/gl-renderer.so
* /usr/lib/libweston-13/headless-backend.so
* /usr/lib/libweston-13/pipewire-backend.so
* /usr/lib/libweston-13/pipewire-plugin.so
* /usr/lib/libweston-13/remoting-plugin.so
* /usr/lib/libweston-13/wayland-backend.so
* /usr/lib/libweston-13/x11-backend.so
* /usr/lib/libweston-13/xwayland.so
* /usr/lib/pkgconfig/libweston-13.pc
* /usr/lib/pkgconfig/weston.pc
* /usr/lib/weston/desktop-shell.so
* /usr/lib/weston/fullscreen-shell.so
* /usr/lib/weston/hmi-controller.so
* /usr/lib/weston/ivi-shell.so
* /usr/lib/weston/kiosk-shell.so
* /usr/lib/weston/libexec_weston.so
* /usr/lib/weston/libexec_weston.so.0
* /usr/lib/weston/libexec_weston.so.0.0.0
* /usr/lib/weston/screen-share.so
* /usr/lib/weston/systemd-notify.so
* /usr/lib/weston/weston-desktop-shell
* /usr/lib/weston/weston-ivi-shell-user-interface
* /usr/lib/weston/weston-keyboard
* /usr/lib/weston/weston-simple-im
* /usr/share/doc/weston-13.0.3/COPYING
* /usr/share/doc/weston-13.0.3/README.md
* /usr/share/libweston-13/protocols/weston-content-protection.xml
* /usr/share/libweston-13/protocols/weston-debug.xml
* /usr/share/libweston-13/protocols/weston-direct-display.xml
* /usr/share/libweston-13/protocols/weston-output-capture.xml
* /usr/share/man/man1/weston-debug.1.gz
* /usr/share/man/man1/weston.1.gz
* /usr/share/man/man5/weston.ini.5.gz
* /usr/share/man/man7/weston-bindings.7.gz
* /usr/share/man/man7/weston-drm.7.gz
* /usr/share/pkgconfig/libweston-13-protocols.pc
* /usr/share/wayland-sessions/weston.desktop
* /usr/share/weston/background.png
* /usr/share/weston/border.png
* /usr/share/weston/fullscreen.png
* /usr/share/weston/home.png
* /usr/share/weston/icon_editor.png
* /usr/share/weston/icon_flower.png
* /usr/share/weston/icon_ivi_clickdot.png
* /usr/share/weston/icon_ivi_flower.png
* /usr/share/weston/icon_ivi_simple-egl.png
* /usr/share/weston/icon_ivi_simple-shm.png
* /usr/share/weston/icon_ivi_smoke.png
* /usr/share/weston/icon_terminal.png
* /usr/share/weston/icon_window.png
* /usr/share/weston/panel.png
* /usr/share/weston/pattern.png
* /usr/share/weston/random.png
* /usr/share/weston/sidebyside.png
* /usr/share/weston/sign_close.png
* /usr/share/weston/sign_maximize.png
* /usr/share/weston/sign_minimize.png
* /usr/share/weston/terminal.png
* /usr/share/weston/tiling.png
* /usr/share/weston/wayland.png
* /usr/share/weston/wayland.svg
