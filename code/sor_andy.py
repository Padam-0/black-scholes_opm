"""
Write a program to implement the Spare-SOR algorithm for solving a system of n
linear equations in n unknowns.
Ax = b
with A a nxn matrix in R and x, b nx1 vectors in R
"""

import numpy as np

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

def con_to_csr(matrix, matrix_length):
    # Convert an numpy array to CSR Structure
    val = np.ndarray.flatten(matrix)
    col = []
    rowStart = []
    pos = 0
    zeros = 0
    for entry in np.nditer(matrix):
        if entry != 0:
            col.append((pos) % matrix_length)
            if pos % matrix_length == 0:
                rowStart.append(pos - zeros)
        else:
            zeros += 1
        pos += 1
    rowStart.append(len(col))

    val = [i for i in val if i != 0]
    col = np.asarray(col)
    rowStart = np.asarray(rowStart)

    return val, col, rowStart


def write_outputs(solution_vector, stopping_reason, other_information):
    pass


def calc_vector_norms(vector):
    pass


def zero_diag(val, col, rowStart):
    # Check if there are 0's on the diagonal of the input matrix

    row = 0
    tf = True
    for i in range(len(rowStart)-1):
        r = col[rowStart[i]:rowStart[i+1]]
        if row not in r:
            tf = False
        row += 1

    return tf


def diag_dominant(val, col, rowStart):
    # Check if the diagonal value is larger than the sum of all
    # other entries in that row/column

    diags = []
    col_sums = []
    row_sums = []
    for i in range(len(rowStart) - 1):
        # 0 through 2
        r = col[rowStart[i]:rowStart[i + 1]]

        if i in r:
            diags.append(val[rowStart[i] + int(np.where(r == i)[0])])

        c_sum = 0
        for j in range(len(col)):
            if col[j] == i:
                c_sum += val[j]
        col_sums.append(c_sum)

        row_sums.append(sum(val[rowStart[i]:rowStart[i + 1]]))

    diags = np.asarray(diags)
    col_sums = np.asarray(col_sums) - diags
    row_sums = np.asarray(row_sums) - diags

    if np.greater(diags, col_sums).all() and np.greater(diags,row_sums).all():
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
    matrix_size, matrix_in, vector_b = read_inputs('nas_Sor.in')
    val, col, rowStart = con_to_csr(matrix_in, matrix_size)

    print(val)
    print(col)
    print(rowStart)

    """
    zd = zero_diag(val, col, rowStart)
    dd = col_diag_dominant(val, col, rowStart)

    if zd != True and dd != True:
        exit()
    """



if __name__=='__main__':
    main()