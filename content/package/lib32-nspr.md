+++
draft = false
title = "lib32-nspr 4.35-2"
version = "4.35-2"
date = "2023-09-04T17:12:49"
categories = ['lib32-extra']
upstreamurl = "http://www.mozilla.org/projects/nspr/"
arch = "x86_64"
size = "196652"
usize = "897506"
sha1sum = "af38b486765777cd17f0eefe6e554150c6544a8b"
depends = "['lib32-glibc>=2.34']"
files = "['usr/', 'usr/i686-frugalware-linux/', 'usr/i686-frugalware-linux/bin/', 'usr/i686-frugalware-linux/bin/nspr-config', 'usr/i686-frugalware-linux/bin/prerr.properties', 'usr/i686-frugalware-linux/include/', 'usr/i686-frugalware-linux/include/nspr', 'usr/i686-frugalware-linux/include/nspr4/', 'usr/i686-frugalware-linux/include/nspr4/md/', 'usr/i686-frugalware-linux/include/nspr4/md/_aix32.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_aix64.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_bsdi.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_darwin.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_freebsd.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_hpux32.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_hpux64.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_linux.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_netbsd.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_nto.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_openbsd.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_os2.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_qnx.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_riscos.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_scoos.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_solaris.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_unixware.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_unixware7.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_win95.cfg', 'usr/i686-frugalware-linux/include/nspr4/md/_winnt.cfg', 'usr/i686-frugalware-linux/include/nspr4/nspr.h', 'usr/i686-frugalware-linux/include/nspr4/obsolete/', 'usr/i686-frugalware-linux/include/nspr4/obsolete/pralarm.h', 'usr/i686-frugalware-linux/include/nspr4/obsolete/probslet.h', 'usr/i686-frugalware-linux/include/nspr4/obsolete/protypes.h', 'usr/i686-frugalware-linux/include/nspr4/obsolete/prsem.h', 'usr/i686-frugalware-linux/include/nspr4/plarena.h', 'usr/i686-frugalware-linux/include/nspr4/plarenas.h', 'usr/i686-frugalware-linux/include/nspr4/plbase64.h', 'usr/i686-frugalware-linux/include/nspr4/plerror.h', 'usr/i686-frugalware-linux/include/nspr4/plgetopt.h', 'usr/i686-frugalware-linux/include/nspr4/plhash.h', 'usr/i686-frugalware-linux/include/nspr4/plstr.h', 'usr/i686-frugalware-linux/include/nspr4/pratom.h', 'usr/i686-frugalware-linux/include/nspr4/prbit.h', 'usr/i686-frugalware-linux/include/nspr4/prclist.h', 'usr/i686-frugalware-linux/include/nspr4/prcmon.h', 'usr/i686-frugalware-linux/include/nspr4/prcountr.h', 'usr/i686-frugalware-linux/include/nspr4/prcpucfg.h', 'usr/i686-frugalware-linux/include/nspr4/prcvar.h', 'usr/i686-frugalware-linux/include/nspr4/prdtoa.h', 'usr/i686-frugalware-linux/include/nspr4/prenv.h', 'usr/i686-frugalware-linux/include/nspr4/prerr.h', 'usr/i686-frugalware-linux/include/nspr4/prerror.h', 'usr/i686-frugalware-linux/include/nspr4/prinet.h', 'usr/i686-frugalware-linux/include/nspr4/prinit.h', 'usr/i686-frugalware-linux/include/nspr4/prinrval.h', 'usr/i686-frugalware-linux/include/nspr4/prio.h', 'usr/i686-frugalware-linux/include/nspr4/pripcsem.h', 'usr/i686-frugalware-linux/include/nspr4/private/', 'usr/i686-frugalware-linux/include/nspr4/private/pprio.h', 'usr/i686-frugalware-linux/include/nspr4/private/pprthred.h', 'usr/i686-frugalware-linux/include/nspr4/private/prpriv.h', 'usr/i686-frugalware-linux/include/nspr4/prlink.h', 'usr/i686-frugalware-linux/include/nspr4/prlock.h', 'usr/i686-frugalware-linux/include/nspr4/prlog.h', 'usr/i686-frugalware-linux/include/nspr4/prlong.h', 'usr/i686-frugalware-linux/include/nspr4/prmem.h', 'usr/i686-frugalware-linux/include/nspr4/prmon.h', 'usr/i686-frugalware-linux/include/nspr4/prmwait.h', 'usr/i686-frugalware-linux/include/nspr4/prnetdb.h', 'usr/i686-frugalware-linux/include/nspr4/prolock.h', 'usr/i686-frugalware-linux/include/nspr4/prpdce.h', 'usr/i686-frugalware-linux/include/nspr4/prprf.h', 'usr/i686-frugalware-linux/include/nspr4/prproces.h', 'usr/i686-frugalware-linux/include/nspr4/prrng.h', 'usr/i686-frugalware-linux/include/nspr4/prrwlock.h', 'usr/i686-frugalware-linux/include/nspr4/prshm.h', 'usr/i686-frugalware-linux/include/nspr4/prshma.h', 'usr/i686-frugalware-linux/include/nspr4/prsystem.h', 'usr/i686-frugalware-linux/include/nspr4/prthread.h', 'usr/i686-frugalware-linux/include/nspr4/prtime.h', 'usr/i686-frugalware-linux/include/nspr4/prtpool.h', 'usr/i686-frugalware-linux/include/nspr4/prtrace.h', 'usr/i686-frugalware-linux/include/nspr4/prtypes.h', 'usr/i686-frugalware-linux/include/nspr4/prvrsion.h', 'usr/i686-frugalware-linux/include/nspr4/prwin16.h', 'usr/lib32/', 'usr/lib32/libnspr4.so', 'usr/lib32/libplc4.so', 'usr/lib32/libplds4.so', 'usr/lib32/pkgconfig/', 'usr/lib32/pkgconfig/nspr.pc']"
+++
NSPR library from mozilla.org ( 32bit )