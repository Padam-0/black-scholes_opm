import math
import numpy as np

def csr_input_tests(val, col, rowStart, b):
    errors = []
    if val.size != col.size:
        errors.append("Value and column vectors are not the same length")

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


def dense_input_test(matrix_size, matrix_in, vector_b):

    # Check that first line is a number
    errors = []

    # Check that defined matrix size matches actual matrix size
    if matrix_size == np.size(matrix_in)/matrix_size:
        pass
    else:
        errors.append('Defined matrix size and actual matrix size do not match.')

    # Check that matrix size is an integer
    if matrix_size%1 == 0:
        pass
    else:
        errors.append("Defined matrix size is not an integer")

    # # Check matrix size and vector size are compatible
    if np.size(matrix_in)/matrix_size == np.size(vector_b):
        pass
    else:
        errors.append("Matrix length and vector length are not compatible")

    # Check that matrix is square
    if np.size(matrix_in)/matrix_size == matrix_size:
        pass
    else:
        errors.append("Matrix is not square")

    return errors