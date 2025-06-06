+++
draft = false
title = "asio 1.34.2-1"
version = "1.34.2-1"
description = "A a cross-platform C++ library written in C++ for consistent asynchronous I/O."
date = "2025-04-11T10:06:08"
aliases = "/packages/219638"
categories = ['lib-extra']
upstreamurl = "https://sourceforge.net/projects/asio"
arch = "x86_64"
size = "400276"
usize = "5083508"
sha1sum = "c4b442cf894677891ef3e9df27801a5fc2d493f6"
depends = "[]"
reverse_depends = "['obs-studio', 'opendht']"
+++
### Description: 
A a cross-platform C++ library written in C++ for consistent asynchronous I/O.

### Files: 
* /usr/include/asio.hpp
* /usr/include/asio/any_completion_executor.hpp
* /usr/include/asio/any_completion_handler.hpp
* /usr/include/asio/any_io_executor.hpp
* /usr/include/asio/append.hpp
* /usr/include/asio/associated_allocator.hpp
* /usr/include/asio/associated_cancellation_slot.hpp
* /usr/include/asio/associated_executor.hpp
* /usr/include/asio/associated_immediate_executor.hpp
* /usr/include/asio/associator.hpp
* /usr/include/asio/async_result.hpp
* /usr/include/asio/as_tuple.hpp
* /usr/include/asio/awaitable.hpp
* /usr/include/asio/basic_datagram_socket.hpp
* /usr/include/asio/basic_deadline_timer.hpp
* /usr/include/asio/basic_file.hpp
* /usr/include/asio/basic_io_object.hpp
* /usr/include/asio/basic_random_access_file.hpp
* /usr/include/asio/basic_raw_socket.hpp
* /usr/include/asio/basic_readable_pipe.hpp
* /usr/include/asio/basic_seq_packet_socket.hpp
* /usr/include/asio/basic_serial_port.hpp
* /usr/include/asio/basic_signal_set.hpp
* /usr/include/asio/basic_socket.hpp
* /usr/include/asio/basic_socket_acceptor.hpp
* /usr/include/asio/basic_socket_iostream.hpp
* /usr/include/asio/basic_socket_streambuf.hpp
* /usr/include/asio/basic_streambuf.hpp
* /usr/include/asio/basic_streambuf_fwd.hpp
* /usr/include/asio/basic_stream_file.hpp
* /usr/include/asio/basic_stream_socket.hpp
* /usr/include/asio/basic_waitable_timer.hpp
* /usr/include/asio/basic_writable_pipe.hpp
* /usr/include/asio/bind_allocator.hpp
* /usr/include/asio/bind_cancellation_slot.hpp
* /usr/include/asio/bind_executor.hpp
* /usr/include/asio/bind_immediate_executor.hpp
* /usr/include/asio/buffer.hpp
* /usr/include/asio/buffered_read_stream.hpp
* /usr/include/asio/buffered_read_stream_fwd.hpp
* /usr/include/asio/buffered_stream.hpp
* /usr/include/asio/buffered_stream_fwd.hpp
* /usr/include/asio/buffered_write_stream.hpp
* /usr/include/asio/buffered_write_stream_fwd.hpp
* /usr/include/asio/buffers_iterator.hpp
* /usr/include/asio/buffer_registration.hpp
* /usr/include/asio/cancellation_signal.hpp
* /usr/include/asio/cancellation_state.hpp
* /usr/include/asio/cancellation_type.hpp
* /usr/include/asio/cancel_after.hpp
* /usr/include/asio/cancel_at.hpp
* /usr/include/asio/completion_condition.hpp
* /usr/include/asio/compose.hpp
* /usr/include/asio/composed.hpp
* /usr/include/asio/config.hpp
* /usr/include/asio/connect.hpp
* /usr/include/asio/connect_pipe.hpp
* /usr/include/asio/consign.hpp
* /usr/include/asio/coroutine.hpp
* /usr/include/asio/co_composed.hpp
* /usr/include/asio/co_spawn.hpp
* /usr/include/asio/deadline_timer.hpp
* /usr/include/asio/default_completion_token.hpp
* /usr/include/asio/defer.hpp
* /usr/include/asio/deferred.hpp
* /usr/include/asio/detached.hpp
* /usr/include/asio/detail/array.hpp
* /usr/include/asio/detail/array_fwd.hpp
* /usr/include/asio/detail/assert.hpp
* /usr/include/asio/detail/atomic_count.hpp
* /usr/include/asio/detail/base_from_cancellation_state.hpp
* /usr/include/asio/detail/base_from_completion_cond.hpp
* /usr/include/asio/detail/bind_handler.hpp
* /usr/include/asio/detail/blocking_executor_op.hpp
* /usr/include/asio/detail/buffered_stream_storage.hpp
* /usr/include/asio/detail/buffer_resize_guard.hpp
* /usr/include/asio/detail/buffer_sequence_adapter.hpp
* /usr/include/asio/detail/call_stack.hpp
* /usr/include/asio/detail/chrono.hpp
* /usr/include/asio/detail/chrono_time_traits.hpp
* /usr/include/asio/detail/completion_handler.hpp
* /usr/include/asio/detail/completion_message.hpp
* /usr/include/asio/detail/completion_payload.hpp
* /usr/include/asio/detail/completion_payload_handler.hpp
* /usr/include/asio/detail/composed_work.hpp
* /usr/include/asio/detail/concurrency_hint.hpp
* /usr/include/asio/detail/conditionally_enabled_event.hpp
* /usr/include/asio/detail/conditionally_enabled_mutex.hpp
* /usr/include/asio/detail/config.hpp
* /usr/include/asio/detail/consuming_buffers.hpp
* /usr/include/asio/detail/cstddef.hpp
* /usr/include/asio/detail/cstdint.hpp
* /usr/include/asio/detail/date_time_fwd.hpp
* /usr/include/asio/detail/deadline_timer_service.hpp
* /usr/include/asio/detail/dependent_type.hpp
* /usr/include/asio/detail/descriptor_ops.hpp
* /usr/include/asio/detail/descriptor_read_op.hpp
* /usr/include/asio/detail/descriptor_write_op.hpp
* /usr/include/asio/detail/dev_poll_reactor.hpp
* /usr/include/asio/detail/epoll_reactor.hpp
* /usr/include/asio/detail/event.hpp
* /usr/include/asio/detail/eventfd_select_interrupter.hpp
* /usr/include/asio/detail/exception.hpp
* /usr/include/asio/detail/executor_function.hpp
* /usr/include/asio/detail/executor_op.hpp
* /usr/include/asio/detail/fd_set_adapter.hpp
* /usr/include/asio/detail/fenced_block.hpp
* /usr/include/asio/detail/functional.hpp
* /usr/include/asio/detail/future.hpp
* /usr/include/asio/detail/global.hpp
* /usr/include/asio/detail/handler_alloc_helpers.hpp
* /usr/include/asio/detail/handler_cont_helpers.hpp
* /usr/include/asio/detail/handler_tracking.hpp
* /usr/include/asio/detail/handler_type_requirements.hpp
* /usr/include/asio/detail/handler_work.hpp
* /usr/include/asio/detail/hash_map.hpp
* /usr/include/asio/detail/impl/buffer_sequence_adapter.ipp
* /usr/include/asio/detail/impl/descriptor_ops.ipp
* /usr/include/asio/detail/impl/dev_poll_reactor.hpp
* /usr/include/asio/detail/impl/dev_poll_reactor.ipp
* /usr/include/asio/detail/impl/epoll_reactor.hpp
* /usr/include/asio/detail/impl/epoll_reactor.ipp
* /usr/include/asio/detail/impl/eventfd_select_interrupter.ipp
* /usr/include/asio/detail/impl/handler_tracking.ipp
* /usr/include/asio/detail/impl/io_uring_descriptor_service.ipp
* /usr/include/asio/detail/impl/io_uring_file_service.ipp
* /usr/include/asio/detail/impl/io_uring_service.hpp
* /usr/include/asio/detail/impl/io_uring_service.ipp
* /usr/include/asio/detail/impl/io_uring_socket_service_base.ipp
* /usr/include/asio/detail/impl/kqueue_reactor.hpp
* /usr/include/asio/detail/impl/kqueue_reactor.ipp
* /usr/include/asio/detail/impl/null_event.ipp
* /usr/include/asio/detail/impl/pipe_select_interrupter.ipp
* /usr/include/asio/detail/impl/posix_event.ipp
* /usr/include/asio/detail/impl/posix_mutex.ipp
* /usr/include/asio/detail/impl/posix_serial_port_service.ipp
* /usr/include/asio/detail/impl/posix_thread.ipp
* /usr/include/asio/detail/impl/posix_tss_ptr.ipp
* /usr/include/asio/detail/impl/reactive_descriptor_service.ipp
* /usr/include/asio/detail/impl/reactive_socket_service_base.ipp
* /usr/include/asio/detail/impl/resolver_service_base.ipp
* /usr/include/asio/detail/impl/scheduler.ipp
* /usr/include/asio/detail/impl/select_reactor.hpp
* /usr/include/asio/detail/impl/select_reactor.ipp
* /usr/include/asio/detail/impl/service_registry.hpp
* /usr/include/asio/detail/impl/service_registry.ipp
* /usr/include/asio/detail/impl/signal_set_service.ipp
* /usr/include/asio/detail/impl/socket_ops.ipp
* /usr/include/asio/detail/impl/socket_select_interrupter.ipp
* /usr/include/asio/detail/impl/strand_executor_service.hpp
* /usr/include/asio/detail/impl/strand_executor_service.ipp
* /usr/include/asio/detail/impl/strand_service.hpp
* /usr/include/asio/detail/impl/strand_service.ipp
* /usr/include/asio/detail/impl/thread_context.ipp
* /usr/include/asio/detail/impl/throw_error.ipp
* /usr/include/asio/detail/impl/timer_queue_ptime.ipp
* /usr/include/asio/detail/impl/timer_queue_set.ipp
* /usr/include/asio/detail/impl/winrt_ssocket_service_base.ipp
* /usr/include/asio/detail/impl/winrt_timer_scheduler.hpp
* /usr/include/asio/detail/impl/winrt_timer_scheduler.ipp
* /usr/include/asio/detail/impl/winsock_init.ipp
* /usr/include/asio/detail/impl/win_event.ipp
* /usr/include/asio/detail/impl/win_iocp_file_service.ipp
* /usr/include/asio/detail/impl/win_iocp_handle_service.ipp
* /usr/include/asio/detail/impl/win_iocp_io_context.hpp
* /usr/include/asio/detail/impl/win_iocp_io_context.ipp
* /usr/include/asio/detail/impl/win_iocp_serial_port_service.ipp
* /usr/include/asio/detail/impl/win_iocp_socket_service_base.ipp
* /usr/include/asio/detail/impl/win_mutex.ipp
* /usr/include/asio/detail/impl/win_object_handle_service.ipp
* /usr/include/asio/detail/impl/win_static_mutex.ipp
* /usr/include/asio/detail/impl/win_thread.ipp
* /usr/include/asio/detail/impl/win_tss_ptr.ipp
* /usr/include/asio/detail/initiate_defer.hpp
* /usr/include/asio/detail/initiate_dispatch.hpp
* /usr/include/asio/detail/initiate_post.hpp
* /usr/include/asio/detail/initiation_base.hpp
* /usr/include/asio/detail/io_control.hpp
* /usr/include/asio/detail/io_object_impl.hpp
* /usr/include/asio/detail/io_uring_descriptor_read_at_op.hpp
* /usr/include/asio/detail/io_uring_descriptor_read_op.hpp
* /usr/include/asio/detail/io_uring_descriptor_service.hpp
* /usr/include/asio/detail/io_uring_descriptor_write_at_op.hpp
* /usr/include/asio/detail/io_uring_descriptor_write_op.hpp
* /usr/include/asio/detail/io_uring_file_service.hpp
* /usr/include/asio/detail/io_uring_null_buffers_op.hpp
* /usr/include/asio/detail/io_uring_operation.hpp
* /usr/include/asio/detail/io_uring_service.hpp
* /usr/include/asio/detail/io_uring_socket_accept_op.hpp
* /usr/include/asio/detail/io_uring_socket_connect_op.hpp
* /usr/include/asio/detail/io_uring_socket_recvfrom_op.hpp
* /usr/include/asio/detail/io_uring_socket_recvmsg_op.hpp
* /usr/include/asio/detail/io_uring_socket_recv_op.hpp
* /usr/include/asio/detail/io_uring_socket_sendto_op.hpp
* /usr/include/asio/detail/io_uring_socket_send_op.hpp
* /usr/include/asio/detail/io_uring_socket_service.hpp
* /usr/include/asio/detail/io_uring_socket_service_base.hpp
* /usr/include/asio/detail/io_uring_wait_op.hpp
* /usr/include/asio/detail/is_buffer_sequence.hpp
* /usr/include/asio/detail/is_executor.hpp
* /usr/include/asio/detail/keyword_tss_ptr.hpp
* /usr/include/asio/detail/kqueue_reactor.hpp
* /usr/include/asio/detail/limits.hpp
* /usr/include/asio/detail/local_free_on_block_exit.hpp
* /usr/include/asio/detail/memory.hpp
* /usr/include/asio/detail/mutex.hpp
* /usr/include/asio/detail/noncopyable.hpp
* /usr/include/asio/detail/non_const_lvalue.hpp
* /usr/include/asio/detail/null_event.hpp
* /usr/include/asio/detail/null_fenced_block.hpp
* /usr/include/asio/detail/null_global.hpp
* /usr/include/asio/detail/null_mutex.hpp
* /usr/include/asio/detail/null_reactor.hpp
* /usr/include/asio/detail/null_signal_blocker.hpp
* /usr/include/asio/detail/null_socket_service.hpp
* /usr/include/asio/detail/null_static_mutex.hpp
* /usr/include/asio/detail/null_thread.hpp
* /usr/include/asio/detail/null_tss_ptr.hpp
* /usr/include/asio/detail/object_pool.hpp
* /usr/include/asio/detail/old_win_sdk_compat.hpp
* /usr/include/asio/detail/operation.hpp
* /usr/include/asio/detail/op_queue.hpp
* /usr/include/asio/detail/pipe_select_interrupter.hpp
* /usr/include/asio/detail/pop_options.hpp
* /usr/include/asio/detail/posix_event.hpp
* /usr/include/asio/detail/posix_fd_set_adapter.hpp
* /usr/include/asio/detail/posix_global.hpp
* /usr/include/asio/detail/posix_mutex.hpp
* /usr/include/asio/detail/posix_serial_port_service.hpp
* /usr/include/asio/detail/posix_signal_blocker.hpp
* /usr/include/asio/detail/posix_static_mutex.hpp
* /usr/include/asio/detail/posix_thread.hpp
* /usr/include/asio/detail/posix_tss_ptr.hpp
* /usr/include/asio/detail/push_options.hpp
* /usr/include/asio/detail/reactive_descriptor_service.hpp
* /usr/include/asio/detail/reactive_null_buffers_op.hpp
* /usr/include/asio/detail/reactive_socket_accept_op.hpp
* /usr/include/asio/detail/reactive_socket_connect_op.hpp
* /usr/include/asio/detail/reactive_socket_recvfrom_op.hpp
* /usr/include/asio/detail/reactive_socket_recvmsg_op.hpp
* /usr/include/asio/detail/reactive_socket_recv_op.hpp
* /usr/include/asio/detail/reactive_socket_sendto_op.hpp
* /usr/include/asio/detail/reactive_socket_send_op.hpp
* /usr/include/asio/detail/reactive_socket_service.hpp
* /usr/include/asio/detail/reactive_socket_service_base.hpp
* /usr/include/asio/detail/reactive_wait_op.hpp
* /usr/include/asio/detail/reactor.hpp
* /usr/include/asio/detail/reactor_op.hpp
* /usr/include/asio/detail/reactor_op_queue.hpp
* /usr/include/asio/detail/recycling_allocator.hpp
* /usr/include/asio/detail/regex_fwd.hpp
* /usr/include/asio/detail/resolver_service.hpp
* /usr/include/asio/detail/resolver_service_base.hpp
* /usr/include/asio/detail/resolve_endpoint_op.hpp
* /usr/include/asio/detail/resolve_op.hpp
* /usr/include/asio/detail/resolve_query_op.hpp
* /usr/include/asio/detail/scheduler.hpp
* /usr/include/asio/detail/scheduler_operation.hpp
* /usr/include/asio/detail/scheduler_task.hpp
* /usr/include/asio/detail/scheduler_thread_info.hpp
* /usr/include/asio/detail/scoped_lock.hpp
* /usr/include/asio/detail/scoped_ptr.hpp
* /usr/include/asio/detail/select_interrupter.hpp
* /usr/include/asio/detail/select_reactor.hpp
* /usr/include/asio/detail/service_registry.hpp
* /usr/include/asio/detail/signal_blocker.hpp
* /usr/include/asio/detail/signal_handler.hpp
* /usr/include/asio/detail/signal_init.hpp
* /usr/include/asio/detail/signal_op.hpp
* /usr/include/asio/detail/signal_set_service.hpp
* /usr/include/asio/detail/socket_holder.hpp
* /usr/include/asio/detail/socket_ops.hpp
* /usr/include/asio/detail/socket_option.hpp
* /usr/include/asio/detail/socket_select_interrupter.hpp
* /usr/include/asio/detail/socket_types.hpp
* /usr/include/asio/detail/source_location.hpp
* /usr/include/asio/detail/static_mutex.hpp
* /usr/include/asio/detail/std_event.hpp
* /usr/include/asio/detail/std_fenced_block.hpp
* /usr/include/asio/detail/std_global.hpp
* /usr/include/asio/detail/std_mutex.hpp
* /usr/include/asio/detail/std_static_mutex.hpp
* /usr/include/asio/detail/std_thread.hpp
* /usr/include/asio/detail/strand_executor_service.hpp
* /usr/include/asio/detail/strand_service.hpp
* /usr/include/asio/detail/string_view.hpp
* /usr/include/asio/detail/thread.hpp
* /usr/include/asio/detail/thread_context.hpp
* /usr/include/asio/detail/thread_group.hpp
* /usr/include/asio/detail/thread_info_base.hpp
* /usr/include/asio/detail/throw_error.hpp
* /usr/include/asio/detail/throw_exception.hpp
* /usr/include/asio/detail/timed_cancel_op.hpp
* /usr/include/asio/detail/timer_queue.hpp
* /usr/include/asio/detail/timer_queue_base.hpp
* /usr/include/asio/detail/timer_queue_ptime.hpp
* /usr/include/asio/detail/timer_queue_set.hpp
* /usr/include/asio/detail/timer_scheduler.hpp
* /usr/include/asio/detail/timer_scheduler_fwd.hpp
* /usr/include/asio/detail/tss_ptr.hpp
* /usr/include/asio/detail/type_traits.hpp
* /usr/include/asio/detail/utility.hpp
* /usr/include/asio/detail/wait_handler.hpp
* /usr/include/asio/detail/wait_op.hpp
* /usr/include/asio/detail/winapp_thread.hpp
* /usr/include/asio/detail/wince_thread.hpp
* /usr/include/asio/detail/winrt_async_manager.hpp
* /usr/include/asio/detail/winrt_async_op.hpp
* /usr/include/asio/detail/winrt_resolver_service.hpp
* /usr/include/asio/detail/winrt_resolve_op.hpp
* /usr/include/asio/detail/winrt_socket_connect_op.hpp
* /usr/include/asio/detail/winrt_socket_recv_op.hpp
* /usr/include/asio/detail/winrt_socket_send_op.hpp
* /usr/include/asio/detail/winrt_ssocket_service.hpp
* /usr/include/asio/detail/winrt_ssocket_service_base.hpp
* /usr/include/asio/detail/winrt_timer_scheduler.hpp
* /usr/include/asio/detail/winrt_utils.hpp
* /usr/include/asio/detail/winsock_init.hpp
* /usr/include/asio/detail/win_event.hpp
* /usr/include/asio/detail/win_fd_set_adapter.hpp
* /usr/include/asio/detail/win_global.hpp
* /usr/include/asio/detail/win_iocp_file_service.hpp
* /usr/include/asio/detail/win_iocp_handle_read_op.hpp
* /usr/include/asio/detail/win_iocp_handle_service.hpp
* /usr/include/asio/detail/win_iocp_handle_write_op.hpp
* /usr/include/asio/detail/win_iocp_io_context.hpp
* /usr/include/asio/detail/win_iocp_null_buffers_op.hpp
* /usr/include/asio/detail/win_iocp_operation.hpp
* /usr/include/asio/detail/win_iocp_overlapped_op.hpp
* /usr/include/asio/detail/win_iocp_overlapped_ptr.hpp
* /usr/include/asio/detail/win_iocp_serial_port_service.hpp
* /usr/include/asio/detail/win_iocp_socket_accept_op.hpp
* /usr/include/asio/detail/win_iocp_socket_connect_op.hpp
* /usr/include/asio/detail/win_iocp_socket_recvfrom_op.hpp
* /usr/include/asio/detail/win_iocp_socket_recvmsg_op.hpp
* /usr/include/asio/detail/win_iocp_socket_recv_op.hpp
* /usr/include/asio/detail/win_iocp_socket_send_op.hpp
* /usr/include/asio/detail/win_iocp_socket_service.hpp
* /usr/include/asio/detail/win_iocp_socket_service_base.hpp
* /usr/include/asio/detail/win_iocp_thread_info.hpp
* /usr/include/asio/detail/win_iocp_wait_op.hpp
* /usr/include/asio/detail/win_mutex.hpp
* /usr/include/asio/detail/win_object_handle_service.hpp
* /usr/include/asio/detail/win_static_mutex.hpp
* /usr/include/asio/detail/win_thread.hpp
* /usr/include/asio/detail/win_tss_ptr.hpp
* /usr/include/asio/detail/work_dispatcher.hpp
* /usr/include/asio/detail/wrapped_handler.hpp
* /usr/include/asio/dispatch.hpp
* /usr/include/asio/disposition.hpp
* /usr/include/asio/error.hpp
* /usr/include/asio/error_code.hpp
* /usr/include/asio/execution.hpp
* /usr/include/asio/execution/allocator.hpp
* /usr/include/asio/execution/any_executor.hpp
* /usr/include/asio/execution/bad_executor.hpp
* /usr/include/asio/execution/blocking.hpp
* /usr/include/asio/execution/blocking_adaptation.hpp
* /usr/include/asio/execution/context.hpp
* /usr/include/asio/execution/context_as.hpp
* /usr/include/asio/execution/executor.hpp
* /usr/include/asio/execution/impl/bad_executor.ipp
* /usr/include/asio/execution/invocable_archetype.hpp
* /usr/include/asio/execution/mapping.hpp
* /usr/include/asio/execution/occupancy.hpp
* /usr/include/asio/execution/outstanding_work.hpp
* /usr/include/asio/execution/prefer_only.hpp
* /usr/include/asio/execution/relationship.hpp
* /usr/include/asio/execution_context.hpp
* /usr/include/asio/executor.hpp
* /usr/include/asio/executor_work_guard.hpp
* /usr/include/asio/experimental/as_single.hpp
* /usr/include/asio/experimental/awaitable_operators.hpp
* /usr/include/asio/experimental/basic_channel.hpp
* /usr/include/asio/experimental/basic_concurrent_channel.hpp
* /usr/include/asio/experimental/cancellation_condition.hpp
* /usr/include/asio/experimental/channel.hpp
* /usr/include/asio/experimental/channel_error.hpp
* /usr/include/asio/experimental/channel_traits.hpp
* /usr/include/asio/experimental/concurrent_channel.hpp
* /usr/include/asio/experimental/coro.hpp
* /usr/include/asio/experimental/coro_traits.hpp
* /usr/include/asio/experimental/co_composed.hpp
* /usr/include/asio/experimental/co_spawn.hpp
* /usr/include/asio/experimental/detail/channel_operation.hpp
* /usr/include/asio/experimental/detail/channel_receive_op.hpp
* /usr/include/asio/experimental/detail/channel_send_functions.hpp
* /usr/include/asio/experimental/detail/channel_send_op.hpp
* /usr/include/asio/experimental/detail/channel_service.hpp
* /usr/include/asio/experimental/detail/coro_completion_handler.hpp
* /usr/include/asio/experimental/detail/coro_promise_allocator.hpp
* /usr/include/asio/experimental/detail/has_signature.hpp
* /usr/include/asio/experimental/detail/impl/channel_service.hpp
* /usr/include/asio/experimental/detail/partial_promise.hpp
* /usr/include/asio/experimental/impl/as_single.hpp
* /usr/include/asio/experimental/impl/channel_error.ipp
* /usr/include/asio/experimental/impl/coro.hpp
* /usr/include/asio/experimental/impl/parallel_group.hpp
* /usr/include/asio/experimental/impl/promise.hpp
* /usr/include/asio/experimental/impl/use_coro.hpp
* /usr/include/asio/experimental/impl/use_promise.hpp
* /usr/include/asio/experimental/parallel_group.hpp
* /usr/include/asio/experimental/promise.hpp
* /usr/include/asio/experimental/use_coro.hpp
* /usr/include/asio/experimental/use_promise.hpp
* /usr/include/asio/file_base.hpp
* /usr/include/asio/generic/basic_endpoint.hpp
* /usr/include/asio/generic/datagram_protocol.hpp
* /usr/include/asio/generic/detail/endpoint.hpp
* /usr/include/asio/generic/detail/impl/endpoint.ipp
* /usr/include/asio/generic/raw_protocol.hpp
* /usr/include/asio/generic/seq_packet_protocol.hpp
* /usr/include/asio/generic/stream_protocol.hpp
* /usr/include/asio/handler_continuation_hook.hpp
* /usr/include/asio/high_resolution_timer.hpp
* /usr/include/asio/immediate.hpp
* /usr/include/asio/impl/any_completion_executor.ipp
* /usr/include/asio/impl/any_io_executor.ipp
* /usr/include/asio/impl/append.hpp
* /usr/include/asio/impl/as_tuple.hpp
* /usr/include/asio/impl/awaitable.hpp
* /usr/include/asio/impl/buffered_read_stream.hpp
* /usr/include/asio/impl/buffered_write_stream.hpp
* /usr/include/asio/impl/cancellation_signal.ipp
* /usr/include/asio/impl/cancel_after.hpp
* /usr/include/asio/impl/cancel_at.hpp
* /usr/include/asio/impl/config.hpp
* /usr/include/asio/impl/config.ipp
* /usr/include/asio/impl/connect.hpp
* /usr/include/asio/impl/connect_pipe.hpp
* /usr/include/asio/impl/connect_pipe.ipp
* /usr/include/asio/impl/consign.hpp
* /usr/include/asio/impl/co_spawn.hpp
* /usr/include/asio/impl/deferred.hpp
* /usr/include/asio/impl/detached.hpp
* /usr/include/asio/impl/error.ipp
* /usr/include/asio/impl/error_code.ipp
* /usr/include/asio/impl/execution_context.hpp
* /usr/include/asio/impl/execution_context.ipp
* /usr/include/asio/impl/executor.hpp
* /usr/include/asio/impl/executor.ipp
* /usr/include/asio/impl/io_context.hpp
* /usr/include/asio/impl/io_context.ipp
* /usr/include/asio/impl/multiple_exceptions.ipp
* /usr/include/asio/impl/prepend.hpp
* /usr/include/asio/impl/read.hpp
* /usr/include/asio/impl/read_at.hpp
* /usr/include/asio/impl/read_until.hpp
* /usr/include/asio/impl/redirect_error.hpp
* /usr/include/asio/impl/serial_port_base.hpp
* /usr/include/asio/impl/serial_port_base.ipp
* /usr/include/asio/impl/spawn.hpp
* /usr/include/asio/impl/src.hpp
* /usr/include/asio/impl/system_context.hpp
* /usr/include/asio/impl/system_context.ipp
* /usr/include/asio/impl/system_executor.hpp
* /usr/include/asio/impl/thread_pool.hpp
* /usr/include/asio/impl/thread_pool.ipp
* /usr/include/asio/impl/use_awaitable.hpp
* /usr/include/asio/impl/use_future.hpp
* /usr/include/asio/impl/write.hpp
* /usr/include/asio/impl/write_at.hpp
* /usr/include/asio/io_context.hpp
* /usr/include/asio/io_context_strand.hpp
* /usr/include/asio/ip/address.hpp
* /usr/include/asio/ip/address_v4.hpp
* /usr/include/asio/ip/address_v4_iterator.hpp
* /usr/include/asio/ip/address_v4_range.hpp
* /usr/include/asio/ip/address_v6.hpp
* /usr/include/asio/ip/address_v6_iterator.hpp
* /usr/include/asio/ip/address_v6_range.hpp
* /usr/include/asio/ip/bad_address_cast.hpp
* /usr/include/asio/ip/basic_endpoint.hpp
* /usr/include/asio/ip/basic_resolver.hpp
* /usr/include/asio/ip/basic_resolver_entry.hpp
* /usr/include/asio/ip/basic_resolver_iterator.hpp
* /usr/include/asio/ip/basic_resolver_query.hpp
* /usr/include/asio/ip/basic_resolver_results.hpp
* /usr/include/asio/ip/detail/endpoint.hpp
* /usr/include/asio/ip/detail/impl/endpoint.ipp
* /usr/include/asio/ip/detail/socket_option.hpp
* /usr/include/asio/ip/host_name.hpp
* /usr/include/asio/ip/icmp.hpp
* /usr/include/asio/ip/impl/address.hpp
* /usr/include/asio/ip/impl/address.ipp
* /usr/include/asio/ip/impl/address_v4.hpp
* /usr/include/asio/ip/impl/address_v4.ipp
* /usr/include/asio/ip/impl/address_v6.hpp
* /usr/include/asio/ip/impl/address_v6.ipp
* /usr/include/asio/ip/impl/basic_endpoint.hpp
* /usr/include/asio/ip/impl/host_name.ipp
* /usr/include/asio/ip/impl/network_v4.hpp
* /usr/include/asio/ip/impl/network_v4.ipp
* /usr/include/asio/ip/impl/network_v6.hpp
* /usr/include/asio/ip/impl/network_v6.ipp
* /usr/include/asio/ip/multicast.hpp
* /usr/include/asio/ip/network_v4.hpp
* /usr/include/asio/ip/network_v6.hpp
* /usr/include/asio/ip/resolver_base.hpp
* /usr/include/asio/ip/resolver_query_base.hpp
* /usr/include/asio/ip/tcp.hpp
* /usr/include/asio/ip/udp.hpp
* /usr/include/asio/ip/unicast.hpp
* /usr/include/asio/ip/v6_only.hpp
* /usr/include/asio/is_applicable_property.hpp
* /usr/include/asio/is_contiguous_iterator.hpp
* /usr/include/asio/is_executor.hpp
* /usr/include/asio/is_read_buffered.hpp
* /usr/include/asio/is_write_buffered.hpp
* /usr/include/asio/local/basic_endpoint.hpp
* /usr/include/asio/local/connect_pair.hpp
* /usr/include/asio/local/datagram_protocol.hpp
* /usr/include/asio/local/detail/endpoint.hpp
* /usr/include/asio/local/detail/impl/endpoint.ipp
* /usr/include/asio/local/seq_packet_protocol.hpp
* /usr/include/asio/local/stream_protocol.hpp
* /usr/include/asio/multiple_exceptions.hpp
* /usr/include/asio/packaged_task.hpp
* /usr/include/asio/placeholders.hpp
* /usr/include/asio/posix/basic_descriptor.hpp
* /usr/include/asio/posix/basic_stream_descriptor.hpp
* /usr/include/asio/posix/descriptor.hpp
* /usr/include/asio/posix/descriptor_base.hpp
* /usr/include/asio/posix/stream_descriptor.hpp
* /usr/include/asio/post.hpp
* /usr/include/asio/prefer.hpp
* /usr/include/asio/prepend.hpp
* /usr/include/asio/query.hpp
* /usr/include/asio/random_access_file.hpp
* /usr/include/asio/read.hpp
* /usr/include/asio/readable_pipe.hpp
* /usr/include/asio/read_at.hpp
* /usr/include/asio/read_until.hpp
* /usr/include/asio/recycling_allocator.hpp
* /usr/include/asio/redirect_error.hpp
* /usr/include/asio/registered_buffer.hpp
* /usr/include/asio/require.hpp
* /usr/include/asio/require_concept.hpp
* /usr/include/asio/serial_port.hpp
* /usr/include/asio/serial_port_base.hpp
* /usr/include/asio/signal_set.hpp
* /usr/include/asio/signal_set_base.hpp
* /usr/include/asio/socket_base.hpp
* /usr/include/asio/spawn.hpp
* /usr/include/asio/ssl.hpp
* /usr/include/asio/ssl/context.hpp
* /usr/include/asio/ssl/context_base.hpp
* /usr/include/asio/ssl/detail/buffered_handshake_op.hpp
* /usr/include/asio/ssl/detail/engine.hpp
* /usr/include/asio/ssl/detail/handshake_op.hpp
* /usr/include/asio/ssl/detail/impl/engine.ipp
* /usr/include/asio/ssl/detail/impl/openssl_init.ipp
* /usr/include/asio/ssl/detail/io.hpp
* /usr/include/asio/ssl/detail/openssl_init.hpp
* /usr/include/asio/ssl/detail/openssl_types.hpp
* /usr/include/asio/ssl/detail/password_callback.hpp
* /usr/include/asio/ssl/detail/read_op.hpp
* /usr/include/asio/ssl/detail/shutdown_op.hpp
* /usr/include/asio/ssl/detail/stream_core.hpp
* /usr/include/asio/ssl/detail/verify_callback.hpp
* /usr/include/asio/ssl/detail/write_op.hpp
* /usr/include/asio/ssl/error.hpp
* /usr/include/asio/ssl/host_name_verification.hpp
* /usr/include/asio/ssl/impl/context.hpp
* /usr/include/asio/ssl/impl/context.ipp
* /usr/include/asio/ssl/impl/error.ipp
* /usr/include/asio/ssl/impl/host_name_verification.ipp
* /usr/include/asio/ssl/impl/src.hpp
* /usr/include/asio/ssl/stream.hpp
* /usr/include/asio/ssl/stream_base.hpp
* /usr/include/asio/ssl/verify_context.hpp
* /usr/include/asio/ssl/verify_mode.hpp
* /usr/include/asio/static_thread_pool.hpp
* /usr/include/asio/steady_timer.hpp
* /usr/include/asio/strand.hpp
* /usr/include/asio/streambuf.hpp
* /usr/include/asio/stream_file.hpp
* /usr/include/asio/system_context.hpp
* /usr/include/asio/system_error.hpp
* /usr/include/asio/system_executor.hpp
* /usr/include/asio/system_timer.hpp
* /usr/include/asio/this_coro.hpp
* /usr/include/asio/thread.hpp
* /usr/include/asio/thread_pool.hpp
* /usr/include/asio/time_traits.hpp
* /usr/include/asio/traits/equality_comparable.hpp
* /usr/include/asio/traits/execute_member.hpp
* /usr/include/asio/traits/prefer_free.hpp
* /usr/include/asio/traits/prefer_member.hpp
* /usr/include/asio/traits/query_free.hpp
* /usr/include/asio/traits/query_member.hpp
* /usr/include/asio/traits/query_static_constexpr_member.hpp
* /usr/include/asio/traits/require_concept_free.hpp
* /usr/include/asio/traits/require_concept_member.hpp
* /usr/include/asio/traits/require_free.hpp
* /usr/include/asio/traits/require_member.hpp
* /usr/include/asio/traits/static_query.hpp
* /usr/include/asio/traits/static_require.hpp
* /usr/include/asio/traits/static_require_concept.hpp
* /usr/include/asio/ts/buffer.hpp
* /usr/include/asio/ts/executor.hpp
* /usr/include/asio/ts/internet.hpp
* /usr/include/asio/ts/io_context.hpp
* /usr/include/asio/ts/net.hpp
* /usr/include/asio/ts/netfwd.hpp
* /usr/include/asio/ts/socket.hpp
* /usr/include/asio/ts/timer.hpp
* /usr/include/asio/unyield.hpp
* /usr/include/asio/uses_executor.hpp
* /usr/include/asio/use_awaitable.hpp
* /usr/include/asio/use_future.hpp
* /usr/include/asio/version.hpp
* /usr/include/asio/wait_traits.hpp
* /usr/include/asio/windows/basic_object_handle.hpp
* /usr/include/asio/windows/basic_overlapped_handle.hpp
* /usr/include/asio/windows/basic_random_access_handle.hpp
* /usr/include/asio/windows/basic_stream_handle.hpp
* /usr/include/asio/windows/object_handle.hpp
* /usr/include/asio/windows/overlapped_handle.hpp
* /usr/include/asio/windows/overlapped_ptr.hpp
* /usr/include/asio/windows/random_access_handle.hpp
* /usr/include/asio/windows/stream_handle.hpp
* /usr/include/asio/writable_pipe.hpp
* /usr/include/asio/write.hpp
* /usr/include/asio/write_at.hpp
* /usr/include/asio/yield.hpp
* /usr/share/doc/asio-1.34.2/COPYING
* /usr/share/doc/asio-1.34.2/INSTALL
* /usr/share/doc/asio-1.34.2/README
* /usr/share/pkgconfig/asio.pc
