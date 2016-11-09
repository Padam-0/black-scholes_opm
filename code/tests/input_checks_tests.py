from nose.tools import *
import numpy.testing
import numpy as np
from sor_modules import input_checks

""""
def test_csr_input_checks():
    val = np.array([13, 4, 4, 11, 4, 7, 8, 20, 4, 1, 1, 14])
    val2 = np.array([13, 4, 4, 11, 4])

    col = np.array([0, 3, 0, 1, 3, 0, 1, 2, 3, 0, 2, 3])
    rowStart = np.array([0, 2, 5, 9, 12])
    b = np.array([1, 2, 3, 4])

    res1 = input_checks.csr_input_checks(val, col, rowStart, b)
    res2 = input_checks.csr_input_checks(val2, col, rowStart, b)

    assert_equal(res1, None)
    assert_equal(res2, "Value and column vectors are not the same length")
"""

def test_dense_input_test():
    matrix_size = None
    matrix_in = None
    vector_b = None

    #res1 = input_checks.dense_input_checks(matrix_size, matrix_in, vector_b)

    assert_equal(res1, None)