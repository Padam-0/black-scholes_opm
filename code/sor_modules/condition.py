from scipy.linalg import eigvals
import numpy as np
from scipy.sparse import csr_matrix

def condition(m, n):
    all_eigenvalues=eigvals(m)
    max_eigenvalue = abs(max(all_eigenvalues))
    min_eigenvalue = abs(min(all_eigenvalues))
    relative_condition = max_eigenvalue/min_eigenvalue
    return relative_condition

def create_dense(row, col, vals, n):
        m = csr_matrix((vals, (row, col)), shape=(n, n)).todense()
        return m
m= np.array([[ 0.01513653,  0.91844431],[ 0.47155416,  0.32966512]])
#not_diag_dom_evls_less_than_one3.in, condition = 2.69149789298
m=np.array([[0.07632839, 0.61860076],[0.59402266, 0.51434347]])
print(condition(m,2))
# # example inputs and output
# row = np.array([0,0,1,2,2,2])
# col = np.array([0,2,1,0,1,2])
# data = np.array([1,2,3,4,5,6])
# row=row.astype(float)
# col=col.astype(float)
# data=data.astype(float)
# n=3
# print(condition(row,col,data,n))