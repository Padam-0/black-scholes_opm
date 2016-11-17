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
    N = 20
    X = 12
    S_max = 20
    h = (S_max/N)
    k = 5
    sigma = 0.02
    r = 0.3

    res1 = create_BS_b.create_BS_b(N, X, h, k, sigma, r)

    numpy.testing.assert_equal(res1, np.array([11., 10., 9., 8., 7., 6., 5., 4., 3., 2.,
                                               0., 0., 0., 0., 0., 0., 0., 0., 0.]))

