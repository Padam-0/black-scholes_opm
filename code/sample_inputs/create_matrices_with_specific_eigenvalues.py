from scipy.linalg import eigvals
import numpy as np
from scipy.sparse import csr_matrix

def create_test_matrix(value, A=None):
    if value == "less than":
        if A is None:
            for i in range(500):
                A = np.random.rand(2,2)
                if eigenvalues_less_than(A)==True and not_diag_dom(A)==True:
                    return "less than", eigenvalues_less_than(A), not_diag_dom(A), A
        else:
            if eigenvalues_less_than(A) == True and not_diag_dom(A) == True:
                return "less than", eigenvalues_less_than(A), not_diag_dom(A)
            else:
                return "less than", False
    else:
        if A is None:
            for i in range(500):
                A = np.random.rand(2,2)
                if eigenvalues_greater_than(A)==True and not_diag_dom(A)==True:
                    return "greater than", eigenvalues_greater_than(A), not_diag_dom(A), A
        else:
            if eigenvalues_greater_than(A) == True and not_diag_dom(A) == True:
                return "greater than", eigenvalues_greater_than(A), not_diag_dom(A)
            else:
                return "greater than", False
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
def eigenvalues_greater_than(A):
    toggle = False
    all_eigenvalues = eigvals(A)
    l = list(all_eigenvalues)
    for item in l:
        # if an eigenvalue is less than 1
        if abs(item) > 1:
            toggle = True
    #False means the matrix isn't right, True means the matrix is right
    return toggle
def not_diag_dom(A):
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
    if np.greater_equal(diag, col).any() or \
               np.greater_equal(diag, row).any():
        return False #diag dom
    else:
        return True #not diag dom

# A=np.array([[2, 5],[5 ,2]])
# A=np.array([[0.6787815, 0.88149846],[0.824858, 0.48882749]])
# A=np.array([[ 0.08479672,  0.88982317],[ 0.37376882,  0.05942828]])

print(create_test_matrix("less than"))

# print(not_diag_dom(A))
# all_eigenvalues = eigvals(A)
# l = list(all_eigenvalues)
# print(l)
# for item in l:
#     if abs(item)>1:
#         print("greater than", abs(item))
#     else:
#         print("less than", abs(item))
# print(0.6>0.8 or 0.6>0.8)
# print(0.4>0.8 or 0.4>0.8)