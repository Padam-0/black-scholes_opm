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


def zero_diag(matrix):
    # Check if there are 0's on the diagonal of the input matrix

    if some_condition:
        return True
    else:
        return False

def s_diag_dominant(matrix):
    # Check if the diagonal value is larger than the sum of all
    # other entries in that row/column

    if some_condition:
        return True
    else:
        return False

def divergence(matrix):
    # Check for divergence in successive matrix norms

    # I think this actually needs to go inside solve_matrix()
    # but I'll leave it here for now


def solve_matrix(A):
    # Check for cycling

    # Define maxits?

    # Stop when maxits reached


def main():
    # Read input file containing A and b
    # If the user provides an argument to the program, use that as filename
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
        # solve the matrix using SOR
        sol_vector, stop_r, other_inf = solve_matrix(A)


    # write computed solution vector x, reason for stopping
    # and other information
    write_outputs(sol_vector, stop_r, other_inf)


if __name__ == "__main__":
    main()