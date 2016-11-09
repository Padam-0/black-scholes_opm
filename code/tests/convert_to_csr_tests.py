from nose.tools import *
import numpy.testing
import numpy as np
from sor_modules import convert_to_csr

"""
con_to_csr.py

This module contains four test cases. All four contain different valid tests that
are expected to pass and raise no errors

"""

def test_con_to_csr():

    vector1 = np.array([13., 0., 0., 4.])
    vector2 = np.array([4., 11., 0., 4.])
    vector3 = np.array([7., 8., 20., 4.])
    vector4 = np.array([1., 0., 1., 14.])

    matrix_size = 4

    rowStart1 = 0
    rowStart2 = 2
    rowStart3 = 5
    rowStart4 = 9

    res1 = convert_to_csr.con_to_csr(vector1, matrix_size, rowStart1)
    res2 = convert_to_csr.con_to_csr(vector2, matrix_size, rowStart2)
    res3 = convert_to_csr.con_to_csr(vector3, matrix_size, rowStart3)
    res4 = convert_to_csr.con_to_csr(vector4, matrix_size, rowStart4)

    assert_equal(res1, ([np.array([13]), np.array([4])], [0, 3], 2))
    assert_equal(res2, ([np.array([4]), np.array([11]), np.array([4])], [0, 1, 3], 5))
    assert_equal(res3, ([np.array([7]), np.array([8]), np.array([20]), np.array([4])], [0, 1, 2, 3], 9))
    assert_equal(res4, ([np.array([1]), np.array([1]), np.array([14])], [0, 2, 3], 12))
