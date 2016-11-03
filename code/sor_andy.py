"""
Write a program to implement the Spare-SOR algorithm for solving a system of n
linear equations in n unknowns.
Ax = b
with A a nxn matrix in R and x, b nx1 vectors in R
"""

from bin import sor
import sys
import os


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

    #input_filename, output_filename = sor.check_CM_args(sys.argv)

    #matrix_size, matrix_in, vector_b = sor.read_inputs(input_filename)

    """
    val, col, rowStart = sor.con_to_csr(matrix_in, matrix_size)

    sor.matrix_det(matrix_in)

    zd = sor.zero_diag(val, col, rowStart)
    dd = sor.col_diag_dominant(val, col, rowStart)

    if zd != True and dd != True:
        exit()
    """


if __name__=='__main__':
    main()