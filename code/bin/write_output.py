"""
write_output.py


"""


def output_text_file(output_file_name, stopping_reason, maxit, iterations,
                     mach_e, x_seq_tol, res_tol,w, x):
    f = open(output_file_name, 'w')
    # Output solution_vector_x, stopping_reason, maxits, #_of_iterations,
    # machine_epsilon, x-seq_tolerance, residual, w
    first_line = ["Stopping Reason", "Maximum Number of Iterations",
                  "Number of Iterations", "Machine Epsilon",
                  "X Sequence Tolerance", "Residual Sequence Tolerance"]

    second_line = [stopping_reason, maxit, iterations, mach_e, x_seq_tol,
                   res_tol]

    spacing = 30

    f.write('| '.join(["%s" % (heading.ljust(spacing)) for heading in
                       first_line]))
    f.write("\n")
    f.write('| '.join(["%s" % (str(value).ljust(spacing)) for value in
                       second_line]))
    f.write("\n")
    f.write(str(x))
    f.close()

