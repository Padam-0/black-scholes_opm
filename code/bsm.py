"""
We start by defining the region in which we want to solve teh PDE. There are
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


"""