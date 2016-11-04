# need the value of n (the size of the n*n matrix) stored from previously for this function
# need machine epsilon
# check if diverged: //xk-x(k-1)\\ increasing with each iteration
# ^^ for this, need function to calculate vector norms

import numpy as np
import math
from bin import calculate_residual, vector_norm


# #input two vectors and epilson to test for x convergence
# def x_convergence(val1,val2,e,x,k):
#     if vectornorm(abs(val1-val2))<e:
#         return "x-convergence. solution vector = %s . k=%s . e=%s"%(x, k,e)


# Find a good x initial vector

def create_initial_x(val, col, rowStart, b, n):
    l=[]
    for i in range(50):
        # Create 50 random initial vectors of size n
        x = np.random.randint(-100, 100, size=(n))
        # Calculate residuals of each random vector
        l.append([calculate_residual.residual(val, col, rowStart, b, x),x])
    best = l[0]
    # Find random vector with lowest residual
    for item in l:
        if item[0]<best[0]:
            best=item[1]
    return best



def sor(val, col, rowStart, b, n, maxits, w, x, e, tol):

    l = []

    """
    val= val.astype(float)
    col = col.astype(float)
    rowStart = rowStart.astype(float)
    b = b.astype(float)
    x = x.astype(float)
    """

    k = 0
    while k <= maxits:
        x1 = np.array(x.tolist()) #store x(k)th vector in x1
        for i in range(0, n):
            sum1 = 0
            for j in range(int(rowStart[i]), int(rowStart[i+1])):
                sum1=sum1+val[j] *x[int(col[j])]
                if col[j] == i:  # identify and store diagonal entry
                    d = val[j]
            x[i] = x[i] + w * (b[i] - sum1) / d

        x2 = np.array(x.tolist()) #store x(k-1)th vector in x2

        r = calculate_residual.residual(val, col, rowStart, b, x)

        l.append(vector_norm.vectornorm(abs(x1 - x2)))

        #  return solution_vector_x, stopping_reason, maxits, #_of_iterations, machine_epsilon, x-seq_tolerance, residual, w
        if r==0:
            return x, "Residual convergence", maxits, k+1, tol, r
            # ^^ have to return residual tolerance used..?

        elif vector_norm.vectornorm(abs(x1-x2)) < tol-4*e:
            #x-convergence
            return x, "x Sequence Convergence", maxits, k+1, tol, r
        #divergence
        elif k > 0 and l[k]>l[k-1]:
            return x, "Divergence",  maxits, k+1, tol, r
        else:
            k += 1
            if k== maxits:
                return x, "Max Iterations Reached", maxits, k, tol, r


"""
# How necessary is this? How does it affect the number of calculations
performed? Is the total saving significantly less than just an arbitrary guess?

#try out different values of w
def solve_axb_with_best_w(val, col, rowStart, b, n, maxits, w, x, A, tol):
    l=[]
    #if the user inputed any of these:
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
    #if the user inputed something other than 1.2, 1.3 or 1.4
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
"""

