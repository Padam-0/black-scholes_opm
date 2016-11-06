from nose.tools import *
import numpy.testing
import numpy as np
from code import bsm

def test_create_BS_matrix():
    Mn = -3
    M0 = 2
    M1 = 3

    T = 30
    r = 0.02
    theta = 0.3

    resMn = bsm.create_BS_matrix(Mn, T/Mn, r, theta)
    resM0 = bsm.create_BS_matrix(M0, T/M0, r, theta)
    resM1 = bsm.create_BS_matrix(M1, T/M1, r, theta)

    assert_equal(resMn[0], "There must be at least 3 intervals")
    assert_equal(resM0[0], "There must be at least 3 intervals")

    numpy.testing.assert_array_almost_equal(resM1[0], np.array([2.1, -0.55,
        -1.6, 4.8, -2, -3.75, 9.3]), decimal=6)
    numpy.testing.assert_array_equal(resM1[1], np.array([0,1,0,1,2,1,2]))
    numpy.testing.assert_array_equal(resM1[2], np.array([0,2,5,7]))