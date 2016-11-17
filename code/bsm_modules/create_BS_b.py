"""
create_BS_b.py

This module contains 1 function, create_BS_b(), which takes 3 arguments:

  - M - Number of partitions between time 0 and time T
  - X - Strike price
  - S_max - The maximum strike price, such that the value of the option is
  essentially 0

create_BS_b() aims to create an initial vector b, to solve Ax = b.

The boundary conditions determine the f_(0,m) and the f_(N, m) while the
'initial' (actually a final condition) determines f_(n, M). The problem is
then to find the f_(n, m) for:
    0 <= m < M (ie 0 <= t < T) and
    0 < n < N (ie 0 < S < S_max)

Looking at the final condition first, the value of the put option at time T is:

            max{X-S_T, 0} where S_T is the stock price at time T.

This gives:

                    f_(n,M) = {X - nh, 0}, n = 0,1,...,N

The value of the put option when S = 0 is just the strike price X, giving:

                        f_(0,m) = X, m=0,1,...,M

and the value of the put option is 0 when S = S_max

                    f_(N,m) = 0, m = 0,1,...,M

The vector is then of the form:

f_0,m
[
f_(1, m+1) + k/2(sigma^2 - r)X
f_(2, m+1)
f_(3, m+1)
...
f_(N-1, m+1)
]
f_N,m

f_0,m = S_max
f_N,m = 0

f_(n,m) = max{X-nh, 0} where h = S_max / N

Returns the initial array b based on inputs.

Requirements: numpy

"""

import numpy as np

def create_BS_b(N, X, h, k, sigma, r):
    # Set matrix partition as the division of S_max over M intervals

    # Initialize b
    b = []

    # For values of b from 0 to N:
    for n in range(1,N):
        # For the first iteration:
        if (X - (n + 1) * h) > 0:
            # Append the option value to the list
            b.append(X - n * h)

        # If the option value is 0 or negative
        else:
            # Append 0
            b.append(0)

    # Convert to the vector to a numpy arrays
    b = np.array(b)

    # Return b
    return b