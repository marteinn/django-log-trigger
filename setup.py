#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages

import log_trigger


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

# Handle requirements
install_requires = [
    'Django>=1.6'
]

tests_require = [
    'Django>=1.6'
]

# Convert markdown to rst
try:
    from pypandoc import convert
    long_description = convert("README.md", "rst")
except:
    long_description = ""


setup(
    name="django-log-trigger",
    version=log_trigger.__version__,
    description=("Simulate exceptions and logging calls in django through http"),  # NOQA
    long_description=long_description,
    author="Martin Sandström",
    author_email="martin@marteinn.se",
    url="https://github.com/marteinn/django-log-trigger",
    packages=find_packages(exclude=('tests*',)),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        'Environment :: Web Environment',
        "Intended Audience :: Developers",
        "Natural Language :: English",
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        'Framework :: Django',
        'Topic :: Utilities',
    ],
)
