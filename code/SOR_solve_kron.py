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
import math

#||v|| = sqrt(v1^2 + v2^2 +... +vn^2) 
def vectornorm(v):
    total = 0
    for element in v:
        total += element**2
    return math.sqrt(total)

# #input two vectors and epilson to test for x convergence
# def x_convergence(val1,val2,e,x,k):
#     if vectornorm(abs(val1-val2))<e:
#         return "x-convergence. solution vector = %s . k=%s . e=%s"%(x, k,e)

#residual = b-Ax^ x^ is the current guess at x  
def residual(b,A,x):
    Ax =A @ x
    return vectornorm(b-Ax)

def solve_axb(val, col, rowstart, b, n, maxits, e, w, x, A):
    k = 0
    l=[]
    while k <= maxits:
        x1=x.tolist()
        x1= np.array(x1) #store x(k)th vector in x1
#         l.append(x1)
        for i in range(0, n):
            sum1 = 0
            for j in range(int(rowstart[i]), int(rowstart[i+1])):
                sum1=sum1+val[j] *x[int(col[j])]                 
#                 print (x[col[j]]) 

                if col[j] == i:  # identify and store diagonal entry
                    d = val[j]
            x[i] = x[i] + w * (b[i] - sum1) / d
        x2=x.tolist()
        x2=np.array(x2) #store x(k-1)th vector in x2
#         l.append(x2)
        
        r=residual(b,A,x)
        print("residual at %s iteration = %s"%(k,r))
        print("x-convergence test = %s"%(vectornorm(x1-x2)))
        print("current solution vector \t", x)
        print()
        if r==0:
            return "residual ==0", x,k
        
        if vectornorm(abs(x1-x2))<e:
            return "x-convergence:", x, "k=%s"%(k), "e=%s"%(e)
        #test for divergence
        l.append(vectornorm(abs(x1-x2)))
        if k>0 and l[k]>l[k-1]:
            return "diverging: \n ||x(k) − x(k−1)|| increased on this iteration: \
            \n value at (k)th iteration = %s \
            \n value at (k-1)th iteration = %s"%(l[k],l[k-1])
        
        k = k + 1
    return "something unexpected has happened.."

val = np.array([1.,2.,3.])
col = np.array([0.,1.,2.])
rowstart = np.array([0., 1., 2., 3.])
b = np.array([1., 2., 13.])
x = np.array([1., 1., 1.])
n = 3
maxits = 50
w = 1.3
e = 0.1
A = np.array([[1.,0.,0.],[0.,2.,0.],[0.,0.,3.]])
print(solve_axb(val, col, rowstart, b, n, maxits, e, w, x, A))


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

##floats
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