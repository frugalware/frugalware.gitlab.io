+++
draft = false
title = "znc 1.9.1-2"
version = "1.9.1-2"
description = "An IRC bouncer with modules and scripts support."
date = "2025-03-19T10:13:16"
aliases = "/packages/135816"
categories = ['network-extra']
upstreamurl = "http://znc.in"
arch = "x86_64"
size = "1725940"
usize = "6804368"
sha1sum = "82296910e6c85f9ae7c56e11323ffa407daa067a"
depends = "['cyrus-sasl', 'icu4c>=77.1', 'libstdc++', 'openssl>=3.1.0', 'python3>=3.12']"
+++
### Description: 
An IRC bouncer with modules and scripts support.

### Files: 
* /usr/bin/znc
* /usr/bin/znc-buildmod
* /usr/include/znc/Buffer.h
* /usr/include/znc/Chan.h
* /usr/include/znc/Client.h
* /usr/include/znc/Config.h
* /usr/include/znc/Csocket.h
* /usr/include/znc/defines.h
* /usr/include/znc/ExecSock.h
* /usr/include/znc/FileUtils.h
* /usr/include/znc/HTTPSock.h
* /usr/include/znc/IRCNetwork.h
* /usr/include/znc/IRCSock.h
* /usr/include/znc/Listener.h
* /usr/include/znc/main.h
* /usr/include/znc/MD5.h
* /usr/include/znc/Message.h
* /usr/include/znc/Modules.h
* /usr/include/znc/Nick.h
* /usr/include/znc/Query.h
* /usr/include/znc/Server.h
* /usr/include/znc/SHA256.h
* /usr/include/znc/Socket.h
* /usr/include/znc/SSLVerifyHost.h
* /usr/include/znc/Template.h
* /usr/include/znc/Threads.h
* /usr/include/znc/Translation.h
* /usr/include/znc/User.h
* /usr/include/znc/Utils.h
* /usr/include/znc/version.h
* /usr/include/znc/WebModules.h
* /usr/include/znc/znc.h
* /usr/include/znc/zncconfig.h
* /usr/include/znc/ZNCDebug.h
* /usr/include/znc/ZNCString.h
* /usr/include/znc/znc_export_lib_export.h
* /usr/lib/pkgconfig/znc.pc
* /usr/lib/znc/admindebug.so
* /usr/lib/znc/adminlog.so
* /usr/lib/znc/alias.so
* /usr/lib/znc/autoattach.so
* /usr/lib/znc/autocycle.so
* /usr/lib/znc/autoop.so
* /usr/lib/znc/autoreply.so
* /usr/lib/znc/autovoice.so
* /usr/lib/znc/awaynick.so
* /usr/lib/znc/awaystore.so
* /usr/lib/znc/blockuser.so
* /usr/lib/znc/block_motd.so
* /usr/lib/znc/bouncedcc.so
* /usr/lib/znc/buffextras.so
* /usr/lib/znc/cert.so
* /usr/lib/znc/certauth.so
* /usr/lib/znc/chansaver.so
* /usr/lib/znc/clearbufferonmsg.so
* /usr/lib/znc/clientnotify.so
* /usr/lib/znc/controlpanel.so
* /usr/lib/znc/corecaps.so
* /usr/lib/znc/crypt.so
* /usr/lib/znc/ctcpflood.so
* /usr/lib/znc/cyrusauth.so
* /usr/lib/znc/dcc.so
* /usr/lib/znc/disconkick.so
* /usr/lib/znc/fail2ban.so
* /usr/lib/znc/flooddetach.so
* /usr/lib/znc/identfile.so
* /usr/lib/znc/imapauth.so
* /usr/lib/znc/keepnick.so
* /usr/lib/znc/kickrejoin.so
* /usr/lib/znc/lastseen.so
* /usr/lib/znc/listsockets.so
* /usr/lib/znc/log.so
* /usr/lib/znc/missingmotd.so
* /usr/lib/znc/modules_online.so
* /usr/lib/znc/nickserv.so
* /usr/lib/znc/notes.so
* /usr/lib/znc/notify_connect.so
* /usr/lib/znc/perform.so
* /usr/lib/znc/raw.so
* /usr/lib/znc/route_replies.so
* /usr/lib/znc/sample.so
* /usr/lib/znc/samplewebapi.so
* /usr/lib/znc/sasl.so
* /usr/lib/znc/savebuff.so
* /usr/lib/znc/schat.so
* /usr/lib/znc/send_raw.so
* /usr/lib/znc/shell.so
* /usr/lib/znc/simple_away.so
* /usr/lib/znc/stickychan.so
* /usr/lib/znc/stripcontrols.so
* /usr/lib/znc/watch.so
* /usr/lib/znc/webadmin.so
* /usr/share/doc/znc-1.9.1/LICENSE
* /usr/share/doc/znc-1.9.1/README.md
* /usr/share/man/man1/znc-buildmod.1.gz
* /usr/share/man/man1/znc.1.gz
* /usr/share/znc/cmake/CMakeFindDependencyMacroPC.cmake
* /usr/share/znc/cmake/use_homebrew.cmake
* /usr/share/znc/cmake/ZNCConfig.cmake
* /usr/share/znc/cmake/ZNCConfigVersion.cmake
* /usr/share/znc/cmake/znc_internal-release.cmake
* /usr/share/znc/cmake/znc_internal.cmake
* /usr/share/znc/cmake/znc_public.cmake
* /usr/share/znc/modules/blockuser/tmpl/blockuser_WebadminUser.tmpl
* /usr/share/znc/modules/cert/tmpl/index.tmpl
* /usr/share/znc/modules/certauth/tmpl/index.tmpl
* /usr/share/znc/modules/lastseen/tmpl/index.tmpl
* /usr/share/znc/modules/lastseen/tmpl/lastseen_WebadminUser.tmpl
* /usr/share/znc/modules/listsockets/tmpl/index.tmpl
* /usr/share/znc/modules/notes/files/trash.gif
* /usr/share/znc/modules/notes/tmpl/index.tmpl
* /usr/share/znc/modules/perform/tmpl/index.tmpl
* /usr/share/znc/modules/q/tmpl/index.tmpl
* /usr/share/znc/modules/samplewebapi/tmpl/index.tmpl
* /usr/share/znc/modules/sasl/tmpl/index.tmpl
* /usr/share/znc/modules/send_raw/files/select.js
* /usr/share/znc/modules/send_raw/tmpl/index.tmpl
* /usr/share/znc/modules/stickychan/tmpl/index.tmpl
* /usr/share/znc/modules/stickychan/tmpl/stickychan_WebadminChan.tmpl
* /usr/share/znc/modules/webadmin/files/webadmin.css
* /usr/share/znc/modules/webadmin/files/webadmin.js
* /usr/share/znc/modules/webadmin/tmpl/add_edit_chan.tmpl
* /usr/share/znc/modules/webadmin/tmpl/add_edit_network.tmpl
* /usr/share/znc/modules/webadmin/tmpl/add_edit_user.tmpl
* /usr/share/znc/modules/webadmin/tmpl/del_network.tmpl
* /usr/share/znc/modules/webadmin/tmpl/del_user.tmpl
* /usr/share/znc/modules/webadmin/tmpl/encoding_settings.tmpl
* /usr/share/znc/modules/webadmin/tmpl/index.tmpl
* /usr/share/znc/modules/webadmin/tmpl/listusers.tmpl
* /usr/share/znc/modules/webadmin/tmpl/settings.tmpl
* /usr/share/znc/modules/webadmin/tmpl/traffic.tmpl
* /usr/share/znc/translations/bg-BG
* /usr/share/znc/translations/de-DE
* /usr/share/znc/translations/es-ES
* /usr/share/znc/translations/fr-FR
* /usr/share/znc/translations/id-ID
* /usr/share/znc/translations/it-IT
* /usr/share/znc/translations/nl-NL
* /usr/share/znc/translations/pl-PL
* /usr/share/znc/translations/pt-BR
* /usr/share/znc/translations/pt-PT
* /usr/share/znc/translations/ru-RU
* /usr/share/znc/translations/tr-TR
* /usr/share/znc/webskins/dark-clouds/pub/clouds-header.jpg
* /usr/share/znc/webskins/dark-clouds/pub/dark-clouds.css
* /usr/share/znc/webskins/dark-clouds/pub/favicon.ico
* /usr/share/znc/webskins/dark-clouds/tmpl/Banner.tmpl
* /usr/share/znc/webskins/dark-clouds/tmpl/FooterTag.tmpl
* /usr/share/znc/webskins/dark-clouds/tmpl/Header.tmpl
* /usr/share/znc/webskins/dark-clouds/tmpl/LowerBanner.tmpl
* /usr/share/znc/webskins/forest/pub/favicon.ico
* /usr/share/znc/webskins/forest/pub/forest-header.png
* /usr/share/znc/webskins/forest/pub/forest.css
* /usr/share/znc/webskins/forest/tmpl/Banner.tmpl
* /usr/share/znc/webskins/forest/tmpl/FooterTag.tmpl
* /usr/share/znc/webskins/forest/tmpl/Header.tmpl
* /usr/share/znc/webskins/forest/tmpl/LowerBanner.tmpl
* /usr/share/znc/webskins/ice/pub/favicon.ico
* /usr/share/znc/webskins/ice/pub/ice.css
* /usr/share/znc/webskins/ice/pub/linkbg.jpg
* /usr/share/znc/webskins/ice/pub/pagebg.gif
* /usr/share/znc/webskins/ice/tmpl/FooterTag.tmpl
* /usr/share/znc/webskins/ice/tmpl/Header.tmpl
* /usr/share/znc/webskins/_default_/pub/External.png
* /usr/share/znc/webskins/_default_/pub/favicon.ico
* /usr/share/znc/webskins/_default_/pub/global.css
* /usr/share/znc/webskins/_default_/pub/jquery-1.11.2.js
* /usr/share/znc/webskins/_default_/pub/jquery-1.11.2.min.js
* /usr/share/znc/webskins/_default_/pub/jquery-ui-sortable.1.11.4.css
* /usr/share/znc/webskins/_default_/pub/jquery-ui-sortable.1.11.4.js
* /usr/share/znc/webskins/_default_/pub/jquery-ui-sortable.1.11.4.min.css
* /usr/share/znc/webskins/_default_/pub/jquery-ui-sortable.1.11.4.min.js
* /usr/share/znc/webskins/_default_/pub/robots.txt
* /usr/share/znc/webskins/_default_/pub/selectize-0.12.1.css
* /usr/share/znc/webskins/_default_/pub/selectize-standalone-0.12.1.js
* /usr/share/znc/webskins/_default_/pub/selectize-standalone-0.12.1.min.js
* /usr/share/znc/webskins/_default_/pub/_default_.css
* /usr/share/znc/webskins/_default_/tmpl/Banner.tmpl
* /usr/share/znc/webskins/_default_/tmpl/BaseHeader.tmpl
* /usr/share/znc/webskins/_default_/tmpl/BreadCrumbs.tmpl
* /usr/share/znc/webskins/_default_/tmpl/DocType.tmpl
* /usr/share/znc/webskins/_default_/tmpl/Error.tmpl
* /usr/share/znc/webskins/_default_/tmpl/ExtraHeader.tmpl
* /usr/share/znc/webskins/_default_/tmpl/Footer.tmpl
* /usr/share/znc/webskins/_default_/tmpl/FooterTag.tmpl
* /usr/share/znc/webskins/_default_/tmpl/Header.tmpl
* /usr/share/znc/webskins/_default_/tmpl/index.tmpl
* /usr/share/znc/webskins/_default_/tmpl/InfoBar.tmpl
* /usr/share/znc/webskins/_default_/tmpl/LoginBar.tmpl
* /usr/share/znc/webskins/_default_/tmpl/LowerBanner.tmpl
* /usr/share/znc/webskins/_default_/tmpl/Menu.tmpl
* /usr/share/znc/webskins/_default_/tmpl/MessageBar.tmpl
* /usr/share/znc/webskins/_default_/tmpl/Options.tmpl
* /usr/share/znc/webskins/_default_/tmpl/_csrf_check.tmpl
