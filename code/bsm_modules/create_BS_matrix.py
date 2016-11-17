"""
create_BS_matrix.py

This module contains 1 function, create_BS_matrix() which takes 4 arguments:

  - M - Number of partitions of the time interval from 0 to T, integer.
  - k - Size of each partition of the time interval, T/M, float.
  - r - Daily risk free rate, a float
  - sigma - Volatility, a float.

To solve an option pricing model, we first form a system of linear equations
for the timestep m = M - 1 and solve the resulting equation Af = b. This gives:

f_(n, M) = -nk/2(n * sigma^2-r) * f_(n-1,M-1)
    + (1 + kr + k * sigma^2 * n^2)* f_(n,M-1)
    - nk/2(n * sigma^2 + r) * f_(n+1, M-1)

The Black-Scholes matrix, A, is created by finding the solution for each m
from the equation above. Simply put, this is a sparse matrix with bandwidth
1. The diagonal values (n = m) are of the form:

f_(n,m) = 1 + k * r + k * n^2 * sigma^2

The lower band values (left-hand side of the diagonal) are:

f_(n - 1, m) = -nk/2 * (n * sigma^2 - r)

The upper band values (right-hand side of the diagonal) are:

f_(n - 1, m) = -nk/2 * (n * sigma^2 + r)

Using this, a CSR matrix can be built for given inputs M, k, r and sigma,
which can then be solved using Successive Over Relaxation.

Note 1: Appending values to a growing list is a simple way to deal with the
iterative nature of building the val, col and rowStart arrays, Numpy arrays
do not deal well with having entries appended to them, as each new array is
written into memory individually. As such, col and rowStart are created and
grown as lists, then converted into numpy arrays when their contents will
not be changed.

Note 2: Traditional CSR refers to the first entry of each row as being in
column 1. However, due to Python using 0-indexing, the first column of this
matrix is referred to in this function as column 0. As such, the last entry of
rowStart is simply t, not t + 1, and so on.

Requirements: math, numpy

"""

import math
import numpy as np

def create_BS_matrix(M, k, r, sigma):
    # Check that there are at least 3 intervals
    # If there aren't:

    N = M - 1

    if N < 3:
        # Exit
        exit("There must be at least 3 intervals")
    # If there are:
    else:
        # Create matrix in CSR form

        # Initialize empty lists
        val = []
        col = []
        rowStart = [1]

        # for 0 through 3 * (N-2) + 5 (total number of matrix entries):
        for n in range(1, 3 * (N-2) + 5):
            # Calculate the row number
            row = math.floor(n / 3) + 1
            # If diagonal value:
            if n % 3 == 1:
                # Calculate diagonal value for the given row
                value = 1 + (k * r) + k * ((sigma) ** 2) * ((row) ** 2)
                # Set column to current row
                column = row
            # If upper band:
            elif n % 3 == 2:
                # Calculate upper band value for the given row
                value = ((-1 * row * k)/2) * (row * (sigma ** 2) + r)
                # Set column to current row + 1
                column = row + 1
            # If lower band:
            else:
                # Calculate the lower band value for the given row
                value = ((-1 * row * k)/2) * (row * (sigma ** 2) - r)
                # Set column to current row - 1
                column = row - 1
                # Append current index to rowStart
                rowStart.append(n)
            # Append value and column to the appropriate list
            val.append(value)
            col.append(column)

        # Append the total number of entries in A to rowStart, as the n+1-th
        # row, or the stopping limit
        rowStart.append(3 * (N-2) + 5)

        # Convert lists to numpy arrays
        val = np.array(val)
        col = np.array(col) - 1
        rowStart = np.array(rowStart) - 1

        # Return arrays
        return val, col, rowStart


M = 5
k = 5
r = 0.02
sigma = 0.3
val, col, rowStart = create_BS_matrix(M, k, r, sigma)

print('val: ', val)
print('col: ', col)
print('rowStart: ', rowStart)