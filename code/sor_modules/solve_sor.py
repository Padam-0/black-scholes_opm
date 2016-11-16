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


Requirements: numpy, calculate_residual, vector_norm, optimise_w, write_output
"""

import numpy as np
from sor_modules import calculate_residual, vector_norm, optimise_w, \
    write_output


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

    w_l = []

    k = 0
    while k <= maxits:
        print(w, ": Iteration: ", k)
        x1 = x.copy()

        for i in range(0, n):
            sum1 = 0
            for j in range(int(rowStart[i]), int(rowStart[i+1])):
                sum1 = sum1 + val[j] * x[int(col[j])]
                if col[j] == i:  # identify and store diagonal entry
                    d = val[j]
            x[i] = x[i] + w * (b[i] - sum1) / d

        x2 = x #store x(k-1)th vector in x2

        r = calculate_residual.residual(val, col, rowStart, b, x)

        print(w, ": Residual: ", r)

        l.append(vector_norm.vectornorm(abs(x1 - x2)))

        print(w, ": X-Residual: ", l[-1])

        """
        if len(l) >= 3:
            w = optimise_w.op_w(l, w)

        print(w)

        w_l.append(w)
        """
        # Return solution_vector_x, stopping_reason, maxits, #_of_iterations,
        # machine_epsilon, x-seq_tolerance, residual, w
        if r == 0:
            return x, "Residual convergence", maxits, k+1, tol, r
            # ^^ have to return residual tolerance used..? residual tolerance = ||r|| / ||b|| ?

        elif vector_norm.vectornorm(abs(x1-x2)) < tol + 4*e:
            #x-convergence
            return x, "x Sequence Convergence", maxits, k+1, tol, r

        elif k > 0 and l[k]>l[k-1]:
            # divergence
            return x, "Divergence",  maxits, k+1, tol, r

        else:
            k += 1
            if k == maxits:
                return x, "Max Iterations Reached", maxits, k, tol, r


def choose_w(val, col, rowStart, vector_b, n, x, e, tol, output_filename):
    l=[]
    #if the user inputed any of these:
    w_test = sor(val, col, rowStart, vector_b, n, 3, 1.2, x, e, tol)
    if w_test[1] == \
            "Divergence":
        write_output.output_text_file(output_filename, w_test)
        exit()

    w12 = sor(val, col, rowStart, vector_b, n, 10, 1.2, x, e, tol)
    w13 = sor(val, col, rowStart, vector_b, n, 10, 1.3, x, e, tol)
    w14 = sor(val, col, rowStart, vector_b, n, 10, 1.4, x, e, tol)

    if w13[5] < w14[5]:
        if w12[5] < w13[5]:
            return 1.2
        else:
            return 1.3
    else:
        if w12[5] < w14[5]:
            return 1.2
        else:
            return 1.4