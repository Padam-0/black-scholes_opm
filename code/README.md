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

----------------------
Operating Instructions
----------------------

If you are happy to use the default files, run either sor.py or bsm.py and
follow the instructions given.

If you would like to use your own input file: add your file to the directory,
run sor.py or bsm.py and give this filename as your input file when prompted.

You can also define your own output filename if you so desire.

The default input and output files are nas_Sor.in and nas_Sor.out, these are
both located in the sample_inputs directory.

File names can also be specified from the command line, by calling:
python sor.py input_filename.in output_filename.in

Input Format
------------

Input files can take 1 of three file formats:

- Dense;
- Compressed Sparse Row; and
- Matrix Market .mtx

Dense matrix files contain n + 2 lines, where n is the dimension of the 
matrix. The first is a single integer n, the number of rows and columns 
in the matrix. The next n lines contain n floats, the entries of the 
matrix. The final line contains n floats, the entries of the solution
vector b.

Compressed Sparse Row files contain 4 lines. The first contains t floats,
the non-zero entries of the matrix. The second line contains t integers, 
the column indices of the entries in the first line. The third line contains
n + 1 integers, the indices of the first entry of each line of the matrix.
The final line contains n floats, the entries of the solution vector b.


All Dense and CSR files must be space or tab delimited. See sample_inputs
for details.

---------------
List of Authors
---------------

Peter Adam - peter.adam@ucdconnect.ie,
Kieron Ellis - kieron.ellis@ucdconnect.ie,
Andy McSweeney - andy.mcsweeney@ucdconnect.ie.