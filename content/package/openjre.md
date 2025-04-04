+++
draft = false
title = "openjre 23.0.2-1"
version = "23.0.2-1"
description = "Open-source Java Runtime Environment."
date = "2025-01-23T14:53:53"
aliases = "/packages/102858"
categories = ['apps']
upstreamurl = "http://openjdk.java.net/"
arch = "x86_64"
size = "52546380"
usize = "214694164"
sha1sum = "ed4253d3be3f41132ee68042af4bc5e8f255cf5b"
depends = "['ca-certificates-java', 'harfbuzz', 'lcms2', 'libkrb5', 'libpulse>=7.1', 'libuuid>=2.40.2', 'lksctp-tools>=1.0.18-2', 'nss', 'pcsc-lite']"
reverse_depends = "['antlr-openjava', 'apache-ant', 'apache-log4j1', 'bcel', 'bcprov', 'bouncycastle-mail', 'commons-cli', 'commons-codec', 'commons-io', 'commons-logging', 'dom4j', 'freerapid', 'gnu-crypto', 'gnuinetlib', 'gradle', 'insight-toolkit', 'iso-relax', 'itext-core', 'jaf', 'jakarta-oro', 'jakarta-regexp', 'java-hamcrest', 'javacup', 'libreoffice', 'lxmed', 'ntru', 'oneswarm', 'openjdk', 'openjre-x', 'rhino', 'sac', 'servletapi', 'subversion-bindings', 'sweethome3d', 'swt', 'vtk-java', 'xalan-j-serializer', 'xjavac', 'xml-commons-resolver']"
+++
### Description: 
Open-source Java Runtime Environment.

### Files: 
* /etc/java/jaxp-strict.properties.template
* /etc/java/jaxp.properties
* /etc/java/logging.properties
* /etc/java/management/jmxremote.access
* /etc/java/management/jmxremote.password.template
* /etc/java/management/management.properties
* /etc/java/net.properties
* /etc/java/sdp/sdp.conf.template
* /etc/java/security/java.policy
* /etc/java/security/java.security
* /etc/java/security/policy/limited/default_local.policy
* /etc/java/security/policy/limited/default_US_export.policy
* /etc/java/security/policy/limited/exempt_local.policy
* /etc/java/security/policy/README.txt
* /etc/java/security/policy/unlimited/default_local.policy
* /etc/java/security/policy/unlimited/default_US_export.policy
* /etc/java/sound.properties
* /etc/ld.so.conf.d/openjre.conf
* /etc/profile.d/openjre.sh
* /usr/lib/jvm/java-23-openjdk/bin/java
* /usr/lib/jvm/java-23-openjdk/bin/java.debuginfo
* /usr/lib/jvm/java-23-openjdk/bin/jfr
* /usr/lib/jvm/java-23-openjdk/bin/jfr.debuginfo
* /usr/lib/jvm/java-23-openjdk/bin/jrunscript
* /usr/lib/jvm/java-23-openjdk/bin/jrunscript.debuginfo
* /usr/lib/jvm/java-23-openjdk/bin/jwebserver
* /usr/lib/jvm/java-23-openjdk/bin/jwebserver.debuginfo
* /usr/lib/jvm/java-23-openjdk/bin/keytool
* /usr/lib/jvm/java-23-openjdk/bin/keytool.debuginfo
* /usr/lib/jvm/java-23-openjdk/bin/rmiregistry
* /usr/lib/jvm/java-23-openjdk/bin/rmiregistry.debuginfo
* /usr/lib/jvm/java-23-openjdk/conf
* /usr/lib/jvm/java-23-openjdk/lib/classlist
* /usr/lib/jvm/java-23-openjdk/lib/ct.sym
* /usr/lib/jvm/java-23-openjdk/lib/jexec
* /usr/lib/jvm/java-23-openjdk/lib/jexec.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/jfr/default.jfc
* /usr/lib/jvm/java-23-openjdk/lib/jfr/profile.jfc
* /usr/lib/jvm/java-23-openjdk/lib/jrt-fs.jar
* /usr/lib/jvm/java-23-openjdk/lib/jspawnhelper
* /usr/lib/jvm/java-23-openjdk/lib/jspawnhelper.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/jvm.cfg
* /usr/lib/jvm/java-23-openjdk/lib/libattach.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libattach.so
* /usr/lib/jvm/java-23-openjdk/lib/libawt.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libawt.so
* /usr/lib/jvm/java-23-openjdk/lib/libawt_headless.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libawt_headless.so
* /usr/lib/jvm/java-23-openjdk/lib/libdt_socket.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libdt_socket.so
* /usr/lib/jvm/java-23-openjdk/lib/libextnet.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libextnet.so
* /usr/lib/jvm/java-23-openjdk/lib/libfontmanager.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libfontmanager.so
* /usr/lib/jvm/java-23-openjdk/lib/libinstrument.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libinstrument.so
* /usr/lib/jvm/java-23-openjdk/lib/libj2gss.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libj2gss.so
* /usr/lib/jvm/java-23-openjdk/lib/libj2pcsc.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libj2pcsc.so
* /usr/lib/jvm/java-23-openjdk/lib/libj2pkcs11.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libj2pkcs11.so
* /usr/lib/jvm/java-23-openjdk/lib/libjaas.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libjaas.so
* /usr/lib/jvm/java-23-openjdk/lib/libjava.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libjava.so
* /usr/lib/jvm/java-23-openjdk/lib/libjavajpeg.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libjavajpeg.so
* /usr/lib/jvm/java-23-openjdk/lib/libjdwp.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libjdwp.so
* /usr/lib/jvm/java-23-openjdk/lib/libjimage.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libjimage.so
* /usr/lib/jvm/java-23-openjdk/lib/libjli.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libjli.so
* /usr/lib/jvm/java-23-openjdk/lib/libjsig.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libjsig.so
* /usr/lib/jvm/java-23-openjdk/lib/libjsvml.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libjsvml.so
* /usr/lib/jvm/java-23-openjdk/lib/liblcms.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/liblcms.so
* /usr/lib/jvm/java-23-openjdk/lib/libmanagement.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libmanagement.so
* /usr/lib/jvm/java-23-openjdk/lib/libmanagement_agent.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libmanagement_agent.so
* /usr/lib/jvm/java-23-openjdk/lib/libmanagement_ext.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libmanagement_ext.so
* /usr/lib/jvm/java-23-openjdk/lib/libmlib_image.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libmlib_image.so
* /usr/lib/jvm/java-23-openjdk/lib/libnet.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libnet.so
* /usr/lib/jvm/java-23-openjdk/lib/libnio.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libnio.so
* /usr/lib/jvm/java-23-openjdk/lib/libprefs.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libprefs.so
* /usr/lib/jvm/java-23-openjdk/lib/librmi.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/librmi.so
* /usr/lib/jvm/java-23-openjdk/lib/libsaproc.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libsaproc.so
* /usr/lib/jvm/java-23-openjdk/lib/libsctp.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libsctp.so
* /usr/lib/jvm/java-23-openjdk/lib/libsimdsort.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libsimdsort.so
* /usr/lib/jvm/java-23-openjdk/lib/libsyslookup.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libsyslookup.so
* /usr/lib/jvm/java-23-openjdk/lib/libverify.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libverify.so
* /usr/lib/jvm/java-23-openjdk/lib/libzip.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/libzip.so
* /usr/lib/jvm/java-23-openjdk/lib/modules
* /usr/lib/jvm/java-23-openjdk/lib/psfont.properties.ja
* /usr/lib/jvm/java-23-openjdk/lib/psfontj2d.properties
* /usr/lib/jvm/java-23-openjdk/lib/security/blocked.certs
* /usr/lib/jvm/java-23-openjdk/lib/security/cacerts
* /usr/lib/jvm/java-23-openjdk/lib/security/default.policy
* /usr/lib/jvm/java-23-openjdk/lib/security/public_suffix_list.dat
* /usr/lib/jvm/java-23-openjdk/lib/server/classes.jsa
* /usr/lib/jvm/java-23-openjdk/lib/server/classes_nocoops.jsa
* /usr/lib/jvm/java-23-openjdk/lib/server/libjsig.so
* /usr/lib/jvm/java-23-openjdk/lib/server/libjvm.debuginfo
* /usr/lib/jvm/java-23-openjdk/lib/server/libjvm.so
* /usr/lib/jvm/java-23-openjdk/lib/tzdb.dat
* /usr/lib/jvm/java-23-openjdk/release
