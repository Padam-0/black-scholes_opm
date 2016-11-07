from nose.tools import *
import numpy.testing
import numpy as np
from bin import read_inputs

def test_read_inputs():
    a = 'nas_Sor.in'

    val = np.array([13, 4, 4, 11, 4, 7, 8, 20, 4, 1, 1, 14])
    col = np.array([0, 3, 0, 1, 3, 0, 1, 2, 3, 0, 2, 3])
    rowStart = np.array([0, 2, 5, 9, 12])
    vector_b = np.array([1, 2, 3, 4])

    res1 = read_inputs.read_inputs(a)

    assert_equal(res1, (val, col, rowStart, vector_b))

