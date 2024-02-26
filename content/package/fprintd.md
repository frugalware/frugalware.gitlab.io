+++
draft = false
title = "fprintd 1.94.2-3"
version = "1.94.2-3"
description = "D-Bus daemon that offers libfprint functionality over the D-Bus interprocess communication bus."
date = "2024-01-14T15:56:17"
aliases = "/packages/217782"
categories = ['apps-extra']
upstreamurl = "http://www.freedesktop.org/wiki/Software/fprint/fprintd"
arch = "x86_64"
size = "123520"
usize = "811041"
sha1sum = "17b43b68c56acbeceb42738a45dac70c57ce3b1f"
depends = "['libfprint>=0.6.0', 'libgudev', 'polkit>=0.113-5']"
+++
D-Bus daemon that offers libfprint functionality over the D-Bus interprocess communication bus."

{{< files text="show files" >}}* /etc/fprintd.conf
* /usr/bin/fprintd-delete
* /usr/bin/fprintd-enroll
* /usr/bin/fprintd-list
* /usr/bin/fprintd-verify
* /usr/lib/fprintd/fprintd
* /usr/lib/security/pam_fprintd.so
* /usr/lib/systemd/system/fprintd.service
* /usr/share/dbus-1/interfaces/net.reactivated.Fprint.Device.xml
* /usr/share/dbus-1/interfaces/net.reactivated.Fprint.Manager.xml
* /usr/share/dbus-1/system-services/net.reactivated.Fprint.service
* /usr/share/dbus-1/system.d/net.reactivated.Fprint.conf
* /usr/share/doc/fprintd-1.94.2/AUTHORS
* /usr/share/doc/fprintd-1.94.2/COPYING
* /usr/share/doc/fprintd-1.94.2/NEWS
* /usr/share/doc/fprintd-1.94.2/README
* /usr/share/doc/fprintd-1.94.2/TODO
* /usr/share/locale/af/LC_MESSAGES/fprintd.mo
* /usr/share/locale/ar/LC_MESSAGES/fprintd.mo
* /usr/share/locale/as/LC_MESSAGES/fprintd.mo
* /usr/share/locale/ast/LC_MESSAGES/fprintd.mo
* /usr/share/locale/az/LC_MESSAGES/fprintd.mo
* /usr/share/locale/be/LC_MESSAGES/fprintd.mo
* /usr/share/locale/bg/LC_MESSAGES/fprintd.mo
* /usr/share/locale/bn_IN/LC_MESSAGES/fprintd.mo
* /usr/share/locale/ca/LC_MESSAGES/fprintd.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/fprintd.mo
* /usr/share/locale/cs/LC_MESSAGES/fprintd.mo
* /usr/share/locale/cy/LC_MESSAGES/fprintd.mo
* /usr/share/locale/da/LC_MESSAGES/fprintd.mo
* /usr/share/locale/de/LC_MESSAGES/fprintd.mo
* /usr/share/locale/el/LC_MESSAGES/fprintd.mo
* /usr/share/locale/en_GB/LC_MESSAGES/fprintd.mo
* /usr/share/locale/eo/LC_MESSAGES/fprintd.mo
* /usr/share/locale/es/LC_MESSAGES/fprintd.mo
* /usr/share/locale/et/LC_MESSAGES/fprintd.mo
* /usr/share/locale/eu/LC_MESSAGES/fprintd.mo
* /usr/share/locale/fa/LC_MESSAGES/fprintd.mo
* /usr/share/locale/fi/LC_MESSAGES/fprintd.mo
* /usr/share/locale/fo/LC_MESSAGES/fprintd.mo
* /usr/share/locale/fr/LC_MESSAGES/fprintd.mo
* /usr/share/locale/fur/LC_MESSAGES/fprintd.mo
* /usr/share/locale/ga/LC_MESSAGES/fprintd.mo
* /usr/share/locale/gl/LC_MESSAGES/fprintd.mo
* /usr/share/locale/gu/LC_MESSAGES/fprintd.mo
* /usr/share/locale/he/LC_MESSAGES/fprintd.mo
* /usr/share/locale/hi/LC_MESSAGES/fprintd.mo
* /usr/share/locale/hr/LC_MESSAGES/fprintd.mo
* /usr/share/locale/hu/LC_MESSAGES/fprintd.mo
* /usr/share/locale/ia/LC_MESSAGES/fprintd.mo
* /usr/share/locale/id/LC_MESSAGES/fprintd.mo
* /usr/share/locale/it/LC_MESSAGES/fprintd.mo
* /usr/share/locale/ja/LC_MESSAGES/fprintd.mo
* /usr/share/locale/ka/LC_MESSAGES/fprintd.mo
* /usr/share/locale/kk/LC_MESSAGES/fprintd.mo
* /usr/share/locale/kn/LC_MESSAGES/fprintd.mo
* /usr/share/locale/ko/LC_MESSAGES/fprintd.mo
* /usr/share/locale/ky/LC_MESSAGES/fprintd.mo
* /usr/share/locale/lt/LC_MESSAGES/fprintd.mo
* /usr/share/locale/lv/LC_MESSAGES/fprintd.mo
* /usr/share/locale/ml/LC_MESSAGES/fprintd.mo
* /usr/share/locale/mr/LC_MESSAGES/fprintd.mo
* /usr/share/locale/ms/LC_MESSAGES/fprintd.mo
* /usr/share/locale/nb/LC_MESSAGES/fprintd.mo
* /usr/share/locale/nl/LC_MESSAGES/fprintd.mo
* /usr/share/locale/nn/LC_MESSAGES/fprintd.mo
* /usr/share/locale/oc/LC_MESSAGES/fprintd.mo
* /usr/share/locale/or/LC_MESSAGES/fprintd.mo
* /usr/share/locale/pa/LC_MESSAGES/fprintd.mo
* /usr/share/locale/pl/LC_MESSAGES/fprintd.mo
* /usr/share/locale/pt/LC_MESSAGES/fprintd.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/fprintd.mo
* /usr/share/locale/ro/LC_MESSAGES/fprintd.mo
* /usr/share/locale/ru/LC_MESSAGES/fprintd.mo
* /usr/share/locale/sk/LC_MESSAGES/fprintd.mo
* /usr/share/locale/sl/LC_MESSAGES/fprintd.mo
* /usr/share/locale/sq/LC_MESSAGES/fprintd.mo
* /usr/share/locale/sr/LC_MESSAGES/fprintd.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/fprintd.mo
* /usr/share/locale/sv/LC_MESSAGES/fprintd.mo
* /usr/share/locale/ta/LC_MESSAGES/fprintd.mo
* /usr/share/locale/te/LC_MESSAGES/fprintd.mo
* /usr/share/locale/th/LC_MESSAGES/fprintd.mo
* /usr/share/locale/tr/LC_MESSAGES/fprintd.mo
* /usr/share/locale/uk/LC_MESSAGES/fprintd.mo
* /usr/share/locale/vi/LC_MESSAGES/fprintd.mo
* /usr/share/locale/wa/LC_MESSAGES/fprintd.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/fprintd.mo
* /usr/share/locale/zh_HK/LC_MESSAGES/fprintd.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/fprintd.mo
* /usr/share/man/man1/fprintd.1.gz
* /usr/share/man/man8/pam_fprintd.8.gz
* /usr/share/polkit-1/actions/net.reactivated.fprint.device.policy
{{< /files >}}