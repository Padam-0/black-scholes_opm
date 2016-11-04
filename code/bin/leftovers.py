# If you can't find something you wrote, I probably deleted it and it's now
# in here

import numpy as np
import math

"""
val = np.array([12,4,11,7,8,16])
col = np.array([0,0,1,0,1,2])
rowStart = np.array([0,1,3,6])
b = np.array([1,2,3])
"""

def ssor(val, col, rowStart, b):
    mach_ep = np.finfo(float).eps
    w = 1.2
    maxits = 75
    tol = 1 * 10 ** (-6)

    n = len(rowStart) - 1

    x = np.random.randn(n)

    k = 0

    x_no = 1
    converged = False

    while k <= maxits and converged == False:
        ns = 1
        for i in range(0, n):
            sum = 0
            for j in range(rowStart[i], rowStart[i + 1]):
                sum = sum + val[j] * x[col[j]]
                if col[j] == i:
                    d = val[j]
            x[i] = x[i] + w * (b[i] - sum) / d
            ns += (x[i]) ** 2
        k += 1

        x_norm = math.sqrt(ns - 1)
        #print(abs(x_no - x_norm))
        if abs(x_no - x_norm) < (tol + 4 * mach_ep):
            converged = True
        x_no = x_norm

    return k, x

"""
From output
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

"""



"""
From test_solve_axb


# val = np.array([1.,2.,3.])
# col = np.array([0.,1.,2.])
# rowstart = np.array([0., 1., 2., 3.])
# b = np.array([1., 2., 13.])
# x = np.array([1., 1., 1.])
# n = 3
# maxits = 50
# tol = 1*10**-6
# A = np.array([[1,0,0],[0,2,0],[0,0,3]])
# w = 1.22
# # print(solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol))
# # w = 1.3
# # print(solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol))
# # w = 1.4
# # print(solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol))
# print(solve_axb_with_best_w(val, col, rowstart, b, n, maxits, w, x, A, tol))




# ##floats
# val = np.array([1.,2.,3.])
# col = np.array([0.,1.,2.])
# rowstart = np.array([0., 1., 2., 3.])
# b = np.array([1., 2., 13.])
# x = np.array([1., 1., 1.])
# n = 3
# maxits = 50
# w = 1.3
# e = 0.1
# A = np.array([[1.,0.,0.],[0.,2.,0.],[0.,0.,3.]])
# print(solve_axb(val, col, rowstart, b, n, maxits, w, x, A))



##integers
# maxits = 50
# w = 1.4
# e = 0.1
# val = np.array([21, 12, 49, 31,16,23,85,55,91,41])
# col = np.array([0,3,1,0,2,5,3,0,4,5])
# rowstart = np.array([0,2,3,6,7,9,10])
# b = np.array([11, 2, 3,4,5,6])
# x = np.array([60, 15, 2,84,4,100])
# n = 6
# A= np.array([[21,0,0,12,0,0], [0,49,0,0,0,0], [31,0,16,0,0,23], [0,0,0,85,0,0],[55,0,0,0,91,0],[0,0,0,0,0,41]])
# print(solve_axb(val, col, rowstart, b, n, maxits, e, w, x, A))

# #floats
# maxits = 50
# w = 1.4
# e = 0.1
# val = np.array([21., 12., 49., 31.,16.,23.,85.,55.,91.,41.])
# col = np.array([0.,3.,1.,0.,2.,5.,3.,0.,4.,5.])
# rowstart = np.array([0.,2.,3.,6.,7.,9.,10.])
# b = np.array([11., 2., 3., 4., 5., 6.])
# x = np.array([60., 15., 2., 84., 4., 100.])
# n = 6
# A= np.array([[21.,0.,0.,12.,0.,0.], [0.,49.,0.,0.,0.,0.], [31.,0.,16.,0.,0.,23.], [0.,0.,0.,85.,0.,0.],[55.,0.,0.,0.,91.,0.],[0.,0.,0.,0.,0.,41.]])
# print(solve_axb(val, col, rowstart, b, n, maxits, e, w, x, A))

# print(solve_axb_with_best_w(val, col, rowstart, b, n, maxits, w, x, A, tol))

"""