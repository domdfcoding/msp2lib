#!/usr/bin/env python3
#
#  utils.py
"""
utilities for ``msp2lib``.
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
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

# stdlib
import distutils.spawn
import os
import pathlib
import re
import subprocess
from typing import Sequence, Tuple, Union

# this package
from msp2lib import __copyright__, __version__

__all__ = ["about", "build_docker_image", "download_docker_image", "subprocess_with_log", "test_docker", "version"]


def test_docker() -> bool:
	"""
	Returns whether Docker is installed on the system.

	:return: :py:obj:`True` if Docker is installed, :py:obj:`False` otherwise.
	"""

	return bool(distutils.spawn.find_executable("docker"))


def version() -> str:
	"""
	Prints the version number of ``msp2lib``.
	"""

	print(__version__)
	return __version__


def about() -> str:
	"""
	Prints information about ``msp2lib``.
	"""

	about_text = f"""msp2lib Version {__version__} Copyright (C) {__copyright__}
This program comes with ABSOLUTELY NO WARRANTY, to the extent permitted by law.
This is free software: you are free to change and redistribute it under certain conditions.
See https://www.gnu.org/licenses/lgpl-3.0.en.html for more information."""

	print(about_text)
	return about_text


def _prep_workdirs(workdir: Union[str, pathlib.Path, os.PathLike]) -> Tuple[pathlib.Path, pathlib.Path]:
	"""
	Prepare input and output directories in the given directory.
	These will be then mounted in the docker container.

	:param workdir:
	:return: The newly created directories
	"""

	workdir = pathlib.Path(workdir)

	input_workdir = workdir / "input"
	input_workdir.mkdir(parents=True)

	output_workdir = workdir / "output"
	output_workdir.mkdir(parents=True)

	return input_workdir, output_workdir


def _ask_existing_lib(lib_name: str) -> bool:
	"""
	Asks the user whether they wish to remove an existing library that exists with the same name.

	:param lib_name: The name of the library that already exists

	:return: :py:obj:`True` if the user responded with ``y`` to indicate they wish to remove
		the existing library, :py:obj:`False` otherwise.
	"""

	print(f"\nA library already exists in the output location with the name '{lib_name}'.")
	return input("Do you want to remove the existing library? [y/N] ").lower().startswith('y')


def download_docker_image() -> int:
	"""
	Pull the lib2nist-wine docker image from dockerhub.

	:return: The return code of the ``docker pull`` command
	:rtype: int
	"""

	process = subprocess_with_log("docker pull domdfcoding/lib2nist-wine")
	return int(process.returncode)


def build_docker_image() -> int:
	"""
	Build the lib2nist-wine docker image from the Dockerfile.

	:return: The return code of the ``docker build`` command
	:rtype: int
	"""

	pkg_dir = pathlib.Path(__file__).parent.absolute()
	process = subprocess_with_log(f"docker build --no-cache -t domdfcoding/lib2nist-wine {pkg_dir}/.")
	return int(process.returncode)


_newline_re = re.compile(r"\n$")


def subprocess_with_log(command: Union[str, Sequence[str]]) -> subprocess.Popen:
	"""
	The ``command`` with :class:`python:subprocess.Popen`, printing any stdout from the command.

	:param command: The command to run

	:return:
	"""

	process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

	if process is not None:
		for line in iter(process.stdout.readline, b''):  # type: ignore
			print(_newline_re.sub('', line.decode("UTF-8")))

	return process
