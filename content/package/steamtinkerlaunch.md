+++
draft = false
title = "steamtinkerlaunch 12.12-1"
version = "12.12-1"
description = "Wrapper script for Steam custom launch options"
date = "2023-03-31T11:42:21"
aliases = "/packages/220323"
categories = ['games-extra']
upstreamurl = "https://github.com/frostworx/steamtinkerlaunch"
arch = "x86_64"
size = "273792"
usize = "1600162"
sha1sum = "9569619cac01cb330134d92de7e52a4bda378cb5"
depends = "['bash', 'bc', 'git', 'procps-ng', 'unzip', 'which', 'xdotool', 'xprop', 'xrandr', 'xwininfo', 'yad']"
+++
### Description: 
Wrapper script for Steam custom launch options

### Files: 
* /usr/bin/steamtinkerlaunch
* /usr/share/applications
* /usr/share/doc/steamtinkerlaunch-12.12/LICENSE
* /usr/share/doc/steamtinkerlaunch-12.12/README.md
* /usr/share/icons/hicolor/scalable/apps
* /usr/share/steamtinkerlaunch/collections/Backup.conf
* /usr/share/steamtinkerlaunch/collections/BlockInternet.conf
* /usr/share/steamtinkerlaunch/collections/Conty.conf
* /usr/share/steamtinkerlaunch/collections/DelCompat.conf
* /usr/share/steamtinkerlaunch/collections/Dependencies.conf
* /usr/share/steamtinkerlaunch/collections/DLSS.conf
* /usr/share/steamtinkerlaunch/collections/DOSBox.conf
* /usr/share/steamtinkerlaunch/collections/FSR.conf
* /usr/share/steamtinkerlaunch/collections/FWS.conf
* /usr/share/steamtinkerlaunch/collections/GDB.conf
* /usr/share/steamtinkerlaunch/collections/Geo11-VR.conf
* /usr/share/steamtinkerlaunch/collections/Geo11.conf
* /usr/share/steamtinkerlaunch/collections/Luxtorpeda.conf
* /usr/share/steamtinkerlaunch/collections/MangoApp.conf
* /usr/share/steamtinkerlaunch/collections/MangoHud.conf
* /usr/share/steamtinkerlaunch/collections/MangoHudCfg.conf
* /usr/share/steamtinkerlaunch/collections/MO2.conf
* /usr/share/steamtinkerlaunch/collections/OpenVR-FSR.conf
* /usr/share/steamtinkerlaunch/collections/PEV.conf
* /usr/share/steamtinkerlaunch/collections/PrimeRun.conf
* /usr/share/steamtinkerlaunch/collections/Raytracing.conf
* /usr/share/steamtinkerlaunch/collections/Regedit.conf
* /usr/share/steamtinkerlaunch/collections/ReShade.conf
* /usr/share/steamtinkerlaunch/collections/ReShadeSBS.conf
* /usr/share/steamtinkerlaunch/collections/ReShadeVR.conf
* /usr/share/steamtinkerlaunch/collections/SBS-VR.conf
* /usr/share/steamtinkerlaunch/collections/SBS.conf
* /usr/share/steamtinkerlaunch/collections/ScummVM.conf
* /usr/share/steamtinkerlaunch/collections/SortGameArgs.conf
* /usr/share/steamtinkerlaunch/collections/SpecialK.conf
* /usr/share/steamtinkerlaunch/collections/Vortex.conf
* /usr/share/steamtinkerlaunch/collections/Wine.conf
* /usr/share/steamtinkerlaunch/collections/Wineconsole.conf
* /usr/share/steamtinkerlaunch/collections/x64dbg.conf
* /usr/share/steamtinkerlaunch/collections/Zink.conf
* /usr/share/steamtinkerlaunch/eval/order.txt
* /usr/share/steamtinkerlaunch/eval/packages/directx2010
* /usr/share/steamtinkerlaunch/eval/packages/dotnet35
* /usr/share/steamtinkerlaunch/eval/packages/dotnet40
* /usr/share/steamtinkerlaunch/eval/packages/dotnet40-client-profile
* /usr/share/steamtinkerlaunch/eval/packages/dotnet452
* /usr/share/steamtinkerlaunch/eval/packages/dotnet46
* /usr/share/steamtinkerlaunch/eval/packages/dotnet472
* /usr/share/steamtinkerlaunch/eval/packages/dotnet48
* /usr/share/steamtinkerlaunch/eval/packages/openal
* /usr/share/steamtinkerlaunch/eval/packages/physx-9.12
* /usr/share/steamtinkerlaunch/eval/packages/physx-9.14
* /usr/share/steamtinkerlaunch/eval/packages/vcredist2005
* /usr/share/steamtinkerlaunch/eval/packages/vcredist2008
* /usr/share/steamtinkerlaunch/eval/packages/vcredist2010
* /usr/share/steamtinkerlaunch/eval/packages/vcredist2012
* /usr/share/steamtinkerlaunch/eval/packages/vcredist2013
* /usr/share/steamtinkerlaunch/eval/packages/vcredist2015
* /usr/share/steamtinkerlaunch/eval/packages/vcredist2017
* /usr/share/steamtinkerlaunch/eval/packages/vcredist2019
* /usr/share/steamtinkerlaunch/eval/packages/vcredist2022
* /usr/share/steamtinkerlaunch/eval/packages/xna40
* /usr/share/steamtinkerlaunch/eval/sets/evaluatorscript_depressurizer.vdf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-AddVortexStage.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-Ask_Recreate_Compatdata.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-CategorySelection.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-chooseWinetricksPrefix.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-CreateCustomEvaluatorScript.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-DownloadCustomProton.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-DownloadWine.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-DXVK-Hud-Options.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-Editor.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-EntryBlockSelection.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-Favorites.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-FavoritesSelection.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-GameScopeGui.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-Gui.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-HelpUrlMenu.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-HMM.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-installVortexGui.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-launchGameMenu.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-launchGameTemplateMenu.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-launchGlobalMenu.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-MainMenu.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-Misc.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-non-steam game.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-OneTimeRunGui.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-PressureVessel.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-Proton.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-set game artwork.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-SetWineDebugChannels.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-Shader.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-SortCategories.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-SteamGridDB.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-Stl.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-Tools.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-Urls.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-Vortex.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-VortexOptions.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-VR.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-Wine.conf
* /usr/share/steamtinkerlaunch/guicfgs/1920x1080/template/SteamTinkerLaunch-WinetricksPackageSelection-dlls.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-AddVortexStage.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-Ask_Recreate_Compatdata.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-CategorySelection.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-chooseWinetricksPrefix.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-DownloadCustomProton.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-DownloadWine.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-DXVK-Hud-Options.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-Editor.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-EntryBlockSelection.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-Favorites.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-FavoritesSelection.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-GameScopeGui.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-Gui.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-HelpUrlMenu.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-HMM.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-installVortexGui.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-launchGameMenu.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-launchGameTemplateMenu.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-launchGlobalMenu.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-MainMenu.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-Misc.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-non-steam game.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-OneTimeRunGui.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-PressureVessel.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-Proton.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-set game artwork.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-SetWineDebugChannels.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-Shader.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-SortCategories.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-SteamCollectionSelection.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-SteamGridDB.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-Stl.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-Tools.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-Urls.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-Vortex Toggle.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-Vortex.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-VortexOptions.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-VR.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-Wine.conf
* /usr/share/steamtinkerlaunch/guicfgs/3840x2160/template/SteamTinkerLaunch-WinetricksPackageSelection-dlls.conf
* /usr/share/steamtinkerlaunch/lang/chinese.txt
* /usr/share/steamtinkerlaunch/lang/dutch.txt
* /usr/share/steamtinkerlaunch/lang/english.txt
* /usr/share/steamtinkerlaunch/lang/englishUK.txt
* /usr/share/steamtinkerlaunch/lang/french.txt
* /usr/share/steamtinkerlaunch/lang/german.txt
* /usr/share/steamtinkerlaunch/lang/italian.txt
* /usr/share/steamtinkerlaunch/lang/polish.txt
* /usr/share/steamtinkerlaunch/lang/russian.txt
* /usr/share/steamtinkerlaunch/misc/appinfo.txt
* /usr/share/steamtinkerlaunch/misc/dxvk-no-nvapiHack.conf
* /usr/share/steamtinkerlaunch/misc/favorites.conf
* /usr/share/steamtinkerlaunch/misc/helpurls.txt
* /usr/share/steamtinkerlaunch/misc/hmmgames.txt
* /usr/share/steamtinkerlaunch/misc/mo2games.txt
* /usr/share/steamtinkerlaunch/misc/repocustomlist.txt
* /usr/share/steamtinkerlaunch/misc/sbstweaks/108800.conf
* /usr/share/steamtinkerlaunch/misc/sbstweaks/108800.sh
* /usr/share/steamtinkerlaunch/misc/sbstweaks/1282690.conf
* /usr/share/steamtinkerlaunch/misc/sbstweaks/208200.conf
* /usr/share/steamtinkerlaunch/misc/sbstweaks/214490.conf
* /usr/share/steamtinkerlaunch/misc/sbstweaks/319910.conf
* /usr/share/steamtinkerlaunch/misc/sbstweaks/35700.conf
* /usr/share/steamtinkerlaunch/misc/sbstweaks/35720.conf
* /usr/share/steamtinkerlaunch/misc/sbstweaks/391220.conf
* /usr/share/steamtinkerlaunch/misc/sbstweaks/425210.conf
* /usr/share/steamtinkerlaunch/misc/sbstweaks/444000.conf
* /usr/share/steamtinkerlaunch/misc/sbstweaks/539330.conf
* /usr/share/steamtinkerlaunch/misc/sbstweaks/71340.conf
* /usr/share/steamtinkerlaunch/misc/sbstweaks/750920.conf
* /usr/share/steamtinkerlaunch/misc/steamtinkerlaunch.desktop
* /usr/share/steamtinkerlaunch/misc/steamtinkerlaunch.svg
* /usr/share/steamtinkerlaunch/misc/steamworks-shared.txt
* /usr/share/steamtinkerlaunch/misc/stl-steamdeck-control.vdf
* /usr/share/steamtinkerlaunch/misc/stl-vr-patch
* /usr/share/steamtinkerlaunch/misc/vortexgames.txt
* /usr/share/steamtinkerlaunch/misc/winedebugchannels.txt
* /usr/share/steamtinkerlaunch/misc/x64dbg.reg
