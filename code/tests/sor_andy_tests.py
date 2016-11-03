from nose.tools import *
import bsm
import sor_andy
import numpy.testing
import numpy as np


def test_create_BS_matrix():
    Mn = -3
    M0 = 2
    M1 = 3

    T = 30
    r = 0.02
    theta = 0.3

    resMn = bsm.create_BS_matrix(Mn, T/Mn, r, theta)
    resM0 = bsm.create_BS_matrix(M0, T/M0, r, theta)
    resM1 = bsm.create_BS_matrix(M1, T/M1, r, theta)

    assert_equal(resMn[0], "There must be at least 3 intervals")
    assert_equal(resM0[0], "There must be at least 3 intervals")

    numpy.testing.assert_array_almost_equal(resM1[0], np.array([2.1, -0.55,
        -1.6, 4.8, -2, -3.75, 9.3]), decimal=6)
    numpy.testing.assert_array_equal(resM1[1], np.array([0,1,0,1,2,1,2]))
    numpy.testing.assert_array_equal(resM1[2], np.array([0,2,5,7]))


def test_con_to_csr():
    res1 = sor_andy.con_to_csr(np.array([[12, 0, 0], [4, 11, 0],[7, 8, 16]]),
                                3.0)

    numpy.testing.assert_array_equal(res1[0],
                    np.array([12,4,11,7,8,16]))
    numpy.testing.assert_array_equal(res1[1],
                    np.array([0,0,1,0,1,2]))
    numpy.testing.assert_array_equal(res1[2], np.array([0,1,3,6]))


def test_zero_diag():
    res1 = sor_andy.con_to_csr(np.array([[12, 0, 0], [4, 11, 0], [7, 8, 16]]),
                                3.0)
    res2 = sor_andy.con_to_csr(np.array([[12, 0, 0, 5], [4, 11, 0, 4],
                                         [7, 8, 16, 12], [1,1,1,1]]),
                               4.0)
    res3 = sor_andy.con_to_csr(np.array([[12, 0, 0, 5, 7], [4, 11, 0, 4, 12],
                                         [7, 8, 0, 12, 14], [1, 1, 1, 1, 1],
                                         [2, 2, 2, 2, 2]]),
                               5.0)

    assert_equal(sor_andy.zero_diag(res1[0], res1[1], res1[2]), True)
    assert_equal(sor_andy.zero_diag(res2[0], res2[1], res2[2]), True)
    assert_equal(sor_andy.zero_diag(res3[0], res3[1], res3[2]), False)


def test_diag_dominant():
    res1 = sor_andy.con_to_csr(np.array([[12, 0, 0], [4, 11, 0], [7, 8, 16]]),
                               3.0)
    res2 = sor_andy.con_to_csr(np.array([[13, 0, 3, 5], [4, 11, 0, 4],
                                         [7, 8, 19, 1], [1, 1, 1, 11]]),
                               4.0)
    res3 = sor_andy.con_to_csr(np.array([[12, 0, 0, 5, 7], [4, 11, 0, 4, 12],
                                         [7, 8, 1, 12, 14], [1, 1, 1, 1, 1],
                                         [2, 2, 2, 2, 2]]),
                               5.0)
    assert_equal(sor_andy.diag_dominant(res1[0], res1[1], res1[2]), True)
    assert_equal(sor_andy.diag_dominant(res2[0], res2[1], res2[2]), True)
    assert_equal(sor_andy.diag_dominant(res3[0], res3[1], res3[2]), False)


def test_read_inputs():
    a = 'sample.in'
    b = 'sample'
    c = '/sample.in'
    d = './sa1ple.in'

    res1 = sor.read_inputs(a)
    res2 = sor.read_inputs(b)
    res3 = sor.read_inputs(c)
    res4 = sor.read_inputs(d)

    assert_equal(res1, outputsTBC)
    assert_equal(res2, outputsTBC)
    assert_equal(res3, outputsTBC)
    assert_equal(res4, "File doesn't exist!")

"""


#Sample Tests:



def test_getfilename():
    a = '../test.txt'
    b = '/Users/Padams/Documents/Programming/Python/projects/projpartners/test'
    c = 'test.ext'

    res0 = projpartners.getfilename(a)
    res1 = projpartners.getfilename(b)
    res2 = projpartners.getfilename(c)

    assert_equal(res0, os.path.join('..','test.txt'))
    assert_equal(res1, os.path.join('..','test.txt'))
    assert_equal(res2, os.path.join('..','test.txt'))


def test_create_criteria_matrix():
    s = [['peter.adam', 'Peter', 'Adam', 'Australia', 'Engineering', 'Y',
          'OaG'],
         ['andy.mcsweeney', 'Andy', 'McSweeney', 'Ireland', 'Engineering',
          'N', 'NA'],
         ['nicole.mcconville', 'Nicole', 'McConville', 'Ireland', 'Commerce',
          'N', 'NA']]
    res0 = projpartners.create_criteria_matrix(s, "CountryOfBirth")
    res1 = projpartners.create_criteria_matrix(s, "Industry")
    res2 = projpartners.create_criteria_matrix(s, "UnderGrad")

    numpy.testing.assert_array_equal(res0, [[0, 0, 0],[0, 0, 1],[0, 1, 0]])
    numpy.testing.assert_array_equal(res1, [[0, 0, 0],[0, 0, 0],[0, 0, 0]])
    numpy.testing.assert_array_equal(res2, [[0, 1, 0],[1, 0, 0],[0, 0, 0]])


def test_create_pp_matrix():
    s = [['peter.adam', 'Peter', 'Adam', 'Australia', 'Engineering', 'Y',
           'OaG'],
          ['andy.mcsweeney', 'Andy', 'McSweeney', 'Ireland', 'Engineering',
           'Y', 'Consulting'],
          ['nicole.mcconville', 'Nicole', 'McConville', 'Ireland', 'Commerce',
           'Y', 'Accounting']]
    p1 = [['peter.adam', 'andy.mcsweeney']]
    p2 = [['peter.adam', 'nicole.mcconville'],['peter.adam', 'andy.mcsweeney']]
    p3 = [['peter.adam', 'andy.mcsweeney'],['peter.adam', 'andy.mcsweeney']]
    M = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
    N = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
    O = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
    res0 = projpartners.create_pp_matrix(s, p1, M)
    res1 = projpartners.create_pp_matrix(s, p2, N)
    res2 = projpartners.create_pp_matrix(s, p3, O)

    numpy.testing.assert_array_equal(res0, [[1, -3, 3],[-2, 2, 3],[1, 2, 3]])
    numpy.testing.assert_array_equal(res1, [[1, -3, -4],[-2, 2, 3],[-2, 2, 3]])
    numpy.testing.assert_array_equal(res2, [[1, -4, 3],[-3, 2, 3],[1, 2, 3]])


def test_create_neye_matrix():
    res2 = projpartners.create_neye_matrix([1, 2])
    numpy.testing.assert_array_equal(res2, [[-1, -0],[-0, -1]])


def test_find_member_name():
    s = [['peter.adam', 'Peter', 'Adam', 'Australia', 'Engineering', 'Y',
          'OaG'],
         ['andy.mcsweeney', 'Andy', 'McSweeney', 'Ireland', 'Engineering',
          'Y', 'Consulting'],
         ['nicole.mcconville', 'Nicole', 'McConville', 'Ireland', 'Commerce',
          'Y', 'Accounting']]
    res0 = projpartners.find_member_name('peter.adam', s)
    res1 = projpartners.find_member_name('andy.mcsweeney', s)
    res2 = projpartners.find_member_name('nicole.mcconville', s)

    assert_equal(res0, "Peter Adam")
    assert_equal(res1, "Andy McSweeney")
    assert_equal(res2, "Nicole McConville")

"""