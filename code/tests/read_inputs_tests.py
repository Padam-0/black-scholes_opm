from nose.tools import *
import numpy.testing
import numpy as np
from sor_modules import read_inputs

def test_read_inputs():
    a = 'sample_inputs/nas_Sor.in'
    b = 'nas_Sor.out'

    val = np.array([13, 4, 4, 11, 4, 7, 8, 20, 4, 1, 1, 14])
    col = np.array([0, 3, 0, 1, 3, 0, 1, 2, 3, 0, 2, 3])
    rowStart = np.array([0, 2, 5, 9, 12])
    vector_b = np.array([1, 2, 3, 4])

    res1 = read_inputs.read_inputs(a, b)

    numpy.testing.assert_array_equal(res1[0], val)
    numpy.testing.assert_array_equal(res1[1], col)
    numpy.testing.assert_array_equal(res1[2], rowStart)
    numpy.testing.assert_array_equal(res1[3], vector_b)

