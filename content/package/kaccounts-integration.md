+++
draft = false
title = "kaccounts-integration 23.08.5-1"
version = "23.08.5-1"
description = "Small system to administer web accounts like: Google, Facebook, Owncloud, IMAP, Jabber and others"
date = "2024-02-19T23:12:13"
aliases = "/packages/218267"
categories = ['kde5']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "119924"
usize = "582439"
sha1sum = "42e19ce722c382cf5afbeaffc485f89c02d67b7e"
depends = "['kcmutils>=5.115.0', 'kconfigwidgets>=5.115.0', 'kdbusaddons>=5.115.0', 'kdeclarative>=5.115.0', 'libaccounts-qt>=1.14-3', 'qcoro', 'qt5-declarative>=5.15.12', 'qt5-x11extras>=5.15.12', 'signon-kwallet-extension>=23.08.5']"
reverse_depends = "['akonadi', 'kaccounts-provider-opendesktop', 'kaccounts-providers', 'plasma-welcome']"
+++
Small system to administer web accounts like: Google, Facebook, Owncloud, IMAP, Jabber and others{{< files text="show files" >}}* /usr/include/KAccounts/AccountServiceToggleJob
* /usr/include/KAccounts/accountservicetogglejob.h
* /usr/include/KAccounts/AccountsModel
* /usr/include/KAccounts/accountsmodel.h
* /usr/include/KAccounts/ChangeAccountDisplayNameJob
* /usr/include/KAccounts/changeaccountdisplaynamejob.h
* /usr/include/KAccounts/Core
* /usr/include/KAccounts/core.h
* /usr/include/KAccounts/CreateAccountJob
* /usr/include/KAccounts/createaccountjob.h
* /usr/include/KAccounts/GetCredentialsJob
* /usr/include/KAccounts/getcredentialsjob.h
* /usr/include/KAccounts/KAccountsDPlugin
* /usr/include/KAccounts/kaccountsdplugin.h
* /usr/include/KAccounts/KAccountsUiPlugin
* /usr/include/KAccounts/kaccountsuiplugin.h
* /usr/include/KAccounts/kaccounts_export.h
* /usr/include/KAccounts/kaccounts_version.h
* /usr/include/KAccounts/ProvidersModel
* /usr/include/KAccounts/providersmodel.h
* /usr/include/KAccounts/RemoveAccountJob
* /usr/include/KAccounts/removeaccountjob.h
* /usr/include/KAccounts/ServicesModel
* /usr/include/KAccounts/servicesmodel.h
* /usr/lib/cmake/KAccounts/KAccountsConfig.cmake
* /usr/lib/cmake/KAccounts/KAccountsConfigVersion.cmake
* /usr/lib/cmake/KAccounts/KAccountsMacros.cmake
* /usr/lib/cmake/KAccounts/KAccountsTargets-release.cmake
* /usr/lib/cmake/KAccounts/KAccountsTargets.cmake
* /usr/lib/libkaccounts.so
* /usr/lib/libkaccounts.so.2
* /usr/lib/libkaccounts.so.23.08.5
* /usr/lib/qt5/plugins/kaccounts/daemonplugins/kaccounts_kio_webdav_plugin.so
* /usr/lib/qt5/plugins/kf5/kded/kded_accounts.so
* /usr/lib/qt5/plugins/plasma/kcms/systemsettings/kcm_kaccounts.so
* /usr/share/applications/kcm_kaccounts.desktop
* /usr/share/doc/kaccounts-integration-23.08.5/README
* /usr/share/doc/kaccounts-integration-23.08.5/README.md
* /usr/share/kpackage/kcms/kcm_kaccounts/contents/ui/AccountDetails.qml
* /usr/share/kpackage/kcms/kcm_kaccounts/contents/ui/AvailableAccounts.qml
* /usr/share/kpackage/kcms/kcm_kaccounts/contents/ui/main.qml
* /usr/share/kpackage/kcms/kcm_kaccounts/contents/ui/MessageBoxSheet.qml
* /usr/share/kpackage/kcms/kcm_kaccounts/contents/ui/RemoveAccountDialog.qml
* /usr/share/kpackage/kcms/kcm_kaccounts/contents/ui/RenameAccountDialog.qml
* /usr/share/locale/ar/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/az/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/bg/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/bs/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/ca/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/cs/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/da/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/de/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/el/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/en_GB/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/es/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/et/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/eu/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/fi/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/fr/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/gl/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/hu/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/ia/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/id/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/it/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/ja/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/ka/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/ko/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/lt/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/nl/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/nn/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/pa/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/pl/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/pt/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/ro/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/ru/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/sk/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/sl/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/sr/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/sr@ijekavian/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/sv/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/tr/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/uk/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/kaccounts-integration.mo
* /usr/share/qt5/qml/org/kde/kaccounts/libkaccountsdeclarativeplugin.so
* /usr/share/qt5/qml/org/kde/kaccounts/qmldir
{{< /files >}}