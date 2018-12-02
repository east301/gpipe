#!/usr/bin/env python3
#
# copyright (c) 2018 east301
#
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php
#

try:
    import setuptools_scm
    print(setuptools_scm.get_version(root='..', relative_to=__file__))
except (ImportError, LookupError):
    print('0.0.0')
