import numpy as np
from sor_modules import get_filename, raw_input_check, read_inputs, \
    input_checks, convert_to_csr, value_checks, solve_sor, vector_norm, \
    calculate_residual, write_output, print_errors
import timeit

def sor(input_filename, output_filename):

    # Check for any non-decimal entries in the input file
    if input_filename[-4:] != '.mtx' and raw_input_check.read_raw_inputs(
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
        exit("The following errors were identified:\n\n" + "\n"
             .join([" -  %s" % (str(value)) for value in errors]) +
             "\n\nPlease correct these errors and restart the program")

    # Add complex value checks to the errors list
    value_checks.value_tests(val, col, rowStart, errors, output_filename)

    # Set Tolerance
    tol = 1 * 10 ** (-10)

    # Calculate n based on size of input matrix
    n = rowStart.size - 1

    # Set number of maximum iterations
    maxits = 100

    # Set initial relaxation factor
    w = 1.3

    # Create initial vector x (if required)
    x = solve_sor.create_initial_x(val, col, rowStart, vector_b, n)
    # Set Machine Epsilon based on computer specifications
    e = np.finfo(float).eps

    #w = solve_sor.choose_w(val, col, rowStart, vector_b, n, x, e, tol,
    #                       output_filename)

    # Solve matrixing using Successive Over Relaxation
    x, stop, maxits, iterations, xseqtol, residual = \
        solve_sor.sor(val, col, rowStart, vector_b, n, maxits, w, x, e, tol)

    # Output results to specified output file
    write_output.output_text_file(output_filename, stop, maxits, iterations,
                                  e, xseqtol, residual, w, x)


def wrapper(func, *args, **kwargs):
    """
    Takes a function and arguments as an input. Returns the time taken to run
    the function.
    """
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def main():
    wrapped = wrapper(sor, 'sample_inputs/large_matrix.in',
                      'sample_inputs/large_matrix.out')
    print(timeit.timeit(wrapped, number=10))