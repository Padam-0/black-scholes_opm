from nose.tools import *
import numpy.testing
import numpy as np
from sor_modules import value_checks

"""
value_check.py

This module tests whether a SystemExit is trigger when a zero is located
on the diagonal of a matrix loaded into the program

"""
# Matrix Values
val1 = np.array([13.0, 4.0, 4.0, 11.0, 4.0, 7.0, 8.0, 4.0, 1.0, 1.0, 14.0])
col1 = np.array([0, 3, 0, 1, 3, 0, 1, 3, 0, 2, 3])
rowStart1 = np.array([0, 2, 5, 8, 11])


def test_value_tests():

    assert_raises(SystemExit, value_checks.value_tests, val1, col1, rowStart1, 'nas_Sor.out')

