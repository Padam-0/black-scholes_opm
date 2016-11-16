"""
value_checks.py

This module contains 1 function value_tests() that takes 4 arguments:

  - val - A 1 dimensional numpy array containing the input matrix (A) values in
CRS format.
  - col - A 1 dimensional numpy array containing the column references for the
input matrix (A) entries in val.
  - rowStart - A 1 dimensional numpy array containing the reference indices for
the beginning of each new row of the the input matrix (A).
output_filename - A file name to write errors to

value_tests() identifies any 0's on the diagonal of a matrix in CSR
format. It does this by cycling through each row of the matrix, and finding
the value where row number = column number, ie the diagonal entry. If this
number is not present (aka zero in a CSR format), the alerts the user and
writes an output file. This is repeated for all rows.

Requirements: numpy, write_output

"""

from sor_modules import write_output

def value_tests(val, col, rowStart, output_file_name):

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