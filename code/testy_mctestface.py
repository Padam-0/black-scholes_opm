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