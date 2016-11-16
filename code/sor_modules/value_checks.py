"""
value_checks.py

This module contains 3 functions:

  - zero_diag();
  - diag_dominant(); and
  - value_tests().

zero_diag() takes 3 arguments. These are:

  - val - A 1 dimensional numpy array containing the input matrix (A) values in
CRS format.
  - col - A 1 dimensional numpy array containing the column references for the
input matrix (A) entries in val.
  - rowStart - A 1 dimensional numpy array containing the reference indices for
the beginning of each new row of the the input matrix (A).

zero_diag() aims to identify any 0's on the diagonal of a matrix in CSR
format. It does this by cycling through each row of the matrix, and finding
the value where row number = column number, ie the diagonal entry. If this
number is not present (aka zero in a CSR format), the function returns False.
This is repeated for all rows.


diag_dominant() takes 3 arguments. These are:

  - val - A 1 dimensional numpy array containing the input matrix (A) values in
CRS format.
  - col - A 1 dimensional numpy array containing the column references for the
input matrix (A) entries in val.
  - rowStart - A 1 dimensional numpy array containing the reference indices for
the beginning of each new row of the the input matrix (A).

diag_dominant() calculates the sum of the absolute values of entries in each
row, and the sum of the absolute values of entries in each column. It then
subtracts the absolute value of the diagonal element. If the absolute value
of the diagonal element is greater than the remainder, that row / column is
deemed to be strictly row / column diagonally dominant.

If this is true for all rows or columns in a matrix, the matrix is strictly
diagonally dominant. For conversion of SOR, the input matrix must either be
row or column diagonally dominant. diag_dominant() calculates both, and if
either is satisfied, returns True. Otherwise, returns False.


value_tests() takes 4 arguments. These are:

  - val - A 1 dimensional numpy array containing the input matrix (A) values in
CRS format.
  - col - A 1 dimensional numpy array containing the column references for the
input matrix (A) entries in val.
  - rowStart - A 1 dimensional numpy array containing the reference indices for
the beginning of each new row of the the input matrix (A).
errors - A list of errors, potentially empty.

value_tests() applies zero_diag() and diag_dominant() to the input matrix,
and if they fail, appends a given error statement to the errors list. The
errors list is returned.

Requirements: numpy, write_output

"""

from sor_modules import write_output
import numpy as np

def zero_diag(val, col, rowStart):
    # Check if there are 0's on the diagonal of the input matrix

    # Set initial row number
    row = 0

    # For each row
    for i in range(len(rowStart)-1):
        # Create r, a list of all column values for that row
        r = col[int(rowStart[i]):int(rowStart[i+1])]
        # If the row number is not in r:
        if row not in r:
            # Output False
            return False

        row += 1

    # If all diagonal values are non-zero
    return True


def diag_dominant(val, col, rowStart):
    # Check if the diagonal value is larger than the sum of all
    # other entries in that row or column

    # Initialize empty lists
    diags = []
    col_sums = []
    row_sums = []

    # For each row in the matrix:
    for i in range(len(rowStart) - 1):

        # Create r, a list of all column values for that row
        r = col[int(rowStart[i]):int(rowStart[i + 1])]
        # For each non-zero column entry in a row

        if i in r:
            # Append the diagonal entry (row number = column number) to the
            # diags list
            diags.append(abs(val[int(rowStart[i] + np.where(r == i)[0])]))

        # Set the column sum to 0
        c_sum = 0
        # For each column index:
        for j in range(len(col)):
            # If the column index is equal to the current
            if col[j] == i:
                c_sum += abs(val[j])
        col_sums.append(c_sum)

        # Set the row sum to 0

        r_sum = 0
        for k in range(int(rowStart[i]), int(rowStart[i + 1])):
            r_sum += abs(val[k])

        row_sums.append(r_sum)

    # Convert diag to numpy array to allow element-wise operations
    diags = np.array(diags)

    # Subtract the diagonal element of each row / column from the row or
    # column sum
    col_sums = np.array(col_sums) - diags
    row_sums = np.array(row_sums) - diags

    # If the diagonal element or a row / column is greater than the row or
    # column sum, return True
    return np.greater(diags, col_sums).all() or \
           np.greater(diags,row_sums).all()
#changed np.greater() to np.greater_equal on line 137 and 138

def value_tests(val, col, rowStart, errors, output_file_name):

    # Check if the matrix has zeros on the diagonal:
    if not zero_diag(val, col, rowStart):
        # Write output file
        write_output.output_text_file(output_file_name, "Zero on diagonal")
        # Quit
        exit("There are zeros on the diagonal")
    # Check if the matrix is strictly row or column diagonally dominant:
    """
    elif not diag_dominant(val, col, rowStart):
        # Write output

        # Quit
        exit("The matrix is not strictly row or column diagonally "
                      "dominant")
    """