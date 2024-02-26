+++
draft = false
title = "libsepol 3.6-2"
version = "3.6-2"
description = "SELinux binary policy manipulation library"
date = "2024-01-16T12:25:22"
aliases = "/packages/219880"
categories = ['lib-extra']
upstreamurl = "http://userspace.selinuxproject.org"
arch = "x86_64"
size = "451724"
usize = "2638262"
sha1sum = "d022e5b602c831a69b06ca02d8c3b97af227699f"
depends = "['glibc>=2.34']"
reverse_depends = "['libselinux']"
+++
SELinux binary policy manipulation library{{< files text="show files" >}}* /usr/bin/chkcon
* /usr/bin/sepol_check_access
* /usr/bin/sepol_compute_av
* /usr/bin/sepol_compute_member
* /usr/bin/sepol_compute_relabel
* /usr/bin/sepol_validate_transition
* /usr/include/sepol/booleans.h
* /usr/include/sepol/boolean_record.h
* /usr/include/sepol/cil/cil.h
* /usr/include/sepol/context.h
* /usr/include/sepol/context_record.h
* /usr/include/sepol/debug.h
* /usr/include/sepol/errcodes.h
* /usr/include/sepol/handle.h
* /usr/include/sepol/ibendports.h
* /usr/include/sepol/ibendport_record.h
* /usr/include/sepol/ibpkeys.h
* /usr/include/sepol/ibpkey_record.h
* /usr/include/sepol/iface_record.h
* /usr/include/sepol/interfaces.h
* /usr/include/sepol/kernel_to_cil.h
* /usr/include/sepol/kernel_to_conf.h
* /usr/include/sepol/module.h
* /usr/include/sepol/module_to_cil.h
* /usr/include/sepol/nodes.h
* /usr/include/sepol/node_record.h
* /usr/include/sepol/policydb.h
* /usr/include/sepol/policydb/avrule_block.h
* /usr/include/sepol/policydb/avtab.h
* /usr/include/sepol/policydb/conditional.h
* /usr/include/sepol/policydb/constraint.h
* /usr/include/sepol/policydb/context.h
* /usr/include/sepol/policydb/ebitmap.h
* /usr/include/sepol/policydb/expand.h
* /usr/include/sepol/policydb/flask_types.h
* /usr/include/sepol/policydb/hashtab.h
* /usr/include/sepol/policydb/hierarchy.h
* /usr/include/sepol/policydb/link.h
* /usr/include/sepol/policydb/mls_types.h
* /usr/include/sepol/policydb/module.h
* /usr/include/sepol/policydb/polcaps.h
* /usr/include/sepol/policydb/policydb.h
* /usr/include/sepol/policydb/services.h
* /usr/include/sepol/policydb/sidtab.h
* /usr/include/sepol/policydb/symtab.h
* /usr/include/sepol/policydb/util.h
* /usr/include/sepol/ports.h
* /usr/include/sepol/port_record.h
* /usr/include/sepol/sepol.h
* /usr/include/sepol/users.h
* /usr/include/sepol/user_record.h
* /usr/lib/libsepol.a
* /usr/lib/libsepol.so
* /usr/lib/libsepol.so.2
* /usr/lib/pkgconfig/libsepol.pc
* /usr/share/doc/libsepol-3.6/LICENSE
* /usr/share/doc/libsepol-3.6/VERSION
* /usr/share/man/man3/sepol_check_context.3.gz
* /usr/share/man/man8/chkcon.8.gz
* /usr/share/man/man8/genpolbools.8.gz
* /usr/share/man/man8/genpolusers.8.gz
{{< /files >}}