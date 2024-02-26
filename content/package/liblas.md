+++
draft = false
title = "liblas 1.8.1-4"
version = "1.8.1-4"
description = "C/C++ library for reading and writing the very common LAS LiDAR format"
date = "2023-09-05T22:00:45"
aliases = "/packages/220258"
categories = ['lib-extra']
upstreamurl = "https://www.liblas.org"
arch = "x86_64"
size = "612036"
usize = "3154325"
sha1sum = "98df635eabbac74c6a91c9ea6295e1dd0ca7be8c"
depends = "['gdal', 'libboost>=1.83.0', 'libgeotiff']"
reverse_depends = "['vtk']"
+++
C/C++ library for reading and writing the very common LAS LiDAR format"

{{< files text="show files" >}}* /usr/bin/las2col
* /usr/bin/las2las
* /usr/bin/las2pg
* /usr/bin/las2txt
* /usr/bin/lasblock
* /usr/bin/lasinfo
* /usr/bin/liblas-config
* /usr/bin/ts2las
* /usr/bin/txt2las
* /usr/include/liblas/bounds.hpp
* /usr/include/liblas/capi/las_config.h
* /usr/include/liblas/capi/las_version.h
* /usr/include/liblas/capi/liblas.h
* /usr/include/liblas/chipper.hpp
* /usr/include/liblas/classification.hpp
* /usr/include/liblas/color.hpp
* /usr/include/liblas/compatibility.hpp
* /usr/include/liblas/detail/binary.hpp
* /usr/include/liblas/detail/endian.hpp
* /usr/include/liblas/detail/file_ptr_stream.hpp
* /usr/include/liblas/detail/fwd.hpp
* /usr/include/liblas/detail/index/indexcell.hpp
* /usr/include/liblas/detail/index/indexoutput.hpp
* /usr/include/liblas/detail/opt_allocator.hpp
* /usr/include/liblas/detail/pointrecord.hpp
* /usr/include/liblas/detail/private_utility.hpp
* /usr/include/liblas/detail/reader/cachedreader.hpp
* /usr/include/liblas/detail/reader/header.hpp
* /usr/include/liblas/detail/reader/reader.hpp
* /usr/include/liblas/detail/reader/zipreader.hpp
* /usr/include/liblas/detail/sha1.hpp
* /usr/include/liblas/detail/singleton.hpp
* /usr/include/liblas/detail/timer.hpp
* /usr/include/liblas/detail/writer/header.hpp
* /usr/include/liblas/detail/writer/point.hpp
* /usr/include/liblas/detail/writer/writer.hpp
* /usr/include/liblas/detail/writer/zipwriter.hpp
* /usr/include/liblas/detail/zippoint.hpp
* /usr/include/liblas/dimension.hpp
* /usr/include/liblas/error.hpp
* /usr/include/liblas/exception.hpp
* /usr/include/liblas/export.hpp
* /usr/include/liblas/external/property_tree/detail/exception_implementation.hpp
* /usr/include/liblas/external/property_tree/detail/file_parser_error.hpp
* /usr/include/liblas/external/property_tree/detail/info_parser_error.hpp
* /usr/include/liblas/external/property_tree/detail/info_parser_read.hpp
* /usr/include/liblas/external/property_tree/detail/info_parser_utils.hpp
* /usr/include/liblas/external/property_tree/detail/info_parser_write.hpp
* /usr/include/liblas/external/property_tree/detail/info_parser_writer_settings.hpp
* /usr/include/liblas/external/property_tree/detail/json_parser_error.hpp
* /usr/include/liblas/external/property_tree/detail/json_parser_read.hpp
* /usr/include/liblas/external/property_tree/detail/json_parser_write.hpp
* /usr/include/liblas/external/property_tree/detail/ptree_implementation.hpp
* /usr/include/liblas/external/property_tree/detail/ptree_utils.hpp
* /usr/include/liblas/external/property_tree/detail/rapidxml.hpp
* /usr/include/liblas/external/property_tree/detail/xml_parser_error.hpp
* /usr/include/liblas/external/property_tree/detail/xml_parser_flags.hpp
* /usr/include/liblas/external/property_tree/detail/xml_parser_read_rapidxml.hpp
* /usr/include/liblas/external/property_tree/detail/xml_parser_utils.hpp
* /usr/include/liblas/external/property_tree/detail/xml_parser_write.hpp
* /usr/include/liblas/external/property_tree/detail/xml_parser_writer_settings.hpp
* /usr/include/liblas/external/property_tree/exceptions.hpp
* /usr/include/liblas/external/property_tree/id_translator.hpp
* /usr/include/liblas/external/property_tree/info_parser.hpp
* /usr/include/liblas/external/property_tree/ini_parser.hpp
* /usr/include/liblas/external/property_tree/json_parser.hpp
* /usr/include/liblas/external/property_tree/ptree.hpp
* /usr/include/liblas/external/property_tree/ptree_fwd.hpp
* /usr/include/liblas/external/property_tree/ptree_serialization.hpp
* /usr/include/liblas/external/property_tree/stream_translator.hpp
* /usr/include/liblas/external/property_tree/string_path.hpp
* /usr/include/liblas/external/property_tree/xml_parser.hpp
* /usr/include/liblas/factory.hpp
* /usr/include/liblas/filter.hpp
* /usr/include/liblas/header.hpp
* /usr/include/liblas/index.hpp
* /usr/include/liblas/iterator.hpp
* /usr/include/liblas/liblas.hpp
* /usr/include/liblas/point.hpp
* /usr/include/liblas/reader.hpp
* /usr/include/liblas/schema.hpp
* /usr/include/liblas/spatialreference.hpp
* /usr/include/liblas/transform.hpp
* /usr/include/liblas/utility.hpp
* /usr/include/liblas/variablerecord.hpp
* /usr/include/liblas/version.hpp
* /usr/include/liblas/writer.hpp
* /usr/lib/liblas.so
* /usr/lib/liblas.so.2.4.0
* /usr/lib/liblas.so.3
* /usr/lib/liblas_c.so
* /usr/lib/liblas_c.so.2.4.0
* /usr/lib/liblas_c.so.3
* /usr/share/cmake/libLAS/liblas-config-version.cmake
* /usr/share/cmake/libLAS/liblas-config.cmake
* /usr/share/cmake/libLAS/liblas-depends-release.cmake
* /usr/share/cmake/libLAS/liblas-depends.cmake
* /usr/share/doc/liblas-1.8.1/AUTHORS
* /usr/share/doc/liblas-1.8.1/COPYING
* /usr/share/doc/liblas-1.8.1/HOWTORELEASE.txt
* /usr/share/doc/liblas-1.8.1/INSTALL
* /usr/share/doc/liblas-1.8.1/NEWS
* /usr/share/doc/liblas-1.8.1/README.txt
* /usr/share/liblas/doc/AUTHORS
* /usr/share/liblas/doc/COPYING
* /usr/share/liblas/doc/INSTALL
* /usr/share/liblas/doc/LICENSE.txt
* /usr/share/liblas/doc/README.txt
{{< /files >}}