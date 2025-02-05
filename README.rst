=========
msp2lib
=========

**The NIST Library Conversion program running in Wine and Docker**

This is a Python script to facilitate conversion from MSP files to NIST MS Search user libraries.


.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |actions_linux|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Docker
	  - |docker_build| |docker_automated| |docker_size|
	* - Other
	  - |license| |language| |requires|

.. |docs| image:: https://img.shields.io/readthedocs/msp2lib/latest?logo=read-the-docs
	:target: https://msp2lib.readthedocs.io/en/latest
	:alt: Documentation Build Status

.. |docs_check| image:: https://github.com/domdfcoding/msp2lib/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/msp2lib/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |actions_linux| image:: https://github.com/domdfcoding/msp2lib/workflows/Linux/badge.svg
	:target: https://github.com/domdfcoding/msp2lib/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_flake8| image:: https://github.com/domdfcoding/msp2lib/workflows/Flake8/badge.svg
	:target: https://github.com/domdfcoding/msp2lib/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/domdfcoding/msp2lib/workflows/mypy/badge.svg
	:target: https://github.com/domdfcoding/msp2lib/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://dependency-dash.repo-helper.uk/github/domdfcoding/msp2lib/badge.svg
	:target: https://dependency-dash.repo-helper.uk/github/domdfcoding/msp2lib/
	:alt: Requirements Status

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/msp2lib?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/msp2lib
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/msp2lib
	:target: https://pypi.org/project/msp2lib/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/msp2lib?logo=python&logoColor=white
	:target: https://pypi.org/project/msp2lib/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/msp2lib
	:target: https://pypi.org/project/msp2lib/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/msp2lib
	:target: https://pypi.org/project/msp2lib/
	:alt: PyPI - Wheel

.. |license| image:: https://img.shields.io/github/license/domdfcoding/msp2lib
	:target: https://github.com/domdfcoding/msp2lib/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/msp2lib
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/msp2lib/v0.1.3
	:target: https://github.com/domdfcoding/msp2lib/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/msp2lib
	:target: https://github.com/domdfcoding/msp2lib/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2025
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/msp2lib
	:target: https://pypi.org/project/msp2lib/
	:alt: PyPI - Downloads

.. |docker_build| image:: https://img.shields.io/docker/cloud/build/domdfcoding/lib2nist-wine?label=build&logo=docker
	:target: https://hub.docker.com/r/domdfcoding/lib2nist-wine
	:alt: Docker Hub Build Status

.. |docker_automated| image:: https://img.shields.io/docker/cloud/automated/domdfcoding/lib2nist-wine?label=build&logo=docker
	:target: https://hub.docker.com/r/domdfcoding/lib2nist-wine/builds
	:alt: Docker Hub Automated build

.. |docker_size| image:: https://img.shields.io/docker/image-size/domdfcoding/lib2nist-wine?label=image%20size&logo=docker
	:target: https://hub.docker.com/r/domdfcoding/lib2nist-wine
	:alt: Docker Image Size

.. end shields


Installation
===============

.. start installation

``msp2lib`` can be installed from PyPI.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install msp2lib

.. end installation


Usage
=========

.. code-block::

	msp2lib.py [input_file] [output_dir]

where ``input_file`` is the MSP file to be converted and ``output_dir`` is the directory to
save the output library in. If ``output_dir`` is unspecified the current working directory
is used instead.

Docker must be installed to use this program.

The first time this script is run it will download the latest
version of the docker image automatically. This can also be done manually,
such as to upgrade to the latest version, by running with the ``--get-docker-image`` flag.

For more usage information see the manpage or run with the ``--help`` flag.
