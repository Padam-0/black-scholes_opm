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

#find a good x initial vector
def create_good_inital_x_vector(A,b,n):
    l=[]
    for i in range(50):
        x=np.random.randint(-100, 100, size=(n)) #create an initial vector of size n
        l.append([residual(b,A,x),x])
    best=l[0]
    for item in l:
        if item[0]<best[0]:
            best=item[1]
    return best

#try out different values of w
def solve_axb_with_best_w(val, col, rowstart, b, n, maxits, w, x, A, tol):
    l=[]
    if w == 1.2 or w == 1.3 or w == 1.2:
        w = 1.2
        solved1 = solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol)
        w = 1.3
        solved2 = solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol)
        if solved1[3]<solved2[3]:
            best = solved1
        else:
            best = solved2
        w =1.4
        solved3 = solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol)
        if solved3[3]<best[3]:
            return solved3
        else:
            return best
    else:
        solved1 = solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol)
        w = 1.2
        solved2 = solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol)
        if solved1[3]<solved2[3]:
            best = solved1
        else:
            best = solved2
        w = 1.3
        solved3 = solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol)
        if solved3[3] < best[3]:
            best = solved3
        w = 1.4
        solved4 = solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol)
        if solved4[3]<best[3]:
            return solved4
        else:
            return best


def solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol):

    k = 0
    l=[]
    e = np.finfo(float).eps
    val= val.astype(float)
    col = col.astype(float)
    rowstart = rowstart.astype(float)
    b = b.astype(float)
    x= x.astype(float)
    A=A.astype(float)
    x = create_good_inital_x_vector(A, b, n) #override the given x vector, this can be taken out of the solve_axb function
    #and can be used to create x in the first place
    while k <= maxits:
        x1=x.tolist()
        x1= np.array(x1) #store x(k)th vector in x1
        for i in range(0, n):
            sum1 = 0
            for j in range(int(rowstart[i]), int(rowstart[i+1])):
                sum1=sum1+val[j] *x[int(col[j])]
                if col[j] == i:  # identify and store diagonal entry
                    d = val[j]
            x[i] = x[i] + w * (b[i] - sum1) / d
        x2=x.tolist()
        x2=np.array(x2) #store x(k-1)th vector in x2
        r=residual(b,A,x)
        # print("residual at %s iteration = %s"%(k,r))
        # print("x-convergence test = %s"%(vectornorm(x1-x2)))
        # print("current solution vector \t", x)
        l.append(vectornorm(abs(x1 - x2)))
        #  return solution_vector_x, stopping_reason, maxits, #_of_iterations, machine_epsilon, x-seq_tolerance, residual, w
        if r==0:
            return x, "Residual convergence", maxits, k+1, e, tol, r, w
            # have to return residual tolerance used..
        elif vectornorm(abs(x1-x2)) < tol-4*e:
            #x-convergence
            return x, "x Sequence Convergence", maxits, k+1, e, tol, r, w
        elif k>0 and l[k]>l[k-1]:
            return x, "Divergence",  maxits, k+1, e, tol, r, w
        else:
            k += 1
            if k== maxits:
                return x, "Max Iterations Reached", maxits, k, e, tol, r, w
    # return "something unexpected has happened.."


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
print(solve_axb_with_best_w(val, col, rowstart, b, n, maxits, w, x, A, tol))




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