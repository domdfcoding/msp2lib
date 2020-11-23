#!/usr/bin/env python3
#
#  __init__.py
"""
Convert an MSP file representing one or more Mass Spectra to a NIST MS Search user library.

Docker must be installed to use this program.
"""
#
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as
#  published by the Free Software Foundation; either version 3 of
#  the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

# this package
from .core import main, msp2lib
from .utils import about, build_docker_image, download_docker_image, subprocess_with_log, test_docker, version

__author__ = "Dominic Davis-Foster"
__copyright__ = "2020 Dominic Davis-Foster"
__license__ = "LGPLv3"
__version__ = "0.1.3"
__email__ = "dominic@davis-foster.co.uk"
