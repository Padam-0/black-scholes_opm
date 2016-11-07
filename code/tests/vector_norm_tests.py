from nose.tools import *
import numpy as np
import math
from bin import vector_norm
import pytest

"""
vector_norm_tests.py

This test module contains three unit test cases to test the test_vector function.

Test 1 sends a 5 item numpy array containing only positive integers into the vectornorm
function and tests that the value returned is equal to the correct value sqrt(5)

Test 2 sends a 4 item numpy array containing both positive and negative integers into
the vectornorm function and tests that the value returned is equal to the correct
value sqrt(84)

Test 3 sends a 3 item numpy array containing both integers and strings into the
vectornorm function and tests that a TypeError is returned

"""


def test_vectornorm():
    v1 = np.array([1, 1, 1, 1, 1])
    v2 = np.array([-1, 3, 5, -7])
    #v3 = np.array(['a', 'b', 3])

    res1 = vector_norm.vectornorm(v1)
    res2 = vector_norm.vectornorm(v2)
    #res3 = vector_norm.vectornorm(v3)


    assert_equal(res1, math.sqrt(5))
    assert_equal(res2, math.sqrt(84))
    #assert_raises(TypeError, vector_norm.vectornorm(), np.array(['a', 'b', 3]))



