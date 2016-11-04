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
    from bin import get_filename, raw_input_check, read_inputs, input_tests, \
        convert_to_csr, value_tests, solve_sor, vector_norm, \
        calculate_residual, write_output

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

    #errors.extend(value_tests.value_tests(val, col, rowStart, errors))

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

    w = 1.3
    x = solve_sor.create_initial_x(val, col, rowStart, vector_b, n)
    e = np.finfo(float).eps

    x, stop, maxits, iterations, xseqtol, residual = \
    solve_sor.sor(val, col, rowStart, vector_b, n, maxits, w, x, e, tol)

    print(x)

    """
    # outputs
    write_output.output_text_file(output_filename, stop, maxits, iterations,
                                  e, xseqtol, residual ,w, x)
    """

if __name__ == '__main__':
    main()