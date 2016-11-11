from nose.tools import *
import numpy.testing
import numpy as np
from sor_modules import write_output

def test_output_test_file():

    """
    Difficult to unittest functions that output files. Needs more work.

    """
    a = 'nas_Sor.out'

    res1 = write_output.output_test_file(a, "x Sequence Convergence", 100, 31, 2.22044604925e-16, 1e-10, 1.8884963934515226e-10, 0, [-0.00979991834387, 0.0828909759224, 0.0639036341383, 0.281849734586])

    assert_equal(res1, "nas_Sor.out")