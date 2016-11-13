##
--------
Synopsis
--------

code
----
The directory code contains two main programs sor.py and bsm.py. It also
contains 4 sub-directories: bsm_modules, sample_inputs, sor_modules, and tests.

sor.py
------
This is a program to implement the Sparse-SOR (Successive Over Relaxation)
algorithm for solving a system of n linear equations in n unknowns, Ax = b (A
being a matrix of size n*n with real values. x and b being vectors of size n*1
with real values).

The program reads data from an input file and conducts a series of error checks.
If the data passes these tests, the program will solve Ax = b using the
Sparse-SOR algorithm and CSR (Compressed Sparse Row) format.

It will then write the computed solution vector x, together with the
reason for stopping and other information, to an output text file.

bsm.py
------
This program solves the The Black-Scholes-Merton option pricing problem using
the sor.py program to solve a system of linear equations.

bsm_modules
-----------
This sub-directory contains all the modules only used by the bsm.py main
program.

sample_inputs
-------------
This sub-directory contains all of the sample inputs used.

sor_modules
-----------
This sub-directory contains all the modules only used by the sor.py main
program.

tests
-----
This sub-directory contains all of the tests and error checks used.

---------------
List of Authors
---------------

Peter Adam - peter.adam@ucdconnect.ie,
Kieron Ellis - kieron.ellis@ucdconnect.ie,
Andy McSweeney - andy.mcsweeney@ucdconnect.ie.