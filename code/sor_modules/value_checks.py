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

def value_tests(val, col, rowStart, errors, output_file_name):

    # Check if the matrix has zeros on the diagonal:

    # Set initial row number
    row = 0

    for i in range(len(rowStart)-1):
        # Create r, a list of all column values for that row
        r = col[int(rowStart[i]):int(rowStart[i+1])]
        # If the row number is not in r:
        if row not in r:
            # Output False
            write_output.output_text_file(output_file_name, "Zero on diagonal")
            exit("There are zeros on the diagonal")
        row += 1
