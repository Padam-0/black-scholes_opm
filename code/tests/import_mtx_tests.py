from nose.tools import *
import numpy.testing
import numpy as np
from sor_modules import import_mtx

def test_import_mtx():
    a = 'sample_inputs/sample_mtx.mtx'
    b = 'sample_inputs/s3dkt3m2.mtx'
    out = 'nas_Sor.out'
    res1 = import_mtx.import_mtx(a, out)

    val = np.array([1,2,3,4,5,6,7,8,9])
    col = np.array([0,1,2,0,1,2,0,1,2])
    rowStart = np.array([0,3,6,9])

    numpy.testing.assert_equal(res1[0], val)
    numpy.testing.assert_equal(res1[1], col)
    numpy.testing.assert_equal(res1[2], rowStart)

    assert_raises(SystemExit, import_mtx.import_mtx, b, out)

def test_get_mtx_b():
    """
    No unit available for this function as it initally prompts the command line.
    This functionality is tested during functional testing.

    """