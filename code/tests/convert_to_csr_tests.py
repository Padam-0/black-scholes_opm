from nose.tools import *
import numpy.testing
import numpy as np
from code.bin import  convert_to_csr

### convert_to_csr tests ###
# Two test cases set up to test

def test_con_to_csr():
    res1 = convert_to_csr.con_to_csr(np.array(
            [[12, 0, 0], [4, 11, 0],[7, 8, 16]]), 3.0)

    res2 = convert_to_csr.con_to_csr(np.array(
        [[13, 0, 0, 4], [4, 11, 0, 4], [7, 8, 20, 4], [1, 0, 1, 14]]), 4)


    # 3x3 Matrix Tests
    numpy.testing.assert_array_equal(res1[0], np.array([12,4,11,7,8,16]))
    numpy.testing.assert_array_equal(res1[1], np.array([0,0,1,0,1,2]))
    numpy.testing.assert_array_equal(res1[2], np.array([0,1,3,6]))

    #4x4 Matrix Tests
    numpy.testing.assert_array_equal(res2[0], np.array([13.0, 4.0, 4.0, 11.0, 4.0, 7.0, 8.0, 20.0, 4.0, 1.0, 1.0, 14.0]))
    numpy.testing.assert_array_equal(res2[1], np.array([0, 3, 0, 1, 3, 0, 1, 2, 3, 0, 2, 3]))
    numpy.testing.assert_array_equal(res2[2], np.array([0, 2, 5, 9, 12]))