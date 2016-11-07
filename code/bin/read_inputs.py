"""
read_inputs.py

This module contains 1 function:

read_inputs().

read_inputs() takes 1 arguments:

  - filename - A string containing the path to the required input file

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
iterative nature of building the col and rowStart arrays, Numpy arrays do not
deal well with having entries appended to them, as each new array is written
into memory individually. As such, col and rowStart are created and grown as
lists, then converted into numpy arrays when their contents will not be
changed.

Note 2: Traditional CSR refers to the first entry of each row as being in column
1. However, due to Python using 0-indexing, the first column of this matrix
is referred to in this function as column 0. As such, the last entry of
rowStart is simply t, not t + 1, and so on.

Required: numpy, convert_to_csr

"""

import numpy as np
from bin import convert_to_csr

def read_inputs(filename):
    # Open a file and extract data
    if np.genfromtxt(filename, max_rows=1).size == 1:
        # Input type is dense

        # Open a file and extract matrix size data

        val, col, rowStart = [], [], [0]

        matrix_size = int(np.genfromtxt(filename, max_rows=1))
        for i in range(matrix_size):
            line_in = np.genfromtxt(filename, skip_header=i+1, max_rows = 1)
            if line_in.size != matrix_size:
                print("Input matrix is not square. Please ensure that all rows of "
                "the matrix have the same number of entries.")
                exit(0)
            else:
                last_rowS = rowStart[-1]

                val.extend(convert_to_csr.con_to_csr(line_in, matrix_size,
                                                last_rowS)[0])
                col.extend(convert_to_csr.con_to_csr(line_in, matrix_size,
                                                last_rowS)[1])
                rowStart.append(convert_to_csr.con_to_csr(line_in, matrix_size,
                                                last_rowS)[2])

        # After all value indices have been added to the col and rowStart
        # vectors, the final value of rowStart is t, the length of the col
        # list.

        val  = np.array(val)

        # Convert to the col list to a numpy array
        col = np.array(col)

        # Convert to the rowStart list to a numpy array
        rowStart = np.array(rowStart)

        vector_b = np.genfromtxt(filename, skip_header = matrix_size + 1)

    else:
        # Input type is CSR
        val = np.genfromtxt(filename, max_rows=1)
        col = np.genfromtxt(filename, skip_header=1, skip_footer=2)
        rowStart = np.genfromtxt(filename, skip_header=2, skip_footer=1)
        vector_b = np.genfromtxt(filename, skip_header=3)

    return val, col, rowStart, vector_b