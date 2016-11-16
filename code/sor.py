"""
sor.py

This module contains 1 function, main(), which takes no inputs.

main() is a wrapper function to implement the Sparse-Successive Over
Relaxation for solving a system of linear equations in n unknowns.

Ax = b

with A a nxn matrix in R (reals) and x, b n x 1 vectors in R.

main() retrieves file names from the command line or user, and imports the
file data, reformatting it to CSR format if necessary (from dense or .mtx
formats). A series of error checks are conducted, returning faults to the
user for them to fix.

If there are no formatting or value errors (zeros on the diagonal or the
matrix is not strictly row or column diagonally dominant), a number of
parameters are set and the system of linear equations solved using Successive
Over Relaxation.

Outputs are printed in a text file, the name of which is provided by the user.

Requirements: numpy, sys
"""

try:
    import numpy as np
    import sys
    from sor_modules import get_filename, raw_input_check, read_inputs, \
        input_checks, convert_to_csr, value_checks, solve_sor, vector_norm, \
        calculate_residual, write_output, print_errors
except ImportError as import_err:
    print(import_err)
    print("Unable to import required libraries. Please check installation of "
          "sys, numpy, os, scipy.io & re libraries for python 3.5")
    exit(0)


def main():
    # Get input and outfile file names from command line arguments or the
    # user and check files exist
    input_filename, output_filename = get_filename.check_CM_args(sys.argv)

    # Check for any non-decimal entries in the input file
    if input_filename[-4:] != '.mtx' and raw_input_check.read_raw_inputs(\
            input_filename, output_filename):
        write_output.output_text_file(output_filename, "Cannot Proceed")
        exit("There is a non-decimal entry in the input file. Please amend "
             "the input according to the guidelines in README.md")

    # Read val, col and rowStart vectors from the specified filename
    val, col, rowStart, vector_b = read_inputs.read_inputs(
                                        input_filename, output_filename)

    # Initialize empty errors list
    errors = []

    # Add top level formatting errors to errors list
    errors.extend(input_checks.csr_input_checks(val, col, rowStart, vector_b))

    # Return errors
    if len(errors) != 0:
        write_output.output_text_file(output_filename, "Cannot Proceed")
        print_errors.print_errors(errors)

    # Add complex value checks to the errors list
    value_checks.value_tests(val, col, rowStart, errors, output_filename)

    # Set Tolerance
    tol = 1 * 10 ** (-10)

    # Calculate n based on size of input matrix
    n = rowStart.size - 1

    # Set number of maximum iterations
    maxits = 100

    # Set initial relaxation factor
    #w = 1.3

    # Create initial vector x (if required)
    x = solve_sor.create_initial_x(val, col, rowStart, vector_b, n)
    # Set Machine Epsilon based on computer specifications
    e = np.finfo(float).eps

    w = solve_sor.choose_w(val, col, rowStart, vector_b, n, x, e, tol, output_filename)

    # Solve matrixing using Successive Over Relaxation
    x, stop, maxits, iterations, xseqtol, residual = \
    solve_sor.sor(val, col, rowStart, vector_b, n, maxits, w, x, e, tol)

    # Output results to specified output file
    write_output.output_text_file(output_filename, stop, maxits, iterations,
                                  e, xseqtol, residual ,w, x)


if __name__ == '__main__':
    main()