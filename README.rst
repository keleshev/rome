A practical Roman numerals implementation
======================================================================

   New in version 0.0.2:

   * Fix bug that did not allow numbers greater than MCMXCIX

.. code::

    pip install rome==0.0.2

**rome** is the first industrial-strength Roman numerals
implementation for Python. It features Roman-to-Arabic and
Arabic-to-Roman numerals convertion, as well as normalization of
denormalized Roman numerals using unified object-oriented interface.
It is developed using test-driven development, and features an
extensive test-suite.

.. code:: python

    >>> from rome import Roman

    >>> Roman('IX')
    Roman('IX')

    >>> str(Roman('IX'))
    'IX'

    >>> int(Roman('IX'))  # to Arabic numerals
    9

    >>> Roman('IX') == 9
    True

    >>> Roman('IX') + Roman('XI') == Roman('XX')
    True

    >>> Roman('XXI') - 13 == 8
    True

    >>> Roman(4)  # from Arabic numerals
    Roman('IV')

    >>> Roman(1903)
    Roman('MCMIII')

    >>> Roman('IIII')  # bring to normalized form
    Roman('IV')

    >>> Roman('MDCCCCLXXXXVIIII')
    Roman('MCMXCIX')

    >>> int(Roman('MCMXCIX'))
    1999

    >>> int(Roman('M cM xC iX'))  # spaces and mixed case are
    ...                           # allowed for readability
    1999
