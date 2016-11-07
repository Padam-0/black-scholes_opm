"""
write_output.py

This module contains
"""


def output_text_file(output_file_name, stopping_reason, maxit, iterations,
                     mach_e, x_seq_tol, res_tol,w, x):

    with open(output_file_name, 'w') as f:
        # Output solution_vector_x, stopping_reason, maxits, #_of_iterations,
        # machine_epsilon, x-seq_tolerance, residual, w
        first_line = [["Stopping Reason", 24],
                      ["Maximum Number of Iterations", 30],
                      ["Number of Iterations", 22], ["Machine Epsilon", 22],
                      ["X Sequence Tolerance", 22],
                      ["Residual Sequence Tolerance", 30]]

        second_line = [[stopping_reason, 24],
                      [maxit, 30],
                      [iterations, 22], [mach_e, 22],
                      [x_seq_tol, 22],
                      [res_tol, 30]]

        # Output headings
        f.write('| '.join(["%s" % (heading[0].ljust(heading[1])) for heading in
                           first_line]))
        f.write("\n")
        # Output values from second_line
        f.write('| '.join(["%s" % (str(value[0]).ljust(value[1])) for value in
                           second_line]))

        # If convergence, print x
        if stopping_reason != "Divergence":
            f.write("\n")
            f.write(' '.join(["%s" % (str(value)) for value in x]))