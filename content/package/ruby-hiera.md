+++
draft = false
title = "ruby-hiera 3.12.0-2"
version = "3.12.0-2"
description = "A pluggable data store for hierarchical data."
date = "2024-01-22T16:04:57"
aliases = "/packages/218444"
categories = ['devel-extra']
upstreamurl = "http://projects.puppetlabs.com/projects/hiera"
arch = "x86_64"
size = "82676"
usize = "246832"
sha1sum = "e3705c28ad4b0badb19888e9c2241cb576aaac35"
depends = "['ruby>=3.3.0', 'ruby>=3.3.0']"
reverse_depends = "['puppet']"
+++
A pluggable data store for hierarchical data."

{{< files text="show files" >}}* /etc/hiera.yaml
* /usr/bin/hiera
* /usr/lib/ruby/gems/3.3.0/cache/hiera-3.12.0.gem
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/cache.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/Backend1xWrapper/cdesc-Backend1xWrapper.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/Backend1xWrapper/lookup-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/Backend1xWrapper/new-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/cdesc-Backend.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/clear%21-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/datadir-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/datafile-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/datafile_in-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/datasourcefiles-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/datasources-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/find_backend-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/interpolate_config-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/Json_backend/cdesc-Json_backend.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/Json_backend/lookup-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/Json_backend/new-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/lookup-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/merge_answer-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/parse_answer-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/parse_string-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/qualified_lookup-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/resolve_answer-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/Yaml_backend/cdesc-Yaml_backend.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/Yaml_backend/file_exists%3f-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/Yaml_backend/lookup-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Backend/Yaml_backend/new-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/cdesc-Hiera.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/config-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Config/%5b%5d-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Config/cdesc-Config.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Config/include%3f-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Config/load-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Config/load_backends-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Config/validate%21-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Config/yaml_load_file-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Console_logger/cdesc-Console_logger.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Console_logger/debug-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Console_logger/warn-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/debug-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Error/cdesc-Error.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/FallbackLogger/cdesc-FallbackLogger.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/FallbackLogger/debug-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/FallbackLogger/new-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/FallbackLogger/warn-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Filecache/cdesc-Filecache.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Filecache/new-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Filecache/path_metadata-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Filecache/read-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Filecache/read_file-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Filecache/stale%3f-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Interpolate/alias_interpolate-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Interpolate/cdesc-Interpolate.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Interpolate/do_interpolation-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Interpolate/get_interpolation_method_and_key-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Interpolate/hiera_interpolate-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Interpolate/interpolate-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Interpolate/literal_interpolate-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Interpolate/scope_interpolate-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/InterpolationInvalidValue/cdesc-InterpolationInvalidValue.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/InterpolationLoop/cdesc-InterpolationLoop.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/InvalidConfigurationError/cdesc-InvalidConfigurationError.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/logger%3d-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/logger-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/lookup-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/new-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Noop_logger/cdesc-Noop_logger.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Noop_logger/debug-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Noop_logger/warn-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/options-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Puppet_logger/cdesc-Puppet_logger.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Puppet_logger/debug-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Puppet_logger/suitable%3f-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Puppet_logger/warn-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/read_version_file-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/RecursiveGuard/cdesc-RecursiveGuard.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/RecursiveGuard/check-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/RecursiveGuard/new-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Util/cdesc-Util.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Util/code_dir-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Util/common_appdata-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Util/config_dir-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Util/file_alt_separator-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Util/microsoft_windows%3f-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Util/posix%3f-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Util/split_key-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Util/var_dir-i.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Util/Win32/cdesc-Win32.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/Util/Win32/get_common_appdata-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/version%3d-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/version-c.ri
* /usr/lib/ruby/gems/3.3.0/doc/hiera-3.12.0/ri/Hiera/warn-c.ri
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/bin/hiera
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/COPYING
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/lib/hiera.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/lib/hiera/backend.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/lib/hiera/backend/json_backend.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/lib/hiera/backend/yaml_backend.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/lib/hiera/config.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/lib/hiera/console_logger.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/lib/hiera/error.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/lib/hiera/fallback_logger.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/lib/hiera/filecache.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/lib/hiera/interpolate.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/lib/hiera/noop_logger.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/lib/hiera/puppet_logger.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/lib/hiera/recursive_guard.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/lib/hiera/util.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/lib/hiera/util/win32.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/lib/hiera/version.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/LICENSE
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/README.md
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/spec_helper.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/backend/json_backend_spec.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/backend/yaml_backend_spec.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/backend_spec.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/config_spec.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/console_logger_spec.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/fallback_logger_spec.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/filecache_spec.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/fixtures/badconfig/config/hiera.yaml
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/fixtures/badconfig/data/common.yaml
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/config/hiera.yaml
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/config/hiera_iplm_hiera.yaml
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/config/hiera_iplm_hiera_bad.yaml
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/data/bad_interpolation.yaml
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/data/complex.yaml
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/data/dotted_keys.yaml
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/data/empty_interpolation.yaml
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/data/frontend.json
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/data/niltest.yaml
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/data/recursive.yaml
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/data/role.json
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/fixtures/interpolate/data/weird_keys.yaml
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/fixtures/override/config/hiera.yaml
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/fixtures/override/data/alternate.yaml
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/fixtures/override/data/common.yaml
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/hiera_spec.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/interpolate_spec.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/puppet_logger_spec.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/util_spec.rb
* /usr/lib/ruby/gems/3.3.0/gems/hiera-3.12.0/spec/unit/version_spec.rb
* /usr/lib/ruby/gems/3.3.0/specifications/hiera-3.12.0.gemspec
{{< /files >}}