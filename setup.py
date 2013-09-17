#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    readme = f.read()

requires = [
    'pelican',
]

setup(
    name='pelican-link-bugs',
    version='0.1',
    description='Automatically link bug tracker references.',
    long_description=readme,
    author='Paul McLanahan',
    author_email='paul@mclanahan.net',
    url='https://github.com/pmclanahan/pelican-list-bugs',
    py_modules=('pelican_bugs',),
    package_data={'': ['LICENSE', ]},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
    ),
)

