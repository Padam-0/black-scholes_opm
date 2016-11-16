from nose.tools import *
import numpy.testing
import numpy as np
from sor_modules import raw_input_check

"""
raw_input_check_tests.py

This test module contains three test cases which submit clean and dirty test
files to the read_raw_inputs function and check whether it catches characters
that we do not want to import

"""


def test_read_raw_inputs():
    a = 'sample_inputs/nas_Sor4.in'
    b = 'sample_inputs/nas_Sor5.in'

    out = 'nas_Sor.out'

    res1 = raw_input_check.read_raw_inputs(a, out)

    assert_equals(res1, False)
    assert_raises(SystemExit, raw_input_check.read_raw_inputs, b, out)


