#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wrapper_script.py
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
import distutils.spawn
import os
import pathlib
import shutil
import sys
import tempfile


# The first time this script is run it will download the latest
# version of the docker image automatically.

# This can also be done manually, such as to upgrade to the latest version,
# with the following bash command:
#
#	$ docker pull domdfcoding/pywine-pyms-nist
#

__author__ = "Dominic Davis-Foster"
__copyright__ = "2020 Dominic Davis-Foster"

__license__ = "LGPLv3"
__version__ = "0.0.0"
__email__ = "dominic@davis-foster.co.uk"

# TODo: manpage
# TODO: windows version


def test_docker():
	return bool(distutils.spawn.find_executable("docker"))


def main():
	import argparse
	
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('input_file', help='The MSP file to convert.', nargs="?")
	parser.add_argument('output_dir', help='The directory to save the output library in.', nargs="?")
	
	args = parser.parse_args()

	if not test_docker():
		parser.error("""Docker installation not found. Please install Docker and try again.
See https://docs.docker.com/get-docker/ for more information.""")

	if args.input_file:
		# input_file = "/home/domdf/Downloads/lib2nist/MoNA.msp"
		input_file = pathlib.Path(args.input_file).absolute()
		
		if not input_file.is_file():
			parser.error(f"Input file not found at the given path: {input_file}")
		
		lib_name = input_file.stem
		
		if args.output_dir:
			# output_dir = "/home/domdf/Downloads/lib2nist/"
			output_dir = pathlib.Path(args.output_dir).absolute()
			
		else:
			output_dir = pathlib.Path.cwd().absolute()
		
		if not output_dir.is_dir():
			output_dir.mkdir(parents=True)
		
		output_lib_dir = output_dir / lib_name
	
		if output_lib_dir.exists():
			print(f"\nA library already exists in the output location with the name '{lib_name}'.")
			if not input("Do you want to remove the existing library? [y/N] ").startswith("y"):
				sys.exit(0)
			else:
				shutil.rmtree(output_lib_dir)

		msp2lib(input_file, output_dir, lib_name)
		
	else:
		parser.error("Please specify an input file.")


def msp2lib(msp_file, output_dir, lib_name):
	with tempfile.TemporaryDirectory() as workdir:
		input_workdir, output_workdir = prep_workdirs(workdir)
		
		# Copy input file into input
		shutil.copy(msp_file, input_workdir / "input.msp")
		
		print("Launching Docker...")
		
		run_docker(input_workdir, output_workdir)
		
		shutil.copytree(output_workdir / "input", output_dir / lib_name)


def prep_workdirs(workdir):
	workdir = pathlib.Path(workdir)
	
	input_workdir = workdir / "input"
	input_workdir.mkdir(parents=True)
	
	output_workdir = workdir / "output"
	output_workdir.mkdir(parents=True)
	
	return input_workdir, output_workdir


def run_docker(input_dir, output_dir):
	return os.system(
			"docker run --name=lib2nist-wine --rm "
			f"-v '{input_dir}:/input' "
			f"-v '{output_dir}:/output' "
			f"--env USER_UID={os.getuid()} domdfcoding/lib2nist-wine "
			"/make_nistlib.sh")


if __name__ == '__main__':
	main()
