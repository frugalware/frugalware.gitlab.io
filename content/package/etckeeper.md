+++
draft = false
title = "etckeeper 1.18.21-1"
version = "1.18.21-1"
description = "Stores the /etc directory in a git repo."
date = "2024-01-14T16:20:47"
aliases = "/packages/38744"
categories = ['apps-extra']
upstreamurl = "https://etckeeper.branchable.com/"
arch = "x86_64"
size = "33892"
usize = "93191"
sha1sum = "8068b3fb98660f4fd827d524a44c06587842ff67"
depends = "['dcron>=3.2-4', 'git>=1.5.3.4', 'pacman-g2>=3.6.7']"
+++
### Description: 
Stores the /etc directory in a git repo.

### Files: 
* /etc/etckeeper/commit.d/10vcs-test
* /etc/etckeeper/commit.d/20store-metadata
* /etc/etckeeper/commit.d/30bzr-add
* /etc/etckeeper/commit.d/30darcs-add
* /etc/etckeeper/commit.d/30git-add
* /etc/etckeeper/commit.d/30hg-addremove
* /etc/etckeeper/commit.d/50vcs-commit
* /etc/etckeeper/commit.d/99push
* /etc/etckeeper/commit.d/README
* /etc/etckeeper/daily
* /etc/etckeeper/etckeeper.conf
* /etc/etckeeper/init.d/10restore-metadata
* /etc/etckeeper/init.d/20restore-etckeeper
* /etc/etckeeper/init.d/40vcs-init
* /etc/etckeeper/init.d/50vcs-ignore
* /etc/etckeeper/init.d/50vcs-perm
* /etc/etckeeper/init.d/50vcs-pre-commit-hook
* /etc/etckeeper/init.d/60darcs-deleted-symlinks
* /etc/etckeeper/init.d/70vcs-add
* /etc/etckeeper/init.d/README
* /etc/etckeeper/list-installed.d/50list-installed
* /etc/etckeeper/post-install.d/50vcs-commit
* /etc/etckeeper/post-install.d/README
* /etc/etckeeper/pre-commit.d/20warn-problem-files
* /etc/etckeeper/pre-commit.d/30store-metadata
* /etc/etckeeper/pre-commit.d/README
* /etc/etckeeper/pre-install.d/10packagelist
* /etc/etckeeper/pre-install.d/50uncommitted-changes
* /etc/etckeeper/pre-install.d/README
* /etc/etckeeper/unclean.d/50test
* /etc/etckeeper/unclean.d/README
* /etc/etckeeper/uninit.d/01prompt
* /etc/etckeeper/uninit.d/50remove-metadata
* /etc/etckeeper/uninit.d/50vcs-uninit
* /etc/etckeeper/uninit.d/README
* /etc/etckeeper/update-ignore.d/01update-ignore
* /etc/etckeeper/update-ignore.d/README
* /etc/etckeeper/vcs.d/50vcs-cmd
* /etc/pacman-g2/hooks/etckeeper
* /usr/bin/etckeeper
* /usr/lib/systemd/system/etckeeper.service
* /usr/lib/systemd/system/etckeeper.timer
* /usr/share/bash-completion/completions/etckeeper
* /usr/share/doc/etckeeper-1.18.21/CHANGELOG
* /usr/share/doc/etckeeper-1.18.21/COPYRIGHT
* /usr/share/doc/etckeeper-1.18.21/INSTALL
* /usr/share/doc/etckeeper-1.18.21/README.md
* /usr/share/man/man8/etckeeper.8.gz
* /usr/share/zsh/vendor-completions/_etckeeper
