#!/usr/bin/env python3
#
#  core.py
"""
Convert an MSP file representing one or more Mass Spectra to a NIST MS Search user library.

Docker must be installed to use this program.

The first time this script is run it will download the latest
version of the docker image automatically.

This can also be done manually, such as to upgrade to the latest version,
by running with the ``--get-docker-image`` flag.
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

# stdlib
import os
import pathlib
import shutil
import tempfile
from typing import Optional

# 3rd party
from domdf_python_tools.typing import PathLike

# this package
from .utils import _prep_workdirs

__all__ = ["msp2lib"]

# TODO: windows version
# TODO: ability to run multiple jobs in the same container, rather than starting and stopping them


def msp2lib(
		msp_file: PathLike,
		output_dir: PathLike,
		lib_name: Optional[str] = None,
		):
	"""
	Convert the provided MSP file to a NIST User Library, and store the newly
	created library in the given output directory.

	:param msp_file: The MSP file to convert to a NIST User Library
	:param output_dir: The directory to store the NIST User Library in
	:param lib_name: The name of the NIST User Library. If ``None`` this will
		be the filename of the MSP file without the extension.
	:type lib_name: str, optional
	"""

	msp_file = pathlib.Path(msp_file)
	output_dir = pathlib.Path(output_dir)

	if lib_name is None:
		lib_name = msp_file.stem

	with tempfile.TemporaryDirectory() as workdir:
		input_workdir, output_workdir = _prep_workdirs(workdir)

		# Copy input file into input
		shutil.copy(msp_file, input_workdir / "input.msp")

		# print("Launching Docker...")

		_run_docker(input_workdir, output_workdir)

		output_library: pathlib.Path = output_dir / lib_name
		shutil.copytree(output_workdir / "input", output_library)


def _run_docker(
		input_dir: PathLike,
		output_dir: PathLike,
		):
	"""
	Launch the docker container.

	:param input_dir: The path to the directory containing the input MSP file.
		The input MSP file MUST be named `input.msp`
	:type input_dir: str or pathlib.Path
	:param output_dir: The path to the directory where docker will save the created library.
		The new library will be named `input`, but can be renamed after creation.
	:type output_dir: str or pathlib.Path

	On Unix, the return value is the exit status of the process encoded in the
	format specified for :func:`python:os.wait()`. Note that POSIX does not specify
	the meaning of the return value of the C system() function, so the return value
	is system-dependent.

	On Windows, the return value is that returned by the system shell after running command.
	The shell is given by the Windows environment variable COMSPEC: it is usually cmd.exe,
	which returns the exit status of the command run; on systems using a non-native shell,
	consult your shell documentation.
	"""

	return os.system(
			"docker run --name=lib2nist-wine --rm "
			f"-v '{input_dir}:/input' "
			f"-v '{output_dir}:/output' "
			f"--env USER_UID={os.getuid()} domdfcoding/lib2nist-wine "
			"/make_nistlib.sh"
			)
