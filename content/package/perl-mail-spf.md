+++
draft = false
title = "perl-mail-spf v2.9.0-8"
version = "v2.9.0-8"
description = "An object-oriented implementation of Sender Policy Framework"
date = "2024-01-17T13:33:07"
aliases = "/packages/23511"
categories = ['devel-extra']
upstreamurl = "http://cpan.org/"
arch = "x86_64"
size = "107656"
usize = "308068"
sha1sum = "adc74b3476061b2562ca3ac09d82f61d13e8a92f"
depends = "['perl>=5.34.0', 'perl-error', 'perl-net-dns', 'perl-netaddr-ip', 'perl-uri']"
reverse_depends = "['spamassassin']"
+++
An object-oriented implementation of Sender Policy Framework{{< spoiler text="show files" >}}* /usr/bin/site_perl/spfquery
* /usr/bin/spfd
* /usr/lib/perl5/site_perl/Mail/SPF.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Base.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Exception.pm
* /usr/lib/perl5/site_perl/Mail/SPF/MacroString.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Mech.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Mech/A.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Mech/All.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Mech/Exists.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Mech/Include.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Mech/IP4.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Mech/IP6.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Mech/MX.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Mech/PTR.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Mod.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Mod/Exp.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Mod/Redirect.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Record.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Request.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Result.pm
* /usr/lib/perl5/site_perl/Mail/SPF/SenderIPAddrMech.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Server.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Term.pm
* /usr/lib/perl5/site_perl/Mail/SPF/Util.pm
* /usr/lib/perl5/site_perl/Mail/SPF/v1/Record.pm
* /usr/lib/perl5/site_perl/Mail/SPF/v2/Record.pm
* /usr/share/doc/perl-mail-spf-v2.9.0/CHANGES
* /usr/share/doc/perl-mail-spf-v2.9.0/INSTALL
* /usr/share/doc/perl-mail-spf-v2.9.0/LICENSE
* /usr/share/doc/perl-mail-spf-v2.9.0/MANIFEST
* /usr/share/doc/perl-mail-spf-v2.9.0/README
* /usr/share/doc/perl-mail-spf-v2.9.0/TODO
* /usr/share/man/man1/spfquery.1perl.gz
* /usr/share/man/man3/Mail::SPF.3perl.gz
* /usr/share/man/man3/Mail::SPF::Base.3perl.gz
* /usr/share/man/man3/Mail::SPF::MacroString.3perl.gz
* /usr/share/man/man3/Mail::SPF::Mech.3perl.gz
* /usr/share/man/man3/Mail::SPF::Mech::A.3perl.gz
* /usr/share/man/man3/Mail::SPF::Mech::All.3perl.gz
* /usr/share/man/man3/Mail::SPF::Mech::Exists.3perl.gz
* /usr/share/man/man3/Mail::SPF::Mech::Include.3perl.gz
* /usr/share/man/man3/Mail::SPF::Mech::IP4.3perl.gz
* /usr/share/man/man3/Mail::SPF::Mech::IP6.3perl.gz
* /usr/share/man/man3/Mail::SPF::Mech::MX.3perl.gz
* /usr/share/man/man3/Mail::SPF::Mech::PTR.3perl.gz
* /usr/share/man/man3/Mail::SPF::Mod.3perl.gz
* /usr/share/man/man3/Mail::SPF::Mod::Exp.3perl.gz
* /usr/share/man/man3/Mail::SPF::Mod::Redirect.3perl.gz
* /usr/share/man/man3/Mail::SPF::Record.3perl.gz
* /usr/share/man/man3/Mail::SPF::Request.3perl.gz
* /usr/share/man/man3/Mail::SPF::Result.3perl.gz
* /usr/share/man/man3/Mail::SPF::SenderIPAddrMech.3perl.gz
* /usr/share/man/man3/Mail::SPF::Server.3perl.gz
* /usr/share/man/man3/Mail::SPF::Term.3perl.gz
* /usr/share/man/man3/Mail::SPF::Util.3perl.gz
* /usr/share/man/man3/Mail::SPF::v1::Record.3perl.gz
* /usr/share/man/man3/Mail::SPF::v2::Record.3perl.gz
{{< /spoiler >}}