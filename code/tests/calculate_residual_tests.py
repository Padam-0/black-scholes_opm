from nose.tools import *
import numpy.testing
import numpy as np
from code.bin import calculate_residual

"""
### calculate_residual tests ###

This function contains values to test the residual function with calculate_residual.py

Test data generated from current nas_Sor.in file
    Contents of nas_Sor.in:
    4
    13 0 0 4
    4 11 0 4
    7 8 20 4
    1 0 1 14
    1 2 3 4

"""

def test_calculate_residual():
    val = [13.0, 4.0, 4.0, 11.0, 4.0, 7.0, 8.0, 20.0, 4.0, 1.0, 1.0, 14.0]
    col = np.array([0,  3,  0,  1,  3,  0,  1,  2,  3,  0,  2,  3])
    rowStart = np.array([0, 2, 5, 9, 12])
    b = np.array([1, 2, 3, 4] )
    x = np.array([-0.00979992, 0.08289098, 0.06390363, 0.28184973])

    res1 = calculate_residual.residual(val, col, rowStart, b, x)

    numpy.testing.assert_almost_equal(res1, 2.5404391594785375e-10, decimal=5)
