+++
draft = false
title = "scim 1.4.18-3"
version = "1.4.18-3"
date = "2023-02-25T10:42:32"
categories = ['xapps-extra']
upstreamurl = "http://www.scim-im.org/"
arch = "x86_64"
size = "742684"
usize = "3652998"
sha1sum = "191627d86e8e28fb402cbc743b0001cb4e7742b7"
depends = "['gtk+2>=2.20.0-2', 'libstdc++', 'freetype2', 'pango>=1.14.2', 'libtool']"
files = "['etc/', 'etc/profile.d/', 'etc/profile.d/scim.sh', 'etc/scim/', 'etc/scim/config', 'etc/scim/global', 'usr/', 'usr/bin/', 'usr/bin/scim', 'usr/bin/scim-config-agent', 'usr/bin/scim-im-agent', 'usr/bin/scim-setup', 'usr/include/', 'usr/include/scim-1.0/', 'usr/include/scim-1.0/gtk/', 'usr/include/scim-1.0/gtk/scimkeyselection.h', 'usr/include/scim-1.0/gtk/scimstringview.h', 'usr/include/scim-1.0/gtk/scimtrayicon.h', 'usr/include/scim-1.0/scim.h', 'usr/include/scim-1.0/scim_attribute.h', 'usr/include/scim-1.0/scim_backend.h', 'usr/include/scim-1.0/scim_bind.h', 'usr/include/scim-1.0/scim_compose_key.h', 'usr/include/scim-1.0/scim_config_base.h', 'usr/include/scim-1.0/scim_config_module.h', 'usr/include/scim-1.0/scim_config_path.h', 'usr/include/scim-1.0/scim_connection.h', 'usr/include/scim-1.0/scim_debug.h', 'usr/include/scim-1.0/scim_event.h', 'usr/include/scim-1.0/scim_exception.h', 'usr/include/scim-1.0/scim_filter.h', 'usr/include/scim-1.0/scim_filter_manager.h', 'usr/include/scim-1.0/scim_filter_module.h', 'usr/include/scim-1.0/scim_frontend.h', 'usr/include/scim-1.0/scim_frontend_module.h', 'usr/include/scim-1.0/scim_global_config.h', 'usr/include/scim-1.0/scim_helper.h', 'usr/include/scim-1.0/scim_helper_manager.h', 'usr/include/scim-1.0/scim_helper_module.h', 'usr/include/scim-1.0/scim_hotkey.h', 'usr/include/scim-1.0/scim_iconv.h', 'usr/include/scim-1.0/scim_imengine.h', 'usr/include/scim-1.0/scim_imengine_module.h', 'usr/include/scim-1.0/scim_lookup_table.h', 'usr/include/scim-1.0/scim_module.h', 'usr/include/scim-1.0/scim_object.h', 'usr/include/scim-1.0/scim_panel_agent.h', 'usr/include/scim-1.0/scim_panel_client.h', 'usr/include/scim-1.0/scim_panel_common.h', 'usr/include/scim-1.0/scim_pointer.h', 'usr/include/scim-1.0/scim_property.h', 'usr/include/scim-1.0/scim_signals.h', 'usr/include/scim-1.0/scim_slot.h', 'usr/include/scim-1.0/scim_socket.h', 'usr/include/scim-1.0/scim_trans_commands.h', 'usr/include/scim-1.0/scim_transaction.h', 'usr/include/scim-1.0/scim_types.h', 'usr/include/scim-1.0/scim_utility.h', 'usr/include/scim-1.0/x11/', 'usr/include/scim-1.0/x11/scim_x11_utils.h', 'usr/lib/', 'usr/lib/gtk-2.0/', 'usr/lib/gtk-2.0/2.10.0/', 'usr/lib/gtk-2.0/2.10.0/immodules/', 'usr/lib/gtk-2.0/2.10.0/immodules/im-scim.so', 'usr/lib/libscim-1.0.so', 'usr/lib/libscim-1.0.so.8', 'usr/lib/libscim-1.0.so.8.2.6', 'usr/lib/libscim-gtkutils-1.0.so', 'usr/lib/libscim-gtkutils-1.0.so.8', 'usr/lib/libscim-gtkutils-1.0.so.8.2.6', 'usr/lib/libscim-x11utils-1.0.so', 'usr/lib/libscim-x11utils-1.0.so.8', 'usr/lib/libscim-x11utils-1.0.so.8.2.6', 'usr/lib/pkgconfig/', 'usr/lib/pkgconfig/scim-gtkutils.pc', 'usr/lib/pkgconfig/scim-x11utils.pc', 'usr/lib/pkgconfig/scim.pc', 'usr/lib/scim-1.0/', 'usr/lib/scim-1.0/1.4.0/', 'usr/lib/scim-1.0/1.4.0/Config/', 'usr/lib/scim-1.0/1.4.0/Config/simple.so', 'usr/lib/scim-1.0/1.4.0/Config/socket.so', 'usr/lib/scim-1.0/1.4.0/Filter/', 'usr/lib/scim-1.0/1.4.0/Filter/sctc.so', 'usr/lib/scim-1.0/1.4.0/FrontEnd/', 'usr/lib/scim-1.0/1.4.0/FrontEnd/socket.so', 'usr/lib/scim-1.0/1.4.0/FrontEnd/x11.so', 'usr/lib/scim-1.0/1.4.0/Helper/', 'usr/lib/scim-1.0/1.4.0/Helper/setup.so', 'usr/lib/scim-1.0/1.4.0/IMEngine/', 'usr/lib/scim-1.0/1.4.0/IMEngine/rawcode.so', 'usr/lib/scim-1.0/1.4.0/IMEngine/socket.so', 'usr/lib/scim-1.0/1.4.0/SetupUI/', 'usr/lib/scim-1.0/1.4.0/SetupUI/aaa-frontend-setup.so', 'usr/lib/scim-1.0/1.4.0/SetupUI/aaa-imengine-setup.so', 'usr/lib/scim-1.0/1.4.0/SetupUI/panel-gtk-setup.so', 'usr/lib/scim-1.0/scim-helper-launcher', 'usr/lib/scim-1.0/scim-helper-manager', 'usr/lib/scim-1.0/scim-launcher', 'usr/lib/scim-1.0/scim-panel-gtk', 'usr/share/', 'usr/share/applications/', 'usr/share/applications/scim-setup.desktop', 'usr/share/control-center-2.0/', 'usr/share/control-center-2.0/capplets/', 'usr/share/control-center-2.0/capplets/scim-setup.desktop', 'usr/share/doc/', 'usr/share/doc/scim-1.4.18/', 'usr/share/doc/scim-1.4.18/AUTHORS', 'usr/share/doc/scim-1.4.18/COPYING', 'usr/share/doc/scim-1.4.18/ChangeLog', 'usr/share/doc/scim-1.4.18/INSTALL', 'usr/share/doc/scim-1.4.18/NEWS', 'usr/share/doc/scim-1.4.18/README', 'usr/share/doc/scim-1.4.18/THANKS', 'usr/share/doc/scim-1.4.18/TODO', 'usr/share/locale/', 'usr/share/locale/as/', 'usr/share/locale/as/LC_MESSAGES/', 'usr/share/locale/as/LC_MESSAGES/scim.mo', 'usr/share/locale/bn_IN/', 'usr/share/locale/bn_IN/LC_MESSAGES/', 'usr/share/locale/bn_IN/LC_MESSAGES/scim.mo', 'usr/share/locale/ca/', 'usr/share/locale/ca/LC_MESSAGES/', 'usr/share/locale/ca/LC_MESSAGES/scim.mo', 'usr/share/locale/cs/', 'usr/share/locale/cs/LC_MESSAGES/', 'usr/share/locale/cs/LC_MESSAGES/scim.mo', 'usr/share/locale/de/', 'usr/share/locale/de/LC_MESSAGES/', 'usr/share/locale/de/LC_MESSAGES/scim.mo', 'usr/share/locale/es/', 'usr/share/locale/es/LC_MESSAGES/', 'usr/share/locale/es/LC_MESSAGES/scim.mo', 'usr/share/locale/fi/', 'usr/share/locale/fi/LC_MESSAGES/', 'usr/share/locale/fi/LC_MESSAGES/scim.mo', 'usr/share/locale/fr/', 'usr/share/locale/fr/LC_MESSAGES/', 'usr/share/locale/fr/LC_MESSAGES/scim.mo', 'usr/share/locale/gu/', 'usr/share/locale/gu/LC_MESSAGES/', 'usr/share/locale/gu/LC_MESSAGES/scim.mo', 'usr/share/locale/hi/', 'usr/share/locale/hi/LC_MESSAGES/', 'usr/share/locale/hi/LC_MESSAGES/scim.mo', 'usr/share/locale/it/', 'usr/share/locale/it/LC_MESSAGES/', 'usr/share/locale/it/LC_MESSAGES/scim.mo', 'usr/share/locale/ja/', 'usr/share/locale/ja/LC_MESSAGES/', 'usr/share/locale/ja/LC_MESSAGES/scim.mo', 'usr/share/locale/kn/', 'usr/share/locale/kn/LC_MESSAGES/', 'usr/share/locale/kn/LC_MESSAGES/scim.mo', 'usr/share/locale/ko/', 'usr/share/locale/ko/LC_MESSAGES/', 'usr/share/locale/ko/LC_MESSAGES/scim.mo', 'usr/share/locale/ml/', 'usr/share/locale/ml/LC_MESSAGES/', 'usr/share/locale/ml/LC_MESSAGES/scim.mo', 'usr/share/locale/mr/', 'usr/share/locale/mr/LC_MESSAGES/', 'usr/share/locale/mr/LC_MESSAGES/scim.mo', 'usr/share/locale/nl/', 'usr/share/locale/nl/LC_MESSAGES/', 'usr/share/locale/nl/LC_MESSAGES/scim.mo', 'usr/share/locale/pa/', 'usr/share/locale/pa/LC_MESSAGES/', 'usr/share/locale/pa/LC_MESSAGES/scim.mo', 'usr/share/locale/pt_BR/', 'usr/share/locale/pt_BR/LC_MESSAGES/', 'usr/share/locale/pt_BR/LC_MESSAGES/scim.mo', 'usr/share/locale/ru/', 'usr/share/locale/ru/LC_MESSAGES/', 'usr/share/locale/ru/LC_MESSAGES/scim.mo', 'usr/share/locale/sk/', 'usr/share/locale/sk/LC_MESSAGES/', 'usr/share/locale/sk/LC_MESSAGES/scim.mo', 'usr/share/locale/sv/', 'usr/share/locale/sv/LC_MESSAGES/', 'usr/share/locale/sv/LC_MESSAGES/scim.mo', 'usr/share/locale/ta/', 'usr/share/locale/ta/LC_MESSAGES/', 'usr/share/locale/ta/LC_MESSAGES/scim.mo', 'usr/share/locale/te/', 'usr/share/locale/te/LC_MESSAGES/', 'usr/share/locale/te/LC_MESSAGES/scim.mo', 'usr/share/locale/vi/', 'usr/share/locale/vi/LC_MESSAGES/', 'usr/share/locale/vi/LC_MESSAGES/scim.mo', 'usr/share/locale/zh_CN/', 'usr/share/locale/zh_CN/LC_MESSAGES/', 'usr/share/locale/zh_CN/LC_MESSAGES/scim.mo', 'usr/share/locale/zh_TW/', 'usr/share/locale/zh_TW/LC_MESSAGES/', 'usr/share/locale/zh_TW/LC_MESSAGES/scim.mo', 'usr/share/pixmaps/', 'usr/share/pixmaps/scim-setup.png', 'usr/share/scim/', 'usr/share/scim/icons/', 'usr/share/scim/icons/down.png', 'usr/share/scim/icons/full-letter.png', 'usr/share/scim/icons/full-punct.png', 'usr/share/scim/icons/half-letter.png', 'usr/share/scim/icons/half-punct.png', 'usr/share/scim/icons/help.png', 'usr/share/scim/icons/keyboard.png', 'usr/share/scim/icons/left.png', 'usr/share/scim/icons/menu.png', 'usr/share/scim/icons/pin-down.png', 'usr/share/scim/icons/pin-up.png', 'usr/share/scim/icons/rawcode.png', 'usr/share/scim/icons/right.png', 'usr/share/scim/icons/sctc-sc-to-tc.png', 'usr/share/scim/icons/sctc-tc-to-sc.png', 'usr/share/scim/icons/sctc.png', 'usr/share/scim/icons/setup.png', 'usr/share/scim/icons/trademark.png', 'usr/share/scim/icons/up.png']"
+++
Input methods covering more than 30 languages.