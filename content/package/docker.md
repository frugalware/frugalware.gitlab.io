+++
draft = false
title = "docker 28.3.2-1"
version = "28.3.2-1"
description = "Docker - the Linux container runtime"
date = "2025-07-10T09:44:24"
aliases = "/packages/217244"
categories = ['apps-extra']
upstreamurl = "https://github.com/docker/cli"
arch = "x86_64"
size = "26102596"
usize = "111960132"
sha1sum = "3e5f2428fdef44aaf79e5ae667cfd5dbe12815ce"
depends = "['bridge-utils', 'btrfs-progs>=4.10-2', 'containerd', 'iproute2', 'lvm2', 'runc', 'sqlite3', 'tini']"
reverse_depends = "['docker-compose']"
+++
### Description: 
Docker - the Linux container runtime

### Files: 
* /etc/modprobe.d/overlay.conf
* /usr/bin/docker
* /usr/bin/docker-proxy
* /usr/bin/dockerd
* /usr/lib/systemd/system/docker.service
* /usr/lib/systemd/system/docker.socket
* /usr/lib/sysusers.d/docker.conf
* /usr/share/bash-completion/completions/docker
* /usr/share/fish/vendor_completions.d/docker.fish
* /usr/share/man/man1/docker-attach.1.gz
* /usr/share/man/man1/docker-bake.1.gz
* /usr/share/man/man1/docker-build.1.gz
* /usr/share/man/man1/docker-builder-build.1.gz
* /usr/share/man/man1/docker-builder-prune.1.gz
* /usr/share/man/man1/docker-builder.1.gz
* /usr/share/man/man1/docker-checkpoint-create.1.gz
* /usr/share/man/man1/docker-checkpoint-ls.1.gz
* /usr/share/man/man1/docker-checkpoint-rm.1.gz
* /usr/share/man/man1/docker-checkpoint.1.gz
* /usr/share/man/man1/docker-commit.1.gz
* /usr/share/man/man1/docker-config-create.1.gz
* /usr/share/man/man1/docker-config-inspect.1.gz
* /usr/share/man/man1/docker-config-ls.1.gz
* /usr/share/man/man1/docker-config-rm.1.gz
* /usr/share/man/man1/docker-config.1.gz
* /usr/share/man/man1/docker-container-attach.1.gz
* /usr/share/man/man1/docker-container-commit.1.gz
* /usr/share/man/man1/docker-container-cp.1.gz
* /usr/share/man/man1/docker-container-create.1.gz
* /usr/share/man/man1/docker-container-diff.1.gz
* /usr/share/man/man1/docker-container-exec.1.gz
* /usr/share/man/man1/docker-container-export.1.gz
* /usr/share/man/man1/docker-container-inspect.1.gz
* /usr/share/man/man1/docker-container-kill.1.gz
* /usr/share/man/man1/docker-container-logs.1.gz
* /usr/share/man/man1/docker-container-ls.1.gz
* /usr/share/man/man1/docker-container-pause.1.gz
* /usr/share/man/man1/docker-container-port.1.gz
* /usr/share/man/man1/docker-container-prune.1.gz
* /usr/share/man/man1/docker-container-rename.1.gz
* /usr/share/man/man1/docker-container-restart.1.gz
* /usr/share/man/man1/docker-container-rm.1.gz
* /usr/share/man/man1/docker-container-run.1.gz
* /usr/share/man/man1/docker-container-start.1.gz
* /usr/share/man/man1/docker-container-stats.1.gz
* /usr/share/man/man1/docker-container-stop.1.gz
* /usr/share/man/man1/docker-container-top.1.gz
* /usr/share/man/man1/docker-container-unpause.1.gz
* /usr/share/man/man1/docker-container-update.1.gz
* /usr/share/man/man1/docker-container-wait.1.gz
* /usr/share/man/man1/docker-container.1.gz
* /usr/share/man/man1/docker-context-create.1.gz
* /usr/share/man/man1/docker-context-export.1.gz
* /usr/share/man/man1/docker-context-import.1.gz
* /usr/share/man/man1/docker-context-inspect.1.gz
* /usr/share/man/man1/docker-context-ls.1.gz
* /usr/share/man/man1/docker-context-rm.1.gz
* /usr/share/man/man1/docker-context-show.1.gz
* /usr/share/man/man1/docker-context-update.1.gz
* /usr/share/man/man1/docker-context-use.1.gz
* /usr/share/man/man1/docker-context.1.gz
* /usr/share/man/man1/docker-cp.1.gz
* /usr/share/man/man1/docker-create.1.gz
* /usr/share/man/man1/docker-diff.1.gz
* /usr/share/man/man1/docker-events.1.gz
* /usr/share/man/man1/docker-exec.1.gz
* /usr/share/man/man1/docker-export.1.gz
* /usr/share/man/man1/docker-history.1.gz
* /usr/share/man/man1/docker-image-build.1.gz
* /usr/share/man/man1/docker-image-history.1.gz
* /usr/share/man/man1/docker-image-import.1.gz
* /usr/share/man/man1/docker-image-inspect.1.gz
* /usr/share/man/man1/docker-image-load.1.gz
* /usr/share/man/man1/docker-image-ls.1.gz
* /usr/share/man/man1/docker-image-prune.1.gz
* /usr/share/man/man1/docker-image-pull.1.gz
* /usr/share/man/man1/docker-image-push.1.gz
* /usr/share/man/man1/docker-image-rm.1.gz
* /usr/share/man/man1/docker-image-save.1.gz
* /usr/share/man/man1/docker-image-tag.1.gz
* /usr/share/man/man1/docker-image.1.gz
* /usr/share/man/man1/docker-images.1.gz
* /usr/share/man/man1/docker-import.1.gz
* /usr/share/man/man1/docker-info.1.gz
* /usr/share/man/man1/docker-inspect.1.gz
* /usr/share/man/man1/docker-kill.1.gz
* /usr/share/man/man1/docker-load.1.gz
* /usr/share/man/man1/docker-login.1.gz
* /usr/share/man/man1/docker-logout.1.gz
* /usr/share/man/man1/docker-logs.1.gz
* /usr/share/man/man1/docker-manifest-annotate.1.gz
* /usr/share/man/man1/docker-manifest-create.1.gz
* /usr/share/man/man1/docker-manifest-inspect.1.gz
* /usr/share/man/man1/docker-manifest-push.1.gz
* /usr/share/man/man1/docker-manifest-rm.1.gz
* /usr/share/man/man1/docker-manifest.1.gz
* /usr/share/man/man1/docker-network-connect.1.gz
* /usr/share/man/man1/docker-network-create.1.gz
* /usr/share/man/man1/docker-network-disconnect.1.gz
* /usr/share/man/man1/docker-network-inspect.1.gz
* /usr/share/man/man1/docker-network-ls.1.gz
* /usr/share/man/man1/docker-network-prune.1.gz
* /usr/share/man/man1/docker-network-rm.1.gz
* /usr/share/man/man1/docker-network.1.gz
* /usr/share/man/man1/docker-node-demote.1.gz
* /usr/share/man/man1/docker-node-inspect.1.gz
* /usr/share/man/man1/docker-node-ls.1.gz
* /usr/share/man/man1/docker-node-promote.1.gz
* /usr/share/man/man1/docker-node-ps.1.gz
* /usr/share/man/man1/docker-node-rm.1.gz
* /usr/share/man/man1/docker-node-update.1.gz
* /usr/share/man/man1/docker-node.1.gz
* /usr/share/man/man1/docker-pause.1.gz
* /usr/share/man/man1/docker-plugin-create.1.gz
* /usr/share/man/man1/docker-plugin-disable.1.gz
* /usr/share/man/man1/docker-plugin-enable.1.gz
* /usr/share/man/man1/docker-plugin-inspect.1.gz
* /usr/share/man/man1/docker-plugin-install.1.gz
* /usr/share/man/man1/docker-plugin-ls.1.gz
* /usr/share/man/man1/docker-plugin-push.1.gz
* /usr/share/man/man1/docker-plugin-rm.1.gz
* /usr/share/man/man1/docker-plugin-set.1.gz
* /usr/share/man/man1/docker-plugin-upgrade.1.gz
* /usr/share/man/man1/docker-plugin.1.gz
* /usr/share/man/man1/docker-port.1.gz
* /usr/share/man/man1/docker-ps.1.gz
* /usr/share/man/man1/docker-pull.1.gz
* /usr/share/man/man1/docker-push.1.gz
* /usr/share/man/man1/docker-rename.1.gz
* /usr/share/man/man1/docker-restart.1.gz
* /usr/share/man/man1/docker-rm.1.gz
* /usr/share/man/man1/docker-rmi.1.gz
* /usr/share/man/man1/docker-run.1.gz
* /usr/share/man/man1/docker-save.1.gz
* /usr/share/man/man1/docker-search.1.gz
* /usr/share/man/man1/docker-secret-create.1.gz
* /usr/share/man/man1/docker-secret-inspect.1.gz
* /usr/share/man/man1/docker-secret-ls.1.gz
* /usr/share/man/man1/docker-secret-rm.1.gz
* /usr/share/man/man1/docker-secret.1.gz
* /usr/share/man/man1/docker-service-create.1.gz
* /usr/share/man/man1/docker-service-inspect.1.gz
* /usr/share/man/man1/docker-service-logs.1.gz
* /usr/share/man/man1/docker-service-ls.1.gz
* /usr/share/man/man1/docker-service-ps.1.gz
* /usr/share/man/man1/docker-service-rm.1.gz
* /usr/share/man/man1/docker-service-rollback.1.gz
* /usr/share/man/man1/docker-service-scale.1.gz
* /usr/share/man/man1/docker-service-update.1.gz
* /usr/share/man/man1/docker-service.1.gz
* /usr/share/man/man1/docker-stack-config.1.gz
* /usr/share/man/man1/docker-stack-deploy.1.gz
* /usr/share/man/man1/docker-stack-ls.1.gz
* /usr/share/man/man1/docker-stack-ps.1.gz
* /usr/share/man/man1/docker-stack-rm.1.gz
* /usr/share/man/man1/docker-stack-services.1.gz
* /usr/share/man/man1/docker-stack.1.gz
* /usr/share/man/man1/docker-start.1.gz
* /usr/share/man/man1/docker-stats.1.gz
* /usr/share/man/man1/docker-stop.1.gz
* /usr/share/man/man1/docker-swarm-ca.1.gz
* /usr/share/man/man1/docker-swarm-init.1.gz
* /usr/share/man/man1/docker-swarm-join-token.1.gz
* /usr/share/man/man1/docker-swarm-join.1.gz
* /usr/share/man/man1/docker-swarm-leave.1.gz
* /usr/share/man/man1/docker-swarm-unlock-key.1.gz
* /usr/share/man/man1/docker-swarm-unlock.1.gz
* /usr/share/man/man1/docker-swarm-update.1.gz
* /usr/share/man/man1/docker-swarm.1.gz
* /usr/share/man/man1/docker-system-df.1.gz
* /usr/share/man/man1/docker-system-events.1.gz
* /usr/share/man/man1/docker-system-info.1.gz
* /usr/share/man/man1/docker-system-prune.1.gz
* /usr/share/man/man1/docker-system.1.gz
* /usr/share/man/man1/docker-tag.1.gz
* /usr/share/man/man1/docker-top.1.gz
* /usr/share/man/man1/docker-trust-inspect.1.gz
* /usr/share/man/man1/docker-trust-key-generate.1.gz
* /usr/share/man/man1/docker-trust-key-load.1.gz
* /usr/share/man/man1/docker-trust-key.1.gz
* /usr/share/man/man1/docker-trust-revoke.1.gz
* /usr/share/man/man1/docker-trust-sign.1.gz
* /usr/share/man/man1/docker-trust-signer-add.1.gz
* /usr/share/man/man1/docker-trust-signer-remove.1.gz
* /usr/share/man/man1/docker-trust-signer.1.gz
* /usr/share/man/man1/docker-trust.1.gz
* /usr/share/man/man1/docker-unpause.1.gz
* /usr/share/man/man1/docker-update.1.gz
* /usr/share/man/man1/docker-version.1.gz
* /usr/share/man/man1/docker-volume-create.1.gz
* /usr/share/man/man1/docker-volume-inspect.1.gz
* /usr/share/man/man1/docker-volume-ls.1.gz
* /usr/share/man/man1/docker-volume-prune.1.gz
* /usr/share/man/man1/docker-volume-rm.1.gz
* /usr/share/man/man1/docker-volume-update.1.gz
* /usr/share/man/man1/docker-volume.1.gz
* /usr/share/man/man1/docker-wait.1.gz
* /usr/share/man/man1/docker.1.gz
* /usr/share/man/man5/docker-config-json.5.gz
* /usr/share/man/man5/Dockerfile.5.gz
* /usr/share/zsh/site-functions/_docker
