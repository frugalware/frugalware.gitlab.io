+++
draft = false
title = "alembic 1.8.5-1"
version = "1.8.5-1"
date = "2023-06-06T19:55:46"
categories = ['lib-extra']
upstreamurl = "http://www.alembic.io"
arch = "x86_64"
size = "753564"
usize = "3290056"
sha1sum = "f72c2f172dfe2c7fd1c7de20ec12ec2ceaf5bc75"
depends = "['hdf5', 'libboost', 'imath>=3.1.9']"
files = "['usr/', 'usr/bin/', 'usr/bin/abcconvert', 'usr/bin/abcdiff', 'usr/bin/abcecho', 'usr/bin/abcechobounds', 'usr/bin/abcls', 'usr/bin/abcstitcher', 'usr/bin/abctree', 'usr/include/', 'usr/include/Alembic/', 'usr/include/Alembic/Abc/', 'usr/include/Alembic/Abc/All.h', 'usr/include/Alembic/Abc/ArchiveInfo.h', 'usr/include/Alembic/Abc/Argument.h', 'usr/include/Alembic/Abc/Base.h', 'usr/include/Alembic/Abc/ErrorHandler.h', 'usr/include/Alembic/Abc/Foundation.h', 'usr/include/Alembic/Abc/IArchive.h', 'usr/include/Alembic/Abc/IArrayProperty.h', 'usr/include/Alembic/Abc/IBaseProperty.h', 'usr/include/Alembic/Abc/ICompoundProperty.h', 'usr/include/Alembic/Abc/IObject.h', 'usr/include/Alembic/Abc/ISampleSelector.h', 'usr/include/Alembic/Abc/IScalarProperty.h', 'usr/include/Alembic/Abc/ISchema.h', 'usr/include/Alembic/Abc/ISchemaObject.h', 'usr/include/Alembic/Abc/ITypedArrayProperty.h', 'usr/include/Alembic/Abc/ITypedScalarProperty.h', 'usr/include/Alembic/Abc/OArchive.h', 'usr/include/Alembic/Abc/OArrayProperty.h', 'usr/include/Alembic/Abc/OBaseProperty.h', 'usr/include/Alembic/Abc/OCompoundProperty.h', 'usr/include/Alembic/Abc/OObject.h', 'usr/include/Alembic/Abc/OScalarProperty.h', 'usr/include/Alembic/Abc/OSchema.h', 'usr/include/Alembic/Abc/OSchemaObject.h', 'usr/include/Alembic/Abc/OTypedArrayProperty.h', 'usr/include/Alembic/Abc/OTypedScalarProperty.h', 'usr/include/Alembic/Abc/Reference.h', 'usr/include/Alembic/Abc/SourceName.h', 'usr/include/Alembic/Abc/TypedArraySample.h', 'usr/include/Alembic/Abc/TypedPropertyTraits.h', 'usr/include/Alembic/AbcCollection/', 'usr/include/Alembic/AbcCollection/All.h', 'usr/include/Alembic/AbcCollection/ICollections.h', 'usr/include/Alembic/AbcCollection/OCollections.h', 'usr/include/Alembic/AbcCollection/SchemaInfoDeclarations.h', 'usr/include/Alembic/AbcCoreAbstract/', 'usr/include/Alembic/AbcCoreAbstract/All.h', 'usr/include/Alembic/AbcCoreAbstract/ArchiveReader.h', 'usr/include/Alembic/AbcCoreAbstract/ArchiveWriter.h', 'usr/include/Alembic/AbcCoreAbstract/ArrayPropertyReader.h', 'usr/include/Alembic/AbcCoreAbstract/ArrayPropertyWriter.h', 'usr/include/Alembic/AbcCoreAbstract/ArraySample.h', 'usr/include/Alembic/AbcCoreAbstract/ArraySampleKey.h', 'usr/include/Alembic/AbcCoreAbstract/BasePropertyReader.h', 'usr/include/Alembic/AbcCoreAbstract/BasePropertyWriter.h', 'usr/include/Alembic/AbcCoreAbstract/CompoundPropertyReader.h', 'usr/include/Alembic/AbcCoreAbstract/CompoundPropertyWriter.h', 'usr/include/Alembic/AbcCoreAbstract/DataType.h', 'usr/include/Alembic/AbcCoreAbstract/ForwardDeclarations.h', 'usr/include/Alembic/AbcCoreAbstract/Foundation.h', 'usr/include/Alembic/AbcCoreAbstract/MetaData.h', 'usr/include/Alembic/AbcCoreAbstract/ObjectHeader.h', 'usr/include/Alembic/AbcCoreAbstract/ObjectReader.h', 'usr/include/Alembic/AbcCoreAbstract/ObjectWriter.h', 'usr/include/Alembic/AbcCoreAbstract/PropertyHeader.h', 'usr/include/Alembic/AbcCoreAbstract/ReadArraySampleCache.h', 'usr/include/Alembic/AbcCoreAbstract/ScalarPropertyReader.h', 'usr/include/Alembic/AbcCoreAbstract/ScalarPropertyWriter.h', 'usr/include/Alembic/AbcCoreAbstract/ScalarSample.h', 'usr/include/Alembic/AbcCoreAbstract/TimeSampling.h', 'usr/include/Alembic/AbcCoreAbstract/TimeSamplingType.h', 'usr/include/Alembic/AbcCoreFactory/', 'usr/include/Alembic/AbcCoreFactory/All.h', 'usr/include/Alembic/AbcCoreFactory/IFactory.h', 'usr/include/Alembic/AbcCoreHDF5/', 'usr/include/Alembic/AbcCoreHDF5/All.h', 'usr/include/Alembic/AbcCoreHDF5/ReadWrite.h', 'usr/include/Alembic/AbcCoreLayer/', 'usr/include/Alembic/AbcCoreLayer/Foundation.h', 'usr/include/Alembic/AbcCoreLayer/Read.h', 'usr/include/Alembic/AbcCoreLayer/Util.h', 'usr/include/Alembic/AbcCoreOgawa/', 'usr/include/Alembic/AbcCoreOgawa/All.h', 'usr/include/Alembic/AbcCoreOgawa/ReadWrite.h', 'usr/include/Alembic/AbcGeom/', 'usr/include/Alembic/AbcGeom/All.h', 'usr/include/Alembic/AbcGeom/ArchiveBounds.h', 'usr/include/Alembic/AbcGeom/Basis.h', 'usr/include/Alembic/AbcGeom/CameraSample.h', 'usr/include/Alembic/AbcGeom/CurveType.h', 'usr/include/Alembic/AbcGeom/FaceSetExclusivity.h', 'usr/include/Alembic/AbcGeom/FilmBackXformOp.h', 'usr/include/Alembic/AbcGeom/Foundation.h', 'usr/include/Alembic/AbcGeom/GeometryScope.h', 'usr/include/Alembic/AbcGeom/ICamera.h', 'usr/include/Alembic/AbcGeom/ICurves.h', 'usr/include/Alembic/AbcGeom/IFaceSet.h', 'usr/include/Alembic/AbcGeom/IGeomBase.h', 'usr/include/Alembic/AbcGeom/IGeomParam.h', 'usr/include/Alembic/AbcGeom/ILight.h', 'usr/include/Alembic/AbcGeom/INuPatch.h', 'usr/include/Alembic/AbcGeom/IPoints.h', 'usr/include/Alembic/AbcGeom/IPolyMesh.h', 'usr/include/Alembic/AbcGeom/ISubD.h', 'usr/include/Alembic/AbcGeom/IXform.h', 'usr/include/Alembic/AbcGeom/OCamera.h', 'usr/include/Alembic/AbcGeom/OCurves.h', 'usr/include/Alembic/AbcGeom/OFaceSet.h', 'usr/include/Alembic/AbcGeom/OGeomBase.h', 'usr/include/Alembic/AbcGeom/OGeomParam.h', 'usr/include/Alembic/AbcGeom/OLight.h', 'usr/include/Alembic/AbcGeom/ONuPatch.h', 'usr/include/Alembic/AbcGeom/OPoints.h', 'usr/include/Alembic/AbcGeom/OPolyMesh.h', 'usr/include/Alembic/AbcGeom/OSubD.h', 'usr/include/Alembic/AbcGeom/OXform.h', 'usr/include/Alembic/AbcGeom/SchemaInfoDeclarations.h', 'usr/include/Alembic/AbcGeom/Visibility.h', 'usr/include/Alembic/AbcGeom/XformOp.h', 'usr/include/Alembic/AbcGeom/XformSample.h', 'usr/include/Alembic/AbcMaterial/', 'usr/include/Alembic/AbcMaterial/All.h', 'usr/include/Alembic/AbcMaterial/IMaterial.h', 'usr/include/Alembic/AbcMaterial/MaterialAssignment.h', 'usr/include/Alembic/AbcMaterial/MaterialFlatten.h', 'usr/include/Alembic/AbcMaterial/OMaterial.h', 'usr/include/Alembic/AbcMaterial/SchemaInfoDeclarations.h', 'usr/include/Alembic/Util/', 'usr/include/Alembic/Util/All.h', 'usr/include/Alembic/Util/Config.h', 'usr/include/Alembic/Util/Digest.h', 'usr/include/Alembic/Util/Dimensions.h', 'usr/include/Alembic/Util/Exception.h', 'usr/include/Alembic/Util/Export.h', 'usr/include/Alembic/Util/Foundation.h', 'usr/include/Alembic/Util/Murmur3.h', 'usr/include/Alembic/Util/Naming.h', 'usr/include/Alembic/Util/OperatorBool.h', 'usr/include/Alembic/Util/PlainOldDataType.h', 'usr/include/Alembic/Util/SpookyV2.h', 'usr/include/Alembic/Util/TokenMap.h', 'usr/lib/', 'usr/lib/cmake/', 'usr/lib/cmake/Alembic/', 'usr/lib/cmake/Alembic/AlembicConfig.cmake', 'usr/lib/cmake/Alembic/AlembicConfigVersion.cmake', 'usr/lib/cmake/Alembic/AlembicTargets-release.cmake', 'usr/lib/cmake/Alembic/AlembicTargets.cmake', 'usr/lib/libAlembic.so', 'usr/lib/libAlembic.so.1.8', 'usr/lib/libAlembic.so.1.8.5', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/alembic-1.8.5/', 'usr/share/doc/alembic-1.8.5/README.txt']"
+++
A open framework for storing and sharing scene data