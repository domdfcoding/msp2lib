****************
msp2lib
****************

Convert an MSP file representing one or more Mass Spectra to a NIST MS Search user library.

Docker must be installed to use this program.


Synopsis
-----------

msp2lib [-h] [*input_file*] [*output_dir*]


Description
-------------

Convert an MSP file representing one or more Mass Spectra to a NIST MS Search user library.

**positional arguments:**

	**input_file**
		The path of the MSP file to be converted into a NIST User Library.

	**output_dir**
		The path to the directory to save the output library in. If unspecified the current working directory is used instead.


**optional arguments:**

	**-h**, **--help**
		Show usage information and exit.

	**--version**
		Show the version number and exit.

	**--get-docker-image**
		Download the docker image now rather than at first run, then exit.
		This can also be used to update the docker image.

	**--build-docker-image**
		Build the docker image from the Dockerfile, then exit.
		This can be useful when installing offline.




Examples
---------

msp2lib spectra/example.msp output/
	Convert the file ``example.msp`` in the directory ``spectra`` to a library, which is saved in the directory ``output``.


Installation
-------------

.. TODO: explain installing docker

Before installing |pkgname2|, ensure you have a working Docker installation. For more information visit https://docs.docker.com/get-docker/ for more information.

|pkgname2| can then be installed with pip:

.. parsed-literal::

	$ pip install |pkgname|


Once installed, |pkgname2| can be run by typing:

.. parsed-literal::

		$ |pkgname|

If |pkgname2| is not installed in a directory in ``$PATH``, you may need to add ``~/.local/bin/`` to your ``$PATH``.


Reporting Bugs
---------------

Please use the GitHub issue tracker to report bugs: <`https://github.com/domdfcoding/msp2lib/issues <https://github.com/domdfcoding/rsc-on-this-day/issues>`_>
