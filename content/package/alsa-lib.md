+++
draft = false
title = "alsa-lib 1.2.12-1"
version = "1.2.12-1"
description = "An alternative implementation of Linux sound support"
date = "2024-06-12T08:53:39"
aliases = "/packages/2345"
categories = ['multimedia']
upstreamurl = "https://www.alsa-project.org"
arch = "x86_64"
size = "509636"
usize = "1909177"
sha1sum = "e156c8ff5d6ac730e7dbabb9836f6c8d6a842894"
depends = "['alsa-topology-conf', 'alsa-ucm-conf', 'glibc>=2.34']"
reverse_depends = "['allegro', 'alsa-plugins', 'alsa-tools', 'alsa-utils', 'bluez', 'cef', 'enlightenment', 'ffmpeg', 'ffmpeg4.4', 'firefox', 'gst1-plugins-base-alsa', 'jack2', 'libao', 'libcanberra-alsa', 'libpulse', 'libsndfile', 'lirc', 'mlt', 'pcaudiolib', 'portaudio', 'portmidi', 'pyalsa', 'qemu', 'qt5-webengine', 'qv4l2', 'sphinxbase', 'spice-vdagent', 'stepmania', 'teams', 'tuxguitar', 'v4l-utils', 'virtualbox', 'vlc', 'volumeicon', 'whalebird', 'wildmidi', 'xcfa', 'xonotic']"
+++
### Description: 
An alternative implementation of Linux sound support

### Files: 
* /usr/bin/aserver
* /usr/include/alsa/asoundef.h
* /usr/include/alsa/asoundlib.h
* /usr/include/alsa/conf.h
* /usr/include/alsa/control.h
* /usr/include/alsa/control_external.h
* /usr/include/alsa/control_plugin.h
* /usr/include/alsa/error.h
* /usr/include/alsa/global.h
* /usr/include/alsa/hwdep.h
* /usr/include/alsa/input.h
* /usr/include/alsa/mixer.h
* /usr/include/alsa/mixer_abst.h
* /usr/include/alsa/output.h
* /usr/include/alsa/pcm.h
* /usr/include/alsa/pcm_external.h
* /usr/include/alsa/pcm_extplug.h
* /usr/include/alsa/pcm_ioplug.h
* /usr/include/alsa/pcm_old.h
* /usr/include/alsa/pcm_plugin.h
* /usr/include/alsa/pcm_rate.h
* /usr/include/alsa/rawmidi.h
* /usr/include/alsa/seq.h
* /usr/include/alsa/seqmid.h
* /usr/include/alsa/seq_event.h
* /usr/include/alsa/seq_midi_event.h
* /usr/include/alsa/sound/asoc.h
* /usr/include/alsa/sound/asound_fm.h
* /usr/include/alsa/sound/emu10k1.h
* /usr/include/alsa/sound/hdsp.h
* /usr/include/alsa/sound/hdspm.h
* /usr/include/alsa/sound/sb16_csp.h
* /usr/include/alsa/sound/sscape_ioctl.h
* /usr/include/alsa/sound/tlv.h
* /usr/include/alsa/sound/type_compat.h
* /usr/include/alsa/sound/uapi/asoc.h
* /usr/include/alsa/sound/uapi/asound_fm.h
* /usr/include/alsa/sound/uapi/emu10k1.h
* /usr/include/alsa/sound/uapi/hdsp.h
* /usr/include/alsa/sound/uapi/hdspm.h
* /usr/include/alsa/sound/uapi/sb16_csp.h
* /usr/include/alsa/sound/uapi/sscape_ioctl.h
* /usr/include/alsa/sound/uapi/tlv.h
* /usr/include/alsa/timer.h
* /usr/include/alsa/topology.h
* /usr/include/alsa/ump.h
* /usr/include/alsa/ump_msg.h
* /usr/include/alsa/use-case.h
* /usr/include/alsa/version.h
* /usr/include/asoundlib.h
* /usr/include/sys/asoundlib.h
* /usr/lib/libasound.so
* /usr/lib/libasound.so.2
* /usr/lib/libasound.so.2.0.0
* /usr/lib/libatopology.so
* /usr/lib/libatopology.so.2
* /usr/lib/libatopology.so.2.0.0
* /usr/lib/pkgconfig/alsa-topology.pc
* /usr/lib/pkgconfig/alsa.pc
* /usr/share/aclocal/alsa.m4
* /usr/share/alsa/alsa.conf
* /usr/share/alsa/cards/AACI.conf
* /usr/share/alsa/cards/aliases.conf
* /usr/share/alsa/cards/ATIIXP-MODEM.conf
* /usr/share/alsa/cards/ATIIXP-SPDMA.conf
* /usr/share/alsa/cards/ATIIXP.conf
* /usr/share/alsa/cards/AU8810.conf
* /usr/share/alsa/cards/AU8820.conf
* /usr/share/alsa/cards/AU8830.conf
* /usr/share/alsa/cards/Audigy.conf
* /usr/share/alsa/cards/Audigy2.conf
* /usr/share/alsa/cards/Aureon51.conf
* /usr/share/alsa/cards/Aureon71.conf
* /usr/share/alsa/cards/CA0106.conf
* /usr/share/alsa/cards/CMI8338-SWIEC.conf
* /usr/share/alsa/cards/CMI8338.conf
* /usr/share/alsa/cards/CMI8738-MC6.conf
* /usr/share/alsa/cards/CMI8738-MC8.conf
* /usr/share/alsa/cards/CMI8788.conf
* /usr/share/alsa/cards/CS46xx.conf
* /usr/share/alsa/cards/Echo_Echo3G.conf
* /usr/share/alsa/cards/EMU10K1.conf
* /usr/share/alsa/cards/EMU10K1X.conf
* /usr/share/alsa/cards/ENS1370.conf
* /usr/share/alsa/cards/ENS1371.conf
* /usr/share/alsa/cards/ES1968.conf
* /usr/share/alsa/cards/FireWave.conf
* /usr/share/alsa/cards/FM801.conf
* /usr/share/alsa/cards/FWSpeakers.conf
* /usr/share/alsa/cards/GUS.conf
* /usr/share/alsa/cards/HDA-Intel.conf
* /usr/share/alsa/cards/HdmiLpeAudio.conf
* /usr/share/alsa/cards/ICE1712.conf
* /usr/share/alsa/cards/ICE1724.conf
* /usr/share/alsa/cards/ICH-MODEM.conf
* /usr/share/alsa/cards/ICH.conf
* /usr/share/alsa/cards/ICH4.conf
* /usr/share/alsa/cards/Loopback.conf
* /usr/share/alsa/cards/Maestro3.conf
* /usr/share/alsa/cards/NFORCE.conf
* /usr/share/alsa/cards/PC-Speaker.conf
* /usr/share/alsa/cards/pistachio-card.conf
* /usr/share/alsa/cards/PMac.conf
* /usr/share/alsa/cards/PMacToonie.conf
* /usr/share/alsa/cards/PS3.conf
* /usr/share/alsa/cards/RME9636.conf
* /usr/share/alsa/cards/RME9652.conf
* /usr/share/alsa/cards/SB-XFi.conf
* /usr/share/alsa/cards/SI7018.conf
* /usr/share/alsa/cards/TRID4DWAVENX.conf
* /usr/share/alsa/cards/USB-Audio.conf
* /usr/share/alsa/cards/vc4-hdmi.conf
* /usr/share/alsa/cards/VIA686A.conf
* /usr/share/alsa/cards/VIA8233.conf
* /usr/share/alsa/cards/VIA8233A.conf
* /usr/share/alsa/cards/VIA8237.conf
* /usr/share/alsa/cards/VX222.conf
* /usr/share/alsa/cards/VXPocket.conf
* /usr/share/alsa/cards/VXPocket440.conf
* /usr/share/alsa/cards/YMF744.conf
* /usr/share/alsa/ctl/default.conf
* /usr/share/alsa/pcm/center_lfe.conf
* /usr/share/alsa/pcm/default.conf
* /usr/share/alsa/pcm/dmix.conf
* /usr/share/alsa/pcm/dpl.conf
* /usr/share/alsa/pcm/dsnoop.conf
* /usr/share/alsa/pcm/front.conf
* /usr/share/alsa/pcm/hdmi.conf
* /usr/share/alsa/pcm/iec958.conf
* /usr/share/alsa/pcm/modem.conf
* /usr/share/alsa/pcm/rear.conf
* /usr/share/alsa/pcm/side.conf
* /usr/share/alsa/pcm/surround21.conf
* /usr/share/alsa/pcm/surround40.conf
* /usr/share/alsa/pcm/surround41.conf
* /usr/share/alsa/pcm/surround50.conf
* /usr/share/alsa/pcm/surround51.conf
* /usr/share/alsa/pcm/surround71.conf
* /usr/share/doc/alsa-lib-1.2.12/ChangeLog
* /usr/share/doc/alsa-lib-1.2.12/COPYING
* /usr/share/doc/alsa-lib-1.2.12/INSTALL
* /usr/share/doc/alsa-lib-1.2.12/README.md
* /usr/share/doc/alsa-lib-1.2.12/TODO
