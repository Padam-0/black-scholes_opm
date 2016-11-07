"""
convert_to_csr.py

This module contains 1 function, con_to_csr(), which takes 3 arguments. These
are:

  - vector - An 1 dimensional numpy array containing values corresponding to
the input matrix A.
  - matrix_length - An integer representing the number of rows / columns n,
in the n x n input matrix A.

Compressed Sparse Row formatting, or CSR, is an efficient storage algorithm
for sparse matrices. It takes a n x n matrix and converts it to 3 vectors,
2 of length t (number of non-zero entries in the input matrix A) and one of
length n + 1. These are:

  - val - A vector of length t that contains all the non-zero entries of
matrix A.
  - col - A vector of length t that contains the column indices of all the
non-zero entries of matrix A.
  - rowStart - A vector of length n + 1 that contains the indices of the
entries of val which correspond to the first entry of each row of A. The
first entry is always 0, and the last entry is t + 1, which corresponds to
the first entry of the (n + 1)th row of the matrix, or the end of the matrix.

con_to_csr() returns these 3 vectors as numpy arrays.

Requirements: numpy

"""

import numpy as np

def con_to_csr(vector, matrix_size, row_start):
    # Convert an numpy array to Compressed Sparse Row Structure

    # Remove non-zero entries in val
    val = [i for i in vector if i != 0]

    # Initialize empty col lists
    col = []

    #Set position counter and number of 0's counter to 0
    pos = 0
    zeros = 0

    # For each entry in the given row of A:
    for entry in np.nditer(vector):
        # If the entry is not equal to 0:
        if entry != 0:
            # Add the column index of the entry (remainder of the current
            # position divided by the total number of columns) to the col list
            col.append(pos % matrix_size)

        # If the entry is equal to 0:
        else:
            # Add 1 to the zeros counter
            zeros += 1

        # Add 1 to the position counter
        pos += 1

    return val, col, row_start + pos - zeros