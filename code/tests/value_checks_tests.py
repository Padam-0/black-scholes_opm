from nose.tools import *
import numpy.testing
import numpy as np
from sor_modules import value_checks

"""
value_check.py
"""
# Matrix Values
val1 = [13.0, 4.0, 4.0, 11.0, 4.0, 7.0, 8.0, 20.0, 4.0, 1.0, 1.0, 14.0]
val2 = [0.0, 4.0, 4.0, 11.0, 4.0, 7.0, 8.0, 20.0, 4.0, 1.0, 1.0, 0.0]
val3 = [3.0, 4.0, 4.0, 11.0, 4.0, 7.0, 8.0, 20.0, 4.0, 1.0, 1.0, 14.0]

col1 = np.array([0, 3, 0, 1, 3, 0, 1, 2, 3, 0, 2, 3])
col2 = np.array([0, 3, 0, 1, 3, 0, 1, 2, 3, 0, 2])
col3 = np.array([0, 3, 0, 1, 3, 0, 1, 2, 3, 0, 2, 3])

rowStart1 = np.array([0, 2, 5, 9, 12])
rowStart2 = np.array([0, 2, 5, 9, 12])
rowStart3 = np.array([0, 2, 5, 9, 12])


def test_zero_diag():
    res1 = value_checks.zero_diag(val1, col1, rowStart1)
    res2 = value_checks.zero_diag(val2, col2, rowStart2)
    res3 = value_checks.zero_diag(val3, col3, rowStart3)

    assert_equal(res1, True)
    assert_equal(res2, False)
    assert_equal(res3, True)

def test_diag_dominant():
    res1 = convert_to_csr.con_to_csr(np.array(
            [[12, 0, 0], [4, 11, 0],
             [7, 8, 16]]),
                               3.0)
    res2 = convert_to_csr.con_to_csr(np.array(
            [[13, 0, 3, 5], [4, 11, 0, 4],
             [7, 8, 19, 1], [1, 1, 1, 11]]),
                               4.0)
    res3 = convert_to_csr.con_to_csr(np.array(
            [[12, 0, 0, 5, 7], [4, 11, 0, 4, 12],
             [7, 8, 1, 12, 14], [1, 1, 1, 1, 1],
             [2, 2, 2, 2, 2]]),
                               5.0)
    assert_equal(value_checks.diag_dominant(res1[0], res1[1], res1[2]), True)
    assert_equal(value_checks.diag_dominant(res2[0], res2[1], res2[2]), True)
    assert_equal(value_checks.diag_dominant(res3[0], res3[1], res3[2]), False)


def test_value_tests():

    errors = 0

    res1 = value_checks.value_tests(val1, col1, rowStart1, errors)
    res2 = value_checks.value_tests(val2, col2, rowStart2, errors)
    res3 = value_checks.value_tests(val3, col3, rowStart3, errors)

    assert_equal(res1, None)
    assert_equal(res2, "There are zeros on the diagonal")
    assert_equal(res3, "The matrix is not row and column diagonally dominant")

