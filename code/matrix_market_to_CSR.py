import scipy.io
def mm_to_CSR(file1):
    A = scipy.io.mmread(file1)
    A = A.tocsr()
    value = A.data
    column_index = A.indices
    row_pointers = A.indptr
    return value, column_index, row_pointers

val1, col1, rowstart1 = mm_to_CSR("s3dkt3m2.mtx")
print(val1[0])