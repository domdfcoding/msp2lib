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
import sys
import tempfile
from typing import Optional, Union

# this package
from .utils import (
		_ask_existing_lib, _prep_workdirs, about, build_docker_image, download_docker_image, test_docker, version
		)

# TODO: windows version
# TODO: ability to run multiple jobs in the same container, rather than starting and stopping them


def msp2lib(
		msp_file: Union[str, pathlib.Path, os.PathLike],
		output_dir: Union[str, pathlib.Path, os.PathLike],
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
		input_dir: Union[str, pathlib.Path, os.PathLike],
		output_dir: Union[str, pathlib.Path, os.PathLike],
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
	format specified for :fun:`python:os.wait()`. Note that POSIX does not specify
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


def main():
	"""
	Entry point for running from the command line.
	"""

	# stdlib
	import argparse

	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('input_file', help='The MSP file to convert.', nargs="?")
	parser.add_argument('output_dir', help='The directory to save the output library in.', nargs="?")

	parser.add_argument(
		'--version', dest="version", action="store_true", default=False,
		help='Show the version number and exit.')  # yapf: disable

	parser.add_argument(
		'--get-docker-image', dest="get_image", action="store_true", default=False,
		help='Download the docker image now rather than at first run, then exit.')  # yapf: disable

	parser.add_argument(
		'--build-docker-image', dest="build_image", action="store_true", default=False,
		help='Build the docker image from the Dockerfile, then exit.')  # yapf: disable

	args = parser.parse_args()

	if args.version:
		version()
		sys.exit(0)

	if not test_docker():
		parser.error(
				"""Docker installation not found. Please install Docker and try again.
See https://docs.docker.com/get-docker/ for more information."""
				)

	if args.get_image:
		sys.exit(download_docker_image())

	elif args.build_image:
		sys.exit(build_docker_image())

	elif args.input_file:

		about()

		input_file = pathlib.Path(args.input_file).absolute()
		lib_name = input_file.stem

		if not input_file.is_file():
			parser.error(f"Input file not found at the given path: {input_file}")

		if args.output_dir:
			output_dir = pathlib.Path(args.output_dir).absolute()
		else:
			output_dir = pathlib.Path.cwd().absolute()

		if not output_dir.is_dir():
			output_dir.mkdir(parents=True)

		output_lib_dir = output_dir / lib_name

		if output_lib_dir.exists():
			if _ask_existing_lib(lib_name):
				shutil.rmtree(output_lib_dir)
			else:
				sys.exit(0)

		msp2lib(input_file, output_dir, lib_name)

	else:
		parser.error("Please specify an input file.")
