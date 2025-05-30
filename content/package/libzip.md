+++
draft = false
title = "libzip 1.11.4-1"
version = "1.11.4-1"
description = "libzip is a C library for reading, creating, and modifying zip archives."
date = "2025-05-27T07:48:23"
aliases = "/packages/23306"
categories = ['lib']
upstreamurl = "http://www.nih.at/libzip/"
arch = "x86_64"
size = "134216"
usize = "1207453"
sha1sum = "0bdbeabc63c0f30cd2cec02c94cbeb7fa500e615"
depends = "['bzip2', 'gnutls', 'openssl>=3.0.7', 'zstd']"
reverse_depends = "['ark', 'ebook-tools', 'libykneomgr', 'naev', 'okular', 'warzone2100']"
+++
### Description: 
libzip is a C library for reading, creating, and modifying zip archives.

### Files: 
* /usr/bin/zipcmp
* /usr/bin/zipmerge
* /usr/bin/ziptool
* /usr/include/zip.h
* /usr/include/zipconf.h
* /usr/lib/cmake/libzip/libzip-bin-targets-release.cmake
* /usr/lib/cmake/libzip/libzip-bin-targets.cmake
* /usr/lib/cmake/libzip/libzip-config-version.cmake
* /usr/lib/cmake/libzip/libzip-config.cmake
* /usr/lib/cmake/libzip/libzip-targets-release.cmake
* /usr/lib/cmake/libzip/libzip-targets.cmake
* /usr/lib/cmake/libzip/modules/FindMbedTLS.cmake
* /usr/lib/cmake/libzip/modules/FindNettle.cmake
* /usr/lib/cmake/libzip/modules/Findzstd.cmake
* /usr/lib/libzip.so
* /usr/lib/libzip.so.5
* /usr/lib/libzip.so.5.5
* /usr/lib/pkgconfig/libzip.pc
* /usr/share/doc/libzip-1.11.4/AUTHORS
* /usr/share/doc/libzip-1.11.4/INSTALL.md
* /usr/share/doc/libzip-1.11.4/LICENSE
* /usr/share/doc/libzip-1.11.4/README.md
* /usr/share/doc/libzip-1.11.4/THANKS
* /usr/share/doc/libzip/libzip/libzip.html
* /usr/share/doc/libzip/libzip/zip.html
* /usr/share/doc/libzip/libzip/zipcmp.html
* /usr/share/doc/libzip/libzip/zipmerge.html
* /usr/share/doc/libzip/libzip/ziptool.html
* /usr/share/doc/libzip/libzip/zip_add.html
* /usr/share/doc/libzip/libzip/zip_add_dir.html
* /usr/share/doc/libzip/libzip/zip_close.html
* /usr/share/doc/libzip/libzip/zip_compression_method_supported.html
* /usr/share/doc/libzip/libzip/zip_delete.html
* /usr/share/doc/libzip/libzip/zip_dir_add.html
* /usr/share/doc/libzip/libzip/zip_discard.html
* /usr/share/doc/libzip/libzip/zip_encryption_method_supported.html
* /usr/share/doc/libzip/libzip/zip_error.html
* /usr/share/doc/libzip/libzip/zip_errors.html
* /usr/share/doc/libzip/libzip/zip_error_clear.html
* /usr/share/doc/libzip/libzip/zip_error_code_system.html
* /usr/share/doc/libzip/libzip/zip_error_code_zip.html
* /usr/share/doc/libzip/libzip/zip_error_fini.html
* /usr/share/doc/libzip/libzip/zip_error_get.html
* /usr/share/doc/libzip/libzip/zip_error_get_sys_type.html
* /usr/share/doc/libzip/libzip/zip_error_init.html
* /usr/share/doc/libzip/libzip/zip_error_init_with_code.html
* /usr/share/doc/libzip/libzip/zip_error_set.html
* /usr/share/doc/libzip/libzip/zip_error_set_from_source.html
* /usr/share/doc/libzip/libzip/zip_error_strerror.html
* /usr/share/doc/libzip/libzip/zip_error_system_type.html
* /usr/share/doc/libzip/libzip/zip_error_to_data.html
* /usr/share/doc/libzip/libzip/zip_error_to_str.html
* /usr/share/doc/libzip/libzip/zip_fclose.html
* /usr/share/doc/libzip/libzip/zip_fdopen.html
* /usr/share/doc/libzip/libzip/zip_file.html
* /usr/share/doc/libzip/libzip/zip_file_add.html
* /usr/share/doc/libzip/libzip/zip_file_attributes_init.html
* /usr/share/doc/libzip/libzip/zip_file_error_clear.html
* /usr/share/doc/libzip/libzip/zip_file_error_get.html
* /usr/share/doc/libzip/libzip/zip_file_extra_fields_count.html
* /usr/share/doc/libzip/libzip/zip_file_extra_fields_count_by_id.html
* /usr/share/doc/libzip/libzip/zip_file_extra_field_delete.html
* /usr/share/doc/libzip/libzip/zip_file_extra_field_delete_by_id.html
* /usr/share/doc/libzip/libzip/zip_file_extra_field_get.html
* /usr/share/doc/libzip/libzip/zip_file_extra_field_get_by_id.html
* /usr/share/doc/libzip/libzip/zip_file_extra_field_set.html
* /usr/share/doc/libzip/libzip/zip_file_get_comment.html
* /usr/share/doc/libzip/libzip/zip_file_get_error.html
* /usr/share/doc/libzip/libzip/zip_file_get_external_attributes.html
* /usr/share/doc/libzip/libzip/zip_file_is_seekable.html
* /usr/share/doc/libzip/libzip/zip_file_rename.html
* /usr/share/doc/libzip/libzip/zip_file_replace.html
* /usr/share/doc/libzip/libzip/zip_file_set_comment.html
* /usr/share/doc/libzip/libzip/zip_file_set_dostime.html
* /usr/share/doc/libzip/libzip/zip_file_set_encryption.html
* /usr/share/doc/libzip/libzip/zip_file_set_external_attributes.html
* /usr/share/doc/libzip/libzip/zip_file_set_mtime.html
* /usr/share/doc/libzip/libzip/zip_file_strerror.html
* /usr/share/doc/libzip/libzip/zip_fopen.html
* /usr/share/doc/libzip/libzip/zip_fopen_encrypted.html
* /usr/share/doc/libzip/libzip/zip_fopen_index.html
* /usr/share/doc/libzip/libzip/zip_fopen_index_encrypted.html
* /usr/share/doc/libzip/libzip/zip_fread.html
* /usr/share/doc/libzip/libzip/zip_fseek.html
* /usr/share/doc/libzip/libzip/zip_ftell.html
* /usr/share/doc/libzip/libzip/zip_get_archive_comment.html
* /usr/share/doc/libzip/libzip/zip_get_archive_flag.html
* /usr/share/doc/libzip/libzip/zip_get_error.html
* /usr/share/doc/libzip/libzip/zip_get_file_comment.html
* /usr/share/doc/libzip/libzip/zip_get_name.html
* /usr/share/doc/libzip/libzip/zip_get_num_entries.html
* /usr/share/doc/libzip/libzip/zip_get_num_files.html
* /usr/share/doc/libzip/libzip/zip_libzip_version.html
* /usr/share/doc/libzip/libzip/zip_name_locate.html
* /usr/share/doc/libzip/libzip/zip_open.html
* /usr/share/doc/libzip/libzip/zip_open_from_source.html
* /usr/share/doc/libzip/libzip/zip_register_cancel_callback_with_state.html
* /usr/share/doc/libzip/libzip/zip_register_progress_callback.html
* /usr/share/doc/libzip/libzip/zip_register_progress_callback_with_state.html
* /usr/share/doc/libzip/libzip/zip_rename.html
* /usr/share/doc/libzip/libzip/zip_replace.html
* /usr/share/doc/libzip/libzip/zip_set_archive_comment.html
* /usr/share/doc/libzip/libzip/zip_set_archive_flag.html
* /usr/share/doc/libzip/libzip/zip_set_default_password.html
* /usr/share/doc/libzip/libzip/zip_set_file_comment.html
* /usr/share/doc/libzip/libzip/zip_set_file_compression.html
* /usr/share/doc/libzip/libzip/zip_source.html
* /usr/share/doc/libzip/libzip/zip_source_begin_write.html
* /usr/share/doc/libzip/libzip/zip_source_begin_write_cloning.html
* /usr/share/doc/libzip/libzip/zip_source_buffer.html
* /usr/share/doc/libzip/libzip/zip_source_buffer_create.html
* /usr/share/doc/libzip/libzip/zip_source_buffer_fragment.html
* /usr/share/doc/libzip/libzip/zip_source_buffer_fragment_create.html
* /usr/share/doc/libzip/libzip/zip_source_close.html
* /usr/share/doc/libzip/libzip/zip_source_commit_write.html
* /usr/share/doc/libzip/libzip/zip_source_error.html
* /usr/share/doc/libzip/libzip/zip_source_file.html
* /usr/share/doc/libzip/libzip/zip_source_filep.html
* /usr/share/doc/libzip/libzip/zip_source_filep_create.html
* /usr/share/doc/libzip/libzip/zip_source_file_create.html
* /usr/share/doc/libzip/libzip/zip_source_free.html
* /usr/share/doc/libzip/libzip/zip_source_function.html
* /usr/share/doc/libzip/libzip/zip_source_function_create.html
* /usr/share/doc/libzip/libzip/ZIP_SOURCE_GET_ARGS.html
* /usr/share/doc/libzip/libzip/zip_source_is_deleted.html
* /usr/share/doc/libzip/libzip/zip_source_is_seekable.html
* /usr/share/doc/libzip/libzip/zip_source_keep.html
* /usr/share/doc/libzip/libzip/zip_source_layered.html
* /usr/share/doc/libzip/libzip/zip_source_layered_create.html
* /usr/share/doc/libzip/libzip/zip_source_make_command_bitmap.html
* /usr/share/doc/libzip/libzip/zip_source_open.html
* /usr/share/doc/libzip/libzip/zip_source_read.html
* /usr/share/doc/libzip/libzip/zip_source_rollback_write.html
* /usr/share/doc/libzip/libzip/zip_source_seek.html
* /usr/share/doc/libzip/libzip/zip_source_seek_compute_offset.html
* /usr/share/doc/libzip/libzip/zip_source_seek_write.html
* /usr/share/doc/libzip/libzip/zip_source_stat.html
* /usr/share/doc/libzip/libzip/zip_source_tell.html
* /usr/share/doc/libzip/libzip/zip_source_tell_write.html
* /usr/share/doc/libzip/libzip/zip_source_win32a.html
* /usr/share/doc/libzip/libzip/zip_source_win32a_create.html
* /usr/share/doc/libzip/libzip/zip_source_win32handle.html
* /usr/share/doc/libzip/libzip/zip_source_win32handle_create.html
* /usr/share/doc/libzip/libzip/zip_source_win32w.html
* /usr/share/doc/libzip/libzip/zip_source_win32w_create.html
* /usr/share/doc/libzip/libzip/zip_source_window_create.html
* /usr/share/doc/libzip/libzip/zip_source_write.html
* /usr/share/doc/libzip/libzip/zip_source_zip.html
* /usr/share/doc/libzip/libzip/zip_source_zip_create.html
* /usr/share/doc/libzip/libzip/zip_source_zip_file.html
* /usr/share/doc/libzip/libzip/zip_source_zip_file_create.html
* /usr/share/doc/libzip/libzip/zip_stat.html
* /usr/share/doc/libzip/libzip/zip_stat_index.html
* /usr/share/doc/libzip/libzip/zip_stat_init.html
* /usr/share/doc/libzip/libzip/zip_strerror.html
* /usr/share/doc/libzip/libzip/zip_unchange.html
* /usr/share/doc/libzip/libzip/zip_unchange_all.html
* /usr/share/doc/libzip/libzip/zip_unchange_archive.html
