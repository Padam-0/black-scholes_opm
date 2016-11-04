import numpy as np
from bin import vector_norm

def residual(val, col, rowStart, b, x):
    #solve b - Ax
    # Let Ax = c, then b - c
    n = rowStart.size - 1
    c = np.zeros(n)
    for i in range(n):
        sum = 0
        for j in range(rowStart[i], rowStart[i + 1]):
            sum = sum + val[j] * x[int(col[j])]
        c[i] = c[i] + sum
    residual = vector_norm.vectornorm(b-c)
    return residual

"""
#residual = b-Ax^ x^ is the current guess at x
def residual(b,A,x):
    Ax =A @ x
    return vectornorm(b-Ax)

"""