#!/usr/bin/env python3
#
#  __main__.py
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

# stdlib
from typing import TYPE_CHECKING

# 3rd party
import click
from click import version_option
from consolekit import click_command

# this package
from msp2lib import __version__

if TYPE_CHECKING:
	# 3rd party
	from click import Context, Parameter
	from domdf_python_tools.typing import PathLike

__all__ = ["build_docker_image_callback", "get_docker_image_callback", "main", "require_docker"]


def require_docker():
	# stdlib
	from textwrap import dedent

	# this package
	from msp2lib.utils import test_docker

	if not test_docker():
		raise click.UsageError(
				dedent(
						"""\
			Docker installation not found. Please install Docker and try again.
			See https://docs.docker.com/get-docker/ for more information.
			"""
						)
				)


def get_docker_image_callback(ctx: "Context", param: "Parameter", value: str):
	if not value or ctx.resilient_parsing:
		return

	# stdlib
	import sys

	# this package
	from msp2lib.utils import download_docker_image

	require_docker()

	sys.exit(download_docker_image())


def build_docker_image_callback(ctx: "Context", param: "Parameter", value: str):
	if not value or ctx.resilient_parsing:
		return

	# stdlib
	import sys

	# this package
	from msp2lib.utils import build_docker_image

	require_docker()

	sys.exit(build_docker_image())


@click.argument("input_file")
@click.argument("output_dir", type=click.STRING, default='.')
@click.option(
		"--get-docker-image",
		is_eager=True,
		is_flag=True,
		default=False,
		expose_value=False,
		help="Download the docker image now rather than at first run, then exit.",
		callback=get_docker_image_callback,
		)
@click.option(
		"--build-docker-image",
		is_eager=True,
		is_flag=True,
		default=False,
		expose_value=False,
		help="Build the docker image from the Dockerfile, then exit.",
		callback=build_docker_image_callback,
		)
@version_option(__version__)
@click_command()
def main(input_file: "PathLike", output_dir: "PathLike"):
	"""
	Convert INPUT_FILE to a NIST library and save the output in OUTPUT_DIR.

	INPUT_FILE is a .msp file.
	"""

	# stdlib
	import pathlib
	import shutil
	import sys

	# 3rd party
	from domdf_python_tools.paths import PathPlus

	# this package
	from msp2lib.core import msp2lib
	from msp2lib.utils import _ask_existing_lib, about

	about()

	input_file = pathlib.Path(input_file).absolute()
	lib_name = input_file.stem

	if not input_file.is_file():
		raise FileNotFoundError(f"Input file not found at the given path: {input_file}")

	output_dir = PathPlus(output_dir).absolute()

	if not output_dir.is_dir():
		output_dir.mkdir(parents=True)

	output_lib_dir = output_dir / lib_name

	if output_lib_dir.exists():
		if _ask_existing_lib(lib_name):
			shutil.rmtree(output_lib_dir)
		else:
			sys.exit(1)

	msp2lib(input_file, output_dir, lib_name)

	sys.exit(0)


if __name__ == "__main__":
	main()
