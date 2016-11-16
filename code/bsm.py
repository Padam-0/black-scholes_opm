"""
We start by defining the region in which we want to solve the PDE. There are
two independent variables, S (stock price) and t (time), so this is a region
in R^2. The value of f(S,t) can be graphed along a third (vertical) axis.

The maturity date of the option is T
The strike price (price of option at time T) is X

Let S_max be a stock price sufficiently high that the option value f() is
effectively 0 when S=S_max (In particular, S_max > X)

Then we get a rectangular region [0,S_max] x [0,T] in R^2 which we must solve
for f

We divide the interval [0, S_max] into N equal subintervals of length h,
defining a spatial grid {S_n}^N_n=0 in the S-direction by:

S_0 = 0
S_n = nh = S_(n-1) + h, 1 <= n <= N-1, S_N = S_max

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

This gives:

f_(n, m+1) = -nk/2(n*sigma^2-r) * f_(n-1,m)
    + (1 + kr + k * sigma^2 * n^2)* f_(n,m)
    - nk/2(n* sigma^2 + r) * f_(n+1, m)

This represents 4 grid points, and as the value of f_(n, m+1) is known,
the others represent a system of linear equations.

We solve the difference equations (above) for 0 < n < N and 0 < m <= M.

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
As assumed earlier, the value of the put option is 0 when S = S_max
    f_(N,m) = 0, m = 0,1,...,M

These define the value of the option along the three edges of our grid
(where S = 0 (LH vertical), S = S_max (RH vertical), and t = T (top horizontal)
and allow us to start

We first form a system of linear equations for the timestep m = M - 1 and solve
the resulting equation Af = b. This gives:

f_(n, M) = -nk/2(n*sigma^2-r) * f_(n-1,M-1)
    + (1 + kr + k * sigma^2 * n^2)* f_(n,M-1)
    - nk/2(n* sigma^2 + r) * f_(n+1, M-1)

for n = 1,...,N-1, and we know all the numbers on the RHS from the boundary
conditions and 'final' condition when t = T so we can solve this

(also have f_(n-1, M-1) = f_(0, M-1) for n = 1 and
    f_(n+1, M-1) = f_(N, M-1) for n = N-1

So we solve this for all the f values of f_(n, M-1) so can find the values
f_(n, M-2) for the M-2 timestep, and use these to solve for the M-3 timestep
and so on until the timestep 0 is solved.




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
    s, X, T, sigma, r, = get_bsm_inputs.get_bsm_inputs()

    S_max = min([100, 10 * max(X, s)])

    maxits = 300 # Maximum iterations
    e = np.finfo(float).eps # Machine Epsilon
    w = 1.3 # Relaxation factor
    tol = 1 * 10 ** (-10) # X sequence tolerance

    # Define spacing conditions
    M = 300 # Number of time steps
    N = 300
    k = T / M # Time Step distance
    h = S_max / N

    # Create Black-Scholes matrix in CSR format
    val, col, rowStart = create_BS_matrix.create_BS_matrix(N, k, r, sigma)
    # Set matrix size
    n = rowStart.size - 1

    # Create initial vector b, f_n,M
    b = create_BS_b.create_BS_b(N, X, h, k, sigma, r)

    # Create optimized initial vector x
    x = solve_sor.create_initial_x(val, col, rowStart, b, n)

    # Iterate through each timestamp from M-1 to 0
    for m in range(M - 1, -1, -1):
        b[0] += k / 2 * (sigma ** 2 - r) * X
        b = solve_sor.sor(val, col, rowStart, b, n, maxits, w, x, e, tol)[0]

    option_val = b[int(N - round(s / (S_max / N), 0) - 1)]

    print("Option value for given inputs is $%s" % (str(option_val)))
    print("Output file written to bsm_solution.out")

    output_bsm.output_bsm("bsm_solution.out", option_val, s, X, T, sigma, r)

if __name__ == "__main__":
    main()