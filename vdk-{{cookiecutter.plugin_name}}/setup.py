# Copyright 2021 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0
import pathlib

import setuptools

"""
Builds a package with the help of setuptools in order for this package to be imported in other projects
"""

__version__ = "0.1.0"

setuptools.setup(
    name="vdk-{{cookiecutter.plugin_name}}",
    version=__version__,
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    url="https://github.com/vmware/versatile-data-kit",
    description='{{cookiecutter.short_description}}',
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    install_requires=["vdk-core"],
    package_dir={"": "src"},
    packages=setuptools.find_namespace_packages(where="src"),
    # This is the only vdk plugin specifc part
    # Define entry point called "vdk.plugin.run" with name of plugin and module to act as entry point.
    entry_points={
        "vdk.plugin.run": [
            "{{cookiecutter.plugin_name}} = vdk.plugin.{{cookiecutter.plugin_module_name}}.plugin_entry"
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
