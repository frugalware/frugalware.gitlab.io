+++
draft = false
title = "weston 14.0.2-1"
version = "14.0.2-1"
description = "Wayland Default Display Compositor"
date = "2025-04-29T13:19:27"
aliases = "/packages/168990"
categories = ['x11-extra']
upstreamurl = "http://wayland.freedesktop.org/"
arch = "x86_64"
size = "1296040"
usize = "5066654"
sha1sum = "ec3c13687904efea26767c51fa5401e319f1843e"
depends = "['freerdp', 'gst1-plugins-base', 'lcms2', 'libdisplay-info>=0.2.0', 'libgbm', 'libglvnd', 'libinput', 'libva', 'libwebp', 'libxcursor', 'libxkbcommon', 'neatvnc', 'pango', 'pipewire', 'seatd', 'wayland']"
+++
### Description: 
Wayland Default Display Compositor

### Files: 
* /etc/pam.d/weston-remote-access
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
* /usr/include/libweston-14/libweston/backend-drm.h
* /usr/include/libweston-14/libweston/backend-headless.h
* /usr/include/libweston-14/libweston/backend-pipewire.h
* /usr/include/libweston-14/libweston/backend-rdp.h
* /usr/include/libweston-14/libweston/backend-vnc.h
* /usr/include/libweston-14/libweston/backend-wayland.h
* /usr/include/libweston-14/libweston/backend-x11.h
* /usr/include/libweston-14/libweston/config-parser.h
* /usr/include/libweston-14/libweston/desktop.h
* /usr/include/libweston-14/libweston/libweston.h
* /usr/include/libweston-14/libweston/matrix.h
* /usr/include/libweston-14/libweston/pipewire-plugin.h
* /usr/include/libweston-14/libweston/plugin-registry.h
* /usr/include/libweston-14/libweston/remoting-plugin.h
* /usr/include/libweston-14/libweston/shell-utils.h
* /usr/include/libweston-14/libweston/version.h
* /usr/include/libweston-14/libweston/weston-log.h
* /usr/include/libweston-14/libweston/windowed-output-api.h
* /usr/include/libweston-14/libweston/xwayland-api.h
* /usr/include/libweston-14/libweston/zalloc.h
* /usr/include/weston/ivi-layout-export.h
* /usr/include/weston/weston.h
* /usr/lib/libweston-14.so
* /usr/lib/libweston-14.so.0
* /usr/lib/libweston-14.so.0.0.2
* /usr/lib/libweston-14/color-lcms.so
* /usr/lib/libweston-14/drm-backend.so
* /usr/lib/libweston-14/gl-renderer.so
* /usr/lib/libweston-14/headless-backend.so
* /usr/lib/libweston-14/pipewire-backend.so
* /usr/lib/libweston-14/pipewire-plugin.so
* /usr/lib/libweston-14/rdp-backend.so
* /usr/lib/libweston-14/remoting-plugin.so
* /usr/lib/libweston-14/vnc-backend.so
* /usr/lib/libweston-14/wayland-backend.so
* /usr/lib/libweston-14/x11-backend.so
* /usr/lib/libweston-14/xwayland.so
* /usr/lib/pkgconfig/libweston-14.pc
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
* /usr/share/doc/weston-14.0.2/COPYING
* /usr/share/doc/weston-14.0.2/README.md
* /usr/share/libweston-14/protocols/weston-content-protection.xml
* /usr/share/libweston-14/protocols/weston-debug.xml
* /usr/share/libweston-14/protocols/weston-direct-display.xml
* /usr/share/libweston-14/protocols/weston-output-capture.xml
* /usr/share/man/man1/weston-debug.1.gz
* /usr/share/man/man1/weston.1.gz
* /usr/share/man/man5/weston.ini.5.gz
* /usr/share/man/man7/weston-bindings.7.gz
* /usr/share/man/man7/weston-drm.7.gz
* /usr/share/man/man7/weston-rdp.7.gz
* /usr/share/man/man7/weston-vnc.7.gz
* /usr/share/pkgconfig/libweston-14-protocols.pc
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
