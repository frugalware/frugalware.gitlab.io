+++
draft = false
title = "flickcurl 1.26-4"
version = "1.26-4"
description = "C library for the Flickr API"
date = "2022-02-08T15:01:17"
aliases = "/packages/219326"
categories = ['lib-extra']
upstreamurl = "http://librdf.org/flickcurl/"
arch = "x86_64"
size = "794752"
usize = "2780537"
sha1sum = "dcadeec2f09b6866264b2171015f239b98f43434"
depends = "['curl', 'raptor']"
reverse_depends = "['darktable']"
+++
C library for the Flickr API{{< files text="show files" >}}* /usr/bin/flickcurl
* /usr/bin/flickcurl-config
* /usr/bin/flickrdf
* /usr/include/flickcurl.h
* /usr/lib/libflickcurl.so
* /usr/lib/libflickcurl.so.0
* /usr/lib/libflickcurl.so.0.0.0
* /usr/lib/pkgconfig/flickcurl.pc
* /usr/share/doc/flickcurl-1.26/AUTHORS
* /usr/share/doc/flickcurl-1.26/ChangeLog
* /usr/share/doc/flickcurl-1.26/COPYING
* /usr/share/doc/flickcurl-1.26/COPYING.LIB
* /usr/share/doc/flickcurl-1.26/INSTALL
* /usr/share/doc/flickcurl-1.26/NEWS
* /usr/share/doc/flickcurl-1.26/README
* /usr/share/doc/flickcurl-1.26/README.html
* /usr/share/gtk-doc/html/flickcurl/appgarden-commercial-picker.png
* /usr/share/gtk-doc/html/flickcurl/appgarden-edit-auth-flow-mobile.png
* /usr/share/gtk-doc/html/flickcurl/appgarden-edit-auth-flow.png
* /usr/share/gtk-doc/html/flickcurl/appgarden-get-your-api-key.png
* /usr/share/gtk-doc/html/flickcurl/appgarden-mobile-auth-page.png
* /usr/share/gtk-doc/html/flickcurl/appgarden-new-api-key-secret.png
* /usr/share/gtk-doc/html/flickcurl/appgarden-tell-us-about-your-app.png
* /usr/share/gtk-doc/html/flickcurl/appgarden-test-app-page.png
* /usr/share/gtk-doc/html/flickcurl/flickcurl-auth-authenticate.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-auth-build.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-auth-register.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-auth-upgrade.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-auth-use.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-auth.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-legacy-auth-authenticate.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-legacy-auth-build.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-legacy-auth-register.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-legacy-auth-use.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-legacy-auth.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-searching-search-example.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-searching-search-extras.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-searching-search-paging.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-searching-search-parameters.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-searching-search-result-formats.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-searching-search-results.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-searching-search-run.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-searching.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-activity.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-auth.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-blogs.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-category.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-collections.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-comment.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-commons.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-config.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-contact.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-context.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-core.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-exif.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-favorite.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-gallery.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-general.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-group.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-machinetags.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-misc.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-note.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-panda.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-people.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-person.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-photo.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-photos-people.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-photoset.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-photoslist.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-place.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-prefs.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-reflection.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-serializer.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-stats.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-tag.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-test.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-upload.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-urls.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl-section-video.html
* /usr/share/gtk-doc/html/flickcurl/flickcurl.devhelp2
* /usr/share/gtk-doc/html/flickcurl/home.png
* /usr/share/gtk-doc/html/flickcurl/index.html
* /usr/share/gtk-doc/html/flickcurl/index.sgml
* /usr/share/gtk-doc/html/flickcurl/indexes.html
* /usr/share/gtk-doc/html/flickcurl/introduction.html
* /usr/share/gtk-doc/html/flickcurl/left.png
* /usr/share/gtk-doc/html/flickcurl/right.png
* /usr/share/gtk-doc/html/flickcurl/style.css
* /usr/share/gtk-doc/html/flickcurl/up.png
* /usr/share/man/man1/flickcurl-config.1.gz
* /usr/share/man/man1/flickcurl.1.gz
* /usr/share/man/man1/flickrdf.1.gz
{{< /files >}}