+++
draft = false
title = "ostree 2024.5-1"
version = "2024.5-1"
description = "Operating system and container binary deployment and upgrades"
date = "2024-06-04T19:30:44"
aliases = "/packages/220840"
categories = ['apps-extra']
upstreamurl = "https://github.com/ostreedev/ostree"
arch = "x86_64"
size = "700348"
usize = "4214338"
sha1sum = "902619dc9a3b4c05cf702788492cb16db76d6bd9"
depends = "['curl', 'fuse3', 'gpgme', 'libarchive', 'libsodium>=1.0.19', 'libsoup']"
reverse_depends = "['flatpak']"
+++
### Description: 
Operating system and container binary deployment and upgrades

### Files: 
* /etc/dracut.conf.d/ostree.conf
* /usr/bin/ostree
* /usr/bin/rofiles-fuse
* /usr/include/ostree-1/ostree-async-progress.h
* /usr/include/ostree-1/ostree-autocleanups.h
* /usr/include/ostree-1/ostree-bootconfig-parser.h
* /usr/include/ostree-1/ostree-content-writer.h
* /usr/include/ostree-1/ostree-core.h
* /usr/include/ostree-1/ostree-deployment.h
* /usr/include/ostree-1/ostree-diff.h
* /usr/include/ostree-1/ostree-dummy-enumtypes.h
* /usr/include/ostree-1/ostree-gpg-verify-result.h
* /usr/include/ostree-1/ostree-kernel-args.h
* /usr/include/ostree-1/ostree-mutable-tree.h
* /usr/include/ostree-1/ostree-ref.h
* /usr/include/ostree-1/ostree-remote.h
* /usr/include/ostree-1/ostree-repo-deprecated.h
* /usr/include/ostree-1/ostree-repo-file.h
* /usr/include/ostree-1/ostree-repo-finder-avahi.h
* /usr/include/ostree-1/ostree-repo-finder-config.h
* /usr/include/ostree-1/ostree-repo-finder-mount.h
* /usr/include/ostree-1/ostree-repo-finder-override.h
* /usr/include/ostree-1/ostree-repo-finder.h
* /usr/include/ostree-1/ostree-repo-os.h
* /usr/include/ostree-1/ostree-repo.h
* /usr/include/ostree-1/ostree-sepolicy.h
* /usr/include/ostree-1/ostree-sign-ed25519.h
* /usr/include/ostree-1/ostree-sign.h
* /usr/include/ostree-1/ostree-sysroot-upgrader.h
* /usr/include/ostree-1/ostree-sysroot.h
* /usr/include/ostree-1/ostree-types.h
* /usr/include/ostree-1/ostree-version.h
* /usr/include/ostree-1/ostree.h
* /usr/lib/dracut/modules.d/98ostree/module-setup.sh
* /usr/lib/girepository-1.0/OSTree-1.0.typelib
* /usr/lib/libostree-1.so
* /usr/lib/libostree-1.so.1
* /usr/lib/libostree-1.so.1.0.0
* /usr/lib/ostree/ostree-grub-generator
* /usr/lib/ostree/ostree-prepare-root
* /usr/lib/ostree/ostree-remount
* /usr/lib/pkgconfig/ostree-1.pc
* /usr/lib/systemd/system-generators/ostree-system-generator
* /usr/lib/systemd/system/ostree-boot-complete.service
* /usr/lib/systemd/system/ostree-finalize-staged-hold.service
* /usr/lib/systemd/system/ostree-finalize-staged.path
* /usr/lib/systemd/system/ostree-finalize-staged.service
* /usr/lib/systemd/system/ostree-prepare-root.service
* /usr/lib/systemd/system/ostree-remount.service
* /usr/lib/systemd/system/ostree-state-overlay@.service
* /usr/lib/tmpfiles.d/ostree-tmpfiles.conf
* /usr/share/bash-completion/completions/ostree
* /usr/share/doc/ostree-2024.5/COPYING
* /usr/share/doc/ostree-2024.5/README.md
* /usr/share/doc/ostree-2024.5/TODO
* /usr/share/gir-1.0/OSTree-1.0.gir
* /usr/share/gtk-doc/html/ostree/home.png
* /usr/share/gtk-doc/html/ostree/index.html
* /usr/share/gtk-doc/html/ostree/left-insensitive.png
* /usr/share/gtk-doc/html/ostree/left.png
* /usr/share/gtk-doc/html/ostree/ostree-Core-repository-independent-functions.html
* /usr/share/gtk-doc/html/ostree/ostree-GPG-signature-verification-results.html
* /usr/share/gtk-doc/html/ostree/ostree-In-memory-modifiable-filesystem-tree.html
* /usr/share/gtk-doc/html/ostree/ostree-ostree-bootconfig-parser.html
* /usr/share/gtk-doc/html/ostree/ostree-ostree-chain-input-stream.html
* /usr/share/gtk-doc/html/ostree/ostree-ostree-checksum-input-stream.html
* /usr/share/gtk-doc/html/ostree/ostree-ostree-content-writer.html
* /usr/share/gtk-doc/html/ostree/ostree-ostree-deployment.html
* /usr/share/gtk-doc/html/ostree/ostree-ostree-diff.html
* /usr/share/gtk-doc/html/ostree/ostree-ostree-kernel-args.html
* /usr/share/gtk-doc/html/ostree/ostree-ostree-ref.html
* /usr/share/gtk-doc/html/ostree/ostree-ostree-remote.html
* /usr/share/gtk-doc/html/ostree/ostree-ostree-repo-file.html
* /usr/share/gtk-doc/html/ostree/ostree-ostree-repo-finder.html
* /usr/share/gtk-doc/html/ostree/ostree-ostree-repo-remote-finder.html
* /usr/share/gtk-doc/html/ostree/ostree-ostree-version.html
* /usr/share/gtk-doc/html/ostree/ostree-OstreeRepo.html
* /usr/share/gtk-doc/html/ostree/ostree-Progress-notification-system-for-asynchronous-operations.html
* /usr/share/gtk-doc/html/ostree/ostree-Root-partition-mount-point.html
* /usr/share/gtk-doc/html/ostree/ostree-SELinux-policy-management.html
* /usr/share/gtk-doc/html/ostree/ostree-Signature-management.html
* /usr/share/gtk-doc/html/ostree/ostree-Simple-upgrade-class.html
* /usr/share/gtk-doc/html/ostree/reference.html
* /usr/share/gtk-doc/html/ostree/right-insensitive.png
* /usr/share/gtk-doc/html/ostree/right.png
* /usr/share/gtk-doc/html/ostree/style.css
* /usr/share/gtk-doc/html/ostree/up-insensitive.png
* /usr/share/gtk-doc/html/ostree/up.png
* /usr/share/man/man1/ostree-admin-cleanup.1.gz
* /usr/share/man/man1/ostree-admin-config-diff.1.gz
* /usr/share/man/man1/ostree-admin-deploy.1.gz
* /usr/share/man/man1/ostree-admin-init-fs.1.gz
* /usr/share/man/man1/ostree-admin-instutil.1.gz
* /usr/share/man/man1/ostree-admin-lock-finalization.1.gz
* /usr/share/man/man1/ostree-admin-os-init.1.gz
* /usr/share/man/man1/ostree-admin-pin.1.gz
* /usr/share/man/man1/ostree-admin-post-copy.1.gz
* /usr/share/man/man1/ostree-admin-set-default.1.gz
* /usr/share/man/man1/ostree-admin-set-origin.1.gz
* /usr/share/man/man1/ostree-admin-stateroot-init.1.gz
* /usr/share/man/man1/ostree-admin-status.1.gz
* /usr/share/man/man1/ostree-admin-switch.1.gz
* /usr/share/man/man1/ostree-admin-undeploy.1.gz
* /usr/share/man/man1/ostree-admin-unlock.1.gz
* /usr/share/man/man1/ostree-admin-upgrade.1.gz
* /usr/share/man/man1/ostree-admin.1.gz
* /usr/share/man/man1/ostree-cat.1.gz
* /usr/share/man/man1/ostree-checkout.1.gz
* /usr/share/man/man1/ostree-checksum.1.gz
* /usr/share/man/man1/ostree-commit.1.gz
* /usr/share/man/man1/ostree-config.1.gz
* /usr/share/man/man1/ostree-create-usb.1.gz
* /usr/share/man/man1/ostree-diff.1.gz
* /usr/share/man/man1/ostree-export.1.gz
* /usr/share/man/man1/ostree-find-remotes.1.gz
* /usr/share/man/man1/ostree-fsck.1.gz
* /usr/share/man/man1/ostree-gpg-sign.1.gz
* /usr/share/man/man1/ostree-init.1.gz
* /usr/share/man/man1/ostree-log.1.gz
* /usr/share/man/man1/ostree-ls.1.gz
* /usr/share/man/man1/ostree-prepare-root.1.gz
* /usr/share/man/man1/ostree-prune.1.gz
* /usr/share/man/man1/ostree-pull-local.1.gz
* /usr/share/man/man1/ostree-pull.1.gz
* /usr/share/man/man1/ostree-refs.1.gz
* /usr/share/man/man1/ostree-remote.1.gz
* /usr/share/man/man1/ostree-reset.1.gz
* /usr/share/man/man1/ostree-rev-parse.1.gz
* /usr/share/man/man1/ostree-show.1.gz
* /usr/share/man/man1/ostree-sign.1.gz
* /usr/share/man/man1/ostree-static-delta.1.gz
* /usr/share/man/man1/ostree-summary.1.gz
* /usr/share/man/man1/ostree.1.gz
* /usr/share/man/man1/rofiles-fuse.1.gz
* /usr/share/man/man5/ostree.repo-config.5.gz
* /usr/share/man/man5/ostree.repo.5.gz
* /usr/share/man/man8/ostree-state-overlay@.service.8.gz
* /usr/share/ostree/trusted.gpg.d/README-gpg
