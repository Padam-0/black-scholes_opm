"""
convert_to_csr.py

This module contains 1 function, con_to_csr(), which takes 3 arguments. These
are:

  - vector - An 1 dimensional numpy array containing values corresponding to
the input matrix A.
  - matrix_size - An integer representing the number of rows / columns n,
in the n x n input matrix A.
  - row_start - An integer representing the current val index of the
beginning of the current row.

con_to_csr() is run on each row of the input matrix A, represented as the
input vector. For this row, the non-zero entries are comprehended to val,
and returned. For each entry in the vector, the column index is added to the
col list, which is also returned.

con_to_csr() returns the the val and col lists for the given row, as well as
the index of the last value in the list.

Requirements: numpy

"""

import numpy as np

def con_to_csr(vector, matrix_size, row_start):
    # Convert an numpy array to Compressed Sparse Row Structure

    # Initialize empty val and col lists
    val = []
    col = []

    #Set position counter and number of 0's counter to 0
    pos = 0
    zeros = 0

    # For each entry in the given row of A:
    for entry in np.nditer(vector):
        # If the entry is not equal to 0:
        if entry != 0:
            # Add the value (non-zero) to the val list
            val.append(entry)

            # Add the column index of the entry (remainder of the current
            # position divided by the total number of columns) to the col list
            col.append(pos % matrix_size)

        # If the entry is equal to 0:
        else:
            # Add 1 to the zeros counter
            zeros += 1

        # Add 1 to the position counter
        pos += 1

    # Return the val and col lists, and add the length of the array to the
    # index of the beginning index of the row
    return val, col, row_start + len(val)
