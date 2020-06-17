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
	  - |travis| |actions_windows| |actions_macos|
	    |codefactor|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - Other
	  - |license| |language| |requires|

.. |docs| image:: https://img.shields.io/readthedocs/msp2lib/latest?logo=read-the-docs
	:target: https://msp2lib.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status
	
.. |docs| image:: [Docs Check](https://github.com/domdfcoding/msp2lib/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/msp2lib/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |travis| image:: https://img.shields.io/travis/com/domdfcoding/msp2lib/master?logo=travis
	:target: https://travis-ci.com/domdfcoding/msp2lib
	:alt: Travis Build Status

.. |actions_windows| image:: https://github.com/domdfcoding/msp2lib/workflows/Windows%20Tests/badge.svg
	:target: https://github.com/domdfcoding/msp2lib/actions?query=workflow%3A%22Windows+Tests%22
	:alt: Windows Tests Status
	
.. |actions_macos| image:: https://github.com/domdfcoding/msp2lib/workflows/macOS%20Tests/badge.svg
	:target: https://github.com/domdfcoding/msp2lib/actions?query=workflow%3A%22macOS+Tests%22
	:alt: macOS Tests Status

.. |requires| image:: https://requires.io/github/domdfcoding/msp2lib/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/msp2lib/requirements/?branch=master
	:alt: Requirements Status

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/msp2lib?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/msp2lib
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/msp2lib
	:target: https://pypi.org/project/msp2lib/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/msp2lib
	:target: https://pypi.org/project/msp2lib/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/msp2lib
	:target: https://pypi.org/project/msp2lib/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/msp2lib
	:target: https://pypi.org/project/msp2lib/
	:alt: PyPI - Wheel

.. |license| image:: https://img.shields.io/github/license/domdfcoding/msp2lib
	:alt: License
	:target: https://github.com/domdfcoding/msp2lib/blob/master/LICENSE

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

.. end shields

Installation
----------------

.. start installation

.. tabs::

	.. tab:: from PyPI

		.. prompt:: bash

			pip install msp2lib


	.. tab:: from GitHub

		.. prompt:: bash

			pip install git+https://github.com/domdfcoding/msp2lib@master

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