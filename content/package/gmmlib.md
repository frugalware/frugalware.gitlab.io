+++
draft = false
title = "gmmlib 22.8.0-1"
version = "22.8.0-1"
description = "Intel Graphics Memory Management Library"
date = "2025-07-05T08:34:42"
aliases = "/packages/220080"
categories = ['lib']
upstreamurl = "https://github.com/intel/gmmlib"
arch = "x86_64"
size = "286720"
usize = "1896508"
sha1sum = "b806f6e31e085fd632023d83ade2678e5adee0f2"
depends = "['libstdc++>=12.2']"
reverse_depends = "['intel-compute-runtime', 'media-driver']"
+++
### Description: 
Intel Graphics Memory Management Library

### Files: 
* /usr/include/igdgmm/GmmLib/CachePolicy/GmmCachePolicyConditionals.h
* /usr/include/igdgmm/GmmLib/CachePolicy/GmmCachePolicyResourceUsageDefinitions.h
* /usr/include/igdgmm/GmmLib/CachePolicy/GmmCachePolicyUndefineConditionals.h
* /usr/include/igdgmm/GmmLib/CachePolicy/GmmGen10CachePolicy.h
* /usr/include/igdgmm/GmmLib/CachePolicy/GmmGen11CachePolicy.h
* /usr/include/igdgmm/GmmLib/CachePolicy/GmmGen12CachePolicy.h
* /usr/include/igdgmm/GmmLib/CachePolicy/GmmGen12dGPUCachePolicy.h
* /usr/include/igdgmm/GmmLib/CachePolicy/GmmGen8CachePolicy.h
* /usr/include/igdgmm/GmmLib/CachePolicy/GmmGen9CachePolicy.h
* /usr/include/igdgmm/GmmLib/CachePolicy/GmmXe2_LPGCachePolicy.h
* /usr/include/igdgmm/GmmLib/CachePolicy/GmmXe_LPGCachePolicy.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/CachePolicy/GmmCachePolicyGen10.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/CachePolicy/GmmCachePolicyGen11.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/CachePolicy/GmmCachePolicyGen12.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/CachePolicy/GmmCachePolicyGen12dGPU.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/CachePolicy/GmmCachePolicyGen8.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/CachePolicy/GmmCachePolicyGen9.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/CachePolicy/GmmCachePolicyXe2_LPG.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/CachePolicy/GmmCachePolicyXe_LPG.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmCachePolicy.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmCachePolicyCommon.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmCachePolicyExt.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmClientContext.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmCommonExt.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmConst.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmDebug.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmFormatTable.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmHw.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmInfo.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmInfoExt.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmInternal.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmLibDll.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmLibDllName.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmMemAllocator.hpp
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmPageTableMgr.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmPlatformExt.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmProto.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmResourceFlags.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmResourceInfo.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmResourceInfoCommon.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmResourceInfoExt.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmTextureExt.h
* /usr/include/igdgmm/GmmLib/inc/External/Common/GmmUtil.h
* /usr/include/igdgmm/GmmLib/inc/External/Linux/GmmResourceInfoLin.h
* /usr/include/igdgmm/GmmLib/inc/External/Linux/GmmResourceInfoLinExt.h
* /usr/include/igdgmm/GmmLib/inc/GmmLib.h
* /usr/include/igdgmm/GmmLib/Platform/GmmPlatforms.h
* /usr/include/igdgmm/GmmLib/Texture/GmmTexture.h
* /usr/include/igdgmm/GmmLib/TranslationTable/GmmUmdTranslationTable.h
* /usr/include/igdgmm/GmmLib/Utility/CpuSwizzleBlt/assert.h
* /usr/include/igdgmm/GmmLib/Utility/CpuSwizzleBlt/CpuSwizzleBlt.c
* /usr/include/igdgmm/GmmLib/Utility/GmmLog/GmmLog.h
* /usr/include/igdgmm/GmmLib/Utility/GmmUtility.h
* /usr/include/igdgmm/igdgmm.h
* /usr/include/igdgmm/inc/common/gfxmacro.h
* /usr/include/igdgmm/inc/common/gfxplatform.h
* /usr/include/igdgmm/inc/common/gtsysinfo.h
* /usr/include/igdgmm/inc/common/igfxfmid.h
* /usr/include/igdgmm/inc/common/sku_wa.h
* /usr/include/igdgmm/inc/portable_compiler.h
* /usr/include/igdgmm/inc/umKmInc/sharedata.h
* /usr/include/igdgmm/inc/umKmInc/UmKmDmaPerfTimer.h
* /usr/include/igdgmm/inc/umKmInc/UmKmEnum.h
* /usr/include/igdgmm/util/gfxDebug.h
* /usr/include/igdgmm/util/g_gfxDebug.h
* /usr/lib/libigdgmm.so
* /usr/lib/libigdgmm.so.12
* /usr/lib/libigdgmm.so.12.8.0
* /usr/lib/pkgconfig/igdgmm.pc
* /usr/share/doc/gmmlib-22.8.0/README.rst
