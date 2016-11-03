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
    errors = []

    if sor.read_inputs(input_filename)[0] == "Dense":
        matrix_size, matrix_in, vector_b = sor.read_inputs(input_filename)[1:]
        input_test_res, t_errors = sor.dense_input_tests(matrix_size,
                                    matrix_in, vector_b)
        val, col, rowStart = sor.con_to_csr(matrix_in, matrix_size)
    else:
        val, col, rowStart, vector_b = sor.read_inputs(input_filename)[1:]
        input_test_res, t_errors = sor.csr_input_tests(val, col, rowStart,
                                                   vector_b)

    if not input_test_res:
        errors.extend(t_errors)
    if not sor.zero_diag(val, col, rowStart):
        errors.append("There are zeros on the diagonal")
    if not sor.col_diag_dominant(val, col, rowStart):
        errors.append("The matrix is not row and column diagonally dominant")

    if len(errors) != 0:
        print("The following errors were identified:")
        for i in errors:
            print(i)
        print("Please correct these errors and restart the program")
        exit()

if __name__=='__main__':
    main()