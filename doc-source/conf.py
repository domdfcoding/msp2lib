#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('..'))

from sphinx_shared import *

version = __version__
copyright = __copyright__
master_doc = 'index'

# All other settings are in `sphinx_shared`
