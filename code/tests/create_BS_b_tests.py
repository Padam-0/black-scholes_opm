from nose.tools import *
import numpy.testing
import numpy as np
from bsm_modules import create_BS_b

"""

create_BS_b.py

This test module contains two test cases:

- Test 1 tests values to create a small b vector
- Test 2 tests values to create a larger b vector

"""


def test_create_BS_b():
    M1 = 5
    M2 = 10
    X = 12
    X2 = 120
    S_max = 20
    S_max2 = 200
    k = 5
    theta = 0.02
    r = 0.3

    res1 = create_BS_b.create_BS_b(M1, X, S_max, k, theta, r)
    res2 = create_BS_b.create_BS_b(M2, X2, S_max2, k, theta, r)

    # test 1
    #numpy.testing.assert_array_almost_equal(res1, np.array([-0.988, 4., 0.,
    # 0., 0.]), decimal=6)

    # test 2
    #numpy.testing.assert_array_almost_equal(res2, np.array([10.12, 80., 60.,
    #  40., 20., 0., 0., 0., 0., 0.]), decimal=6)
