+++
draft = false
title = "python3-rapidfuzz 3.5.2-1"
version = "3.5.2-1"
description = "Rapid fuzzy string matching in Python using various string metrics"
date = "2023-11-06T16:49:41"
aliases = "/packages/221158"
categories = ['devel-extra']
upstreamurl = "http://pypi.python.org/pypi/rapidfuzz"
arch = "x86_64"
size = "1864272"
usize = "10624761"
sha1sum = "6de1204fcf15c1bac05a49a9e079475cecda9e75"
depends = "['python3-numpy']"
reverse_depends = "['python3-cleo']"
+++
Rapid fuzzy string matching in Python using various string metrics

{{< files text="show files" >}}* /usr/lib/python3.12/site-packages/rapidfuzz-3.5.2.dist-info/entry_points.txt
* /usr/lib/python3.12/site-packages/rapidfuzz-3.5.2.dist-info/LICENSE
* /usr/lib/python3.12/site-packages/rapidfuzz-3.5.2.dist-info/METADATA
* /usr/lib/python3.12/site-packages/rapidfuzz-3.5.2.dist-info/RECORD
* /usr/lib/python3.12/site-packages/rapidfuzz-3.5.2.dist-info/top_level.txt
* /usr/lib/python3.12/site-packages/rapidfuzz-3.5.2.dist-info/WHEEL
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/DamerauLevenshtein.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/DamerauLevenshtein.pyi
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/DamerauLevenshtein_py.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/Hamming.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/Hamming.pyi
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/Hamming_py.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/Indel.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/Indel.pyi
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/Indel_py.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/Jaro.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/Jaro.pyi
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/JaroWinkler.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/JaroWinkler.pyi
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/JaroWinkler_py.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/Jaro_py.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/LCSseq.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/LCSseq.pyi
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/LCSseq_py.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/Levenshtein.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/Levenshtein.pyi
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/Levenshtein_py.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/metrics_cpp.cpython-312-x86_64-linux-gnu.so
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/metrics_cpp.pyi
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/metrics_cpp_avx2.cpython-312-x86_64-linux-gnu.so
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/metrics_py.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/OSA.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/OSA.pyi
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/OSA_py.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/Postfix.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/Postfix_py.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/Prefix.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/Prefix_py.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/_initialize.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/_initialize.pyi
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/_initialize_cpp.cpython-312-x86_64-linux-gnu.so
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/_initialize_py.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__init__.py
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__init__.pyi
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/DamerauLevenshtein.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/DamerauLevenshtein.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/DamerauLevenshtein_py.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/DamerauLevenshtein_py.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Hamming.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Hamming.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Hamming_py.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Hamming_py.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Indel.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Indel.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Indel_py.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Indel_py.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Jaro.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Jaro.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/JaroWinkler.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/JaroWinkler.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/JaroWinkler_py.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/JaroWinkler_py.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Jaro_py.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Jaro_py.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/LCSseq.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/LCSseq.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/LCSseq_py.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/LCSseq_py.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Levenshtein.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Levenshtein.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Levenshtein_py.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Levenshtein_py.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/metrics_py.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/metrics_py.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/OSA.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/OSA.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/OSA_py.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/OSA_py.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Postfix.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Postfix.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Postfix_py.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Postfix_py.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Prefix.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Prefix.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Prefix_py.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/Prefix_py.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/_initialize.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/_initialize.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/_initialize_py.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/_initialize_py.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/distance/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/fuzz.py
* /usr/lib/python3.12/site-packages/rapidfuzz/fuzz.pyi
* /usr/lib/python3.12/site-packages/rapidfuzz/fuzz_cpp.cpython-312-x86_64-linux-gnu.so
* /usr/lib/python3.12/site-packages/rapidfuzz/fuzz_cpp_avx2.cpython-312-x86_64-linux-gnu.so
* /usr/lib/python3.12/site-packages/rapidfuzz/fuzz_py.py
* /usr/lib/python3.12/site-packages/rapidfuzz/process.py
* /usr/lib/python3.12/site-packages/rapidfuzz/process.pyi
* /usr/lib/python3.12/site-packages/rapidfuzz/process_cpp.py
* /usr/lib/python3.12/site-packages/rapidfuzz/process_cpp_impl.cpython-312-x86_64-linux-gnu.so
* /usr/lib/python3.12/site-packages/rapidfuzz/process_cpp_impl.pyi
* /usr/lib/python3.12/site-packages/rapidfuzz/process_py.py
* /usr/lib/python3.12/site-packages/rapidfuzz/py.typed
* /usr/lib/python3.12/site-packages/rapidfuzz/rapidfuzz.h
* /usr/lib/python3.12/site-packages/rapidfuzz/utils.py
* /usr/lib/python3.12/site-packages/rapidfuzz/utils.pyi
* /usr/lib/python3.12/site-packages/rapidfuzz/utils_cpp.cpython-312-x86_64-linux-gnu.so
* /usr/lib/python3.12/site-packages/rapidfuzz/utils_py.py
* /usr/lib/python3.12/site-packages/rapidfuzz/_common_py.py
* /usr/lib/python3.12/site-packages/rapidfuzz/_feature_detector.py
* /usr/lib/python3.12/site-packages/rapidfuzz/_feature_detector_cpp.cpython-312-x86_64-linux-gnu.so
* /usr/lib/python3.12/site-packages/rapidfuzz/_utils.py
* /usr/lib/python3.12/site-packages/rapidfuzz/__init__.pxd
* /usr/lib/python3.12/site-packages/rapidfuzz/__init__.py
* /usr/lib/python3.12/site-packages/rapidfuzz/__init__.pyi
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/fuzz.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/fuzz.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/fuzz_py.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/fuzz_py.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/process.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/process.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/process_cpp.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/process_cpp.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/process_py.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/process_py.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/utils.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/utils.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/utils_py.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/utils_py.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/_common_py.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/_common_py.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/_feature_detector.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/_feature_detector.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/_utils.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/_utils.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pycache__/__init__.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pyinstaller/hook-rapidfuzz.py
* /usr/lib/python3.12/site-packages/rapidfuzz/__pyinstaller/test_rapidfuzz_packaging.py
* /usr/lib/python3.12/site-packages/rapidfuzz/__pyinstaller/__init__.py
* /usr/lib/python3.12/site-packages/rapidfuzz/__pyinstaller/__pycache__/hook-rapidfuzz.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pyinstaller/__pycache__/hook-rapidfuzz.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pyinstaller/__pycache__/test_rapidfuzz_packaging.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pyinstaller/__pycache__/test_rapidfuzz_packaging.cpython-312.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pyinstaller/__pycache__/__init__.cpython-312.opt-1.pyc
* /usr/lib/python3.12/site-packages/rapidfuzz/__pyinstaller/__pycache__/__init__.cpython-312.pyc
* /usr/share/doc/python3-rapidfuzz-3.5.2/LICENSE
* /usr/share/doc/python3-rapidfuzz-3.5.2/README.md
{{< /files >}}