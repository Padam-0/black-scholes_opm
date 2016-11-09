"""
solve_sor.py

This module contains two functions:

- create_initial_x(); and
- sor().

create_initial_x() takes 5 arguments. These are:

  - val - A 1 dimensional numpy array containing the input matrix (A) values in
CRS format.
  - col - A 1 dimensional numpy array containing the column references for the
input matrix (A) entries in val.
  - rowStart - A 1 dimensional numpy array containing the reference indices for
the beginning of each new row of the the input matrix (A).
  - b - A 1 dimensional numpy array that represents the solution vector b.
  - n - an integer the size of the x vector to be created.

create_initial_x() creates 50 initial x-vectors made up of n random
integers whose values range from -100 to 100. The function residual()
is imported to calculate residuals. Each x-vector and its residual is appended
to a list.

Whichever x-vector has the lowest residual returned to be used as the initial x-vector in SOR.

Requirements: numpy and calculate_residual

sor() takes 10 arguments. These are:

  - val - A 1 dimensional numpy array containing the input matrix (A) values in
CRS format.
  - col - A 1 dimensional numpy array containing the column references for the
input matrix (A) entries in val.
  - rowStart - A 1 dimensional numpy array containing the reference indices for
the beginning of each new row of the the input matrix (A).
  - b - A 1 dimensional numpy array that represents the solution vector b.
  - n - an integer the size of the x vector to be created.
  - maxits - Maximum integer of iterations allowed.
  - w - Relaxation factor, float.
  - x - A 1 dimensional numpy array created from create_initial_x() which is the
initial solution to Ax=b.
  - e - the machine epsilon to be used, float.
  - tol - X Sequence tolerance allowed, float.

what does it do
Sor() solves Ax=b for x when the matrix A is in CSR format. It creates a while loop
which iterates a maximum number of times (equal to maxits), improving the initial
guess for the x-vector each time. After each iteration the function checks whether
there was residual convergence, x-sequence convergence, or divergence and stops if
any of these are true. If after maxits number of iterations none of these conditions
are true then the loop stops.


The function will return:

- the solution vector_x
- the stopping reason
- the maximum number of iterations
- the actual number of iterations
- machine epsilon
- the tolerance allowed
- the current residual
- and w, the relaxation factor.


Requirements: numpy, vector_norm
"""

import numpy as np
from sor_modules import calculate_residual, vector_norm


def create_initial_x(val, col, rowStart, b, n):
    # Find a good x initial vector
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

    b = b.astype(float)
    x = x.astype(float)

    k = 0
    while k <= maxits:
        x1 = x.copy()

        for i in range(0, n):
            sum1 = 0
            for j in range(int(rowStart[i]), int(rowStart[i+1])):
                sum1=sum1+val[j] * x[int(col[j])]
                if col[j] == i:  # identify and store diagonal entry
                    d = val[j]
            x[i] = x[i] + w * (b[i] - sum1) / d

        x2 = x #store x(k-1)th vector in x2

        r = calculate_residual.residual(val, col, rowStart, b, x)

        l.append(vector_norm.vectornorm(abs(x1 - x2)))

        # Return solution_vector_x, stopping_reason, maxits, #_of_iterations,
        # machine_epsilon, x-seq_tolerance, residual, w
        if r == 0:
            return x, "Residual convergence", maxits, k+1, tol, r
            # ^^ have to return residual tolerance used..? residual tolerance = ||r|| / ||b|| ?

        elif vector_norm.vectornorm(abs(x1-x2)) < tol+4*e:
            #x-convergence
            return x, "x Sequence Convergence", maxits, k+1, tol, r

        elif k > 0 and l[k]>l[k-1]:
            # divergence
            return x, "Divergence",  maxits, k+1, tol, r

        else:
            k += 1
            if k == maxits:
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

