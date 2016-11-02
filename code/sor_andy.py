"""
Write a program to implement the Spare-SOR algorithm for solving a system of n
linear equations in n unknowns.
Ax = b
with A a nxn matrix in R and x, b nx1 vectors in R
"""

import numpy as np
from con_to_csr import con_to_csr

def read_inputs(filename):

    matrix_size = np.genfromtxt(filename, max_rows=1)
    #print('Matrix size n:',matrix_size)
    #print('----------')

    matrix_in = np.genfromtxt(filename, skip_header=1, skip_footer=1)
    #print('Matrix A:')
    #print(matrix_in)
    #print('----------')

    column = np.genfromtxt(filename, usecols=0)
    col_len = len(column)
    #print('Column length', col_len)
    #print('----------')

    vector_b = np.genfromtxt(filename, skip_header=(col_len-1))
    #print('Vector b: ',vector_b)

    return matrix_size, matrix_in, vector_b


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
    matrix_size, matrix_in, vector_b = read_inputs('nas_Sor2.in')
    print(con_to_csr(matrix_in, matrix_size)[0])
    print(con_to_csr(matrix_in, matrix_size)[1])
    print(con_to_csr(matrix_in, matrix_size)[2])

if __name__=='__main__':
    main()