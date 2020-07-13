#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import re

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('..'))

from __pkginfo__ import __version__

copyright = (
		f"Copyright 2020 Dominic Davis-Foster. License LGPLv3+: GNU LGPL version 3 or later "
		f"<http://gnu.org/licenses/lgpl.html>\n\n"
		"This is free software: you are free to change and redistribute it under certain conditions.\n\n"
		"There is NO WARRANTY, to the extent permitted by law."
		)

author = "Dominic Davis-Foster"
project = "msp2lib"
release = version = f"{project} {__version__}"
language = 'en'
slug = re.sub(r'\W+', '-', project.lower())

master_doc = 'manpage'

extensions = [
		'sphinx.ext.intersphinx',
		'sphinx.ext.autodoc',
		'sphinx.ext.mathjax',
		'sphinx.ext.viewcode',
		'sphinxcontrib.httpdomain',
		]

source_suffix = '.rst'
exclude_patterns = []

html_context = {"conf_py_path": "/"}

htmlhelp_basename = slug

man_pages = [(master_doc, slug, project, [author], 1)]
