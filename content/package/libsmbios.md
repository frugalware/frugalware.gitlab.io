+++
draft = false
title = "libsmbios 2.4.3-10"
version = "2.4.3-10"
description = "libsmbios is a library and set of tools that provide access to BIOS information."
date = "2024-11-03T15:22:40"
aliases = "/packages/219166"
categories = ['lib']
upstreamurl = "https://github.com/dell/libsmbios"
arch = "x86_64"
size = "193560"
usize = "1143513"
sha1sum = "22536e437f1d03cf7b20b983e3e0b5fc9dc3f54d"
depends = "['libstdc++>=9.1.0-3', 'python3>=3.13']"
reverse_depends = "['fwupd']"
license = "GPL"
+++
### Description: 
libsmbios is a library and set of tools that provide access to BIOS information.

### Files: 
* /etc/libsmbios/logging.conf
* /usr/bin/smbios-battery-ctl
* /usr/bin/smbios-get-ut-data
* /usr/bin/smbios-keyboard-ctl
* /usr/bin/smbios-lcd-brightness
* /usr/bin/smbios-passwd
* /usr/bin/smbios-state-byte-ctl
* /usr/bin/smbios-sys-info
* /usr/bin/smbios-sys-info-lite
* /usr/bin/smbios-thermal-ctl
* /usr/bin/smbios-token-ctl
* /usr/bin/smbios-upflag-ctl
* /usr/bin/smbios-wakeup-ctl
* /usr/bin/smbios-wireless-ctl
* /usr/include/Makefile.am
* /usr/include/smbios/dlopen.h
* /usr/include/smbios_c/cmos.h
* /usr/include/smbios_c/compat.h
* /usr/include/smbios_c/config/abi/msvc_prefix.h
* /usr/include/smbios_c/config/abi/msvc_suffix.h
* /usr/include/smbios_c/config/abi_prefix.h
* /usr/include/smbios_c/config/abi_suffix.h
* /usr/include/smbios_c/config/auto_link.h
* /usr/include/smbios_c/config/boost_LICENSE_1_0_txt
* /usr/include/smbios_c/config/compiler/gcc.h
* /usr/include/smbios_c/config/compiler/sunpro_cc.h
* /usr/include/smbios_c/config/compiler/visualc.h
* /usr/include/smbios_c/config/get_config.h
* /usr/include/smbios_c/config/platform/linux.h
* /usr/include/smbios_c/config/platform/win32.h
* /usr/include/smbios_c/config/platform/win64.h
* /usr/include/smbios_c/config/README
* /usr/include/smbios_c/config/select_compiler_config.h
* /usr/include/smbios_c/config/select_platform_config.h
* /usr/include/smbios_c/config/suffix.h
* /usr/include/smbios_c/config/user.h
* /usr/include/smbios_c/dlopen.h
* /usr/include/smbios_c/memory.h
* /usr/include/smbios_c/obj/cmos.h
* /usr/include/smbios_c/obj/memory.h
* /usr/include/smbios_c/obj/smbios.h
* /usr/include/smbios_c/obj/smi.h
* /usr/include/smbios_c/obj/token.h
* /usr/include/smbios_c/smbios.h
* /usr/include/smbios_c/smi.h
* /usr/include/smbios_c/system_info.h
* /usr/include/smbios_c/token.h
* /usr/include/smbios_c/types.h
* /usr/lib/libsmbios_c.so
* /usr/lib/libsmbios_c.so.2
* /usr/lib/libsmbios_c.so.2.2.1
* /usr/lib/pkgconfig/libsmbios_c.pc
* /usr/lib/python3.13/site-packages/libsmbios_c/cmos.py
* /usr/lib/python3.13/site-packages/libsmbios_c/memory.py
* /usr/lib/python3.13/site-packages/libsmbios_c/smbios.py
* /usr/lib/python3.13/site-packages/libsmbios_c/smbios_token.py
* /usr/lib/python3.13/site-packages/libsmbios_c/smi.py
* /usr/lib/python3.13/site-packages/libsmbios_c/system_info.py
* /usr/lib/python3.13/site-packages/libsmbios_c/trace_decorator.py
* /usr/lib/python3.13/site-packages/libsmbios_c/_common.py
* /usr/lib/python3.13/site-packages/libsmbios_c/_vars.py
* /usr/lib/python3.13/site-packages/libsmbios_c/__init__.py
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/cmos.cpython-313.opt-1.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/cmos.cpython-313.opt-2.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/cmos.cpython-313.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/memory.cpython-313.opt-1.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/memory.cpython-313.opt-2.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/memory.cpython-313.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/smbios.cpython-313.opt-1.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/smbios.cpython-313.opt-2.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/smbios.cpython-313.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/smbios_token.cpython-313.opt-1.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/smbios_token.cpython-313.opt-2.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/smbios_token.cpython-313.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/smi.cpython-313.opt-1.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/smi.cpython-313.opt-2.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/smi.cpython-313.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/system_info.cpython-313.opt-1.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/system_info.cpython-313.opt-2.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/system_info.cpython-313.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/trace_decorator.cpython-313.opt-1.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/trace_decorator.cpython-313.opt-2.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/trace_decorator.cpython-313.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/_common.cpython-313.opt-1.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/_common.cpython-313.opt-2.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/_common.cpython-313.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/_vars.cpython-313.opt-1.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/_vars.cpython-313.opt-2.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/_vars.cpython-313.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/__init__.cpython-313.opt-1.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/__init__.cpython-313.opt-2.pyc
* /usr/lib/python3.13/site-packages/libsmbios_c/__pycache__/__init__.cpython-313.pyc
* /usr/share/doc/libsmbios-2.4.3/COPYING
* /usr/share/doc/libsmbios-2.4.3/COPYING-GPL
* /usr/share/doc/libsmbios-2.4.3/COPYING-OSL
* /usr/share/doc/libsmbios-2.4.3/README.md
* /usr/share/locale/de/LC_MESSAGES/libsmbios.mo
* /usr/share/locale/en/LC_MESSAGES/libsmbios.mo
* /usr/share/locale/en@boldquot/LC_MESSAGES/libsmbios.mo
* /usr/share/locale/en@quot/LC_MESSAGES/libsmbios.mo
* /usr/share/locale/es/LC_MESSAGES/libsmbios.mo
* /usr/share/locale/fr/LC_MESSAGES/libsmbios.mo
* /usr/share/locale/it/LC_MESSAGES/libsmbios.mo
* /usr/share/locale/ja/LC_MESSAGES/libsmbios.mo
* /usr/share/locale/ko/LC_MESSAGES/libsmbios.mo
* /usr/share/locale/nl/LC_MESSAGES/libsmbios.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/libsmbios.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/libsmbios.mo
* /usr/share/man/man1/smbios-battery-ctl.1.gz
* /usr/share/man/man1/smbios-get-ut-data.1.gz
* /usr/share/man/man1/smbios-keyboard-ctl.1.gz
* /usr/share/man/man1/smbios-lcd-brightness.1.gz
* /usr/share/man/man1/smbios-passwd.1.gz
* /usr/share/man/man1/smbios-state-byte-ctl.1.gz
* /usr/share/man/man1/smbios-sys-info-lite.1.gz
* /usr/share/man/man1/smbios-sys-info.1.gz
* /usr/share/man/man1/smbios-thermal-ctl.1.gz
* /usr/share/man/man1/smbios-token-ctl.1.gz
* /usr/share/man/man1/smbios-upflag-ctl.1.gz
* /usr/share/man/man1/smbios-wakeup-ctl.1.gz
* /usr/share/man/man1/smbios-wireless-ctl.1.gz
* /usr/share/smbios-utils/cli.py
* /usr/share/smbios-utils/token_blacklist.csv
* /usr/share/smbios-utils/token_list.csv
* /usr/share/smbios-utils/__pycache__/cli.cpython-313.opt-1.pyc
* /usr/share/smbios-utils/__pycache__/cli.cpython-313.opt-2.pyc
* /usr/share/smbios-utils/__pycache__/cli.cpython-313.pyc
