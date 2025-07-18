+++
draft = false
title = "perl-mail-dkim 1.20240923-2"
version = "1.20240923-2"
description = "Signs/verifies Internet mail with DKIM/DomainKey signatures"
date = "2025-07-04T11:22:51"
aliases = "/packages/23496"
categories = ['devel-extra']
upstreamurl = "http://cpan.org/"
arch = "x86_64"
size = "138252"
usize = "408359"
sha1sum = "b476e2e0b01fd3c3226b65f14025eb595116d277"
depends = "['perl-crypt-openssl-rsa>=0.24', 'perl-digest-sha1', 'perl-mailtools', 'perl-net-dns']"
reverse_depends = "['spamassassin']"
+++
### Description: 
Signs/verifies Internet mail with DKIM/DomainKey signatures

### Files: 
* /usr/lib/perl5/site_perl/Mail/DKIM.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Algorithm/Base.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Algorithm/dk_rsa_sha1.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Algorithm/ed25519_sha256.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Algorithm/rsa_sha1.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Algorithm/rsa_sha256.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/ARC/MessageSignature.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/ARC/Seal.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/ARC/Signer.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/ARC/Verifier.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/AuthorDomainPolicy.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Canonicalization/Base.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Canonicalization/DkCommon.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Canonicalization/DkimCommon.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Canonicalization/dk_nofws.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Canonicalization/dk_simple.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Canonicalization/nowsp.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Canonicalization/relaxed.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Canonicalization/seal.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Canonicalization/simple.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Common.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/DkimPolicy.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/DkPolicy.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/DkSignature.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/DNS.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Key.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/KeyValueList.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/MessageParser.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Policy.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/PrivateKey.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/PublicKey.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Signature.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Signer.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/SignerPolicy.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/TextWrap.pm
* /usr/lib/perl5/site_perl/Mail/DKIM/Verifier.pm
* /usr/share/doc/perl-mail-dkim-1.20240923/LICENSE
* /usr/share/doc/perl-mail-dkim-1.20240923/MANIFEST
* /usr/share/doc/perl-mail-dkim-1.20240923/README
* /usr/share/doc/perl-mail-dkim-1.20240923/README.md
* /usr/share/doc/perl-mail-dkim-1.20240923/TODO
* /usr/share/man/man3/Mail::DKIM.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Algorithm::Base.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Algorithm::dk_rsa_sha1.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Algorithm::ed25519_sha256.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Algorithm::rsa_sha1.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Algorithm::rsa_sha256.3perl.gz
* /usr/share/man/man3/Mail::DKIM::ARC::MessageSignature.3perl.gz
* /usr/share/man/man3/Mail::DKIM::ARC::Seal.3perl.gz
* /usr/share/man/man3/Mail::DKIM::ARC::Signer.3perl.gz
* /usr/share/man/man3/Mail::DKIM::ARC::Verifier.3perl.gz
* /usr/share/man/man3/Mail::DKIM::AuthorDomainPolicy.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Canonicalization::Base.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Canonicalization::DkCommon.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Canonicalization::DkimCommon.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Canonicalization::dk_nofws.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Canonicalization::dk_simple.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Canonicalization::nowsp.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Canonicalization::relaxed.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Canonicalization::seal.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Canonicalization::simple.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Common.3perl.gz
* /usr/share/man/man3/Mail::DKIM::DkimPolicy.3perl.gz
* /usr/share/man/man3/Mail::DKIM::DkPolicy.3perl.gz
* /usr/share/man/man3/Mail::DKIM::DkSignature.3perl.gz
* /usr/share/man/man3/Mail::DKIM::DNS.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Key.3perl.gz
* /usr/share/man/man3/Mail::DKIM::KeyValueList.3perl.gz
* /usr/share/man/man3/Mail::DKIM::MessageParser.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Policy.3perl.gz
* /usr/share/man/man3/Mail::DKIM::PrivateKey.3perl.gz
* /usr/share/man/man3/Mail::DKIM::PublicKey.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Signature.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Signer.3perl.gz
* /usr/share/man/man3/Mail::DKIM::SignerPolicy.3perl.gz
* /usr/share/man/man3/Mail::DKIM::TextWrap.3perl.gz
* /usr/share/man/man3/Mail::DKIM::Verifier.3perl.gz
