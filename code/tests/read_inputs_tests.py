from nose.tools import *
import numpy.testing
import numpy as np
from sor_modules import read_inputs

def test_read_inputs():
    a = 'sample_inputs/nas_Sor.in'
    b = 'nas_Sor.out'

    val = np.array([12, 1, 4, 11, 3, 7, 8, 16, 1, 3])
    col = np.array([0, 3, 0, 1, 3, 0, 1, 2, 0, 3])
    rowStart = np.array([0, 2, 5, 8, 10])
    vector_b = np.array([1, 2, 3, 4])

    res1 = read_inputs.read_inputs(a, b)

    numpy.testing.assert_array_equal(res1[0], val)
    numpy.testing.assert_array_equal(res1[1], col)
    numpy.testing.assert_array_equal(res1[2], rowStart)
    numpy.testing.assert_array_equal(res1[3], vector_b)

