#!/usr/bin/env python
"""Setup script"""

import os
import pathlib
import sys
import warnings

from setuptools import setup

from __pkginfo__ import (
	author, author_email, classifiers, entry_points, install_requires, license, long_description, modname, py_modules,
	short_desc, VERSION, web,
	)

if not pathlib.Path("msp2lib.1").is_file():
	warnings.warn("manpage not found. Trying to build now.")
	exit_code = os.system("./make_manpage.sh")
	if exit_code:
		sys.exit(exit_code)

setup(
		author=author,
		author_email=author_email,
		classifiers=classifiers,
		description=short_desc,
		entry_points=entry_points,
		install_requires=install_requires,
		license=license,
		long_description=long_description,
		name=modname,
		packages=None,
		py_modules=py_modules,
		url=web,
		version=VERSION,
		)

# TODO: include manpage in wheel and put in right place on filesystem
