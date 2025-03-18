+++
draft = false
title = "hip-runtime-amd 6.3.3-1"
version = "6.3.3-1"
description = "Heterogeneous Interface for Portability ROCm"
date = "2025-03-18T15:57:49"
aliases = "/packages/221255"
categories = ['devel-extra']
upstreamurl = "https://rocm.docs.amd.com/projects/HIP/en/latest/"
arch = "x86_64"
size = "9321576"
usize = "27850417"
sha1sum = "5986cb2d2a8850642c918a926ac9b367b0c535c8"
depends = "['comgr', 'libglvnd', 'rocm-core', 'rocminfo', 'rocprofiler-register']"
reverse_depends = "['roctracer']"
+++
### Description: 
Heterogeneous Interface for Portability ROCm

### Files: 
* /opt/rocm/bin/hipcc
* /opt/rocm/bin/hipcc.pl
* /opt/rocm/bin/hipcc_cmake_linker_helper
* /opt/rocm/bin/hipconfig
* /opt/rocm/bin/hipconfig.pl
* /opt/rocm/bin/hipdemangleatp
* /opt/rocm/bin/hipvars.pm
* /opt/rocm/bin/roc-obj
* /opt/rocm/bin/roc-obj-extract
* /opt/rocm/bin/roc-obj-extract.bat
* /opt/rocm/bin/roc-obj-ls
* /opt/rocm/bin/roc-obj-ls.bat
* /opt/rocm/include/hip/amd_detail/amd_channel_descriptor.h
* /opt/rocm/include/hip/amd_detail/amd_device_functions.h
* /opt/rocm/include/hip/amd_detail/amd_hip_atomic.h
* /opt/rocm/include/hip/amd_detail/amd_hip_bf16.h
* /opt/rocm/include/hip/amd_detail/amd_hip_bfloat16.h
* /opt/rocm/include/hip/amd_detail/amd_hip_common.h
* /opt/rocm/include/hip/amd_detail/amd_hip_complex.h
* /opt/rocm/include/hip/amd_detail/amd_hip_cooperative_groups.h
* /opt/rocm/include/hip/amd_detail/amd_hip_fp16.h
* /opt/rocm/include/hip/amd_detail/amd_hip_fp8.h
* /opt/rocm/include/hip/amd_detail/amd_hip_gl_interop.h
* /opt/rocm/include/hip/amd_detail/amd_hip_math_constants.h
* /opt/rocm/include/hip/amd_detail/amd_hip_runtime.h
* /opt/rocm/include/hip/amd_detail/amd_hip_runtime_pt_api.h
* /opt/rocm/include/hip/amd_detail/amd_hip_unsafe_atomics.h
* /opt/rocm/include/hip/amd_detail/amd_hip_vector_types.h
* /opt/rocm/include/hip/amd_detail/amd_math_functions.h
* /opt/rocm/include/hip/amd_detail/amd_surface_functions.h
* /opt/rocm/include/hip/amd_detail/amd_warp_functions.h
* /opt/rocm/include/hip/amd_detail/amd_warp_sync_functions.h
* /opt/rocm/include/hip/amd_detail/concepts.hpp
* /opt/rocm/include/hip/amd_detail/device_library_decls.h
* /opt/rocm/include/hip/amd_detail/functional_grid_launch.hpp
* /opt/rocm/include/hip/amd_detail/grid_launch.h
* /opt/rocm/include/hip/amd_detail/grid_launch.hpp
* /opt/rocm/include/hip/amd_detail/grid_launch_GGL.hpp
* /opt/rocm/include/hip/amd_detail/helpers.hpp
* /opt/rocm/include/hip/amd_detail/hip_api_trace.hpp
* /opt/rocm/include/hip/amd_detail/hip_assert.h
* /opt/rocm/include/hip/amd_detail/hip_cooperative_groups_helper.h
* /opt/rocm/include/hip/amd_detail/hip_fp16_gcc.h
* /opt/rocm/include/hip/amd_detail/hip_fp16_math_fwd.h
* /opt/rocm/include/hip/amd_detail/hip_ldg.h
* /opt/rocm/include/hip/amd_detail/hip_prof_str.h
* /opt/rocm/include/hip/amd_detail/hip_runtime_prof.h
* /opt/rocm/include/hip/amd_detail/host_defines.h
* /opt/rocm/include/hip/amd_detail/hsa_helpers.hpp
* /opt/rocm/include/hip/amd_detail/macro_based_grid_launch.hpp
* /opt/rocm/include/hip/amd_detail/math_fwd.h
* /opt/rocm/include/hip/amd_detail/ockl_image.h
* /opt/rocm/include/hip/amd_detail/program_state.hpp
* /opt/rocm/include/hip/amd_detail/texture_fetch_functions.h
* /opt/rocm/include/hip/amd_detail/texture_indirect_functions.h
* /opt/rocm/include/hip/channel_descriptor.h
* /opt/rocm/include/hip/device_functions.h
* /opt/rocm/include/hip/driver_types.h
* /opt/rocm/include/hip/hiprtc.h
* /opt/rocm/include/hip/hip_bf16.h
* /opt/rocm/include/hip/hip_bfloat16.h
* /opt/rocm/include/hip/hip_common.h
* /opt/rocm/include/hip/hip_complex.h
* /opt/rocm/include/hip/hip_cooperative_groups.h
* /opt/rocm/include/hip/hip_deprecated.h
* /opt/rocm/include/hip/hip_ext.h
* /opt/rocm/include/hip/hip_fp16.h
* /opt/rocm/include/hip/hip_fp8.h
* /opt/rocm/include/hip/hip_gl_interop.h
* /opt/rocm/include/hip/hip_hcc.h
* /opt/rocm/include/hip/hip_math_constants.h
* /opt/rocm/include/hip/hip_profile.h
* /opt/rocm/include/hip/hip_runtime.h
* /opt/rocm/include/hip/hip_runtime_api.h
* /opt/rocm/include/hip/hip_texture_types.h
* /opt/rocm/include/hip/hip_vector_types.h
* /opt/rocm/include/hip/hip_version.h
* /opt/rocm/include/hip/library_types.h
* /opt/rocm/include/hip/math_functions.h
* /opt/rocm/include/hip/surface_types.h
* /opt/rocm/include/hip/texture_types.h
* /opt/rocm/include/hip_prof_str.h
* /opt/rocm/lib/.hipInfo
* /opt/rocm/lib/cmake/hip-lang/hip-lang-config-version.cmake
* /opt/rocm/lib/cmake/hip-lang/hip-lang-config.cmake
* /opt/rocm/lib/cmake/hip-lang/hip-lang-targets-release.cmake
* /opt/rocm/lib/cmake/hip-lang/hip-lang-targets.cmake
* /opt/rocm/lib/cmake/hip/FindHIP.cmake
* /opt/rocm/lib/cmake/hip/FindHIP/run_hipcc.cmake
* /opt/rocm/lib/cmake/hip/FindHIP/run_make2cmake.cmake
* /opt/rocm/lib/cmake/hip/hip-config-amd.cmake
* /opt/rocm/lib/cmake/hip/hip-config-nvidia.cmake
* /opt/rocm/lib/cmake/hip/hip-config-version.cmake
* /opt/rocm/lib/cmake/hip/hip-config.cmake
* /opt/rocm/lib/cmake/hip/hip-targets-release.cmake
* /opt/rocm/lib/cmake/hip/hip-targets.cmake
* /opt/rocm/lib/cmake/hiprtc/hiprtc-config-version.cmake
* /opt/rocm/lib/cmake/hiprtc/hiprtc-config.cmake
* /opt/rocm/lib/cmake/hiprtc/hiprtc-targets-release.cmake
* /opt/rocm/lib/cmake/hiprtc/hiprtc-targets.cmake
* /opt/rocm/lib/libamdhip64.so
* /opt/rocm/lib/libamdhip64.so.6
* /opt/rocm/lib/libamdhip64.so.6.3.42134
* /opt/rocm/lib/libhiprtc-builtins.so
* /opt/rocm/lib/libhiprtc-builtins.so.6
* /opt/rocm/lib/libhiprtc-builtins.so.6.3.42134
* /opt/rocm/lib/libhiprtc.so
* /opt/rocm/lib/libhiprtc.so.6
* /opt/rocm/lib/libhiprtc.so.6.3.42134
* /opt/rocm/share/doc/hip-asan/LICENSE.txt
* /opt/rocm/share/doc/hip/LICENSE.txt
* /opt/rocm/share/hip/version
* /usr/share/doc/hip-runtime-amd-6.3.3/README.md
* /usr/share/doc/hip-runtime-amd-6.3.3/RELEASE.md
* /usr/share/doc/hip-runtime-amd-6.3.3/VERSION
