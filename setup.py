#!/usr/bin/env python
# coding: utf8
#
# Copyright (c) 2021 Centre National d'Etudes Spatiales (CNES).
#
# This file is part of PANDORA2D
#
#     https://github.com/CNES/Pandora2d
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
This module contains the required libraries and softwares allowing to execute the software,
and setup elements to configure and identify the software.
"""
from codecs import open as copen
from setuptools import setup

CMDCLASS = {}

try:
    from sphinx.setup_command import BuildDoc

    CMDCLASS["build_sphinx"] = BuildDoc
except ImportError:
    print("WARNING: sphinx not available. Doc cannot be built")

# Use Cython if available.
try:
    from Cython.Build import cythonize
except ImportError:
    raise SystemExit(
        "ERROR: Cython.Build.cythonize not found. "
        "Cython is required to build pandora2d.")

def readme():
    with copen("README.md", "r", "utf-8") as fstream:
        return fstream.read()


setup(
    use_scm_version=True,
    long_description=readme(),
    command_options={
        "build_sphinx": {
            "build_dir": ("setup.py", "doc/build/"),
            "source_dir": ("setup.py", "doc/sources/"),
            "warning_is_error": ("setup.py", True),
        }
    },
    ext_modules=cythonize("./pandora2d/refinement/fo_cython.pyx")
)
