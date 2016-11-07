from nose.tools import *
import numpy.testing
import numpy as np
from bin import raw_input_check

"""
raw_input_check_tests.py

This test module contains three test cases which submit clean and dirty test
files to the read_raw_inputs function and check whether it catches characters
that we do not want to import

"""


def test_read_raw_inputs():
    a = 'nas_Sor.in'
    b = 'sample_inputs/nas_Sor2.in'
    c = 'sample_inputs/nas_Sor4.in'

    res1 = raw_input_check.read_raw_inputs(a)
    res2 = raw_input_check.read_raw_inputs(b)
    res3 = raw_input_check.read_raw_inputs(c)

    assert_equals(res1, True)
    assert_equals(res2, True)
    assert_equals(res3, False)


