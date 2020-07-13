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
	  - |travis| |codefactor|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - Docker
	  - |docker_build| |docker_automated| |docker_size|
	* - Other
	  - |license| |language| |requires| |pre_commit|

.. |docs| image:: https://img.shields.io/readthedocs/msp2lib/latest?logo=read-the-docs
	:target: https://msp2lib.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status

.. |docs_check| image:: https://github.com/domdfcoding/msp2lib/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/msp2lib/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |travis| image:: https://img.shields.io/travis/com/domdfcoding/msp2lib/master?logo=travis
	:target: https://travis-ci.com/domdfcoding/msp2lib
	:alt: Travis Build Status

.. |requires| image:: https://requires.io/github/domdfcoding/msp2lib/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/msp2lib/requirements/?branch=master
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

.. |maintained| image:: https://img.shields.io/maintenance/yes/2020
	:alt: Maintenance

.. |docker_build| image:: https://img.shields.io/docker/cloud/build/domdfcoding/lib2nist-wine?label=build&logo=docker
	:target: https://hub.docker.com/r/domdfcoding/lib2nist-wine
	:alt: Docker Hub Build Status

.. |docker_automated| image:: https://img.shields.io/docker/cloud/automated/domdfcoding/lib2nist-wine?label=build&logo=docker
	:target: https://hub.docker.com/r/domdfcoding/lib2nist-wine/builds
	:alt: Docker Hub Automated build

.. |docker_size| image:: https://img.shields.io/docker/image-size/domdfcoding/lib2nist-wine?label=image%20size&logo=docker
	:target: https://hub.docker.com/r/domdfcoding/lib2nist-wine
	:alt: Docker Image Size

.. |pre_commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
	:target: https://github.com/pre-commit/pre-commit
	:alt: pre-commit

.. end shields

Installation
----------------

.. start installation

.. tabs::

	.. tab:: from PyPI

		.. prompt:: bash

			python3 -m pip install msp2lib --user


	.. tab:: from GitHub

		.. prompt:: bash

			python3 -m pip install git+https://github.com/domdfcoding/msp2lib@master --user

.. end installation

.. toctree::
	:hidden:

	self

.. toctree::
	:maxdepth: 3
	:caption: Documentation

	docs
	Source
	Building
	Manpage<manpage>


.. start links

View the :ref:`Function Index <genindex>` or browse the `Source Code <_modules/index.html>`__.

`Browse the GitHub Repository <https://github.com/domdfcoding/msp2lib>`__

.. end links