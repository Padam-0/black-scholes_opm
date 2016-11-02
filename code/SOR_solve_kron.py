# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 12:45:06 2016

@author: Kieron
"""
# need the value of n (the size of the n*n matrix) stored from previously for this function
# need machine epsilon
# check if diverged: //xk-x(k-1)\\ increasing with each iteration
# ^^ for this, need function to calculate vector norms 
import numpy as np


def solve_axb(val, col, rowstart, b, n, maxits, e, w, x):
    # def converged(e):
    #     if k == 0 or k==1:
    #         return False
    #     elif abs(x[k-1] - x[k-2]) < e:
    #         return True
    #     else:
    #         return False

    # converged(e) == False and
    k = 0
    while k <= maxits:
        for i in range(0, n):
            sum1 = 0
            for j in range(rowstart[i], rowstart[i + 1]-1):
                sum1 = sum1 + val[j] * x[col[j]]
                if col[j] == i:  # identify and store diagonal entry # ??
                    d = val[j]
                print(i,j)
            d = 1
            x[i] = x[i] + w * (b[i] - sum1) / d
        k = k + 1
    return x, k, d


rowstart = np.array([0, 1, 2, 3])
col = np.array([0,1,2])
val = np.array([1,2,3])

b = np.array([1, 2, 3])
n = 3
maxits = 9
w = 1.3
x = np.array([0, 0, 0])
e = 0.0001
print(solve_axb(val, col, rowstart, b, n, maxits, e, w, x))
