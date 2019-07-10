#!/usr/bin/env python

"""Distutils setup script for packaging and distribution."""

import pathlib

import setuptools

PROJECT_AUTHOR = 'Labrys of Knossos'
PROJECT_AUTHOR_EMAIL = 'labrys.git@gmail.com'
PROJECT_ROOT = pathlib.Path(__file__).parent
PROJECT_NAME = 'mediares'
PROJECT_VERSION = '0.0.0'
PROJECT_URL = ''
PROJECT_LICENSE = 'MIT License'
PROJECT_DESCRIPTION = 'A Python library for accessing media databases.'
PROJECT_README = PROJECT_ROOT / 'README.rst'
PROJECT_SOURCE_DIRECTORY = PROJECT_ROOT / 'src'
PROJECT_CLASSIFIERS = [
    # complete classifier list:
    #  http://pypi.python.org/pypi?%3Aaction=list_classifiers
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: Implementation :: CPython',
    'Topic :: Utilities',
]
PROJECT_KEYWORDS = [
    'media',
    'metadata',
]

setuptools.setup(
    name=PROJECT_NAME,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_AUTHOR_EMAIL,
    version=PROJECT_VERSION,
    license=PROJECT_LICENSE,
    description=PROJECT_DESCRIPTION,
    long_description=PROJECT_README.read_text('utf-8'),
    url=PROJECT_URL,
    packages=setuptools.find_packages(str(PROJECT_SOURCE_DIRECTORY)),
    package_dir={
        '': str(PROJECT_SOURCE_DIRECTORY.relative_to(PROJECT_ROOT)),
    },
    python_requires='>=3.7',
    include_package_data=True,
    zip_safe=False,
    classifiers=PROJECT_CLASSIFIERS,
    keywords=PROJECT_KEYWORDS,
)
