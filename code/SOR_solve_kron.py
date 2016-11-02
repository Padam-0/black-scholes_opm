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
    k = 0
    while k <= maxits:
        for i in range(0, n):
            sum1 = 0
            for j in range(rowstart[i], rowstart[i+1]):
                sum1=sum1+val[j] *x[col[j]] # multiply each value in A by an element from the zero vector..?
                                            # that will just make sum1=0
                
#                 print (x[col[j]]) 

                if col[j] == i:  # identify and store diagonal entry
                    d = val[j]
            x[i] = x[i] + w * (b[i] - sum1) / d
        k = k + 1
        if abs(x[k] - x[k-1]) < e:
            print(x)
            print(x[k])
            print(x[k-1])
            print(abs(x[k] - x[k-1]))
            return "converged", x,k
    return x, k

val = np.array([1,2,3])
col = np.array([0,1,2])
rowstart = np.array([0, 1, 2, 3])
b = np.array([1, 2, 13])
x = np.array([0, 0, 0])
n = 3

maxits = 0
w = 1.3
e = 0.000000000001
# print(solve_axb(val, col, rowstart, b, n, maxits, e, w, x))


val = np.array([21, 12, 49, 31,16,23,85,55,91,41])
col = np.array([0,3,1,0,2,5,3,0,4,5])
rowstart = np.array([0,2,3,6,7,9,10])
b = np.array([1, 2, 3,4,5,6])
x = np.array([0, 0, 0,0,0,0])
# x = np.array([1,1,1,1,1,1])
n = 6
print(solve_axb(val, col, rowstart, b, n, maxits, e, w, x))