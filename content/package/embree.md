+++
draft = false
title = "embree 4.3.3-1"
version = "4.3.3-1"
description = "Collection of high-performance ray tracing kernels"
date = "2024-08-04T16:58:06"
aliases = "/packages/220211"
categories = ['xlib-extra']
upstreamurl = "https://github.com/RenderKit/embree"
arch = "x86_64"
size = "11533324"
usize = "45319493"
sha1sum = "855c4937cc70a9e646e5c6ab2811c9a8bca5694d"
depends = "['glfw', 'intel-tbb', 'openimageio>=2.3.15.0']"
reverse_depends = "['blender', 'openvkl']"
+++
### Description: 
Collection of high-performance ray tracing kernels

### Files: 
* /usr/include/embree4/rtcore.h
* /usr/include/embree4/rtcore.isph
* /usr/include/embree4/rtcore_buffer.h
* /usr/include/embree4/rtcore_buffer.isph
* /usr/include/embree4/rtcore_builder.h
* /usr/include/embree4/rtcore_common.h
* /usr/include/embree4/rtcore_common.isph
* /usr/include/embree4/rtcore_config.h
* /usr/include/embree4/rtcore_device.h
* /usr/include/embree4/rtcore_device.isph
* /usr/include/embree4/rtcore_geometry.h
* /usr/include/embree4/rtcore_geometry.isph
* /usr/include/embree4/rtcore_quaternion.h
* /usr/include/embree4/rtcore_quaternion.isph
* /usr/include/embree4/rtcore_ray.h
* /usr/include/embree4/rtcore_ray.isph
* /usr/include/embree4/rtcore_scene.h
* /usr/include/embree4/rtcore_scene.isph
* /usr/lib/cmake/embree-4.3.3/embree-config-version.cmake
* /usr/lib/cmake/embree-4.3.3/embree-config.cmake
* /usr/lib/cmake/embree-4.3.3/embree-targets-release.cmake
* /usr/lib/cmake/embree-4.3.3/embree-targets.cmake
* /usr/lib/libembree4.so
* /usr/lib/libembree4.so.4
* /usr/share/doc/embree-4.3.3/README.md
* /usr/share/doc/embree4/CHANGELOG.md
* /usr/share/doc/embree4/LICENSE.txt
* /usr/share/doc/embree4/README.md
* /usr/share/doc/embree4/readme.pdf
* /usr/share/doc/embree4/third-party-programs-DPCPP.txt
* /usr/share/doc/embree4/third-party-programs-OIDN.txt
* /usr/share/doc/embree4/third-party-programs-oneAPI-DPCPP.txt
* /usr/share/doc/embree4/third-party-programs-TBB.txt
* /usr/share/doc/embree4/third-party-programs.txt
* /usr/share/man/man3/rtcAttachGeometry.4embree4.gz
* /usr/share/man/man3/rtcAttachGeometryByID.4embree4.gz
* /usr/share/man/man3/RTCBufferType.4embree4.gz
* /usr/share/man/man3/rtcBuildBVH.4embree4.gz
* /usr/share/man/man3/rtcCollide.4embree4.gz
* /usr/share/man/man3/rtcCommitGeometry.4embree4.gz
* /usr/share/man/man3/rtcCommitScene.4embree4.gz
* /usr/share/man/man3/RTCCurveFlags.4embree4.gz
* /usr/share/man/man3/rtcDetachGeometry.4embree4.gz
* /usr/share/man/man3/rtcDisableGeometry.4embree4.gz
* /usr/share/man/man3/rtcEnableGeometry.4embree4.gz
* /usr/share/man/man3/RTCFeatureFlags.4embree4.gz
* /usr/share/man/man3/rtcFilterIntersection.4embree4.gz
* /usr/share/man/man3/rtcFilterOcclusion.4embree4.gz
* /usr/share/man/man3/RTCFormat.4embree4.gz
* /usr/share/man/man3/rtcForwardIntersect1.4embree4.gz
* /usr/share/man/man3/rtcForwardIntersect4.4embree4.gz
* /usr/share/man/man3/rtcForwardOccluded1.4embree4.gz
* /usr/share/man/man3/rtcForwardOccluded4.4embree4.gz
* /usr/share/man/man3/rtcGetBufferData.4embree4.gz
* /usr/share/man/man3/rtcGetDeviceError.4embree4.gz
* /usr/share/man/man3/rtcGetDeviceLastErrorMessage.4embree4.gz
* /usr/share/man/man3/rtcGetDeviceProperty.4embree4.gz
* /usr/share/man/man3/rtcGetErrorString.4embree4.gz
* /usr/share/man/man3/rtcGetGeometry.4embree4.gz
* /usr/share/man/man3/rtcGetGeometryBufferData.4embree4.gz
* /usr/share/man/man3/rtcGetGeometryFace.4embree4.gz
* /usr/share/man/man3/rtcGetGeometryFirstHalfEdge.4embree4.gz
* /usr/share/man/man3/rtcGetGeometryNextHalfEdge.4embree4.gz
* /usr/share/man/man3/rtcGetGeometryOppositeHalfEdge.4embree4.gz
* /usr/share/man/man3/rtcGetGeometryPreviousHalfEdge.4embree4.gz
* /usr/share/man/man3/rtcGetGeometryThreadSafe.4embree4.gz
* /usr/share/man/man3/rtcGetGeometryTransform.4embree4.gz
* /usr/share/man/man3/rtcGetGeometryTransformEx.4embree4.gz
* /usr/share/man/man3/rtcGetGeometryTransformFromScene.4embree4.gz
* /usr/share/man/man3/rtcGetGeometryUserData.4embree4.gz
* /usr/share/man/man3/rtcGetGeometryUserDataFromScene.4embree4.gz
* /usr/share/man/man3/rtcGetSceneBounds.4embree4.gz
* /usr/share/man/man3/rtcGetSceneDevice.4embree4.gz
* /usr/share/man/man3/rtcGetSceneFlags.4embree4.gz
* /usr/share/man/man3/rtcGetSceneLinearBounds.4embree4.gz
* /usr/share/man/man3/rtcGetSYCLDeviceFunctionPointer.4embree4.gz
* /usr/share/man/man3/RTCHit.4embree4.gz
* /usr/share/man/man3/RTCHitN.4embree4.gz
* /usr/share/man/man3/rtcInitIntersectArguments.4embree4.gz
* /usr/share/man/man3/rtcInitOccludedArguments.4embree4.gz
* /usr/share/man/man3/rtcInitPointQueryContext.4embree4.gz
* /usr/share/man/man3/rtcInitQuaternionDecomposition.4embree4.gz
* /usr/share/man/man3/rtcInitRayQueryContext.4embree4.gz
* /usr/share/man/man3/rtcInterpolate.4embree4.gz
* /usr/share/man/man3/rtcInterpolateN.4embree4.gz
* /usr/share/man/man3/rtcIntersect1.4embree4.gz
* /usr/share/man/man3/rtcIntersect4.4embree4.gz
* /usr/share/man/man3/rtcInvokeIntersectFilterFromGeometry.4embree4.gz
* /usr/share/man/man3/rtcInvokeOccludedFilterFromGeometry.4embree4.gz
* /usr/share/man/man3/rtcIsSYCLDeviceSupported.4embree4.gz
* /usr/share/man/man3/rtcJoinCommitScene.4embree4.gz
* /usr/share/man/man3/rtcNewBuffer.4embree4.gz
* /usr/share/man/man3/rtcNewBVH.4embree4.gz
* /usr/share/man/man3/rtcNewDevice.4embree4.gz
* /usr/share/man/man3/rtcNewGeometry.4embree4.gz
* /usr/share/man/man3/rtcNewScene.4embree4.gz
* /usr/share/man/man3/rtcNewSharedBuffer.4embree4.gz
* /usr/share/man/man3/rtcNewSYCLDevice.4embree4.gz
* /usr/share/man/man3/rtcOccluded1.4embree4.gz
* /usr/share/man/man3/rtcOccluded4.4embree4.gz
* /usr/share/man/man3/rtcPointQuery.4embree4.gz
* /usr/share/man/man3/rtcPointQuery4.4embree4.gz
* /usr/share/man/man3/RTCQuaternionDecomposition.4embree4.gz
* /usr/share/man/man3/RTCRay.4embree4.gz
* /usr/share/man/man3/RTCRayHit.4embree4.gz
* /usr/share/man/man3/RTCRayHitN.4embree4.gz
* /usr/share/man/man3/RTCRayN.4embree4.gz
* /usr/share/man/man3/rtcReleaseBuffer.4embree4.gz
* /usr/share/man/man3/rtcReleaseBVH.4embree4.gz
* /usr/share/man/man3/rtcReleaseDevice.4embree4.gz
* /usr/share/man/man3/rtcReleaseGeometry.4embree4.gz
* /usr/share/man/man3/rtcReleaseScene.4embree4.gz
* /usr/share/man/man3/rtcRetainBuffer.4embree4.gz
* /usr/share/man/man3/rtcRetainBVH.4embree4.gz
* /usr/share/man/man3/rtcRetainDevice.4embree4.gz
* /usr/share/man/man3/rtcRetainGeometry.4embree4.gz
* /usr/share/man/man3/rtcRetainScene.4embree4.gz
* /usr/share/man/man3/rtcSetDeviceErrorFunction.4embree4.gz
* /usr/share/man/man3/rtcSetDeviceMemoryMonitorFunction.4embree4.gz
* /usr/share/man/man3/rtcSetDeviceSYCLDevice.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryBoundsFunction.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryBuffer.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryBuildQuality.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryDisplacementFunction.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryEnableFilterFunctionFromArguments.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryInstancedScene.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryInstancedScenes.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryIntersectFilterFunction.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryIntersectFunction.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryMask.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryMaxRadiusScale.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryOccludedFilterFunction.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryOccludedFunction.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryPointQueryFunction.4embree4.gz
* /usr/share/man/man3/rtcSetGeometrySubdivisionMode.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryTessellationRate.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryTimeRange.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryTimeStepCount.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryTopologyCount.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryTransform.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryTransformQuaternion.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryUserData.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryUserPrimitiveCount.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryVertexAttributeCount.4embree4.gz
* /usr/share/man/man3/rtcSetGeometryVertexAttributeTopology.4embree4.gz
* /usr/share/man/man3/rtcSetNewGeometryBuffer.4embree4.gz
* /usr/share/man/man3/rtcSetSceneBuildQuality.4embree4.gz
* /usr/share/man/man3/rtcSetSceneFlags.4embree4.gz
* /usr/share/man/man3/rtcSetSceneProgressMonitorFunction.4embree4.gz
* /usr/share/man/man3/rtcSetSharedGeometryBuffer.4embree4.gz
* /usr/share/man/man3/rtcSYCLDeviceSelector.4embree4.gz
* /usr/share/man/man3/rtcUpdateGeometryBuffer.4embree4.gz
* /usr/share/man/man3/RTC_GEOMETRY_TYPE_CURVE.4embree4.gz
* /usr/share/man/man3/RTC_GEOMETRY_TYPE_GRID.4embree4.gz
* /usr/share/man/man3/RTC_GEOMETRY_TYPE_INSTANCE.4embree4.gz
* /usr/share/man/man3/RTC_GEOMETRY_TYPE_INSTANCE_ARRAY.4embree4.gz
* /usr/share/man/man3/RTC_GEOMETRY_TYPE_POINT.4embree4.gz
* /usr/share/man/man3/RTC_GEOMETRY_TYPE_QUAD.4embree4.gz
* /usr/share/man/man3/RTC_GEOMETRY_TYPE_SUBDIVISION.4embree4.gz
* /usr/share/man/man3/RTC_GEOMETRY_TYPE_TRIANGLE.4embree4.gz
* /usr/share/man/man3/RTC_GEOMETRY_TYPE_USER.4embree4.gz
