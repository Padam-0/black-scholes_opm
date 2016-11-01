# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 12:45:06 2016

@author: Kieron
"""
#need the value of n (the size of the n*n matrix) stored from previously for this function
# need machine epsilon
# check if diverged: //xk-x(k-1)\\ increasing with each iteration
# ^^ for this, need function to calculate vector norms 
import numpy as np


def solve_axb(val, col, rowstart, b, n,maxits, e, w, x):
    def converged(e):
        if abs(x[k+1]-x[k])<e:
            return False
    k = 0
    while not converged(e) and k <= maxits:
        for i in range(1,n+1):
            sum1 = 0
            for j in range(rowstart[i], rowstart[i + 1]-1):
                sum1 = sum1 + val[j] * x[col[j]]
                if col[j] == i: # identify and store diagonal entry # ?? 
                    d =val[j]
            #d=10
            x[i] = x[i] + w * (b[i]-sum1)/d
        k = k + 1
    return x
val = np.array([21, 12, 49, 31, 16, 23, 85, 55, 91, 41])
col = np.array([1,4,2,1,3,6,4,1,5,6])
rowstart = np.array([1,3,4,7,8,10,11])
b= np.array([1,2,3,12,13,14])
n = 6
maxits = 100
w=1.3
x= np.array([0,0,0,0,0,0])
e=0.0001
solve_axb(val,col, rowstart,b,n,maxits,e,w,x)