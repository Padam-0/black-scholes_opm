from nose.tools import *
import numpy.testing
import numpy as np
from bin import value_checks, convert_to_csr

"""
value_check.py





"""

def test_zero_diag():
    res1 = convert_to_csr.con_to_csr(np.array(
            [[12, 0, 0], [4, 11, 0], [7, 8, 16]]),
                                3.0)
    res2 = convert_to_csr.con_to_csr(np.array(
            [[13, 0, 3, 5], [4, 11, 0, 4],
             [7, 8, 19, 1], [1, 1, 1, 11]]),
                                4.0)
    res3 = convert_to_csr.con_to_csr(np.array(
            [[12, 0, 0, 5, 7], [4, 0, 0, 4, 12],
             [7, 8, 1, 12, 14], [1, 1, 1, 1, 1],
             [2, 2, 2, 2, 2]]),
                                5.0)

    assert_equal(value_checks.zero_diag(res1[0], res1[1], res1[2]), True)
    assert_equal(value_checks.zero_diag(res2[0], res2[1], res2[2]), True)
    assert_equal(value_checks.zero_diag(res3[0], res3[1], res3[2]), False)


def test_matrix_det():
    import numpy as np
    a = np.array([[12, 0, 0], [4, 11, 0], [7, 8, 16]])
    b = np.array([[12, 0, 0], [4, 0, 0], [7, 8, 16]])

    res1 = value_checks.matrix_det(a)
    res2 = value_checks.matrix_det(b)

    assert_equal(res1, True)
    assert_equal(res2, False)


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
    a = np.array([[12, 0, 0], [4, 0, 0], [7, 8, 16]])

    res1 = value_checks.value_tests(a)

    assert_equal(res1, "There are zeros on the diagonal")