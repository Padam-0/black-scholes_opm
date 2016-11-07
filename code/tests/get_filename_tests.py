from nose.tools import *
import numpy.testing
import numpy as np
from code.bin import get_filename

### get_filename check_CM_args ###

"""
def test_check_CM_args():
    res1 = get_filename.check_CM_args(["sor.py", "nas_Sor.in",
                                     "nas_Sor.out"])

    assert_equal(res1, ("nas_Sor.in", "nas_Sor.out"))
"""

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

# Needs more work

def test_con_filename():
    a = 'nas_Sor.in'
    b = 'nas_Sor'
    c = '/nas_Sor.in'
    d = './nas_Sor.in'
    i = 'san_Ros.ni'

    e = 'nas_Sor.out'
    f = 'nas_Sor'
    g = '/nas_Sor.out'
    h = './nas_Sor.out'
    j = 'san_Ros.tuo'


    res1 = get_filename.con_filename(a,1)
    res2 = get_filename.con_filename(b,1)
    res3 = get_filename.con_filename(c,1)
    res4 = get_filename.con_filename(d,1)
    res9 = get_filename.con_filename(i,1)

    res5 = get_filename.con_filename(e, 2)
    res6 = get_filename.con_filename(f, 2)
    res7 = get_filename.con_filename(g, 2)
    res8 = get_filename.con_filename(h, 2)
    res10 = get_filename.con_filename(j,2)

    assert_equal(res1, True)
    assert_equal(res2, True)
    assert_equal(res3, True)
    assert_equal(res4, True)
    assert_equal(res5, True)
    assert_equal(res6, True)
    assert_equal(res7, True)
    assert_equal(res8, True)
    assert_equal(res9, False)
    assert_equal(res10, False)