import SOR_solve_kron
import numpy as np

val = np.array([1.,2.,3.])
col = np.array([0.,1.,2.])
rowstart = np.array([0., 1., 2., 3.])
b = np.array([1., 2., 13.])
x = np.array([1., 1., 1.])
n = 3
maxits = 50
tol = 1*10**-6
A = np.array([[1,0,0],[0,2,0],[0,0,3]])
w = 1.22
# print(solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol))
# w = 1.3
# print(solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol))
# w = 1.4
# print(solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol))



