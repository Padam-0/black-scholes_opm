"""
Write a program to implement the Spare-SOR algorithm for solving a system of n
linear equations in n unknowns.
Ax = b
with A a nxn matrix in R and x, b nx1 vectors in R
"""

def read_inputs(filename):
    pass


def write_outputs(solution_vector, stopping_reason, other_information):
    pass


def calc_vector_norms(vector):
    pass


def main():
    # Read input file containing A and b
    A = read_inputs('nas_Sor.in')

    # Solve (if possible) Ax = b
    """
    Check if:
        There are no zeros on the diagonal
        If the matrix is strictly row or column diagonally dominant
            C := -(D + L)^-1 * U has spectral radius r(C)<1
        Check for divergence (cycling or ||x^(k)-x^(k-1)||

    """
    if zero_diag(A):
        # There are 0's on the diagonal, so quit
        exit(0)
    elif s_diag_dominant(A) == False:
        # Matrix isn't diagonally dominant, so quit
        exit(0)
    elif divergence(A):
        # The matrix divergences, so quit
        exit(0)
    else:
        solve_matrix(A)







    # write computed solution vector x, reason for stopping
    # and other information
    write_outputs(sol_vector, stop_r, other_inf)


if name == "__main__":
    main()