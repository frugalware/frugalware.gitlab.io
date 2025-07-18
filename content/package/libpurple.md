+++
draft = false
title = "libpurple 2.14.14-2"
version = "2.14.14-2"
description = "Library intended to be used by programmers seeking to write an IM client that connects to many IM networks."
date = "2025-07-04T13:28:37"
aliases = "/packages/50023"
categories = ['xlib']
upstreamurl = "http://www.pidgin.im/"
arch = "x86_64"
size = "1616308"
usize = "7203824"
sha1sum = "6056c0a6afc42f16499c6b8e7fc91a3d537bc897"
depends = "['cyrus-sasl', 'dbus-glib', 'farstream', 'libgadu', 'libidn>=1.35', 'meanwhile', 'nss']"
reverse_depends = "['bitlbee-libpurple', 'finch', 'pidgin', 'pidgin-facebookchat', 'pidgin-skypeweb', 'telepathy-haze']"
+++
### Description: 
Library intended to be used by programmers seeking to write an IM client that connects to many IM networks.

### Files: 
* /usr/include/libpurple/account.h
* /usr/include/libpurple/accountopt.h
* /usr/include/libpurple/blist.h
* /usr/include/libpurple/buddyicon.h
* /usr/include/libpurple/certificate.h
* /usr/include/libpurple/cipher.h
* /usr/include/libpurple/circbuffer.h
* /usr/include/libpurple/cmds.h
* /usr/include/libpurple/connection.h
* /usr/include/libpurple/conversation.h
* /usr/include/libpurple/core.h
* /usr/include/libpurple/dbus-bindings.h
* /usr/include/libpurple/dbus-define-api.h
* /usr/include/libpurple/dbus-maybe.h
* /usr/include/libpurple/dbus-purple.h
* /usr/include/libpurple/dbus-server.h
* /usr/include/libpurple/dbus-types.h
* /usr/include/libpurple/dbus-useful.h
* /usr/include/libpurple/debug.h
* /usr/include/libpurple/desktopitem.h
* /usr/include/libpurple/dnsquery.h
* /usr/include/libpurple/dnssrv.h
* /usr/include/libpurple/eventloop.h
* /usr/include/libpurple/ft.h
* /usr/include/libpurple/gaim-compat.h
* /usr/include/libpurple/glibcompat.h
* /usr/include/libpurple/idle.h
* /usr/include/libpurple/imgstore.h
* /usr/include/libpurple/log.h
* /usr/include/libpurple/marshallers.h
* /usr/include/libpurple/media-gst.h
* /usr/include/libpurple/media.h
* /usr/include/libpurple/media/backend-iface.h
* /usr/include/libpurple/media/candidate.h
* /usr/include/libpurple/media/codec.h
* /usr/include/libpurple/media/enum-types.h
* /usr/include/libpurple/mediamanager.h
* /usr/include/libpurple/mime.h
* /usr/include/libpurple/nat-pmp.h
* /usr/include/libpurple/network.h
* /usr/include/libpurple/notify.h
* /usr/include/libpurple/ntlm.h
* /usr/include/libpurple/plugin.h
* /usr/include/libpurple/pluginpref.h
* /usr/include/libpurple/pounce.h
* /usr/include/libpurple/prefs.h
* /usr/include/libpurple/privacy.h
* /usr/include/libpurple/proxy.h
* /usr/include/libpurple/prpl.h
* /usr/include/libpurple/purple.h
* /usr/include/libpurple/request.h
* /usr/include/libpurple/roomlist.h
* /usr/include/libpurple/savedstatuses.h
* /usr/include/libpurple/server.h
* /usr/include/libpurple/signals.h
* /usr/include/libpurple/smiley.h
* /usr/include/libpurple/sound-theme-loader.h
* /usr/include/libpurple/sound-theme.h
* /usr/include/libpurple/sound.h
* /usr/include/libpurple/sslconn.h
* /usr/include/libpurple/status.h
* /usr/include/libpurple/stringref.h
* /usr/include/libpurple/stun.h
* /usr/include/libpurple/theme-loader.h
* /usr/include/libpurple/theme-manager.h
* /usr/include/libpurple/theme.h
* /usr/include/libpurple/upnp.h
* /usr/include/libpurple/util.h
* /usr/include/libpurple/value.h
* /usr/include/libpurple/version.h
* /usr/include/libpurple/whiteboard.h
* /usr/include/libpurple/xmlnode.h
* /usr/lib/libpurple-client.so
* /usr/lib/libpurple-client.so.0
* /usr/lib/libpurple-client.so.0.14.14
* /usr/lib/libpurple.so
* /usr/lib/libpurple.so.0
* /usr/lib/libpurple.so.0.14.14
* /usr/lib/pkgconfig/purple.pc
* /usr/lib/purple-2/autoaccept.so
* /usr/lib/purple-2/buddynote.so
* /usr/lib/purple-2/dbus-example.so
* /usr/lib/purple-2/idle.so
* /usr/lib/purple-2/joinpart.so
* /usr/lib/purple-2/libgg.so
* /usr/lib/purple-2/libirc.so
* /usr/lib/purple-2/libjabber.so
* /usr/lib/purple-2/libjabber.so.0
* /usr/lib/purple-2/libjabber.so.0.0.0
* /usr/lib/purple-2/libnovell.so
* /usr/lib/purple-2/libsametime.so
* /usr/lib/purple-2/libsimple.so
* /usr/lib/purple-2/libxmpp.so
* /usr/lib/purple-2/libzephyr.so
* /usr/lib/purple-2/log_reader.so
* /usr/lib/purple-2/newline.so
* /usr/lib/purple-2/nss-prefs.so
* /usr/lib/purple-2/offlinemsg.so
* /usr/lib/purple-2/perl.so
* /usr/lib/purple-2/perl/auto/Purple/.packlist
* /usr/lib/purple-2/perl/auto/Purple/autosplit.ix
* /usr/lib/purple-2/perl/auto/Purple/Purple.so
* /usr/lib/purple-2/perl/Purple.pm
* /usr/lib/purple-2/psychic.so
* /usr/lib/purple-2/ssl-gnutls.so
* /usr/lib/purple-2/ssl-nss.so
* /usr/lib/purple-2/ssl.so
* /usr/lib/purple-2/statenotify.so
* /usr/share/aclocal/purple.m4
