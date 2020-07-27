#!/usr/bin/env python
# This file is managed by 'repo_helper'. Don't edit it directly.

# stdlib
import os
import pathlib
import sys
import warnings

# 3rd party
from setuptools import setup

sys.path.append('.')

# this package
from __pkginfo__ import *  # pylint: disable=wildcard-import

if not pathlib.Path("msp2lib.1").is_file():
	warnings.warn("manpage not found. Trying to build now.")
	exit_code = os.system("./make_manpage.sh")
	if exit_code:
		sys.exit(exit_code)

setup(
		description="Convert an MSP file representing one or more Mass Spectra to a NIST MS Search user library.",
		extras_require=extras_require,
		install_requires=install_requires,
		py_modules=[],
		version=__version__,
		)

# TODO: include manpage in wheel and put in right place on filesystem
