+++
draft = false
title = "subversion 1.14.2-3"
version = "1.14.2-3"
date = "2023-10-12T09:30:56"
categories = ['devel-extra']
upstreamurl = "http://subversion.apache.org/"
arch = "x86_64"
size = "3137828"
usize = "12513537"
sha1sum = "8ec49f682ecc67b8c0b26b046d6a004f3be6753e"
depends = "['serf>=1.3.9-4', 'file>=5.25-3', 'utf8proc']"
files = "['etc/', 'etc/bash_completion.d/', 'etc/bash_completion.d/subversion', 'lib/', 'lib/systemd/', 'usr/', 'usr/bin/', 'usr/bin/svn', 'usr/bin/svnadmin', 'usr/bin/svnbench', 'usr/bin/svndumpfilter', 'usr/bin/svnfsfs', 'usr/bin/svnlook', 'usr/bin/svnmucc', 'usr/bin/svnrdump', 'usr/bin/svnsync', 'usr/bin/svnversion', 'usr/include/', 'usr/include/subversion-1/', 'usr/include/subversion-1/mod_authz_svn.h', 'usr/include/subversion-1/mod_dav_svn.h', 'usr/include/subversion-1/svn-revision.txt', 'usr/include/subversion-1/svn_auth.h', 'usr/include/subversion-1/svn_base64.h', 'usr/include/subversion-1/svn_cache_config.h', 'usr/include/subversion-1/svn_checksum.h', 'usr/include/subversion-1/svn_client.h', 'usr/include/subversion-1/svn_cmdline.h', 'usr/include/subversion-1/svn_compat.h', 'usr/include/subversion-1/svn_config.h', 'usr/include/subversion-1/svn_ctype.h', 'usr/include/subversion-1/svn_dav.h', 'usr/include/subversion-1/svn_delta.h', 'usr/include/subversion-1/svn_diff.h', 'usr/include/subversion-1/svn_dirent_uri.h', 'usr/include/subversion-1/svn_dso.h', 'usr/include/subversion-1/svn_error.h', 'usr/include/subversion-1/svn_error_codes.h', 'usr/include/subversion-1/svn_fs.h', 'usr/include/subversion-1/svn_hash.h', 'usr/include/subversion-1/svn_io.h', 'usr/include/subversion-1/svn_iter.h', 'usr/include/subversion-1/svn_md5.h', 'usr/include/subversion-1/svn_mergeinfo.h', 'usr/include/subversion-1/svn_nls.h', 'usr/include/subversion-1/svn_opt.h', 'usr/include/subversion-1/svn_opt_impl.h', 'usr/include/subversion-1/svn_path.h', 'usr/include/subversion-1/svn_pools.h', 'usr/include/subversion-1/svn_props.h', 'usr/include/subversion-1/svn_quoprint.h', 'usr/include/subversion-1/svn_ra.h', 'usr/include/subversion-1/svn_ra_svn.h', 'usr/include/subversion-1/svn_repos.h', 'usr/include/subversion-1/svn_sorts.h', 'usr/include/subversion-1/svn_string.h', 'usr/include/subversion-1/svn_subst.h', 'usr/include/subversion-1/svn_time.h', 'usr/include/subversion-1/svn_types.h', 'usr/include/subversion-1/svn_types_impl.h', 'usr/include/subversion-1/svn_user.h', 'usr/include/subversion-1/svn_utf.h', 'usr/include/subversion-1/svn_version.h', 'usr/include/subversion-1/svn_wc.h', 'usr/include/subversion-1/svn_x509.h', 'usr/include/subversion-1/svn_xml.h', 'usr/lib/', 'usr/lib/libsvn_client-1.so', 'usr/lib/libsvn_client-1.so.0', 'usr/lib/libsvn_client-1.so.0.0.0', 'usr/lib/libsvn_delta-1.so', 'usr/lib/libsvn_delta-1.so.0', 'usr/lib/libsvn_delta-1.so.0.0.0', 'usr/lib/libsvn_diff-1.so', 'usr/lib/libsvn_diff-1.so.0', 'usr/lib/libsvn_diff-1.so.0.0.0', 'usr/lib/libsvn_fs-1.so', 'usr/lib/libsvn_fs-1.so.0', 'usr/lib/libsvn_fs-1.so.0.0.0', 'usr/lib/libsvn_fs_base-1.so', 'usr/lib/libsvn_fs_base-1.so.0', 'usr/lib/libsvn_fs_base-1.so.0.0.0', 'usr/lib/libsvn_fs_fs-1.so', 'usr/lib/libsvn_fs_fs-1.so.0', 'usr/lib/libsvn_fs_fs-1.so.0.0.0', 'usr/lib/libsvn_fs_util-1.so', 'usr/lib/libsvn_fs_util-1.so.0', 'usr/lib/libsvn_fs_util-1.so.0.0.0', 'usr/lib/libsvn_fs_x-1.so', 'usr/lib/libsvn_fs_x-1.so.0', 'usr/lib/libsvn_fs_x-1.so.0.0.0', 'usr/lib/libsvn_ra-1.so', 'usr/lib/libsvn_ra-1.so.0', 'usr/lib/libsvn_ra-1.so.0.0.0', 'usr/lib/libsvn_ra_local-1.so', 'usr/lib/libsvn_ra_local-1.so.0', 'usr/lib/libsvn_ra_local-1.so.0.0.0', 'usr/lib/libsvn_ra_serf-1.so', 'usr/lib/libsvn_ra_serf-1.so.0', 'usr/lib/libsvn_ra_serf-1.so.0.0.0', 'usr/lib/libsvn_ra_svn-1.so', 'usr/lib/libsvn_ra_svn-1.so.0', 'usr/lib/libsvn_ra_svn-1.so.0.0.0', 'usr/lib/libsvn_repos-1.so', 'usr/lib/libsvn_repos-1.so.0', 'usr/lib/libsvn_repos-1.so.0.0.0', 'usr/lib/libsvn_subr-1.so', 'usr/lib/libsvn_subr-1.so.0', 'usr/lib/libsvn_subr-1.so.0.0.0', 'usr/lib/libsvn_wc-1.so', 'usr/lib/libsvn_wc-1.so.0', 'usr/lib/libsvn_wc-1.so.0.0.0', 'usr/lib/pkgconfig/', 'usr/lib/pkgconfig/libsvn_client.pc', 'usr/lib/pkgconfig/libsvn_delta.pc', 'usr/lib/pkgconfig/libsvn_diff.pc', 'usr/lib/pkgconfig/libsvn_fs.pc', 'usr/lib/pkgconfig/libsvn_fs_base.pc', 'usr/lib/pkgconfig/libsvn_fs_fs.pc', 'usr/lib/pkgconfig/libsvn_fs_util.pc', 'usr/lib/pkgconfig/libsvn_fs_x.pc', 'usr/lib/pkgconfig/libsvn_ra.pc', 'usr/lib/pkgconfig/libsvn_ra_local.pc', 'usr/lib/pkgconfig/libsvn_ra_serf.pc', 'usr/lib/pkgconfig/libsvn_ra_svn.pc', 'usr/lib/pkgconfig/libsvn_repos.pc', 'usr/lib/pkgconfig/libsvn_subr.pc', 'usr/lib/pkgconfig/libsvn_wc.pc', 'usr/lib/python3.12/', 'usr/share/', 'usr/share/doc/', 'usr/share/doc/subversion-1.14.2/', 'usr/share/doc/subversion-1.14.2/BUGS', 'usr/share/doc/subversion-1.14.2/CHANGES', 'usr/share/doc/subversion-1.14.2/INSTALL', 'usr/share/doc/subversion-1.14.2/LICENSE', 'usr/share/doc/subversion-1.14.2/README', 'usr/share/doc/subversion-1.14.2/doc/', 'usr/share/doc/subversion-1.14.2/doc/README', 'usr/share/doc/subversion-1.14.2/doc/doxygen.conf', 'usr/share/doc/subversion-1.14.2/doc/programmer/', 'usr/share/doc/subversion-1.14.2/doc/programmer/WritingChangeLogs.txt', 'usr/share/doc/subversion-1.14.2/doc/svn-square.jpg', 'usr/share/doc/subversion-1.14.2/doc/user/', 'usr/share/doc/subversion-1.14.2/doc/user/cvs-crossover-guide.html', 'usr/share/doc/subversion-1.14.2/doc/user/lj_article.txt', 'usr/share/doc/subversion-1.14.2/doc/user/svn-best-practices.html', 'usr/share/locale/', 'usr/share/locale/de/', 'usr/share/locale/de/LC_MESSAGES/', 'usr/share/locale/de/LC_MESSAGES/subversion.mo', 'usr/share/locale/es/', 'usr/share/locale/es/LC_MESSAGES/', 'usr/share/locale/es/LC_MESSAGES/subversion.mo', 'usr/share/locale/fr/', 'usr/share/locale/fr/LC_MESSAGES/', 'usr/share/locale/fr/LC_MESSAGES/subversion.mo', 'usr/share/locale/it/', 'usr/share/locale/it/LC_MESSAGES/', 'usr/share/locale/it/LC_MESSAGES/subversion.mo', 'usr/share/locale/ja/', 'usr/share/locale/ja/LC_MESSAGES/', 'usr/share/locale/ja/LC_MESSAGES/subversion.mo', 'usr/share/locale/ko/', 'usr/share/locale/ko/LC_MESSAGES/', 'usr/share/locale/ko/LC_MESSAGES/subversion.mo', 'usr/share/locale/nb/', 'usr/share/locale/nb/LC_MESSAGES/', 'usr/share/locale/nb/LC_MESSAGES/subversion.mo', 'usr/share/locale/pl/', 'usr/share/locale/pl/LC_MESSAGES/', 'usr/share/locale/pl/LC_MESSAGES/subversion.mo', 'usr/share/locale/pt_BR/', 'usr/share/locale/pt_BR/LC_MESSAGES/', 'usr/share/locale/pt_BR/LC_MESSAGES/subversion.mo', 'usr/share/locale/sv/', 'usr/share/locale/sv/LC_MESSAGES/', 'usr/share/locale/sv/LC_MESSAGES/subversion.mo', 'usr/share/locale/zh_CN/', 'usr/share/locale/zh_CN/LC_MESSAGES/', 'usr/share/locale/zh_CN/LC_MESSAGES/subversion.mo', 'usr/share/locale/zh_TW/', 'usr/share/locale/zh_TW/LC_MESSAGES/', 'usr/share/locale/zh_TW/LC_MESSAGES/subversion.mo', 'usr/share/man/', 'usr/share/man/man1/', 'usr/share/man/man1/svn.1.gz', 'usr/share/man/man1/svnadmin.1.gz', 'usr/share/man/man1/svndumpfilter.1.gz', 'usr/share/man/man1/svnlook.1.gz', 'usr/share/man/man1/svnmucc.1.gz', 'usr/share/man/man1/svnrdump.1.gz', 'usr/share/man/man1/svnsync.1.gz', 'usr/share/man/man1/svnversion.1.gz', 'usr/share/man/man3/', 'usr/share/man/man5/', 'usr/share/man/man8/', 'usr/share/subversion/', 'usr/share/subversion/dev/', 'usr/share/subversion/dev/.libs/', 'usr/share/subversion/dev/.libs/fsfs-access-map', 'usr/share/subversion/dev/.libs/fsfs-access-map.o', 'usr/share/subversion/dev/.libs/x509-parser', 'usr/share/subversion/dev/.libs/x509-parser.o', 'usr/share/subversion/dev/analyze-svnlogs.py', 'usr/share/subversion/dev/aprerr.txt', 'usr/share/subversion/dev/benchmarks/', 'usr/share/subversion/dev/benchmarks/RepoPerf/', 'usr/share/subversion/dev/benchmarks/RepoPerf/ClearMemory.cpp', 'usr/share/subversion/dev/benchmarks/RepoPerf/TimeWin.cpp', 'usr/share/subversion/dev/benchmarks/RepoPerf/copy_repo.py', 'usr/share/subversion/dev/benchmarks/RepoPerf/win_repo_bench.py', 'usr/share/subversion/dev/benchmarks/large_dirs/', 'usr/share/subversion/dev/benchmarks/large_dirs/create_bigdir.sh', 'usr/share/subversion/dev/benchmarks/suite1/', 'usr/share/subversion/dev/benchmarks/suite1/benchmark.py', 'usr/share/subversion/dev/benchmarks/suite1/cronjob', 'usr/share/subversion/dev/benchmarks/suite1/crontab.entry', 'usr/share/subversion/dev/benchmarks/suite1/generate_charts', 'usr/share/subversion/dev/benchmarks/suite1/run', 'usr/share/subversion/dev/benchmarks/suite1/run.bat', 'usr/share/subversion/dev/build-svn-deps-win.pl', 'usr/share/subversion/dev/check-license.py', 'usr/share/subversion/dev/contribulyze.py', 'usr/share/subversion/dev/datecheck.py', 'usr/share/subversion/dev/find-bad-style.py', 'usr/share/subversion/dev/find-control-statements.py', 'usr/share/subversion/dev/find-unmoved-deprecated.sh', 'usr/share/subversion/dev/fsfs-access-map', 'usr/share/subversion/dev/fsfs-access-map.c', 'usr/share/subversion/dev/fsfs-access-map.lo', 'usr/share/subversion/dev/gdb-py/', 'usr/share/subversion/dev/gdb-py/README', 'usr/share/subversion/dev/gdb-py/svndbg/', 'usr/share/subversion/dev/gdb-py/svndbg/__init__.py', 'usr/share/subversion/dev/gdb-py/svndbg/printers.py', 'usr/share/subversion/dev/gen-javahl-errors.py', 'usr/share/subversion/dev/gen-py-errors.py', 'usr/share/subversion/dev/gen_junit_report.py', 'usr/share/subversion/dev/gnuify-changelog.pl', 'usr/share/subversion/dev/graph-dav-servers.py', 'usr/share/subversion/dev/histogram.py', 'usr/share/subversion/dev/hot-backup.py', 'usr/share/subversion/dev/hot-backup.py.in', 'usr/share/subversion/dev/iz/', 'usr/share/subversion/dev/iz/defect.dem', 'usr/share/subversion/dev/iz/ff2csv.command', 'usr/share/subversion/dev/iz/ff2csv.py', 'usr/share/subversion/dev/iz/find-fix.py', 'usr/share/subversion/dev/iz/run-queries.sh', 'usr/share/subversion/dev/lock-check.py', 'usr/share/subversion/dev/log_revnum_change_asf.py', 'usr/share/subversion/dev/merge-graph.py', 'usr/share/subversion/dev/mergegraph/', 'usr/share/subversion/dev/mergegraph/__init__.py', 'usr/share/subversion/dev/mergegraph/mergegraph.py', 'usr/share/subversion/dev/mergegraph/save_as_sh.py', 'usr/share/subversion/dev/min-includes.sh', 'usr/share/subversion/dev/mklog.py', 'usr/share/subversion/dev/mlpatch.py', 'usr/share/subversion/dev/normalize-dump.py', 'usr/share/subversion/dev/po-merge.py', 'usr/share/subversion/dev/prebuild-cleanup.sh', 'usr/share/subversion/dev/random-commits.py', 'usr/share/subversion/dev/remove-trailing-whitespace.sh', 'usr/share/subversion/dev/sbox-ospath.py', 'usr/share/subversion/dev/scramble-tree.py', 'usr/share/subversion/dev/stress.pl', 'usr/share/subversion/dev/svn-dev.el', 'usr/share/subversion/dev/svn-dev.vim', 'usr/share/subversion/dev/svn-entries.el', 'usr/share/subversion/dev/svn-merge-revs.py', 'usr/share/subversion/dev/svnmover/', 'usr/share/subversion/dev/svnmover/.libs/', 'usr/share/subversion/dev/svnmover/.libs/merge3.o', 'usr/share/subversion/dev/svnmover/.libs/ra.o', 'usr/share/subversion/dev/svnmover/.libs/scanlog.o', 'usr/share/subversion/dev/svnmover/.libs/svnmover', 'usr/share/subversion/dev/svnmover/.libs/svnmover.o', 'usr/share/subversion/dev/svnmover/.libs/util.o', 'usr/share/subversion/dev/svnmover/linenoise/', 'usr/share/subversion/dev/svnmover/linenoise/LICENSE', 'usr/share/subversion/dev/svnmover/linenoise/README.markdown', 'usr/share/subversion/dev/svnmover/linenoise/linenoise.c', 'usr/share/subversion/dev/svnmover/linenoise/linenoise.h', 'usr/share/subversion/dev/svnmover/merge3.c', 'usr/share/subversion/dev/svnmover/merge3.lo', 'usr/share/subversion/dev/svnmover/ra.c', 'usr/share/subversion/dev/svnmover/ra.lo', 'usr/share/subversion/dev/svnmover/scanlog.c', 'usr/share/subversion/dev/svnmover/scanlog.lo', 'usr/share/subversion/dev/svnmover/svnmover', 'usr/share/subversion/dev/svnmover/svnmover.c', 'usr/share/subversion/dev/svnmover/svnmover.h', 'usr/share/subversion/dev/svnmover/svnmover.lo', 'usr/share/subversion/dev/svnmover/util.c', 'usr/share/subversion/dev/svnmover/util.lo', 'usr/share/subversion/dev/svnqlite3-dump', 'usr/share/subversion/dev/svnraisetreeconflict/', 'usr/share/subversion/dev/svnraisetreeconflict/.libs/', 'usr/share/subversion/dev/svnraisetreeconflict/.libs/svnraisetreeconflict', 'usr/share/subversion/dev/svnraisetreeconflict/.libs/svnraisetreeconflict.o', 'usr/share/subversion/dev/svnraisetreeconflict/svnraisetreeconflict', 'usr/share/subversion/dev/svnraisetreeconflict/svnraisetreeconflict.c', 'usr/share/subversion/dev/svnraisetreeconflict/svnraisetreeconflict.lo', 'usr/share/subversion/dev/trails.py', 'usr/share/subversion/dev/unix-build/', 'usr/share/subversion/dev/unix-build/Makefile.svn', 'usr/share/subversion/dev/unix-build/README', 'usr/share/subversion/dev/verify-history.py', 'usr/share/subversion/dev/warn-ignored-err.sh', 'usr/share/subversion/dev/wc-format.py', 'usr/share/subversion/dev/wc-ng/', 'usr/share/subversion/dev/wc-ng/.libs/', 'usr/share/subversion/dev/wc-ng/.libs/svn-wc-db-tester', 'usr/share/subversion/dev/wc-ng/.libs/svn-wc-db-tester.o', 'usr/share/subversion/dev/wc-ng/bump-to-19.py', 'usr/share/subversion/dev/wc-ng/count-progress.py', 'usr/share/subversion/dev/wc-ng/gather-data.sh', 'usr/share/subversion/dev/wc-ng/graph-data.py', 'usr/share/subversion/dev/wc-ng/populate-pristine.py', 'usr/share/subversion/dev/wc-ng/svn-wc-db-tester', 'usr/share/subversion/dev/wc-ng/svn-wc-db-tester.c', 'usr/share/subversion/dev/wc-ng/svn-wc-db-tester.lo', 'usr/share/subversion/dev/which-error.py', 'usr/share/subversion/dev/windows-build/', 'usr/share/subversion/dev/windows-build/Makefile', 'usr/share/subversion/dev/windows-build/README', 'usr/share/subversion/dev/windows-build/document-version.pl', 'usr/share/subversion/dev/x509-parser', 'usr/share/subversion/dev/x509-parser.c', 'usr/share/subversion/dev/x509-parser.lo', 'usr/share/subversion/hook-scripts/', 'usr/share/subversion/hook-scripts/CVE-2017-9800-pre-commit.py', 'usr/share/subversion/hook-scripts/commit-access-control.cfg.example', 'usr/share/subversion/hook-scripts/commit-access-control.pl', 'usr/share/subversion/hook-scripts/commit-email.rb', 'usr/share/subversion/hook-scripts/control-chars.py', 'usr/share/subversion/hook-scripts/log-police.py', 'usr/share/subversion/hook-scripts/mailer/', 'usr/share/subversion/hook-scripts/mailer/mailer.conf.example', 'usr/share/subversion/hook-scripts/mailer/mailer.py', 'usr/share/subversion/hook-scripts/mailer/tests/', 'usr/share/subversion/hook-scripts/mailer/tests/mailer-init.sh', 'usr/share/subversion/hook-scripts/mailer/tests/mailer-t1.output', 'usr/share/subversion/hook-scripts/mailer/tests/mailer-t1.sh', 'usr/share/subversion/hook-scripts/mailer/tests/mailer-tweak.py', 'usr/share/subversion/hook-scripts/mailer/tests/mailer.conf', 'usr/share/subversion/hook-scripts/persist-ephemeral-txnprops.py', 'usr/share/subversion/hook-scripts/reject-detected-sha1-collisions.sh', 'usr/share/subversion/hook-scripts/reject-known-sha1-collisions.sh', 'usr/share/subversion/hook-scripts/svn2feed.py', 'usr/share/subversion/hook-scripts/svnperms.conf.example', 'usr/share/subversion/hook-scripts/svnperms.py', 'usr/share/subversion/hook-scripts/validate-extensions.py', 'usr/share/subversion/hook-scripts/validate-files.conf.example', 'usr/share/subversion/hook-scripts/validate-files.py', 'usr/share/subversion/hook-scripts/verify-po.py']"
+++
A version control system that is a compelling replacement for CVS.