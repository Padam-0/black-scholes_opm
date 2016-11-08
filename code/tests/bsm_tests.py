from nose.tools import *
import numpy.testing
import numpy as np
from bsm_modules import create_BS_b, create_BS_matrix

def test_create_BS_matrix():
    Mn = -3
    M0 = 2
    M1 = 3

    T = 30
    r = 0.02
    theta = 0.3


    M = 2
    X = 12
    S_Max = 20
    k = 20
    r = 0.02
    theta = 0.3


    # resMn = create_BS_matrix.create_BS_matrix(Mn, T/Mn, r, theta)
    # resM0 = create_BS_matrix.create_BS_matrix(M0, T/M0, r, theta)
    # resM1 = create_BS_matrix.create_BS_matrix(M1, T/M1, r, theta)

    #res1 = create_BS_matrix.create_BS_matrix(M, k, r, theta)

    assert_raises(SystemExit, create_BS_matrix.create_BS_matrix, M ,k, r, theta)

    # assert_equal(resMn[0], "There must be at least 3 intervals")
    # assert_equal(resM0[0], "There must be at least 3 intervals")
    #
    # numpy.testing.assert_array_almost_equal(resM1[0], np.array([2.1, -0.55,
    #     -1.6, 4.8, -2, -3.75, 9.3]), decimal=6)
    # numpy.testing.assert_array_equal(resM1[1], np.array([0,1,0,1,2,1,2]))
    # numpy.testing.assert_array_equal(resM1[2], np.array([0,2,5,7]))