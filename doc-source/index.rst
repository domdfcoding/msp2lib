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
	  - |codefactor| |actions_flake8| |actions_mypy| |pre_commit_ci|
	* - Docker
	  - |docker_build| |docker_automated| |docker_size|
	* - Other
	  - |license| |language| |requires|

.. |docs| rtfd-shield::
	:project: msp2lib
	:alt: Documentation Build Status

.. |docs_check| actions-shield::
	:workflow: Docs Check
	:alt: Docs Check Status

.. |actions_linux| actions-shield::
	:workflow: Linux
	:alt: Linux Test Status

.. |actions_flake8| actions-shield::
	:workflow: Flake8
	:alt: Flake8 Status

.. |actions_mypy| actions-shield::
	:workflow: mypy
	:alt: mypy status

.. |requires| requires-io-shield::
	:alt: Requirements Status

.. |codefactor| codefactor-shield::
	:alt: CodeFactor Grade

.. |pypi-version| pypi-shield::
	:project: msp2lib
	:version:
	:alt: PyPI - Package Version

.. |supported-versions| pypi-shield::
	:project: msp2lib
	:py-versions:
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| pypi-shield::
	:project: msp2lib
	:implementations:
	:alt: PyPI - Supported Implementations

.. |wheel| pypi-shield::
	:project: msp2lib
	:wheel:
	:alt: PyPI - Wheel

.. |license| github-shield::
	:license:
	:alt: License

.. |language| github-shield::
	:top-language:
	:alt: GitHub top language

.. |commits-since| github-shield::
	:commits-since: v0.1.3
	:alt: GitHub commits since tagged version

.. |commits-latest| github-shield::
	:last-commit:
	:alt: GitHub last commit

.. |maintained| maintained-shield:: 2021
	:alt: Maintenance

.. |pypi-downloads| pypi-shield::
	:project: msp2lib
	:downloads: month
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

.. |pre_commit_ci| pre-commit-ci-shield::
	:alt: pre-commit.ci status

.. end shields

Installation
----------------

.. TODO: explain installing docker

Before installing ``msp2lib``, ensure you have a working Docker installation.
For more information visit https://docs.docker.com/get-docker/ for more information.


.. start installation

.. installation:: msp2lib
	:pypi:
	:github:

.. end installation

.. toctree::
	:hidden:

	self

.. toctree::
	:maxdepth: 3
	:caption: Documentation

	docs
	usage
	contributing
	Source


.. start links

View the :ref:`Function Index <genindex>` or browse the `Source Code <_modules/index.html>`__.

`Browse the GitHub Repository <https://github.com/domdfcoding/msp2lib>`__

.. end links
