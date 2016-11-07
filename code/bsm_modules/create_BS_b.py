"""
create_BS_b.py

This module contains 1 function, create_BS_b(), which takes 3 arguments:

  - M - Number of partitions between time 0 and time T
  - X - Strike price
  - S_max - The maximum strike price, such that the value of the option is
  essentially 0

create_BS_b() aims to create an initial vector b, to solve Ax = b. The matrix
is of the form:

f_0,m
[
f_(1, m+1) + k/2(theta^2 - r)X
f_(2, m+1)
f_(3, m+1)
...
f_(N-1, m+1)
]
f_N,m

f_0,m = S_max
f_N,m = 0

f_(n,m) = max{X-nh, 0} where h = S_max / N

Returns the intial array b based on inputs.

Requirements: numpy

"""

import numpy as np

def create_BS_b(M, X, S_max, k, theta, r):
    # Set matrix partition as the division of S_max over M intervals
    h = S_max / M

    # Initialize b
    b = []

    # For values of b from 0 to M:
    for n in range(M):
        # For the first iteration:
        if n == 0:
            # Append the option value to the list
            b.append((X - (n + 1) * h) + k/2 * (theta ** 2 - r) * X)
        # If the value of the option is positive:
        elif X - (n+1) * h > 0:
            # Append the option value to the list
            b.append(X - (n+1) * h)
        # If the option value is 0 or negative
        else:
            # Append 0
            b.append(0)

    # Convert to the vector to a numpy arrays
    b = np.array(b)

    # Return b
    return b