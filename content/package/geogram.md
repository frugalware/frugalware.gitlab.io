+++
draft = false
title = "geogram 1.7.9-1"
version = "1.7.9-1"
description = "Library of geometric algorithms. It includes a simple yet efficient Mesh data structure."
date = "2022-08-02T11:24:00"
aliases = "/packages/220122"
categories = ['lib-extra']
upstreamurl = "http://alice.loria.fr/software/geogram/doc/html/index.html"
arch = "x86_64"
size = "3567220"
usize = "14547074"
sha1sum = "75cf2535b216bf36f3fc61aad37b20f3f0f4a864"
depends = "['glfw', 'libglu', 'libxcursor', 'libxi', 'libxinerama', 'libxrandr', 'libxxf86vm']"
reverse_depends = "['alicevision']"
+++
### Description: 
Library of geometric algorithms. It includes a simple yet efficient Mesh data structure.

### Files: 
* /usr/include/geogram1/geogram/api/defs.h
* /usr/include/geogram1/geogram/basic/algorithm.h
* /usr/include/geogram1/geogram/basic/android_utils.h
* /usr/include/geogram1/geogram/basic/android_wrapper.h
* /usr/include/geogram1/geogram/basic/argused.h
* /usr/include/geogram1/geogram/basic/assert.h
* /usr/include/geogram1/geogram/basic/atomics.h
* /usr/include/geogram1/geogram/basic/attributes.h
* /usr/include/geogram1/geogram/basic/b_stream.h
* /usr/include/geogram1/geogram/basic/command_line.h
* /usr/include/geogram1/geogram/basic/command_line_args.h
* /usr/include/geogram1/geogram/basic/common.h
* /usr/include/geogram1/geogram/basic/counted.h
* /usr/include/geogram1/geogram/basic/environment.h
* /usr/include/geogram1/geogram/basic/factory.h
* /usr/include/geogram1/geogram/basic/file_system.h
* /usr/include/geogram1/geogram/basic/geofile.h
* /usr/include/geogram1/geogram/basic/geometry.h
* /usr/include/geogram1/geogram/basic/geometry_nd.h
* /usr/include/geogram1/geogram/basic/line_stream.h
* /usr/include/geogram1/geogram/basic/logger.h
* /usr/include/geogram1/geogram/basic/matrix.h
* /usr/include/geogram1/geogram/basic/memory.h
* /usr/include/geogram1/geogram/basic/numeric.h
* /usr/include/geogram1/geogram/basic/packed_arrays.h
* /usr/include/geogram1/geogram/basic/permutation.h
* /usr/include/geogram1/geogram/basic/process.h
* /usr/include/geogram1/geogram/basic/process_private.h
* /usr/include/geogram1/geogram/basic/progress.h
* /usr/include/geogram1/geogram/basic/psm.h
* /usr/include/geogram1/geogram/basic/quaternion.h
* /usr/include/geogram1/geogram/basic/range.h
* /usr/include/geogram1/geogram/basic/smart_pointer.h
* /usr/include/geogram1/geogram/basic/stopwatch.h
* /usr/include/geogram1/geogram/basic/string.h
* /usr/include/geogram1/geogram/basic/thread_sync.h
* /usr/include/geogram1/geogram/basic/vecg.h
* /usr/include/geogram1/geogram/bibliography/bibliography.h
* /usr/include/geogram1/geogram/delaunay/cavity.h
* /usr/include/geogram1/geogram/delaunay/delaunay.h
* /usr/include/geogram1/geogram/delaunay/delaunay_2d.h
* /usr/include/geogram1/geogram/delaunay/delaunay_3d.h
* /usr/include/geogram1/geogram/delaunay/delaunay_nn.h
* /usr/include/geogram1/geogram/delaunay/delaunay_tetgen.h
* /usr/include/geogram1/geogram/delaunay/delaunay_triangle.h
* /usr/include/geogram1/geogram/delaunay/LFS.h
* /usr/include/geogram1/geogram/delaunay/parallel_delaunay_3d.h
* /usr/include/geogram1/geogram/delaunay/periodic.h
* /usr/include/geogram1/geogram/delaunay/periodic_delaunay_3d.h
* /usr/include/geogram1/geogram/image/color.h
* /usr/include/geogram1/geogram/image/colormap.h
* /usr/include/geogram1/geogram/image/image.h
* /usr/include/geogram1/geogram/image/image_library.h
* /usr/include/geogram1/geogram/image/image_rasterizer.h
* /usr/include/geogram1/geogram/image/image_serializer.h
* /usr/include/geogram1/geogram/image/image_serializer_pgm.h
* /usr/include/geogram1/geogram/image/image_serializer_stb.h
* /usr/include/geogram1/geogram/image/image_serializer_xpm.h
* /usr/include/geogram1/geogram/image/morpho_math.h
* /usr/include/geogram1/geogram/lua/lua_io.h
* /usr/include/geogram1/geogram/lua/lua_wrap.h
* /usr/include/geogram1/geogram/mesh/index.h
* /usr/include/geogram1/geogram/mesh/mesh.h
* /usr/include/geogram1/geogram/mesh/mesh_AABB.h
* /usr/include/geogram1/geogram/mesh/mesh_baking.h
* /usr/include/geogram1/geogram/mesh/mesh_compare.h
* /usr/include/geogram1/geogram/mesh/mesh_decimate.h
* /usr/include/geogram1/geogram/mesh/mesh_degree3_vertices.h
* /usr/include/geogram1/geogram/mesh/mesh_distance.h
* /usr/include/geogram1/geogram/mesh/mesh_fill_holes.h
* /usr/include/geogram1/geogram/mesh/mesh_frame_field.h
* /usr/include/geogram1/geogram/mesh/mesh_geometry.h
* /usr/include/geogram1/geogram/mesh/mesh_halfedges.h
* /usr/include/geogram1/geogram/mesh/mesh_intersection.h
* /usr/include/geogram1/geogram/mesh/mesh_io.h
* /usr/include/geogram1/geogram/mesh/mesh_manifold_harmonics.h
* /usr/include/geogram1/geogram/mesh/mesh_partition.h
* /usr/include/geogram1/geogram/mesh/mesh_preprocessing.h
* /usr/include/geogram1/geogram/mesh/mesh_remesh.h
* /usr/include/geogram1/geogram/mesh/mesh_reorder.h
* /usr/include/geogram1/geogram/mesh/mesh_repair.h
* /usr/include/geogram1/geogram/mesh/mesh_sampling.h
* /usr/include/geogram1/geogram/mesh/mesh_smoothing.h
* /usr/include/geogram1/geogram/mesh/mesh_subdivision.h
* /usr/include/geogram1/geogram/mesh/mesh_tetrahedralize.h
* /usr/include/geogram1/geogram/mesh/mesh_topology.h
* /usr/include/geogram1/geogram/mesh/triangle_intersection.h
* /usr/include/geogram1/geogram/NL/nl.h
* /usr/include/geogram1/geogram/NL/nl_64.h
* /usr/include/geogram1/geogram/NL/nl_arpack.h
* /usr/include/geogram1/geogram/NL/nl_blas.h
* /usr/include/geogram1/geogram/NL/nl_cholmod.h
* /usr/include/geogram1/geogram/NL/nl_context.h
* /usr/include/geogram1/geogram/NL/nl_cuda.h
* /usr/include/geogram1/geogram/NL/nl_ext.h
* /usr/include/geogram1/geogram/NL/nl_iterative_solvers.h
* /usr/include/geogram1/geogram/NL/nl_linkage.h
* /usr/include/geogram1/geogram/NL/nl_matrix.h
* /usr/include/geogram1/geogram/NL/nl_mkl.h
* /usr/include/geogram1/geogram/NL/nl_preconditioners.h
* /usr/include/geogram1/geogram/NL/nl_private.h
* /usr/include/geogram1/geogram/NL/nl_superlu.h
* /usr/include/geogram1/geogram/numerics/expansion_nt.h
* /usr/include/geogram1/geogram/numerics/lbfgs_optimizers.h
* /usr/include/geogram1/geogram/numerics/matrix_util.h
* /usr/include/geogram1/geogram/numerics/multi_precision.h
* /usr/include/geogram1/geogram/numerics/optimizer.h
* /usr/include/geogram1/geogram/numerics/predicates.h
* /usr/include/geogram1/geogram/numerics/predicates/aligned3d.h
* /usr/include/geogram1/geogram/numerics/predicates/det3d.h
* /usr/include/geogram1/geogram/numerics/predicates/det4d.h
* /usr/include/geogram1/geogram/numerics/predicates/det_compare_4d.h
* /usr/include/geogram1/geogram/numerics/predicates/dot3d.h
* /usr/include/geogram1/geogram/numerics/predicates/dot_compare_3d.h
* /usr/include/geogram1/geogram/numerics/predicates/orient2d.h
* /usr/include/geogram1/geogram/numerics/predicates/orient3d.h
* /usr/include/geogram1/geogram/numerics/predicates/orient4d.h
* /usr/include/geogram1/geogram/numerics/predicates/side1.h
* /usr/include/geogram1/geogram/numerics/predicates/side2.h
* /usr/include/geogram1/geogram/numerics/predicates/side3.h
* /usr/include/geogram1/geogram/numerics/predicates/side3h.h
* /usr/include/geogram1/geogram/numerics/predicates/side3_2dlifted.h
* /usr/include/geogram1/geogram/numerics/predicates/side4.h
* /usr/include/geogram1/geogram/numerics/predicates/side4h.h
* /usr/include/geogram1/geogram/parameterization/mesh_ABF.h
* /usr/include/geogram1/geogram/parameterization/mesh_atlas_maker.h
* /usr/include/geogram1/geogram/parameterization/mesh_global_param.h
* /usr/include/geogram1/geogram/parameterization/mesh_LSCM.h
* /usr/include/geogram1/geogram/parameterization/mesh_param_packer.h
* /usr/include/geogram1/geogram/parameterization/mesh_param_validator.h
* /usr/include/geogram1/geogram/parameterization/mesh_PGP_2d.h
* /usr/include/geogram1/geogram/parameterization/mesh_segmentation.h
* /usr/include/geogram1/geogram/points/co3ne.h
* /usr/include/geogram1/geogram/points/colocate.h
* /usr/include/geogram1/geogram/points/kd_tree.h
* /usr/include/geogram1/geogram/points/nn_search.h
* /usr/include/geogram1/geogram/points/principal_axes.h
* /usr/include/geogram1/geogram/third_party/HLBFGS/HLBFGS.h
* /usr/include/geogram1/geogram/third_party/HLBFGS/HLBFGS_BLAS.h
* /usr/include/geogram1/geogram/third_party/HLBFGS/ICFS.h
* /usr/include/geogram1/geogram/third_party/HLBFGS/LineSearch.h
* /usr/include/geogram1/geogram/third_party/HLBFGS/Lite_Sparse_Matrix.h
* /usr/include/geogram1/geogram/third_party/HLBFGS/Sparse_Entry.h
* /usr/include/geogram1/geogram/third_party/LM7/libmeshb7.h
* /usr/include/geogram1/geogram/third_party/lua/lapi.h
* /usr/include/geogram1/geogram/third_party/lua/lauxlib.h
* /usr/include/geogram1/geogram/third_party/lua/lcode.h
* /usr/include/geogram1/geogram/third_party/lua/lctype.h
* /usr/include/geogram1/geogram/third_party/lua/ldebug.h
* /usr/include/geogram1/geogram/third_party/lua/ldo.h
* /usr/include/geogram1/geogram/third_party/lua/lfunc.h
* /usr/include/geogram1/geogram/third_party/lua/lgc.h
* /usr/include/geogram1/geogram/third_party/lua/llex.h
* /usr/include/geogram1/geogram/third_party/lua/llimits.h
* /usr/include/geogram1/geogram/third_party/lua/lmem.h
* /usr/include/geogram1/geogram/third_party/lua/lobject.h
* /usr/include/geogram1/geogram/third_party/lua/lopcodes.h
* /usr/include/geogram1/geogram/third_party/lua/lparser.h
* /usr/include/geogram1/geogram/third_party/lua/lprefix.h
* /usr/include/geogram1/geogram/third_party/lua/lstate.h
* /usr/include/geogram1/geogram/third_party/lua/lstring.h
* /usr/include/geogram1/geogram/third_party/lua/ltable.h
* /usr/include/geogram1/geogram/third_party/lua/ltm.h
* /usr/include/geogram1/geogram/third_party/lua/lua.h
* /usr/include/geogram1/geogram/third_party/lua/luaconf.h
* /usr/include/geogram1/geogram/third_party/lua/lualib.h
* /usr/include/geogram1/geogram/third_party/lua/lundump.h
* /usr/include/geogram1/geogram/third_party/lua/lvm.h
* /usr/include/geogram1/geogram/third_party/lua/lzio.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/Allocator.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/Array.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/BinaryNode.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/BSplineData.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/Factor.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/FunctionData.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/Geometry.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/Hash.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/MarchingCubes.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/MAT.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/MemoryUsage.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/MultiGridOctreeData.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/MyTime.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/Octree.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/PlyVertexMini.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/PointStream.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/poisson_geogram.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/Polynomial.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/PPolynomial.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/SparseMatrix.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/unused/CmdLineParser.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/unused/Ply.h
* /usr/include/geogram1/geogram/third_party/PoissonRecon/unused/PlyPointStream.h
* /usr/include/geogram1/geogram/third_party/pstdint.h
* /usr/include/geogram1/geogram/third_party/rply/rply.h
* /usr/include/geogram1/geogram/third_party/rply/rplyfile.h
* /usr/include/geogram1/geogram/third_party/stb_image/stb_image.h
* /usr/include/geogram1/geogram/third_party/stb_image/stb_image_write.h
* /usr/include/geogram1/geogram/third_party/tetgen/tetgen.h
* /usr/include/geogram1/geogram/third_party/triangle/triangle.h
* /usr/include/geogram1/geogram/third_party/xatlas/xatlas.h
* /usr/include/geogram1/geogram/third_party/zlib/crc32.h
* /usr/include/geogram1/geogram/third_party/zlib/deflate.h
* /usr/include/geogram1/geogram/third_party/zlib/gzguts.h
* /usr/include/geogram1/geogram/third_party/zlib/inffast.h
* /usr/include/geogram1/geogram/third_party/zlib/inffixed.h
* /usr/include/geogram1/geogram/third_party/zlib/inflate.h
* /usr/include/geogram1/geogram/third_party/zlib/inftrees.h
* /usr/include/geogram1/geogram/third_party/zlib/trees.h
* /usr/include/geogram1/geogram/third_party/zlib/zconf.h
* /usr/include/geogram1/geogram/third_party/zlib/zlib.h
* /usr/include/geogram1/geogram/third_party/zlib/zutil.h
* /usr/include/geogram1/geogram/voronoi/convex_cell.h
* /usr/include/geogram1/geogram/voronoi/CVT.h
* /usr/include/geogram1/geogram/voronoi/generic_RVD.h
* /usr/include/geogram1/geogram/voronoi/generic_RVD_cell.h
* /usr/include/geogram1/geogram/voronoi/generic_RVD_polygon.h
* /usr/include/geogram1/geogram/voronoi/generic_RVD_utils.h
* /usr/include/geogram1/geogram/voronoi/generic_RVD_vertex.h
* /usr/include/geogram1/geogram/voronoi/integration_simplex.h
* /usr/include/geogram1/geogram/voronoi/RVD.h
* /usr/include/geogram1/geogram/voronoi/RVD_callback.h
* /usr/include/geogram1/geogram/voronoi/RVD_mesh_builder.h
* /usr/include/geogram1/geogram_gfx/api/defs.h
* /usr/include/geogram1/geogram_gfx/basic/common.h
* /usr/include/geogram1/geogram_gfx/basic/frame_buffer_object.h
* /usr/include/geogram1/geogram_gfx/basic/GL.h
* /usr/include/geogram1/geogram_gfx/basic/GLSL.h
* /usr/include/geogram1/geogram_gfx/full_screen_effects/ambient_occlusion.h
* /usr/include/geogram1/geogram_gfx/full_screen_effects/full_screen_effect.h
* /usr/include/geogram1/geogram_gfx/full_screen_effects/unsharp_masking.h
* /usr/include/geogram1/geogram_gfx/GLUP/GLUP.h
* /usr/include/geogram1/geogram_gfx/GLUP/GLUP_context.h
* /usr/include/geogram1/geogram_gfx/GLUP/GLUP_context_ES.h
* /usr/include/geogram1/geogram_gfx/GLUP/GLUP_context_GLSL.h
* /usr/include/geogram1/geogram_gfx/GLUP/GLUP_marching_cells.h
* /usr/include/geogram1/geogram_gfx/GLUP/GLUP_private.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/embedded_shaders.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/fullscreen/ambient_occlusion_fragment_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/fullscreen/blur_fragment_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/fullscreen/depth_dependent_blur_fragment_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/fullscreen/unsharp_masking_fragment_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/fullscreen/vertex_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUP/constants.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUP/defs.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUP/fragment_ray_tracing.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUP/fragment_shader_utils.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUP/portable_fragment_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUP/ShaderToy.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUP/stdglup.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPES/fragment_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPES/fragment_shader_state.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPES/fragment_shader_utils.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPES/lines_fragment_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPES/points_fragment_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPES/points_vertex_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPES/spheres_fragment_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPES/spheres_vertex_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPES/vertex_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPES/vertex_shader_state.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPGLSL/fragment_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPGLSL/gather_vertex_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPGLSL/geometry_shader_preamble.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPGLSL/lines_fragment_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPGLSL/marching_cells.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPGLSL/points_fragment_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPGLSL/points_vertex_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPGLSL/spheres_fragment_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPGLSL/spheres_vertex_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPGLSL/state.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPGLSL/tess_evaluation_shader.h
* /usr/include/geogram1/geogram_gfx/GLUP/shaders/GLUPGLSL/vertex_shader.h
* /usr/include/geogram1/geogram_gfx/gui/application.h
* /usr/include/geogram1/geogram_gfx/gui/arc_ball.h
* /usr/include/geogram1/geogram_gfx/gui/command.h
* /usr/include/geogram1/geogram_gfx/gui/console.h
* /usr/include/geogram1/geogram_gfx/gui/events.h
* /usr/include/geogram1/geogram_gfx/gui/gui_state.h
* /usr/include/geogram1/geogram_gfx/gui/gui_state_h.h
* /usr/include/geogram1/geogram_gfx/gui/gui_state_v.h
* /usr/include/geogram1/geogram_gfx/gui/simple_application.h
* /usr/include/geogram1/geogram_gfx/gui/simple_mesh_application.h
* /usr/include/geogram1/geogram_gfx/gui/status_bar.h
* /usr/include/geogram1/geogram_gfx/gui/text_editor.h
* /usr/include/geogram1/geogram_gfx/ImGui_ext/icon_font.h
* /usr/include/geogram1/geogram_gfx/ImGui_ext/imgui_ext.h
* /usr/include/geogram1/geogram_gfx/lua/lua_glup.h
* /usr/include/geogram1/geogram_gfx/lua/lua_imgui.h
* /usr/include/geogram1/geogram_gfx/lua/lua_simple_application.h
* /usr/include/geogram1/geogram_gfx/mesh/mesh_gfx.h
* /usr/include/geogram1/geogram_gfx/third_party/glad/glad.h
* /usr/include/geogram1/geogram_gfx/third_party/glad/KHR/khrplatform.h
* /usr/include/geogram1/geogram_gfx/third_party/ImGui/glup_compat.h
* /usr/include/geogram1/geogram_gfx/third_party/ImGui/imconfig.h
* /usr/include/geogram1/geogram_gfx/third_party/ImGui/imgui.h
* /usr/include/geogram1/geogram_gfx/third_party/ImGui/imgui_impl_android.h
* /usr/include/geogram1/geogram_gfx/third_party/ImGui/imgui_impl_glfw.h
* /usr/include/geogram1/geogram_gfx/third_party/ImGui/imgui_impl_opengl3.h
* /usr/include/geogram1/geogram_gfx/third_party/ImGui/imgui_impl_win32.h
* /usr/include/geogram1/geogram_gfx/third_party/ImGui/imgui_internal.h
* /usr/include/geogram1/geogram_gfx/third_party/ImGui/imstb_rectpack.h
* /usr/include/geogram1/geogram_gfx/third_party/ImGui/imstb_textedit.h
* /usr/include/geogram1/geogram_gfx/third_party/ImGui/imstb_truetype.h
* /usr/include/geogram1/geogram_gfx/third_party/ImGuiColorTextEdit/TextEditor.h
* /usr/include/geogram1/geogram_gfx/third_party/imgui_fonts/cousine_regular.h
* /usr/include/geogram1/geogram_gfx/third_party/imgui_fonts/fa_brands.h
* /usr/include/geogram1/geogram_gfx/third_party/imgui_fonts/fa_regular.h
* /usr/include/geogram1/geogram_gfx/third_party/imgui_fonts/fa_solid.h
* /usr/include/geogram1/geogram_gfx/third_party/imgui_fonts/roboto_medium.h
* /usr/include/geogram1/geogram_gfx/third_party/imgui_lua_bindings/imgui_iterator.h
* /usr/lib/cmake/modules/FindGeogram.cmake
* /usr/lib/libgeogram.so
* /usr/lib/libgeogram.so.1
* /usr/lib/libgeogram.so.1.7.9
* /usr/lib/libgeogram_gfx.so
* /usr/lib/libgeogram_gfx.so.1
* /usr/lib/libgeogram_gfx.so.1.7.9
* /usr/lib/libgeogram_num_3rdparty.so
* /usr/lib/libgeogram_num_3rdparty.so.1
* /usr/lib/libgeogram_num_3rdparty.so.1.7.9
* /usr/lib/pkgconfig/geogram1.pc
* /usr/lib/pkgconfig/geogram_gfx1.pc
* /usr/share/doc/geogram-1.7.9/geogram/VERSION.txt
* /usr/share/doc/geogram-1.7.9/LICENSE
* /usr/share/doc/geogram-1.7.9/README.md
