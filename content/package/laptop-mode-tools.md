+++
draft = false
title = "laptop-mode-tools 1.74-3"
version = "1.74-3"
description = "A kernel mode that allows you to extend the battery life of your laptop"
date = "2024-12-17T16:24:34"
aliases = "/packages/136012"
categories = ['apps-extra']
upstreamurl = "https://github.com/rickysarraf/laptop-mode-tools"
arch = "x86_64"
size = "77564"
usize = "264376"
sha1sum = "722527d50035887b9cb21b799e933489b3f64ab9"
depends = "['acpid', 'hdparm']"
+++
### Description: 
A kernel mode that allows you to extend the battery life of your laptop

### Files: 
* /etc/acpi/actions/lm_ac_adapter.sh
* /etc/acpi/actions/lm_battery.sh
* /etc/acpi/actions/lm_lid.sh
* /etc/acpi/events/lm_ac_adapter
* /etc/acpi/events/lm_battery
* /etc/acpi/events/lm_lid
* /etc/laptop-mode/conf.d/ac97-powersave.conf
* /etc/laptop-mode/conf.d/auto-hibernate.conf
* /etc/laptop-mode/conf.d/battery-level-polling.conf
* /etc/laptop-mode/conf.d/bluetooth.conf
* /etc/laptop-mode/conf.d/board-specific/README.Board-Specific
* /etc/laptop-mode/conf.d/configuration-file-control.conf
* /etc/laptop-mode/conf.d/cpufreq.conf
* /etc/laptop-mode/conf.d/cpuhotplug.conf
* /etc/laptop-mode/conf.d/dpms-standby.conf
* /etc/laptop-mode/conf.d/eee-superhe.conf
* /etc/laptop-mode/conf.d/ethernet.conf
* /etc/laptop-mode/conf.d/exec-commands.conf
* /etc/laptop-mode/conf.d/hal-polling.conf
* /etc/laptop-mode/conf.d/intel-hda-powersave.conf
* /etc/laptop-mode/conf.d/intel-sata-powermgmt.conf
* /etc/laptop-mode/conf.d/intel_pstate.conf
* /etc/laptop-mode/conf.d/kbd-backlight.conf
* /etc/laptop-mode/conf.d/lcd-brightness.conf
* /etc/laptop-mode/conf.d/nmi-watchdog.conf
* /etc/laptop-mode/conf.d/nouveau.conf
* /etc/laptop-mode/conf.d/pcie-aspm.conf
* /etc/laptop-mode/conf.d/radeon-dpm.conf
* /etc/laptop-mode/conf.d/runtime-pm.conf
* /etc/laptop-mode/conf.d/sched-mc-power-savings.conf
* /etc/laptop-mode/conf.d/sched-smt-power-savings.conf
* /etc/laptop-mode/conf.d/start-stop-programs.conf
* /etc/laptop-mode/conf.d/terminal-blanking.conf
* /etc/laptop-mode/conf.d/vgaswitcheroo.conf
* /etc/laptop-mode/conf.d/video-out.conf
* /etc/laptop-mode/conf.d/wireless-ipw-power.conf
* /etc/laptop-mode/conf.d/wireless-iwl-power.conf
* /etc/laptop-mode/conf.d/wireless-power.conf
* /etc/laptop-mode/laptop-mode.conf
* /etc/laptop-mode/lm-profiler.conf
* /usr/bin/laptop_mode
* /usr/bin/lm-profiler
* /usr/bin/lm-syslog-setup
* /usr/bin/lmt-config-gui
* /usr/bin/lmt-config-gui-pkexec
* /usr/lib/pm-utils/sleep.d/01laptop-mode
* /usr/lib/systemd/system/laptop-mode.service
* /usr/lib/systemd/system/laptop-mode.timer
* /usr/lib/systemd/system/lmt-poll.service
* /usr/lib/tmpfiles.d/laptop-mode.conf
* /usr/lib/udev/lmt-udev
* /usr/lib/udev/rules.d/99-laptop-mode.rules
* /usr/share/applications/laptop-mode-tools.desktop
* /usr/share/doc/laptop-mode-tools-1.74/COPYING
* /usr/share/doc/laptop-mode-tools-1.74/README.Board-Specific
* /usr/share/doc/laptop-mode-tools-1.74/README.md
* /usr/share/laptop-mode-tools/lmt.py
* /usr/share/laptop-mode-tools/module-helpers/lm-polling-daemon
* /usr/share/laptop-mode-tools/module-helpers/pm-freeze
* /usr/share/laptop-mode-tools/module-helpers/pm-helper
* /usr/share/laptop-mode-tools/module-helpers/pm-hibernate
* /usr/share/laptop-mode-tools/module-helpers/pm-suspend
* /usr/share/laptop-mode-tools/modules/ac97-powersave
* /usr/share/laptop-mode-tools/modules/battery-level-polling
* /usr/share/laptop-mode-tools/modules/bluetooth
* /usr/share/laptop-mode-tools/modules/configuration-file-control
* /usr/share/laptop-mode-tools/modules/cpufreq
* /usr/share/laptop-mode-tools/modules/cpuhotplug
* /usr/share/laptop-mode-tools/modules/dpms-standby
* /usr/share/laptop-mode-tools/modules/eee-superhe
* /usr/share/laptop-mode-tools/modules/ethernet
* /usr/share/laptop-mode-tools/modules/exec-commands
* /usr/share/laptop-mode-tools/modules/hal-polling
* /usr/share/laptop-mode-tools/modules/hdparm
* /usr/share/laptop-mode-tools/modules/intel-hda-powersave
* /usr/share/laptop-mode-tools/modules/intel-sata-powermgmt
* /usr/share/laptop-mode-tools/modules/intel_pstate
* /usr/share/laptop-mode-tools/modules/kbd-backlight
* /usr/share/laptop-mode-tools/modules/laptop-mode
* /usr/share/laptop-mode-tools/modules/lcd-brightness
* /usr/share/laptop-mode-tools/modules/nmi-watchdog
* /usr/share/laptop-mode-tools/modules/nouveau
* /usr/share/laptop-mode-tools/modules/pcie-aspm
* /usr/share/laptop-mode-tools/modules/radeon-dpm
* /usr/share/laptop-mode-tools/modules/runtime-pm
* /usr/share/laptop-mode-tools/modules/sched-mc-power-savings
* /usr/share/laptop-mode-tools/modules/sched-smt-power-savings
* /usr/share/laptop-mode-tools/modules/start-stop-programs
* /usr/share/laptop-mode-tools/modules/syslog-conf
* /usr/share/laptop-mode-tools/modules/terminal-blanking
* /usr/share/laptop-mode-tools/modules/vgaswitcheroo
* /usr/share/laptop-mode-tools/modules/video-out
* /usr/share/laptop-mode-tools/modules/wireless-ipw-power
* /usr/share/laptop-mode-tools/modules/wireless-iwl-power
* /usr/share/laptop-mode-tools/modules/wireless-power
* /usr/share/man/man8/laptop-mode.conf.8.gz
* /usr/share/man/man8/laptop_mode.8.gz
* /usr/share/man/man8/lm-profiler.8.gz
* /usr/share/man/man8/lm-profiler.conf.8.gz
* /usr/share/man/man8/lm-syslog-setup.8.gz
* /usr/share/pixmaps/laptop-mode-tools.svg
* /usr/share/polkit-1/actions/org.linux.lmt.gui.policy
