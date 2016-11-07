"""
input_checks.py

This module contains 1 function, csr_input_checks(), which takes 4 arguments:

  - val - A 1 dimensional numpy array containing the input matrix (A) values in
CRS format.
  - col - A 1 dimensional numpy array containing the column references for the
input matrix (A) entries in val.
  - rowStart - A 1 dimensional numpy array containing the reference indices for
the beginning of each new row of the the input matrix (A)
  - b - A 1 dimensional numpy array that represents the solution vector b

csr_input_checks() aims to conduct basic tests on the structure of the
dense input file provided by the user. These include:

  - Check that the col and val vectors have the same number of entries
  - Check that the dimension of the matrix (rowStart - 1) is the same as vector_b
  - Check that col and rowStart vectors only contain integers
  - Check that the first entry of rowStart is 0
  - Check that the last entry of rowStart is equal to the size of val + 1
  - Check that the matrix is square, such that the number of rows (rowStart - 1)
is equal to the number of columns (maximum entry in col)

If any of these errors are identified, they are appended to a list and
returned to be shown to the user at a later time. Rather than show errors one
at a time to the user, as many as possible are grouped and shown at once,
to speed up the correction process for the user if errors are identified.

Requirements: math, numpy

"""

import math
import numpy as np

def csr_input_checks(val, col, rowStart, b):

    # Initialize emtpy error list
    errors = []

    # Check if the number of entries in val is the same as in col
    if val.size != col.size:
        errors.append("Value and column vectors do not have the same number "
                      "of entries")

    # Check if the number of entries in rowStart is the one more than in b
    if rowStart.size - 1 != b.size:
        errors.append("Number of columns in matrix is not the same as the "
                      "number of rows in Vector b")

    # Count number of non-integer entries in col
    col_int_err = 0
    for i in col:
        if i % 1 != 0:
            col_int_err += 1
    if col_int_err > 0:
        errors.append("Column vector contains non-integer entries")

    # Count number of non-integer entries in rowStart
    rs_int_err = 0
    for i in rowStart:
        if i % 1 != 0:
            rs_int_err += 1
    if rs_int_err > 0:
        errors.append("RowStart vector contains non-integer entries")

    # Check if first entry of rowStart is 0
    if rowStart[0] != 0:
        errors.append("First entry of RowStart vector is not 0")

    # Check if the last entry of rowStart is the same as the size of val
    if rowStart[-1] != val.size:
        errors.append("Last entry of RowStart vector is equivalent to the "
                      "nth entry of val + 1")

    # Check if the number of rows (rowStart - 1) is the same as the number of
    # columns (maximum value of col)
    if (rowStart.size - 1) != math.sqrt((max(col) + 1) ** 2):
        errors.append("Uneven number of rows and columns")

    # Return the list of accumulated errors
    return errors