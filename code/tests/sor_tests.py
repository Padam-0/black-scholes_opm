# sor test file
from nose.tools import *
import sor
import numpy.testing
import numpy as np
import os


def test_read_inputs():
    print('Testing the inputs')

    a = 'sample.in'
    b = 'sample'
    c = '/sample.in'
    d = './sa1ple.in'

    res1 = sor.read_inputs(a)
    res2 = sor.read_inputs(b)
    res3 = sor.read_inputs(c)
    res4 = sor.read_inputs(d)

    print(res1)

    #assert_equal(res1, )
    # assert_equal(res2, outputsTBC)
    # assert_equal(res3, outputsTBC)
    # assert_equal(res4, "File doesn't exist!")



test_read_inputs()