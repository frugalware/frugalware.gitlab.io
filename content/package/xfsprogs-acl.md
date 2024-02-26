+++
draft = false
title = "xfsprogs-acl 2.3.2-1"
version = "2.3.2-1"
description = "Dynamic library for access control list support."
date = "2024-01-24T18:35:44"
aliases = "/packages/2463"
categories = ['base']
upstreamurl = "http://oss.sgi.com/projects/xfs/"
arch = "x86_64"
size = "155912"
usize = "401858"
sha1sum = "c33a42a6fd4e7a7dc735591933fa6c14cf7e7bbd"
depends = "['xfsprogs-attr>=2.5.1-3']"
reverse_depends = "['aide', 'cdrtools', 'coreutils', 'libisofs', 'libsystemd', 'logrotate', 'tar', 'vim', 'xorriso']"
+++
Dynamic library for access control list support.

{{< files text="show files" >}}* /usr/bin/chacl
* /usr/bin/getfacl
* /usr/bin/setfacl
* /usr/include/acl/libacl.h
* /usr/include/sys/acl.h
* /usr/lib/libacl.so
* /usr/lib/libacl.so.1
* /usr/lib/libacl.so.1.1.2302
* /usr/lib/pkgconfig/libacl.pc
* /usr/share/doc/xfsprogs-acl-2.3.2/AUTHORS
* /usr/share/doc/xfsprogs-acl-2.3.2/CHANGES
* /usr/share/doc/xfsprogs-acl-2.3.2/COPYING
* /usr/share/doc/xfsprogs-acl-2.3.2/COPYING.LGPL
* /usr/share/doc/xfsprogs-acl-2.3.2/extensions.txt
* /usr/share/doc/xfsprogs-acl-2.3.2/libacl.txt
* /usr/share/doc/xfsprogs-acl-2.3.2/LICENSE
* /usr/share/doc/xfsprogs-acl-2.3.2/README
* /usr/share/doc/xfsprogs-acl-2.3.2/README.md
* /usr/share/locale/de/LC_MESSAGES/acl.mo
* /usr/share/locale/en@boldquot/LC_MESSAGES/acl.mo
* /usr/share/locale/en@quot/LC_MESSAGES/acl.mo
* /usr/share/locale/es/LC_MESSAGES/acl.mo
* /usr/share/locale/fr/LC_MESSAGES/acl.mo
* /usr/share/locale/gl/LC_MESSAGES/acl.mo
* /usr/share/locale/ka/LC_MESSAGES/acl.mo
* /usr/share/locale/pl/LC_MESSAGES/acl.mo
* /usr/share/locale/sv/LC_MESSAGES/acl.mo
* /usr/share/man/man1/chacl.1.gz
* /usr/share/man/man1/getfacl.1.gz
* /usr/share/man/man1/setfacl.1.gz
* /usr/share/man/man3/acl_add_perm.3.gz
* /usr/share/man/man3/acl_calc_mask.3.gz
* /usr/share/man/man3/acl_check.3.gz
* /usr/share/man/man3/acl_clear_perms.3.gz
* /usr/share/man/man3/acl_cmp.3.gz
* /usr/share/man/man3/acl_copy_entry.3.gz
* /usr/share/man/man3/acl_copy_ext.3.gz
* /usr/share/man/man3/acl_copy_int.3.gz
* /usr/share/man/man3/acl_create_entry.3.gz
* /usr/share/man/man3/acl_delete_def_file.3.gz
* /usr/share/man/man3/acl_delete_entry.3.gz
* /usr/share/man/man3/acl_delete_perm.3.gz
* /usr/share/man/man3/acl_dup.3.gz
* /usr/share/man/man3/acl_entries.3.gz
* /usr/share/man/man3/acl_equiv_mode.3.gz
* /usr/share/man/man3/acl_error.3.gz
* /usr/share/man/man3/acl_extended_fd.3.gz
* /usr/share/man/man3/acl_extended_file.3.gz
* /usr/share/man/man3/acl_extended_file_nofollow.3.gz
* /usr/share/man/man3/acl_free.3.gz
* /usr/share/man/man3/acl_from_mode.3.gz
* /usr/share/man/man3/acl_from_text.3.gz
* /usr/share/man/man3/acl_get_entry.3.gz
* /usr/share/man/man3/acl_get_fd.3.gz
* /usr/share/man/man3/acl_get_file.3.gz
* /usr/share/man/man3/acl_get_perm.3.gz
* /usr/share/man/man3/acl_get_permset.3.gz
* /usr/share/man/man3/acl_get_qualifier.3.gz
* /usr/share/man/man3/acl_get_tag_type.3.gz
* /usr/share/man/man3/acl_init.3.gz
* /usr/share/man/man3/acl_set_fd.3.gz
* /usr/share/man/man3/acl_set_file.3.gz
* /usr/share/man/man3/acl_set_permset.3.gz
* /usr/share/man/man3/acl_set_qualifier.3.gz
* /usr/share/man/man3/acl_set_tag_type.3.gz
* /usr/share/man/man3/acl_size.3.gz
* /usr/share/man/man3/acl_to_any_text.3.gz
* /usr/share/man/man3/acl_to_text.3.gz
* /usr/share/man/man3/acl_valid.3.gz
* /usr/share/man/man5/acl.5.gz
{{< /files >}}