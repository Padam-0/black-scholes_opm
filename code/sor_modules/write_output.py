"""
write_output.py

This module contains 1 function, output_text_file(), which takes 9 inputs:

  - output_file_name - A string containing the file to write to.
  - stopping_reason - A string of the reason why the iterations stopped.
  - maxits - Maximum integer of iterations allowed.
  - iterations - Integer of iterations performed.
  - mach_e - Machine Epsilon, float, calculated based on the users operating
system.
  - x_seq_tol - X Sequence tolerance allowed, float.
  - res_tol - Residual test tolerance allowed, float.
  - w - Relaxation factor, float.
  - x - The solution vector x containing n floats, solved using SOR for the
  given input matrix A (n x n) and vector b, Ax = b.

output_text_file() outputs the results of SOR into a text file with a
user-specified name.

Requirements: None

"""


def output_text_file(output_file_name, stopping_reason, maxits, iterations,
                     mach_e, x_seq_tol, res_tol, w, x):

    with open(output_file_name, 'w') as f:
        # Output solution_vector_x, stopping_reason, maxits, #_of_iterations,
        # machine_epsilon, x-seq_tolerance, residual, w

        # Create headings list, along with spacings
        headings = [["Stopping Reason", 24],
                      ["Maximum Number of Iterations", 30],
                      ["Number of Iterations", 22], ["Machine Epsilon", 22],
                      ["X Sequence Tolerance", 22],
                      ["Residual Sequence Tolerance", 30]]

        # Create values list, along with spacings
        values = [[stopping_reason, 24],
                      [maxits, 30],
                      [iterations, 22], [mach_e, 22],
                      [x_seq_tol, 22],
                      [res_tol, 30]]

        # Output headings
        f.write('| '.join(["%s" % (heading[0].ljust(heading[1])) for heading in
                           headings]))
        f.write("\n")
        # Output values from second_line
        f.write('| '.join(["%s" % (str(value[0]).ljust(value[1])) for value in
                           values]))

        # If convergence, print x
        if stopping_reason != "Divergence":
            f.write("\n")
            f.write(' '.join(["%s" % (str(value)) for value in x]))


