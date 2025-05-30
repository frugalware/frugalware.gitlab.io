+++
draft = false
title = "gpgme 1.24.3-1"
version = "1.24.3-1"
description = "A high-level crypto API for encryption"
date = "2025-05-27T08:15:55"
aliases = "/packages/3620"
categories = ['apps']
upstreamurl = "http://www.gnupg.org/related_software/gpgme/"
arch = "x86_64"
size = "2322136"
usize = "4134587"
sha1sum = "6af5d679d879ac8cd402513c5df4ae1d97854911"
depends = "['glibc>=2.34', 'libassuan>=3.0.1', 'libgpg-error>=1.27-3']"
reverse_depends = "['claws-mail-plugin-pgpcore', 'claws-mail-plugin-pgpinline', 'claws-mail-plugin-pgpmime', 'claws-mail-plugin-smime', 'fwupd', 'gmime2', 'gmime3', 'kgpg', 'libgpgmepp', 'libjcat', 'libqgpgme', 'libsmbclient', 'mcabber', 'mutt-devel', 'openvas-libraries', 'openvas-manager', 'ostree', 'python3-gpgme', 'sylpheed', 'volume_key', 'wget2']"
+++
### Description: 
A high-level crypto API for encryption

### Files: 
* /usr/bin/gpgme-json
* /usr/bin/gpgme-tool
* /usr/include/gpgme++/configuration.h
* /usr/include/gpgme++/context.h
* /usr/include/gpgme++/data.h
* /usr/include/gpgme++/decryptionresult.h
* /usr/include/gpgme++/defaultassuantransaction.h
* /usr/include/gpgme++/editinteractor.h
* /usr/include/gpgme++/encryptionresult.h
* /usr/include/gpgme++/engineinfo.h
* /usr/include/gpgme++/error.h
* /usr/include/gpgme++/eventloopinteractor.h
* /usr/include/gpgme++/exception.h
* /usr/include/gpgme++/global.h
* /usr/include/gpgme++/gpgaddexistingsubkeyeditinteractor.h
* /usr/include/gpgme++/gpgadduserideditinteractor.h
* /usr/include/gpgme++/gpgagentgetinfoassuantransaction.h
* /usr/include/gpgme++/gpggencardkeyinteractor.h
* /usr/include/gpgme++/gpgmefw.h
* /usr/include/gpgme++/gpgmepp_export.h
* /usr/include/gpgme++/gpgmepp_version.h
* /usr/include/gpgme++/gpgrevokekeyeditinteractor.h
* /usr/include/gpgme++/gpgsetexpirytimeeditinteractor.h
* /usr/include/gpgme++/gpgsetownertrusteditinteractor.h
* /usr/include/gpgme++/gpgsignkeyeditinteractor.h
* /usr/include/gpgme++/importresult.h
* /usr/include/gpgme++/interfaces/assuantransaction.h
* /usr/include/gpgme++/interfaces/dataprovider.h
* /usr/include/gpgme++/interfaces/passphraseprovider.h
* /usr/include/gpgme++/interfaces/progressprovider.h
* /usr/include/gpgme++/interfaces/statusconsumer.h
* /usr/include/gpgme++/key.h
* /usr/include/gpgme++/keygenerationresult.h
* /usr/include/gpgme++/keylistresult.h
* /usr/include/gpgme++/notation.h
* /usr/include/gpgme++/result.h
* /usr/include/gpgme++/scdgetinfoassuantransaction.h
* /usr/include/gpgme++/signingresult.h
* /usr/include/gpgme++/statusconsumerassuantransaction.h
* /usr/include/gpgme++/swdbresult.h
* /usr/include/gpgme++/tofuinfo.h
* /usr/include/gpgme++/trustitem.h
* /usr/include/gpgme++/verificationresult.h
* /usr/include/gpgme++/vfsmountresult.h
* /usr/include/gpgme.h
* /usr/include/qgpgme-qt6/QGpgME/AbstractImportJob
* /usr/include/qgpgme-qt6/qgpgme/abstractimportjob.h
* /usr/include/qgpgme-qt6/QGpgME/AddExistingSubkeyJob
* /usr/include/qgpgme-qt6/qgpgme/addexistingsubkeyjob.h
* /usr/include/qgpgme-qt6/QGpgME/AddUserIDJob
* /usr/include/qgpgme-qt6/qgpgme/adduseridjob.h
* /usr/include/qgpgme-qt6/QGpgME/ChangeExpiryJob
* /usr/include/qgpgme-qt6/qgpgme/changeexpiryjob.h
* /usr/include/qgpgme-qt6/QGpgME/ChangeOwnerTrustJob
* /usr/include/qgpgme-qt6/qgpgme/changeownertrustjob.h
* /usr/include/qgpgme-qt6/QGpgME/ChangePasswdJob
* /usr/include/qgpgme-qt6/qgpgme/changepasswdjob.h
* /usr/include/qgpgme-qt6/QGpgME/CryptoConfig
* /usr/include/qgpgme-qt6/qgpgme/cryptoconfig.h
* /usr/include/qgpgme-qt6/QGpgME/DataProvider
* /usr/include/qgpgme-qt6/qgpgme/dataprovider.h
* /usr/include/qgpgme-qt6/QGpgME/Debug
* /usr/include/qgpgme-qt6/qgpgme/debug.h
* /usr/include/qgpgme-qt6/QGpgME/DecryptJob
* /usr/include/qgpgme-qt6/qgpgme/decryptjob.h
* /usr/include/qgpgme-qt6/QGpgME/DecryptVerifyArchiveJob
* /usr/include/qgpgme-qt6/qgpgme/decryptverifyarchivejob.h
* /usr/include/qgpgme-qt6/QGpgME/DecryptVerifyJob
* /usr/include/qgpgme-qt6/qgpgme/decryptverifyjob.h
* /usr/include/qgpgme-qt6/QGpgME/DefaultKeyGenerationJob
* /usr/include/qgpgme-qt6/qgpgme/defaultkeygenerationjob.h
* /usr/include/qgpgme-qt6/QGpgME/DeleteJob
* /usr/include/qgpgme-qt6/qgpgme/deletejob.h
* /usr/include/qgpgme-qt6/QGpgME/DN
* /usr/include/qgpgme-qt6/qgpgme/dn.h
* /usr/include/qgpgme-qt6/QGpgME/DownloadJob
* /usr/include/qgpgme-qt6/qgpgme/downloadjob.h
* /usr/include/qgpgme-qt6/QGpgME/EncryptArchiveJob
* /usr/include/qgpgme-qt6/qgpgme/encryptarchivejob.h
* /usr/include/qgpgme-qt6/QGpgME/EncryptJob
* /usr/include/qgpgme-qt6/qgpgme/encryptjob.h
* /usr/include/qgpgme-qt6/QGpgME/ExportJob
* /usr/include/qgpgme-qt6/qgpgme/exportjob.h
* /usr/include/qgpgme-qt6/QGpgME/FileListDataProvider
* /usr/include/qgpgme-qt6/qgpgme/filelistdataprovider.h
* /usr/include/qgpgme-qt6/QGpgME/GpgCardJob
* /usr/include/qgpgme-qt6/qgpgme/gpgcardjob.h
* /usr/include/qgpgme-qt6/QGpgME/HierarchicalKeyListJob
* /usr/include/qgpgme-qt6/qgpgme/hierarchicalkeylistjob.h
* /usr/include/qgpgme-qt6/QGpgME/ImportFromKeyserverJob
* /usr/include/qgpgme-qt6/qgpgme/importfromkeyserverjob.h
* /usr/include/qgpgme-qt6/QGpgME/ImportJob
* /usr/include/qgpgme-qt6/qgpgme/importjob.h
* /usr/include/qgpgme-qt6/QGpgME/Job
* /usr/include/qgpgme-qt6/qgpgme/job.h
* /usr/include/qgpgme-qt6/QGpgME/KeyForMailboxJob
* /usr/include/qgpgme-qt6/qgpgme/keyformailboxjob.h
* /usr/include/qgpgme-qt6/QGpgME/KeyGenerationJob
* /usr/include/qgpgme-qt6/qgpgme/keygenerationjob.h
* /usr/include/qgpgme-qt6/QGpgME/KeyListJob
* /usr/include/qgpgme-qt6/qgpgme/keylistjob.h
* /usr/include/qgpgme-qt6/QGpgME/ListAllKeysJob
* /usr/include/qgpgme-qt6/qgpgme/listallkeysjob.h
* /usr/include/qgpgme-qt6/QGpgME/MultiDeleteJob
* /usr/include/qgpgme-qt6/qgpgme/multideletejob.h
* /usr/include/qgpgme-qt6/QGpgME/Protocol
* /usr/include/qgpgme-qt6/qgpgme/protocol.h
* /usr/include/qgpgme-qt6/QGpgME/QGpgMENewCryptoConfig
* /usr/include/qgpgme-qt6/qgpgme/qgpgmenewcryptoconfig.h
* /usr/include/qgpgme-qt6/qgpgme/qgpgme_export.h
* /usr/include/qgpgme-qt6/qgpgme/qgpgme_version.h
* /usr/include/qgpgme-qt6/QGpgME/QuickJob
* /usr/include/qgpgme-qt6/qgpgme/quickjob.h
* /usr/include/qgpgme-qt6/QGpgME/ReceiveKeysJob
* /usr/include/qgpgme-qt6/qgpgme/receivekeysjob.h
* /usr/include/qgpgme-qt6/QGpgME/RefreshKeysJob
* /usr/include/qgpgme-qt6/qgpgme/refreshkeysjob.h
* /usr/include/qgpgme-qt6/QGpgME/RevokeKeyJob
* /usr/include/qgpgme-qt6/qgpgme/revokekeyjob.h
* /usr/include/qgpgme-qt6/QGpgME/SetPrimaryUserIDJob
* /usr/include/qgpgme-qt6/qgpgme/setprimaryuseridjob.h
* /usr/include/qgpgme-qt6/QGpgME/SignArchiveJob
* /usr/include/qgpgme-qt6/qgpgme/signarchivejob.h
* /usr/include/qgpgme-qt6/QGpgME/SignEncryptArchiveJob
* /usr/include/qgpgme-qt6/qgpgme/signencryptarchivejob.h
* /usr/include/qgpgme-qt6/QGpgME/SignEncryptJob
* /usr/include/qgpgme-qt6/qgpgme/signencryptjob.h
* /usr/include/qgpgme-qt6/QGpgME/SignJob
* /usr/include/qgpgme-qt6/qgpgme/signjob.h
* /usr/include/qgpgme-qt6/QGpgME/SignKeyJob
* /usr/include/qgpgme-qt6/qgpgme/signkeyjob.h
* /usr/include/qgpgme-qt6/QGpgME/SpecialJob
* /usr/include/qgpgme-qt6/qgpgme/specialjob.h
* /usr/include/qgpgme-qt6/QGpgME/TofuPolicyJob
* /usr/include/qgpgme-qt6/qgpgme/tofupolicyjob.h
* /usr/include/qgpgme-qt6/QGpgME/VerifyDetachedJob
* /usr/include/qgpgme-qt6/qgpgme/verifydetachedjob.h
* /usr/include/qgpgme-qt6/QGpgME/VerifyOpaqueJob
* /usr/include/qgpgme-qt6/qgpgme/verifyopaquejob.h
* /usr/include/qgpgme-qt6/QGpgME/WKDLookupJob
* /usr/include/qgpgme-qt6/qgpgme/wkdlookupjob.h
* /usr/include/qgpgme-qt6/QGpgME/WKDLookupResult
* /usr/include/qgpgme-qt6/qgpgme/wkdlookupresult.h
* /usr/include/qgpgme-qt6/QGpgME/WKDRefreshJob
* /usr/include/qgpgme-qt6/qgpgme/wkdrefreshjob.h
* /usr/include/qgpgme-qt6/QGpgME/WKSPublishJob
* /usr/include/qgpgme-qt6/qgpgme/wkspublishjob.h
* /usr/lib/cmake/Gpgmepp/GpgmeppConfig.cmake
* /usr/lib/cmake/Gpgmepp/GpgmeppConfigVersion.cmake
* /usr/lib/cmake/QGpgmeQt6/QGpgmeQt6Config.cmake
* /usr/lib/cmake/QGpgmeQt6/QGpgmeQt6ConfigVersion.cmake
* /usr/lib/libgpgme.a
* /usr/lib/libgpgme.so
* /usr/lib/libgpgme.so.11
* /usr/lib/libgpgme.so.11.33.2
* /usr/lib/pkgconfig/gpgme-glib.pc
* /usr/lib/pkgconfig/gpgme.pc
* /usr/lib/pkgconfig/gpgmepp.pc
* /usr/share/aclocal/gpgme.m4
* /usr/share/common-lisp/source/gpgme/gpgme-grovel.lisp
* /usr/share/common-lisp/source/gpgme/gpgme-package.lisp
* /usr/share/common-lisp/source/gpgme/gpgme.asd
* /usr/share/common-lisp/source/gpgme/gpgme.lisp
* /usr/share/doc/gpgme-1.24.3/AUTHORS
* /usr/share/doc/gpgme-1.24.3/ChangeLog
* /usr/share/doc/gpgme-1.24.3/COPYING
* /usr/share/doc/gpgme-1.24.3/COPYING.LESSER
* /usr/share/doc/gpgme-1.24.3/INSTALL
* /usr/share/doc/gpgme-1.24.3/NEWS
* /usr/share/doc/gpgme-1.24.3/README
* /usr/share/doc/gpgme-1.24.3/THANKS
* /usr/share/doc/gpgme-1.24.3/TODO
* /usr/share/doc/gpgme-1.24.3/VERSION
* /usr/share/info/gpgme.info-1.gz
* /usr/share/info/gpgme.info-2.gz
* /usr/share/info/gpgme.info.gz
* /usr/share/man/man1/gpgme-json.1.gz
