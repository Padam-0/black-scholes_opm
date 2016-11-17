from nose.tools import *
import numpy.testing
import numpy as np
from sor_modules import optimise_w

def test_op_w():

    list = [0.6, 0.7, 0.79, 0.7, 0.8]
    w = 1.2

    res1 =  optimise_w.op_w(list, w)

    assert_equal(res1, 1.2)

