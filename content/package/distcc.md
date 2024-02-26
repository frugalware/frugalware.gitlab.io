+++
draft = false
title = "distcc 3.4-6"
version = "3.4-6"
description = "A distributed C, C++, Obj C compiler"
date = "2024-01-10T19:37:36"
aliases = "/packages/4212"
categories = ['devel-extra']
upstreamurl = "https://github.com/distcc/distcc"
arch = "x86_64"
size = "484444"
usize = "1954344"
sha1sum = "9a698bae19f457b2c9b8e3ac7b6c96cfeb63d1a1"
depends = "['lzo', 'popt>=1.14-2', 'python3>=3.10', 'shadow>=4.1.2.1-2']"
reverse_depends = "['distcc-gui']"
+++
A distributed C, C++, Obj C compiler{{< spoiler text="show files" >}}* /etc/default/distcc
* /etc/distcc/clients.allow
* /etc/distcc/commands.allow.sh
* /etc/distcc/hosts
* /etc/sysconfig/distccd
* /usr/bin/distcc
* /usr/bin/distccd
* /usr/bin/distccmon-text
* /usr/bin/lsdistcc
* /usr/bin/pump
* /usr/bin/update-distcc-symlinks
* /usr/lib/distcc/bin/c++
* /usr/lib/distcc/bin/cc
* /usr/lib/distcc/bin/clang
* /usr/lib/distcc/bin/clang++
* /usr/lib/distcc/bin/g++
* /usr/lib/distcc/bin/gcc
* /usr/lib/distcc/bin/x86_64-frugalware-linux-c++
* /usr/lib/distcc/bin/x86_64-frugalware-linux-cc
* /usr/lib/distcc/bin/x86_64-frugalware-linux-clang
* /usr/lib/distcc/bin/x86_64-frugalware-linux-clang++
* /usr/lib/distcc/bin/x86_64-frugalware-linux-g++
* /usr/lib/distcc/bin/x86_64-frugalware-linux-gcc
* /usr/lib/distcc/bin/x86_64-frugalware-linux-wrapper
* /usr/lib/python3.12/site-packages/include_server-3.4-py3.12.egg-info/dependency_links.txt
* /usr/lib/python3.12/site-packages/include_server-3.4-py3.12.egg-info/PKG-INFO
* /usr/lib/python3.12/site-packages/include_server-3.4-py3.12.egg-info/SOURCES.txt
* /usr/lib/python3.12/site-packages/include_server-3.4-py3.12.egg-info/top_level.txt
* /usr/lib/python3.12/site-packages/include_server/basics.py
* /usr/lib/python3.12/site-packages/include_server/basics_test.py
* /usr/lib/python3.12/site-packages/include_server/cache_basics.py
* /usr/lib/python3.12/site-packages/include_server/compiler_defaults.py
* /usr/lib/python3.12/site-packages/include_server/compress_files.py
* /usr/lib/python3.12/site-packages/include_server/c_extensions_test.py
* /usr/lib/python3.12/site-packages/include_server/distcc_pump_c_extensions.cpython-312-x86_64-linux-gnu.so
* /usr/lib/python3.12/site-packages/include_server/include_analyzer.py
* /usr/lib/python3.12/site-packages/include_server/include_analyzer_memoizing_node.py
* /usr/lib/python3.12/site-packages/include_server/include_analyzer_memoizing_node_test.py
* /usr/lib/python3.12/site-packages/include_server/include_analyzer_test.py
* /usr/lib/python3.12/site-packages/include_server/include_server.py
* /usr/lib/python3.12/site-packages/include_server/include_server_test.py
* /usr/lib/python3.12/site-packages/include_server/macro_eval.py
* /usr/lib/python3.12/site-packages/include_server/macro_eval_test.py
* /usr/lib/python3.12/site-packages/include_server/mirror_path.py
* /usr/lib/python3.12/site-packages/include_server/mirror_path_test.py
* /usr/lib/python3.12/site-packages/include_server/parse_command.py
* /usr/lib/python3.12/site-packages/include_server/parse_command_test.py
* /usr/lib/python3.12/site-packages/include_server/parse_file.py
* /usr/lib/python3.12/site-packages/include_server/parse_file_test.py
* /usr/lib/python3.12/site-packages/include_server/run.py
* /usr/lib/python3.12/site-packages/include_server/setup.py
* /usr/lib/python3.12/site-packages/include_server/statistics.py
* /usr/lib/python3.12/site-packages/include_server/__pycache__/basics.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/basics_test.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/cache_basics.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/compiler_defaults.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/compress_files.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/c_extensions_test.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/include_analyzer.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/include_analyzer_memoizing_node.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/include_analyzer_memoizing_node_test.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/include_analyzer_test.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/include_server.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/include_server_test.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/macro_eval.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/macro_eval_test.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/mirror_path.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/mirror_path_test.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/parse_command.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/parse_command_test.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/parse_file.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/parse_file_test.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/run.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/setup.cpython-312.pyc
* /usr/lib/python3.12/site-packages/include_server/__pycache__/statistics.cpython-312.pyc
* /usr/lib/systemd/system/distccd.service
* /usr/share/doc/distcc-3.4/AUTHORS
* /usr/share/doc/distcc-3.4/ChangeLog
* /usr/share/doc/distcc-3.4/COPYING
* /usr/share/doc/distcc-3.4/example/default
* /usr/share/doc/distcc-3.4/example/hosts.allow
* /usr/share/doc/distcc-3.4/example/init
* /usr/share/doc/distcc-3.4/example/init-suse
* /usr/share/doc/distcc-3.4/example/logrotate
* /usr/share/doc/distcc-3.4/example/README
* /usr/share/doc/distcc-3.4/example/services
* /usr/share/doc/distcc-3.4/example/xinetd
* /usr/share/doc/distcc-3.4/INSTALL
* /usr/share/doc/distcc-3.4/NEWS
* /usr/share/doc/distcc-3.4/protocol-1.txt
* /usr/share/doc/distcc-3.4/protocol-2.txt
* /usr/share/doc/distcc-3.4/protocol-3-impl.txt
* /usr/share/doc/distcc-3.4/protocol-3.txt
* /usr/share/doc/distcc-3.4/protocol-gssapi.txt
* /usr/share/doc/distcc-3.4/README
* /usr/share/doc/distcc-3.4/README.md
* /usr/share/doc/distcc-3.4/README.packaging
* /usr/share/doc/distcc-3.4/README.pump
* /usr/share/doc/distcc-3.4/reporting-bugs.txt
* /usr/share/doc/distcc-3.4/status-1.txt
* /usr/share/doc/distcc-3.4/survey.txt
* /usr/share/doc/distcc-3.4/TODO
* /usr/share/man/man1/distcc.1.gz
* /usr/share/man/man1/distccd.1.gz
* /usr/share/man/man1/distccmon-text.1.gz
* /usr/share/man/man1/include_server.1.gz
* /usr/share/man/man1/lsdistcc.1.gz
* /usr/share/man/man1/pump.1.gz
{{< /spoiler >}}