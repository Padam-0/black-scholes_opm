import sys
sys.path.append("..")

import numpy as np
from bin import vector_norm

"""
calculate_residual.py

This module contains 1 function, residual(), which takes 5 argumentss. These
are:

val - A 1 dimensional numpy array containing the input matrix (A) values in
CRS format.
col - A 1 dimensional numpy array containing the column references for the
input matrix (A) entries in val.
rowStart - A 1 dimensional numpy array containing the reference indices for
the beginning of each new row of the the input matrix (A)
b - A 1 dimensional numpy array that represents the solution vector b
x - A 1 dimensional numpy array that is the calculated solution to the
equation Ax = b for the given input matrix A and vector b.

residual() solves the equation b - Ax for the given input vector b, calculated
solution vector x, and input matrix A (in CRS format). An zero numpy array c
is initialized with length n (dimension of matrix A). The entries of c are
populated with the solution of Ax.

Once Ax = c is solved, the norm of the resultant vector b - c is returned,
a float, residual.

This represents the 'distance' to the correct value of x from the current
guess (of x) at an iteration. A smaller value of residual suggests that the
distance between current guess for x and the true solution is small.

"""

def residual(val, col, rowStart, b, x):
    # Solve ||b - Ax||
    # Let Ax = c, then ||b - c||

    # Calculate n, the number of rows in the input matrix
    n = rowStart.size - 1
    # Initialize an empty vector c, of size n
    c = np.zeros(n)

    # For each row in the matrix:
    for i in range(n):
        # Reset the sum to 0
        sum = 0

        # For each entry in a given row:
        for j in range(int(rowStart[i]), int(rowStart[i + 1])):
            # sum increases by the i-th row / j-th column value in A
            # multiplied by the j-th entry in x
            sum += val[j] * x[int(col[j])]
        # Once the i-th row has been completed, set the corresponding i-th
        # entry of c to the solution for that row of Ax
        c[i] = sum

    # The residual is the vector norm of b - c
    residual = vector_norm.vectornorm(b-c)

    return residual