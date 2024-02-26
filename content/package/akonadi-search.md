+++
draft = false
title = "akonadi-search 23.08.5-1"
version = "23.08.5-1"
description = "Libraries and daemons to implement searching in Akonad"
date = "2024-02-19T23:40:47"
aliases = "/packages/218250"
categories = ['kde5']
upstreamurl = "http://www.kde.org"
arch = "x86_64"
size = "260740"
usize = "1117161"
sha1sum = "0576c3108809c117aec852d0f4f5b4fc5edf1d58"
depends = "['akonadi-contacts>=23.08.5', 'kcmutils>=5.115.0', 'krunner5>=5.115.0', 'qt5-declarative>=5.15.12', 'qt5-svg>=5.15.12', 'xapian-core>=1.4.0-2']"
reverse_depends = "['libkdepim']"
+++
Libraries and daemons to implement searching in Akonad

{{< files text="show files" >}}* /usr/bin/akonadi_html_to_text
* /usr/bin/akonadi_indexing_agent
* /usr/include/KPim5/AkonadiSearch/akonadi_search_version.h
* /usr/include/KPim5/AkonadiSearch/Core/Query
* /usr/include/KPim5/AkonadiSearch/core/query.h
* /usr/include/KPim5/AkonadiSearch/Core/ResultIterator
* /usr/include/KPim5/AkonadiSearch/core/resultiterator.h
* /usr/include/KPim5/AkonadiSearch/Core/SearchStore
* /usr/include/KPim5/AkonadiSearch/core/searchstore.h
* /usr/include/KPim5/AkonadiSearch/Core/Term
* /usr/include/KPim5/AkonadiSearch/core/term.h
* /usr/include/KPim5/AkonadiSearch/Debug/akonadisearchdebugdialog.h
* /usr/include/KPim5/AkonadiSearch/Debug/akonadisearchdebugsearchpathcombobox.h
* /usr/include/KPim5/AkonadiSearch/Debug/search_debug_export.h
* /usr/include/KPim5/AkonadiSearch/PIM/collectionquery.h
* /usr/include/KPim5/AkonadiSearch/PIM/contactcompleter.h
* /usr/include/KPim5/AkonadiSearch/PIM/contactquery.h
* /usr/include/KPim5/AkonadiSearch/PIM/emailquery.h
* /usr/include/KPim5/AkonadiSearch/PIM/indexeditems.h
* /usr/include/KPim5/AkonadiSearch/PIM/notequery.h
* /usr/include/KPim5/AkonadiSearch/PIM/query.h
* /usr/include/KPim5/AkonadiSearch/PIM/resultiterator.h
* /usr/include/KPim5/AkonadiSearch/PIM/search_pim_export.h
* /usr/include/KPim5/AkonadiSearch/search_core_export.h
* /usr/include/KPim5/AkonadiSearch/Xapian/search_xapian_export.h
* /usr/include/KPim5/AkonadiSearch/Xapian/xapiandatabase.h
* /usr/include/KPim5/AkonadiSearch/Xapian/xapiandocument.h
* /usr/include/KPim5/AkonadiSearch/Xapian/xapianqueryparser.h
* /usr/include/KPim5/AkonadiSearch/Xapian/xapiansearchstore.h
* /usr/include/KPim5/AkonadiSearch/Xapian/xapiantermgenerator.h
* /usr/lib/cmake/KPim5AkonadiSearch/KPim5AkonadiSearchConfig.cmake
* /usr/lib/cmake/KPim5AkonadiSearch/KPim5AkonadiSearchConfigVersion.cmake
* /usr/lib/cmake/KPim5AkonadiSearch/KPim5AkonadiSearchTargets-release.cmake
* /usr/lib/cmake/KPim5AkonadiSearch/KPim5AkonadiSearchTargets.cmake
* /usr/lib/libKPim5AkonadiSearchCore.so
* /usr/lib/libKPim5AkonadiSearchCore.so.5
* /usr/lib/libKPim5AkonadiSearchCore.so.5.24.5
* /usr/lib/libKPim5AkonadiSearchDebug.so
* /usr/lib/libKPim5AkonadiSearchDebug.so.5
* /usr/lib/libKPim5AkonadiSearchDebug.so.5.24.5
* /usr/lib/libKPim5AkonadiSearchPIM.so
* /usr/lib/libKPim5AkonadiSearchPIM.so.5
* /usr/lib/libKPim5AkonadiSearchPIM.so.5.24.5
* /usr/lib/libKPim5AkonadiSearchXapian.so
* /usr/lib/libKPim5AkonadiSearchXapian.so.5
* /usr/lib/libKPim5AkonadiSearchXapian.so.5.24.5
* /usr/lib/qt5/plugins/kf5/krunner/kcms/kcm_krunner_pimcontacts.so
* /usr/lib/qt5/plugins/kf5/krunner/krunner_pimcontacts.so
* /usr/lib/qt5/plugins/pim5/akonadi/akonadi_search_plugin.so
* /usr/lib/qt5/plugins/pim5/akonadi/calendarsearchstore.so
* /usr/lib/qt5/plugins/pim5/akonadi/contactsearchstore.so
* /usr/lib/qt5/plugins/pim5/akonadi/emailsearchstore.so
* /usr/lib/qt5/plugins/pim5/akonadi/notesearchstore.so
* /usr/share/akonadi/agents/akonadiindexingagent.desktop
* /usr/share/doc/akonadi-search-23.08.5/README.md
* /usr/share/doc/akonadi-search-23.08.5/README.md.license
* /usr/share/locale/ar/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/az/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/bg/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/ca/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/ca@valencia/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/cs/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/da/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/de/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/el/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/en_GB/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/es/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/et/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/eu/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/fi/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/fr/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/gl/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/hi/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/hsb/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/hu/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/ia/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/id/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/it/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/ja/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/ka/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/ko/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/lt/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/nb/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/nl/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/nn/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/pl/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/pt/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/pt_BR/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/ro/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/ru/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/sk/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/sl/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/sr/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/sr@ijekavian/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/sr@latin/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/sv/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/tr/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/uk/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/zh_CN/LC_MESSAGES/akonadi_search.mo
* /usr/share/locale/zh_TW/LC_MESSAGES/akonadi_search.mo
* /usr/share/qlogging-categories5/akonadi-search.categories
* /usr/share/qlogging-categories5/akonadi-search.renamecategories
{{< /files >}}