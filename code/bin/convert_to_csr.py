import numpy as np

"""
convert_to_csr.py

This module contains 1 function, con_to_csr(), which takes 2 arguments. These
are:

matrix - An n x n numpy array containing values corresponding to the input
matrix A.
matrix_length - An integer representing the number of rows / columns n, in the
n x n input matrix A.

Compressed Sparse Row formatting, or CSR, is an efficient storage algorithm
for sparse matrices. It takes a n x n matrix and converts it to 3 vectors,
2 of length t (number of non-zero entries in the input matrix A) and one of
length n + 1. These are:

val - A vector of length t that contains all the non-zero entries of matrix A.
col - A vector of length t that contains the column indices of all the
non-zero entries of matrix A.
rowStart - A vector of length n + 1 that contains the indices of the entries of
val which correspond to the first entry of each row of A. The first entry is
always 0, and the last entry is t + 1, which corresponds to the first entry
of the (n + 1)th row of the matrix, or the end of the matrix.

con_to_csr() returns these 3 vectors as numpy arrays.

Note 1: Appending values to a growing list is a simple way to deal with the
iterative nature of building the col and rowStart arrays, Numpy arrays do not
deal well with having entries appended to them, as each new array is written
into memory individually. As such, col and rowStart are created and grown as
lists, then converted into numpy arrays when their contents will not be
changed.

Note 2: Traditional CSR refers to the first entry of each row as being in column
1. However, due to Python using 0-indexing, the first column of this matrix
is referred to in this function as column 0. As such, the last entry of
rowStart is simply t, not t + 1, and so on.

"""


def con_to_csr(matrix, matrix_length):
    # Convert an numpy array to Compressed Sparse Row Structure

    # Reformat initial matrix A into a continuous vector
    val = np.ndarray.flatten(matrix)
    # Remove non-zero entries in val
    val = [i for i in val if i != 0]

    # Initialize empty col and rowStart lists
    col = []
    rowStart = []

    #Set position counter and number of 0's counter to 0
    pos = 0
    zeros = 0

    # For each entry in the initial matrix A:
    for entry in np.nditer(matrix):
        # If the entry is not equal to 0:
        if entry != 0:
            # Add the column index of the entry (remainder of the current
            # position divided by the total number of columns) to the col list
            col.append((pos) % matrix_length)

            # if the current entry is the last in a given row:
            if pos % matrix_length == 0:

                # Add the current position index to the rowStart list
                rowStart.append(pos - zeros)
        # If the entry is equal to 0:
        else:
            # Add 1 to the zeros counter
            zeros += 1

        # Add 1 to the position counter
        pos += 1

    # After all value indices have been added to the col and rowStart vectors,
    # the final value of rowStart is t, the length of the col list.
    rowStart.append(len(col))

    # Convert to the col list to a numpy array
    col = np.array(col)

    # Convert to the rowStart list to a numpy array
    rowStart = np.array(rowStart)

    return val, col, rowStart