from nose.tools import *
import numpy.testing
import numpy as np
from bin import raw_input_check

def test_read_raw_inputs():
    a = 'nas_Sor.in'
    b = 'sample_inputs/nas_Sor2.in'

    res1 = raw_input_check.read_raw_inputs(a)
    res2 = raw_input_check.read_raw_inputs(b)

    assert_equals(res1, True)
    assert_equals(res2, True)

