+++
draft = false
title = "openrazer 3.8.0-24"
version = "3.8.0-24"
description = "An entirely open source driver and user-space daemon that allows you to manage your Razer peripherals on GNU/Linux."
date = "2024-08-30T11:04:16"
aliases = "/packages/220390"
categories = ['apps-extra']
upstreamurl = "https://github.com/openrazer/openrazer"
arch = "x86_64"
size = "280280"
usize = "2053401"
sha1sum = "31b49a2167f208beb96e6b856cbb19cae127b1b1"
depends = "['gtk+3', 'kernel=6.10.7-1', 'pygobject3', 'python3-daemonize', 'python3-notify2', 'python3-numpy', 'python3-setproctitle', 'pyudev', 'xautomation']"
reverse_depends = "['libopenrazer', 'polychromatic']"
+++
### Description: 
An entirely open source driver and user-space daemon that allows you to manage your Razer peripherals on GNU/Linux.

### Files: 
* /usr/bin/openrazer-daemon
* /usr/lib/modules/6.10.7-fw1/kernel/drivers/hid/razeraccessory.ko
* /usr/lib/modules/6.10.7-fw1/kernel/drivers/hid/razerkbd.ko
* /usr/lib/modules/6.10.7-fw1/kernel/drivers/hid/razerkraken.ko
* /usr/lib/modules/6.10.7-fw1/kernel/drivers/hid/razermouse.ko
* /usr/lib/python3.12/site-packages/openrazer-3.8.0-py3.12.egg-info/dependency_links.txt
* /usr/lib/python3.12/site-packages/openrazer-3.8.0-py3.12.egg-info/PKG-INFO
* /usr/lib/python3.12/site-packages/openrazer-3.8.0-py3.12.egg-info/requires.txt
* /usr/lib/python3.12/site-packages/openrazer-3.8.0-py3.12.egg-info/SOURCES.txt
* /usr/lib/python3.12/site-packages/openrazer-3.8.0-py3.12.egg-info/top_level.txt
* /usr/lib/python3.12/site-packages/openrazer/client/constants.py
* /usr/lib/python3.12/site-packages/openrazer/client/debug.py
* /usr/lib/python3.12/site-packages/openrazer/client/device.py
* /usr/lib/python3.12/site-packages/openrazer/client/devices/keyboard.py
* /usr/lib/python3.12/site-packages/openrazer/client/devices/mice.py
* /usr/lib/python3.12/site-packages/openrazer/client/devices/mousemat.py
* /usr/lib/python3.12/site-packages/openrazer/client/devices/__init__.py
* /usr/lib/python3.12/site-packages/openrazer/client/devices/__pycache__/keyboard.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer/client/devices/__pycache__/mice.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer/client/devices/__pycache__/mousemat.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer/client/devices/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer/client/fx.py
* /usr/lib/python3.12/site-packages/openrazer/client/macro.py
* /usr/lib/python3.12/site-packages/openrazer/client/__init__.py
* /usr/lib/python3.12/site-packages/openrazer/client/__pycache__/constants.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer/client/__pycache__/debug.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer/client/__pycache__/device.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer/client/__pycache__/fx.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer/client/__pycache__/macro.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer/client/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer/__init__.py
* /usr/lib/python3.12/site-packages/openrazer/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon-3.8.0-py3.12.egg-info/dependency_links.txt
* /usr/lib/python3.12/site-packages/openrazer_daemon-3.8.0-py3.12.egg-info/PKG-INFO
* /usr/lib/python3.12/site-packages/openrazer_daemon-3.8.0-py3.12.egg-info/requires.txt
* /usr/lib/python3.12/site-packages/openrazer_daemon-3.8.0-py3.12.egg-info/SOURCES.txt
* /usr/lib/python3.12/site-packages/openrazer_daemon-3.8.0-py3.12.egg-info/top_level.txt
* /usr/lib/python3.12/site-packages/openrazer_daemon/daemon.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/accessory.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/all.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/argb_controller.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/bw2013.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/charging_pad_chroma.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/chroma_keyboard.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/deathadder_chroma.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/keypad.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/kraken.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/lanceheadte.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/macro.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/mamba.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/mouse_scroll_wheel.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/nagahex.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/nagahexv2.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/__init__.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/__pycache__/accessory.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/__pycache__/all.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/__pycache__/argb_controller.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/__pycache__/bw2013.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/__pycache__/charging_pad_chroma.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/__pycache__/chroma_keyboard.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/__pycache__/deathadder_chroma.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/__pycache__/keypad.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/__pycache__/kraken.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/__pycache__/lanceheadte.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/__pycache__/macro.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/__pycache__/mamba.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/__pycache__/mouse_scroll_wheel.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/__pycache__/nagahex.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/__pycache__/nagahexv2.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/dbus_methods/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/service.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/__init__.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/__pycache__/service.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/dbus_services/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/device.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/hardware/accessory.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/hardware/core.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/hardware/device_base.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/hardware/headsets.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/hardware/keyboards.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/hardware/monitor.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/hardware/mouse.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/hardware/mouse_mat.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/hardware/__init__.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/hardware/__pycache__/accessory.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/hardware/__pycache__/core.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/hardware/__pycache__/device_base.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/hardware/__pycache__/headsets.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/hardware/__pycache__/keyboards.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/hardware/__pycache__/monitor.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/hardware/__pycache__/mouse.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/hardware/__pycache__/mouse_mat.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/hardware/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/keyboard.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/misc/autosave_persistence.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/misc/battery_notifier.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/misc/effect_sync.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/misc/key_event_management.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/misc/macro.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/misc/ripple_effect.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/misc/screensaver_monitor.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/misc/__init__.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/misc/__pycache__/autosave_persistence.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/misc/__pycache__/battery_notifier.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/misc/__pycache__/effect_sync.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/misc/__pycache__/key_event_management.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/misc/__pycache__/macro.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/misc/__pycache__/ripple_effect.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/misc/__pycache__/screensaver_monitor.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/misc/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/__init__.py
* /usr/lib/python3.12/site-packages/openrazer_daemon/__pycache__/daemon.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/__pycache__/device.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/__pycache__/keyboard.cpython-312.pyc
* /usr/lib/python3.12/site-packages/openrazer_daemon/__pycache__/__init__.cpython-312.pyc
* /usr/lib/systemd/user/openrazer-daemon.service
* /usr/lib/udev/razer_mount
* /usr/lib/udev/rules.d/99-razer.rules
* /usr/share/dbus-1/services/org.razer.service
* /usr/share/doc/openrazer-3.8.0/README.md
* /usr/share/man/man5/razer.conf.5.gz
* /usr/share/man/man8/openrazer-daemon.8.gz
* /usr/share/openrazer/razer.conf.example
