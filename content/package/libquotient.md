+++
draft = false
title = "libquotient 0.8.1.2-2"
version = "0.8.1.2-2"
description = "A Qt library to write cross-platform clients for Matrix"
date = "2023-10-27T16:03:33"
aliases = "/packages/220989"
categories = ['lib-extra']
upstreamurl = "https://matrix.org/docs/projects/sdk/quotient"
arch = "x86_64"
size = "545944"
usize = "2301767"
sha1sum = "af15012869e2e109522d3cce5a4cfd12c8817bb2"
depends = "['qt5-multimedia>=5.15.10', 'qtkeychain']"
reverse_depends = "['neochat']"
+++
A Qt library to write cross-platform clients for Matrix{{< files text="show files" >}}* /usr/bin/quotest
* /usr/include/Quotient/accountregistry.h
* /usr/include/Quotient/application-service/definitions/location.h
* /usr/include/Quotient/application-service/definitions/protocol.h
* /usr/include/Quotient/application-service/definitions/user.h
* /usr/include/Quotient/avatar.h
* /usr/include/Quotient/connection.h
* /usr/include/Quotient/connectiondata.h
* /usr/include/Quotient/connectionencryptiondata_p.h
* /usr/include/Quotient/connection_p.h
* /usr/include/Quotient/converters.h
* /usr/include/Quotient/csapi/account-data.h
* /usr/include/Quotient/csapi/admin.h
* /usr/include/Quotient/csapi/administrative_contact.h
* /usr/include/Quotient/csapi/appservice_room_directory.h
* /usr/include/Quotient/csapi/banning.h
* /usr/include/Quotient/csapi/capabilities.h
* /usr/include/Quotient/csapi/content-repo.h
* /usr/include/Quotient/csapi/create_room.h
* /usr/include/Quotient/csapi/cross_signing.h
* /usr/include/Quotient/csapi/definitions/auth_data.h
* /usr/include/Quotient/csapi/definitions/client_device.h
* /usr/include/Quotient/csapi/definitions/cross_signing_key.h
* /usr/include/Quotient/csapi/definitions/device_keys.h
* /usr/include/Quotient/csapi/definitions/event_filter.h
* /usr/include/Quotient/csapi/definitions/key_backup_data.h
* /usr/include/Quotient/csapi/definitions/openid_token.h
* /usr/include/Quotient/csapi/definitions/public_rooms_response.h
* /usr/include/Quotient/csapi/definitions/push_condition.h
* /usr/include/Quotient/csapi/definitions/push_rule.h
* /usr/include/Quotient/csapi/definitions/push_ruleset.h
* /usr/include/Quotient/csapi/definitions/request_email_validation.h
* /usr/include/Quotient/csapi/definitions/request_msisdn_validation.h
* /usr/include/Quotient/csapi/definitions/request_token_response.h
* /usr/include/Quotient/csapi/definitions/room_event_filter.h
* /usr/include/Quotient/csapi/definitions/room_key_backup.h
* /usr/include/Quotient/csapi/definitions/sync_filter.h
* /usr/include/Quotient/csapi/definitions/third_party_signed.h
* /usr/include/Quotient/csapi/definitions/user_identifier.h
* /usr/include/Quotient/csapi/definitions/wellknown/full.h
* /usr/include/Quotient/csapi/definitions/wellknown/homeserver.h
* /usr/include/Quotient/csapi/definitions/wellknown/identity_server.h
* /usr/include/Quotient/csapi/device_management.h
* /usr/include/Quotient/csapi/directory.h
* /usr/include/Quotient/csapi/event_context.h
* /usr/include/Quotient/csapi/filter.h
* /usr/include/Quotient/csapi/inviting.h
* /usr/include/Quotient/csapi/joining.h
* /usr/include/Quotient/csapi/keys.h
* /usr/include/Quotient/csapi/key_backup.h
* /usr/include/Quotient/csapi/kicking.h
* /usr/include/Quotient/csapi/knocking.h
* /usr/include/Quotient/csapi/leaving.h
* /usr/include/Quotient/csapi/list_joined_rooms.h
* /usr/include/Quotient/csapi/list_public_rooms.h
* /usr/include/Quotient/csapi/login.h
* /usr/include/Quotient/csapi/login_token.h
* /usr/include/Quotient/csapi/logout.h
* /usr/include/Quotient/csapi/message_pagination.h
* /usr/include/Quotient/csapi/notifications.h
* /usr/include/Quotient/csapi/openid.h
* /usr/include/Quotient/csapi/peeking_events.h
* /usr/include/Quotient/csapi/presence.h
* /usr/include/Quotient/csapi/profile.h
* /usr/include/Quotient/csapi/pusher.h
* /usr/include/Quotient/csapi/pushrules.h
* /usr/include/Quotient/csapi/read_markers.h
* /usr/include/Quotient/csapi/receipts.h
* /usr/include/Quotient/csapi/redaction.h
* /usr/include/Quotient/csapi/refresh.h
* /usr/include/Quotient/csapi/registration.h
* /usr/include/Quotient/csapi/registration_tokens.h
* /usr/include/Quotient/csapi/relations.h
* /usr/include/Quotient/csapi/report_content.h
* /usr/include/Quotient/csapi/rooms.h
* /usr/include/Quotient/csapi/room_event_by_timestamp.h
* /usr/include/Quotient/csapi/room_send.h
* /usr/include/Quotient/csapi/room_state.h
* /usr/include/Quotient/csapi/room_upgrades.h
* /usr/include/Quotient/csapi/search.h
* /usr/include/Quotient/csapi/space_hierarchy.h
* /usr/include/Quotient/csapi/sso_login_redirect.h
* /usr/include/Quotient/csapi/tags.h
* /usr/include/Quotient/csapi/third_party_lookup.h
* /usr/include/Quotient/csapi/third_party_membership.h
* /usr/include/Quotient/csapi/threads_list.h
* /usr/include/Quotient/csapi/to_device.h
* /usr/include/Quotient/csapi/typing.h
* /usr/include/Quotient/csapi/users.h
* /usr/include/Quotient/csapi/versions.h
* /usr/include/Quotient/csapi/voip.h
* /usr/include/Quotient/csapi/wellknown.h
* /usr/include/Quotient/csapi/whoami.h
* /usr/include/Quotient/database.h
* /usr/include/Quotient/e2ee/e2ee_common.h
* /usr/include/Quotient/e2ee/qolmaccount.h
* /usr/include/Quotient/e2ee/qolminboundsession.h
* /usr/include/Quotient/e2ee/qolmmessage.h
* /usr/include/Quotient/e2ee/qolmoutboundsession.h
* /usr/include/Quotient/e2ee/qolmsession.h
* /usr/include/Quotient/e2ee/qolmutility.h
* /usr/include/Quotient/eventitem.h
* /usr/include/Quotient/events/accountdataevents.h
* /usr/include/Quotient/events/callevents.h
* /usr/include/Quotient/events/directchatevent.h
* /usr/include/Quotient/events/encryptedevent.h
* /usr/include/Quotient/events/encryptionevent.h
* /usr/include/Quotient/events/event.h
* /usr/include/Quotient/events/eventcontent.h
* /usr/include/Quotient/events/eventloader.h
* /usr/include/Quotient/events/eventrelation.h
* /usr/include/Quotient/events/filesourceinfo.h
* /usr/include/Quotient/events/keyverificationevent.h
* /usr/include/Quotient/events/reactionevent.h
* /usr/include/Quotient/events/receiptevent.h
* /usr/include/Quotient/events/redactionevent.h
* /usr/include/Quotient/events/roomavatarevent.h
* /usr/include/Quotient/events/roomcanonicalaliasevent.h
* /usr/include/Quotient/events/roomcreateevent.h
* /usr/include/Quotient/events/roomevent.h
* /usr/include/Quotient/events/roomkeyevent.h
* /usr/include/Quotient/events/roommemberevent.h
* /usr/include/Quotient/events/roommessageevent.h
* /usr/include/Quotient/events/roompowerlevelsevent.h
* /usr/include/Quotient/events/roomtombstoneevent.h
* /usr/include/Quotient/events/simplestateevents.h
* /usr/include/Quotient/events/single_key_value.h
* /usr/include/Quotient/events/stateevent.h
* /usr/include/Quotient/events/stickerevent.h
* /usr/include/Quotient/events/typingevent.h
* /usr/include/Quotient/eventstats.h
* /usr/include/Quotient/expected.h
* /usr/include/Quotient/function_traits.h
* /usr/include/Quotient/identity/definitions/request_email_validation.h
* /usr/include/Quotient/identity/definitions/request_msisdn_validation.h
* /usr/include/Quotient/jobs/basejob.h
* /usr/include/Quotient/jobs/downloadfilejob.h
* /usr/include/Quotient/jobs/mediathumbnailjob.h
* /usr/include/Quotient/jobs/requestdata.h
* /usr/include/Quotient/jobs/syncjob.h
* /usr/include/Quotient/keyverificationsession.h
* /usr/include/Quotient/logging_categories_p.h
* /usr/include/Quotient/mxcreply.h
* /usr/include/Quotient/networkaccessmanager.h
* /usr/include/Quotient/networksettings.h
* /usr/include/Quotient/omittable.h
* /usr/include/Quotient/qt_connection_util.h
* /usr/include/Quotient/quotient_common.h
* /usr/include/Quotient/quotient_export.h
* /usr/include/Quotient/room.h
* /usr/include/Quotient/roomstateview.h
* /usr/include/Quotient/settings.h
* /usr/include/Quotient/ssosession.h
* /usr/include/Quotient/syncdata.h
* /usr/include/Quotient/uri.h
* /usr/include/Quotient/uriresolver.h
* /usr/include/Quotient/user.h
* /usr/include/Quotient/util.h
* /usr/lib/cmake/Quotient/QuotientConfig.cmake
* /usr/lib/cmake/Quotient/QuotientConfigVersion.cmake
* /usr/lib/cmake/Quotient/QuotientTargets-release.cmake
* /usr/lib/cmake/Quotient/QuotientTargets.cmake
* /usr/lib/libQuotient.so
* /usr/lib/libQuotient.so.0.8
* /usr/lib/libQuotient.so.0.8.1.2
* /usr/lib/pkgconfig/Quotient.pc
* /usr/share/doc/libquotient-0.8.1.2/COPYING
* /usr/share/doc/libquotient-0.8.1.2/README.md
* /usr/share/ndk-modules/Android.mk
{{< /files >}}