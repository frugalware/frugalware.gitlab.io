+++
draft = false
title = "restinio 0.7.3-1"
version = "0.7.3-1"
description = "Header-only C++14 library that gives you an embedded HTTP/Websocket server"
date = "2024-12-17T10:53:48"
aliases = "/packages/220118"
categories = ['devel-extra']
upstreamurl = "https://stiffstream.com/en/products/restinio.html"
arch = "x86_64"
size = "186200"
usize = "1174562"
sha1sum = "fe3f84d61ba6b57b8336e02ee5b386191b11ea78"
depends = "['glibc']"
reverse_depends = "['opendht']"
+++
### Description: 
Header-only C++14 library that gives you an embedded HTTP/Websocket server

### Files: 
* /usr/include/llhttp.h
* /usr/include/restinio/all.hpp
* /usr/include/restinio/asio_include.hpp
* /usr/include/restinio/asio_timer_manager.hpp
* /usr/include/restinio/async_chain/common.hpp
* /usr/include/restinio/async_chain/fixed_size.hpp
* /usr/include/restinio/async_chain/growable_size.hpp
* /usr/include/restinio/buffers.hpp
* /usr/include/restinio/cast_to.hpp
* /usr/include/restinio/chunked_input_info.hpp
* /usr/include/restinio/common_types.hpp
* /usr/include/restinio/compiler_features.hpp
* /usr/include/restinio/connection_count_limiter.hpp
* /usr/include/restinio/connection_state_listener.hpp
* /usr/include/restinio/core.hpp
* /usr/include/restinio/default_strands.hpp
* /usr/include/restinio/detect_os.hpp
* /usr/include/restinio/exception.hpp
* /usr/include/restinio/expected.hpp
* /usr/include/restinio/helpers/easy_parser.hpp
* /usr/include/restinio/helpers/file_upload.hpp
* /usr/include/restinio/helpers/http_field_parsers/accept-charset.hpp
* /usr/include/restinio/helpers/http_field_parsers/accept-encoding.hpp
* /usr/include/restinio/helpers/http_field_parsers/accept-language.hpp
* /usr/include/restinio/helpers/http_field_parsers/accept.hpp
* /usr/include/restinio/helpers/http_field_parsers/authorization.hpp
* /usr/include/restinio/helpers/http_field_parsers/basics.hpp
* /usr/include/restinio/helpers/http_field_parsers/basic_auth.hpp
* /usr/include/restinio/helpers/http_field_parsers/bearer_auth.hpp
* /usr/include/restinio/helpers/http_field_parsers/cache-control.hpp
* /usr/include/restinio/helpers/http_field_parsers/connection.hpp
* /usr/include/restinio/helpers/http_field_parsers/content-disposition.hpp
* /usr/include/restinio/helpers/http_field_parsers/content-encoding.hpp
* /usr/include/restinio/helpers/http_field_parsers/content-type.hpp
* /usr/include/restinio/helpers/http_field_parsers/details/pct_encoded_symbols.hpp
* /usr/include/restinio/helpers/http_field_parsers/host.hpp
* /usr/include/restinio/helpers/http_field_parsers/media-type.hpp
* /usr/include/restinio/helpers/http_field_parsers/range.hpp
* /usr/include/restinio/helpers/http_field_parsers/transfer-encoding.hpp
* /usr/include/restinio/helpers/http_field_parsers/try_parse_field.hpp
* /usr/include/restinio/helpers/http_field_parsers/user-agent.hpp
* /usr/include/restinio/helpers/multipart_body.hpp
* /usr/include/restinio/helpers/string_algo.hpp
* /usr/include/restinio/http_headers.hpp
* /usr/include/restinio/http_server.hpp
* /usr/include/restinio/http_server_run.hpp
* /usr/include/restinio/impl/acceptor.hpp
* /usr/include/restinio/impl/connection.hpp
* /usr/include/restinio/impl/connection_base.hpp
* /usr/include/restinio/impl/connection_settings.hpp
* /usr/include/restinio/impl/executor_wrapper.hpp
* /usr/include/restinio/impl/fixed_buffer.hpp
* /usr/include/restinio/impl/header_helpers.hpp
* /usr/include/restinio/impl/include_fmtlib.hpp
* /usr/include/restinio/impl/ioctx_on_thread_pool.hpp
* /usr/include/restinio/impl/os_posix.ipp
* /usr/include/restinio/impl/os_unknown.ipp
* /usr/include/restinio/impl/os_win.ipp
* /usr/include/restinio/impl/overflow_controlled_integer_accumulator.hpp
* /usr/include/restinio/impl/parser_callbacks.ipp
* /usr/include/restinio/impl/response_coordinator.hpp
* /usr/include/restinio/impl/sendfile_operation.hpp
* /usr/include/restinio/impl/sendfile_operation_default.ipp
* /usr/include/restinio/impl/sendfile_operation_posix.ipp
* /usr/include/restinio/impl/sendfile_operation_win.ipp
* /usr/include/restinio/impl/string_caseless_compare.hpp
* /usr/include/restinio/impl/tls_socket.hpp
* /usr/include/restinio/impl/to_lower_lut.hpp
* /usr/include/restinio/impl/write_group_output_ctx.hpp
* /usr/include/restinio/incoming_http_msg_limits.hpp
* /usr/include/restinio/ip_blocker.hpp
* /usr/include/restinio/message_builders.hpp
* /usr/include/restinio/null_logger.hpp
* /usr/include/restinio/null_mutex.hpp
* /usr/include/restinio/null_timer_manager.hpp
* /usr/include/restinio/os.hpp
* /usr/include/restinio/ostream_logger.hpp
* /usr/include/restinio/path2regex/path2regex.hpp
* /usr/include/restinio/request_handler.hpp
* /usr/include/restinio/router/boost_regex_engine.hpp
* /usr/include/restinio/router/easy_parser_router.hpp
* /usr/include/restinio/router/express.hpp
* /usr/include/restinio/router/impl/target_path_holder.hpp
* /usr/include/restinio/router/method_matcher.hpp
* /usr/include/restinio/router/non_matched_request_handler.hpp
* /usr/include/restinio/router/pcre2_regex_engine.hpp
* /usr/include/restinio/router/pcre_regex_engine.hpp
* /usr/include/restinio/router/std_regex_engine.hpp
* /usr/include/restinio/sendfile.hpp
* /usr/include/restinio/sendfile_defs_default.hpp
* /usr/include/restinio/sendfile_defs_posix.hpp
* /usr/include/restinio/sendfile_defs_win.hpp
* /usr/include/restinio/settings.hpp
* /usr/include/restinio/so5/so_timer_manager.hpp
* /usr/include/restinio/string_view.hpp
* /usr/include/restinio/sync_chain/fixed_size.hpp
* /usr/include/restinio/sync_chain/growable_size.hpp
* /usr/include/restinio/tcp_connection_ctx_base.hpp
* /usr/include/restinio/timer_common.hpp
* /usr/include/restinio/tls.hpp
* /usr/include/restinio/tls_fwd.hpp
* /usr/include/restinio/traits.hpp
* /usr/include/restinio/transforms/zlib.hpp
* /usr/include/restinio/uri_helpers.hpp
* /usr/include/restinio/utils/at_scope_exit.hpp
* /usr/include/restinio/utils/base64.hpp
* /usr/include/restinio/utils/base64_lut.ipp
* /usr/include/restinio/utils/from_string.hpp
* /usr/include/restinio/utils/from_string_details.ipp
* /usr/include/restinio/utils/impl/bitops.hpp
* /usr/include/restinio/utils/impl/safe_uint_truncate.hpp
* /usr/include/restinio/utils/metaprogramming.hpp
* /usr/include/restinio/utils/percent_encoding.hpp
* /usr/include/restinio/utils/sha1.hpp
* /usr/include/restinio/utils/suppress_exceptions.hpp
* /usr/include/restinio/utils/tagged_scalar.hpp
* /usr/include/restinio/utils/tuple_algorithms.hpp
* /usr/include/restinio/utils/utf8_checker.hpp
* /usr/include/restinio/value_or.hpp
* /usr/include/restinio/version.hpp
* /usr/include/restinio/websocket/impl/utf8.hpp
* /usr/include/restinio/websocket/impl/ws_connection.hpp
* /usr/include/restinio/websocket/impl/ws_connection_base.hpp
* /usr/include/restinio/websocket/impl/ws_parser.hpp
* /usr/include/restinio/websocket/impl/ws_protocol_validator.hpp
* /usr/include/restinio/websocket/message.hpp
* /usr/include/restinio/websocket/websocket.hpp
* /usr/lib/cmake/llhttp/llhttp-config-release.cmake
* /usr/lib/cmake/llhttp/llhttp-config.cmake
* /usr/lib/cmake/restinio/restinio-config-version.cmake
* /usr/lib/cmake/restinio/restinio-config.cmake
* /usr/lib/cmake/restinio/restinio-targets.cmake
* /usr/lib/pkgconfig/libllhttp.pc
* /usr/share/doc/restinio-0.7.3/LICENSE
* /usr/share/doc/restinio-0.7.3/README.md
