"""

bsm.py

This module contains 1 function, main(), which takes no inputs.

main() is a wrapper function to implement the Black-Scholes matrix for a
given set of inputs.

The function defines the region to solve the PDE by gaining a number of
inputs from the user. These include:

  - S - Stock price today
  - X - Strike price of the opn.
  - T - Time until maturity (days)
  - sigma - The expected volatility over the interval.
  - r - The risk free interest rate.

There are two independent variables, S (stock price) and t (time), so this is
a region in R^2. The value of f(S,t) can be graphed along a third (vertical)
axis. This is what the function aims to solve.

We let S_max be a stock price sufficiently high that the option value f() is
effectively 0 when S = S_max.

Then we get a rectangular region [0,S_max] x [0,T] in R^2 which we must solve
for f

We divide the interval [0, S_max] into N equal subintervals of length h,
defining a spatial grid {S_n}^N_n=0 in the S-direction by:

S_0 = 0
S_n = nh = S_(n-1) + h, 1 <= n <= N-1

We divide the interval [0, T] into M equal subintervals (timesteps) of length
k, restricting our attention to uniform time intervals.

t_m = mk = t_(m-1)+k, m = 0,1,2,...,M

This gives a two-dimensional grid:

   <h>
T _ _ _ _ _ _ _
 |            _
3|            k
2|            _
1|_ _ _ _ _ _ _
  1 2 3 4     S_max

We denote the approximate solution at grid point (S_n, t_m) = (nh, mk) by:

f_(n,m) = f(nh, mk)

The result x represents the value of f(S, t), the option price given a stock
price and time away from T.

However, we can't solve at a given timestamp until we have relations among
all the f_(n,m) for that timestamp: then we get a system of algebraic
equations in the unknowns f_(n,m) where m is fixed and 0 <= n <= N.

There is a slight complication, as we know the option value at maturity date
(t=T) but not today (t=0), so we start at t = T and work backwards to 0 in
the time dimension, so a backward t difference is actually a negative forward
difference.

The function creates the Black-Scholes matrix for the given inputs, and the
initial (final) b vector.

So we use SOR to solve this for all the f values of f_(n, M-1) so can find the
values f_(n, M-2) for the M-2 timestep, and use these to solve for the M-3
timestep and so on until the timestep 0 is solved.

The function then uses today's stock price to find the appropriate value of
the option today, and returns this to the user. An output file is also created.

Requirements: numpy, math, solve_sor, create_BS_matrix, create_BS_b,
get_bsm_inputs, output_bsm

"""

try:
    import numpy as np
    import math
    from sor_modules import solve_sor
    from bsm_modules import create_BS_matrix, create_BS_b, get_bsm_inputs, \
        output_bsm
    import matplotlib.pyplot as plt
except ImportError as import_err:
    print(import_err)
    print("Unable to import required libraries. Please check installation of "
          "numpy and math libraries for python 3.5")
    exit(0)

def main():

    # Define inital conditions
    s, X, T, sigma, r = get_bsm_inputs.get_bsm_inputs()

    if max([X, s]) < 50:
        S_max = min([100, max([20, 10 * max([X, s])])])
    else:
        S_max = max([100, 10 * max([X, s])])

    maxits = 300 # Maximum iterations
    e = np.finfo(float).eps # Machine Epsilon
    w = 1.3 # Relaxation factor
    tol = 1 * 10 ** (-10) # X sequence tolerance

    # Define spacing conditions
    M = 100 # Number of time steps
    N = 300 # Number of price steps
    k = T / M # Time Step distance
    h = S_max / N

    # Create Black-Scholes matrix in CSR format
    val, col, rowStart = create_BS_matrix.create_BS_matrix(N, k, r, sigma)
    # Set matrix size
    n = rowStart.size - 1

    # Create initial vector b, f_n,M
    b = create_BS_b.create_BS_b(N, X, h, k, sigma, r)

    # Create optimized initial vector x
    x = np.random.rand(n)

    # Iterate through each timestamp from M-1 to 0
    for m in range(M - 1, -1, -1):
        b[0] += k / 2 * (sigma ** 2 - r) * X
        b = solve_sor.sor(val, col, rowStart, b, n, maxits, w, x, e, tol)[0]

    option_val = b[int(N - round(s / (S_max / N), 0) - 1)]

    print("Option value for given inputs is $%.2f" % (option_val))
    print("Output file written to bsm_solution.out")

    output_bsm.output_bsm("bsm_solution.out", option_val, s, X, T, sigma, r)

if __name__ == "__main__":
    main()