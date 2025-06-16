+++
draft = false
title = "ruby-hiera 3.12.0-3"
version = "3.12.0-3"
description = "A pluggable data store for hierarchical data."
date = "2025-02-13T17:27:16"
aliases = "/packages/218444"
categories = ['devel-extra']
upstreamurl = "http://projects.puppetlabs.com/projects/hiera"
arch = "x86_64"
size = "74872"
usize = "196360"
sha1sum = "268d16b04ea9aafbba36dc826592bee652f5daee"
depends = "['ruby>=3.4.1']"
reverse_depends = "['puppet']"
+++
### Description: 
A pluggable data store for hierarchical data.

### Files: 
* /etc/hiera.yaml
* /usr/bin/hiera
* /usr/lib/ruby/gems/3.4.0/cache/hiera-3.12.0.gem
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/bin/hiera
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/COPYING
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/lib/hiera.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/lib/hiera/backend.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/lib/hiera/backend/json_backend.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/lib/hiera/backend/yaml_backend.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/lib/hiera/config.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/lib/hiera/console_logger.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/lib/hiera/error.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/lib/hiera/fallback_logger.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/lib/hiera/filecache.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/lib/hiera/interpolate.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/lib/hiera/noop_logger.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/lib/hiera/puppet_logger.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/lib/hiera/recursive_guard.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/lib/hiera/util.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/lib/hiera/util/win32.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/lib/hiera/version.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/LICENSE
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/README.md
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/spec_helper.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/backend/json_backend_spec.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/backend/yaml_backend_spec.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/backend_spec.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/config_spec.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/console_logger_spec.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/fallback_logger_spec.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/filecache_spec.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/fixtures/badconfig/config/hiera.yaml
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/fixtures/badconfig/data/common.yaml
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/config/hiera.yaml
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/config/hiera_iplm_hiera.yaml
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/config/hiera_iplm_hiera_bad.yaml
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/data/bad_interpolation.yaml
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/data/complex.yaml
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/data/dotted_keys.yaml
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/data/empty_interpolation.yaml
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/data/frontend.json
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/data/niltest.yaml
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/data/recursive.yaml
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/data/role.json
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/data/weird_keys.yaml
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/fixtures/override/config/hiera.yaml
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/fixtures/override/data/alternate.yaml
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/fixtures/override/data/common.yaml
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/hiera_spec.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/interpolate_spec.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/puppet_logger_spec.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/util_spec.rb
* /usr/lib/ruby/gems/3.4.0/gems/hiera-3.12.0/spec/unit/version_spec.rb
* /usr/lib/ruby/gems/3.4.0/specifications/hiera-3.12.0.gemspec
