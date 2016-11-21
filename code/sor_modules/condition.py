"""
condition.py

This module contains two functions condition() and create dense.

condition() takes 2 arguments. These are:

    - m - A dense format matrix and
    - n - the size of the matrix.

condition() calculates the relative condition of the matrix m. It does this by
finding all of m's eigenvalues and then dividing the absolut value of largest by
the smallest.

A single number is returned, the relative condition of m.

create_dense() takes 4 arguments. These are:

  - val - A 1 dimensional numpy array containing the input matrix (A) values in
CRS format.
  - col - A 1 dimensional numpy array containing the column references for the
input matrix (A) entries in val.
  - rowStart - A 1 dimensional numpy array containing the reference indices for
the beginning of each new row of the the input matrix (A).
  - n - an integer the size of matrix to be created.

create_dense() creates a dense matrix from a matrix in CSR format to be used in
condition().

The function will return a matrix in dense form.
"""

from scipy.linalg import eigvals
import numpy as np
from scipy.sparse import csr_matrix
import numpy as np

def condition(m, n):
    all_eigenvalues=eigvals(m)
    max_eigenvalue = abs(max(all_eigenvalues))
    min_eigenvalue = abs(min(all_eigenvalues))
    relative_condition = max_eigenvalue/min_eigenvalue
    return relative_condition

def create_dense(row, col, vals, n):
    # m = csr_matrix((vals, (row, col)), shape=(n, n)).todense()
    m_out = csr_matrix((vals, col, row), shape=(n, n)).todense()
    return m_out