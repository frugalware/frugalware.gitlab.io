+++
draft = false
title = "python3-jsonschema 4.20.0-1"
version = "4.20.0-1"
description = "An implementation of JSON Schema validation for Python"
date = "2023-12-04T14:46:25"
aliases = "/packages/220537"
categories = ['devel-extra']
upstreamurl = "http://pypi.python.org/pypi/jsonschema"
arch = "x86_64"
size = "166408"
usize = "1360620"
sha1sum = "8eb945e89f5552270a2ecc9679a19715b35172bf"
depends = "['python3-attrs', 'python3-pyrsistent', 'python3-typing_extensions']"
reverse_depends = "['python3-poetry-core']"
+++
An implementation of JSON Schema validation for Python{{< files text="show files" >}}* /usr/bin/jsonschema
* /usr/lib/python3.12/site-packages/jsonschema-4.20.0.dist-info/entry_points.txt
* /usr/lib/python3.12/site-packages/jsonschema-4.20.0.dist-info/licenses/COPYING
* /usr/lib/python3.12/site-packages/jsonschema-4.20.0.dist-info/METADATA
* /usr/lib/python3.12/site-packages/jsonschema-4.20.0.dist-info/RECORD
* /usr/lib/python3.12/site-packages/jsonschema-4.20.0.dist-info/WHEEL
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/issue232.py
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/issue232/issue.json
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/json_schema_test_suite.py
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/nested_schemas.py
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/subcomponents.py
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/unused_registry.py
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/validator_creation.py
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/__init__.py
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/__pycache__/issue232.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/__pycache__/issue232.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/__pycache__/json_schema_test_suite.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/__pycache__/json_schema_test_suite.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/__pycache__/nested_schemas.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/__pycache__/nested_schemas.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/__pycache__/subcomponents.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/__pycache__/subcomponents.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/__pycache__/unused_registry.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/__pycache__/unused_registry.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/__pycache__/validator_creation.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/__pycache__/validator_creation.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/benchmarks/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/cli.py
* /usr/lib/python3.12/site-packages/jsonschema/exceptions.py
* /usr/lib/python3.12/site-packages/jsonschema/protocols.py
* /usr/lib/python3.12/site-packages/jsonschema/tests/fuzz_validate.py
* /usr/lib/python3.12/site-packages/jsonschema/tests/test_cli.py
* /usr/lib/python3.12/site-packages/jsonschema/tests/test_deprecations.py
* /usr/lib/python3.12/site-packages/jsonschema/tests/test_exceptions.py
* /usr/lib/python3.12/site-packages/jsonschema/tests/test_format.py
* /usr/lib/python3.12/site-packages/jsonschema/tests/test_jsonschema_test_suite.py
* /usr/lib/python3.12/site-packages/jsonschema/tests/test_types.py
* /usr/lib/python3.12/site-packages/jsonschema/tests/test_utils.py
* /usr/lib/python3.12/site-packages/jsonschema/tests/test_validators.py
* /usr/lib/python3.12/site-packages/jsonschema/tests/_suite.py
* /usr/lib/python3.12/site-packages/jsonschema/tests/__init__.py
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/fuzz_validate.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/fuzz_validate.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/test_cli.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/test_cli.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/test_deprecations.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/test_deprecations.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/test_exceptions.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/test_exceptions.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/test_format.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/test_format.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/test_jsonschema_test_suite.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/test_jsonschema_test_suite.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/test_types.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/test_types.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/test_utils.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/test_utils.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/test_validators.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/test_validators.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/_suite.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/_suite.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/tests/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/validators.py
* /usr/lib/python3.12/site-packages/jsonschema/_format.py
* /usr/lib/python3.12/site-packages/jsonschema/_keywords.py
* /usr/lib/python3.12/site-packages/jsonschema/_legacy_keywords.py
* /usr/lib/python3.12/site-packages/jsonschema/_types.py
* /usr/lib/python3.12/site-packages/jsonschema/_typing.py
* /usr/lib/python3.12/site-packages/jsonschema/_utils.py
* /usr/lib/python3.12/site-packages/jsonschema/__init__.py
* /usr/lib/python3.12/site-packages/jsonschema/__main__.py
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/cli.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/cli.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/exceptions.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/exceptions.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/protocols.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/protocols.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/validators.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/validators.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/_format.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/_format.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/_keywords.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/_keywords.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/_legacy_keywords.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/_legacy_keywords.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/_types.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/_types.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/_typing.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/_typing.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/_utils.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/_utils.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/__main__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/jsonschema/__pycache__/__main__.cpython-312.pyc
* /usr/share/doc/python3-jsonschema-4.20.0/COPYING
* /usr/share/doc/python3-jsonschema-4.20.0/README.rst
{{< /files >}}