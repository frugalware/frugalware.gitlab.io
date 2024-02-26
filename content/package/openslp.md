+++
draft = false
title = "openslp 2.0.0-11"
version = "2.0.0-11"
description = "Service Location Protocol."
date = "2024-01-08T10:42:50"
aliases = "/packages/8873"
categories = ['network']
upstreamurl = "http://www.openslp.org/"
arch = "x86_64"
size = "331324"
usize = "1596445"
sha1sum = "86d92fc2a0286fb69ae93e6cec97c6a3a8aa6519"
depends = "['glibc>=2.29-6', 'openssl>=3.1.0']"
reverse_depends = "['kio-extras', 'open-isns']"
+++
Service Location Protocol.{{< files text="show files" >}}* /etc/slp.conf
* /etc/slp.reg
* /etc/slp.spi
* /usr/bin/slpd
* /usr/bin/slptool
* /usr/include/slp.h
* /usr/lib/libslp.so
* /usr/lib/libslp.so.1
* /usr/lib/libslp.so.1.0.0
* /usr/lib/systemd/system/openslp.service
* /usr/share/doc/openslp-2.0.0/AUTHORS
* /usr/share/doc/openslp-2.0.0/ChangeLog
* /usr/share/doc/openslp-2.0.0/COPYING
* /usr/share/doc/openslp-2.0.0/FAQ
* /usr/share/doc/openslp-2.0.0/html/faq.html
* /usr/share/doc/openslp-2.0.0/html/IntroductionToSLP/index.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/Callbacks.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/Divergence.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/index.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/Security.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPAttrCallback.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPClose.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPDelAttrs.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPDereg.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPError.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPEscape.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPFindAttrs.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPFindScopes.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPFindSrvs.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPFindSrvTypes.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPFree.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPGetProperty.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPGetRefreshInterval.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPOpen.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPParseSrvURL.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPReg.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPRegReport.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPSetProperty.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPSrvTypeCallback.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPSrvURLCallback.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPTypes.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/SLPUnescape.html
* /usr/share/doc/openslp-2.0.0/html/ProgrammersGuide/Syntax.html
* /usr/share/doc/openslp-2.0.0/html/UsersGuide/CommandLine.html
* /usr/share/doc/openslp-2.0.0/html/UsersGuide/FileLocations.html
* /usr/share/doc/openslp-2.0.0/html/UsersGuide/index.html
* /usr/share/doc/openslp-2.0.0/html/UsersGuide/Installation.html
* /usr/share/doc/openslp-2.0.0/html/UsersGuide/Optimization.html
* /usr/share/doc/openslp-2.0.0/html/UsersGuide/Security.html
* /usr/share/doc/openslp-2.0.0/html/UsersGuide/SlpConf.html
* /usr/share/doc/openslp-2.0.0/html/UsersGuide/SlpReg.html
* /usr/share/doc/openslp-2.0.0/html/UsersGuide/WhenToRunSlpd.html
* /usr/share/doc/openslp-2.0.0/html/UsersGuide/WhoShouldRead.html
* /usr/share/doc/openslp-2.0.0/INSTALL
* /usr/share/doc/openslp-2.0.0/NEWS
* /usr/share/doc/openslp-2.0.0/README
* /usr/share/doc/openslp-2.0.0/README.W32
* /usr/share/doc/openslp-2.0.0/rfc/rfc1766.txt
* /usr/share/doc/openslp-2.0.0/rfc/rfc2165.txt
* /usr/share/doc/openslp-2.0.0/rfc/rfc2254.txt
* /usr/share/doc/openslp-2.0.0/rfc/rfc2396.txt
* /usr/share/doc/openslp-2.0.0/rfc/rfc2608.txt
* /usr/share/doc/openslp-2.0.0/rfc/rfc2609.txt
* /usr/share/doc/openslp-2.0.0/rfc/rfc2610.txt
* /usr/share/doc/openslp-2.0.0/rfc/rfc2614.txt
* /usr/share/doc/openslp-2.0.0/rfc/rfc2926.txt
* /usr/share/doc/openslp-2.0.0/rfc/rfc3059.txt
* /usr/share/doc/openslp-2.0.0/rfc/rfc3082.txt
* /usr/share/doc/openslp-2.0.0/rfc/rfc3111.txt
* /usr/share/doc/openslp-2.0.0/rfc/rfc3224.txt
* /usr/share/doc/openslp-2.0.0/rfc/rfc3421.txt
* /usr/share/doc/openslp-2.0.0/rfc/rfc3528.txt
* /usr/share/doc/openslp-2.0.0/security/openslp_security_whitepaper.html
* /usr/share/doc/openslp-2.0.0/security/srvreg-integrity.html
* /usr/share/doc/openslp-2.0.0/security/threat_analysis_min_security.html
* /usr/share/doc/openslp-2.0.0/THANKS
{{< /files >}}