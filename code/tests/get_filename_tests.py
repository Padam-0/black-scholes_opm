from nose.tools import *
import numpy.testing
import numpy as np
from sor_modules import get_filename

"""
get_filename_tests.py

This test module has three test functions:

test_check_CM_args();
test_check_file_exists(); and
test_con_filename()

test_check_CM_args() has one test scenario where both input and output
file names are given as arguments. Test scenarios for zero or one input
arguments cannot be checked as these prompt command line inputs

test_check_file_exists() has four test cases checking whether input file
names are available either the code or the sample_inputs folder

test_con_file() has six test cases which test input filename and output
filename scenarios

"""

def test_check_CM_args():
    pass

    """
    Due to command prompts present during the check_CM_args flow, it was not
    possible to create a reasonable set of unit tests

    """

def test_check_file_exists():
    a = 'nas_Sor.in'
    b = 'nas_Sor'
    c = '/nas_Sor.in'
    d = './nas_Sor.in'

    res1 = get_filename.check_file_exists(a)
    res2 = get_filename.check_file_exists(b)
    res3 = get_filename.check_file_exists(c)
    res4 = get_filename.check_file_exists(d)

    assert_equal(res1, True)
    assert_equal(res2, False)
    assert_equal(res3, False)
    assert_equal(res4, True)


def test_con_filename():
    a = 'nas_Sor2.in'
    b = 'Input_descriptions.txt'
    c = 'san_Ros.ni'
    d = 'sample_inputs/nas_Sor3.in'
    e = 'input.txt'


    res1 = get_filename.con_filename(a, 1)
    res2 = get_filename.con_filename(b, 0)
    res3 = get_filename.con_filename(c, 0)
    res4 = get_filename.con_filename(d, 0)
    res5 = get_filename.con_filename(e, 2)


    assert_equal(res1, ("sample_inputs/nas_Sor2.in", True))
    assert_equal(res2, ("Input_descriptions.txt", True))
    assert_equal(res3, ("san_Ros.ni", False))
    assert_equal(res4, ("sample_inputs/nas_Sor3.in", True))
    assert_equal(res5, ("input.txt", False))
