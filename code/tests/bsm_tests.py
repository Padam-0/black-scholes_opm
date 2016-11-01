from nose.tools import *
import bsm
import numpy.testing
import numpy as np


def test_create_BS_matrix():
    Mn = -3
    M0 = 2
    M1 = 3
    M2 = 5
    M3 = 9
    M4 = 10

    T = 30

    r = 0.02
    theta = 0.3

    resMn = bsm.create_BS_matrix(Mn, Mn/T, r, theta)
    resM0 = bsm.create_BS_matrix(M0, M0/T, r, theta)
    resM1 = bsm.create_BS_matrix(M1, M1/T, r, theta)
    resM2 = bsm.create_BS_matrix(M2, M2/T, r, theta)
    resM3 = bsm.create_BS_matrix(M3, M3/T, r, theta)
    resM4 = bsm.create_BS_matrix(M4, M4/T, r, theta)

    assert_equal(resM1, outputsTBC)
    assert_equal(resM2, outputsTBC)
    assert_equal(resM3, outputsTBC)
    assert_equal(resM4, "File doesn't exist!")
    assert_equal(resM3, outputsTBC)
    assert_equal(resM3, outputsTBC)