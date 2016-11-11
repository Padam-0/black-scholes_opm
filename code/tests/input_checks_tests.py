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
# Matrix Values
val1 = np.array([13.0, 4.0, 4.0, 11.0, 4.0, 7.0, 8.0, 20.0, 4.0, 1.0, 1.0, 14.0])
val2 = np.array([13.0, 4.0, 4.0, 11.0, 4.0, 7.0, 8.0, 4.0, 1.0, 1.0, 14.0])
val3 = np.array([3.0, 4.0, 4.0, 11.0, 4.0, 7.0, 8.0, 20.0, 4.0, 1.0, 1.0, 14.0, 15.0])

col1 = np.array([0, 3, 0, 1, 3, 0, 1, 2, 3, 0, 2, 3])
col2 = np.array([0, 3, 0, 1, 3, 0, 1, 3, 0, 2, 3, 4])
col3 = np.array([0, 3, 0, 3.5, 3, 0, 1, 2, 3, 0, 2, 3])

rowStart1 = np.array([0, 2, 5, 9, 12])
rowStart2 = np.array([0, 2, 5, 8, 10])
rowStart3 = np.array([1, 2, 5, 9, 12])
rowStart4 = np.array([0, 2.5, 5, 9, 12])
rowStart5 = np.array([0, 2, 5, 9, 13])

b1 = np.array([2, 3, 4, 5])
b2 = np.array([2, 3, 4, 5, 6])
b3 = np.array([2, 3, 4, 5])
b4 = np.array([2, 3, 4, 5])

def test_csr_input_checks():
    res1 = input_checks.csr_input_checks(val1, col1, rowStart1, b1)
    res2 = input_checks.csr_input_checks(val1, col1, rowStart1, b2)
    res3 = input_checks.csr_input_checks(val1, col2, rowStart1, b1)
    res4 = input_checks.csr_input_checks(val1, col1, rowStart2, b1)
    res5 = input_checks.csr_input_checks(val1, col1, rowStart3, b1)
    res6 = input_checks.csr_input_checks(val1, col1, rowStart4, b1)
    res7 = input_checks.csr_input_checks(val3, col1, rowStart5, b1)
    res8 = input_checks.csr_input_checks(val1, col3, rowStart1, b1)

    assert_equal(res1, [])
    assert_equal(res2, ["Number of columns in matrix is not the same as the "
                      "number of rows in Vector b"])
    assert_equal(res3, ["Uneven number of rows and columns"])
    assert_equal(res4, ["Last entry of RowStart vector is equivalent to the "
                      "nth entry of val + 1"])
    assert_equal(res5, ["First entry of RowStart vector is not 0"])
    assert_equal(res6, ["RowStart vector contains non-integer entries"])
    assert_equal(res7, ["Value and column vectors do not have the same number "
                      "of entries"])
    assert_equal(res8, ["Column vector contains non-integer entries", "Uneven number of rows and columns"])