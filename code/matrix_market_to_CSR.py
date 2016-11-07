import scipy.io
import numpy as np
def mm_to_CSR(file1):
    A = scipy.io.mmread(file1)
    size = A.shape[0]
    for i in range(size):
        b = np.random.randint(-100, 100, size=(size))
    A = A.tocsr()
    value = A.data
    column_index = A.indices
    row_pointers = A.indptr
    return value, column_index, row_pointers, b
val1, col1, row1, b = mm_to_CSR("s3dkt3m2.mtx")