from nose.tools import *
import numpy.testing
import numpy as np
from sor_modules import condition

def test_condition():
    row = np.array([0, 0, 1, 2, 2, 2])
    col = np.array([0, 2, 1, 0, 1, 2])
    data = np.array([1, 2, 3, 4, 5, 6])
    row = row.astype(float)
    col = col.astype(float)
    data = data.astype(float)
    n = 3

    res1 = condition.condition(row,col,data,n)

    numpy.testing.assert_almost_equal(res1, 26.4622102617, decimal=10)