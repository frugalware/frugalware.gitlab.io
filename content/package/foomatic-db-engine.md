+++
draft = false
title = "foomatic-db-engine 4.0.13-2"
version = "4.0.13-2"
description = "Foomatic's database engine generates PPD files from the data in Foomatic's XML database."
date = "2024-01-14T16:05:50"
aliases = "/packages/168919"
categories = ['apps-extra']
upstreamurl = "http://www.linuxfoundation.org/collaborate/workgroups/openprinting/databasefoomatic"
arch = "x86_64"
size = "240740"
usize = "1001840"
sha1sum = "db49de0d752772859fa955e34dcdb027103b7dae"
depends = "['libxml2', 'perl', 'xz']"
reverse_depends = "['hplip-driver']"
+++
Foomatic's database engine generates PPD files from the data in Foomatic's XML database."

{{< files text="show files" >}}* /usr/bin/foomatic-addpjloptions
* /usr/bin/foomatic-cleanupdrivers
* /usr/bin/foomatic-combo-xml
* /usr/bin/foomatic-compiledb
* /usr/bin/foomatic-configure
* /usr/bin/foomatic-datafile
* /usr/bin/foomatic-extract-text
* /usr/bin/foomatic-fix-xml
* /usr/bin/foomatic-getpjloptions
* /usr/bin/foomatic-kitload
* /usr/bin/foomatic-nonumericalids
* /usr/bin/foomatic-perl-data
* /usr/bin/foomatic-ppd-options
* /usr/bin/foomatic-ppd-to-xml
* /usr/bin/foomatic-ppdfile
* /usr/bin/foomatic-preferred-driver
* /usr/bin/foomatic-printermap-to-gutenprint-xml
* /usr/bin/foomatic-printjob
* /usr/bin/foomatic-replaceoldprinterids
* /usr/bin/foomatic-searchprinter
* /usr/lib/perl5/site_perl/Foomatic/DB.pm
* /usr/lib/perl5/site_perl/Foomatic/Defaults.pm
* /usr/lib/perl5/site_perl/Foomatic/PPD.pm
* /usr/lib/perl5/site_perl/Foomatic/UIElem.pm
* /usr/share/doc/foomatic-db-engine-4.0.13/ChangeLog
* /usr/share/doc/foomatic-db-engine-4.0.13/COPYING
* /usr/share/doc/foomatic-db-engine-4.0.13/README
* /usr/share/doc/foomatic-db-engine-4.0.13/TODO
* /usr/share/foomatic/templates/pjl_enum_choice.xml
* /usr/share/foomatic/templates/pjl_enum_option.xml
* /usr/share/foomatic/templates/pjl_num_option.xml
* /usr/share/man/man1/foomatic-combo-xml.1.gz
* /usr/share/man/man1/foomatic-compiledb.1.gz
* /usr/share/man/man1/foomatic-configure.1.gz
* /usr/share/man/man1/foomatic-perl-data.1.gz
* /usr/share/man/man1/foomatic-ppd-options.1.gz
* /usr/share/man/man1/foomatic-ppdfile.1.gz
* /usr/share/man/man1/foomatic-printjob.1.gz
* /usr/share/man/man8/foomatic-addpjloptions.8.gz
* /usr/share/man/man8/foomatic-getpjloptions.8.gz
* /usr/share/man/man8/foomatic-kitload.8.gz
* /usr/share/man/man8/foomatic-preferred-driver.8.gz
{{< /files >}}