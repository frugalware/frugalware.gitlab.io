+++
draft = false
title = "wlroots 0.18.2-1"
version = "0.18.2-1"
description = "Modular Wayland compositor library"
date = "2024-12-24T15:59:12"
aliases = "/packages/220461"
categories = ['xlib-extra']
upstreamurl = "https://gitlab.freedesktop.org/wlroots/wlroots"
arch = "x86_64"
size = "329448"
usize = "1198041"
sha1sum = "43e33e015b7c3861ad1a6c91b22ca83354aec517"
depends = "['libdrm', 'libgbm', 'libglvnd', 'libinput', 'libxcb', 'libxkbcommon', 'pixman', 'seatd', 'vulkan-icd-loader', 'wayland', 'xcb-util', 'xcb-util-renderutil', 'xcb-util-wm']"
reverse_depends = "['greetd-qt6greet']"
+++
### Description: 
Modular Wayland compositor library

### Files: 
* /usr/include/wlroots-0.18/wlr/backend.h
* /usr/include/wlroots-0.18/wlr/backend/headless.h
* /usr/include/wlroots-0.18/wlr/backend/interface.h
* /usr/include/wlroots-0.18/wlr/backend/libinput.h
* /usr/include/wlroots-0.18/wlr/backend/multi.h
* /usr/include/wlroots-0.18/wlr/backend/session.h
* /usr/include/wlroots-0.18/wlr/backend/wayland.h
* /usr/include/wlroots-0.18/wlr/config.h
* /usr/include/wlroots-0.18/wlr/interfaces/wlr_buffer.h
* /usr/include/wlroots-0.18/wlr/interfaces/wlr_keyboard.h
* /usr/include/wlroots-0.18/wlr/interfaces/wlr_output.h
* /usr/include/wlroots-0.18/wlr/interfaces/wlr_pointer.h
* /usr/include/wlroots-0.18/wlr/interfaces/wlr_switch.h
* /usr/include/wlroots-0.18/wlr/interfaces/wlr_tablet_pad.h
* /usr/include/wlroots-0.18/wlr/interfaces/wlr_tablet_tool.h
* /usr/include/wlroots-0.18/wlr/interfaces/wlr_touch.h
* /usr/include/wlroots-0.18/wlr/render/allocator.h
* /usr/include/wlroots-0.18/wlr/render/color.h
* /usr/include/wlroots-0.18/wlr/render/dmabuf.h
* /usr/include/wlroots-0.18/wlr/render/drm_format_set.h
* /usr/include/wlroots-0.18/wlr/render/drm_syncobj.h
* /usr/include/wlroots-0.18/wlr/render/egl.h
* /usr/include/wlroots-0.18/wlr/render/gles2.h
* /usr/include/wlroots-0.18/wlr/render/interface.h
* /usr/include/wlroots-0.18/wlr/render/pass.h
* /usr/include/wlroots-0.18/wlr/render/pixman.h
* /usr/include/wlroots-0.18/wlr/render/swapchain.h
* /usr/include/wlroots-0.18/wlr/render/vulkan.h
* /usr/include/wlroots-0.18/wlr/render/wlr_renderer.h
* /usr/include/wlroots-0.18/wlr/render/wlr_texture.h
* /usr/include/wlroots-0.18/wlr/types/wlr_alpha_modifier_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_buffer.h
* /usr/include/wlroots-0.18/wlr/types/wlr_compositor.h
* /usr/include/wlroots-0.18/wlr/types/wlr_content_type_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_cursor.h
* /usr/include/wlroots-0.18/wlr/types/wlr_cursor_shape_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_damage_ring.h
* /usr/include/wlroots-0.18/wlr/types/wlr_data_control_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_data_device.h
* /usr/include/wlroots-0.18/wlr/types/wlr_drm.h
* /usr/include/wlroots-0.18/wlr/types/wlr_export_dmabuf_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_ext_foreign_toplevel_list_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_foreign_toplevel_management_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_fractional_scale_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_fullscreen_shell_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_gamma_control_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_idle_inhibit_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_idle_notify_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_input_device.h
* /usr/include/wlroots-0.18/wlr/types/wlr_input_method_v2.h
* /usr/include/wlroots-0.18/wlr/types/wlr_keyboard.h
* /usr/include/wlroots-0.18/wlr/types/wlr_keyboard_group.h
* /usr/include/wlroots-0.18/wlr/types/wlr_keyboard_shortcuts_inhibit_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_layer_shell_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_linux_dmabuf_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_linux_drm_syncobj_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_matrix.h
* /usr/include/wlroots-0.18/wlr/types/wlr_output.h
* /usr/include/wlroots-0.18/wlr/types/wlr_output_layer.h
* /usr/include/wlroots-0.18/wlr/types/wlr_output_layout.h
* /usr/include/wlroots-0.18/wlr/types/wlr_output_management_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_output_power_management_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_output_swapchain_manager.h
* /usr/include/wlroots-0.18/wlr/types/wlr_pointer.h
* /usr/include/wlroots-0.18/wlr/types/wlr_pointer_constraints_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_pointer_gestures_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_presentation_time.h
* /usr/include/wlroots-0.18/wlr/types/wlr_primary_selection.h
* /usr/include/wlroots-0.18/wlr/types/wlr_primary_selection_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_region.h
* /usr/include/wlroots-0.18/wlr/types/wlr_relative_pointer_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_scene.h
* /usr/include/wlroots-0.18/wlr/types/wlr_screencopy_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_seat.h
* /usr/include/wlroots-0.18/wlr/types/wlr_security_context_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_server_decoration.h
* /usr/include/wlroots-0.18/wlr/types/wlr_session_lock_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_shm.h
* /usr/include/wlroots-0.18/wlr/types/wlr_single_pixel_buffer_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_subcompositor.h
* /usr/include/wlroots-0.18/wlr/types/wlr_switch.h
* /usr/include/wlroots-0.18/wlr/types/wlr_tablet_pad.h
* /usr/include/wlroots-0.18/wlr/types/wlr_tablet_tool.h
* /usr/include/wlroots-0.18/wlr/types/wlr_tablet_v2.h
* /usr/include/wlroots-0.18/wlr/types/wlr_tearing_control_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_text_input_v3.h
* /usr/include/wlroots-0.18/wlr/types/wlr_touch.h
* /usr/include/wlroots-0.18/wlr/types/wlr_transient_seat_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_viewporter.h
* /usr/include/wlroots-0.18/wlr/types/wlr_virtual_keyboard_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_virtual_pointer_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_xcursor_manager.h
* /usr/include/wlroots-0.18/wlr/types/wlr_xdg_activation_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_xdg_decoration_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_xdg_foreign_registry.h
* /usr/include/wlroots-0.18/wlr/types/wlr_xdg_foreign_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_xdg_foreign_v2.h
* /usr/include/wlroots-0.18/wlr/types/wlr_xdg_output_v1.h
* /usr/include/wlroots-0.18/wlr/types/wlr_xdg_shell.h
* /usr/include/wlroots-0.18/wlr/util/addon.h
* /usr/include/wlroots-0.18/wlr/util/box.h
* /usr/include/wlroots-0.18/wlr/util/edges.h
* /usr/include/wlroots-0.18/wlr/util/log.h
* /usr/include/wlroots-0.18/wlr/util/region.h
* /usr/include/wlroots-0.18/wlr/util/transform.h
* /usr/include/wlroots-0.18/wlr/version.h
* /usr/include/wlroots-0.18/wlr/xcursor.h
* /usr/include/wlroots-0.18/wlr/xwayland/server.h
* /usr/include/wlroots-0.18/wlr/xwayland/shell.h
* /usr/include/wlroots-0.18/wlr/xwayland/xwayland.h
* /usr/lib/libwlroots-0.18.so
* /usr/lib/pkgconfig/wlroots-0.18.pc
* /usr/share/doc/wlroots-0.18.2/LICENSE
* /usr/share/doc/wlroots-0.18.2/README.md
