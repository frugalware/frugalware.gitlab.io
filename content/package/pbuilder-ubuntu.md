+++
draft = false
title = "pbuilder-ubuntu 0.229.1-2"
version = "0.229.1-2"
date = "2022-07-31T10:37:05"
categories = ['apps-extra']
upstreamurl = "https://launchpad.net/ubuntu/+source/pbuilder"
arch = "x86_64"
size = "306536"
usize = "837148"
sha1sum = "262ec778811efd51added2a5b7df6deb17672016"
depends = "['debootstrap', 'dpkg', 'coreutils', 'wget', 'perl-datetime']"
license = "GPL"
files = "['etc/', 'etc/pbuilder/', 'etc/pbuilder/buildd-config.sh', 'usr/', 'usr/bin/', 'usr/bin/debuild-pbuilder', 'usr/bin/pdebuild', 'usr/lib/', 'usr/lib/pbuilder/', 'usr/lib/pbuilder/pbuilder-apt-config', 'usr/lib/pbuilder/pbuilder-buildpackage', 'usr/lib/pbuilder/pbuilder-buildpackage-funcs', 'usr/lib/pbuilder/pbuilder-checkparams', 'usr/lib/pbuilder/pbuilder-createbuildenv', 'usr/lib/pbuilder/pbuilder-loadconfig', 'usr/lib/pbuilder/pbuilder-modules', 'usr/lib/pbuilder/pbuilder-runhooks', 'usr/lib/pbuilder/pbuilder-satisfydepends', 'usr/lib/pbuilder/pbuilder-satisfydepends-apt', 'usr/lib/pbuilder/pbuilder-satisfydepends-aptitude', 'usr/lib/pbuilder/pbuilder-satisfydepends-checkparams', 'usr/lib/pbuilder/pbuilder-satisfydepends-classic', 'usr/lib/pbuilder/pbuilder-satisfydepends-experimental', 'usr/lib/pbuilder/pbuilder-satisfydepends-funcs', 'usr/lib/pbuilder/pbuilder-satisfydepends-gdebi', 'usr/lib/pbuilder/pbuilder-unshare-wrapper', 'usr/lib/pbuilder/pbuilder-updatebuildenv', 'usr/lib/pbuilder/pdebuild-checkparams', 'usr/lib/pbuilder/pdebuild-internal', 'usr/sbin/', 'usr/sbin/pbuilder', 'usr/share/', 'usr/share/bash-completion/', 'usr/share/bash-completion/completions/', 'usr/share/bash-completion/completions/pbuilder', 'usr/share/doc-base/', 'usr/share/doc-base/pbuilder', 'usr/share/doc/', 'usr/share/doc/pbuilder-0.229.1/', 'usr/share/doc/pbuilder-0.229.1/AUTHORS', 'usr/share/doc/pbuilder-0.229.1/NEWS.Debian.gz', 'usr/share/doc/pbuilder-0.229.1/README', 'usr/share/doc/pbuilder-0.229.1/README.Debian', 'usr/share/doc/pbuilder-0.229.1/THANKS', 'usr/share/doc/pbuilder-0.229.1/TODO', 'usr/share/doc/pbuilder-0.229.1/changelog.gz', 'usr/share/doc/pbuilder-0.229.1/copyright', 'usr/share/doc/pbuilder-0.229.1/examples/', 'usr/share/doc/pbuilder-0.229.1/examples/B20autopkgtest', 'usr/share/doc/pbuilder-0.229.1/examples/B90lintian', 'usr/share/doc/pbuilder-0.229.1/examples/B90list-missing', 'usr/share/doc/pbuilder-0.229.1/examples/B91debc', 'usr/share/doc/pbuilder-0.229.1/examples/B91dpkg-i', 'usr/share/doc/pbuilder-0.229.1/examples/B92test-pkg', 'usr/share/doc/pbuilder-0.229.1/examples/C10shell', 'usr/share/doc/pbuilder-0.229.1/examples/C11screen', 'usr/share/doc/pbuilder-0.229.1/examples/D10tmp', 'usr/share/doc/pbuilder-0.229.1/examples/D20addnonfree', 'usr/share/doc/pbuilder-0.229.1/examples/D65various-compiler-support', 'usr/share/doc/pbuilder-0.229.1/examples/D80no-man-db-rebuild', 'usr/share/doc/pbuilder-0.229.1/examples/D90chrootmemo', 'usr/share/doc/pbuilder-0.229.1/examples/F90chrootmemo', 'usr/share/doc/pbuilder-0.229.1/examples/execute_installtest.sh', 'usr/share/doc/pbuilder-0.229.1/examples/execute_paramtest.sh', 'usr/share/doc/pbuilder-0.229.1/examples/lvmpbuilder/', 'usr/share/doc/pbuilder-0.229.1/examples/lvmpbuilder/README', 'usr/share/doc/pbuilder-0.229.1/examples/lvmpbuilder/STRATEGY', 'usr/share/doc/pbuilder-0.229.1/examples/lvmpbuilder/lib/', 'usr/share/doc/pbuilder-0.229.1/examples/lvmpbuilder/lib/lvmbuilder-checkparams', 'usr/share/doc/pbuilder-0.229.1/examples/lvmpbuilder/lib/lvmbuilder-modules.gz', 'usr/share/doc/pbuilder-0.229.1/examples/lvmpbuilder/lib/lvmbuilder-unimplemented', 'usr/share/doc/pbuilder-0.229.1/examples/lvmpbuilder/lvmbuilder', 'usr/share/doc/pbuilder-0.229.1/examples/pbuildd/', 'usr/share/doc/pbuilder-0.229.1/examples/pbuildd/buildd.sh', 'usr/share/doc/pbuilder-0.229.1/examples/pbuildd/hookdir/', 'usr/share/doc/pbuilder-0.229.1/examples/pbuildd/hookdir/A10dpkg-l.sh', 'usr/share/doc/pbuilder-0.229.1/examples/pbuilder-distribution.sh', 'usr/share/doc/pbuilder-0.229.1/examples/pbuilder-test/', 'usr/share/doc/pbuilder-0.229.1/examples/pbuilder-test/000_prepinstall', 'usr/share/doc/pbuilder-0.229.1/examples/pbuilder-test/001_apprun', 'usr/share/doc/pbuilder-0.229.1/examples/pbuilder-test/002_libfile', 'usr/share/doc/pbuilder-0.229.1/examples/pbuilder-test/002_sample.c', 'usr/share/doc/pbuilder-0.229.1/examples/pbuilder-test/003_makecheck', 'usr/share/doc/pbuilder-0.229.1/examples/pbuilder-test/004_ldd', 'usr/share/doc/pbuilder-0.229.1/examples/pbuilder-test/README', 'usr/share/doc/pbuilder-0.229.1/examples/pbuilderrc.gz', 'usr/share/doc/pbuilder-0.229.1/examples/rebuild/', 'usr/share/doc/pbuilder-0.229.1/examples/rebuild/README', 'usr/share/doc/pbuilder-0.229.1/examples/rebuild/buildall', 'usr/share/doc/pbuilder-0.229.1/examples/rebuild/getlist', 'usr/share/doc/pbuilder-0.229.1/pbuilder-doc.de.html', 'usr/share/doc/pbuilder-0.229.1/pbuilder-doc.fr.html', 'usr/share/doc/pbuilder-0.229.1/pbuilder-doc.html', 'usr/share/doc/pbuilder-0.229.1/pbuilder-doc.ja.html', 'usr/share/doc/pbuilder-0.229.1/pbuilder-doc.pdf', 'usr/share/man/', 'usr/share/man/man1/', 'usr/share/man/man1/debuild-pbuilder.1.gz', 'usr/share/man/man1/pdebuild.1.gz', 'usr/share/man/man5/', 'usr/share/man/man5/pbuilderrc.5.gz', 'usr/share/man/man8/', 'usr/share/man/man8/pbuilder.8.gz', 'usr/share/pbuilder/', 'usr/share/pbuilder/pbuilderrc', 'var/', 'var/cache/', 'var/cache/pbuilder/', 'var/cache/pbuilder/aptcache/', 'var/cache/pbuilder/build/', 'var/cache/pbuilder/ccache/', 'var/cache/pbuilder/pbuildd/', 'var/cache/pbuilder/pbuilder-mnt/', 'var/cache/pbuilder/result/']"
+++
personal package builder for Debian packages