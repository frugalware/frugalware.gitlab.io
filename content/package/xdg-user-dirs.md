+++
draft = false
title = "xdg-user-dirs 0.18-1"
version = "0.18-1"
description = "xdg-user-dirs is a tool to help manage user directories like the desktop folder and the music folder."
date = "2023-01-06T13:30:12"
aliases = "/packages/50049"
categories = ['apps']
upstreamurl = "http://www.freedesktop.org/wiki/Software/xdg-user-dirs"
arch = "x86_64"
size = "53980"
usize = "257602"
sha1sum = "01e39400124a878670f6b36df4eeecbf6cd9a01c"
depends = "['glibc>=2.29-6']"
reverse_depends = "['lumina-desktop', 'plasma-workspace', 'xdg-user-dirs-gtk']"
+++
xdg-user-dirs is a tool to help manage user directories like the desktop folder and the music folder."

{{< files text="show files" >}}* /etc/X11/xinit/xinitrc.d/xdg-user-dirs.sh
* /etc/xdg/autostart/xdg-user-dirs.desktop
* /etc/xdg/user-dirs.conf
* /etc/xdg/user-dirs.defaults
* /usr/bin/xdg-user-dir
* /usr/bin/xdg-user-dirs-update
* /usr/share/doc/xdg-user-dirs-0.18/AUTHORS
* /usr/share/doc/xdg-user-dirs-0.18/ChangeLog
* /usr/share/doc/xdg-user-dirs-0.18/COPYING
* /usr/share/doc/xdg-user-dirs-0.18/NEWS
* /usr/share/doc/xdg-user-dirs-0.18/README
* /usr/share/locale/af/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/an/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/ar/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/as/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/ast/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/be/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/be@latin/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/bg/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/bn_IN/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/br/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/ca/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/crh/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/cs/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/da/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/de/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/el/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/eo/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/es/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/et/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/eu/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/fa/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/fi/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/fr/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/fur/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/ga/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/gd/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/gl/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/gu/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/he/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/hi/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/hr/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/hu/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/ia/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/id/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/is/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/it/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/ja/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/kk/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/kn/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/ko/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/ku/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/ky/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/lt/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/lv/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/mk/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/ml/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/mr/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/nb/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/nds/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/nl/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/nn/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/or/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/pa/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/pl/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/ps/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/pt/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/ro/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/ru/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/sk/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/sl/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/sq/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/sr/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/sr@Latn/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/sv/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/ta/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/te/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/th/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/tr/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/uk/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/vi/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/zh_HK/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/xdg-user-dirs.mo
* /usr/share/man/man1/xdg-user-dir.1.gz
* /usr/share/man/man1/xdg-user-dirs-update.1.gz
* /usr/share/man/man5/user-dirs.conf.5.gz
* /usr/share/man/man5/user-dirs.defaults.5.gz
* /usr/share/man/man5/user-dirs.dirs.5.gz
{{< /files >}}