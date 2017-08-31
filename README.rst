.. image:: pygredients_logo.png

Pygredients
===========

Pygredients allows to follow data on its way through variables, functions and assignments of a python application.

**This project is pre-alpha. So nothing really works right now and the project itself is under heavy development.**

Example
-------
File **main.py**

.. code-block:: python

    import sys
    import my_module

    if "main" in __name__:
        a = sys.argv[1]
        b = sys.argv[2]
        c = my_module.calculate(a,b)
        print(c)

File **my_module.py**

.. code-block:: python

    def calculate(a, b):
        b = b + 2
        c = a+b
        print(b)
        return c

A possible answer for tracing **calculate.b** could look like:

.. code-block:: text

    sys.argv[2]
    ->main.b
    ->**my_module.calculate.b**
    ->my_module.calculate.b+2
    ->print(b) && ->my_module.calculate.c=a+b
                  ->main.c
                  ->print(c)