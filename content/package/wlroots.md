+++
draft = false
title = "wlroots 0.17.1-1"
version = "0.17.1-1"
description = "Modular Wayland compositor library"
date = "2023-12-29T10:11:46"
aliases = "/packages/220461"
categories = ['xlib-extra']
upstreamurl = "https://gitlab.freedesktop.org/wlroots/wlroots"
arch = "x86_64"
size = "326380"
usize = "1186955"
sha1sum = "f93ffbdef10fb63c161e91e583c6ebef996304fb"
depends = "['libdrm', 'libgbm', 'libglvnd', 'libinput', 'libxcb', 'libxkbcommon', 'pixman', 'seatd', 'vulkan-icd-loader', 'wayland', 'xcb-util', 'xcb-util-renderutil', 'xcb-util-wm']"
reverse_depends = "['greetd-qtgreet']"
+++
Modular Wayland compositor library"

{{< files text="show files" >}}* /usr/include/wlr/backend.h
* /usr/include/wlr/backend/headless.h
* /usr/include/wlr/backend/interface.h
* /usr/include/wlr/backend/libinput.h
* /usr/include/wlr/backend/multi.h
* /usr/include/wlr/backend/session.h
* /usr/include/wlr/backend/wayland.h
* /usr/include/wlr/backend/x11.h
* /usr/include/wlr/config.h
* /usr/include/wlr/interfaces/wlr_buffer.h
* /usr/include/wlr/interfaces/wlr_keyboard.h
* /usr/include/wlr/interfaces/wlr_output.h
* /usr/include/wlr/interfaces/wlr_pointer.h
* /usr/include/wlr/interfaces/wlr_switch.h
* /usr/include/wlr/interfaces/wlr_tablet_pad.h
* /usr/include/wlr/interfaces/wlr_tablet_tool.h
* /usr/include/wlr/interfaces/wlr_touch.h
* /usr/include/wlr/render/allocator.h
* /usr/include/wlr/render/dmabuf.h
* /usr/include/wlr/render/drm_format_set.h
* /usr/include/wlr/render/egl.h
* /usr/include/wlr/render/gles2.h
* /usr/include/wlr/render/interface.h
* /usr/include/wlr/render/pass.h
* /usr/include/wlr/render/pixman.h
* /usr/include/wlr/render/swapchain.h
* /usr/include/wlr/render/vulkan.h
* /usr/include/wlr/render/wlr_renderer.h
* /usr/include/wlr/render/wlr_texture.h
* /usr/include/wlr/types/wlr_buffer.h
* /usr/include/wlr/types/wlr_compositor.h
* /usr/include/wlr/types/wlr_content_type_v1.h
* /usr/include/wlr/types/wlr_cursor.h
* /usr/include/wlr/types/wlr_cursor_shape_v1.h
* /usr/include/wlr/types/wlr_damage_ring.h
* /usr/include/wlr/types/wlr_data_control_v1.h
* /usr/include/wlr/types/wlr_data_device.h
* /usr/include/wlr/types/wlr_drm.h
* /usr/include/wlr/types/wlr_export_dmabuf_v1.h
* /usr/include/wlr/types/wlr_foreign_toplevel_management_v1.h
* /usr/include/wlr/types/wlr_fractional_scale_v1.h
* /usr/include/wlr/types/wlr_fullscreen_shell_v1.h
* /usr/include/wlr/types/wlr_gamma_control_v1.h
* /usr/include/wlr/types/wlr_idle_inhibit_v1.h
* /usr/include/wlr/types/wlr_idle_notify_v1.h
* /usr/include/wlr/types/wlr_input_device.h
* /usr/include/wlr/types/wlr_input_inhibitor.h
* /usr/include/wlr/types/wlr_input_method_v2.h
* /usr/include/wlr/types/wlr_keyboard.h
* /usr/include/wlr/types/wlr_keyboard_group.h
* /usr/include/wlr/types/wlr_keyboard_shortcuts_inhibit_v1.h
* /usr/include/wlr/types/wlr_layer_shell_v1.h
* /usr/include/wlr/types/wlr_linux_dmabuf_v1.h
* /usr/include/wlr/types/wlr_matrix.h
* /usr/include/wlr/types/wlr_output.h
* /usr/include/wlr/types/wlr_output_layer.h
* /usr/include/wlr/types/wlr_output_layout.h
* /usr/include/wlr/types/wlr_output_management_v1.h
* /usr/include/wlr/types/wlr_output_power_management_v1.h
* /usr/include/wlr/types/wlr_pointer.h
* /usr/include/wlr/types/wlr_pointer_constraints_v1.h
* /usr/include/wlr/types/wlr_pointer_gestures_v1.h
* /usr/include/wlr/types/wlr_presentation_time.h
* /usr/include/wlr/types/wlr_primary_selection.h
* /usr/include/wlr/types/wlr_primary_selection_v1.h
* /usr/include/wlr/types/wlr_region.h
* /usr/include/wlr/types/wlr_relative_pointer_v1.h
* /usr/include/wlr/types/wlr_scene.h
* /usr/include/wlr/types/wlr_screencopy_v1.h
* /usr/include/wlr/types/wlr_seat.h
* /usr/include/wlr/types/wlr_security_context_v1.h
* /usr/include/wlr/types/wlr_server_decoration.h
* /usr/include/wlr/types/wlr_session_lock_v1.h
* /usr/include/wlr/types/wlr_shm.h
* /usr/include/wlr/types/wlr_single_pixel_buffer_v1.h
* /usr/include/wlr/types/wlr_subcompositor.h
* /usr/include/wlr/types/wlr_switch.h
* /usr/include/wlr/types/wlr_tablet_pad.h
* /usr/include/wlr/types/wlr_tablet_tool.h
* /usr/include/wlr/types/wlr_tablet_v2.h
* /usr/include/wlr/types/wlr_tearing_control_v1.h
* /usr/include/wlr/types/wlr_text_input_v3.h
* /usr/include/wlr/types/wlr_touch.h
* /usr/include/wlr/types/wlr_viewporter.h
* /usr/include/wlr/types/wlr_virtual_keyboard_v1.h
* /usr/include/wlr/types/wlr_virtual_pointer_v1.h
* /usr/include/wlr/types/wlr_xcursor_manager.h
* /usr/include/wlr/types/wlr_xdg_activation_v1.h
* /usr/include/wlr/types/wlr_xdg_decoration_v1.h
* /usr/include/wlr/types/wlr_xdg_foreign_registry.h
* /usr/include/wlr/types/wlr_xdg_foreign_v1.h
* /usr/include/wlr/types/wlr_xdg_foreign_v2.h
* /usr/include/wlr/types/wlr_xdg_output_v1.h
* /usr/include/wlr/types/wlr_xdg_shell.h
* /usr/include/wlr/util/addon.h
* /usr/include/wlr/util/box.h
* /usr/include/wlr/util/edges.h
* /usr/include/wlr/util/log.h
* /usr/include/wlr/util/region.h
* /usr/include/wlr/version.h
* /usr/include/wlr/xcursor.h
* /usr/include/wlr/xwayland/server.h
* /usr/include/wlr/xwayland/shell.h
* /usr/include/wlr/xwayland/xwayland.h
* /usr/lib/libwlroots.so
* /usr/lib/libwlroots.so.12
* /usr/lib/pkgconfig/wlroots.pc
* /usr/share/doc/wlroots-0.17.1/LICENSE
* /usr/share/doc/wlroots-0.17.1/README.md
{{< /files >}}