+++
draft = false
title = "subversion-svnserve 1.14.3-1"
version = "1.14.3-1"
description = "Standalone SVN server daemon"
date = "2024-01-14T11:03:28"
aliases = "/packages/14125"
categories = ['devel-extra']
upstreamurl = "http://subversion.apache.org/"
arch = "x86_64"
size = "42904"
usize = "108469"
sha1sum = "6eb5ec46b0153739833779c55b93133964df3e61"
depends = "['apr-util>=1.5.4-3', 'subversion=1.14.3']"
+++
Standalone SVN server daemon"

{{< files text="show files" >}}* /etc/sysconfig/svnserve
* /usr/bin/svnserve
* /usr/lib/systemd/system/svnserve.service
* /usr/share/man/man5/svnserve.conf.5.gz
* /usr/share/man/man8/svnserve.8.gz
{{< /files >}}