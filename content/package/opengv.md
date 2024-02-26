+++
draft = false
title = "opengv 20230906-1"
version = "20230906-1"
description = "An efficient C++ library for calibrated camera pose computation using geometric computer vision algorithms."
date = "2023-09-06T13:48:46"
aliases = "/packages/220129"
categories = ['lib-extra']
upstreamurl = "https://github.com/laurentkneip/opengv"
arch = "x86_64"
size = "30364320"
usize = "47662024"
sha1sum = "5748312f2a89b4cc5a9c7de08155268cc45cd13e"
depends = "['eigen', 'libboost>=1.83']"
reverse_depends = "['alicevision']"
+++
An efficient C++ library for calibrated camera pose computation using geometric computer vision algorithms."

{{< files text="show files" >}}* /usr/include/opengv/absolute_pose/AbsoluteAdapterBase.hpp
* /usr/include/opengv/absolute_pose/AbsoluteMultiAdapterBase.hpp
* /usr/include/opengv/absolute_pose/CentralAbsoluteAdapter.hpp
* /usr/include/opengv/absolute_pose/MACentralAbsolute.hpp
* /usr/include/opengv/absolute_pose/MANoncentralAbsolute.hpp
* /usr/include/opengv/absolute_pose/methods.hpp
* /usr/include/opengv/absolute_pose/modules/Epnp.hpp
* /usr/include/opengv/absolute_pose/modules/gp3p/modules.hpp
* /usr/include/opengv/absolute_pose/modules/gpnp1/modules.hpp
* /usr/include/opengv/absolute_pose/modules/gpnp2/modules.hpp
* /usr/include/opengv/absolute_pose/modules/gpnp3/modules.hpp
* /usr/include/opengv/absolute_pose/modules/gpnp4/modules.hpp
* /usr/include/opengv/absolute_pose/modules/gpnp5/modules.hpp
* /usr/include/opengv/absolute_pose/modules/main.hpp
* /usr/include/opengv/absolute_pose/modules/upnp2.hpp
* /usr/include/opengv/absolute_pose/modules/upnp4.hpp
* /usr/include/opengv/absolute_pose/NoncentralAbsoluteAdapter.hpp
* /usr/include/opengv/absolute_pose/NoncentralAbsoluteMultiAdapter.hpp
* /usr/include/opengv/Indices.hpp
* /usr/include/opengv/math/arun.hpp
* /usr/include/opengv/math/cayley.hpp
* /usr/include/opengv/math/gauss_jordan.hpp
* /usr/include/opengv/math/quaternion.hpp
* /usr/include/opengv/math/roots.hpp
* /usr/include/opengv/math/Sturm.hpp
* /usr/include/opengv/OptimizationFunctor.hpp
* /usr/include/opengv/point_cloud/MAPointCloud.hpp
* /usr/include/opengv/point_cloud/methods.hpp
* /usr/include/opengv/point_cloud/PointCloudAdapter.hpp
* /usr/include/opengv/point_cloud/PointCloudAdapterBase.hpp
* /usr/include/opengv/relative_pose/CentralRelativeAdapter.hpp
* /usr/include/opengv/relative_pose/CentralRelativeMultiAdapter.hpp
* /usr/include/opengv/relative_pose/CentralRelativeWeightingAdapter.hpp
* /usr/include/opengv/relative_pose/MACentralRelative.hpp
* /usr/include/opengv/relative_pose/MANoncentralRelative.hpp
* /usr/include/opengv/relative_pose/MANoncentralRelativeMulti.hpp
* /usr/include/opengv/relative_pose/methods.hpp
* /usr/include/opengv/relative_pose/modules/eigensolver/modules.hpp
* /usr/include/opengv/relative_pose/modules/fivept_kneip/modules.hpp
* /usr/include/opengv/relative_pose/modules/fivept_nister/modules.hpp
* /usr/include/opengv/relative_pose/modules/fivept_stewenius/modules.hpp
* /usr/include/opengv/relative_pose/modules/ge/modules.hpp
* /usr/include/opengv/relative_pose/modules/main.hpp
* /usr/include/opengv/relative_pose/modules/sixpt/modules.hpp
* /usr/include/opengv/relative_pose/NoncentralRelativeAdapter.hpp
* /usr/include/opengv/relative_pose/NoncentralRelativeMultiAdapter.hpp
* /usr/include/opengv/relative_pose/RelativeAdapterBase.hpp
* /usr/include/opengv/relative_pose/RelativeMultiAdapterBase.hpp
* /usr/include/opengv/sac/implementation/Lmeds.hpp
* /usr/include/opengv/sac/implementation/MultiRansac.hpp
* /usr/include/opengv/sac/implementation/MultiSampleConsensus.hpp
* /usr/include/opengv/sac/implementation/MultiSampleConsensusProblem.hpp
* /usr/include/opengv/sac/implementation/Ransac.hpp
* /usr/include/opengv/sac/implementation/SampleConsensus.hpp
* /usr/include/opengv/sac/implementation/SampleConsensusProblem.hpp
* /usr/include/opengv/sac/Lmeds.hpp
* /usr/include/opengv/sac/MultiRansac.hpp
* /usr/include/opengv/sac/MultiSampleConsensus.hpp
* /usr/include/opengv/sac/MultiSampleConsensusProblem.hpp
* /usr/include/opengv/sac/Ransac.hpp
* /usr/include/opengv/sac/SampleConsensus.hpp
* /usr/include/opengv/sac/SampleConsensusProblem.hpp
* /usr/include/opengv/sac_problems/absolute_pose/AbsolutePoseSacProblem.hpp
* /usr/include/opengv/sac_problems/absolute_pose/MultiNoncentralAbsolutePoseSacProblem.hpp
* /usr/include/opengv/sac_problems/point_cloud/PointCloudSacProblem.hpp
* /usr/include/opengv/sac_problems/relative_pose/CentralRelativePoseSacProblem.hpp
* /usr/include/opengv/sac_problems/relative_pose/EigensolverSacProblem.hpp
* /usr/include/opengv/sac_problems/relative_pose/MultiCentralRelativePoseSacProblem.hpp
* /usr/include/opengv/sac_problems/relative_pose/MultiNoncentralRelativePoseSacProblem.hpp
* /usr/include/opengv/sac_problems/relative_pose/NoncentralRelativePoseSacProblem.hpp
* /usr/include/opengv/sac_problems/relative_pose/RotationOnlySacProblem.hpp
* /usr/include/opengv/sac_problems/relative_pose/TranslationOnlySacProblem.hpp
* /usr/include/opengv/triangulation/methods.hpp
* /usr/include/opengv/types.hpp
* /usr/lib/cmake/opengv-1.0/opengvConfig.cmake
* /usr/lib/cmake/opengv-1.0/opengvConfigVersion.cmake
* /usr/lib/cmake/opengv-1.0/opengvTargets-release.cmake
* /usr/lib/cmake/opengv-1.0/opengvTargets.cmake
* /usr/lib/libopengv.a
* /usr/share/doc/opengv-20230906/README.txt
{{< /files >}}