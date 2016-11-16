from scipy.linalg import eigvals
import numpy as np
from scipy.sparse import csr_matrix

def condition(row, col, vals, n):
    m = csr_matrix((vals, (row, col)), shape=(n, n)).todense()
    all_eigenvalues=eigvals(m)
    max_eigenvalue = abs(max(all_eigenvalues))
    min_eigenvalue = abs(min(all_eigenvalues))
    relative_condition = max_eigenvalue/min_eigenvalue
    return relative_condition

# # example inputs and output
# row = np.array([0,0,1,2,2,2])
# col = np.array([0,2,1,0,1,2])
# data = np.array([1,2,3,4,5,6])
# row=row.astype(float)
# col=col.astype(float)
# data=data.astype(float)
# n=3
# print(condition(row,col,data,n))