"""
read_inputs.py

This module contains 1 function read_inputs() which takes 1 arguments:

  - filename - A string containing the path to the required input file

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

read_inputs() imports data from an input file in one of two formats. First is
a dense matrix format:

  - First row contains 1 integer, the size of the matrix n
  - Rows 2 - (n + 1) all contain n floats, the entries of the dense matrix A
  - Row n + 2 (final row) contains n floats, the vector b

The second is a Compressed Sparse Row matrix format:

  - First row contains t floats, entries of the val array (non-zero entries of
the matrix A)
  - Row 2 contains t integers, the column indices associated with the
corresponding entries of val in the matrix A
  - Row 3 contains n + 1 integers, the indices of the entries of val that
correspond to a new line of the matrix A
  - Row 4 contains n floats, the vector b

read_inputs() differentiates between these input types and imports them. It
does this by checking the number of entries in row 1. If there are more than
1, the format must be CSR.

If the format is dense, the first row is read in as the matrix size (n). The
next n rows are read in 1 at a time (to minimize storage requirements) and
non-zero values stored, and the col and rowStart lists populated accordingly
using convert_to_csr()

If the format is CSR, the 4 vectors are imported directly into numpy arrays
using np.genfromtext().

Both methods return 4 vectors:

  - val containing the non-zero values of the input matrix
  - col containing the associated column indices of these entries
  - rowStart containing the indices associated with each new row of the matrix
  - vector_b, the vector b

Note 1: Appending values to a growing list is a simple way to deal with the
iterative nature of building the val, col and rowStart arrays, Numpy arrays
do not deal well with having entries appended to them, as each new array is
written into memory individually. As such, col and rowStart are created and
grown as lists, then converted into numpy arrays when their contents will
not be changed.

Note 2: Traditional CSR refers to the first entry of each row as being in
column 1. However, due to Python using 0-indexing, the first column of this
matrix is referred to in this function as column 0. As such, the last entry of
rowStart is simply t, not t + 1, and so on.

Required: numpy, convert_to_csr

"""

import numpy as np
import scipy.io
from bin import convert_to_csr

def read_inputs(filename):
    # Open a file and extract data
    print(filename[-4:])
    if filename[-3:] == 'mtx':
        A = scipy.io.mmread(filename)
        A = A.tocsr()
        val = A.data
        col = A.indices
        rowStart = A.indptr

    elif np.genfromtxt(filename, max_rows=1).size == 1:

        # Initialize val, col and rowStart lists
        val, col, rowStart = [], [], [0]

        # Open a file and extract matrix size data
        matrix_size = int(np.genfromtxt(filename, max_rows=1))

        # For for the next n lines
        for i in range(matrix_size):
            # Read the line into memory
            line_in = np.genfromtxt(filename, skip_header=i+1, max_rows = 1)

            # If the line length is not equal to the number of rows in the
            # matrix:
            if line_in.size != matrix_size:
                # Exit with error
                exit("Input matrix is not square. Please ensure that all rows of "
                "the matrix have the same number of entries.")
            else:
                # Extend the val, col and rowStart lists with the outputs
                # from con_to_csr

                res_c2c = convert_to_csr.con_to_csr(line_in, matrix_size,
                                rowStart[-1])

                val.extend(res_c2c[0])
                col.extend(res_c2c[1])
                rowStart.append(res_c2c[2])

        # Convert to the lists to a numpy arrays
        val = np.array(val)
        col = np.array(col)
        rowStart = np.array(rowStart)

        print(val)
        print(col)
        print(rowStart)

        # Extract vector_b from file
        vector_b = np.genfromtxt(filename, skip_header = matrix_size + 1)

    else:
        # Input type is CSR
        val = np.genfromtxt(filename, max_rows=1)
        col = np.genfromtxt(filename, skip_header=1, skip_footer=2)
        rowStart = np.genfromtxt(filename, skip_header=2, skip_footer=1)
        vector_b = np.genfromtxt(filename, skip_header=3)

    return val, col, rowStart, vector_b