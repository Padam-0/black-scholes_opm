from nose.tools import *
import numpy.testing
import numpy as np
from sor_modules import solve_sor


def test_sor():
    val = [13.0, 4.0, 4.0, 11.0, 4.0, 7.0, 8.0, 20.0, 4.0, 1.0, 1.0, 14.0]
    col = np.array([0, 3, 0, 1, 3, 0, 1, 2, 3, 0, 2, 3])
    rowStart = np.array([0, 2, 5, 9, 12])
    b = np.array([1, 2, 3, 4])
    n = 4
    maxits = 100
    w = 1.2
    x = np.array([-0.00979992, 0.08289098, 0.06390363, 0.28184973])
    e = 2.22044604925e-16
    tol = 1e-10

    res = solve_sor.sor(val, col, rowStart, b, n, maxits, w, x, e, tol)

    numpy.testing.assert_almost_equal(res[0], np.array([-0.00979992,  0.08289098,  0.06390363,  0.28184973]), decimal=6)
    numpy.testing.assert_equal(res[3], np.array([5]))
    numpy.testing.assert_almost_equal(res[5], np.array([1.040731881863575e-10]), decimal=6)
