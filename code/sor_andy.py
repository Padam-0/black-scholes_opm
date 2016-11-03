"""
Write a program to implement the Spare-SOR algorithm for solving a system of n
linear equations in n unknowns.
Ax = b
with A a nxn matrix in R and x, b nx1 vectors in R
"""

from bin import sor
import sys
import os
import numpy as np


def divergence(matrix):
    pass
    # Check for divergence in successive matrix norms

    # I think this actually needs to go inside solve_matrix()
    # but I'll leave it here for now


def solve_matrix(A):
    pass
    # Check for cycling

    # Define maxits?

    # Stop when maxits reached


def main():
    input_filename, output_filename = sor.check_CM_args(sys.argv)
    if not sor.read_raw_inputs(input_filename):
        exit("There is a non-decimal entry in the input file. Please amend "
              "the input according to the guidelines in README.md")

    errors = []

    if sor.read_inputs(input_filename)[0] == "Dense":
        matrix_size, matrix_in, vector_b = sor.read_inputs(input_filename)[1:]

        errors.extend(sor.dense_input_tests(matrix_size, matrix_in, vector_b))

        val, col, rowStart = sor.con_to_csr(matrix_in, matrix_size)
    else:
        val, col, rowStart, vector_b = sor.read_inputs(input_filename)[1:]

        errors.extend(sor.csr_input_tests(val, col, rowStart, vector_b))

    errors.extend(sor.value_tests(val, col, rowStart, errors))

    if len(errors) != 0:
        print("The following errors were identified:")
        for i in errors:
            print(i)
        print("Please correct these errors and restart the program")
        exit()

    tol = 1 * 10 ** (-10)
    n = rowStart.size - 1
    print(n)
    maxits = 100
    x = np.random.randn(n)
    #A = original matrix, get rid of this when have resid in CSR sorted
    #solve_axb(val, col, rowStart, vector_b, n, maxits, w, x, A, tol)

if __name__=='__main__':
    main()