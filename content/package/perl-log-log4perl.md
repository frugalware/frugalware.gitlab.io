+++
draft = false
title = "perl-log-log4perl 1.57-1"
version = "1.57-1"
description = "Log4j implementation for Perl"
date = "2023-02-21T14:19:27"
aliases = "/packages/219253"
categories = ['devel-extra']
upstreamurl = "http://cpan.org/"
arch = "x86_64"
size = "347320"
usize = "932966"
sha1sum = "2fad5e11c03b67895a9321832fb5f46f5355d14b"
depends = "['perl>=5.34.0']"
+++
Log4j implementation for Perl

{{< files text="show files" >}}* /usr/bin/site_perl/l4p-tmpl
* /usr/lib/perl5/site_perl/Log/Log4perl.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Appender.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Appender/Buffer.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Appender/DBI.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Appender/File.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Appender/Limit.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Appender/RRDs.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Appender/Screen.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Appender/ScreenColoredLevels.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Appender/Socket.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Appender/String.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Appender/Synchronized.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Appender/TestArrayBuffer.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Appender/TestBuffer.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Appender/TestFileCreeper.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Catalyst.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Config.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Config/BaseConfigurator.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Config/DOMConfigurator.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Config/PropertyConfigurator.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Config/Watch.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/DateFormat.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/FAQ.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Filter.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Filter/Boolean.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Filter/LevelMatch.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Filter/LevelRange.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Filter/MDC.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Filter/StringMatch.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/InternalDebug.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/JavaMap.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/JavaMap/ConsoleAppender.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/JavaMap/FileAppender.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/JavaMap/JDBCAppender.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/JavaMap/NTEventLogAppender.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/JavaMap/RollingFileAppender.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/JavaMap/SyslogAppender.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/JavaMap/TestBuffer.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Layout.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Layout/NoopLayout.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Layout/PatternLayout.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Layout/PatternLayout/Multiline.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Layout/SimpleLayout.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Level.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Logger.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/MDC.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/NDC.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Resurrector.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Util.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Util/Semaphore.pm
* /usr/lib/perl5/site_perl/Log/Log4perl/Util/TimeTracker.pm
* /usr/share/doc/perl-log-log4perl-1.57/LICENSE
* /usr/share/doc/perl-log-log4perl-1.57/MANIFEST
* /usr/share/doc/perl-log-log4perl-1.57/README
* /usr/share/man/man1/l4p-tmpl.1perl.gz
* /usr/share/man/man3/Log::Log4perl.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Appender.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Appender::Buffer.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Appender::DBI.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Appender::File.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Appender::Limit.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Appender::RRDs.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Appender::Screen.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Appender::ScreenColoredLevels.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Appender::Socket.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Appender::String.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Appender::Synchronized.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Appender::TestArrayBuffer.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Appender::TestBuffer.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Appender::TestFileCreeper.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Catalyst.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Config.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Config::BaseConfigurator.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Config::DOMConfigurator.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Config::PropertyConfigurator.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Config::Watch.3perl.gz
* /usr/share/man/man3/Log::Log4perl::DateFormat.3perl.gz
* /usr/share/man/man3/Log::Log4perl::FAQ.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Filter.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Filter::Boolean.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Filter::LevelMatch.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Filter::LevelRange.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Filter::MDC.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Filter::StringMatch.3perl.gz
* /usr/share/man/man3/Log::Log4perl::InternalDebug.3perl.gz
* /usr/share/man/man3/Log::Log4perl::JavaMap.3perl.gz
* /usr/share/man/man3/Log::Log4perl::JavaMap::ConsoleAppender.3perl.gz
* /usr/share/man/man3/Log::Log4perl::JavaMap::FileAppender.3perl.gz
* /usr/share/man/man3/Log::Log4perl::JavaMap::JDBCAppender.3perl.gz
* /usr/share/man/man3/Log::Log4perl::JavaMap::NTEventLogAppender.3perl.gz
* /usr/share/man/man3/Log::Log4perl::JavaMap::RollingFileAppender.3perl.gz
* /usr/share/man/man3/Log::Log4perl::JavaMap::SyslogAppender.3perl.gz
* /usr/share/man/man3/Log::Log4perl::JavaMap::TestBuffer.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Layout.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Layout::NoopLayout.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Layout::PatternLayout.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Layout::PatternLayout::Multiline.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Layout::SimpleLayout.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Level.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Logger.3perl.gz
* /usr/share/man/man3/Log::Log4perl::MDC.3perl.gz
* /usr/share/man/man3/Log::Log4perl::NDC.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Resurrector.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Util.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Util::Semaphore.3perl.gz
* /usr/share/man/man3/Log::Log4perl::Util::TimeTracker.3perl.gz
{{< /files >}}