from nose.tools import *
import numpy.testing
import numpy as np
from bin import get_filename

### get_filename check_CM_args ###

"""
get_filename_tests.py

This test module has three test functions:

test_check_CM_args();
test_check_file_exists(); and
test_con_filename()

test_check_CM_args() has one test scenario

test_con_file() has six test cases which test input filename and output
filename scenarios

"""

def test_check_CM_args():

    res1 = get_filename.check_CM_args(["sor.py", "nas_Sor.in",
                                     "nas_Sor.out"])


    assert_equal(res1, ("nas_Sor.in", "nas_Sor.out"))

### get_filename check_file_exists ###

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


### get_filename con_filename ###


def test_con_filename():
    a = 'nas_Sor2.in'
    b = 'Input_descriptions.txt'
    c = 'san_Ros.ni'
    d = 'sample_inputs/nas_Sor3.in'
    e = 'output.txt'
    f = 'input.txt'


    res1 = get_filename.con_filename(a, 1)
    res2 = get_filename.con_filename(b, 0)
    res3 = get_filename.con_filename(c, 0)
    res4 = get_filename.con_filename(d, 0)
    res5 = get_filename.con_filename(e, 2)
    res6 = get_filename.con_filename(f, 2)


    assert_equal(res1, ("sample_inputs/nas_Sor2.in", True))
    assert_equal(res2, ("Input_descriptions.txt", True))
    assert_equal(res3, ("san_Ros.ni",False))
    assert_equal(res4, ("sample_inputs/nas_Sor3.in", True))
    assert_equal(res5, ("sample_outputs/output.txt", True))
    assert_equal(res6, ("input.txt", False))
