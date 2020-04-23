********************
msp2lib
********************

**The NIST Library Conversion program running in Wine and Docker**


.. image:: https://img.shields.io/docker/cloud/build/domdfcoding/msp2lib
    :alt: Docker Cloud Build Status
    :target: https://hub.docker.com/r/domdfcoding/msp2lib
.. image:: https://img.shields.io/docker/cloud/automated/domdfcoding/msp2lib
    :alt: Docker Cloud Automated build
    :target: https://hub.docker.com/r/domdfcoding/msp2lib/builds
.. image:: https://img.shields.io/github/license/domdfcoding/msp2lib
    :alt: GitHub
    :target: https://opensource.org/licenses/MIT
.. image:: https://travis-ci.com/domdfcoding/msp2lib.svg?branch=master
    :target: https://travis-ci.com/domdfcoding/msp2lib
    :alt: Build Status
.. image:: https://readthedocs.org/projects/msp2lib/badge/?version=latest
    :target: https://msp2lib.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. image:: https://img.shields.io/pypi/v/msp2lib.svg
    :target: https://pypi.org/project/msp2lib/
    :alt: PyPI
.. image:: https://img.shields.io/pypi/pyversions/msp2lib.svg
    :target: https://pypi.org/project/msp2lib/
    :alt: PyPI - Python Version
.. image:: https://coveralls.io/repos/github/domdfcoding/msp2lib/badge.svg?branch=master
    :target: https://coveralls.io/github/domdfcoding/msp2lib?branch=master
    :alt: Coverage
.. image:: https://img.shields.io/badge/License-LGPL%20v3-blue.svg
    :alt: PyPI - License
    :target: https://github.com/domdfcoding/msp2lib/blob/master/LICENSE


This is a Python script to facilitate conversion from MSP files to NIST MS Search user libraries.

Usage
=========

.. code-block::

    msp2lib.py [input_file] [output_dir]

where ``input_file`` is the MSP file to be converted and ``output_dir`` is the directory to
save the output library in. If ``output_dir`` is unspecified the current working directory
is used instead.


