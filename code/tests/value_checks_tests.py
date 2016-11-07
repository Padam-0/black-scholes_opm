from nose.tools import *
import numpy.testing
import numpy as np
from bin import value_checks, convert_to_csr

"""
value_check





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
    pass


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
    pass