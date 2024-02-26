+++
draft = false
title = "gyp 20220912.g9d09418-3"
version = "20220912.g9d09418-3"
description = "GYP can Generate Your Projects."
date = "2023-10-11T18:27:58"
aliases = "/packages/219979"
categories = ['devel-extra']
upstreamurl = "https://chromium.googlesource.com/external/gyp"
arch = "x86_64"
size = "536508"
usize = "2270861"
sha1sum = "9207dacca363f86cd0e50f8eb9f536abb8fce804"
depends = "['ninja']"
+++
GYP can Generate Your Projects.

{{< files text="show files" >}}* /usr/bin/gyp
* /usr/lib/python3.12/site-packages/gyp-0.1-py3.12.egg-info/dependency_links.txt
* /usr/lib/python3.12/site-packages/gyp-0.1-py3.12.egg-info/entry_points.txt
* /usr/lib/python3.12/site-packages/gyp-0.1-py3.12.egg-info/PKG-INFO
* /usr/lib/python3.12/site-packages/gyp-0.1-py3.12.egg-info/SOURCES.txt
* /usr/lib/python3.12/site-packages/gyp-0.1-py3.12.egg-info/top_level.txt
* /usr/lib/python3.12/site-packages/gyp/common.py
* /usr/lib/python3.12/site-packages/gyp/common_test.py
* /usr/lib/python3.12/site-packages/gyp/easy_xml.py
* /usr/lib/python3.12/site-packages/gyp/easy_xml_test.py
* /usr/lib/python3.12/site-packages/gyp/flock_tool.py
* /usr/lib/python3.12/site-packages/gyp/generator/analyzer.py
* /usr/lib/python3.12/site-packages/gyp/generator/cmake.py
* /usr/lib/python3.12/site-packages/gyp/generator/dump_dependency_json.py
* /usr/lib/python3.12/site-packages/gyp/generator/eclipse.py
* /usr/lib/python3.12/site-packages/gyp/generator/gypd.py
* /usr/lib/python3.12/site-packages/gyp/generator/gypsh.py
* /usr/lib/python3.12/site-packages/gyp/generator/make.py
* /usr/lib/python3.12/site-packages/gyp/generator/msvs.py
* /usr/lib/python3.12/site-packages/gyp/generator/msvs_test.py
* /usr/lib/python3.12/site-packages/gyp/generator/ninja.py
* /usr/lib/python3.12/site-packages/gyp/generator/ninja_test.py
* /usr/lib/python3.12/site-packages/gyp/generator/xcode.py
* /usr/lib/python3.12/site-packages/gyp/generator/xcode_test.py
* /usr/lib/python3.12/site-packages/gyp/generator/__init__.py
* /usr/lib/python3.12/site-packages/gyp/generator/__pycache__/analyzer.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/generator/__pycache__/cmake.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/generator/__pycache__/dump_dependency_json.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/generator/__pycache__/eclipse.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/generator/__pycache__/gypd.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/generator/__pycache__/gypsh.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/generator/__pycache__/make.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/generator/__pycache__/msvs.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/generator/__pycache__/msvs_test.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/generator/__pycache__/ninja.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/generator/__pycache__/ninja_test.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/generator/__pycache__/xcode.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/generator/__pycache__/xcode_test.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/generator/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/input.py
* /usr/lib/python3.12/site-packages/gyp/input_test.py
* /usr/lib/python3.12/site-packages/gyp/mac_tool.py
* /usr/lib/python3.12/site-packages/gyp/MSVSNew.py
* /usr/lib/python3.12/site-packages/gyp/MSVSProject.py
* /usr/lib/python3.12/site-packages/gyp/MSVSSettings.py
* /usr/lib/python3.12/site-packages/gyp/MSVSSettings_test.py
* /usr/lib/python3.12/site-packages/gyp/MSVSToolFile.py
* /usr/lib/python3.12/site-packages/gyp/MSVSUserFile.py
* /usr/lib/python3.12/site-packages/gyp/MSVSUtil.py
* /usr/lib/python3.12/site-packages/gyp/MSVSVersion.py
* /usr/lib/python3.12/site-packages/gyp/msvs_emulation.py
* /usr/lib/python3.12/site-packages/gyp/ninja_syntax.py
* /usr/lib/python3.12/site-packages/gyp/simple_copy.py
* /usr/lib/python3.12/site-packages/gyp/win_tool.py
* /usr/lib/python3.12/site-packages/gyp/xcodeproj_file.py
* /usr/lib/python3.12/site-packages/gyp/xcode_emulation.py
* /usr/lib/python3.12/site-packages/gyp/xcode_ninja.py
* /usr/lib/python3.12/site-packages/gyp/xml_fix.py
* /usr/lib/python3.12/site-packages/gyp/__init__.py
* /usr/lib/python3.12/site-packages/gyp/__pycache__/common.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/common_test.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/easy_xml.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/easy_xml_test.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/flock_tool.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/input.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/input_test.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/mac_tool.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/MSVSNew.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/MSVSProject.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/MSVSSettings.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/MSVSSettings_test.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/MSVSToolFile.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/MSVSUserFile.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/MSVSUtil.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/MSVSVersion.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/msvs_emulation.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/ninja_syntax.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/simple_copy.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/win_tool.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/xcodeproj_file.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/xcode_emulation.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/xcode_ninja.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/xml_fix.cpython-312.pyc
* /usr/lib/python3.12/site-packages/gyp/__pycache__/__init__.cpython-312.pyc
* /usr/share/doc/gyp-20220912.g9d09418/AUTHORS
* /usr/share/doc/gyp-20220912.g9d09418/LICENSE
* /usr/share/doc/gyp-20220912.g9d09418/README.md
{{< /files >}}