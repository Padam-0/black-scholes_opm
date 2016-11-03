import sor_andy
import numpy as np
import SOR_solve_kron

def test_solve_axb():
    A = np.array([[12, 0, 0], [4, 11, 0], [7, 8, 16]])
    n = 3
    val, col, rowstart = sor_andy.con_to_csr(A, n)
    print(type(val))
    b=np.array([1,2,3])
    w=1.3
    x=np.array([1,1,1])
    tol = 1*10**-6
    maxits = 50
    res1 = SOR_solve_kron.solve_axb(val,col,rowstart,b, n, maxits, w, x, A, tol)
    numpy.testing.assert_array_equal(res1[0],
                                     np.array([1/12, 5/33, 53/704]))
    # numpy.testing.assert_array_equal(res1[1],
    #                                  np.array([0, 0, 1, 0, 1, 2]))
    # numpy.testing.assert_array_equal(res1[2], np.array([0, 1, 3, 6]))
test_solve_axb()