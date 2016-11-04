
def output_text_file(output_file_name, stopping_reason, maxit, iterations,
                     mach_e, x_seq_tol, res_tol,w, x):
    f = open(output_file_name, 'w')
    # Output solution_vector_x, stopping_reason, maxits, #_of_iterations,
    # machine_epsilon, x-seq_tolerance, residual, w
    f.write("Stopping reason \t\t Max num of iterations \t Number of "
            "iterations \t Machine epsilon\t\t\tX seq tolerance \t Residual "
            "seq tolerance")
    f.write("\n")
    f.write("%s \t %s \t\t\t\t\t %s \t\t\t\t\t\t %s \t\t\t%s\t\t\t\t %s" %
            (stopping_reason, maxit, iterations, mach_e, x_seq_tol, res_tol))
    f.write("\n")
    f.write(str(x))
    f.close()

