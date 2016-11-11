from nose.tools import *
import numpy.testing
import numpy as np
from sor_modules import value_checks

"""
value_check.py

"""
# Matrix Values
val1 = np.array([13.0, 4.0, 4.0, 11.0, 4.0, 7.0, 8.0, 20.0, 4.0, 1.0, 1.0, 14.0])
val2 = np.array([13.0, 4.0, 4.0, 11.0, 4.0, 7.0, 8.0, 4.0, 1.0, 1.0, 14.0])
val3 = np.array([3.0, 4.0, 4.0, 11.0, 4.0, 7.0, 8.0, 20.0, 4.0, 1.0, 1.0, 14.0])

col1 = np.array([0, 3, 0, 1, 3, 0, 1, 2, 3, 0, 2, 3])
col2 = np.array([0, 3, 0, 1, 3, 0, 1, 3, 0, 2, 3])
col3 = np.array([0, 3, 0, 1, 3, 0, 1, 2, 3, 0, 2, 3])

rowStart1 = np.array([0, 2, 5, 9, 12])
rowStart2 = np.array([0, 2, 5, 8, 11])
rowStart3 = np.array([0, 2, 5, 9, 12])



def test_zero_diag():
    res1 = value_checks.zero_diag(val1, col1, rowStart1)
    res2 = value_checks.zero_diag(val2, col2, rowStart2)
    res3 = value_checks.zero_diag(val3, col3, rowStart3)

    assert_equal(res1, True)
    assert_equal(res2, False)
    assert_equal(res3, True)


def test_diag_dominant():
    res1 = value_checks.diag_dominant(val1, col1, rowStart1)
    res2 = value_checks.diag_dominant(val3, col3, rowStart3)

    assert_equal(res1, True)
    assert_equal(res2, False)


def test_value_tests():
    errors = []

    res1 = value_checks.value_tests(val1, col1, rowStart1, errors)
    res2 = value_checks.value_tests(val2, col2, rowStart2, errors)
    res3 = value_checks.value_tests(val3, col3, rowStart3, errors)

    assert_equal(res1, [])
    assert_equal(res2, ["There are zeros on the diagonal"])
    assert_equal(res3, ["The matrix is not strictly row or column diagonally dominant"])

