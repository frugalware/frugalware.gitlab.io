+++
draft = false
title = "intel-graphics-compiler 2.14.1-1"
version = "2.14.1-1"
description = "Intel Graphics Compiler for OpenCL"
date = "2025-07-08T07:38:29"
aliases = "/packages/220084"
categories = ['devel']
upstreamurl = "https://github.com/intel/intel-graphics-compiler"
arch = "x86_64"
size = "56597676"
usize = "213388893"
sha1sum = "0150dcef939554643441adb575021645b1d9127a"
depends = "['libxml2>=2.14.3']"
reverse_depends = "['intel-compute-runtime']"
+++
### Description: 
Intel Graphics Compiler for OpenCL

### Files: 
* /usr/bin/iga64
* /usr/include/iga/iga.h
* /usr/include/iga/iga.hpp
* /usr/include/iga/igad.h
* /usr/include/iga/igaEncoderWrapper.hpp
* /usr/include/iga/igax.hpp
* /usr/include/iga/iga_bxml_enums.hpp
* /usr/include/iga/iga_bxml_ops.hpp
* /usr/include/iga/iga_types_ext.hpp
* /usr/include/iga/iga_types_swsb.hpp
* /usr/include/iga/kv.h
* /usr/include/iga/kv.hpp
* /usr/include/igc/cif/cif/builtins/builtins_registry.cpp
* /usr/include/igc/cif/cif/builtins/builtins_registry.h
* /usr/include/igc/cif/cif/builtins/memory/buffer/buffer.h
* /usr/include/igc/cif/cif/builtins/memory/buffer/impl/buffer_impl.cpp
* /usr/include/igc/cif/cif/builtins/memory/buffer/impl/buffer_impl.h
* /usr/include/igc/cif/cif/CMakeLists.txt
* /usr/include/igc/cif/cif/common/cif.h
* /usr/include/igc/cif/cif/common/cif_main.h
* /usr/include/igc/cif/cif/common/coder.h
* /usr/include/igc/cif/cif/common/compatibility.h
* /usr/include/igc/cif/cif/common/id.h
* /usr/include/igc/cif/cif/common/library_api.h
* /usr/include/igc/cif/cif/common/library_handle.h
* /usr/include/igc/cif/cif/export/build/binary_version.h
* /usr/include/igc/cif/cif/export/cif_impl.h
* /usr/include/igc/cif/cif/export/cif_main.cpp
* /usr/include/igc/cif/cif/export/cif_main_impl.h
* /usr/include/igc/cif/cif/export/interface_creator.h
* /usr/include/igc/cif/cif/export/library_api.h
* /usr/include/igc/cif/cif/export/muiltiversion.h
* /usr/include/igc/cif/cif/export/pimpl_base.h
* /usr/include/igc/cif/cif/export/registry.cpp
* /usr/include/igc/cif/cif/export/registry.h
* /usr/include/igc/cif/cif/helpers/error.h
* /usr/include/igc/cif/cif/helpers/memory.h
* /usr/include/igc/cif/cif/import/cif_main.cpp
* /usr/include/igc/cif/cif/import/cif_main.h
* /usr/include/igc/cif/cif/import/library_api.h
* /usr/include/igc/cif/cif/macros/disable.h
* /usr/include/igc/cif/cif/macros/enable.h
* /usr/include/igc/cif/cif/os/lin/lin_library_handle.cpp
* /usr/include/igc/cif/cif/os/lin/lin_library_handle.h
* /usr/include/igc/cif/cif/os/win/win_library_handle.cpp
* /usr/include/igc/cif/cif/os/win/win_library_handle.h
* /usr/include/igc/cif/CMakeLists.txt
* /usr/include/igc/cif/readme.txt
* /usr/include/igc/common/StateSaveAreaHeader.h
* /usr/include/igc/igc.opencl.h
* /usr/include/igc/OCLAPI/oclapi.h
* /usr/include/igc/ocl_igc_interface/code_type.h
* /usr/include/igc/ocl_igc_interface/fcl_ocl_device_ctx.h
* /usr/include/igc/ocl_igc_interface/fcl_ocl_translation_ctx.h
* /usr/include/igc/ocl_igc_interface/gt_system_info.h
* /usr/include/igc/ocl_igc_interface/igc_builtins.h
* /usr/include/igc/ocl_igc_interface/igc_features_and_workarounds.h
* /usr/include/igc/ocl_igc_interface/igc_ocl_device_ctx.h
* /usr/include/igc/ocl_igc_interface/igc_ocl_translation_ctx.h
* /usr/include/igc/ocl_igc_interface/impl/fcl_ocl_device_ctx_impl.cpp
* /usr/include/igc/ocl_igc_interface/impl/fcl_ocl_device_ctx_impl.h
* /usr/include/igc/ocl_igc_interface/impl/fcl_ocl_translation_ctx_impl.cpp
* /usr/include/igc/ocl_igc_interface/impl/fcl_ocl_translation_ctx_impl.h
* /usr/include/igc/ocl_igc_interface/impl/gt_system_info_impl.cpp
* /usr/include/igc/ocl_igc_interface/impl/gt_system_info_impl.h
* /usr/include/igc/ocl_igc_interface/impl/igc_builtins_impl.cpp
* /usr/include/igc/ocl_igc_interface/impl/igc_builtins_impl.h
* /usr/include/igc/ocl_igc_interface/impl/igc_features_and_workarounds_impl.cpp
* /usr/include/igc/ocl_igc_interface/impl/igc_features_and_workarounds_impl.h
* /usr/include/igc/ocl_igc_interface/impl/igc_ocl_device_ctx_impl.cpp
* /usr/include/igc/ocl_igc_interface/impl/igc_ocl_device_ctx_impl.h
* /usr/include/igc/ocl_igc_interface/impl/igc_ocl_translation_ctx_impl.cpp
* /usr/include/igc/ocl_igc_interface/impl/igc_ocl_translation_ctx_impl.h
* /usr/include/igc/ocl_igc_interface/impl/igc_signal_guard.h
* /usr/include/igc/ocl_igc_interface/impl/ocl_gen_binary_impl.cpp
* /usr/include/igc/ocl_igc_interface/impl/ocl_gen_binary_impl.h
* /usr/include/igc/ocl_igc_interface/impl/ocl_translation_output_impl.cpp
* /usr/include/igc/ocl_igc_interface/impl/ocl_translation_output_impl.h
* /usr/include/igc/ocl_igc_interface/impl/platform_impl.cpp
* /usr/include/igc/ocl_igc_interface/impl/platform_impl.h
* /usr/include/igc/ocl_igc_interface/impl/version_in.h
* /usr/include/igc/ocl_igc_interface/ocl_gen_binary.h
* /usr/include/igc/ocl_igc_interface/ocl_translation_output.h
* /usr/include/igc/ocl_igc_interface/platform.h
* /usr/include/igc/ocl_igc_interface/platform_helper.h
* /usr/include/igc/ocl_igc_shared/device_enqueue/DeviceEnqueueInternalTypes.h
* /usr/include/igc/ocl_igc_shared/executable_format/patch_g10.h
* /usr/include/igc/ocl_igc_shared/executable_format/patch_g7.h
* /usr/include/igc/ocl_igc_shared/executable_format/patch_g8.h
* /usr/include/igc/ocl_igc_shared/executable_format/patch_g9.h
* /usr/include/igc/ocl_igc_shared/executable_format/patch_list.h
* /usr/include/igc/ocl_igc_shared/executable_format/patch_shared.h
* /usr/include/igc/ocl_igc_shared/executable_format/program_debug_data.h
* /usr/include/igc/ocl_igc_shared/gtpin/gtpin_driver_common.h
* /usr/include/igc/ocl_igc_shared/gtpin/gtpin_driver_common_bti.h
* /usr/include/igc/ocl_igc_shared/gtpin/gtpin_ocl_interface.h
* /usr/include/igc/ocl_igc_shared/indirect_access_detection/version.h
* /usr/include/igc/ocl_igc_shared/raytracing/constants.h
* /usr/include/igc/ocl_igc_shared/raytracing/ocl_raytracing_structures.h
* /usr/include/opencl-c-base.h
* /usr/include/opencl-c.h
* /usr/include/visa/RelocationInfo.h
* /usr/lib/igc2/NOTICES.txt
* /usr/lib/libiga64.so.2
* /usr/lib/libiga64.so.2.14.0+0
* /usr/lib/libigc.so.2
* /usr/lib/libigc.so.2.14.0+0
* /usr/lib/libigdfcl.so.2
* /usr/lib/libigdfcl.so.2.14.0+0
* /usr/lib/libopencl-clang.so.15
* /usr/lib/pkgconfig/igc-opencl.pc
* /usr/share/doc/intel-graphics-compiler-2.14.1/CHANGES
* /usr/share/doc/intel-graphics-compiler-2.14.1/LICENSE
* /usr/share/doc/intel-graphics-compiler-2.14.1/README.md
* /usr/share/doc/intel-graphics-compiler-2.14.1/Readme.md
