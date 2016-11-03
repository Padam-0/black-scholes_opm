import numpy as np
import sys
import os.path
import re

try:
    import numpy as np
    import sys
    import os.path
    import re
except ImportError as import_err:
    print(import_err)
    print("Unable to import required libraries. Please check installation of "
          "sys, numpy, os & re libraries for python 3.5")
    exit(0)


def check_CM_args(cmArgs):
    in_names = []
    while len(in_names) != 2:
        if len(cmArgs) == 1:
            question = input('Would you like to define an input and output '
                             'filename? [y/n]: ').upper()
            if question == 'Y':
                in_names.append(input("Please enter an input file name: "))
                if not check_file_exists(in_names[0]):
                    if input(
                        "I can't find that file. Would you like to try "
                        "again? [y/n]: ").upper() == 'Y':
                        continue
                    else:
                        exit(0)
                in_names.append(input("Please enter an output file name: "))
            elif question == 'N':
                if input('Is using the default file names ok? [y/n]: '
                                     '').upper() =='Y':
                    in_names.append('nas_In.out')
                    in_names.append('nas_Sor.out')
                else:
                    if input('Would you like to exit? [y/n]: ').upper() == 'Y':
                        exit("Default Exit Message")
                    else:
                        continue
            else:
                if input('Looks like an error. Would you like to try '
                                    'again? [y/n]: ').upper() =='Y':
                    continue
                else:
                    exit(0)

        elif len(cmArgs) == 2:
            in_names.append(cmArgs[1])
            in_names.append('nas_Sor.out')
        elif len(cmArgs) == 3:
            in_names.append(cmArgs[1])
            in_names.append(cmArgs[2])
        else:
            in_names = ['nas_Sor.in', 'nas_Sor.out']

    input_file = con_filename(in_names[0], 1)
    output_file = con_filename(in_names[1], 2)
    return input_file, output_file


def check_file_exists(filename):
    return os.path.isfile(filename)


def read_inputs(filename):
    # Open a file and extract data
    matrix_size = np.genfromtxt(filename, max_rows=1)

    matrix_in = np.genfromtxt(filename, skip_header=1, skip_footer=1)

    column = np.genfromtxt(filename, usecols=0)
    col_len = len(column)

    vector_b = np.genfromtxt(filename, skip_header=(col_len - 1))

    return matrix_size, matrix_in, vector_b


"""
Checks to be completed:
Check that first line is a number
If dense matrix, is the matrix size = n
Are all entries numbers
Is the row size of the matrix the same as the vector row size
"""

# -------------------
# DENSE MATRIX TESTS
# -------------------

# Check that first line is a number

def dense_input_test(matrix_size, matrix_in, vector_b):
    errors = []

    # Check that defined matrix size matches actual matrix size
    if matrix_size == len(matrix_in):
        pass
    else:
        errors.append('Defined matrix size and actual matrix size do not match.')

    # Check that matrix size is an integer
    if matrix_size%1 == 0:
        pass
    else:
        errors.append("Defined matrix size is not an integer")

    return errors


def con_to_csr(matrix, matrix_length):
    # Convert an numpy array to CSR Structure
    val = np.ndarray.flatten(matrix)
    col = []
    rowStart = []
    pos = 0
    zeros = 0
    for entry in np.nditer(matrix):
        if entry != 0:
            col.append((pos) % matrix_length)
            if pos % matrix_length == 0:
                rowStart.append(pos - zeros)
        else:
            zeros += 1
        pos += 1
    rowStart.append(len(col))

    val = [i for i in val if i != 0]
    col = np.array(col)
    rowStart = np.array(rowStart)

    return val, col, rowStart


def write_outputs(solution_vector, stopping_reason, other_information):
    pass


def matrix_det(matrix):
    # check that matrix determinant is non zero
    if np.linalg.det(matrix) != 0:
        return True
    else:
        return False


def zero_diag(val, col, rowStart):
    # Check if there are 0's on the diagonal of the input matrix

    row = 0
    tf = True
    for i in range(len(rowStart)-1):
        r = col[rowStart[i]:rowStart[i+1]]
        if row not in r:
            tf = False
        row += 1

    return tf


def diag_dominant(val, col, rowStart):
    # Check if the diagonal value is larger than the sum of all
    # other entries in that row/column

    diags = []
    col_sums = []
    row_sums = []
    for i in range(len(rowStart) - 1):
        # 0 through 2
        r = col[rowStart[i]:rowStart[i + 1]]

        if i in r:
            diags.append(val[rowStart[i] + int(np.where(r == i)[0])])

        c_sum = 0
        for j in range(len(col)):
            if col[j] == i:
                c_sum += val[j]
        col_sums.append(c_sum)

        row_sums.append(sum(val[rowStart[i]:rowStart[i + 1]]))

    diags = np.asarray(diags)
    col_sums = np.array(col_sums) - diags
    row_sums = np.array(row_sums) - diags

    if np.greater(diags, col_sums).all() and np.greater(diags,row_sums).all():
        return True
    else:
        return False

def con_filename(filename, argNum = 0):
    # Takes a filename and reformats it to be in correct input style
    if os.path.join('a', 'b') == 'a/b':  # Checks if OS is Mac/Unix, which uses
        #  the '/' character in directory paths
        # os is unix
        c = filename.count('/')  # Counts number of '/' characters in the string
        if c != 0:
            # If '/' characters are present, replaces all but the last of
            # these. Then finds the index of the last '/'
            i = filename.replace('/', '|', c - 1).find('/')
            # Strips all information prior to and including the last '/',
            # leaving only the filename without a path.
            nf = filename[i + 1:]
        else:
            # If no '/' characters are found, filename is left unchanged
            nf = filename
    else:
        # os is windows
        c = filename.count('\\')  # Counts number of '\' characters
        if c != 0:
            # If '\' characters are present, replaces all but the last of
            # these. Then finds the index of the last '\'
            i = filename.replace('\\', '|', c - 1).find('\\')
            # Strips all information prior to and including the last '\',
            # leaving only the filename without a path
            nf = filename[i + 1:]
        else:
            # If no '\' characters are found, filename is left unchanged
            nf = filename

    pattern = re.compile(r'\..+$')  # Compile a Regular Expression (Regex)
    # pattern to identify the '.' character, followed by one or more other
    # characters at the end of a string
    if re.search(pattern, nf) != None:
        # If the pattern returns a result, find the length of the match
        a = len(re.findall(pattern, nf)[0])
        nf = nf[:-a]  # Remove the file extension from the end of the filename
    if argNum == 1:
        nf += '.in'  # Replace the file extension with '.in'
    elif argNum == 2:
        nf += '.out'  # Replace the file extension with '.out'
    return os.path.join('.', nf)  # Return the extension in the form
    # '../filename.txt'. On windows, will be '..\filename.txt'