#!/usr/bin/env python3
#
# copyright (c) 2018 east301
#
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php
#

import json
import os

from setuptools import setup


# ================================================================================
# dependency
# ================================================================================

def get_dependencies(category):
    dependencies = []
    with open(os.path.join(os.path.dirname(__file__), 'Pipfile.lock')) as fin:
        for key, value in json.load(fin)[category].items():
            dependencies.append(key + value['version'])

    return dependencies


# ================================================================================
# setup
# ================================================================================

setup(
    name='gpipe',
    use_scm_version=True,
    license='MIT',

    description='GridPipe',
    long_description='GridPipe',
    url='https://github.com/east301/gpipe',

    author='east301',
    author_email='me@east301.net',

    keywords='workflow manager grid engine',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ],

    packages=[
        'gpipe'
    ],
    package_data={
        'gpipe': [
            'templates/*.sh.j2'
        ]
    },

    install_requires=get_dependencies('default'),
    setup_requires=['setuptools_scm'],
    extras_require={
        'dev': get_dependencies('develop')
    },

    entry_points="""
        [console_scripts]
        gpipe = gpipe.cli:main
    """
)
