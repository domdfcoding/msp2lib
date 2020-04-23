****************
msp2lib
****************

Displays Royal Society of Chemistry "On This Day" facts in your terminal.

Synopsis
-----------

msp2lib [*OPTION*]... [*month*] [*day*]


Description
-------------

Displays Royal Society of Chemistry "On This Day In Chemistry" facts in your
terminal.

**positional arguments:**

	**month**
		The name or number of the month of the fact to display.

	**day**
		The day number of the fact to display.

**optional arguments:**

	**-h**, **--help**
		Show usage information and exit.

	**-w**, **--width**\=\*WIDTH*
		The number of characters per line of the output.
		Default 80. Set to -1 to disable wrapping.

	**--clear-cache**
		Clears any cached data and exits.

If requesting a specific date both the month and day must be given.


.. TODO: --version  output version information and exit


Examples
---------

msp2lib
	Display the "On This Day In Chemistry" fact for today.

msp2lib Apr 1
	Display the "On This Day In Chemistry" fact for April 1st.

msp2lib 12 25
	Display the "On This Day In Chemistry" fact for 25 December.

msp2lib --clear-cache
	Clear any cached data.

msp2lib October 13 --width 80
	Display the "On This Day In Chemistry" fact for October 13th, with at most 80 characters per line.


Installation
-------------

|pkgname2| can be installed with pip:


.. parsed-literal::

        $ pip install |pkgname|


Once installed, |pkgname2| can be run by typing:

.. parsed-literal::

        $ |pkgname|

If |pkgname2| is not installed in a directory in ``$PATH``, you may need to add ``~/.local/bin/`` to your ``$PATH``.

Adding to ``~/bashrc``
-----------------------

|pkgname2| can be run every time you open a terminal by adding |pkgname2| to your ``~/bashrc`` file. For example:

.. parsed-literal::

    $ echo "|pkgname|" >> ~/.bashrc

Reporting Bugs
---------------

Please use the GitHub issue tracker to report bugs: <`https://github.com/domdfcoding/msp2lib/issues <https://github.com/domdfcoding/rsc-on-this-day/issues>`_>

See Also
-----------
fortune(6)

