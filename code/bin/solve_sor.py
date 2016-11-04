# need the value of n (the size of the n*n matrix) stored from previously for this function
# need machine epsilon
# check if diverged: //xk-x(k-1)\\ increasing with each iteration
# ^^ for this, need function to calculate vector norms

import numpy as np
import math



# #input two vectors and epilson to test for x convergence
# def x_convergence(val1,val2,e,x,k):
#     if vectornorm(abs(val1-val2))<e:
#         return "x-convergence. solution vector = %s . k=%s . e=%s"%(x, k,e)

#find a good x initial vector
def create_good_inital_x_vector(A,b,n):
    l=[]
    for i in range(50):
        x=np.random.randint(-100, 100, size=(n)) #create an initial vector of size n
        l.append([residual(b,A,x),x])
    best=l[0]
    for item in l:
        if item[0]<best[0]:
            best=item[1]
    return best

#try out different values of w
def solve_axb_with_best_w(val, col, rowstart, b, n, maxits, w, x, A, tol):
    l=[]
    #if the user inputed any of these:
    if w == 1.2 or w == 1.3 or w == 1.2:
        w = 1.2
        solved1 = solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol)
        w = 1.3
        solved2 = solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol)
        if solved1[3]<solved2[3]:
            best = solved1
        else:
            best = solved2
        w =1.4
        solved3 = solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol)
        if solved3[3]<best[3]:
            return solved3
        else:
            return best
    else:
    #if the user inputed something other than 1.2, 1.3 or 1.4
        solved1 = solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol)
        w = 1.2
        solved2 = solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol)
        if solved1[3]<solved2[3]:
            best = solved1
        else:
            best = solved2
        w = 1.3
        solved3 = solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol)
        if solved3[3] < best[3]:
            best = solved3
        w = 1.4
        solved4 = solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol)
        if solved4[3]<best[3]:
            return solved4
        else:
            return best


def solve_axb(val, col, rowstart, b, n, maxits, w, x, A, tol):

    k = 0
    l=[]
    e = np.finfo(float).eps
    val= val.astype(float)
    col = col.astype(float)
    rowstart = rowstart.astype(float)
    b = b.astype(float)
    x= x.astype(float)
    A=A.astype(float)
    x = create_good_inital_x_vector(A, b, n) #override the given x vector, this can be taken out of the solve_axb function
    #and can be used to create x in the first place?
    while k <= maxits:
        x1=x.tolist()
        x1= np.array(x1) #store x(k)th vector in x1
        for i in range(0, n):
            sum1 = 0
            for j in range(int(rowstart[i]), int(rowstart[i+1])):
                sum1=sum1+val[j] *x[int(col[j])]
                if col[j] == i:  # identify and store diagonal entry
                    d = val[j]
            x[i] = x[i] + w * (b[i] - sum1) / d
        x2=x.tolist()
        x2=np.array(x2) #store x(k-1)th vector in x2
        r=residual(b,A,x)
        l.append(vectornorm(abs(x1 - x2)))

        #  return solution_vector_x, stopping_reason, maxits, #_of_iterations, machine_epsilon, x-seq_tolerance, residual, w
        if r==0:
            return x, "Residual convergence", maxits, k+1, e, tol, r, w
            # ^^ have to return residual tolerance used..?

        elif vectornorm(abs(x1-x2)) < tol-4*e:
            #x-convergence
            return x, "x Sequence Convergence", maxits, k+1, e, tol, r, w
        #divergence
        elif k>0 and l[k]>l[k-1]:
            return x, "Divergence",  maxits, k+1, e, tol, r, w
        else:
            k += 1
            if k== maxits:
                return x, "Max Iterations Reached", maxits, k, e, tol, r, w