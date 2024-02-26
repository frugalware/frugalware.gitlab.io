+++
draft = false
title = "rrdtool 1.8.0-3"
version = "1.8.0-3"
description = "a program to generate fancy graphs from network usage or from any thing is able to meter"
date = "2024-01-14T14:44:25"
aliases = "/packages/3321"
categories = ['xapps-extra']
upstreamurl = "http://oss.oetiker.ch/rrdtool"
arch = "x86_64"
size = "733368"
usize = "2641071"
sha1sum = "43c79bffe80b67d0e726a6e7c79bb2b24625331b"
depends = "['libxml2>=2.9.3-3', 'pango>=1.38.1', 'python3']"
reverse_depends = "['munin']"
+++
a program to generate fancy graphs from network usage or from any thing is able to meter"

{{< files text="show files" >}}* /usr/bin/rrdcached
* /usr/bin/rrdcgi
* /usr/bin/rrdcreate
* /usr/bin/rrdinfo
* /usr/bin/rrdtool
* /usr/bin/rrdupdate
* /usr/include/rrd.h
* /usr/include/rrd_client.h
* /usr/include/rrd_format.h
* /usr/lib/librrd.so
* /usr/lib/librrd.so.8
* /usr/lib/librrd.so.8.3.0
* /usr/lib/perl/5.38.2/RRDp.pm
* /usr/lib/perl/5.38.2/x86_64-linux-thread-multi/auto/RRDp/.packlist
* /usr/lib/perl/5.38.2/x86_64-linux-thread-multi/auto/RRDs/.packlist
* /usr/lib/perl/5.38.2/x86_64-linux-thread-multi/auto/RRDs/RRDs.so
* /usr/lib/perl/5.38.2/x86_64-linux-thread-multi/perllocal.pod
* /usr/lib/perl/5.38.2/x86_64-linux-thread-multi/RRDs.pm
* /usr/lib/pkgconfig/librrd.pc
* /usr/lib/python3.12/site-packages/rrdtool-0.1.10-py3.12.egg-info/dependency_links.txt
* /usr/lib/python3.12/site-packages/rrdtool-0.1.10-py3.12.egg-info/PKG-INFO
* /usr/lib/python3.12/site-packages/rrdtool-0.1.10-py3.12.egg-info/SOURCES.txt
* /usr/lib/python3.12/site-packages/rrdtool-0.1.10-py3.12.egg-info/top_level.txt
* /usr/lib/python3.12/site-packages/rrdtool.cpython-312-x86_64-linux-gnu.so
* /usr/lib/systemd/system/rrdcached.service
* /usr/lib/systemd/system/rrdcached.socket
* /usr/share/doc/rrdtool-1.8.0/CHANGES
* /usr/share/doc/rrdtool-1.8.0/CONTRIBUTORS
* /usr/share/doc/rrdtool-1.8.0/COPYRIGHT
* /usr/share/doc/rrdtool-1.8.0/html/bin_dec_hex.html
* /usr/share/doc/rrdtool-1.8.0/html/cdeftutorial.html
* /usr/share/doc/rrdtool-1.8.0/html/index.html
* /usr/share/doc/rrdtool-1.8.0/html/librrd.html
* /usr/share/doc/rrdtool-1.8.0/html/rpntutorial.html
* /usr/share/doc/rrdtool-1.8.0/html/rrd-beginners.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdbuild.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdcached.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdcgi.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdcreate.html
* /usr/share/doc/rrdtool-1.8.0/html/rrddump.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdfetch.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdfirst.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdflushcached.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdgraph.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdgraph_data.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdgraph_examples.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdgraph_graph.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdgraph_rpn.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdinfo.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdlast.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdlastupdate.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdlist.html
* /usr/share/doc/rrdtool-1.8.0/html/RRDp.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdpython.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdresize.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdrestore.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdruby.html
* /usr/share/doc/rrdtool-1.8.0/html/RRDs.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdthreads.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdtool.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdtune.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdtutorial.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdupdate.html
* /usr/share/doc/rrdtool-1.8.0/html/rrdxport.html
* /usr/share/doc/rrdtool-1.8.0/html/rrd_pdpcalc.html
* /usr/share/doc/rrdtool-1.8.0/LICENSE
* /usr/share/doc/rrdtool-1.8.0/NEWS
* /usr/share/doc/rrdtool-1.8.0/TODO
* /usr/share/doc/rrdtool-1.8.0/txt/bin_dec_hex.pod
* /usr/share/doc/rrdtool-1.8.0/txt/bin_dec_hex.txt
* /usr/share/doc/rrdtool-1.8.0/txt/cdeftutorial.pod
* /usr/share/doc/rrdtool-1.8.0/txt/cdeftutorial.txt
* /usr/share/doc/rrdtool-1.8.0/txt/librrd.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rpntutorial.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rpntutorial.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrd-beginners.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrd-beginners.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdbuild.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdbuild.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdcached.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdcached.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdcgi.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdcgi.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdcreate.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdcreate.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrddump.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrddump.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdfetch.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdfetch.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdfirst.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdfirst.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdflushcached.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdflushcached.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdgraph.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdgraph.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdgraph_data.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdgraph_data.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdgraph_examples.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdgraph_examples.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdgraph_graph.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdgraph_graph.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdgraph_rpn.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdgraph_rpn.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdinfo.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdinfo.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdlast.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdlast.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdlastupdate.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdlastupdate.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdlist.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdlist.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdpython.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdpython.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdresize.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdresize.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdrestore.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdrestore.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdruby.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdruby.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdthreads.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdthreads.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdtool.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdtool.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdtune.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdtune.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdtutorial.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdtutorial.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdupdate.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdupdate.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrdxport.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrdxport.txt
* /usr/share/doc/rrdtool-1.8.0/txt/rrd_pdpcalc.pod
* /usr/share/doc/rrdtool-1.8.0/txt/rrd_pdpcalc.txt
* /usr/share/doc/rrdtool-1.8.0/VERSION
* /usr/share/locale/fr/LC_MESSAGES/rrdtool.mo
* /usr/share/locale/hu/LC_MESSAGES/rrdtool.mo
* /usr/share/man/man1/bin_dec_hex.1.gz
* /usr/share/man/man1/cdeftutorial.1.gz
* /usr/share/man/man1/rpntutorial.1.gz
* /usr/share/man/man1/rrd-beginners.1.gz
* /usr/share/man/man1/rrdbuild.1.gz
* /usr/share/man/man1/rrdcached.1.gz
* /usr/share/man/man1/rrdcgi.1.gz
* /usr/share/man/man1/rrdcreate.1.gz
* /usr/share/man/man1/rrddump.1.gz
* /usr/share/man/man1/rrdfetch.1.gz
* /usr/share/man/man1/rrdfirst.1.gz
* /usr/share/man/man1/rrdflushcached.1.gz
* /usr/share/man/man1/rrdgraph.1.gz
* /usr/share/man/man1/rrdgraph_data.1.gz
* /usr/share/man/man1/rrdgraph_examples.1.gz
* /usr/share/man/man1/rrdgraph_graph.1.gz
* /usr/share/man/man1/rrdgraph_rpn.1.gz
* /usr/share/man/man1/rrdinfo.1.gz
* /usr/share/man/man1/rrdlast.1.gz
* /usr/share/man/man1/rrdlastupdate.1.gz
* /usr/share/man/man1/rrdlist.1.gz
* /usr/share/man/man1/rrdpython.1.gz
* /usr/share/man/man1/rrdresize.1.gz
* /usr/share/man/man1/rrdrestore.1.gz
* /usr/share/man/man1/rrdruby.1.gz
* /usr/share/man/man1/rrdthreads.1.gz
* /usr/share/man/man1/rrdtool.1.gz
* /usr/share/man/man1/rrdtune.1.gz
* /usr/share/man/man1/rrdtutorial.1.gz
* /usr/share/man/man1/rrdupdate.1.gz
* /usr/share/man/man1/rrdxport.1.gz
* /usr/share/man/man1/rrd_pdpcalc.1.gz
* /usr/share/man/man3/librrd.3.gz
* /usr/share/man/man3/RRDp.3perl.gz
* /usr/share/man/man3/RRDs.3perl.gz
* /usr/share/rrdtool/examples/4charts.pl
* /usr/share/rrdtool/examples/bigtops.pl
* /usr/share/rrdtool/examples/cgi-demo.cgi
* /usr/share/rrdtool/examples/minmax.pl
* /usr/share/rrdtool/examples/perftest.pl
* /usr/share/rrdtool/examples/piped-demo.pl
* /usr/share/rrdtool/examples/rrdcached/rrdcached-size.pl
* /usr/share/rrdtool/examples/rrdcached/RRDCached.pm
* /usr/share/rrdtool/examples/shared-demo.pl
* /usr/share/rrdtool/examples/stripes.pl
* /usr/share/rrdtool/examples/stripes.py
{{< /files >}}