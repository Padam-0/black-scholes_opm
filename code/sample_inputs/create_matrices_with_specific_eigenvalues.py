from scipy.linalg import eigvals
import numpy as np
from scipy.sparse import csr_matrix

def create_test_matrix(A=None):
    if A is None:
        for i in range(500):
            A = np.random.rand(3,3)
            if eigenvalues_less_than(A)==True and diag_dom(A)==True:
                return eigenvalues_less_than(A), diag_dom(A), A
    else:
        if eigenvalues_less_than(A) == True and diag_dom(A) == True:
            return eigenvalues_less_than(A), diag_dom(A)
        else:
            return False
def eigenvalues_less_than(A):
    toggle = True
    all_eigenvalues = eigvals(A)
    l = list(all_eigenvalues)
    for item in l:
        # if an eigenvalue is greater than one break
        if abs(item) >= 1:
            toggle = False
    #False means the matrix isn't right, True means the matrix is right
    return toggle
def diag_dom(A):
    diag = []
    col = []
    row = []
    for i in range(A.shape[0]):
        col.append([])
        row.append([])
    for i in range(A.shape[0]):
        for j in range(A.shape[0]):
            elem = A[i][j]
            if i==j:
                diag.append(elem)
            else:
                row[i].append(elem)
                col[j].append(elem)
    colsum=[]
    rowsum=[]
    for i in range(len(col)):
        colsum.append(sum(col[i]))
        rowsum.append(sum(row[i]))
    diag = np.array(diag)
    col = np.array(colsum)
    row = np.array(rowsum)
    if np.greater(diag, colsum).all() and \
               np.greater(diag, rowsum).all():
        return True #diag dom
    else:
        return False

A=np.array([[.7 , .21],[.32, .39]])
# [ 0.68283148,  0.28007863,  0.10298043],
#        [ 0.13572267,  0.75639731,  0.18839798],
#        [ 0.02094409,  0.06355872,  0.53039456]]
A=np.array([[ 0.6,  0.2,  0.1],[ 0.1,  0.7,  0.1],[ 0.0,  0.0,  0.5]])
print(create_test_matrix(A))