+++
draft = false
title = "rocsparse 6.4.1-1"
version = "6.4.1-1"
description = "BLAS for sparse computation on top of ROCm"
date = "2025-07-01T09:27:06"
aliases = "/packages/222767"
categories = ['lib-extra']
upstreamurl = "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/index.html"
arch = "x86_64"
size = "15208884"
usize = "67531631"
sha1sum = "393eb2e96cf5bf9ec4f818dc847e1623f372d92b"
depends = "['hip-runtime-amd', 'rocm-core', 'rocprim']"
+++
### Description: 
BLAS for sparse computation on top of ROCm

### Files: 
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_bsr2csr.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_bsrpad_value.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_coo2csr.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_coo2dense.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_coosort.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_csc2dense.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_cscsort.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_csr2bsr.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_csr2coo.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_csr2csc.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_csr2csr_compress.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_csr2dense.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_csr2ell.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_csr2gebsr.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_csr2hyb.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_csrsort.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_dense2coo.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_dense2csc.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_dense2csr.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_ell2csr.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_gebsr2csr.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_gebsr2gebsc.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_gebsr2gebsr.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_hyb2csr.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_inverse_permutation.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_nnz.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_nnz_compress.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_prune_csr2csr.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_prune_csr2csr_by_percentage.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_prune_dense2csr.h
* /opt/rocm/include/rocsparse/internal/conversion/rocsparse_prune_dense2csr_by_percentage.h
* /opt/rocm/include/rocsparse/internal/extra/rocsparse_bsrgeam.h
* /opt/rocm/include/rocsparse/internal/extra/rocsparse_bsrgemm.h
* /opt/rocm/include/rocsparse/internal/extra/rocsparse_csrgeam.h
* /opt/rocm/include/rocsparse/internal/extra/rocsparse_csrgemm.h
* /opt/rocm/include/rocsparse/internal/generic/rocsparse_axpby.h
* /opt/rocm/include/rocsparse/internal/generic/rocsparse_check_spmat.h
* /opt/rocm/include/rocsparse/internal/generic/rocsparse_dense_to_sparse.h
* /opt/rocm/include/rocsparse/internal/generic/rocsparse_extract.h
* /opt/rocm/include/rocsparse/internal/generic/rocsparse_gather.h
* /opt/rocm/include/rocsparse/internal/generic/rocsparse_rot.h
* /opt/rocm/include/rocsparse/internal/generic/rocsparse_scatter.h
* /opt/rocm/include/rocsparse/internal/generic/rocsparse_sddmm.h
* /opt/rocm/include/rocsparse/internal/generic/rocsparse_sparse_to_dense.h
* /opt/rocm/include/rocsparse/internal/generic/rocsparse_sparse_to_sparse.h
* /opt/rocm/include/rocsparse/internal/generic/rocsparse_spgemm.h
* /opt/rocm/include/rocsparse/internal/generic/rocsparse_spitsv.h
* /opt/rocm/include/rocsparse/internal/generic/rocsparse_spmm.h
* /opt/rocm/include/rocsparse/internal/generic/rocsparse_spmv.h
* /opt/rocm/include/rocsparse/internal/generic/rocsparse_spsm.h
* /opt/rocm/include/rocsparse/internal/generic/rocsparse_spsv.h
* /opt/rocm/include/rocsparse/internal/generic/rocsparse_spvv.h
* /opt/rocm/include/rocsparse/internal/level1/rocsparse_axpyi.h
* /opt/rocm/include/rocsparse/internal/level1/rocsparse_dotci.h
* /opt/rocm/include/rocsparse/internal/level1/rocsparse_doti.h
* /opt/rocm/include/rocsparse/internal/level1/rocsparse_gthr.h
* /opt/rocm/include/rocsparse/internal/level1/rocsparse_gthrz.h
* /opt/rocm/include/rocsparse/internal/level1/rocsparse_roti.h
* /opt/rocm/include/rocsparse/internal/level1/rocsparse_sctr.h
* /opt/rocm/include/rocsparse/internal/level2/rocsparse_bsrmv.h
* /opt/rocm/include/rocsparse/internal/level2/rocsparse_bsrsv.h
* /opt/rocm/include/rocsparse/internal/level2/rocsparse_bsrxmv.h
* /opt/rocm/include/rocsparse/internal/level2/rocsparse_coomv.h
* /opt/rocm/include/rocsparse/internal/level2/rocsparse_csritsv.h
* /opt/rocm/include/rocsparse/internal/level2/rocsparse_csrmv.h
* /opt/rocm/include/rocsparse/internal/level2/rocsparse_csrsv.h
* /opt/rocm/include/rocsparse/internal/level2/rocsparse_ellmv.h
* /opt/rocm/include/rocsparse/internal/level2/rocsparse_gebsrmv.h
* /opt/rocm/include/rocsparse/internal/level2/rocsparse_gemvi.h
* /opt/rocm/include/rocsparse/internal/level2/rocsparse_hybmv.h
* /opt/rocm/include/rocsparse/internal/level3/rocsparse_bsrmm.h
* /opt/rocm/include/rocsparse/internal/level3/rocsparse_bsrsm.h
* /opt/rocm/include/rocsparse/internal/level3/rocsparse_csrmm.h
* /opt/rocm/include/rocsparse/internal/level3/rocsparse_csrsm.h
* /opt/rocm/include/rocsparse/internal/level3/rocsparse_gebsrmm.h
* /opt/rocm/include/rocsparse/internal/level3/rocsparse_gemmi.h
* /opt/rocm/include/rocsparse/internal/precond/rocsparse_bsric0.h
* /opt/rocm/include/rocsparse/internal/precond/rocsparse_bsrilu0.h
* /opt/rocm/include/rocsparse/internal/precond/rocsparse_csric0.h
* /opt/rocm/include/rocsparse/internal/precond/rocsparse_csrilu0.h
* /opt/rocm/include/rocsparse/internal/precond/rocsparse_csritilu0.h
* /opt/rocm/include/rocsparse/internal/precond/rocsparse_gpsv.h
* /opt/rocm/include/rocsparse/internal/precond/rocsparse_gtsv.h
* /opt/rocm/include/rocsparse/internal/reordering/rocsparse_csrcolor.h
* /opt/rocm/include/rocsparse/internal/rocsparse-conversion.h
* /opt/rocm/include/rocsparse/internal/rocsparse-extra.h
* /opt/rocm/include/rocsparse/internal/rocsparse-generic.h
* /opt/rocm/include/rocsparse/internal/rocsparse-level1.h
* /opt/rocm/include/rocsparse/internal/rocsparse-level2.h
* /opt/rocm/include/rocsparse/internal/rocsparse-level3.h
* /opt/rocm/include/rocsparse/internal/rocsparse-precond.h
* /opt/rocm/include/rocsparse/internal/rocsparse-reordering.h
* /opt/rocm/include/rocsparse/internal/rocsparse-util.h
* /opt/rocm/include/rocsparse/internal/util/rocsparse_check_matrix_coo.h
* /opt/rocm/include/rocsparse/internal/util/rocsparse_check_matrix_csc.h
* /opt/rocm/include/rocsparse/internal/util/rocsparse_check_matrix_csr.h
* /opt/rocm/include/rocsparse/internal/util/rocsparse_check_matrix_ell.h
* /opt/rocm/include/rocsparse/internal/util/rocsparse_check_matrix_gebsc.h
* /opt/rocm/include/rocsparse/internal/util/rocsparse_check_matrix_gebsr.h
* /opt/rocm/include/rocsparse/internal/util/rocsparse_check_matrix_hyb.h
* /opt/rocm/include/rocsparse/rocsparse-auxiliary.h
* /opt/rocm/include/rocsparse/rocsparse-complex-types.h
* /opt/rocm/include/rocsparse/rocsparse-export.h
* /opt/rocm/include/rocsparse/rocsparse-functions.h
* /opt/rocm/include/rocsparse/rocsparse-types.h
* /opt/rocm/include/rocsparse/rocsparse-version.h
* /opt/rocm/include/rocsparse/rocsparse.f90
* /opt/rocm/include/rocsparse/rocsparse.h
* /opt/rocm/include/rocsparse/rocsparse_enums.f90
* /opt/rocm/lib/cmake/rocsparse/rocsparse-config-version.cmake
* /opt/rocm/lib/cmake/rocsparse/rocsparse-config.cmake
* /opt/rocm/lib/cmake/rocsparse/rocsparse-targets-none.cmake
* /opt/rocm/lib/cmake/rocsparse/rocsparse-targets.cmake
* /opt/rocm/lib/librocsparse.so
* /opt/rocm/lib/librocsparse.so.1
* /opt/rocm/lib/librocsparse.so.1.0
* /opt/rocm/share/doc/rocsparse/LICENSE.md
* /usr/share/doc/rocsparse-6.4.1/README.md
