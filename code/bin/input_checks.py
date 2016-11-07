"""
input_checks.py

This module contains 2 functions:

dense_input_checks(); and
csr_input_checks().

dense_input_checks() takes 3 arguments:

matrix_size - An integer representing the number of rows and columns in the
input matrix
matrix_in - An n dimensional numpy array, with each array containing n values
(an n x n matrix).
vector_b - A 1 dimensional numpy array that represents the solution vector b

dense_input_checks() aims to conduct basic tests on the structure of the
dense input file provided by the user. These include:

Check that matrix_size is an integer value
Check that matrix_size matches the size of matrix_in provided
Check that matrix_in is a square matrix
Check that the columns in matrix_in matches the number of rows in vector_b

If any of these errors are identified, they are appended to a list and
returned to be shown to the user at a later time. Rather than show errors one
at a time to the user, as many as possible are grouped and shown at once,
to speed up the correction process for the user if errors are identified.

dense_input_checks() takes 4 arguments:

val - A 1 dimensional numpy array containing the input matrix (A) values in
CRS format.
col - A 1 dimensional numpy array containing the column references for the
input matrix (A) entries in val.
rowStart - A 1 dimensional numpy array containing the reference indices for
the beginning of each new row of the the input matrix (A)
b - A 1 dimensional numpy array that represents the solution vector b

csr_input_checks() aims to conduct basic tests on the structure of the
dense input file provided by the user. These include:

Check that the col and val vectors have the same number of entries
Check that the dimension of the matrix (rowStart - 1) is the same as vector_b
Check that col and rowStart vectors only contain integers
Check that the first entry of rowStart is 0
Check that the last entry of rowStart is equal to the size of val + 1
Check that the matrix is square, such that the number of rows (rowStart - 1)
is equal to the number of columns (maximum entry in col)

If any of these errors are identified, they are appended to a list and
returned to be shown to the user at a later time.

Requirements: math, numpy

"""

import math
import numpy as np


def dense_input_checks(matrix_size, matrix_in, vector_b):

    errors = []

    # Check that matrix size is an integer
    if matrix_size % 1 != 0:
        errors.append("Defined matrix size is not an integer")

    # Check that defined matrix size matches actual matrix size
    if matrix_size != np.size(matrix_in) / matrix_size:
        errors.append('Defined matrix size and actual matrix size do '
                      'not match.')

    # Check that matrix is square
    print(np.size(matrix_in))
    if np.size(matrix_in) / matrix_size != matrix_size:
        errors.append("Matrix is not square")

    # # Check matrix size and vector size are compatible
    if np.size(matrix_in) / matrix_size != np.size(vector_b):
        errors.append("Matrix length and vector length are not compatible")

    return errors


def csr_input_checks(val, col, rowStart, b):

    errors = []

    if val.size != col.size:
        errors.append("Value and column vectors do not have the same number "
                      "of entries")

    if rowStart.size - 1 != b.size:
        errors.append("Number of columns in matrix is not the same as the "
                      "number of rows in Vector b")

    col_int_err = 0
    for i in col:
        if type(i) != int:
            col_int_err += 1
    if col_int_err > 0:
        errors.append("Column vector contains non-integer entries")

    rs_int_err = 0
    for i in rowStart:
        if type(i) != int:
            rs_int_err += 1
    if rs_int_err > 0:
        errors.append("RowStart vector contains non-integer entries")

    if rowStart[0] != 0:
        errors.append("First entry of RowStart vector is not 0")

    if rowStart[-1] != val.size:
        errors.append("Last entry of RowStart vector is equivalent to the "
                      "nth entry of val + 1")

    if (rowStart.size - 1) != math.sqrt((max(col) + 1) ** 2):
        errors.append("Uneven number of rows and columns")

    return errors