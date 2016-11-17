from nose.tools import *
import numpy.testing
import numpy as np
from bsm_modules import create_BS_matrix

"""

bsm_tests.py

The test module has four test cases:

- Test 1 tests an invalid argument, M = 2. A SystemExit is the expected return
- Test 2 tests another invalid argument M = -2. A SystemExit is the expected return
- Test 3 tests four valid inputs
- Test 4 tests another invalid argument, k = "string". A TypeError is the expected return

"""


def test_create_BS_matrix():

    M1 = 2
    M2 = -2
    M3 = 5

    k1 = 5
    k2 = "string"
    r = 0.02
    sigma = 0.3


    res1 = create_BS_matrix.create_BS_matrix(M3, k1, r, sigma)

    # test case 1
    assert_raises(SystemExit, create_BS_matrix.create_BS_matrix, M1 ,k1 , r, sigma)

    # test case 2
    assert_raises(SystemExit, create_BS_matrix.create_BS_matrix, M2, k1, r, sigma)

    # test case 3
    numpy.testing.assert_array_almost_equal(res1[0], np.array([1.55, -0.275, -0.8, 2.9, -1., -1.875,
                                                               5.15, -2.175, -3.4, 8.3]), decimal=10)
    numpy.testing.assert_array_equal(res1[1], np.array([0, 1, 0, 1, 2, 1, 2, 3, 2, 3]))
    numpy.testing.assert_array_equal(res1[2], np.array([0, 2, 5, 8, 10]))

    # test case 4
    assert_raises(TypeError, create_BS_matrix.create_BS_matrix, M3, k2, r, sigma)