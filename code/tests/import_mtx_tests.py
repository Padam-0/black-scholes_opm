from nose.tools import *
import numpy.testing
import numpy as np
from sor_modules import import_mtx

def test_import_mtx():
    a = 'sample_inputs/sample_mtx.mtx'
    res1 = import_mtx.import_mtx(a)
    print(res1)

    val = np.array([1,2,3,4,5,6,7,8,9])
    col = np.array([0,1,2,0,1,2,0,1,2])
    rowStart = np.array([0,3,6,9])

    numpy.testing.assert_equal(res1[0], val)
    numpy.testing.assert_equal(res1[1], col)
    numpy.testing.assert_equal(res1[2], rowStart)

def test_get_mtx_b():
    a = 'sample_inputs/sample_mtx.mtx'

    val, col, rowStart = import_mtx.import_mtx(a)

    res1 = import_mtx.get_mtx_b(val, rowStart, True)

    assert_equal(res1.size, 3)