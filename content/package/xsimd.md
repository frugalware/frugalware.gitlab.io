+++
draft = false
title = "xsimd 13.2.0-1"
version = "13.2.0-1"
description = "QuantStack tools library - Multi-dimensional arrays with broadcasting and lazy computing"
date = "2025-03-02T20:33:42"
aliases = "/packages/220486"
categories = ['devel-extra']
upstreamurl = "https://github.com/xtensor-stack/xsimd"
arch = "x86_64"
size = "127588"
usize = "1481203"
sha1sum = "731b3341a2ad5302e054c7973832f388da896a30"
depends = "['glibc']"
reverse_depends = "['python3-scipy']"
+++
### Description: 
QuantStack tools library - Multi-dimensional arrays with broadcasting and lazy computing

### Files: 
* /usr/include/xsimd/arch/generic/xsimd_generic_arithmetic.hpp
* /usr/include/xsimd/arch/generic/xsimd_generic_complex.hpp
* /usr/include/xsimd/arch/generic/xsimd_generic_details.hpp
* /usr/include/xsimd/arch/generic/xsimd_generic_logical.hpp
* /usr/include/xsimd/arch/generic/xsimd_generic_math.hpp
* /usr/include/xsimd/arch/generic/xsimd_generic_memory.hpp
* /usr/include/xsimd/arch/generic/xsimd_generic_rounding.hpp
* /usr/include/xsimd/arch/generic/xsimd_generic_trigo.hpp
* /usr/include/xsimd/arch/xsimd_avx.hpp
* /usr/include/xsimd/arch/xsimd_avx2.hpp
* /usr/include/xsimd/arch/xsimd_avx512bw.hpp
* /usr/include/xsimd/arch/xsimd_avx512cd.hpp
* /usr/include/xsimd/arch/xsimd_avx512dq.hpp
* /usr/include/xsimd/arch/xsimd_avx512er.hpp
* /usr/include/xsimd/arch/xsimd_avx512f.hpp
* /usr/include/xsimd/arch/xsimd_avx512ifma.hpp
* /usr/include/xsimd/arch/xsimd_avx512pf.hpp
* /usr/include/xsimd/arch/xsimd_avx512vbmi.hpp
* /usr/include/xsimd/arch/xsimd_avx512vnni_avx512bw.hpp
* /usr/include/xsimd/arch/xsimd_avx512vnni_avx512vbmi.hpp
* /usr/include/xsimd/arch/xsimd_avxvnni.hpp
* /usr/include/xsimd/arch/xsimd_constants.hpp
* /usr/include/xsimd/arch/xsimd_emulated.hpp
* /usr/include/xsimd/arch/xsimd_fma3_avx.hpp
* /usr/include/xsimd/arch/xsimd_fma3_avx2.hpp
* /usr/include/xsimd/arch/xsimd_fma3_sse.hpp
* /usr/include/xsimd/arch/xsimd_fma4.hpp
* /usr/include/xsimd/arch/xsimd_generic.hpp
* /usr/include/xsimd/arch/xsimd_generic_fwd.hpp
* /usr/include/xsimd/arch/xsimd_i8mm_neon64.hpp
* /usr/include/xsimd/arch/xsimd_isa.hpp
* /usr/include/xsimd/arch/xsimd_neon.hpp
* /usr/include/xsimd/arch/xsimd_neon64.hpp
* /usr/include/xsimd/arch/xsimd_rvv.hpp
* /usr/include/xsimd/arch/xsimd_scalar.hpp
* /usr/include/xsimd/arch/xsimd_sse2.hpp
* /usr/include/xsimd/arch/xsimd_sse3.hpp
* /usr/include/xsimd/arch/xsimd_sse4_1.hpp
* /usr/include/xsimd/arch/xsimd_sse4_2.hpp
* /usr/include/xsimd/arch/xsimd_ssse3.hpp
* /usr/include/xsimd/arch/xsimd_sve.hpp
* /usr/include/xsimd/arch/xsimd_wasm.hpp
* /usr/include/xsimd/config/xsimd_arch.hpp
* /usr/include/xsimd/config/xsimd_config.hpp
* /usr/include/xsimd/config/xsimd_cpuid.hpp
* /usr/include/xsimd/config/xsimd_inline.hpp
* /usr/include/xsimd/math/xsimd_rem_pio2.hpp
* /usr/include/xsimd/memory/xsimd_aligned_allocator.hpp
* /usr/include/xsimd/memory/xsimd_alignment.hpp
* /usr/include/xsimd/types/xsimd_all_registers.hpp
* /usr/include/xsimd/types/xsimd_api.hpp
* /usr/include/xsimd/types/xsimd_avx2_register.hpp
* /usr/include/xsimd/types/xsimd_avx512bw_register.hpp
* /usr/include/xsimd/types/xsimd_avx512cd_register.hpp
* /usr/include/xsimd/types/xsimd_avx512dq_register.hpp
* /usr/include/xsimd/types/xsimd_avx512er_register.hpp
* /usr/include/xsimd/types/xsimd_avx512f_register.hpp
* /usr/include/xsimd/types/xsimd_avx512ifma_register.hpp
* /usr/include/xsimd/types/xsimd_avx512pf_register.hpp
* /usr/include/xsimd/types/xsimd_avx512vbmi_register.hpp
* /usr/include/xsimd/types/xsimd_avx512vnni_avx512bw_register.hpp
* /usr/include/xsimd/types/xsimd_avx512vnni_avx512vbmi_register.hpp
* /usr/include/xsimd/types/xsimd_avxvnni_register.hpp
* /usr/include/xsimd/types/xsimd_avx_register.hpp
* /usr/include/xsimd/types/xsimd_batch.hpp
* /usr/include/xsimd/types/xsimd_batch_constant.hpp
* /usr/include/xsimd/types/xsimd_emulated_register.hpp
* /usr/include/xsimd/types/xsimd_fma3_avx2_register.hpp
* /usr/include/xsimd/types/xsimd_fma3_avx_register.hpp
* /usr/include/xsimd/types/xsimd_fma3_sse_register.hpp
* /usr/include/xsimd/types/xsimd_fma4_register.hpp
* /usr/include/xsimd/types/xsimd_generic_arch.hpp
* /usr/include/xsimd/types/xsimd_i8mm_neon64_register.hpp
* /usr/include/xsimd/types/xsimd_neon64_register.hpp
* /usr/include/xsimd/types/xsimd_neon_register.hpp
* /usr/include/xsimd/types/xsimd_register.hpp
* /usr/include/xsimd/types/xsimd_rvv_register.hpp
* /usr/include/xsimd/types/xsimd_sse2_register.hpp
* /usr/include/xsimd/types/xsimd_sse3_register.hpp
* /usr/include/xsimd/types/xsimd_sse4_1_register.hpp
* /usr/include/xsimd/types/xsimd_sse4_2_register.hpp
* /usr/include/xsimd/types/xsimd_ssse3_register.hpp
* /usr/include/xsimd/types/xsimd_sve_register.hpp
* /usr/include/xsimd/types/xsimd_traits.hpp
* /usr/include/xsimd/types/xsimd_utils.hpp
* /usr/include/xsimd/types/xsimd_wasm_register.hpp
* /usr/include/xsimd/xsimd.hpp
* /usr/share/cmake/xsimd/xsimdConfig.cmake
* /usr/share/cmake/xsimd/xsimdConfigVersion.cmake
* /usr/share/cmake/xsimd/xsimdTargets.cmake
* /usr/share/doc/xsimd-13.2.0/LICENSE
* /usr/share/doc/xsimd-13.2.0/README.md
* /usr/share/pkgconfig/xsimd.pc
