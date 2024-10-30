+++
draft = false
title = "liblcf 0.8-4"
version = "0.8-4"
description = "liblcf is a library to handle RPG Maker 2000 and 2003 game data."
date = "2024-10-30T21:19:23"
aliases = "/packages/217396"
categories = ['lib-extra']
upstreamurl = "https://easyrpg.org"
arch = "x86_64"
size = "452496"
usize = "2441830"
sha1sum = "d5ab79dc93823cab6d104ef4c5c0764a68996435"
depends = "['expat', 'icu4c>=76.1']"
reverse_depends = "['easyrpg-player']"
+++
### Description: 
liblcf is a library to handle RPG Maker 2000 and 2003 game data.

### Files: 
* /usr/bin/lcf2xml
* /usr/bin/lcfstrings
* /usr/include/lcf/config.h
* /usr/include/lcf/context.h
* /usr/include/lcf/dbarray.h
* /usr/include/lcf/dbarrayalloc.h
* /usr/include/lcf/dbbitarray.h
* /usr/include/lcf/dbstring.h
* /usr/include/lcf/encoder.h
* /usr/include/lcf/enum_tags.h
* /usr/include/lcf/flag_set.h
* /usr/include/lcf/ini.h
* /usr/include/lcf/inireader.h
* /usr/include/lcf/ldb/chunks.h
* /usr/include/lcf/ldb/reader.h
* /usr/include/lcf/lmt/chunks.h
* /usr/include/lcf/lmt/reader.h
* /usr/include/lcf/lmu/chunks.h
* /usr/include/lcf/lmu/reader.h
* /usr/include/lcf/lsd/chunks.h
* /usr/include/lcf/lsd/reader.h
* /usr/include/lcf/reader_lcf.h
* /usr/include/lcf/reader_util.h
* /usr/include/lcf/reader_xml.h
* /usr/include/lcf/rpg/actor.h
* /usr/include/lcf/rpg/animation.h
* /usr/include/lcf/rpg/animationcelldata.h
* /usr/include/lcf/rpg/animationframe.h
* /usr/include/lcf/rpg/animationtiming.h
* /usr/include/lcf/rpg/attribute.h
* /usr/include/lcf/rpg/battlecommand.h
* /usr/include/lcf/rpg/battlecommands.h
* /usr/include/lcf/rpg/battleranimation.h
* /usr/include/lcf/rpg/battleranimationitemskill.h
* /usr/include/lcf/rpg/battleranimationpose.h
* /usr/include/lcf/rpg/battleranimationweapon.h
* /usr/include/lcf/rpg/chipset.h
* /usr/include/lcf/rpg/class.h
* /usr/include/lcf/rpg/commonevent.h
* /usr/include/lcf/rpg/database.h
* /usr/include/lcf/rpg/encounter.h
* /usr/include/lcf/rpg/enemy.h
* /usr/include/lcf/rpg/enemyaction.h
* /usr/include/lcf/rpg/equipment.h
* /usr/include/lcf/rpg/event.h
* /usr/include/lcf/rpg/eventcommand.h
* /usr/include/lcf/rpg/eventpage.h
* /usr/include/lcf/rpg/eventpagecondition.h
* /usr/include/lcf/rpg/fwd.h
* /usr/include/lcf/rpg/item.h
* /usr/include/lcf/rpg/learning.h
* /usr/include/lcf/rpg/map.h
* /usr/include/lcf/rpg/mapinfo.h
* /usr/include/lcf/rpg/movecommand.h
* /usr/include/lcf/rpg/moveroute.h
* /usr/include/lcf/rpg/music.h
* /usr/include/lcf/rpg/parameters.h
* /usr/include/lcf/rpg/rect.h
* /usr/include/lcf/rpg/save.h
* /usr/include/lcf/rpg/saveactor.h
* /usr/include/lcf/rpg/savecommonevent.h
* /usr/include/lcf/rpg/saveeasyrpgdata.h
* /usr/include/lcf/rpg/saveeasyrpgtext.h
* /usr/include/lcf/rpg/saveeasyrpgwindow.h
* /usr/include/lcf/rpg/saveeventexecframe.h
* /usr/include/lcf/rpg/saveeventexecstate.h
* /usr/include/lcf/rpg/saveinventory.h
* /usr/include/lcf/rpg/savemapevent.h
* /usr/include/lcf/rpg/savemapeventbase.h
* /usr/include/lcf/rpg/savemapinfo.h
* /usr/include/lcf/rpg/savepanorama.h
* /usr/include/lcf/rpg/savepartylocation.h
* /usr/include/lcf/rpg/savepicture.h
* /usr/include/lcf/rpg/savescreen.h
* /usr/include/lcf/rpg/savesystem.h
* /usr/include/lcf/rpg/savetarget.h
* /usr/include/lcf/rpg/savetitle.h
* /usr/include/lcf/rpg/savevehiclelocation.h
* /usr/include/lcf/rpg/skill.h
* /usr/include/lcf/rpg/sound.h
* /usr/include/lcf/rpg/start.h
* /usr/include/lcf/rpg/state.h
* /usr/include/lcf/rpg/switch.h
* /usr/include/lcf/rpg/system.h
* /usr/include/lcf/rpg/terms.h
* /usr/include/lcf/rpg/terrain.h
* /usr/include/lcf/rpg/testbattler.h
* /usr/include/lcf/rpg/treemap.h
* /usr/include/lcf/rpg/troop.h
* /usr/include/lcf/rpg/troopmember.h
* /usr/include/lcf/rpg/trooppage.h
* /usr/include/lcf/rpg/trooppagecondition.h
* /usr/include/lcf/rpg/variable.h
* /usr/include/lcf/saveopt.h
* /usr/include/lcf/scope_guard.h
* /usr/include/lcf/span.h
* /usr/include/lcf/string_view.h
* /usr/include/lcf/third_party/span.h
* /usr/include/lcf/third_party/string_view.h
* /usr/include/lcf/writer_lcf.h
* /usr/include/lcf/writer_xml.h
* /usr/lib/cmake/liblcf/liblcf-config-version.cmake
* /usr/lib/cmake/liblcf/liblcf-config.cmake
* /usr/lib/cmake/liblcf/liblcf-targets-release.cmake
* /usr/lib/cmake/liblcf/liblcf-targets.cmake
* /usr/lib/liblcf.so
* /usr/lib/liblcf.so.0
* /usr/lib/pkgconfig/liblcf.pc
* /usr/share/doc/liblcf-0.8/COPYING
* /usr/share/doc/liblcf-0.8/README.md
* /usr/share/mime/packages/liblcf.xml
