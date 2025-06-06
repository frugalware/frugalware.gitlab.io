+++
draft = false
title = "rkcommon 1.14.2-1"
version = "1.14.2-1"
description = "Common C++ infrastructure for oneAPI Rendering Toolkit"
date = "2025-01-03T14:04:34"
aliases = "/packages/220249"
categories = ['xlib-extra']
upstreamurl = "https://github.com/RenderKit/rkcommon"
arch = "x86_64"
size = "523128"
usize = "2428735"
sha1sum = "163b9220dac40fc7bee289084a97811bce1c3095"
depends = "['intel-tbb']"
reverse_depends = "['openvkl']"
+++
### Description: 
Common C++ infrastructure for oneAPI Rendering Toolkit

### Files: 
* /usr/bin/rkcommon_test_suite
* /usr/include/rkcommon/array3D/Array3D.h
* /usr/include/rkcommon/array3D/for_each.h
* /usr/include/rkcommon/common.h
* /usr/include/rkcommon/containers/AlignedVector.h
* /usr/include/rkcommon/containers/aligned_allocator.h
* /usr/include/rkcommon/containers/FlatMap.h
* /usr/include/rkcommon/containers/TransactionalBuffer.h
* /usr/include/rkcommon/math/AffineSpace.h
* /usr/include/rkcommon/math/AffineSpace.ih
* /usr/include/rkcommon/math/arm/emulation.h
* /usr/include/rkcommon/math/arm/sse2neon.h
* /usr/include/rkcommon/math/box.h
* /usr/include/rkcommon/math/box.ih
* /usr/include/rkcommon/math/constants.h
* /usr/include/rkcommon/math/LinearSpace.h
* /usr/include/rkcommon/math/LinearSpace.ih
* /usr/include/rkcommon/math/math.ih
* /usr/include/rkcommon/math/Quaternion.h
* /usr/include/rkcommon/math/range.h
* /usr/include/rkcommon/math/rkmath.h
* /usr/include/rkcommon/math/vec.h
* /usr/include/rkcommon/math/vec.ih
* /usr/include/rkcommon/memory/DeletedUniquePtr.h
* /usr/include/rkcommon/memory/IntrusivePtr.h
* /usr/include/rkcommon/memory/malloc.h
* /usr/include/rkcommon/memory/RefCount.h
* /usr/include/rkcommon/networking/DataStreaming.h
* /usr/include/rkcommon/networking/Fabric.h
* /usr/include/rkcommon/os/FileName.h
* /usr/include/rkcommon/os/library.h
* /usr/include/rkcommon/platform.h
* /usr/include/rkcommon/tasking/async.h
* /usr/include/rkcommon/tasking/AsyncLoop.h
* /usr/include/rkcommon/tasking/AsyncTask.h
* /usr/include/rkcommon/tasking/detail/async_task.inl
* /usr/include/rkcommon/tasking/detail/enkiTS/LockLessMultiReadPipe.h
* /usr/include/rkcommon/tasking/detail/enkiTS/TaskScheduler.h
* /usr/include/rkcommon/tasking/detail/parallel_for.inl
* /usr/include/rkcommon/tasking/detail/schedule.inl
* /usr/include/rkcommon/tasking/detail/TaskSys.h
* /usr/include/rkcommon/tasking/parallel_for.h
* /usr/include/rkcommon/tasking/parallel_foreach.h
* /usr/include/rkcommon/tasking/schedule.h
* /usr/include/rkcommon/tasking/tasking_system_init.h
* /usr/include/rkcommon/tracing/Tracing.h
* /usr/include/rkcommon/traits/rktraits.h
* /usr/include/rkcommon/utility/AbstractArray.h
* /usr/include/rkcommon/utility/Any.h
* /usr/include/rkcommon/utility/ArgumentList.h
* /usr/include/rkcommon/utility/ArrayView.h
* /usr/include/rkcommon/utility/CodeTimer.h
* /usr/include/rkcommon/utility/DataView.h
* /usr/include/rkcommon/utility/demangle.h
* /usr/include/rkcommon/utility/detail/pcg_extras.hpp
* /usr/include/rkcommon/utility/detail/pcg_random.hpp
* /usr/include/rkcommon/utility/detail/pcg_uint128.hpp
* /usr/include/rkcommon/utility/DoubleBufferedValue.h
* /usr/include/rkcommon/utility/FixedArray.h
* /usr/include/rkcommon/utility/FixedArrayView.h
* /usr/include/rkcommon/utility/getEnvVar.h
* /usr/include/rkcommon/utility/multidim_index_sequence.h
* /usr/include/rkcommon/utility/Observer.h
* /usr/include/rkcommon/utility/OnScopeExit.h
* /usr/include/rkcommon/utility/Optional.h
* /usr/include/rkcommon/utility/OwnedArray.h
* /usr/include/rkcommon/utility/ParameterizedObject.h
* /usr/include/rkcommon/utility/PseudoURL.h
* /usr/include/rkcommon/utility/random.h
* /usr/include/rkcommon/utility/random.ih
* /usr/include/rkcommon/utility/SaveImage.h
* /usr/include/rkcommon/utility/StringManip.h
* /usr/include/rkcommon/utility/TimeStamp.h
* /usr/include/rkcommon/utility/TransactionalValue.h
* /usr/include/rkcommon/xml/XML.h
* /usr/lib/cmake/rkcommon-1.14.2/FindTBB.cmake
* /usr/lib/cmake/rkcommon-1.14.2/rkcommonConfig.cmake
* /usr/lib/cmake/rkcommon-1.14.2/rkcommonConfigVersion.cmake
* /usr/lib/cmake/rkcommon-1.14.2/rkcommon_Exports-release.cmake
* /usr/lib/cmake/rkcommon-1.14.2/rkcommon_Exports.cmake
* /usr/lib/cmake/rkcommon-1.14.2/rkcommon_macros.cmake
* /usr/lib/librkcommon.so
* /usr/lib/librkcommon.so.1
* /usr/lib/librkcommon.so.1.14.2
* /usr/share/doc/rkcommon-1.14.2/README.md
