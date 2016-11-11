from nose.tools import *
import numpy.testing
import numpy as np
from sor_modules import import_mtx

def test_import_mtx():
    a = 'sample_inputs/sample_mtx.mtx'
    res1 = import_mtx.import_mtx(a)

    val = np.array([8.04932042e+02, 0.00000000e+00, -1.02927285e-02,..., -4.73610061e+00, 1.90242608e-02, 9.68270142e+00])
    col = np.array([0, 1, 2,...,90446, 90447, 90448])
    rowStart = np.array([0, 18, 36,..., 3753429, 3753448, 3753461])

    numpy.testing.assert_equal(res1, val, col, rowStart)

def test_get_mtx_b():
    val = np.array( [8.04932042e+02, 0.00000000e+00, -1.02927285e-02, ..., -4.73610061e+00, 1.90242608e-02, 9.68270142e+00])
    col = np.array([0, 1, 2, ..., 90446, 90447, 90448])
    rowStart = np.array([0, 18, 36, ..., 3753429, 3753448, 3753461])

    res1 = import_mtx.get_mtx_b(val, rowStart)

    assert_equal(res1, "Would you like tols enter a file containing a vector b?[y/n]: ")