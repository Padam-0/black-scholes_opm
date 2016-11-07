import numpy as np

def read_inputs(filename):
    # Open a file and extract data
    if np.genfromtxt(filename, max_rows=1).size == 1:
        input_type = "Dense"
        # Open a file and extract data
        matrix_size = np.genfromtxt(filename, max_rows=1)
        try:
            matrix_in = np.genfromtxt(filename, skip_header=1, skip_footer=1)
        except ValueError:
            print(
                "Input matrix is not square. Please ensure that all rows of "
                "the matrix have the same number of entries.")
            exit(0)

        col_len = len(np.genfromtxt(filename, usecols=0))

        vector_b = np.genfromtxt(filename, skip_header=(col_len - 1))

        return input_type, matrix_size, matrix_in, vector_b
    else:
        input_type = "CSR"
        val = np.genfromtxt(filename, max_rows=1)
        col = np.genfromtxt(filename, skip_header=1, skip_footer=2)
        rowStart = np.genfromtxt(filename, skip_header=2, skip_footer=1)
        vector_b = np.genfromtxt(filename, skip_header=3)

        return input_type, val, col, rowStart, vector_b