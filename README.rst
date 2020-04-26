********************
msp2lib
********************

**The NIST Library Conversion program running in Wine and Docker**

+----------------------------------------------------------------------------------------------------------+
|.. image:: https://travis-ci.com/domdfcoding/msp2lib.svg?branch=master                                    |
|    :target: https://travis-ci.com/domdfcoding/msp2lib                                                    |
|    :alt: Build Status                                                                                    |
|.. image:: https://readthedocs.org/projects/msp2lib/badge/?version=latest                                 |
|    :target: https://msp2lib.readthedocs.io/en/latest/?badge=latest                                       |
|    :alt: Documentation Status                                                                            |
|.. image:: https://img.shields.io/pypi/v/msp2lib.svg                                                      |
|    :target: https://pypi.org/project/msp2lib/                                                            |
|    :alt: PyPI                                                                                            |
|.. image:: https://img.shields.io/pypi/pyversions/msp2lib.svg                                             |
|    :target: https://pypi.org/project/msp2lib/                                                            |
|    :alt: PyPI - Python Version                                                                           |
|.. image:: https://img.shields.io/github/license/domdfcoding/msp2lib                                      |
|    :alt: License                                                                                         |
|    :target: https://github.com/domdfcoding/msp2lib/blob/master/LICENSE                                   |
+----------------------------------------------------------------------------------------------------------+
|.. image:: https://img.shields.io/docker/cloud/build/domdfcoding/lib2nist-wine                            |
|    :alt: Docker Cloud Build Status                                                                       |
|    :target: https://hub.docker.com/r/domdfcoding/lib2nist-wine                                           |
|.. image:: https://img.shields.io/docker/cloud/automated/domdfcoding/lib2nist-wine                        |
|    :alt: Docker Cloud Automated build                                                                    |
|    :target: https://hub.docker.com/r/domdfcoding/lib2nist-wine/builds                                    |
|.. image:: https://img.shields.io/docker/image-size/domdfcoding/lib2nist-wine?label=docker%20image%20size |
|    :alt: Docker Image Size (latest by date)                                                              |
|    :target: https://hub.docker.com/r/domdfcoding/lib2nist-wine                                           |
+----------------------------------------------------------------------------------------------------------+


.. .. image:: https://coveralls.io/repos/github/domdfcoding/msp2lib/badge.svg?branch=master
    :target: https://coveralls.io/github/domdfcoding/msp2lib?branch=master
    :alt: Coverage

This is a Python script to facilitate conversion from MSP files to NIST MS Search user libraries.

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
