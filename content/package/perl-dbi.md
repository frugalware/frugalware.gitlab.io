+++
draft = false
title = "perl-dbi 1.643-3"
version = "1.643-3"
description = "Database independent interface for Perl"
date = "2023-09-24T20:03:06"
aliases = "/packages/3279"
categories = ['devel-extra']
upstreamurl = "http://cpan.org/"
arch = "x86_64"
size = "712352"
usize = "2048173"
sha1sum = "14fd9ca38fb3b4e2fe1481472b66255b2924e10b"
depends = "['perl>=5.34.0']"
reverse_depends = "['spamassassin']"
+++
Database independent interface for Perl{{< spoiler text="show files" >}}* /usr/bin/site_perl/dbilogstrip
* /usr/bin/site_perl/dbiprof
* /usr/bin/site_perl/dbiproxy
* /usr/lib/perl5/5.38/site_perl/auto/DBI/dbd_xsh.h
* /usr/lib/perl5/5.38/site_perl/auto/DBI/DBI.so
* /usr/lib/perl5/5.38/site_perl/auto/DBI/dbipport.h
* /usr/lib/perl5/5.38/site_perl/auto/DBI/dbivport.h
* /usr/lib/perl5/5.38/site_perl/auto/DBI/DBIXS.h
* /usr/lib/perl5/5.38/site_perl/auto/DBI/dbixs_rev.h
* /usr/lib/perl5/5.38/site_perl/auto/DBI/dbi_sql.h
* /usr/lib/perl5/5.38/site_perl/auto/DBI/Driver.xst
* /usr/lib/perl5/5.38/site_perl/auto/DBI/Driver_xst.h
* /usr/lib/perl5/5.38/site_perl/Bundle/DBI.pm
* /usr/lib/perl5/5.38/site_perl/DBD/DBM.pm
* /usr/lib/perl5/5.38/site_perl/DBD/ExampleP.pm
* /usr/lib/perl5/5.38/site_perl/DBD/File.pm
* /usr/lib/perl5/5.38/site_perl/DBD/File/Developers.pod
* /usr/lib/perl5/5.38/site_perl/DBD/File/HowTo.pod
* /usr/lib/perl5/5.38/site_perl/DBD/File/Roadmap.pod
* /usr/lib/perl5/5.38/site_perl/DBD/Gofer.pm
* /usr/lib/perl5/5.38/site_perl/DBD/Gofer/Policy/Base.pm
* /usr/lib/perl5/5.38/site_perl/DBD/Gofer/Policy/classic.pm
* /usr/lib/perl5/5.38/site_perl/DBD/Gofer/Policy/pedantic.pm
* /usr/lib/perl5/5.38/site_perl/DBD/Gofer/Policy/rush.pm
* /usr/lib/perl5/5.38/site_perl/DBD/Gofer/Transport/Base.pm
* /usr/lib/perl5/5.38/site_perl/DBD/Gofer/Transport/corostream.pm
* /usr/lib/perl5/5.38/site_perl/DBD/Gofer/Transport/null.pm
* /usr/lib/perl5/5.38/site_perl/DBD/Gofer/Transport/pipeone.pm
* /usr/lib/perl5/5.38/site_perl/DBD/Gofer/Transport/stream.pm
* /usr/lib/perl5/5.38/site_perl/DBD/Mem.pm
* /usr/lib/perl5/5.38/site_perl/DBD/NullP.pm
* /usr/lib/perl5/5.38/site_perl/DBD/Proxy.pm
* /usr/lib/perl5/5.38/site_perl/DBD/Sponge.pm
* /usr/lib/perl5/5.38/site_perl/DBI.pm
* /usr/lib/perl5/5.38/site_perl/DBI/Changes.pm
* /usr/lib/perl5/5.38/site_perl/DBI/Const/GetInfo/ANSI.pm
* /usr/lib/perl5/5.38/site_perl/DBI/Const/GetInfo/ODBC.pm
* /usr/lib/perl5/5.38/site_perl/DBI/Const/GetInfoReturn.pm
* /usr/lib/perl5/5.38/site_perl/DBI/Const/GetInfoType.pm
* /usr/lib/perl5/5.38/site_perl/DBI/DBD.pm
* /usr/lib/perl5/5.38/site_perl/DBI/DBD/Metadata.pm
* /usr/lib/perl5/5.38/site_perl/DBI/DBD/SqlEngine.pm
* /usr/lib/perl5/5.38/site_perl/DBI/DBD/SqlEngine/Developers.pod
* /usr/lib/perl5/5.38/site_perl/DBI/DBD/SqlEngine/HowTo.pod
* /usr/lib/perl5/5.38/site_perl/DBI/Gofer/Execute.pm
* /usr/lib/perl5/5.38/site_perl/DBI/Gofer/Request.pm
* /usr/lib/perl5/5.38/site_perl/DBI/Gofer/Response.pm
* /usr/lib/perl5/5.38/site_perl/DBI/Gofer/Serializer/Base.pm
* /usr/lib/perl5/5.38/site_perl/DBI/Gofer/Serializer/DataDumper.pm
* /usr/lib/perl5/5.38/site_perl/DBI/Gofer/Serializer/Storable.pm
* /usr/lib/perl5/5.38/site_perl/DBI/Gofer/Transport/Base.pm
* /usr/lib/perl5/5.38/site_perl/DBI/Gofer/Transport/pipeone.pm
* /usr/lib/perl5/5.38/site_perl/DBI/Gofer/Transport/stream.pm
* /usr/lib/perl5/5.38/site_perl/DBI/Profile.pm
* /usr/lib/perl5/5.38/site_perl/DBI/ProfileData.pm
* /usr/lib/perl5/5.38/site_perl/DBI/ProfileDumper.pm
* /usr/lib/perl5/5.38/site_perl/DBI/ProfileDumper/Apache.pm
* /usr/lib/perl5/5.38/site_perl/DBI/ProfileSubs.pm
* /usr/lib/perl5/5.38/site_perl/DBI/ProxyServer.pm
* /usr/lib/perl5/5.38/site_perl/DBI/PurePerl.pm
* /usr/lib/perl5/5.38/site_perl/DBI/SQL/Nano.pm
* /usr/lib/perl5/5.38/site_perl/DBI/Util/CacheMemory.pm
* /usr/lib/perl5/5.38/site_perl/DBI/Util/_accessor.pm
* /usr/lib/perl5/5.38/site_perl/DBI/W32ODBC.pm
* /usr/lib/perl5/5.38/site_perl/dbixs_rev.pl
* /usr/lib/perl5/5.38/site_perl/Win32/DBIODBC.pm
* /usr/share/doc/perl-dbi-1.643/INSTALL
* /usr/share/doc/perl-dbi-1.643/LICENSE
* /usr/share/doc/perl-dbi-1.643/MANIFEST
* /usr/share/doc/perl-dbi-1.643/README.md
* /usr/share/man/man1/dbilogstrip.1perl.gz
* /usr/share/man/man1/dbiprof.1perl.gz
* /usr/share/man/man1/dbiproxy.1perl.gz
* /usr/share/man/man3/Bundle::DBI.3perl.gz
* /usr/share/man/man3/DBD::DBM.3perl.gz
* /usr/share/man/man3/DBD::File.3perl.gz
* /usr/share/man/man3/DBD::File::Developers.3perl.gz
* /usr/share/man/man3/DBD::File::HowTo.3perl.gz
* /usr/share/man/man3/DBD::File::Roadmap.3perl.gz
* /usr/share/man/man3/DBD::Gofer.3perl.gz
* /usr/share/man/man3/DBD::Gofer::Policy::Base.3perl.gz
* /usr/share/man/man3/DBD::Gofer::Policy::classic.3perl.gz
* /usr/share/man/man3/DBD::Gofer::Policy::pedantic.3perl.gz
* /usr/share/man/man3/DBD::Gofer::Policy::rush.3perl.gz
* /usr/share/man/man3/DBD::Gofer::Transport::Base.3perl.gz
* /usr/share/man/man3/DBD::Gofer::Transport::corostream.3perl.gz
* /usr/share/man/man3/DBD::Gofer::Transport::null.3perl.gz
* /usr/share/man/man3/DBD::Gofer::Transport::pipeone.3perl.gz
* /usr/share/man/man3/DBD::Gofer::Transport::stream.3perl.gz
* /usr/share/man/man3/DBD::Mem.3perl.gz
* /usr/share/man/man3/DBD::Proxy.3perl.gz
* /usr/share/man/man3/DBD::Sponge.3perl.gz
* /usr/share/man/man3/DBI.3perl.gz
* /usr/share/man/man3/DBI::Const::GetInfo::ANSI.3perl.gz
* /usr/share/man/man3/DBI::Const::GetInfo::ODBC.3perl.gz
* /usr/share/man/man3/DBI::Const::GetInfoReturn.3perl.gz
* /usr/share/man/man3/DBI::Const::GetInfoType.3perl.gz
* /usr/share/man/man3/DBI::DBD.3perl.gz
* /usr/share/man/man3/DBI::DBD::Metadata.3perl.gz
* /usr/share/man/man3/DBI::DBD::SqlEngine.3perl.gz
* /usr/share/man/man3/DBI::DBD::SqlEngine::Developers.3perl.gz
* /usr/share/man/man3/DBI::DBD::SqlEngine::HowTo.3perl.gz
* /usr/share/man/man3/DBI::Gofer::Execute.3perl.gz
* /usr/share/man/man3/DBI::Gofer::Request.3perl.gz
* /usr/share/man/man3/DBI::Gofer::Response.3perl.gz
* /usr/share/man/man3/DBI::Gofer::Serializer::Base.3perl.gz
* /usr/share/man/man3/DBI::Gofer::Serializer::DataDumper.3perl.gz
* /usr/share/man/man3/DBI::Gofer::Serializer::Storable.3perl.gz
* /usr/share/man/man3/DBI::Gofer::Transport::Base.3perl.gz
* /usr/share/man/man3/DBI::Gofer::Transport::pipeone.3perl.gz
* /usr/share/man/man3/DBI::Gofer::Transport::stream.3perl.gz
* /usr/share/man/man3/DBI::Profile.3perl.gz
* /usr/share/man/man3/DBI::ProfileData.3perl.gz
* /usr/share/man/man3/DBI::ProfileDumper.3perl.gz
* /usr/share/man/man3/DBI::ProfileDumper::Apache.3perl.gz
* /usr/share/man/man3/DBI::ProfileSubs.3perl.gz
* /usr/share/man/man3/DBI::ProxyServer.3perl.gz
* /usr/share/man/man3/DBI::PurePerl.3perl.gz
* /usr/share/man/man3/DBI::SQL::Nano.3perl.gz
* /usr/share/man/man3/DBI::Util::CacheMemory.3perl.gz
* /usr/share/man/man3/DBI::W32ODBC.3perl.gz
* /usr/share/man/man3/Win32::DBIODBC.3perl.gz
{{< /spoiler >}}