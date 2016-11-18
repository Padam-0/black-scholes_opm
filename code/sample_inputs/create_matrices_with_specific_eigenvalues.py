from scipy.linalg import eigvals
import numpy as np
from scipy.sparse import csr_matrix

def create_test_matrix(value, A=None):
    if value == "less than":
        if A is None:
            for i in range(500):
                A = np.random.rand(2,2)
                A =A*-1
                if not_diag_dom(A)==True:
                    C = find_C(A)
                    if eigenvalues_less_than(C):
                        return "less than", eigenvalues_less_than(C), not_diag_dom(A), A
        else:
            if not_diag_dom(A) == True:
                C = find_C(A)
                if eigenvalues_less_than(C):
                    return "evls less than", eigenvalues_less_than(C), not_diag_dom(A)
                else:
                    return "evls less than", False
            else:
                return "A is diag dom", not_diag_dom(A)
    else:
        if A is None:
            for i in range(500):
                A = np.random.rand(2,2)
                if not_diag_dom(A)==True:
                    C = find_C(A)
                    if eigenvalues_greater_than(C):
                        return "greater than", eigenvalues_greater_than(C), not_diag_dom(A), A
        else:
            if not_diag_dom(A) == True:
                C = find_C(A)
                if eigenvalues_greater_than(C):
                    return "evls less than", eigenvalues_greater_than(C), not_diag_dom(A)
                else:
                    return "evls less than", False
            else:
                return "A is diag dom", not_diag_dom(A)

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
def find_C(A):
    D = np.empty_like(A)
    U = np.empty_like(A)
    L = np.empty_like(A)
    for i in range(A.shape[0]):
        for j in range(A.shape[0]):
            elem = A[i][j]
            if i == j:
                D[i][j] = elem
            else:
                D[i][j]= 0
    for i in range(A.shape[0]):
        for j in range(A.shape[0]):
            elem = A[i][j]
            if i > j:
                U[i][j] = elem
                L[i][j] = 0
            elif i==j:
                U[i][j] = 0
                L[i][j] = 0
            else:
                U[i][j] = 0
                L[i][j] = elem
    inv1 = np.linalg.inv(D+L)
    C = -inv1@U
    return C

less_than_1= np.array([[-0.84095474, -0.14674105],
       [-0.07326811, -0.63363091]])
less_than_2 = np.array([[-0.87525288, -0.4191722 ],
       [-0.05217446, -0.59336394]])
less_than_3 = np.array([[-0.28674648, -0.09610883],
       [-0.15537608, -0.74101286]])
print(create_test_matrix("less than"))
# C = np.array([[ 0.02017705,  0.        ],
#        [-0.11563215,  0.        ]])
# A=np.array([[ 1,  2],[ 3,  4]])
# print(find_C(A))




# A=np.array([[2, 5],[5 ,2]])

# A=np.array([[ 0.08479672,  0.88982317],[ 0.37376882,  0.05942828]])
# A = np.array([[ 0.08,  0.88],[ 0.37,  0.05]])
# D=np.array([[ 0.08,  0.0],[ 0.0,  0.05]])
# L=np.array([[ 0,  0],[ 0.37,  0]])
# U=np.array([[ 0,  0.88],[ 0.0,  0]])
# C=D+L+U
# print(C)
# print(create_test_matrix("less than", A))


# C = - (np.linalg.inv(D+L) * U)
# print(C)
# A= np.array([[1,0],[0,1]])
# B= np.array([[1,0],[0,2]])
# d=A*B
# print(d)

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