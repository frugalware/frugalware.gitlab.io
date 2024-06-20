+++
draft = false
title = "wireplumber 0.5.3-2"
version = "0.5.3-2"
description = "Session / policy manager implementation for PipeWire"
date = "2024-06-20T17:16:00"
aliases = "/packages/220823"
categories = ['apps-extra']
upstreamurl = "https://pipewire.pages.freedesktop.org/wireplumber/"
arch = "x86_64"
size = "337448"
usize = "1423602"
sha1sum = "45f47c9dc0069ef31d3d6e6ecc6c3ca899432314"
depends = "['lua', 'pipewire']"
reverse_depends = "['gst1-plugins-pipewire', 'pipewire-alsa', 'pipewire-jack', 'pipewire-pulse', 'pipewire-x11']"
+++
### Description: 
Session / policy manager implementation for PipeWire

### Files: 
* /usr/bin/wireplumber
* /usr/bin/wpctl
* /usr/bin/wpexec
* /usr/include/wireplumber-0.5/wp/base-dirs.h
* /usr/include/wireplumber-0.5/wp/client.h
* /usr/include/wireplumber-0.5/wp/component-loader.h
* /usr/include/wireplumber-0.5/wp/conf.h
* /usr/include/wireplumber-0.5/wp/core.h
* /usr/include/wireplumber-0.5/wp/defs.h
* /usr/include/wireplumber-0.5/wp/device.h
* /usr/include/wireplumber-0.5/wp/error.h
* /usr/include/wireplumber-0.5/wp/event-dispatcher.h
* /usr/include/wireplumber-0.5/wp/event-hook.h
* /usr/include/wireplumber-0.5/wp/event.h
* /usr/include/wireplumber-0.5/wp/factory.h
* /usr/include/wireplumber-0.5/wp/global-proxy.h
* /usr/include/wireplumber-0.5/wp/iterator.h
* /usr/include/wireplumber-0.5/wp/json-utils.h
* /usr/include/wireplumber-0.5/wp/link.h
* /usr/include/wireplumber-0.5/wp/log.h
* /usr/include/wireplumber-0.5/wp/metadata.h
* /usr/include/wireplumber-0.5/wp/module.h
* /usr/include/wireplumber-0.5/wp/node.h
* /usr/include/wireplumber-0.5/wp/object-interest.h
* /usr/include/wireplumber-0.5/wp/object-manager.h
* /usr/include/wireplumber-0.5/wp/object.h
* /usr/include/wireplumber-0.5/wp/plugin.h
* /usr/include/wireplumber-0.5/wp/port.h
* /usr/include/wireplumber-0.5/wp/properties.h
* /usr/include/wireplumber-0.5/wp/proxy-interfaces.h
* /usr/include/wireplumber-0.5/wp/proxy.h
* /usr/include/wireplumber-0.5/wp/session-item.h
* /usr/include/wireplumber-0.5/wp/settings.h
* /usr/include/wireplumber-0.5/wp/si-factory.h
* /usr/include/wireplumber-0.5/wp/si-interfaces.h
* /usr/include/wireplumber-0.5/wp/spa-json.h
* /usr/include/wireplumber-0.5/wp/spa-pod.h
* /usr/include/wireplumber-0.5/wp/spa-type.h
* /usr/include/wireplumber-0.5/wp/state.h
* /usr/include/wireplumber-0.5/wp/transition.h
* /usr/include/wireplumber-0.5/wp/wp.h
* /usr/include/wireplumber-0.5/wp/wpenums.h
* /usr/include/wireplumber-0.5/wp/wpversion.h
* /usr/lib/libwireplumber-0.5.so
* /usr/lib/libwireplumber-0.5.so.0
* /usr/lib/libwireplumber-0.5.so.0.503.0
* /usr/lib/pkgconfig/wireplumber-0.5.pc
* /usr/lib/systemd/user/wireplumber.service
* /usr/lib/systemd/user/wireplumber@.service
* /usr/lib/wireplumber-0.5/libwireplumber-module-dbus-connection.so
* /usr/lib/wireplumber-0.5/libwireplumber-module-default-nodes-api.so
* /usr/lib/wireplumber-0.5/libwireplumber-module-file-monitor-api.so
* /usr/lib/wireplumber-0.5/libwireplumber-module-log-settings.so
* /usr/lib/wireplumber-0.5/libwireplumber-module-logind.so
* /usr/lib/wireplumber-0.5/libwireplumber-module-lua-scripting.so
* /usr/lib/wireplumber-0.5/libwireplumber-module-mixer-api.so
* /usr/lib/wireplumber-0.5/libwireplumber-module-portal-permissionstore.so
* /usr/lib/wireplumber-0.5/libwireplumber-module-reserve-device.so
* /usr/lib/wireplumber-0.5/libwireplumber-module-settings.so
* /usr/lib/wireplumber-0.5/libwireplumber-module-si-audio-adapter.so
* /usr/lib/wireplumber-0.5/libwireplumber-module-si-audio-virtual.so
* /usr/lib/wireplumber-0.5/libwireplumber-module-si-node.so
* /usr/lib/wireplumber-0.5/libwireplumber-module-si-standard-link.so
* /usr/lib/wireplumber-0.5/libwireplumber-module-standard-event-source.so
* /usr/share/doc/wireplumber-0.5.3/LICENSE
* /usr/share/doc/wireplumber-0.5.3/README.rst
* /usr/share/doc/wireplumber/examples/wireplumber.conf.d/access.conf
* /usr/share/doc/wireplumber/examples/wireplumber.conf.d/alsa.conf
* /usr/share/doc/wireplumber/examples/wireplumber.conf.d/bluetooth.conf
* /usr/share/doc/wireplumber/examples/wireplumber.conf.d/device.conf
* /usr/share/doc/wireplumber/examples/wireplumber.conf.d/libcamera.conf
* /usr/share/doc/wireplumber/examples/wireplumber.conf.d/linking.conf
* /usr/share/doc/wireplumber/examples/wireplumber.conf.d/log.conf
* /usr/share/doc/wireplumber/examples/wireplumber.conf.d/stream.conf
* /usr/share/doc/wireplumber/examples/wireplumber.conf.d/v4l2.conf
* /usr/share/doc/wireplumber/examples/wireplumber.conf.d/virtual.conf
* /usr/share/wireplumber/scripts/client/access-default.lua
* /usr/share/wireplumber/scripts/client/access-portal.lua
* /usr/share/wireplumber/scripts/client/access-snap.lua
* /usr/share/wireplumber/scripts/default-nodes/apply-default-node.lua
* /usr/share/wireplumber/scripts/default-nodes/find-best-default-node.lua
* /usr/share/wireplumber/scripts/default-nodes/find-selected-default-node.lua
* /usr/share/wireplumber/scripts/default-nodes/rescan.lua
* /usr/share/wireplumber/scripts/default-nodes/state-default-nodes.lua
* /usr/share/wireplumber/scripts/device/apply-profile.lua
* /usr/share/wireplumber/scripts/device/apply-routes.lua
* /usr/share/wireplumber/scripts/device/autoswitch-bluetooth-profile.lua
* /usr/share/wireplumber/scripts/device/find-best-profile.lua
* /usr/share/wireplumber/scripts/device/find-best-routes.lua
* /usr/share/wireplumber/scripts/device/find-preferred-profile.lua
* /usr/share/wireplumber/scripts/device/select-profile.lua
* /usr/share/wireplumber/scripts/device/select-routes.lua
* /usr/share/wireplumber/scripts/device/state-profile.lua
* /usr/share/wireplumber/scripts/device/state-routes.lua
* /usr/share/wireplumber/scripts/fallback-sink.lua
* /usr/share/wireplumber/scripts/intended-roles.lua
* /usr/share/wireplumber/scripts/lib/common-utils.lua
* /usr/share/wireplumber/scripts/lib/device-info-cache.lua
* /usr/share/wireplumber/scripts/lib/filter-utils.lua
* /usr/share/wireplumber/scripts/lib/linking-utils.lua
* /usr/share/wireplumber/scripts/lib/monitor-utils.lua
* /usr/share/wireplumber/scripts/lib/node-utils.lua
* /usr/share/wireplumber/scripts/linking/find-best-target.lua
* /usr/share/wireplumber/scripts/linking/find-default-target.lua
* /usr/share/wireplumber/scripts/linking/find-defined-target.lua
* /usr/share/wireplumber/scripts/linking/find-filter-target.lua
* /usr/share/wireplumber/scripts/linking/find-user-target.lua.example
* /usr/share/wireplumber/scripts/linking/find-virtual-target.lua
* /usr/share/wireplumber/scripts/linking/get-filter-from-target.lua
* /usr/share/wireplumber/scripts/linking/link-target.lua
* /usr/share/wireplumber/scripts/linking/prepare-link.lua
* /usr/share/wireplumber/scripts/linking/rescan-virtual-links.lua
* /usr/share/wireplumber/scripts/linking/rescan.lua
* /usr/share/wireplumber/scripts/metadata.lua
* /usr/share/wireplumber/scripts/monitors/alsa-midi.lua
* /usr/share/wireplumber/scripts/monitors/alsa.lua
* /usr/share/wireplumber/scripts/monitors/bluez-midi.lua
* /usr/share/wireplumber/scripts/monitors/bluez.lua
* /usr/share/wireplumber/scripts/monitors/libcamera/create-device.lua
* /usr/share/wireplumber/scripts/monitors/libcamera/create-node.lua
* /usr/share/wireplumber/scripts/monitors/libcamera/enumerate-device.lua
* /usr/share/wireplumber/scripts/monitors/libcamera/name-device.lua
* /usr/share/wireplumber/scripts/monitors/libcamera/name-node.lua
* /usr/share/wireplumber/scripts/monitors/v4l2/create-device.lua
* /usr/share/wireplumber/scripts/monitors/v4l2/create-node.lua
* /usr/share/wireplumber/scripts/monitors/v4l2/enumerate-device.lua
* /usr/share/wireplumber/scripts/monitors/v4l2/name-device.lua
* /usr/share/wireplumber/scripts/monitors/v4l2/name-node.lua
* /usr/share/wireplumber/scripts/node/create-item.lua
* /usr/share/wireplumber/scripts/node/create-virtual-item.lua
* /usr/share/wireplumber/scripts/node/filter-forward-format.lua
* /usr/share/wireplumber/scripts/node/software-dsp.lua
* /usr/share/wireplumber/scripts/node/state-stream.lua
* /usr/share/wireplumber/scripts/node/suspend-node.lua
* /usr/share/wireplumber/scripts/sm-objects.lua
* /usr/share/wireplumber/wireplumber.conf
* /usr/share/wireplumber/wireplumber.conf.d/alsa-vm.conf
* /usr/share/zsh/site-functions/_wpctl
