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

# m= np.array([[ 0.01513653,  0.91844431],[ 0.47155416,  0.32966512]])
# m=np.array([[1007632839, 0.61860076],[0.59402266, 51.434347]])
# m=np.array([[5., 1., 0., 1.],[0., 4., 0., 0.],[1.,0.,6.,0.],[0.,0.,1.,7.]])

# print(condition(m,2))


# greater_than_1 = np.array([[ 0.32485338,  0.75049587],[ 0.71390588,  0.22020623]])
# C_greater_than_1=np.array([[ 7.48983541,  0.        ], [-3.24198766,  0.        ]])
# greater_than_2 = np.array([[ 0.01124162,  0.90960554],[ 0.7327776 ,  0.10667227]])
# greater_than_3 = np.array([[ 0.13534856,  0.44150804],[ 0.85794161,  0.09988733]])
# print(condition(C_greater_than_1,2))
#
# print(condition(greater_than_1,2))
# print(condition(greater_than_2,2))
# print(condition(greater_than_3,2))




# # example inputs and output
# row = np.array([0,0,1,2,2,2])
# col = np.array([0,2,1,0,1,2])
# data = np.array([1,2,3,4,5,6])
# row=row.astype(float)
# col=col.astype(float)
# data=data.astype(float)
# n=3
# print(condition(row,col,data,n))