#!/usr/bin/env python
# encoding: utf-8
"""
setup.py

Created by Ryan Balfanz on 2010-01-30.
Copyright (c) 2010 Ryan Balfanz. All rights reserved.
"""

from distutils.core import setup

setup(name='PyPDS',
	version='0.1',
	description='PyPDS is a Python interface to Planetary Data System (PDS) data products',
	author='Ryan Balfanz',
	author_email='ryan@ryanbalfanz.net',
	url='http://github.com/RyanBalfanz/PyPDS',
	package_dir={'': 'src'},
	packages=['pds', 'pds.core'],
	)