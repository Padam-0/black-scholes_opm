from nose.tools import *
import numpy.testing
import numpy as np
from sor_modules import calculate_residual

"""
calculate_residual tests

This test module has one test case:

- Test case 1 reads in test data from nas_Sor.in which has all valid inputs

"""

def test_calculate_residual():
    val = [13.0, 4.0, 4.0, 11.0, 4.0, 7.0, 8.0, 20.0, 4.0, 1.0, 1.0, 14.0]
    col = np.array([0,  3,  0,  1,  3,  0,  1,  2,  3,  0,  2,  3])
    rowStart = np.array([0, 2, 5, 9, 12])
    b = np.array([1, 2, 3, 4] )
    x = np.array([-0.00979992, 0.08289098, 0.06390363, 0.28184973])

    res1 = calculate_residual.residual(val, col, rowStart, b, x)

    # test case 1
    numpy.testing.assert_almost_equal(res1, 2.5404391594785375e-10, decimal=6)
