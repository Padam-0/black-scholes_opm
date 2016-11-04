"""
Write a program to implement the Spare-SOR algorithm for solving a system of n
linear equations in n unknowns.
Ax = b
with A a nxn matrix in R and x, b nx1 vectors in R
"""

try:
    import numpy as np
    import sys
    import os.path
    import re
    import math
    from bin import *
except ImportError as import_err:
    print(import_err)
    print("Unable to import required libraries. Please check installation of "
          "sys, numpy, os & re libraries for python 3.5")
    exit(0)


def main():
    input_filename, output_filename = get_filename.check_CM_args(sys.argv)

    if not raw_input_check.read_raw_inputs(input_filename):
        exit("There is a non-decimal entry in the input file. Please amend "
             "the input according to the guidelines in README.md")

    errors = []

    if read_inputs.read_inputs(input_filename)[0] == "Dense":
        matrix_size, matrix_in, vector_b = read_inputs.read_inputs(
            input_filename)[1:]

        errors.extend(input_tests.dense_input_test(matrix_size, matrix_in,
                                               vector_b))

        val, col, rowStart = convert_to_csr.con_to_csr(matrix_in, matrix_size)
    else:
        val, col, rowStart, vector_b = read_inputs.read_inputs(
            input_filename)[1:]

        errors.extend(input_tests.csr_input_tests(val, col, rowStart, vector_b))

    errors.extend(matrix_value_tests.value_tests(val, col, rowStart, errors))

    if len(errors) != 0:
        print("The following errors were identified:")
        for i in errors:
            print(i)
        exit("Please correct these errors and restart the program")

    # Set tolerance
    tol = 1 * 10 ** (-10)

    # Calculate n
    n = rowStart.size - 1

    # Set maximum iterations
    maxits = 100

    # x = np.random.randn(n)
    x = np.array([1, 2, 3])
    w = 1.3

    # A = original matrix, get rid of this when have resid in CSR sorted
    # solve_axb(val, col, rowStart, vector_b, n, maxits, w, x, A, tol)

    residual = calculate_residual.calc_csr_residual(val, col, rowStart,
                                                 vector_b, x)
    # outputs
    A = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
    vec_x, stop, maxits, iterations, mach_e, xseqtol, residual, w = \
        solve_sor.solve_axb_with_best_w(val, col, rowStart, vector_b, n,
                                             maxits, w, x, A, tol)

    write_output.output_text_file("output.txt", stop, maxits, iterations,
                                  mach_e,
                            xseqtol, residual, w)


if __name__ == '__main__':
    main()