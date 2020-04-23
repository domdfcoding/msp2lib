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


This is a docker container to allow PyMassSpec NIST Search to function on Linux via a Flask REST API. It is based on the [pywine](https://hub.docker.com/r/tobix/pywine) docker image by [webcomics](https://github.com/webcomics).

This container isn't designed to be run directly; rather it is invoked automatically from [PyMassSpec NIST Search](https://github.com/domdfcoding/pynist) when running on platforms other than Windows. 