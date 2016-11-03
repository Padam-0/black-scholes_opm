import SOR_solve_kron
import numpy as np

def output_text_file(output_file_name, stopping_reason, maxit, iterations, mach_e, x_seq_tol, res_tol,w):
    f = open(output_file_name, 'w')
    f.write("Stopping reason \t\t Max num of iterations \t Number of iterations \t Machine epsilon\t\t\tX seq tolerance \t Residual seq tolerance")
    f.write("\n")
    f.write("%s \t %s \t\t\t\t\t %s \t\t\t\t\t\t %s \t\t\t%s\t\t\t\t %s"%(stopping_reason, maxit, iterations, mach_e, x_seq_tol, res_tol))
    f.write("\n")
    f.write(str(x))
    f.close()

val = np.array([1.,2.,3.])
col = np.array([0.,1.,2.])
rowstart = np.array([0., 1., 2., 3.])
b = np.array([1., 2., 13.])
x = np.array([1., 1., 1.])
n = 3
maxits = 50
tol = 1*10**-6
A = np.array([[1,0,0],[0,2,0],[0,0,3]])
w = 1.22
# print(solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol))
# w = 1.3
# print(solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol))
# w = 1.4
# print(solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol))

#  return solution_vector_x, stopping_reason, maxits, #_of_iterations, machine_epsilon, x-seq_tolerance, residual, w
vec_x, stop, maxits, iterations, mach_e, xseqtol, residual, w =SOR_solve_kron.solve_axb_with_best_w(val, col, rowstart, b, n, maxits, w, x, A, tol)
# outp = SOR_solve_kron.solve_axb_with_best_w(val, col, rowstart, b, n, maxits, w, x, A, tol)


output_text_file("output.txt", stop,maxits, iterations, mach_e, xseqtol, residual, w)
