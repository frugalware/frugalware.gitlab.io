+++
draft = false
title = "plasma-pa 5.27.10-5"
version = "5.27.10-5"
description = "Plasma applet written in QML for PulseAudio"
date = "2024-02-19T12:25:32"
aliases = "/packages/218400"
categories = ['plasma']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "246664"
usize = "1170439"
sha1sum = "c0d110109cae4d6329c3b21d5dffc0b06adbaedf"
depends = "['gst1-plugins-good-pulseaudio', 'kcmutils>=5.115.0', 'kdeclarative>=5.115.0', 'libcanberra', 'libcanberra-pulseaudio', 'phonon-backend-gstreamer', 'plasma-framework>=5.115.0', 'pulseaudio', 'sound-theme-freedesktop']"
reverse_depends = "['plasma-bigscreen']"
+++
Plasma applet written in QML for PulseAudio

{{< files text="show files" >}}* /usr/lib/qt5/plugins/plasma/kcms/systemsettings/kcm_pulseaudio.so
* /usr/share/applications/kcm_pulseaudio.desktop
* /usr/share/doc/HTML/ca/kcontrol/plasma-pa/index.cache.bz2
* /usr/share/doc/HTML/ca/kcontrol/plasma-pa/index.docbook
* /usr/share/doc/HTML/de/kcontrol/plasma-pa/index.cache.bz2
* /usr/share/doc/HTML/de/kcontrol/plasma-pa/index.docbook
* /usr/share/doc/HTML/en/kcontrol/plasma-pa/index.cache.bz2
* /usr/share/doc/HTML/en/kcontrol/plasma-pa/index.docbook
* /usr/share/doc/HTML/es/kcontrol/plasma-pa/index.cache.bz2
* /usr/share/doc/HTML/es/kcontrol/plasma-pa/index.docbook
* /usr/share/doc/HTML/id/kcontrol/plasma-pa/index.cache.bz2
* /usr/share/doc/HTML/id/kcontrol/plasma-pa/index.docbook
* /usr/share/doc/HTML/it/kcontrol/plasma-pa/index.cache.bz2
* /usr/share/doc/HTML/it/kcontrol/plasma-pa/index.docbook
* /usr/share/doc/HTML/nl/kcontrol/plasma-pa/index.cache.bz2
* /usr/share/doc/HTML/nl/kcontrol/plasma-pa/index.docbook
* /usr/share/doc/HTML/pt/kcontrol/plasma-pa/index.cache.bz2
* /usr/share/doc/HTML/pt/kcontrol/plasma-pa/index.docbook
* /usr/share/doc/HTML/pt_BR/kcontrol/plasma-pa/index.cache.bz2
* /usr/share/doc/HTML/pt_BR/kcontrol/plasma-pa/index.docbook
* /usr/share/doc/HTML/ru/kcontrol/plasma-pa/index.cache.bz2
* /usr/share/doc/HTML/ru/kcontrol/plasma-pa/index.docbook
* /usr/share/doc/HTML/sv/kcontrol/plasma-pa/index.cache.bz2
* /usr/share/doc/HTML/sv/kcontrol/plasma-pa/index.docbook
* /usr/share/doc/HTML/uk/kcontrol/plasma-pa/index.cache.bz2
* /usr/share/doc/HTML/uk/kcontrol/plasma-pa/index.docbook
* /usr/share/kconf_update/disable_kmix.upd
* /usr/share/kconf_update/plasmaVolumeDisableKMixAutostart.pl
* /usr/share/kde4/apps/kconf_update/disable_kmix.upd
* /usr/share/kde4/apps/kconf_update/plasmaVolumeDisableKMixAutostart.pl
* /usr/share/kpackage/kcms/kcm_pulseaudio/contents/code/icon.js
* /usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/CardListItem.qml
* /usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/DeviceComboBox.qml
* /usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/DeviceListItem.qml
* /usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/main.qml
* /usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/MuteButton.qml
* /usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/StreamListItem.qml
* /usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/VolumeControlsConfig.qml
* /usr/share/kpackage/kcms/kcm_pulseaudio/contents/ui/VolumeSlider.qml
* /usr/share/kservices5/plasma-applet-org.kde.plasma.volume.desktop
* /usr/share/locale/ar/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/ar/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/az/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/az/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/bg/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/bg/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/ca/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/ca/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/cs/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/cs/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/da/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/da/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/de/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/de/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/el/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/el/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/en_GB/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/en_GB/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/es/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/es/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/et/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/et/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/eu/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/eu/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/fi/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/fi/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/fr/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/fr/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/gl/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/gl/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/he/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/he/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/hsb/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/hu/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/hu/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/ia/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/ia/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/id/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/id/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/it/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/it/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/ja/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/ja/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/ka/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/ka/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/ko/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/ko/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/lt/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/lt/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/lv/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/ml/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/ml/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/nb/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/nl/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/nl/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/nn/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/nn/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/pa/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/pa/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/pl/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/pl/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/pt/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/pt/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/ro/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/ro/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/ru/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/ru/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/sk/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/sk/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/sl/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/sl/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/sr/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/sr/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/sr@ijekavian/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/sr@ijekavian/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/sv/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/sv/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/ta/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/ta/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/tr/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/tr/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/uk/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/uk/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/kcm_pulseaudio.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/plasma_applet_org.kde.plasma.volume.mo
* /usr/share/metainfo/org.kde.plasma.volume.appdata.xml
* /usr/share/plasma/plasmoids/org.kde.plasma.volume/contents/code/icon.js
* /usr/share/plasma/plasmoids/org.kde.plasma.volume/contents/config/main.xml
* /usr/share/plasma/plasmoids/org.kde.plasma.volume/contents/ui/DeviceListItem.qml
* /usr/share/plasma/plasmoids/org.kde.plasma.volume/contents/ui/HorizontalStackView.qml
* /usr/share/plasma/plasmoids/org.kde.plasma.volume/contents/ui/ListItemBase.qml
* /usr/share/plasma/plasmoids/org.kde.plasma.volume/contents/ui/main.qml
* /usr/share/plasma/plasmoids/org.kde.plasma.volume/contents/ui/SmallToolButton.qml
* /usr/share/plasma/plasmoids/org.kde.plasma.volume/contents/ui/StreamListItem.qml
* /usr/share/plasma/plasmoids/org.kde.plasma.volume/contents/ui/VolumeSlider.qml
* /usr/share/plasma/plasmoids/org.kde.plasma.volume/metadata.desktop
* /usr/share/plasma/plasmoids/org.kde.plasma.volume/metadata.json
* /usr/share/qt5/qml/org/kde/plasma/private/volume/libplasma-volume-declarative.so
* /usr/share/qt5/qml/org/kde/plasma/private/volume/PulseObjectFilterModel.qml
* /usr/share/qt5/qml/org/kde/plasma/private/volume/qmldir
{{< /files >}}