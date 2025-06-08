+++
draft = false
title = "polly 19.1.7-3"
version = "19.1.7-3"
description = "High-level loop and data-locality optimizer and optimization infrastructure for LLVM"
date = "2025-06-04T08:54:43"
aliases = "/packages/220521"
categories = ['devel-extra']
upstreamurl = "http://www.llvm.org"
arch = "x86_64"
size = "2931864"
usize = "18548152"
sha1sum = "02ce2c83e7ec9f386e1632c0ef1f5958ffea8053"
depends = "['llvm-libs>=19.1.7']"
+++
### Description: 
High-level loop and data-locality optimizer and optimization infrastructure for LLVM

### Files: 
* /usr/include/polly/Canonicalization.h
* /usr/include/polly/CodeGen/BlockGenerators.h
* /usr/include/polly/CodeGen/CodeGeneration.h
* /usr/include/polly/CodeGen/IRBuilder.h
* /usr/include/polly/CodeGen/IslAst.h
* /usr/include/polly/CodeGen/IslExprBuilder.h
* /usr/include/polly/CodeGen/IslNodeBuilder.h
* /usr/include/polly/CodeGen/LoopGenerators.h
* /usr/include/polly/CodeGen/LoopGeneratorsGOMP.h
* /usr/include/polly/CodeGen/LoopGeneratorsKMP.h
* /usr/include/polly/CodeGen/PerfMonitor.h
* /usr/include/polly/CodeGen/RuntimeDebugBuilder.h
* /usr/include/polly/CodeGen/Utils.h
* /usr/include/polly/CodePreparation.h
* /usr/include/polly/Config/config.h
* /usr/include/polly/DeadCodeElimination.h
* /usr/include/polly/DeLICM.h
* /usr/include/polly/DependenceInfo.h
* /usr/include/polly/FlattenAlgo.h
* /usr/include/polly/FlattenSchedule.h
* /usr/include/polly/ForwardOpTree.h
* /usr/include/polly/isl/aff.h
* /usr/include/polly/isl/aff_type.h
* /usr/include/polly/isl/arg.h
* /usr/include/polly/isl/ast.h
* /usr/include/polly/isl/ast_build.h
* /usr/include/polly/isl/ast_type.h
* /usr/include/polly/isl/constraint.h
* /usr/include/polly/isl/ctx.h
* /usr/include/polly/isl/fixed_box.h
* /usr/include/polly/isl/flow.h
* /usr/include/polly/isl/hash.h
* /usr/include/polly/isl/hmap.h
* /usr/include/polly/isl/id.h
* /usr/include/polly/isl/id_to_ast_expr.h
* /usr/include/polly/isl/id_to_id.h
* /usr/include/polly/isl/id_to_pw_aff.h
* /usr/include/polly/isl/id_type.h
* /usr/include/polly/isl/ilp.h
* /usr/include/polly/isl/isl-noexceptions.h
* /usr/include/polly/isl/list.h
* /usr/include/polly/isl/local_space.h
* /usr/include/polly/isl/lp.h
* /usr/include/polly/isl/map.h
* /usr/include/polly/isl/map_to_basic_set.h
* /usr/include/polly/isl/map_type.h
* /usr/include/polly/isl/mat.h
* /usr/include/polly/isl/maybe.h
* /usr/include/polly/isl/maybe_ast_expr.h
* /usr/include/polly/isl/maybe_basic_set.h
* /usr/include/polly/isl/maybe_id.h
* /usr/include/polly/isl/maybe_pw_aff.h
* /usr/include/polly/isl/maybe_templ.h
* /usr/include/polly/isl/multi.h
* /usr/include/polly/isl/obj.h
* /usr/include/polly/isl/options.h
* /usr/include/polly/isl/point.h
* /usr/include/polly/isl/polynomial.h
* /usr/include/polly/isl/polynomial_type.h
* /usr/include/polly/isl/printer.h
* /usr/include/polly/isl/printer_type.h
* /usr/include/polly/isl/schedule.h
* /usr/include/polly/isl/schedule_node.h
* /usr/include/polly/isl/schedule_type.h
* /usr/include/polly/isl/set.h
* /usr/include/polly/isl/set_type.h
* /usr/include/polly/isl/space.h
* /usr/include/polly/isl/space_type.h
* /usr/include/polly/isl/stdint.h
* /usr/include/polly/isl/stream.h
* /usr/include/polly/isl/stride_info.h
* /usr/include/polly/isl/union_map.h
* /usr/include/polly/isl/union_map_type.h
* /usr/include/polly/isl/union_set.h
* /usr/include/polly/isl/union_set_type.h
* /usr/include/polly/isl/val.h
* /usr/include/polly/isl/val_gmp.h
* /usr/include/polly/isl/val_type.h
* /usr/include/polly/isl/vec.h
* /usr/include/polly/isl/version.h
* /usr/include/polly/isl/vertices.h
* /usr/include/polly/JSONExporter.h
* /usr/include/polly/LinkAllPasses.h
* /usr/include/polly/ManualOptimizer.h
* /usr/include/polly/MatmulOptimizer.h
* /usr/include/polly/MaximalStaticExpansion.h
* /usr/include/polly/Options.h
* /usr/include/polly/PolyhedralInfo.h
* /usr/include/polly/PruneUnprofitable.h
* /usr/include/polly/RegisterPasses.h
* /usr/include/polly/ScheduleOptimizer.h
* /usr/include/polly/ScheduleTreeTransform.h
* /usr/include/polly/ScopBuilder.h
* /usr/include/polly/ScopDetection.h
* /usr/include/polly/ScopDetectionDiagnostic.h
* /usr/include/polly/ScopGraphPrinter.h
* /usr/include/polly/ScopInfo.h
* /usr/include/polly/ScopPass.h
* /usr/include/polly/Simplify.h
* /usr/include/polly/Support/DumpFunctionPass.h
* /usr/include/polly/Support/DumpModulePass.h
* /usr/include/polly/Support/GICHelper.h
* /usr/include/polly/Support/ISLOperators.h
* /usr/include/polly/Support/ISLOStream.h
* /usr/include/polly/Support/ISLTools.h
* /usr/include/polly/Support/PollyDebug.h
* /usr/include/polly/Support/SCEVAffinator.h
* /usr/include/polly/Support/SCEVValidator.h
* /usr/include/polly/Support/ScopHelper.h
* /usr/include/polly/Support/ScopLocation.h
* /usr/include/polly/Support/VirtualInstruction.h
* /usr/include/polly/ZoneAlgo.h
* /usr/lib/cmake/polly/PollyConfig.cmake
* /usr/lib/cmake/polly/PollyConfigVersion.cmake
* /usr/lib/cmake/polly/PollyExports-all.cmake
* /usr/lib/libPolly.a
* /usr/lib/libPollyISL.a
* /usr/lib/LLVMPolly.so
* /usr/share/doc/LLVM/polly/html/.buildinfo
* /usr/share/doc/LLVM/polly/html/Architecture.html
* /usr/share/doc/LLVM/polly/html/genindex.html
* /usr/share/doc/LLVM/polly/html/HowToManuallyUseTheIndividualPiecesOfPolly.html
* /usr/share/doc/LLVM/polly/html/index.html
* /usr/share/doc/LLVM/polly/html/objects.inv
* /usr/share/doc/LLVM/polly/html/Performance.html
* /usr/share/doc/LLVM/polly/html/ReleaseNotes.html
* /usr/share/doc/LLVM/polly/html/search.html
* /usr/share/doc/LLVM/polly/html/searchindex.js
* /usr/share/doc/LLVM/polly/html/TipsAndTricks.html
* /usr/share/doc/LLVM/polly/html/UsingPollyWithClang.html
* /usr/share/doc/LLVM/polly/html/_images/architecture.png
* /usr/share/doc/LLVM/polly/html/_images/GEMM_double.png
* /usr/share/doc/LLVM/polly/html/_images/LLVM-Passes-all.png
* /usr/share/doc/LLVM/polly/html/_images/LLVM-Passes-early.png
* /usr/share/doc/LLVM/polly/html/_images/LLVM-Passes-late.png
* /usr/share/doc/LLVM/polly/html/_images/LLVM-Passes-only.png
* /usr/share/doc/LLVM/polly/html/_sources/Architecture.rst.txt
* /usr/share/doc/LLVM/polly/html/_sources/HowToManuallyUseTheIndividualPiecesOfPolly.rst.txt
* /usr/share/doc/LLVM/polly/html/_sources/index.rst.txt
* /usr/share/doc/LLVM/polly/html/_sources/Performance.rst.txt
* /usr/share/doc/LLVM/polly/html/_sources/ReleaseNotes.rst.txt
* /usr/share/doc/LLVM/polly/html/_sources/TipsAndTricks.rst.txt
* /usr/share/doc/LLVM/polly/html/_sources/UsingPollyWithClang.rst.txt
* /usr/share/doc/LLVM/polly/html/_static/alert_info_32.png
* /usr/share/doc/LLVM/polly/html/_static/alert_warning_32.png
* /usr/share/doc/LLVM/polly/html/_static/basic.css
* /usr/share/doc/LLVM/polly/html/_static/bg-page.png
* /usr/share/doc/LLVM/polly/html/_static/bullet_orange.png
* /usr/share/doc/LLVM/polly/html/_static/doctools.js
* /usr/share/doc/LLVM/polly/html/_static/documentation_options.js
* /usr/share/doc/LLVM/polly/html/_static/file.png
* /usr/share/doc/LLVM/polly/html/_static/haiku.css
* /usr/share/doc/LLVM/polly/html/_static/language_data.js
* /usr/share/doc/LLVM/polly/html/_static/minus.png
* /usr/share/doc/LLVM/polly/html/_static/plus.png
* /usr/share/doc/LLVM/polly/html/_static/pygments.css
* /usr/share/doc/LLVM/polly/html/_static/searchtools.js
* /usr/share/doc/LLVM/polly/html/_static/sphinx_highlight.js
* /usr/share/man/man1/polly.1.gz
