"""
solve_sor.py

This module contains one function sor() which takes 10 arguments. These are:

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

sor() solves Ax=b for x when the matrix A is in CSR format. It creates a
while loop which iterates a maximum number of times (equal to maxits),
improving the initial guess for the x-vector each time. After each iteration
the function checks whether there was residual convergence, x-sequence
convergence, or divergence and stops if any of these are true. If after
maxits number of iterations none of these conditions are true then the loop
stops.

The value for w is optimised per iteration depending on the relative rate of
change of the error term.

The function will return:

- the solution vector_x;
- the stopping reason;
- the maximum number of iterations;
- the actual number of iterations;
- machine epsilon;
- the tolerance allowed;
- the current residual; and
- and w, the relaxation factor.


Requirements: calculate_residual, vector_norm, optimise_w

"""

from sor_modules import calculate_residual, vector_norm, optimise_w


def sor(val, col, rowStart, b, n, maxits, w, x, e, tol):

    l = []

    b = b.astype(float)
    x = x.astype(float)
    residual_tolerance = 1 *10**(-10)
    k = 0
    while k <= maxits:
        x1 = x.copy()

        for i in range(0, n):
            sum1 = 0
            for j in range(int(rowStart[i]), int(rowStart[i+1])):
                sum1 = sum1 + val[j] * x[int(col[j])]
                if col[j] == i:  # identify and store diagonal entry
                    d = val[j]
            x[i] = x[i] + w * (b[i] - sum1) / d

        x2 = x #store x(k-1)th vector in x2

        # Calculate residual
        r = calculate_residual.residual(val, col, rowStart, b, x)

        # Calculate change in calculated vector per iteration
        l.append(vector_norm.vectornorm(abs(x1 - x2)))

        # Optimise w
        if len(l) >= 3:
            w = optimise_w.op_w(l, w)

        # Return solution_vector_x, stopping_reason, maxits, #_of_iterations,
        # machine_epsilon, x-seq_tolerance, residual, w

        # Check for residual convergence:
        if r <= residual_tolerance:
            return x, "Residual convergence", maxits, k+1, tol, residual_tolerance

        # Check for x-sequence convergence
        elif vector_norm.vectornorm(abs(x1-x2)) < tol + 4*e:

            return x, "x Sequence Convergence", maxits, k+1, tol, residual_tolerance

        # Check for divergence
        elif k > 0 and l[k]>l[k-1]:

            return x, "Divergence",  maxits, k+1, tol, residual_tolerance

        # Otherwise
        else:
            k += 1
            if k == maxits:
                return x, "Max Iterations Reached", maxits, k, tol, residual_tolerance